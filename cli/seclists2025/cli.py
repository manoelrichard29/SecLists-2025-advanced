#!/usr/bin/env python3
import argparse
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def cmd_list(args):
    base = os.path.join(ROOT, 'packs', args.tier)
    for dirpath, _, filenames in os.walk(base):
        for name in filenames:
            print(os.path.relpath(os.path.join(dirpath, name), ROOT))

def cmd_filter(args):
    src = os.path.join(ROOT, args.path)
    term = args.contains
    with open(src, 'r', encoding='utf-8', errors='replace') as f:
        for ln in f:
            if term in ln:
                sys.stdout.write(ln)

def main():
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest='cmd', required=True)
    p_list = sp.add_parser('list')
    p_list.add_argument('--tier', choices=['compact', 'balanced', 'full'], default='compact')
    p_list.set_defaults(func=cmd_list)

    p_filter = sp.add_parser('filter')
    p_filter.add_argument('path')
    p_filter.add_argument('--contains', required=True)
    p_filter.set_defaults(func=cmd_filter)

    args = p.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()


