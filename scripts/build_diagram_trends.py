#!/usr/bin/env python3
"""Draw the two CHEM U03 figures: the periodic-trend arrows (S3.6) and atom-vs-ion sizes (S3.7).

Hand-built, not generated, for the same reason as build_diagram_nuclear_notation.py: both
figures carry labels and numbers a student reads as science.

Ion-size circles are drawn to scale from these radii (pm): Na atom 186 (metallic),
Na+ 102 (ionic, 6-coordinate), Cl atom 99 (covalent), Cl- 181 (ionic, 6-coordinate).

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


def ion_sizes():
    white, asphalt, graphite, hair, accent = tokens()
    im = Image.new("RGB", (W, H), white)
    d = ImageDraw.Draw(im)
    f_sym = font("Archivo-Bold.ttf", 48)
    f_chg = font("Archivo-Bold.ttf", 34)
    f_lab = font("Archivo-SemiBold.ttf", 40)

    cy = s(220)
    items = [("Na", "", 186, False, 120), ("Na", "+", 102, True, 340), ("Cl", "", 99, False, 565), ("Cl", "−", 181, True, 780)]
    for sym, charge, r, ion, cx in items:
        R = s(r * 0.6)          # same pm-to-px factor for all four, so the sizes compare honestly
        box = [s(cx) - R, cy - R, s(cx) + R, cy + R]
        col = white if ion else asphalt
        if ion:
            d.ellipse(box, fill=accent)
            # Archivo has no superscript plus/minus glyphs, so the charge is set small and raised.
            # Symbol and charge are centred as one unit so the pair stays inside the circle.
            f_ion = font("Archivo-Bold.ttf", 42)
            sw, chw = d.textlength(sym, font=f_ion), d.textlength(charge, font=f_chg)
            left = s(cx) - (sw + chw + s(2)) / 2
            d.text((left, cy), sym, font=f_ion, fill=col, anchor="lm")
            d.text((left + sw + s(2), cy - s(14)), charge, font=f_chg, fill=col, anchor="lm")
        else:
            d.ellipse(box, outline=asphalt, width=s(3))
            d.text((s(cx), cy), sym, font=f_sym, fill=col, anchor="mm")
        d.text((s(cx), s(380)), f"{r} pm", font=f_lab, fill=asphalt, anchor="ma")

    arrow(d, (s(240), cy), (s(266), cy), graphite, width=4, head=14)
    arrow(d, (s(632), cy), (s(656), cy), graphite, width=4, head=14)
    d.line([(s(452), s(60)), (s(452), s(470))], fill=hair, width=s(2))

    out = os.path.join(ASSETS, "chem_u03_s3.7_ion_size.png")
    im.save(out)
    print(f"wrote {os.path.relpath(out, REPO)}  {im.width}x{im.height}")


def cells_row(d, labels, hi, y, cw, ch, x0, f, white, ink, accent, graphite, under=None, f_under=None):
    for i, lab in enumerate(labels):
        box = [x0 + i * cw, y, x0 + (i + 1) * cw - s(6), y + ch]
        on = i in hi
        d.rectangle(box, outline=graphite, width=s(2), fill=accent if on else None)
        d.text(((box[0] + box[2]) // 2, y + ch // 2), lab, font=f, fill=white if on else ink, anchor="mm")
        if under:
            d.text(((box[0] + box[2]) // 2, y + ch + s(18)), under[i], font=f_under,
                   fill=accent if on else ink, anchor="ma")


def worked_strips():
    """Small figures for the data slot of the three worked-solution slides (4.23 x 2.48 in).
    Text is at least 48 of 900 px, so it clears 16pt once placed."""
    white, asphalt, graphite, hair, accent = tokens()
    f = font("Archivo-Bold.ttf", 52)
    f_u = font("Archivo-SemiBold.ttf", 48)

    im = Image.new("RGB", (W, H), white); d = ImageDraw.Draw(im)
    cells_row(d, ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"], {0, 6}, s(200), s(110), s(120),
              s(10), f, white, asphalt, accent, graphite)
    d.text((s(450), s(110)), "PERIOD 3", font=f_u, fill=asphalt, anchor="mm")
    d.text((s(450), s(410)), "same 3 energy levels", font=f_u, fill=asphalt, anchor="mm")
    im.save(os.path.join(ASSETS, "chem_u03_s3.6_period3.png"))

    im = Image.new("RGB", (W, H), white); d = ImageDraw.Draw(im)
    syms = ["Be", "Mg", "Ca", "Sr", "Ba"]
    for i, sym in enumerate(syms):
        y = s(20) + i * s(100)
        box = [s(130), y, s(330), y + s(90)]
        on = sym in ("Mg", "Ba")
        d.rectangle(box, outline=graphite, width=s(2), fill=accent if on else None)
        d.text((s(230), y + s(45)), sym, font=f, fill=white if on else asphalt, anchor="mm")
        d.text((s(370), y + s(45)), f"{i + 2} levels", font=f_u,
               fill=accent if on else asphalt, anchor="lm")
    im.save(os.path.join(ASSETS, "chem_u03_s3.6_group2.png"))

    im = Image.new("RGB", (W, H), white); d = ImageDraw.Draw(im)
    groups = ["1", "2", "13", "14", "15", "16", "17", "18"]
    charges = ["1+", "2+", "3+", "—", "3−", "2−", "1−", "—"]
    d.text((s(450), s(90)), "GROUP", font=f_u, fill=asphalt, anchor="mm")
    cells_row(d, groups, {1, 5}, s(150), s(110), s(110), s(10), f, white, asphalt, accent, graphite,
              under=charges, f_under=f)
    d.text((s(450), s(440)), "usual ion charge", font=f_u, fill=asphalt, anchor="mm")
    im.save(os.path.join(ASSETS, "chem_u03_s3.7_group_charges.png"))
    print("wrote three worked-solution strips")


if __name__ == "__main__":
    trend_arrows()
    ion_sizes()
    worked_strips()
    sys.exit(0)
