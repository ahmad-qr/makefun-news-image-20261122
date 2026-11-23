#!/usr/bin/env python3
"""Render the infographic for make.fun bounty news-image-20261122.

Draws 'THE WORLD TODAY — WORLD NEWS, Sunday 22 November 2026' as a
1024x1024 PNG with six news panels. Run:  python3 render.py
Writes news.png next to this file.
"""

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (13, 27, 46)          # deep navy
HEADER_BG = (10, 20, 36)
PANEL_BG = (255, 255, 255)
PANEL_EDGE = (210, 216, 224)
INK = (16, 32, 54)
MUTED = (96, 110, 128)
ACCENTS = [
    (0, 150, 136),   # teal
    (198, 40, 40),   # red
    (230, 126, 34),  # orange
    (41, 98, 168),   # blue
    (106, 27, 154),  # purple
    (46, 125, 50),   # green
]

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 76)
F_SUB = font("DejaVuSans.ttf", 30)
F_KICKER = font("DejaVuSans-Bold.ttf", 24)
F_HEAD = font("DejaVuSans-Bold.ttf", 30)
F_BODY = font("DejaVuSans.ttf", 24)
F_FOOT = font("DejaVuSans.ttf", 22)

NEWS = [
    ("01  CLIMATE",
     "COP31 talks deadlock in Antalya",
     "Negotiators miss the deadline as climate talks stall over finance and fossil-fuel wording."),
    ("02  MIDDLE EAST",
     "Iran strikes sites in Bahrain",
     "Missiles hit targets in Bahrain as regional tensions flare across the Gulf."),
    ("03  MEXICO",
     "\u201cEl Chapo Isidro\u201d arrested",
     "Mexican forces capture the cartel boss in a major blow to organised crime."),
    ("04  DIPLOMACY",
     "Trump, Xi and Putin meet in Shenzhen",
     "A rare three-way summit as the three leaders gather for talks in China."),
    ("05  UKRAINE",
     "Russian missiles hit Kryvyi Rih",
     "Strikes damage homes and power lines in the Ukrainian city of Kryvyi Rih."),
    ("06  MARKETS",
     "US stocks slide into correction",
     "Wall Street falls as an AI sell-off deepens and investors rush for safety."),
]


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_panel(draw, x, y, w, h, accent, kicker, headline, body):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=18,
                           fill=PANEL_BG, outline=PANEL_EDGE, width=2)
    # accent bar on top
    draw.rounded_rectangle([x, y, x + w, y + 10], radius=5, fill=accent)
    cx, cy = x + 22, y + 26
    draw.text((cx, cy), kicker, font=F_KICKER, fill=accent)
    cy += 36
    for line in wrap(draw, headline, F_HEAD, w - 44):
        draw.text((cx, cy), line, font=F_HEAD, fill=INK)
        cy += 36
    cy += 6
    for line in wrap(draw, body, F_BODY, w - 44):
        draw.text((cx, cy), line, font=F_BODY, fill=MUTED)
        cy += 31


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Header
    draw.rectangle([0, 0, W, 168], fill=HEADER_BG)
    draw.rectangle([0, 168, W, 174], fill=(255, 193, 7))
    draw.text((36, 28), "THE WORLD TODAY", font=F_TITLE, fill=(255, 255, 255))
    draw.text((36, 116), "WORLD NEWS  ·  Sunday 22 November 2026",
              font=F_SUB, fill=(180, 196, 214))

    # Grid of six panels: 2 columns x 3 rows
    margin = 36
    gap = 20
    top = 196
    bottom = 962
    pw = (W - 2 * margin - gap) // 2
    ph = (bottom - top - 2 * gap) // 3
    for i, (kicker, headline, body) in enumerate(NEWS):
        col, row = i % 2, i // 2
        x = margin + col * (pw + gap)
        y = top + row * (ph + gap)
        draw_panel(draw, x, y, pw, ph, ACCENTS[i], kicker, headline, body)

    # Footer
    draw.text((36, 978), "Six stories that defined the day  ·  make.fun",
              font=F_FOOT, fill=(140, 158, 178))

    out = Path(__file__).resolve().parent / "news.png"
    img.save(out, format="PNG", optimize=True)
    print(f"Wrote {out} ({out.stat().st_size} bytes, {img.size})")


if __name__ == "__main__":
    main()
