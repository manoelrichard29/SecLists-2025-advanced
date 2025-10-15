#!/usr/bin/env python3
"""
Normalize all lists to UTF-8 LF, strip BOM/CR, trim whitespace, remove duplicates.
Writes changes in place and prints a manifest summary.
"""
import hashlib
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def read_binary(path):
    with open(path, 'rb') as f:
        return f.read()

def write_text(path, text):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def normalize_text(b):
    text = b.decode('utf-8', errors='replace')
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    lines = [ln.strip() for ln in text.split('\n')]
    # drop empty lines unless comment
    cleaned = []
    seen = set()
    for ln in lines:
        if ln.startswith('#'):
            cleaned.append(ln)
            continue
        if not ln:
            continue
        if ln in seen:
            continue
        seen.add(ln)
        cleaned.append(ln)
    return '\n'.join(cleaned).rstrip() + '\n'

def iter_repo_files():
    for dirpath, _, filenames in os.walk(ROOT):
        for name in filenames:
            if name.endswith(('.png', '.jpg', '.gif')):
                continue
            path = os.path.join(dirpath, name)
            yield path

def main():
    manifest_rows = ["path,lines,sha256"]
    for path in iter_repo_files():
        rel = os.path.relpath(path, ROOT)
        raw = read_binary(path)
        before = sha256_bytes(raw)
        try:
            normalized = normalize_text(raw)
        except Exception:
            # Binary or non-text: skip normalization
            h = before
            lines = 0
        else:
            write_text(path, normalized)
            h = sha256_bytes(normalized.encode('utf-8'))
            lines = normalized.count('\n')
        manifest_rows.append(f"{rel},{lines},{h}")
    manifest = '\n'.join(manifest_rows) + '\n'
    write_text(os.path.join(ROOT, 'MANIFEST.csv'), manifest)
    print('Updated MANIFEST.csv with', len(manifest_rows) - 1, 'entries')

if __name__ == '__main__':
    sys.exit(main())


