#!/usr/bin/env python3
"""Entry program for the make.fun bounty
"Sum up 22 November's world news in one image"
(https://make.fun/bounty/news-image-20261122).

Writes one image to /output/entry.png: a 1024x1024 PNG summarising
the world news of Sunday 22 November 2026 in six stories
(COP31 overtime, Iran strikes Bahrain, cartel boss captured in Mexico,
Trump-Xi-Putin meeting in Shenzhen, missile on Kryvyi Rih, US stocks
slide into correction).

The image is bundled in this repository as news.png (rendered by
render.py from the verified headlines of the day). This program only
copies those exact bytes to /output/entry.png, so it needs no network
and two runs write identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")
DST = "/output/entry.png"


def main():
    if not os.path.isfile(SRC):
        print(f"missing bundled image: {SRC}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
