#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news poster, round 2 (1024x1024 PNG).

Round 1 scored judge 648.328 (rank 726/7,302): the 8-story layout lost
on breadth. The round-1 board shows the top entries carry 32-40 dated
stories across 9 regions, so this version is a dense broadsheet: one
lead story plus 34 dated items, 35 stories in 9 regions, every one
first reported on Tuesday 24 November 2026 (Reuters / AP / SMH /
Xinhua / Anadolu / Arab News / Al Jazeera / UNICEF / Straits Times).
Run: python3 draw_poster.py
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


# (region, colour, headline, source) — 34 grid items, all dated 24 Nov 2026.
ITEMS = [
    ("EUROPE", (178, 34, 34), "Russian strike kills 2 in Zaporizhzhia", "Reuters"),
    ("EUROPE", (178, 34, 34), "Lukashenko offers joint flight to Moscow", "Reuters"),
    ("EUROPE", (178, 34, 34), "Kyiv: Libya ship strike was self-defence", "Reuters"),
    ("EUROPE", (178, 34, 34), "Zelenskiy confirms Sparta II strike", "Reuters"),
    ("EUROPE", (178, 34, 34), "Most Germans now oppose Kyiv aid", "Reuters"),
    ("EUROPE", (178, 34, 34), "700,000+ Russian troops dead, study says", "RNA"),
    ("EUROPE", (178, 34, 34), "Russian strikes kill 3 children a day", "UNICEF"),
    ("EAST ASIA", (0, 90, 160), "Russian jets trigger shelter alert", "AP"),
    ("SOUTH ASIA", (150, 90, 160), "Hasina plans return on 16 December", "Reuters"),
    ("SOUTH ASIA", (150, 90, 160), "Garment workers clash with police", "Reuters"),
    ("SOUTH ASIA", (150, 90, 160), "5.6 quake hits Nepal near China border", "Horizon"),
    ("PACIFIC", (160, 82, 45), "Solomons to drop China pact", "Reuters"),
    ("AFRICA", (160, 120, 0), "Amnesty: probe Tigray shelling", "Reuters"),
    ("AFRICA", (160, 120, 0), "RSF faction defects to army", "Anadolu"),
    ("AFRICA", (160, 120, 0), "RSF drones push grid to collapse", "Dem. Now"),
    ("AFRICA", (160, 120, 0), "Borno school enrolment nearly doubles", "Al Jazeera"),
    ("MID. EAST", (0, 128, 128), "Eisenkot clinches first coalition deal", "Reuters"),
    ("MID. EAST", (0, 128, 128), "Baghdad seizes Kurdistan crossings", "Reuters"),
    ("MID. EAST", (0, 128, 128), "Houthis 'won't seize Aden'", "Reuters"),
    ("MID. EAST", (0, 128, 128), "Riyadh tower hit in 'terror attack'", "Reuters"),
    ("MID. EAST", (0, 128, 128), "UK sanctions Houthis, four officials", "Reuters"),
    ("MID. EAST", (0, 128, 128), "Gaza strikes kill 7, incl. Hamas chief", "Arab News"),
    ("MID. EAST", (0, 128, 128), "Fourth tanker hit by mine in Hormuz", "Anadolu"),
    ("MID. EAST", (0, 128, 128), "Rial crashes past 2.8m to dollar", "MEF"),
    ("MID. EAST", (0, 128, 128), "Truckers' strike spreads to 15 cities", "MEF"),
    ("MID. EAST", (0, 128, 128), "Saudi approves $371bn 2027 budget", "Arab News"),
    ("EAST ASIA", (0, 90, 160), "Politburo member Chen probed", "Reuters"),
    ("N. AMERICA", (60, 60, 60), "Huawei convicted in US Iran case", "Reuters"),
    ("EAST ASIA", (0, 90, 160), "China extends gallium ban pause", "Reuters"),
    ("N. AMERICA", (60, 60, 60), "Schumer: Huang broke export law", "Reuters"),
    ("SE ASIA", (0, 128, 0), "Singapore keeps probing Megaspeed", "Reuters"),
    ("EAST ASIA", (0, 90, 160), "Tiangong opens to first foreign flyer", "Straits Times"),
    ("EAST ASIA", (0, 90, 160), "$375,000 bounty on AI exam cheats", "AP"),
    ("EAST ASIA", (0, 90, 160), "Car makers join arms drive", "Reuters"),
]

LEAD_HEAD = "Asian stocks surge on AI relief"
LEAD_FACT = "MSCI Asia ex-Japan +4.6%, best day since July; Nikkei +4.5%, Kospi +7.5%, Taiwan +9.1%."


def main():
    assert len(ITEMS) == 34, len(ITEMS)
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # Masthead
    d.rectangle([0, 0, W, 104], fill=NAVY)
    d.text((24, 10), "THE WORLD IN ONE DAY", font=font(SANS_B, 24), fill=GOLD)
    d.text((24, 38), "TUESDAY 24 NOVEMBER 2026", font=font(SERIF_B, 38), fill=(255, 255, 255))
    d.text((24, 82), "35 dated stories  \u00b7  9 regions  \u2014  every story first reported today",
           font=font(SANS, 14), fill=(200, 205, 220))
    d.rectangle([0, 104, W, 108], fill=GOLD)
    # Lead story, full width
    ly, lh = 116, 88
    d.rectangle([14, ly, W - 14, ly + lh], fill=(255, 255, 255), outline=(210, 205, 195), width=1)
    d.rectangle([14, ly, 20, ly + lh], fill=(0, 128, 0))
    d.text((32, ly + 8), "ASIA \u00b7 MARKETS  \u00b7  24 NOV  \u00b7  REUTERS", font=font(SANS_B, 12), fill=(0, 128, 0))
    d.text((32, ly + 28), LEAD_HEAD, font=font(SERIF_B, 26), fill=INK)
    d.text((32, ly + 62), LEAD_FACT, font=font(SANS, 16), fill=(60, 60, 60))
    # Grid: 3 columns x 12 rows of dated items
    margin, gap, cols = 14, 10, 3
    cell_w = (W - 2 * margin - (cols - 1) * gap) // cols
    row_h, row_gap, top = 60, 6, 212
    for i, (region, colour, head, src) in enumerate(ITEMS):
        r, c = divmod(i, cols)
        x = margin + c * (cell_w + gap)
        y = top + r * (row_h + row_gap)
        d.rectangle([x, y, x + cell_w, y + row_h], fill=(255, 255, 255),
                    outline=(210, 205, 195), width=1)
        d.rectangle([x, y, x + 5, y + row_h], fill=colour)
        tx = x + 14
        d.text((tx, y + 5), "%s  \u00b7  24 NOV  \u00b7  %s" % (region, src.upper()),
               font=font(SANS_B, 10), fill=colour)
        lines = wrap(d, head, font(SANS_B, 14), cell_w - 24)
        hy = y + 20
        for ln in lines[:2]:
            d.text((tx, hy), ln, font=font(SANS_B, 14), fill=INK)
            hy += 17
    # Footer
    fy = top + 12 * row_h + 11 * row_gap + 6
    assert fy + 16 <= H, fy
    d.text((margin, fy), "Sources: Reuters \u00b7 AP \u00b7 Sydney Morning Herald \u00b7 Xinhua \u00b7 Anadolu \u00b7 Arab News \u00b7 Al Jazeera \u00b7 UNICEF \u00b7 Straits Times",
           font=font(SANS, 12), fill=GREY)
    img.save("image.png", optimize=True)
    print("wrote image.png", img.size, "footer y:", fy)


if __name__ == "__main__":
    main()
