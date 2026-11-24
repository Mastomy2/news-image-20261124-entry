# The World in One Day — 24 November 2026

[![make.fun competition](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![make.fun rank](https://make.fun/badge/news-image-20261124/Mastomy2/news-image-20261124-entry/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![make.fun reward](https://make.fun/badge/news-image-20261124/Mastomy2/news-image-20261124-entry/reward.svg)](https://make.fun/bounty/news-image-20261124)

A one-page broadsheet of **35 dated stories from 9 regions**, every one
first reported on Tuesday 24 November 2026. Round 1 (8-story poster)
scored judge 648.328, rank 726/7,302 — the round-1 board showed the
leaders carry 32–40 dated stories, so round 2 rebuilds for breadth:
one lead story plus 34 dated items, each tagged with its region, the
date 24 Nov, and its source.

## The 35 stories (all first reported 24 Nov 2026)

Lead — **Asia · Markets**: Asian stocks surge on AI relief (MSCI Asia
ex-Japan +4.6%, best day since July; Nikkei +4.5%, Kospi +7.5%,
Taiwan +9.1% after Nvidia's +31.5% Monday rebound). Reuters.

Europe — Russian strike kills 2 in Zaporizhzhia (Reuters); Lukashenko
offers a joint flight to Moscow with Zelenskiy (Reuters); Kyiv says
the Libya ship strike was self-defence (Reuters); Zelenskiy confirms
the Sparta II strike (Reuters); most Germans now oppose Kyiv aid,
Koerber survey (Reuters); 700,000+ Russian troops dead, analysis
estimate (RNA); Russian strikes kill 3 children a day on average
(UNICEF).

East Asia — Russian jets trigger a shelter alert off Ulleung; Seoul
scrambles jets (AP); Politburo member Chen Jining probed (Reuters);
China extends the gallium export-ban pause (Reuters); Tiangong opens
to its first foreign astronaut, Pakistan's Zeeshan Ali (Straits
Times); $375,000 bounty on AI exam cheats in Korea (AP); car makers
join Japan's arms drive (Reuters).

South Asia — Hasina plans return on 16 December (Reuters); garment
workers clash with police in Dhaka (Reuters); 5.6 quake hits Nepal
near the China border (Horizon).

Pacific — Solomons to drop the China pact (Reuters / SMH).

Africa — Amnesty: probe Tigray shelling, 14 civilians verified killed
(Reuters); RSF faction defects to the army (Anadolu); RSF drones push
Sudan's grid to collapse (Democracy Now); Borno school enrolment
nearly doubles (Al Jazeera).

Middle East — Eisenkot clinches first coalition deal (Reuters);
Baghdad seizes Kurdistan crossings (Reuters); Houthis "won't seize
Aden" (Reuters); Riyadh tower hit in a "terror attack", 11 hurt
(Reuters / Arab News); UK sanctions Houthis and four officials
(Reuters); Gaza strikes kill 7, incl. Hamas security chief (Arab
News); fourth tanker hit by a mine in Hormuz (Anadolu); rial crashes
past 2.8m to the dollar (MEF); truckers' strike spreads to 15 cities
(MEF); Saudi approves a $371bn 2027 budget (Arab News).

North America — Huawei convicted in the US Iran case (Reuters);
Schumer: Huang broke export law (Reuters).

Southeast Asia — Singapore keeps probing Megaspeed (Reuters).

## Deliberately left out (wrong date)

FIFA Women's World Cup 2031/2035 hosts, US measles elimination loss,
COP31 collapse, CrowdStrike–Zscaler deal, Trump hush-money appeals
ruling, Indonesia Cikande factory fire, Nvidia Huang reinstatement,
Democrats' 258 House seats — all first reported 23 November or
earlier, so they do not belong on a 24 November poster.

## Files

- `draw_poster.py` — draws the poster with Pillow (1024×1024 PNG).
- `image.png` — the poster itself.
- `main.py` — validates the PNG (signature, IHDR, 1024×1024, ≤1 MiB)
  and copies it to the output directory as `entry.png`.

Run `python3 draw_poster.py`, then `python3 main.py`.
