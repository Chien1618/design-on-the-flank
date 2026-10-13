#!/usr/bin/env python3
"""Build user downloads from the canonical skill. Uses only Python's stdlib."""
import hashlib
import json
import re
import zipfile
from pathlib import Path

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
    body = source.split("---", 2)[2].strip()
    body = re.sub(r"\[([^\]]+)\]\((?:references|assets)/[^)]+\)", r"\1 (included below)", body)
    sections = [f"# Design on the Flank — Knowledge\n\nVersion: {version}\n\n"
                "Instructions and supporting material for creating Framer components.\n\n" + body]
    for path in sorted((SKILL / "references").glob("*.md")):
        sections.append(path.read_text().strip())
    example = (SKILL / "assets" / "FlankCard.tsx").read_text()
    sections.append("# Complete structural example: FlankCard.tsx\n\n```tsx\n" + example + "```\n")
    sections.append((ROOT / "LICENSE.md").read_text().strip())
    return {
        "design-on-the-flank-knowledge.txt": "\n\n---\n\n".join(sections).encode() + b"\n",
        "chatgpt-instructions.txt": (f"Design on the Flank — version {version}\n\n" +
                                     (ROOT / "adapters" / "chatgpt-instructions.txt").read_text()).encode(),
        "FlankCard.tsx": example.encode(),
    }


def zip_entries():
    entries = {}
    for path in sorted(SKILL.rglob("*")):
        if path.is_file() and path.name != ".DS_Store":
            if path.is_symlink():
                raise ValueError(f"Do not distribute symlinks: {path}")
            entries["design-on-the-flank/" + path.relative_to(SKILL).as_posix()] = path.read_bytes()
    entries["design-on-the-flank/LICENSE.md"] = (ROOT / "LICENSE.md").read_bytes()
    return entries


def main():
    OUT.mkdir(exist_ok=True)
    for name, content in artifacts().items():
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
