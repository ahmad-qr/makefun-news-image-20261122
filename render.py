#!/usr/bin/env python3
"""Render the news infographic for the make.fun bounty
"Sum up 22 November's world news in one image" (news-image-20261122).

Generates news.png (1024x1024, the image the entry program copies).
Run once:  python3 render.py
News content verified from headlines published Sunday 22 Nov 2026
(OneTurn world briefing, AP/WPXI world wire, The Daily Edition, Inshorts).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (12, 27, 42)          # deep navy
PANEL = (18, 38, 58)       # slightly lighter navy
GOLD = (212, 175, 55)
WHITE = (245, 247, 250)
MUTED = (168, 184, 200)
DARK = (10, 22, 34)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


STORIES = [
    ("CLIMATE", (46, 160, 110),
     "COP31 talks run into overtime",
     "Climate summit in Antalya deadlocks over fossil fuels."),
    ("MIDDLE EAST", (178, 80, 72),
     "Iran strikes Bahrain site",
     "Bahrain says an industrial site was hit; tankers targeted in Hormuz."),
    ("MEXICO", (122, 90, 168),
     "Cartel boss \u2018El Chapo Isidro\u2019 captured",
     "Mexican forces arrest Fausto Isidro Meza Flores in Sinaloa; 11 killed."),
    ("DIPLOMACY", (52, 110, 180),
     "Trump, Xi and Putin meet in Shenzhen",
     "The three leaders agree to begin talks on reducing nuclear risks."),
    ("UKRAINE", (186, 140, 40),
     "Missile hits Zelenskyy\u2019s hometown",
     "Russian strike on Kryvyi Rih kills two; Ukraine hits a Russian ship."),
    ("MARKETS", (40, 148, 140),
     "US stocks slide into correction",
     "An AI share sell-off drags the Dow and S&P 500 into correction."),
]

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---- header ----
d.rectangle([0, 0, W, 200], fill=DARK)
d.rectangle([0, 200, W, 206], fill=GOLD)
f_kicker = font(FONT_BOLD, 28)
f_title = font(FONT_BOLD, 88)
f_date = font(FONT_REG, 28)
d.text((48, 30), "THE WORLD TODAY", font=f_kicker, fill=GOLD)
d.text((48, 66), "WORLD NEWS", font=f_title, fill=WHITE)
d.text((48, 162), "SUNDAY  \u2022  22 NOVEMBER 2026", font=f_date, fill=MUTED)

# ---- story rows (one-line summary, auto-shrunk to fit inside the panel) ----
f_chip = font(FONT_BOLD, 23)
f_head = font(FONT_BOLD, 33)
y = 222
ROW_H = 120
PANEL_H = 112
for i, (cat, color, head, summ) in enumerate(STORIES):
    # panel
    d.rounded_rectangle([36, y, W - 36, y + PANEL_H], radius=14, fill=PANEL)
    # category chip
    chip_w = int(d.textlength(cat, font=f_chip)) + 26
    d.rounded_rectangle([54, y + 12, 54 + chip_w, y + 44], radius=9, fill=color)
    d.text((54 + 13, y + 16), cat, font=f_chip, fill=WHITE)
    # headline (one line, shrink if needed)
    hx, hw = 54, W - 54 - 54
    f = f_head
    while d.textlength(head, font=f) > hw and f.size > 26:
        f = font(FONT_BOLD, f.size - 2)
    d.text((hx, y + 48), head, font=f, fill=WHITE)
    # summary: single line, shrink font until it fits
    f_s = font(FONT_REG, 25)
    while d.textlength(summ, font=f_s) > hw and f_s.size > 19:
        f_s = font(FONT_REG, f_s.size - 1)
    d.text((hx, y + 48 + f.size + 6), summ, font=f_s, fill=MUTED)
    y += ROW_H

# ---- footer ----
fy = H - 52
d.rectangle([36, fy - 16, W - 36, fy - 14], fill=(60, 80, 100))
f_foot = font(FONT_REG, 24)
foot = "Six stories that defined the day  \u2022  22 November 2026"
fw = d.textlength(foot, font=f_foot)
d.text(((W - fw) / 2, fy), foot, font=f_foot, fill=MUTED)

img.save("news.png", optimize=True)
print("saved news.png", img.size)
