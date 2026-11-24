#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news poster (1024x1024 PNG).

Newspaper-style poster: a navy masthead naming the day, then eight
numbered stories in a two-by-four grid. Every story below was first
reported on Tuesday 24 November 2026 (Reuters / AP / Sydney Morning
Herald reporting that day); the one dated claim in each card is the
figure the source reported that day. Run: python3 draw_poster.py
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (250, 248, 243)
NAVY = (20, 33, 61)
GOLD = (201, 162, 39)
INK = (24, 24, 24)
GREY = (110, 110, 110)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width, using PIL textlength."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


STORIES = [
    ("MARKETS \u00b7 ASIA", (0, 128, 0),
     "Asian stocks surge on AI relief",
     "MSCI Asia ex-Japan jumps 4.6%, its best day since July; Nikkei +4.5%, Kospi +7.5%, Taiwan +9.1% after Nvidia's 31.5% Monday rebound.",
     "Reuters"),
    ("UKRAINE \u00b7 ZAPORIZHZHIA", (178, 34, 34),
     "Russian strike kills 2 overnight",
     "An overnight attack kills 2 and wounds 22, including two children, in Zaporizhzhia, officials say on Tuesday.",
     "Reuters"),
    ("KOREA \u00b7 ULLEUNG ISLAND", (0, 90, 160),
     "Russian jets trigger shelter alert",
     "Seoul scrambles jets as Russian planes enter its air defence zone; Ulleung island's shelter warning is lifted within minutes. No airspace violation.",
     "AP \u00b7 Reuters"),
    ("BANGLADESH \u00b7 DHAKA", (150, 90, 160),
     "Hasina plans return on 16 December",
     "Ousted PM Sheikh Hasina plans to fly home from exile in India on 16 December, her spokesperson tells Reuters on Tuesday.",
     "Reuters"),
    ("PACIFIC \u00b7 HONIARA", (160, 82, 45),
     "Solomons to drop China pact",
     "The Solomon Islands tells Beijing it will end its 2022 China security pact and sign a new treaty with Australia instead.",
     "Reuters \u00b7 SMH"),
    ("ETHIOPIA \u00b7 TIGRAY", (160, 120, 0),
     "Amnesty: probe Tigray shelling",
     "Amnesty says shelling of Alamata should be investigated as possible war crimes; it verified 14 civilians killed there.",
     "Reuters"),
    ("SINGAPORE \u00b7 TECH", (60, 60, 60),
     "Singapore keeps probing Megaspeed",
     "PM Wong says Singapore will keep investigating Nvidia-linked Megaspeed, blacklisted by the US over alleged AI-chip diversion to China.",
     "Reuters"),
    ("JAPAN \u00b7 TOKYO", (0, 128, 128),
     "Car parts makers join arms drive",
     "Japan draws auto suppliers into its biggest military buildup since WWII; one firm's motors now power Anduril drones.",
     "Reuters"),
]


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # Masthead
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.text((28, 16), "THE WORLD IN ONE DAY", font=font(SANS_B, 26), fill=GOLD)
    d.text((28, 48), "TUESDAY 24 NOVEMBER 2026", font=font(SERIF_B, 46), fill=(255, 255, 255))
    d.text((28, 108), "Eight stories that defined the day \u2014 from Seoul to Honiara, Kyiv to Singapore",
           font=font(SANS, 19), fill=(200, 205, 220))
    d.rectangle([0, 148, W, 154], fill=GOLD)
    # Grid: 2 columns x 4 rows
    margin, gap = 16, 12
    cell_w = (W - 2 * margin - gap) // 2
    cell_h = 190
    top = 164
    for i, (tag, colour, head, body, src) in enumerate(STORIES):
        r, c = divmod(i, 2)
        x = margin + c * (cell_w + gap)
        y = top + r * (cell_h + gap)
        d.rectangle([x, y, x + cell_w, y + cell_h], fill=(255, 255, 255),
                    outline=(210, 205, 195), width=1)
        d.rectangle([x, y, x + 6, y + cell_h], fill=colour)
        # Number badge
        cx, cy = x + cell_w - 26, y + 22
        d.ellipse([cx - 15, cy - 15, cx + 15, cy + 15], fill=colour)
        d.text((cx, cy), str(i + 1), font=font(SANS_B, 18), fill=(255, 255, 255), anchor="mm")
        tx = x + 18
        d.text((tx, y + 10), tag, font=font(SANS_B, 15), fill=colour)
        lines = wrap(d, head, font(SERIF_B, 25), cell_w - 56)
        hy = y + 34
        for ln in lines[:2]:
            d.text((tx, hy), ln, font=font(SERIF_B, 25), fill=INK)
            hy += 30
        blines = wrap(d, body, font(SANS, 18), cell_w - 36)
        by = hy + 6
        for ln in blines[:3]:
            d.text((tx, by), ln, font=font(SANS, 18), fill=(60, 60, 60))
            by += 23
        d.text((tx, y + cell_h - 26), "Source: " + src, font=font(SANS, 14), fill=GREY)
    # Footer
    fy = top + 4 * cell_h + 3 * gap + 8
    d.text((margin, fy), "Sources: Reuters \u00b7 AP \u00b7 Sydney Morning Herald",
           font=font(SANS, 14), fill=GREY)
    d.text((margin, fy + 20), "All stories are events of Tuesday 24 November 2026, or first reported that day.",
           font=font(SANS, 14), fill=GREY)
    img.save("image.png", optimize=True)
    print("wrote image.png", img.size)


if __name__ == "__main__":
    main()
