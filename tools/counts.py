#!/usr/bin/env python3
"""
Generate counts.csv with file, total lines, unique non-empty lines, and sha256.
Also write side-by-side unique files as <name>.unique.txt in-place.
"""
import hashlib
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def process_file(path: str):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()
    lines = [ln for ln in text.split('\n') if ln and not ln.startswith('#')]
    unique = sorted(set(lines))
    uniq_text = '\n'.join(unique) + ('\n' if unique else '')
    base, ext = os.path.splitext(path)
    unique_path = base + '.unique' + ext
    with open(unique_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(uniq_text)
    return len(lines), len(unique), sha256_text(text)

def main():
    rows = ["path,lines,unique,sha256"]
    for dirpath, _, filenames in os.walk(ROOT):
        for name in filenames:
            if name.endswith(('.png', '.jpg', '.gif', '.zip', '.gz', '.tar')):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, ROOT)
            try:
                l, u, h = process_file(path)
            except Exception:
                continue
            rows.append(f"{rel},{l},{u},{h}")
    out = os.path.join(ROOT, 'counts.csv')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(rows) + '\n')
    print('Wrote counts.csv with', len(rows) - 1, 'entries')

if __name__ == '__main__':
    main()


