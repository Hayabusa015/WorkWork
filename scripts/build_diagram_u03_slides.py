#!/usr/bin/env python3
"""Draw the figures for the CHEM U03 periodic-trends deck (3.3 radius, 3.4 IE and EN, 3.6 why).

Hand-built, not generated: every figure carries numbers or symbols a student reads as
science. Primitives and palette come from build_diagram_trends.py so the two scripts draw
alike.

Type floor: a figure is read from a seat, so its smallest label must clear 16pt once
placed. On the 900 x 536 canvas that is about 40 px in an 08 diagram slot, 42 px in an 03
concept slot and 48 px in an 11 setup slot (both height-bound). Sizes below follow that.

Some figures come in pairs (_a, _b) of identical size. The deck stacks _b over _a in the
same slot and reveals it on a click, so the prediction is made before the answer shows.

Data (kJ/mol for ionization energy, pm for radius, Pauling for electronegativity):
  first IE, Z = 1-20 ........ NIST, rounded
  Al successive IE .......... 578, 1817, 2745, 11 577
  Mg successive IE .......... 738, 1451, 7733, 10 543
  radii ..................... textbook metallic/covalent values, the same set as the quiz key
  Mg2+ ...................... 72 pm (ionic, 6-coordinate)

    python3 scripts/build_diagram_u03_slides.py
"""
import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_diagram_trends import tokens, font, s, arrow, ASSETS, REPO, W, H   # noqa: E402

WHITE, INK, GRAPHITE, HAIR, ACCENT = tokens()


def canvas():
    im = Image.new("RGB", (W, H), WHITE)
    return im, ImageDraw.Draw(im)


def save(im, name):
    out = os.path.join(ASSETS, name)
    im.save(out)
    print(f"wrote {os.path.relpath(out, REPO)}")


def charge_label(d, cx, cy, sym, charge, f_sym, f_chg, fill):
    """Symbol with a raised charge, centred as one unit (Archivo has no superscript +/-)."""
    sw = d.textlength(sym, font=f_sym)
    cw = d.textlength(charge, font=f_chg) if charge else 0
    left = cx - (sw + cw + s(2)) / 2
    d.text((left, cy), sym, font=f_sym, fill=fill, anchor="lm")
    if charge:
        d.text((left + sw + s(2), cy - s(16)), charge, font=f_chg, fill=fill, anchor="lm")


# ---------------------------------------------------------------- 3.6 why: two atoms
def two_atoms():
    """Li and F: same two energy levels, 3 vs 9 protons, so F is drawn smaller."""
    im, d = canvas()
    f_nuc = font("Archivo-Bold.ttf", 44)
    f_lab = font("Archivo-Bold.ttf", 48)
    for cx, z, sym, r_out in ((225, "3+", "Li", 200), (675, "9+", "F", 130)):
        cy = 240
        for r in (r_out, r_out * 0.55):
            d.ellipse([s(cx - r), s(cy - r), s(cx + r), s(cy + r)], outline=GRAPHITE, width=s(3))
        d.ellipse([s(cx - 42), s(cy - 42), s(cx + 42), s(cy + 42)], fill=ACCENT)
        d.text((s(cx), s(cy)), z, font=f_nuc, fill=WHITE, anchor="mm")
        d.text((s(cx), s(500)), sym, font=f_lab, fill=INK, anchor="mm")
    save(im, "chem_u03_s3.6_two_atoms.png")


# ---------------------------------------------------------------- 3.4 first IE, Z = 1-20
IE1 = [1312, 2372, 520, 900, 801, 1086, 1402, 1314, 1681, 2081,
       496, 738, 578, 787, 1012, 1000, 1251, 1521, 419, 590]
SYM = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
       "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]


def ie_chart():
    im, d = canvas()
    f = font("Archivo-SemiBold.ttf", 40)
    fb = font("Archivo-Bold.ttf", 42)
    x0, x1, y0, y1 = 130, 880, 40, 470          # plot box: y0 top (2500), y1 bottom (0)
    top = 2500
    d.line([(s(x0), s(y0)), (s(x0), s(y1)), (s(x1), s(y1))], fill=GRAPHITE, width=s(2))
    for v in (0, 1000, 2000):
        y = y1 - (y1 - y0) * v / top
        d.text((s(x0 - 12), s(y)), f"{v}", font=f, fill=INK, anchor="rm")
        if v:
            d.line([(s(x0), s(y)), (s(x1), s(y))], fill=HAIR, width=s(1))
    step = (x1 - x0 - 30) / 19
    pts = [(x0 + 15 + i * step, y1 - (y1 - y0) * v / top) for i, v in enumerate(IE1)]
    d.line([(s(x), s(y)) for x, y in pts], fill=ACCENT, width=s(4))
    for i, (x, y) in enumerate(pts):
        r = 7
        d.ellipse([s(x - r), s(y - r), s(x + r), s(y + r)], fill=ACCENT)
    for sym in ("He", "Ne", "Ar"):
        x, y = pts[SYM.index(sym)]
        d.text((s(x), s(y - 16)), sym, font=fb, fill=INK, anchor="mb")
    for sym in ("Li", "Na", "K"):
        x, y = pts[SYM.index(sym)]
        d.text((s(x), s(y + 14)), sym, font=fb, fill=INK, anchor="mt")
    d.text((s(x1), s(y1 + 14)), "atomic number →", font=f, fill=INK, anchor="ra")
    save(im, "chem_u03_s3.4_ie_chart.png")


# ---------------------------------------------------------------- 3.4 aluminum, successive IE
AL = [578, 1817, 2745, 11577]


def al_bars(reveal):
    im, d = canvas()
    f = font("Archivo-SemiBold.ttf", 40)
    fb = font("Archivo-Bold.ttf", 42)
    x0, x1, y0, y1 = 150, 880, 30, 450
    top = 13000                                   # headroom so the 11,577 label clears the top
    d.line([(s(x0), s(y0)), (s(x0), s(y1)), (s(x1), s(y1))], fill=GRAPHITE, width=s(2))
    for v in (0, 6000, 12000):
        y = y1 - (y1 - y0) * v / top
        d.text((s(x0 - 12), s(y)), f"{v:,}", font=f, fill=INK, anchor="rm")
        if v:
            d.line([(s(x0), s(y)), (s(x1), s(y))], fill=HAIR, width=s(1))
    bw, gapw = 120, 62
    for i, v in enumerate(AL):
        bx = x0 + 40 + i * (bw + gapw)
        d.text((s(bx + bw / 2), s(y1 + 14)), ["1st", "2nd", "3rd", "4th"][i], font=fb, fill=INK, anchor="ma")
        if i == 3 and not reveal:
            # the prediction slot: an empty dashed box at a neutral height, and a question mark
            yt = y1 - 120
            for yy in range(int(yt), y1, 14):
                d.line([(s(bx), s(yy)), (s(bx), s(min(yy + 7, y1)))], fill=GRAPHITE, width=s(2))
                d.line([(s(bx + bw), s(yy)), (s(bx + bw), s(min(yy + 7, y1)))], fill=GRAPHITE, width=s(2))
            for xx in range(int(bx), int(bx + bw), 14):
                d.line([(s(xx), s(yt)), (s(min(xx + 7, bx + bw)), s(yt))], fill=GRAPHITE, width=s(2))
            d.text((s(bx + bw / 2), s(yt - 10)), "?", font=font("Archivo-Bold.ttf", 64), fill=INK, anchor="mb")
            continue
        yt = y1 - (y1 - y0) * v / top
        d.rectangle([s(bx), s(yt), s(bx + bw), s(y1)], fill=ACCENT if i == 3 else GRAPHITE)
        d.text((s(bx + bw / 2), s(yt - 8)), f"{v:,}", font=fb, fill=INK, anchor="mb")
    save(im, f"chem_u03_s3.4_al_ie_{'b' if reveal else 'a'}.png")


# ---------------------------------------------------------------- 3.4 electronegativity
def en_charts():
    im, d = canvas()
    f = font("Archivo-Bold.ttf", 40)
    fh = font("Archivo-Bold.ttf", 42)
    base, top_y, top = 440, 70, 4.0

    def bars(x0, syms, vals, bw, gapw, hi):
        for i, (sym, v) in enumerate(zip(syms, vals)):
            bx = x0 + i * (bw + gapw)
            yt = base - (base - top_y) * v / top
            d.rectangle([s(bx), s(yt), s(bx + bw), s(base)], fill=ACCENT if sym == hi else GRAPHITE)
            d.text((s(bx + bw / 2), s(base + 12)), sym, font=f, fill=INK, anchor="ma")

    d.text((s(20), s(20)), "PERIOD 2", font=fh, fill=INK, anchor="la")
    bars(20, ["Li", "Be", "B", "C", "N", "O", "F"], [0.98, 1.57, 2.04, 2.55, 3.04, 3.44, 3.98], 50, 13, "F")
    d.line([(s(470), s(20)), (s(470), s(510))], fill=HAIR, width=s(2))
    d.text((s(510), s(20)), "GROUP 17", font=fh, fill=INK, anchor="la")
    bars(510, ["F", "Cl", "Br", "I"], [3.98, 3.16, 2.96, 2.66], 66, 26, "F")
    save(im, "chem_u03_s3.4_en_charts.png")


def en_example():
    """O, F and S placed where they sit, for the 11 setup slot (48 px floor)."""
    im, d = canvas()
    f = font("Archivo-Bold.ttf", 60)
    fl = font("Archivo-SemiBold.ttf", 48)
    c, x0, y0 = 150, 330, 120
    d.text((s(x0 + c / 2), s(60)), "16", font=fl, fill=INK, anchor="mm")
    d.text((s(x0 + c * 1.5 + 10), s(60)), "17", font=fl, fill=INK, anchor="mm")
    d.text((s(x0 - 30), s(y0 + c / 2)), "period 2", font=fl, fill=INK, anchor="rm")
    d.text((s(x0 - 30), s(y0 + c * 1.5 + 10)), "period 3", font=fl, fill=INK, anchor="rm")
    cells = {(0, 0): "O", (1, 0): "F", (0, 1): "S", (1, 1): ""}
    for (cx, cy), sym in cells.items():
        bx, by = x0 + cx * (c + 10), y0 + cy * (c + 10)
        d.rectangle([s(bx), s(by), s(bx + c), s(by + c)], outline=GRAPHITE, width=s(3))
        if sym:
            d.text((s(bx + c / 2), s(by + c / 2)), sym, font=f, fill=INK, anchor="mm")
    save(im, "chem_u03_s3.4_en_example.png")


# ---------------------------------------------------------------- 3.3 atomic radius
def radius_rows():
    im, d = canvas()
    fh = font("Archivo-Bold.ttf", 40)
    fs = font("Archivo-Bold.ttf", 40)
    k = 0.42                                   # px per pm of radius, both rows, so they compare

    def row(y_cap, cap, syms, radii, x_start, gapw):
        d.text((s(20), s(y_cap)), cap, font=fh, fill=INK, anchor="la")
        cy = y_cap + 50 + max(radii) * k
        x = x_start
        for sym, r in zip(syms, radii):
            R = r * k
            x += R
            d.ellipse([s(x - R), s(cy - R), s(x + R), s(cy + R)], outline=INK, width=s(3))
            d.text((s(x), s(cy)), sym, font=fs, fill=INK, anchor="mm")
            x += R + gapw

    row(0, "ACROSS PERIOD 3  →  smaller", ["Na", "Mg", "Al", "Si", "P", "S", "Cl"],
        [186, 160, 143, 118, 110, 104, 99], 20, 8)
    row(236, "DOWN GROUP 1  →  larger", ["Li", "Na", "K"], [152, 186, 227], 20, 20)
    save(im, "chem_u03_s3.3_radius_rows.png")


def mg_ion(reveal):
    im, d = canvas()
    f_sym = font("Archivo-Bold.ttf", 52)
    f_chg = font("Archivo-Bold.ttf", 38)
    f_lab = font("Archivo-SemiBold.ttf", 44)
    k = 1.25
    cy = 230
    R1, R2 = 160 * k, 72 * k
    cx1, cx2 = 250, 680
    d.ellipse([s(cx1 - R1), s(cy - R1), s(cx1 + R1), s(cy + R1)], outline=INK, width=s(3))
    charge_label(d, s(cx1), s(cy), "Mg", "", f_sym, f_chg, INK)
    d.text((s(cx1), s(490)), "160 pm", font=f_lab, fill=INK, anchor="mm")
    arrow(d, (s(cx1 + R1 + 30), s(cy)), (s(cx2 - 130), s(cy)), GRAPHITE, width=5, head=20)
    if reveal:
        d.ellipse([s(cx2 - R2), s(cy - R2), s(cx2 + R2), s(cy + R2)], fill=ACCENT)
        charge_label(d, s(cx2), s(cy), "Mg", "2+", f_sym, f_chg, WHITE)
        d.text((s(cx2), s(490)), "72 pm", font=f_lab, fill=ACCENT, anchor="mm")
    else:
        d.text((s(cx2), s(cy)), "?", font=font("Archivo-Bold.ttf", 90), fill=INK, anchor="mm")
        d.text((s(cx2), s(490)), "Mg ion", font=f_lab, fill=INK, anchor="mm")
    save(im, f"chem_u03_s3.3_mg_ion_{'b' if reveal else 'a'}.png")


# ---------------------------------------------------------------- 3.6 check: period 4
def period4():
    im, d = canvas()
    f = font("Archivo-Bold.ttf", 52)
    fl = font("Archivo-SemiBold.ttf", 48)
    syms = ["K", "Ca", "Ga", "Ge", "As", "Se", "Br", "Kr"]
    cw = 108
    x0 = (900 - cw * 8) / 2
    d.text((s(450), s(110)), "PERIOD 4", font=fl, fill=INK, anchor="mm")
    for i, sym in enumerate(syms):
        bx = x0 + i * cw
        on = sym in ("Ca", "Br")
        d.rectangle([s(bx), s(190), s(bx + cw - 6), s(320)], outline=GRAPHITE, width=s(2),
                    fill=ACCENT if on else None)
        d.text((s(bx + (cw - 6) / 2), s(255)), sym, font=f, fill=WHITE if on else INK, anchor="mm")
    d.text((s(450), s(420)), "same 4 energy levels", font=fl, fill=INK, anchor="mm")
    save(im, "chem_u03_s3.6_period4.png")


# ---------------------------------------------------------------- 3.4 your turn: magnesium
MG = [738, 1451, 7733, 10543]


def mg_bars():
    """Magnesium's first four IEs, for the 11 setup slot (48 px floor). No reveal: the
    class finds the jump themselves."""
    im, d = canvas()
    f = font("Archivo-Bold.ttf", 48)
    x0, y0, y1, top = 20, 70, 440, 11000
    bw, gapw = 190, 30
    for i, v in enumerate(MG):
        bx = x0 + i * (bw + gapw)
        yt = y1 - (y1 - y0) * v / top
        d.rectangle([s(bx), s(yt), s(bx + bw), s(y1)], fill=GRAPHITE)
        d.text((s(bx + bw / 2), s(yt - 8)), f"{v:,}", font=f, fill=INK, anchor="mb")
        d.text((s(bx + bw / 2), s(y1 + 12)), ["1st", "2nd", "3rd", "4th"][i], font=f, fill=INK, anchor="ma")
    d.line([(s(x0), s(y1)), (s(x0 + 4 * (bw + gapw)), s(y1))], fill=GRAPHITE, width=s(2))
    save(im, "chem_u03_s3.4_mg_ie.png")


if __name__ == "__main__":
    two_atoms()
    ie_chart()
    al_bars(False)
    al_bars(True)
    en_charts()
    en_example()
    radius_rows()
    mg_ion(False)
    mg_ion(True)
    period4()
    mg_bars()
