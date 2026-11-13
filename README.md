# 13 November 2026 in one picture

An entry for the make.fun competition **news-image-01**: one image that
sums up the world's news of Friday 13 November 2026.

## The image

A clean editorial front-page collage, headed **"FRIDAY 13 NOVEMBER 2026"**,
with four panels, each a flat illustration with a big short label:

1. **EUROPE JOINS UKRAINE TALKS** — European and Ukrainian flags over a
   negotiation table. Russia agreed to European participation in the next
   round of Ukraine peace talks.
2. **NVIDIA CEO RESIGNS — SHARES −16%** — a chip with a plunging chart.
   Nvidia's chief executive resigned; the shares fell as much as 16%
   intraday before recovering part of the drop.
3. **GAZA HOSPITAL STRIKE — 6 DEAD** — a quiet hospital under a grey sky.
   A strike on the Nasser hospital complex in Khan Younis killed six
   people. Shown respectfully, with no gore.
4. **MICROSOFT 365 DOWN WORLDWIDE** — dark screens and a cracked globe.
   Microsoft's mail and Teams services failed across regions.

The four stories were re-checked against live reporting on 13 November
2026 at build time; nothing in the image is invented.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to the output directory:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

The program runs offline and writes the same bytes on every run.
`entry.png` is a 1024×1024 PNG, under 1 MiB.

## License

MIT — see `LICENSE`.
