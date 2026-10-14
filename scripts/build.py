#!/usr/bin/env python3
"""Build user downloads from the canonical skill. Uses only Python's stdlib."""
import hashlib
import json
import posixpath
import re
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "design-on-the-flank"
OUT = ROOT / "downloads"


def artifacts():
    version = (ROOT / "VERSION").read_text().strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("VERSION must be a semantic version such as 0.1.0")
    source = (SKILL / "SKILL.md").read_text()
    if f'version: "{version}"' not in source:
        raise ValueError("SKILL.md metadata.version must match VERSION")
    base = "https://raw.githubusercontent.com/Chien1618/design-on-the-flank/main/"
    def public_links(text, directory):
        def replace(match):
            label, target = match.groups()
            if target.startswith(("https://", "http://", "#", "mailto:")):
                return match.group(0)
            return f"[{label}]({base}{posixpath.normpath(directory + '/' + target)})"
        return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace, text)
    skill_path = "skills/design-on-the-flank"
    body = public_links(source.split("---", 2)[2].strip(), skill_path)
    catalog = public_links((SKILL / "references/catalog.md").read_text(), skill_path + "/references")
    manifest = json.loads((SKILL / "source-manifest.json").read_text())
    fallback = ["# If links cannot be opened", "",
                "Ask for only the needed module download below. The user can download and attach it. "
                "Do not request the entire library. Each module contains its topic text and common integration rules.", ""]
    results = {}
    common = "\n\n".join((SKILL / "references" / name).read_text() for name in
                          ("framer-contract.md", "advanced-integration.md", "updates-and-effects.md", "verification.md"))
    for item in manifest["sources"]:
        name = "modules/" + item["module"] + ".txt"
        fallback.append(f"- {item['module']}: {base}downloads/{name}")
        excerpts = []
        for topic in item["topics"]:
            text = (SKILL / topic["path"]).read_text()
            content = text.split("<!-- BEGIN SOURCE CONTENT -->\n", 1)[1].split("\n<!-- END SOURCE CONTENT -->", 1)[0]
            excerpts.append(public_links(content, skill_path + "/" + str(PurePosixPath(topic['path']).parent)))
        license_name = "gsap-skills-MIT.txt" if item["module"].startswith("gsap-") else "framerlabs-MIT.txt"
        license_text = (SKILL / "licenses" / license_name).read_text()
        results[name] = (f"# Design on the Flank {version} — {item['module']}\n\n"
                         "Selected module for a chat without link access. Use the Framer rules before adapting source examples. "
                         "Deliver complete code and say what was actually tested.\n\n" + common + "\n\n# Source topics\n\n" +
                         ''.join(excerpts) + "\n\n# Upstream license\n\n" + license_text).encode()
    entry = (f"# Design on the Flank — Start here\n\nVersion: {version}\n\n"
             "This is an entry guide and topic directory, not the full library. Read only the references needed for the request. "
             "If link access fails, use the named fallback module downloads below. Never say a linked file was read unless opened.\n\n" +
             body + "\n\n" + catalog + "\n\n" + "\n".join(fallback) + "\n")
    results["design-on-the-flank-knowledge.txt"] = entry.encode()
    results["chatgpt-instructions.txt"] = (f"Design on the Flank — version {version}\n\n" +
                                           (ROOT / "adapters/chatgpt-instructions.txt").read_text()).encode()
    return results


ZIP_FILE_LIMIT = 200  # Claude rejects skill uploads with more files than this
LIBRARY = SKILL / "references" / "library"
LIBRARY_LINK = re.compile(r"\]\((?:\.\./([\w-]+)/)?([\w-]+)\.md(?:#[^)]*)?\)")


def bundle_module(module):
    """Merge a library module's index and topics into one file with in-page anchors."""
    def relink(text):
        def replace(match):
            other, stem = match.groups()
            target = f"{other}.md" if other and other != module.name else ""
            anchor = "" if stem == "index" else f"#{stem}"
            return f"]({target}{anchor or ('' if target else '#top')})"
        return LIBRARY_LINK.sub(replace, text)
    parts = ['<a id="top"></a>\n\n' + relink((module / "index.md").read_text()).rstrip()]
    for path in sorted(module.glob("[0-9]*.md")):
        body = path.read_text().replace("[Topic index](index.md)\n", "", 1)
        parts.append(f'<a id="{path.stem}"></a>\n\n' + relink(body).strip())
    return ("\n\n---\n\n".join(parts) + "\n").encode()


def zip_entries():
    entries = {}
    for path in sorted(SKILL.rglob("*")):
        if path.is_file() and path.name != ".DS_Store" and LIBRARY not in path.parents:
            if path.is_symlink():
                raise ValueError(f"Do not distribute symlinks: {path}")
            content = path.read_bytes()
            if path.suffix == ".md":
                content = re.sub(r"library/([\w-]+)/index\.md", r"library/\1.md", content.decode()).encode()
            entries["design-on-the-flank/" + path.relative_to(SKILL).as_posix()] = content
    for module in sorted(p for p in LIBRARY.iterdir() if p.is_dir()):
        entries[f"design-on-the-flank/references/library/{module.name}.md"] = bundle_module(module)
    if len(entries) + 1 > ZIP_FILE_LIMIT:
        raise ValueError(f"Skill ZIP would contain {len(entries) + 1} files; Claude accepts at most {ZIP_FILE_LIMIT}")
    entries["design-on-the-flank/LICENSE.md"] = (ROOT / "LICENSE.md").read_text().replace(
        "skills/design-on-the-flank/ATTRIBUTION.md", "ATTRIBUTION.md").encode()
    return entries


def main():
    OUT.mkdir(exist_ok=True)
    for name, content in artifacts().items():
        (OUT / name).parent.mkdir(parents=True, exist_ok=True)
        (OUT / name).write_bytes(content)
    with zipfile.ZipFile(OUT / "design-on-the-flank-skill.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(zip_entries().items()):
            info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, content)
    names = sorted([*artifacts(), "design-on-the-flank-skill.zip"])
    manifest = {
        "version": (ROOT / "VERSION").read_text().strip(),
        "files": {name: {"bytes": (OUT / name).stat().st_size,
                          "sha256": hashlib.sha256((OUT / name).read_bytes()).hexdigest()}
                  for name in names},
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Built {len(names)} download files for {manifest['version']}.")


if __name__ == "__main__":
    main()
