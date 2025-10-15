#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import os

app = FastAPI(title="SecLists-2025 API", version="v1")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

@app.get('/v1/releases')
def list_releases():
    # Stub: return current VERSION
    version_path = os.path.join(ROOT, 'VERSION')
    if not os.path.exists(version_path):
        raise HTTPException(500, 'VERSION not found')
    with open(version_path, 'r', encoding='utf-8') as f:
        v = f.read().strip()
    return {"latest": v}

@app.get('/v1/download/{tier}/{category}/{name}')
def download_pack(tier: str, category: str, name: str):
    path = os.path.join(ROOT, 'packs', tier, category, name)
    if not os.path.exists(path):
        raise HTTPException(404, 'Not found')
    return FileResponse(path)

@app.get('/v1/search')
def search(q: str, tier: str = 'compact'):
    base = os.path.join(ROOT, 'packs', tier)
    results = []
    for dirpath, _, filenames in os.walk(base):
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            with open(full, 'r', encoding='utf-8', errors='replace') as f:
                for i, ln in enumerate(f, 1):
                    if q in ln:
                        results.append({"file": os.path.relpath(full, ROOT), "line": i, "entry": ln.strip()})
                        if len(results) >= 2000:
                            return JSONResponse(results)
    return JSONResponse(results)


