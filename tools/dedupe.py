#!/usr/bin/env python3
"""
Create a mirrored unique/ tree with de-duplicated, comment-stripped entries.
Preserves relative paths; skips binary files.
"""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'unique')

def ensure_dir(p):
    os.makedirs(p, exist_ok=True)

def process(src, dst):
    with open(src, 'r', encoding='utf-8', errors='replace') as f:
        lines = [ln.strip() for ln in f.read().split('\n')]
    entries = [ln for ln in lines if ln and not ln.startswith('#')]
    unique = sorted(set(entries))
    ensure_dir(os.path.dirname(dst))
    with open(dst, 'w', encoding='utf-8', newline='\n') as f:
        if unique:
            f.write('\n'.join(unique) + '\n')

def main():
    for dirpath, _, filenames in os.walk(ROOT):
        for name in filenames:
            if any(name.endswith(ext) for ext in ('.png', '.jpg', '.gif', '.zip', '.tar', '.gz')):
                continue
            src = os.path.join(dirpath, name)
            rel = os.path.relpath(src, ROOT)
            if rel.startswith('unique' + os.sep) or rel.startswith('tools' + os.sep) or rel.startswith('.github' + os.sep):
                continue
            dst = os.path.join(OUT, rel)
            process(src, dst)
    print('unique/ tree generated')

if __name__ == '__main__':
    main()


