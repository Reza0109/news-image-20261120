[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Reza0109/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Reza0109/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

# 20 November 2026 in One Image

My entry for the [make.fun](https://make.fun) bounty
[news-image-20261120](https://make.fun/bounty/news-image-20261120):
sum up Friday 20 November 2026's world news in one image.

## The image

`entry.png` (1024×1024) is a five-story infographic of the day:

1. **ICJ: Myanmar Committed Genocide of Rohingya** — the UN's highest court
   rules Myanmar committed genocide against the Rohingya.
2. **Houthis Strike Four Targets in Saudi Arabia** — strikes hit a Riyadh
   financial centre, King Khalid airport, the Sadaf plant in Jubail and
   Khamis Mushait airbase; a landmark in Riyadh is damaged.
3. **Anthropic Debuts on Nasdaq at $111.50** — shares opened 34% above the
   $83 IPO price, briefly hit a $2 trillion value, and closed at $97.17.
   The $81.3B IPO is the largest ever.
4. **GTA VI: 24.58M Sold, $2.3B+ Revenue (Est.)** — Sensor Tower estimates
   24.58 million units sold and over $2.3 billion in revenue; Take-Two has
   not released official figures.
5. **Trump: No Rush on Iran War Decision Until 2027** — Trump says he is in
   no hurry on Iran, delaying any decision to 2027: "see what happens after
   Jan 1," per Reuters.

## How it works

`draw.py` renders `entry.png` with PIL (deterministic: fixed fonts and
colours, no timestamps, no randomness). `main.py` (Python standard
library only) checks the image against the gate (valid PNG, at most 1 MiB,
at most 1024×1024), copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
and verifies the copy landed intact.

Run it:

```sh
python3 draw.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
