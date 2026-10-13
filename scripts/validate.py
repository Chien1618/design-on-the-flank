#!/usr/bin/env python3
"""Check distribution integrity and local documentation links, without network."""
import hashlib
import json
import re
import zipfile
from urllib.parse import unquote

from build import ROOT, OUT, SKILL, artifacts, zip_entries


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
    for path in list(SKILL.rglob("*.md")) + list(OUT.glob("*.txt")):
        if any(token in path.read_text() for token in ("/Users/", "/private/tmp", "framer-preview/node_modules")):
            errors.append(f"Private workspace dependency in {path.relative_to(ROOT)}")
    if errors:
        raise SystemExit("\n".join(errors))
    print("PASS: generated files match source; ZIP integrity/content, version, hashes, local links, and portability checks.")


if __name__ == "__main__":
    main()
