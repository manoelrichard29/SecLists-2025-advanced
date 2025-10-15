#!/usr/bin/env python3
"""
Stub generator for frequency metadata. Produces metadata.csv with columns:
path,entry,seen_count,rank,source

Current implementation assigns seen_count=1, rank=NA, source=unknown.
Replace with real corpus aggregation when sources are available.
"""
import csv
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def iter_entries():
    for dirpath, _, filenames in os.walk(ROOT):
        for name in filenames:
            if any(name.endswith(ext) for ext in ('.png', '.jpg', '.gif', '.zip', '.tar', '.gz', '.lock')):
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), ROOT)
            if rel.startswith(('tools/', '.github/', 'packs/', 'unique/')):
                continue
            with open(os.path.join(ROOT, rel), 'r', encoding='utf-8', errors='replace') as f:
                for ln in f.read().split('\n'):
                    if ln and not ln.startswith('#'):
                        yield rel, ln

def main():
    out = os.path.join(ROOT, 'metadata.csv')
    with open(out, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['path', 'entry', 'seen_count', 'rank', 'source'])
        for path, entry in iter_entries():
            w.writerow([path, entry, 1, 'NA', 'unknown'])
    print('Wrote metadata.csv (stub)')

if __name__ == '__main__':
    main()


