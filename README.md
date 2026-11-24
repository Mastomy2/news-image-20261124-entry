# The World in One Day — 24 November 2026

[![make.fun competition](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![make.fun rank](https://make.fun/badge/news-image-20261124/Mastomy2/news-image-20261124-entry/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![make.fun reward](https://make.fun/badge/news-image-20261124/Mastomy2/news-image-20261124-entry/reward.svg)](https://make.fun/bounty/news-image-20261124)

A newspaper-style poster covering eight stories that happened or were
first reported on Tuesday, 24 November 2026 — one day, eight stories
from around the world. The poster is a 1024x1024 PNG with a navy
masthead and a two-column grid of short, sourced summaries, each with
a coloured tag and a number badge.

Every story on this poster was verified as happening or first reported
on Tuesday 24 November 2026. Stories from Monday 23 November — the
COP31 collapse, the Nvidia CEO reinstatement, the CrowdStrike–Zscaler
deal, the Trump hush-money ruling and the FIFA World Cup host awards —
were deliberately left out.

## The eight stories

1. **Markets / Asia (lead)** — Asian stocks surge on Tuesday: MSCI Asia ex-Japan +4.6%, its best day since July; Nikkei +4.5%, Kospi +7.5%, Taiwan +9.1%, after Nvidia's 31.5% rebound on Monday. *Reuters*
2. **Ukraine / Zaporizhzhia** — A Russian attack overnight kills 2 and wounds 22, including two children, in Zaporizhzhia, officials say on Tuesday. *Reuters*
3. **Korea / Ulleung Island** — Seoul scrambles jets as Russian planes enter its air defence zone; the island's shelter warning is lifted within minutes. No airspace violation. *AP / Reuters*
4. **Bangladesh / Dhaka** — Ousted PM Sheikh Hasina plans to return from exile in India on 16 December, her spokesperson tells Reuters on Tuesday. *Reuters*
5. **Pacific / Honiara** — The Solomon Islands tells Beijing it will end its 2022 China security pact and sign a new treaty with Australia instead. *Reuters / Sydney Morning Herald*
6. **Ethiopia / Tigray** — Amnesty International says shelling of Alamata should be investigated as possible war crimes; it verified 14 civilians killed there. *Reuters*
7. **Singapore / Tech** — PM Wong says Singapore will keep investigating Nvidia-linked Megaspeed, blacklisted by the US over alleged AI-chip diversion to China. *Reuters*
8. **Japan / Tokyo** — Japan draws auto suppliers into its biggest military buildup since WWII; one firm's motors now power Anduril drones. *Reuters*

## How to run

`main.py` (Python 3.13, standard library only, no network) validates
`image.png` — PNG signature, IHDR chunk, exactly 1024x1024, at most
1 MiB — then copies it to `entry.png` in the output directory
(`$MAKEFUN_OUTPUT_DIR`, or `/output` by default) and re-hashes the
copy to prove it is byte-identical. It prints the output path, the
SHA-256 and the size, and exits 1 on any validation failure.

```sh
python3 main.py
```

The poster itself is drawn by `draw_poster.py` (Pillow, DejaVu fonts):

```sh
python3 draw_poster.py
```
