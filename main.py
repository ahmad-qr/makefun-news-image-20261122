#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261122.

Copies the pre-rendered infographic news.png to /output/entry.png.
No network access, no randomness: every run writes identical bytes.
Run:  python3 main.py
"""

import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    src = HERE / "news.png"
    dst = Path("/output/entry.png")
    if not src.is_file():
        fail(f"source image missing: {src}")
    if src.stat().st_size == 0:
        fail(f"source image is empty: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    if not dst.is_file() or dst.stat().st_size == 0:
        fail(f"output was not written: {dst}")
    if dst.stat().st_size != src.stat().st_size:
        fail(
            f"output size {dst.stat().st_size} does not match "
            f"source size {src.stat().st_size}"
        )
    print(f"Wrote {dst} ({dst.stat().st_size} bytes, "
          f"sha256 {sha256_of(dst)})")


if __name__ == "__main__":
    main()
