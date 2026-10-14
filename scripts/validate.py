#!/usr/bin/env python3
"""Check distribution integrity and local documentation links, without network."""
import hashlib
import json
import posixpath
import re
import zipfile
from urllib.parse import unquote

from build import ROOT, OUT, SKILL, artifacts, zip_entries
from import_library import BEGIN, END, sha


def main():
    errors = []
    for name, content in artifacts().items():
        if not (OUT / name).exists() or (OUT / name).read_bytes() != content:
            errors.append(f"Missing or stale generated file: {name}")
    archive_path = OUT / "design-on-the-flank-skill.zip"
    try:
        with zipfile.ZipFile(archive_path) as archive:
            if archive.testzip() is not None:
                errors.append("ZIP integrity check failed")
            actual = {name: archive.read(name) for name in archive.namelist()}
            if actual != zip_entries():
                errors.append("ZIP contents differ from canonical source")
            if len(archive.namelist()) != len(actual):
                errors.append("ZIP has duplicate names")
            for name, content in actual.items():
                if not name.endswith(".md"):
                    continue
                text = content.decode()
                for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", text):
                    if target.startswith(("https://", "http://", "mailto:")):
                        continue
                    path, _, anchor = target.partition("#")
                    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(path))) if path else name
                    if resolved not in actual:
                        errors.append(f"Broken ZIP link: {name} -> {target}")
                    elif anchor and resolved.startswith("design-on-the-flank/references/library/") and \
                            f'<a id="{anchor}"></a>' not in actual[resolved].decode():
                        errors.append(f"Broken ZIP anchor: {name} -> {target}")
    except (FileNotFoundError, zipfile.BadZipFile) as exc:
        errors.append(str(exc))
    try:
        manifest = json.loads((OUT / "manifest.json").read_text())
        expected_names = {*artifacts(), "design-on-the-flank-skill.zip"}
        if set(manifest["files"]) != expected_names:
            errors.append("Manifest file list differs from expected downloads")
        if manifest["version"] != (ROOT / "VERSION").read_text().strip():
            errors.append("Manifest version mismatch")
        for name, entry in manifest["files"].items():
            if name not in expected_names:
                continue
            content = (OUT / name).read_bytes()
            if entry != {"bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()}:
                errors.append(f"Manifest integrity mismatch: {name}")
    except (FileNotFoundError, KeyError, ValueError) as exc:
        errors.append(f"Manifest error: {exc}")
    source_manifest = json.loads((SKILL / "source-manifest.json").read_text())
    sources = source_manifest["sources"]
    if len(sources) != 26 or sum(s["source"].endswith("/SKILL.md") for s in sources) != 20:
        errors.append("Expected 20 source skills plus six reference documents")
    expected_gsap = {"gsap-" + name for name in ("core", "timeline", "scrolltrigger", "plugins", "utils", "react", "performance", "frameworks")}
    if {s["module"] for s in sources if s["module"].startswith("gsap-")} != expected_gsap:
        errors.append("Official GSAP skill coverage mismatch")
    catalog = (SKILL / "references/catalog.md").read_text()
    tracked = set()
    for item in sources:
        if "ui-ux-pro-max" in item["source"]:
            errors.append("Excluded source present in library")
        index_path = SKILL / item["index"]
        index = index_path.read_text()
        tracked.add(index_path)
        if item["index"].removeprefix("references/") not in catalog:
            errors.append("Unrouted module: " + item["module"])
        body = []
        for topic in item["topics"]:
            path = SKILL / topic["path"]
            tracked.add(path)
            payload = path.read_text().split(BEGIN, 1)[1].split(END, 1)[0]
            body.append(payload)
            if sha(payload.encode()) != topic["sha256"] or len(payload.splitlines()) != topic["lines"]:
                errors.append("Topic integrity mismatch: " + topic["path"])
            if path.name not in index:
                errors.append("Unlinked topic: " + topic["path"])
            fence = None
            for line in payload.splitlines():
                mark = re.match(r"^\s*(`{3,}|~{3,})", line)
                if mark:
                    value = mark.group(1)
                    if fence is None:
                        fence = (value[0], len(value))
                    elif value[0] == fence[0] and len(value) >= fence[1]:
                        fence = None
            if fence is not None:
                errors.append("Split or unclosed code fence: " + topic["path"])
        if sha(''.join(body).encode()) != item["adapted_sha256"]:
            errors.append("Reconstructed source mismatch: " + item["source"])
    if tracked != {p for p in (SKILL / "references/library").rglob("*") if p.is_file()}:
        errors.append("Library files differ from manifest")
    for name in ("framerlabs-MIT.txt", "gsap-skills-MIT.txt"):
        if "Permission is hereby granted" not in (SKILL / "licenses" / name).read_text():
            errors.append("Missing upstream MIT notice: " + name)
    if (SKILL / "SKILL.md").stat().st_size > 12000 or (OUT / "design-on-the-flank-knowledge.txt").stat().st_size > 25000:
        errors.append("Entry guide is too large; keep details in topics")
    actual_downloads = {p.relative_to(OUT).as_posix() for p in OUT.rglob("*") if p.is_file()}
    if actual_downloads != {*artifacts(), "design-on-the-flank-skill.zip", "manifest.json"}:
        errors.append("Unexpected or stale download files")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        source = path.read_text()
        for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", source):
            if target.startswith(("https://", "http://", "#", "mailto:")):
                continue
            target = unquote(target.split("#")[0])
            if not (path.parent / target).exists():
                errors.append(f"Broken local link: {path.relative_to(ROOT)} -> {target}")
    for path in list(SKILL.rglob("*.md")) + list(OUT.rglob("*.txt")):
        if any(token in path.read_text() for token in ("/Users/", "/private/tmp", "framer-preview/node_modules")):
            errors.append(f"Private workspace dependency in {path.relative_to(ROOT)}")
    if errors:
        raise SystemExit("\n".join(errors))
    print("PASS: 20 skills + 6 references; all 8 GSAP modules; topic reconstruction, fences, routes, MIT notices, downloads, ZIP, hashes, links and portability.")


if __name__ == "__main__":
    main()
