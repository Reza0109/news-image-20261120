#!/usr/bin/env python3
"""Render entry.png: a five-story infographic of Friday 20 November 2026.

Deterministic: fixed DejaVu fonts, fixed colours, no timestamps, no
randomness, no network. Run: python3 draw.py  (writes entry.png here)
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 48

BG = (11, 22, 38)
CARD = (22, 38, 58)
INK = (255, 255, 255)
BODY = (198, 209, 219)
MUTED = (128, 143, 158)
ORANGE = (245, 166, 35)

ACCENTS = [
    (245, 166, 35),   # 1 orange
    (46, 204, 113),   # 2 green
    (155, 89, 182),   # 3 purple
    (231, 76, 60),    # 4 red
    (52, 152, 219),   # 5 blue
]

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def load_font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except OSError:
        return ImageFont.load_default()


def wrap_text(draw, text, fnt, max_w):
    """Greedy word wrap by pixel width; returns a list of lines."""
    lines, cur = [], ""
    for word in text.split():
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


def fit_headline(draw, text, max_w, start=29):
    """Largest bold size (29 down to 24) that fits the headline on one line."""
    size = start
    while size > 24:
        fnt = load_font(size, bold=True)
        if draw.textlength(text, font=fnt) <= max_w:
            return fnt
        size -= 1
    return load_font(24, bold=True)


STORIES = [
    ("ICJ: Myanmar Committed Genocide of Rohingya",
     "The UN's highest court rules Myanmar committed genocide against the "
     "Rohingya in a landmark judgment."),
    ("Houthis Strike Four Targets in Saudi Arabia",
     "Four strikes hit Riyadh's financial centre, King Khalid airport, "
     "Jubail's Sadaf plant and Khamis Mushait base; a landmark is damaged."),
    ("Anthropic Debuts on Nasdaq at $111.50",
     "Shares opened 34% above the $83 IPO price, briefly hit a $2 trillion "
     "value, and closed at $97.17. The $81.3B IPO is the largest ever."),
    ("GTA VI: 24.58M Sold, $2.3B+ Revenue (Est.)",
     "Sensor Tower estimates 24.58 million units sold and over $2.3 billion "
     "in revenue. Take-Two has not released official figures."),
    ("Trump: No Rush on Iran War Decision Until 2027",
     "Trump says he is in no hurry on Iran, delaying any decision to 2027: "
     "\u201csee what happens after Jan 1,\u201d Reuters reports."),
]


def draw_card(draw, y, idx, headline, body, card_w):
    """Draw one story card at vertical offset y; return its height."""
    accent = ACCENTS[idx]
    body_f = load_font(22)
    text_x = MARGIN + 26 + 56 + 18
    text_w = MARGIN + card_w - 16 - text_x
    head_f = fit_headline(draw, headline, text_w)
    lines = wrap_text(draw, body, body_f, text_w)
    line_h = 28
    content_h = 36 + 8 + len(lines) * line_h
    card_h = content_h + 32

    x0, x1 = MARGIN, MARGIN + card_w
    draw.rounded_rectangle([x0, y, x1, y + card_h], radius=14, fill=CARD)
    draw.rectangle([x0 + 2, y + 10, x0 + 10, y + card_h - 10], fill=accent)

    cx, cy = x0 + 26 + 28, y + card_h // 2
    draw.ellipse([cx - 28, cy - 28, cx + 28, cy + 28], fill=accent)
    num = str(idx + 1)
    num_f = load_font(30, bold=True)
    nw = draw.textlength(num, font=num_f)
    nh = num_f.getbbox(num)[3]
    draw.text((cx - nw / 2, cy - nh / 2 - 2), num, fill=INK, font=num_f)

    ty = y + 16
    draw.text((text_x, ty), headline, fill=INK, font=head_f)
    ty += 36 + 8
    for line in lines:
        draw.text((text_x, ty), line, fill=BODY, font=body_f)
        ty += line_h
    return card_h


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    card_w = W - 2 * MARGIN

    y = 40
    d.text((MARGIN, y), "FRIDAY, 20 NOVEMBER 2026", fill=ORANGE,
           font=load_font(32, bold=True))
    y += 50
    d.text((MARGIN, y), "World News in One Image", fill=INK,
           font=load_font(58, bold=True))
    y += 76
    d.rectangle([MARGIN, y, W - MARGIN, y + 5], fill=ORANGE)
    y += 24

    gap = 12
    for i, (headline, body) in enumerate(STORIES):
        card_h = draw_card(d, y, i, headline, body, card_w)
        y += card_h + gap

    footer = "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 AFP \u2014 20 November 2026"
    foot_f = load_font(20)
    fw = d.textlength(footer, font=foot_f)
    d.text(((W - fw) / 2, H - 44), footer, fill=MUTED, font=foot_f)

    assert y <= H - 56, "cards overflow the page: %d" % y
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, format="PNG")
    print("wrote %s (%dx%d, %d bytes)" % (out, W, H, os.path.getsize(out)))


if __name__ == "__main__":
    main()
