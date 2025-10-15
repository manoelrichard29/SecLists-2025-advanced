#!/usr/bin/env python3
"""
Validate lists for formatting rules: UTF-8, LF newlines, no carriage returns,
no trailing spaces, no tabs, reasonable line length, and uniqueness.
"""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def validate_file(path):
    errors = []
    with open(path, 'rb') as f:
        data = f.read()
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        errors.append('not UTF-8')
        return errors
    if '\r' in text:
        errors.append('contains CR characters')
    lines = text.split('\n')
    seen = set()
    for idx, ln in enumerate(lines, 1):
        if ln.endswith(' '):
            errors.append(f'line {idx}: trailing space')
        if '\t' in ln:
            errors.append(f'line {idx}: contains tab')
        if len(ln) > 2000:
            errors.append(f'line {idx}: excessively long line')
        if ln and not ln.startswith('#'):
            if ln in seen:
                errors.append(f'line {idx}: duplicate entry')
            else:
                seen.add(ln)
    return errors

def main():
    failures = 0
    for dirpath, _, filenames in os.walk(ROOT):
        for name in filenames:
            if name.endswith(('.png', '.jpg', '.gif')):
                continue
            path = os.path.join(dirpath, name)
            errs = validate_file(path)
            if errs:
                failures += 1
                print(f'FAIL {os.path.relpath(path, ROOT)}:')
                for e in errs:
                    print('  -', e)
    if failures:
        print(f'Total files with issues: {failures}')
        return 1
    print('All files passed validation')
    return 0

if __name__ == '__main__':
    sys.exit(main())


