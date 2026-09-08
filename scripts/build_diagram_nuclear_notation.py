#!/usr/bin/env python3
"""Draw the carbon-14 nuclear-symbol / hyphen-notation figure for CHEM U01 S1.4.

Hand-built, not generated. The standard is explicit: anything a student reads as
science - anything carrying a number, a label, or a formula - is built. A generated
"nuclear symbol" would have a plausible-looking wrong subscript and nobody would
catch it at a glance.

Colours come from brand/tokens.json. Type comes from the shipped Archivo files, the
same ones the deck embeds, so the figure and the slide around it are one typeface.

    python3 scripts/build_diagram_nuclear_notation.py
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "templates", "slide", "assets",
                   "chem_u01_s1.4_nuclear_notation.png")
SCALE = 4                      # drawn large, placed small - stays crisp on a projector
W, H = 900 * SCALE, 560 * SCALE


def tokens():
    t = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
    return (t["ground"]["white"]["hex"], t["ground"]["asphalt"]["hex"],
            t["ground"]["graphite"]["hex"], t["courses"]["chemistry"]["primaryDeep"]["hex"])


def font(name, px):
    return ImageFont.truetype(os.path.join(REPO, "brand", "fonts", name), px * SCALE)


def main():
    white, asphalt, graphite, accent = tokens()
    im = Image.new("RGB", (W, H), white)
    d = ImageDraw.Draw(im)

    f_sym = font("Archivo-Bold.ttf", 132)
    f_num = font("Archivo-SemiBold.ttf", 58)
    f_lab = font("Archivo-SemiBold.ttf", 21)
    f_hyp = font("Archivo-Bold.ttf", 62)

    cx = W // 2

    # ---- nuclear symbol: 14 above 6, both left of C ----
    sym_x, sym_y = cx - 40 * SCALE, 150 * SCALE
    d.text((sym_x, sym_y), "C", font=f_sym, fill=asphalt)
    d.text((sym_x - 22 * SCALE, sym_y + 8 * SCALE), "14", font=f_num, fill=asphalt, anchor="ra")
    d.text((sym_x - 22 * SCALE, sym_y + 132 * SCALE), "6", font=f_num, fill=asphalt, anchor="rs")

    # Leader lines out to the labels, so each numeral is named rather than guessed at.
    lead = 118 * SCALE
    d.line([(sym_x - 92 * SCALE, sym_y + 22 * SCALE), (sym_x - lead, sym_y + 22 * SCALE)],
           fill=accent, width=2 * SCALE)
    d.text((sym_x - lead - 10 * SCALE, sym_y + 22 * SCALE), "MASS NUMBER",
           font=f_lab, fill=accent, anchor="rm")
    d.line([(sym_x - 62 * SCALE, sym_y + 112 * SCALE), (sym_x - lead, sym_y + 112 * SCALE)],
           fill=accent, width=2 * SCALE)
    d.text((sym_x - lead - 10 * SCALE, sym_y + 112 * SCALE), "ATOMIC NUMBER",
           font=f_lab, fill=accent, anchor="rm")

    d.line([(sym_x + 100 * SCALE, sym_y + 70 * SCALE), (sym_x + lead + 40 * SCALE, sym_y + 70 * SCALE)],
           fill=accent, width=2 * SCALE)
    d.text((sym_x + lead + 50 * SCALE, sym_y + 70 * SCALE), "ELEMENT SYMBOL",
           font=f_lab, fill=accent, anchor="lm")

    # ---- rule, then the same isotope in hyphen notation ----
    ry = 350 * SCALE
    d.line([(140 * SCALE, ry), (W - 140 * SCALE, ry)], fill=graphite, width=1 * SCALE)
    d.text((cx, ry + 26 * SCALE), "THE SAME ISOTOPE, WRITTEN THE OTHER WAY",
           font=f_lab, fill=graphite, anchor="ma")
    d.text((cx, ry + 62 * SCALE), "carbon-14", font=f_hyp, fill=asphalt, anchor="ma")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    im.save(OUT)
    print(f"wrote {os.path.relpath(OUT, REPO)}  {im.width}x{im.height}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
