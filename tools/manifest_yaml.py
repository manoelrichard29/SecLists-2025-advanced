#!/usr/bin/env python3
"""
Generate MANIFEST.yaml with per-file metadata:
  - path, category, rows, unique_rows, sha256
  - source: unknown (placeholder), date_collected: yyyy-mm-dd (today)
"""
import datetime
import hashlib
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def categorize(rel: str) -> str:
    top = rel.split('/', 1)[0]
    return top

def file_stats(path: str):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()
    rows = [ln for ln in text.split('\n') if ln]
    unique_rows = len(set([ln for ln in rows if not ln.startswith('#')]))
    return len(rows), unique_rows, sha256_text(text)

def main():
    today = datetime.date.today().isoformat()
    items = []
    for dirpath, _, filenames in os.walk(ROOT):
        for name in filenames:
            if any(name.endswith(ext) for ext in ('.png', '.jpg', '.gif', '.zip', '.tar', '.gz', '.lock')):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, ROOT)
            if rel.startswith(('unique/', 'packs/', 'tools/', '.github/')):
                continue
            try:
                rows, uniq, h = file_stats(path)
            except Exception:
                continue
            items.append({
                'path': rel,
                'category': categorize(rel),
                'rows': rows,
                'unique_rows': uniq,
                'sha256': h,
                'source': 'unknown',
                'date_collected': today,
            })

    # naive YAML emitter
    lines = ['files:']
    for it in sorted(items, key=lambda x: x['path']):
        lines.append(f"  - path: {it['path']}")
        lines.append(f"    category: {it['category']}")
        lines.append(f"    rows: {it['rows']}")
        lines.append(f"    unique_rows: {it['unique_rows']}")
        lines.append(f"    sha256: {it['sha256']}")
        lines.append(f"    source: {it['source']}")
        lines.append(f"    date_collected: {it['date_collected']}")
    out = os.path.join(ROOT, 'MANIFEST.yaml')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    print('Wrote MANIFEST.yaml with', len(items), 'entries')

if __name__ == '__main__':
    main()


