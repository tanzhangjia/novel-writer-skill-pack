#!/usr/bin/env python3
"""进度查看工具"""
import os, sys, re, glob, unicodedata

BASE_DIR = os.environ.get("NOVEL_PROJECT_DIR", ".")
DRAFT_DIR = os.path.join(BASE_DIR, "草稿")

def print_status():
    files = sorted(glob.glob(os.path.join(DRAFT_DIR, "*.md")))
    total = 0
    for f in files:
        with open(f) as fh:
            cnt = sum(1 for ch in fh.read() if unicodedata.category(ch).startswith('Lo'))
        total += cnt
        name = os.path.basename(f)
        ok = "OK" if 2000 <= cnt <= 5000 else ("SHORT" if cnt < 2000 else "LONG")
        print(f"{ok}  {cnt:>5d}字  {name}")
    print(f"---\n总计: {len(files)}章, {total}字")

if __name__ == "__main__":
    print_status()
