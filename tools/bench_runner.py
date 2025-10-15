#!/usr/bin/env python3
"""
Run simple benchmarks against the sandbox/vulnapi for redir and xss endpoints.
Outputs bench_results.json with minimal stats.
"""
import json
import time
import urllib.parse
import urllib.request

def try_url(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            return resp.getcode()
    except Exception:
        return None

def run():
    base = 'http://127.0.0.1:8080'
    payloads = [
        '/xss?q=' + urllib.parse.quote('<img src=x onerror=1>'),
        '/redir?url=' + urllib.parse.quote('//example.com'),
    ]
    results = []
    start = time.time()
    for p in payloads:
        code = try_url(base + p)
        results.append({'path': p, 'code': code})
    elapsed = time.time() - start
    with open('bench_results.json', 'w') as f:
        json.dump({'elapsed_sec': elapsed, 'results': results}, f, indent=2)
    print('Wrote bench_results.json')

if __name__ == '__main__':
    run()


