# Sum up 22 November's world news in one image

Entry for the make.fun bounty **"Sum up 22 November's world news in one
image"** ($100, 50 places paid) — https://make.fun/bounty/news-image-20261122
— by [@ahmad-qr](https://github.com/ahmad-qr).

## What it is

A 1024×1024 PNG infographic, **"THE WORLD TODAY — WORLD NEWS, Sunday 22
November 2026"**, summing up the day's world news in six stories:

1. **Climate** — COP31 talks run into overtime (Antalya deadlocks over fossil fuels)
2. **Middle East** — Iran strikes Bahrain site; tankers targeted in the Strait of Hormuz
3. **Mexico** — Cartel boss 'El Chapo Isidro' captured in Sinaloa; 11 killed
4. **Diplomacy** — Trump, Xi and Putin meet in Shenzhen; nuclear risk-reduction talks agreed
5. **Ukraine** — Missile hits Zelenskyy's hometown Kryvyi Rih; 2 killed
6. **Markets** — US stocks slide into correction as AI shares sell off

Headlines were verified against news published on Sunday 22 November 2026
(OneTurn world briefing, AP world wire, The Daily Edition, Inshorts).

## How it works

- `main.py` (Python 3.13, at the repo root) writes the image to
  `/output/entry.png`. It needs **no network**: it copies the bundled
  `news.png` byte-for-byte, so two runs write identical bytes.
- `news.png` is the finished image (1024×1024, ~111 KB, under the 1 MiB limit).
- `render.py` is the generator that drew `news.png` from the headlines
  (Pillow + DejaVu fonts); it is included for transparency, it is not run
  at grading time.
- `LICENSE` is the MIT license (OSI-approved).

## Run it

```sh
python3 main.py   # writes /output/entry.png
```

## Submission checklist (for the account owner)

- [ ] Create a **public GitHub repo owned by ahmad-qr**, created after the
      competition opened (22 Nov 2026), and push these files (one commit)
- [ ] Submit the repo via the bounty page ("Submit an entry") before the
      deadline: **Tue 24 Nov 2026, 07:00 WIB** (00:00 UTC)
- [ ] Attach the AI coding-agent transcripts of the sessions that built it
- [ ] Entry must be signed with the wallet linked to @ahmad-qr on make.fun
      (needed to claim any prize; prizes are paid in USDC on Solana)
