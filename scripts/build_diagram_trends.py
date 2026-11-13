#!/usr/bin/env python3
"""Draw the CHEM U03 periodic-trend arrows figure (S3.6), and the drawing primitives the other
U03 figures share (scripts/build_diagram_u03_slides.py imports them).

Hand-built, not generated, for the same reason as build_diagram_nuclear_notation.py: both
figures carry labels and numbers a student reads as science.

    python3 scripts/build_diagram_trends.py
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(REPO, "templates", "slide", "assets")
SCALE = 4
W, H = 900 * SCALE, 536 * SCALE


def tokens():
    t = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
    g = t["ground"]
    return (g["white"]["hex"], g["asphalt"]["hex"], g["graphite"]["hex"],
            g["ruleHairline"]["hex"], t["courses"]["chemistry"]["primaryDeep"]["hex"])


def font(name, px):
    return ImageFont.truetype(os.path.join(REPO, "brand", "fonts", name), int(px * SCALE))


def s(v):
    return int(v * SCALE)


def arrow(d, a, b, col, width=5, head=18):
    d.line([a, b], fill=col, width=s(width))
    (x1, y1), (x2, y2) = a, b
    if x1 == x2:   # vertical, pointing down
        d.polygon([(x2 - s(head) // 2 - s(4), y2 - s(head)), (x2 + s(head) // 2 + s(4), y2 - s(head)),
                   (x2, y2 + s(4))], fill=col)
    else:          # horizontal, pointing right
        d.polygon([(x2 - s(head), y2 - s(head) // 2 - s(4)), (x2 - s(head), y2 + s(head) // 2 + s(4)),
                   (x2 + s(4), y2)], fill=col)


def trend_arrows():
    # Text inside a figure is read from a seat, so it obeys the 16pt floor once placed:
    # the 08 diagram slot is 5.05 in wide, so 16pt is about 40 of these 900 base px.
    # That is why the words live on the slide's annotations and the figure carries only two labels.
    white, asphalt, graphite, hair, accent = tokens()
    im = Image.new("RGB", (W, H), white)
    d = ImageDraw.Draw(im)
    f_lab = font("Archivo-Bold.ttf", 42)

    x0, y0, c = s(175), s(150), s(37)
    def present(col, row):
        if row == 0:
            return col in (0, 17)
        if col in (0, 1):
            return True
        if 2 <= col <= 11:
            return row >= 3
        return row >= 1
    for row in range(7):
        for col in range(18):
            if present(col, row):
                box = [x0 + col * c, y0 + row * c, x0 + (col + 1) * c - s(4), y0 + (row + 1) * c - s(4)]
                fill = None
                if (col, row) == (16, 1):
                    fill = accent       # fluorine: the green corner
                elif (col, row) == (0, 5):
                    fill = asphalt      # cesium: the black corner
                d.rectangle(box, outline=graphite, width=s(1.5), fill=fill)

    right = x0 + 18 * c
    ay = y0 - s(34)
    arrow(d, (x0, ay), (right - s(8), ay), accent, width=7, head=24)
    d.text((x0, ay - s(18)), "ACROSS", font=f_lab, fill=asphalt, anchor="ls")
    ax = x0 - s(40)
    arrow(d, (ax, y0), (ax, y0 + 7 * c - s(8)), asphalt, width=7, head=24)
    label = "DOWN"
    tw = int(d.textlength(label, font=f_lab)) + s(4)
    tmp = Image.new("RGBA", (tw, s(52)), (0, 0, 0, 0))
    ImageDraw.Draw(tmp).text((0, s(26)), label, font=f_lab, fill=asphalt, anchor="lm")
    tmp = tmp.rotate(90, expand=True)
    im.paste(tmp, (ax - s(70), y0), tmp)

    out = os.path.join(ASSETS, "chem_u03_s3.6_trend_arrows.png")
    im.save(out)
    print(f"wrote {os.path.relpath(out, REPO)}  {im.width}x{im.height}")


if __name__ == "__main__":
    trend_arrows()
    sys.exit(0)
