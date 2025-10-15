#!/usr/bin/env python3
"""
Build compact/balanced/full packs for common tools from curated lists.
Outputs packs/ with categorized wordlists.
"""
import os
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'packs')

def ensure_dir(p):
    os.makedirs(p, exist_ok=True)

def copy_subset(src, dst, limit=None):
    ensure_dir(os.path.dirname(dst))
    with open(src, 'r', encoding='utf-8', errors='replace') as f:
        lines = [ln for ln in f.read().split('\n') if ln]
    if limit is not None:
        lines = lines[:limit]
    with open(dst, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + ('\n' if lines else ''))

def build():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    ensure_dir(OUT)

    tiers = {
        'compact': 1000,
        'balanced': 10000,
        'full': None,
    }

    sources = {
        'discovery/dirs': os.path.join(ROOT, 'Discovery', 'web-content-dirs-large-2025.txt'),
        'discovery/subdomains': os.path.join(ROOT, 'Discovery', 'dns-subdomains-large-2025.txt'),
        'passwords/global': os.path.join(ROOT, 'Passwords', 'passwords-top-2025.txt'),
        'passwords/fr': os.path.join(ROOT, 'Passwords', 'passwords-fr-2025.txt'),
        'fuzzing/params': os.path.join(ROOT, 'Fuzzing', 'params-common-2025.txt'),
    }

    for tier, limit in tiers.items():
        for name, src in sources.items():
            dst = os.path.join(OUT, tier, f'{name}.txt')
            copy_subset(src, dst, limit)

    print('Packs built under packs/')

if __name__ == '__main__':
    build()


