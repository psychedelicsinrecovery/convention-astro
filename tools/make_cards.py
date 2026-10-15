#!/usr/bin/env python3
"""Regenerate the social card (og:image) and gallery preview covers.

    python3 tools/make_cards.py

Zero dependencies beyond Pillow (pip install pillow). Draws the night-sky cards
in the fellowship's palette so the images stay reproducible and editable.
Fonts are looked up per platform (macOS / Windows / Linux) with a graceful
degradation to Pillow's bundled default so the script never hard-fails.
"""
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

TM = "\u2122"
RM = "\u00ae"
TM_LINE = f"Psychedelics In Recovery{TM} \u2013 PIR{RM}"

# Cross-platform font candidates, best first.
_SERIF_B_CANDS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
    "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "/Library/Fonts/Times New Roman Bold.ttf",
    "C:/Windows/Fonts/timesbd.ttf",
]
_SERIF_CANDS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/Library/Fonts/Times New Roman.ttf",
    "C:/Windows/Fonts/times.ttf",
]
_SANS_CANDS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/Library/Fonts/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
]
_SANS_B_CANDS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
]


def _font(cands, size):
    for p in cands:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                continue
    return ImageFont.load_default()


def sky(w, h, seed, glows, stars=420):
    img = Image.new("RGB", (w, h), (0, 0, 0))
    d = ImageDraw.Draw(img)
    top, mid, bot = (11, 9, 26), (7, 6, 17), (4, 3, 10)
    for y in range(h):
        t = y / h
        if t < 0.55:
            f = t / 0.55
            c = tuple(int(top[i] + (mid[i] - top[i]) * f) for i in range(3))
        else:
            f = (t - 0.55) / 0.45
            c = tuple(int(mid[i] + (bot[i] - mid[i]) * f) for i in range(3))
        d.line([(0, y), (w, y)], fill=c)
    g = Image.new("RGB", (w, h), (0, 0, 0))
    gd = ImageDraw.Draw(g)
    for box, col in glows:
        gd.ellipse(box, fill=col)
    g = g.filter(ImageFilter.GaussianBlur(120))
    img = Image.blend(img, Image.blend(img, g, 0.55), 0.85)
    d = ImageDraw.Draw(img)
    random.seed(seed)
    for _ in range(stars):
        x, y = random.randint(0, w - 1), random.randint(0, h - 1)
        r = random.choice([0.4, 0.5, 0.6, 0.8, 1.0, 1.2])
        a = random.randint(50, 220)
        d.ellipse([x - r, y - r, x + r, y + r], fill=(a, int(a * 0.95), int(a * 0.82)))
    return img, d


def mushroom(img, d, cx, base_y, cap_r, stem_h, hue):
    w, h = img.size
    g = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(g)
    gd.ellipse(
        [cx - cap_r * 3, base_y - stem_h - cap_r * 2.4, cx + cap_r * 3, base_y + cap_r * 1.4],
        fill=hue + (70,),
    )
    g = g.filter(ImageFilter.GaussianBlur(28))
    img.paste(Image.alpha_composite(img.convert("RGBA"), g).convert("RGB"), (0, 0))
    dd = ImageDraw.Draw(img)
    sw = cap_r * 0.55
    dd.rounded_rectangle([cx - sw, base_y - stem_h, cx + sw, base_y], radius=sw * 0.8, fill=(246, 235, 214))
    dd.ellipse([cx - cap_r, base_y - stem_h - cap_r * 0.95, cx + cap_r, base_y - stem_h + cap_r * 0.5], fill=hue)
    dd.arc(
        [cx - cap_r * 0.8, base_y - stem_h - cap_r * 0.85, cx + cap_r * 0.4, base_y - stem_h + cap_r * 0.2],
        180, 320, fill=(255, 240, 210), width=3,
    )
    for dx, dy, rr in [(-0.45, -0.45, 0.09), (0.05, -0.62, 0.07), (0.5, -0.35, 0.08), (0.15, -0.2, 0.06)]:
        dd.ellipse(
            [cx + dx * cap_r - rr * cap_r, base_y - stem_h + dy * cap_r - rr * cap_r,
             cx + dx * cap_r + rr * cap_r, base_y - stem_h + dy * cap_r + rr * cap_r],
            fill=(255, 241, 214),
        )


def social_card(path):
    W, H = 1200, 630
    img, d = sky(W, H, 7, [((W * 0.45, -H * 0.5, W * 1.05, H * 0.35), (58, 42, 110)),
                           ((-W * 0.15, -H * 0.35, W * 0.35, H * 0.25), (94, 64, 30))])
    mushroom(img, d, 930, 560, 52, 58, (232, 180, 90))
    mushroom(img, d, 1020, 585, 38, 44, (167, 139, 250))
    mushroom(img, d, 860, 595, 30, 34, (232, 180, 90))
    mushroom(img, d, 1090, 600, 26, 30, (167, 139, 250))
    d.line([(760, 600), (1200, 600)], fill=(60, 50, 84), width=2)
    ser = _font(_SERIF_B_CANDS, 66)
    ser_i = _font(_SERIF_CANDS, 30)
    san = _font(_SANS_CANDS, 26)
    sanb = _font(_SANS_B_CANDS, 24)
    x0, y0 = 84, 92
    d.rectangle([x0, y0 - 4, x0 + 52, y0 + 2], fill=(232, 180, 90))
    d.text((x0, y0 + 18), "THE INAUGURAL", font=sanb, fill=(232, 180, 90))
    d.text((x0 - 4, y0 + 58), f"PIR{RM} Convention", font=ser, fill=(243, 238, 228))
    d.text((x0, y0 + 158), TM_LINE, font=san, fill=(200, 192, 175))
    d.text((x0, y0 + 200), "Denver, Colorado  \u00b7  October 8-11, 2026", font=san, fill=(200, 192, 175))
    d.text((x0, y0 + 252), "Ten years of the fellowship \u2014 gathered in person, at last.", font=ser_i, fill=(214, 205, 188))
    img.save(path, quality=92)


def gallery_cover(path):
    W, H = 1200, 800
    img, d = sky(W, H, 11, [((W * 0.55, -H * 0.3, W * 1.15, H * 0.45), (64, 46, 120)),
                            ((-W * 0.1, H * 0.2, W * 0.4, H * 0.8), (90, 60, 28))], stars=520)
    mushroom(img, d, 600, 660, 110, 120, (232, 180, 90))
    mushroom(img, d, 760, 700, 70, 80, (167, 139, 250))
    mushroom(img, d, 450, 720, 56, 64, (232, 180, 90))
    d.line([(260, 720), (1000, 720)], fill=(64, 52, 88), width=3)
    ser = _font(_SERIF_B_CANDS, 56)
    san = _font(_SANS_CANDS, 26)
    sanb = _font(_SANS_B_CANDS, 22)
    d.text((90, 120), "THE INAUGURAL", font=sanb, fill=(232, 180, 90))
    d.text((84, 152), f"PIR{RM} Convention", font=ser, fill=(243, 238, 228))
    d.text((90, 240), "Denver, Colorado \u00b7 October 8-11, 2026", font=san, fill=(200, 192, 175))
    d.text((90, 284), f"The fellowship's shared album \u00b7 {TM_LINE}", font=san, fill=(170, 162, 150))
    img.save(path, quality=90)


if __name__ == "__main__":
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pub = os.path.join(here, "public")
    social_card(os.path.join(pub, "social-card.jpg"))
    gallery_cover(os.path.join(pub, "gallery-preview.jpg"))
    print("Wrote public/social-card.jpg and public/gallery-preview.jpg")
