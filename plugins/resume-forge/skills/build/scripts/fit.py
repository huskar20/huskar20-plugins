#!/usr/bin/env python3
"""Measure resume lines against the real Calibri that Google Docs renders.

Google Docs serves Calibri from fonts.gstatic.com to every document, so the
font is always available to the finished resume whether or not it is installed
on anyone's machine. This script fetches that exact font and measures against
it, which is why its numbers are authoritative and hand estimates are not.

Two jobs:

  pad   how many &nbsp; put a right-hand date as close to flush as possible
  wrap  which lines are too long and will spill onto a second line

Usage
-----
    python3 fit.py pad  "Job Title, Company - (City, ST)" "Mon Year - Present"
    python3 fit.py wrap "Bullet text without the glyph"
    python3 fit.py selftest

Options
-------
    --col PT     text column width in points. Default 468 (6.5in, which is what
                 Google Docs' HTML import actually produces). Pass 504 for a
                 7.0in column after the margins have been fixed by hand.
    --size PT    font size, default 11.
    --indent PT  left indent for wrap checks, default 20.2 (the 0.28in bullet).

Needs fontTools and network access on first run; the font is cached next to
this script. If either is unavailable, fall back to the estimate table in
references/drive-formatting.md and say that estimates were used.
"""

import argparse
import os
import sys
import urllib.request

CSS = "https://themes.googleusercontent.com/fonts/css?kit=fpjTOVmNbO4Lz34iLyptLUXza5VhXqVC6o75Eld_V98"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".fontcache")
UA = {"User-Agent": "Mozilla/5.0"}
# A run of nbsp is the only way to push a date rightward through HTML import,
# so undershoot deliberately: a slightly-left date is cosmetic, a wrapped one
# costs a whole line.
SAFETY = 2


def _fetch(url, path):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
            data = r.read()
        with open(path, "wb") as fh:
            fh.write(data)
    return path


def load():
    """Return (regular_width_fn, bold_width_fn, space_pt_at_1pt)."""
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        sys.exit("fontTools not installed. Use the estimate table in "
                 "references/drive-formatting.md and say estimates were used.")

    css = _fetch(CSS, os.path.join(CACHE, "calibri.css"))
    with open(css, encoding="utf-8") as fh:
        body = fh.read()
    urls = [ln.split("url(")[1].split(")")[0]
            for ln in body.splitlines() if "url(" in ln]
    if len(urls) < 2:
        sys.exit("Could not find both Calibri faces in Google's CSS.")

    faces = []
    for name, url in (("regular", urls[0]), ("bold", urls[1])):
        font = TTFont(_fetch(url, os.path.join(CACHE, f"calibri-{name}.ttf")))
        upm = font["head"].unitsPerEm
        hmtx, cmap = font["hmtx"], font.getBestCmap()

        def width(text, _u=upm, _h=hmtx, _c=cmap):
            return sum(_h[_c[ord(ch)]][0] for ch in text if ord(ch) in _c) / _u

        faces.append(width)
    return faces[0], faces[1], faces[0](" ")


def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("mode", choices=["pad", "wrap", "selftest"])
    ap.add_argument("text", nargs="*")
    ap.add_argument("--col", type=float, default=468.0)
    ap.add_argument("--size", type=float, default=11.0)
    ap.add_argument("--indent", type=float, default=20.2)
    a = ap.parse_args()

    reg, bold, space_em = load()
    space = space_em * a.size

    if a.mode == "selftest":
        print(f"space   {space_em:.4f} em = {space:.3f} pt at {a.size:g}pt")
        sample = (
            "Architect an agentic LLM ensemble extracting context across 1 billion points."
            "Hold enrichment at 98% precision, cutting defect rate from 35% to 4.5%."
            "Built and maintained Flask AI applications, moving deep learning into production."
            "Productionized a predictive maintenance model built on PhasedLSTM deep learning."
            "Delivered end-to-end machine learning projects for 12 startup clients."
        )
        avg = reg(sample) * a.size / len(sample)
        print(f"avg char {avg / a.size:.4f} em = {avg:.2f} pt (measured on resume prose)")
        print(f"column  {a.col:.0f} pt -> {a.col / avg:.0f} chars, "
              f"detail line {(a.col - a.indent) / avg:.0f} chars")
        return

    if a.mode == "pad":
        if len(a.text) != 2:
            sys.exit('pad needs exactly two arguments: "left text" "right date"')
        left, right = a.text
        gap = a.col - bold(left) * a.size - reg(right) * a.size
        n = int(gap / space) - SAFETY
        if n < 1:
            print(f"0   line is already {-gap:.0f}pt too wide - shorten it, it will wrap")
        else:
            print(f"{n}   (gap {gap:.0f}pt, leaves the date ~{gap - n * space:.0f}pt short of flush)")
        return

    for s in a.text:
        w = reg(s) * a.size
        room = a.col - a.indent
        print(f"{'WRAPS' if w > room else 'fits '}  {w:6.1f}pt / {room:.1f}pt  "
              f"({len(s)} chars)  {s[:52]}")


if __name__ == "__main__":
    main()
