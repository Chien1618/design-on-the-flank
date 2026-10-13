#!/usr/bin/env python3
"""Split supplied handoff and an explicit GSAP checkout into on-demand references."""
import argparse
import hashlib
import json
import os
import posixpath
import re
import shutil
import subprocess
from pathlib import Path
from urllib.parse import unquote, quote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/design-on-the-flank'
LIB = SKILL / 'references/library'
BEGIN = '<!-- BEGIN SOURCE CONTENT -->\n'
END = '\n<!-- END SOURCE CONTENT -->'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def module_name(source):
    parts = source.split('/')
    name = parts[parts.index('skills') + 1]
    names = {'framer-code-components-overrides': 'framer-components', 'framer-plugins': 'framer-plugins'}
    base = names.get(name, name)
    if parts[-1] != 'SKILL.md':
        base += '-' + Path(parts[-1]).stem
    return base


def headings(text, level):
    lines = text.splitlines(keepends=True)
    starts, fence = [], None
    for i, line in enumerate(lines):
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            mark = match.group(1)
            if fence is None:
                fence = (mark[0], len(mark))
            elif mark[0] == fence[0] and len(mark) >= fence[1]:
                fence = None
            continue
        if fence is None and re.match(r'^' + '#' * level + r' ', line):
            starts.append(i)
    return lines, starts


def split_content(text, level=2):
    lines, starts = headings(text, level)
    cuts = sorted(set([0, *starts, len(lines)]))
    parts = [''.join(lines[a:b]) for a, b in zip(cuts, cuts[1:]) if a != b]
    out = []
    for part in parts:
        if len(part.splitlines()) > 150 and level < 4:
            out.extend(split_content(part, level + 1))
        else:
            out.append(part)
    assert ''.join(out) == text
    return out


def topic_title(content):
    fence = False
    for line in content.splitlines():
        if re.match(r'^\s*(```|~~~)', line):
            fence = not fence
        if not fence and re.match(r'^#{1,4} ', line):
            return line.lstrip('# ').strip()
    return 'Overview and metadata'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--handoff', required=True, type=Path)
    parser.add_argument('--gsap', required=True, type=Path)
    parser.add_argument('--framerlabs', required=True, type=Path)
    args = parser.parse_args()
    handoff = args.handoff.read_text()
    blocks = re.findall(r'<!-- BEGIN SOURCE: ([^\n]+) -->\n(.*?)\n<!-- END SOURCE: \1 -->', handoff, re.S)
    if len(blocks) != 19:
        raise ValueError(f'Expected 19 handoff sources, found {len(blocks)}; review changed input.')
    sources = {name: content.strip() + '\n' for name, content in blocks if '/ui-ux-pro-max/' not in name}
    gsap_files = sorted((args.gsap / 'skills').glob('*/SKILL.md'))
    if len(gsap_files) != 8:
        raise ValueError('GSAP upstream skill count changed; review before import.')
    for file in gsap_files:
        sources['gsap-skills/' + file.relative_to(args.gsap).as_posix()] = file.read_text().strip() + '\n'
    destinations = {name: LIB / module_name(name) / 'index.md' for name in sources}
    # This directory contains generated library references only. Refuse mixed content.
    if LIB.exists():
        tracked = {str(p) for p in LIB.rglob('*') if p.is_file()}
        known_path = SKILL / 'source-manifest.json'
        if not known_path.exists():
            raise ValueError('Existing library has no source manifest; refusing replacement.')
        known = json.loads(known_path.read_text())
        expected = {str(SKILL / p['path']) for s in known['sources'] for p in s['topics']}
        expected |= {str(SKILL / s['index']) for s in known['sources']}
        if tracked != expected:
            raise ValueError('Library contains untracked edits/files; inspect before replacement.')
        for source in known['sources']:
            for topic in source['topics']:
                data = (SKILL / topic['path']).read_text().split(BEGIN, 1)[1].split(END, 1)[0]
                if sha(data.encode()) != topic['sha256']:
                    raise ValueError('Library topic was edited; preserve edits before import.')
    manifest = {'handoff_sha256': sha(args.handoff.read_bytes()), 'excluded': ['ui-ux-pro-max'],
                'gsap_repository': 'https://github.com/greensock/gsap-skills',
                'gsap_commit': subprocess.check_output(['git', '-C', str(args.gsap), 'rev-parse', 'HEAD']).decode().strip(),
                'sources': []}
    pending = {}
    for source, original in sources.items():
        destination = destinations[source]
        def relink(match):
            label, target = match.groups()
            if target.startswith(('https://', 'http://', '#', 'mailto:')):
                return match.group(0)
            relative, sep, anchor = target.partition('#')
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(relative)))
            # The handoff's plugin API reference links SKILL.md as a sibling.
            if relative == 'SKILL.md' and '/references/' in source:
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), '../SKILL.md'))
            if resolved in destinations:
                link = os.path.relpath(destinations[resolved], destination.parent)
                return f'[{label}]({link})'
            if resolved.startswith('framerlabs/hacks/'):
                return f'[{label}](https://github.com/fredm00n/framerlabs/blob/main/{quote(resolved[len("framerlabs/"):])})'
            raise ValueError(f'Unresolved reference: {source} -> {target}')
        body = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', relink, original)
        topics = []
        index_lines = [f'# {module_name(source)}', '',
                       'Choose only the topic needed for the current request. Do not read every linked file.', '',
                       f'Source: `{source}`. Preserved reference examples; adapt them to the Framer contract.', '',
                       '| Topic | Lines |', '|---|---:|']
        for i, payload in enumerate(split_content(body), 1):
            title = topic_title(payload)
            slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:72]
            file = destination.parent / f'{i:02d}-{slug}.md'
            pending[file] = f'[Topic index](index.md)\n\nSource excerpt. Read the package Framer integration rules before adapting code.\n\n' + BEGIN + payload + END + '\n'
            topics.append({'path': file.relative_to(SKILL).as_posix(), 'title': title,
                           'lines': len(payload.splitlines()), 'sha256': sha(payload.encode())})
            index_lines.append(f'| [{title.replace("|", "/")}]({file.name}) | {len(payload.splitlines())} |')
        pending[destination] = '\n'.join(index_lines) + '\n'
        manifest['sources'].append({'source': source, 'module': module_name(source),
                                    'source_sha256': sha(original.encode()), 'adapted_sha256': sha(body.encode()),
                                    'index': destination.relative_to(SKILL).as_posix(), 'topics': topics})
    # Resolve every source/link before replacing the generated library.
    license_data = {
        'framerlabs-MIT.txt': (args.framerlabs / 'LICENSE').read_bytes(),
        'gsap-skills-MIT.txt': (args.gsap / 'LICENSE').read_bytes(),
    }
    if LIB.exists():
        shutil.rmtree(LIB)
    for file, content in pending.items():
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content)
    licenses = SKILL / 'licenses'
    licenses.mkdir(exist_ok=True)
    for name, content in license_data.items():
        (licenses / name).write_bytes(content)
    (SKILL / 'source-manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    print(f'Imported {len(sources)} source documents into {sum(len(s["topics"]) for s in manifest["sources"])} topics; UI/UX excluded.')


if __name__ == '__main__':
    main()
