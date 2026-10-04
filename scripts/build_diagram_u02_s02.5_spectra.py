#!/usr/bin/env python3
"""Draw the S2.5 "Atomic & Electron Spectra" figures for CHEM U02.

Hand-built, not generated: every number a student reads off these figures is computed
here from the Rydberg/Bohr relation, never typed. Colours of the UI (text, rules, card
edges) come from brand/tokens.json; type is the shipped Archivo. The spectrum and flame
swatches are physical-colour illustrations of light - the one allowed exception to the
brand palette, and only inside the figure.

    python3 scripts/build_diagram_u02_s02.5_spectra.py

Writes templates/slide/assets/chem_u02_s2.5_*.png, each 1010x600 logical px at 4x, so
it fills layout 08's diagram slot (5.05 x 3.0 in) without letterboxing. 44 logical px is
16 pt at that placement, so no label in any figure is smaller than that.
"""
import json, math, os, sys
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(REPO, "templates", "slide", "assets")
S = 4
W, H = 1010 * S, 600 * S
MIN_PX = 44                     # 16 pt at 200 px/in

R_H = 1.09678e7                 # Rydberg constant, 1/m
H_PLANCK, C_LIGHT = 6.626e-34, 3.00e8
E_1 = 2.18e-18                  # J, hydrogen n = 1 magnitude (brief constants table)


def tok():
    t = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
    g = t["ground"]
    return dict(white=g["white"]["hex"], ink=g["asphalt"]["hex"], grey=g["graphite"]["hex"],
                rule=g["ruleHairline"]["hex"], accent=t["courses"]["chemistry"]["primaryDeep"]["hex"])


T = tok()


def font(name, px):
    return ImageFont.truetype(os.path.join(REPO, "brand", "fonts", name), int(px * S))


F_LAB = font("Archivo-SemiBold.ttf", MIN_PX)
F_BOLD = font("Archivo-Bold.ttf", MIN_PX)
F_SUP = font("Archivo-Bold.ttf", 30)   # superscript charge only; never a stand-alone label


# ---------------------------------------------------------------- physics
def balmer_nm(n):
    """Wavelength (nm) of the n -> 2 line, from the Rydberg relation."""
    return 1e9 / (R_H * (1 / 4 - 1 / n ** 2))


def delta_e(n):
    """Photon energy (J) of the n -> 2 drop, from E_n = -2.18e-18 / n^2."""
    return E_1 * (1 / 4 - 1 / n ** 2)


LINES = {n: balmer_nm(n) for n in (3, 4, 5, 6)}
assert [round(v) for v in LINES.values()] == [656, 486, 434, 410], LINES   # brief: exact facts
# cross-check the two routes (Bohr energy + hc/E vs Rydberg) agree to within rounding
for n, lam in LINES.items():
    assert abs(H_PLANCK * C_LIGHT / delta_e(n) * 1e9 - lam) < 1.5, n


def rgb(wl, floor=1.0):
    """Approximate display colour of a wavelength (Bruton). floor<1 dims the band ends."""
    if 380 <= wl < 440:   r, g, b = -(wl - 440) / 60, 0, 1
    elif wl < 490:        r, g, b = 0, (wl - 440) / 50, 1
    elif wl < 510:        r, g, b = 0, 1, -(wl - 510) / 20
    elif wl < 580:        r, g, b = (wl - 510) / 70, 1, 0
    elif wl < 645:        r, g, b = 1, -(wl - 645) / 65, 0
    else:                 r, g, b = 1, 0, 0
    if floor < 1:
        k = floor + (1 - floor) * (0.0 if wl < 380 or wl > 700 else 1.0)
        if wl < 420:  k = floor + (1 - floor) * (wl - 380) / 40
        elif wl > 645: k = floor + (1 - floor) * (700 - wl) / 55
        else:         k = 1.0
    else:
        k = 1.0
    gam = 0.8
    return tuple(int(255 * (c * k) ** gam) for c in (r, g, b))


# ---------------------------------------------------------------- drawing helpers
def new():
    im = Image.new("RGB", (W, H), T["white"])
    return im, ImageDraw.Draw(im)


def px(v):
    return int(v * S)


def text(d, x, y, s, f=F_LAB, fill=None, anchor="mm"):
    d.text((px(x), px(y)), s, font=f, fill=fill or T["ink"], anchor=anchor)


def ion(d, x, y, sym, charge, fill=None, anchor_left=True):
    """Draw 'Ca' with a raised '2+'. Returns the right edge in logical px."""
    d.text((px(x), px(y)), sym, font=F_BOLD, fill=fill or T["ink"], anchor="lm")
    w = F_BOLD.getlength(sym) / S
    d.text((px(x + w + 2), px(y - 16)), charge, font=F_SUP, fill=fill or T["ink"], anchor="lm")
    return x + w + 2 + F_SUP.getlength(charge) / S


X0, X1 = 40, 970                # spectrum bar span; 400 nm .. 700 nm


def xw(wl):
    return X0 + (wl - 400) / 300 * (X1 - X0)


def rainbow(d, y0, y1, floor=0.35):
    for x in range(X0 * S, X1 * S):
        wl = 400 + (x / S - X0) / (X1 - X0) * 300
        d.line([(x, px(y0)), (x, px(y1))], fill=rgb(wl, floor))


def emission_lines(d, y0, y1):
    """Hydrogen lines on whatever is behind. Soft halo, then a hard core."""
    for lam in LINES.values():
        x = xw(lam)
        col = rgb(lam)
        for wdt, a in ((14, 0.18), (8, 0.35)):
            halo = tuple(int(c * a) for c in col)
            d.rectangle([px(x - wdt / 2), px(y0), px(x + wdt / 2), px(y1)], fill=halo)
        d.rectangle([px(x - 2.5), px(y0), px(x + 2.5), px(y1)], fill=col)


def save(im, name):
    os.makedirs(ASSETS, exist_ok=True)
    out = os.path.join(ASSETS, name)
    im.save(out)
    print(f"wrote {os.path.relpath(out, REPO)}  {im.width}x{im.height}")


# ---------------------------------------------------------------- figure 1: visible spectrum
def fig_visible():
    im, d = new()
    # colour names over the band they sit in; two rows so the narrow yellow/orange fit
    names = [("Violet", 425, 1), ("Blue", 472, 2), ("Green", 532, 1),
             ("Yellow", 580, 2), ("Orange", 605, 1), ("Red", 660, 2)]
    bar0, bar1 = 175, 335
    for nm, wl, row in names:
        x = xw(wl)
        cy = 38 if row == 1 else 105
        text(d, x, cy, nm)
        d.line([(px(x), px(cy + 26)), (px(x), px(bar0))], fill=T["grey"], width=px(2))
    rainbow(d, bar0, bar1)
    d.rectangle([px(X0), px(bar0), px(X1), px(bar1)], outline=T["grey"], width=px(2))
    # band boundaries, staggered two rows
    ticks = [(400, 1), (450, 2), (495, 1), (570, 2), (590, 1), (620, 2), (700, 1)]
    for wl, row in ticks:
        x = xw(wl)
        ty = 385 if row == 1 else 448
        d.line([(px(x), px(bar1)), (px(x), px(ty - 24))], fill=T["grey"], width=px(2))
        anchor = "lm" if wl == 400 else "rm" if wl == 700 else "mm"
        d.text((px(x - (30 if wl == 400 else 0)), px(ty)), str(wl), font=F_BOLD,
               fill=T["ink"], anchor=anchor)
    text(d, 505, 515, "Wavelength (nm)", fill=T["grey"])
    # energy direction
    ay = 570
    d.line([(px(X0 + 4), px(ay)), (px(100), px(ay))], fill=T["accent"], width=px(3))
    d.polygon([(px(X0 + 4), px(ay)), (px(X0 + 26), px(ay - 11)), (px(X0 + 26), px(ay + 11))], fill=T["accent"])
    text(d, 112, ay, "More energy", anchor="lm")
    d.line([(px(920), px(ay)), (px(X1 - 4), px(ay))], fill=T["accent"], width=px(3))
    d.polygon([(px(X1 - 4), px(ay)), (px(X1 - 26), px(ay - 11)), (px(X1 - 26), px(ay + 11))], fill=T["accent"])
    text(d, 908, ay, "Less energy", anchor="rm")
    save(im, "chem_u02_s2.5_visible_spectrum.png")


# ---------------------------------------------------------------- figure 2: hydrogen lines
def fig_h_lines():
    im, d = new()
    y0, y1 = 100, 330
    d.rectangle([px(X0), px(y0), px(X1), px(y1)], fill=(0, 0, 0))
    emission_lines(d, y0, y1)
    text(d, X0, 45, "400 nm", anchor="lm")
    text(d, X1, 45, "700 nm", anchor="rm")
    d.line([(px(X0), px(y0 - 20)), (px(X0), px(y0))], fill=T["grey"], width=px(2))
    d.line([(px(X1), px(y0 - 20)), (px(X1), px(y0))], fill=T["grey"], width=px(2))
    # labels: 410 and 434 are 74 px apart, so alternate rows
    rows = {3: 1, 4: 1, 5: 2, 6: 1}
    for n, lam in LINES.items():
        x = xw(lam)
        ly = 388 if rows[n] == 1 else 452
        d.line([(px(x), px(y1)), (px(x), px(ly - 26))], fill=T["grey"], width=px(2))
        text(d, x, ly, f"{round(lam)}", f=F_BOLD)
    text(d, 505, 548, "Wavelength (nm)", fill=T["grey"])
    save(im, "chem_u02_s2.5_hydrogen_emission_lines.png")


# ---------------------------------------------------------------- figure 3: transitions
def fig_levels():
    im, d = new()
    top, n2 = 50, 440
    def ly(n):
        return top + (n2 - top) * (E_1 / n ** 2) / (E_1 / 4)
    lx0, lx1 = 275, 905
    levels = {2: ly(2), 3: ly(3), 4: ly(4), 5: ly(5), 6: ly(6)}
    d.line([(px(lx0), px(top)), (px(lx1), px(top))], fill=T["grey"], width=px(3))
    for n, y in levels.items():
        d.line([(px(lx0), px(y)), (px(lx1), px(y))], fill=T["ink"], width=px(4))
    # labels in an even column, leaders to the true level height (levels crowd upward)
    lab = {"inf": (38, top), 6: (92, levels[6]), 5: (146, levels[5]),
           4: (200, levels[4]), 3: (254, levels[3]), 2: (n2, levels[2])}
    for key, (cy, y) in lab.items():
        s = "n = ∞" if key == "inf" else f"n = {key}"
        text(d, 20, cy, s, f=F_BOLD, anchor="lm")
        d.line([(px(190), px(cy)), (px(215), px(cy))], fill=T["rule"], width=px(2))
        d.line([(px(215), px(cy)), (px(250), px(y))], fill=T["rule"], width=px(2))
        d.line([(px(250), px(y)), (px(lx0), px(y))], fill=T["rule"], width=px(2))
    # drops to n = 2
    xs = {3: 395, 4: 515, 5: 635, 6: 755}
    for n, x in xs.items():
        col = rgb(LINES[n])
        y_start, y_end = levels[n], levels[2]
        d.line([(px(x), px(y_start + 4)), (px(x), px(y_end - 24))], fill=col, width=px(9))
        d.polygon([(px(x), px(y_end - 2)), (px(x - 20), px(y_end - 34)), (px(x + 20), px(y_end - 34))],
                  fill=col)
        text(d, x, 488, f"{round(LINES[n])}", f=F_BOLD)
    text(d, 575, 548, "Wavelength (nm) of each drop", fill=T["grey"])
    # energy axis
    ax = 995
    d.line([(px(ax), px(n2)), (px(ax), px(top + 40))], fill=T["accent"], width=px(3))
    d.polygon([(px(ax), px(top + 6)), (px(ax - 12), px(top + 40)), (px(ax + 12), px(top + 40))],
              fill=T["accent"])
    tmp = Image.new("RGBA", (px(210), px(60)), (255, 255, 255, 0))
    ImageDraw.Draw(tmp).text((px(105), px(30)), "Energy", font=F_BOLD, fill=T["ink"], anchor="mm")
    rot = tmp.rotate(90, expand=True)
    im.paste(rot, (px(ax - 38) - rot.width // 2, px(245) - rot.height // 2), rot)
    save(im, "chem_u02_s2.5_energy_transitions.png")


# ---------------------------------------------------------------- figure 4: three spectra
def fig_types():
    im, d = new()
    strips = [("Continuous", 62), ("Emission", 222), ("Absorption", 382)]
    for label, y0 in strips:
        y1 = y0 + 90
        text(d, X0, y0 - 30, label, f=F_BOLD, anchor="lm")
        if label == "Continuous":
            rainbow(d, y0, y1)
        elif label == "Emission":
            d.rectangle([px(X0), px(y0), px(X1), px(y1)], fill=(0, 0, 0))
            emission_lines(d, y0, y1)
        else:
            rainbow(d, y0, y1)
            for lam in LINES.values():
                x = xw(lam)
                d.rectangle([px(x - 4.5), px(y0), px(x + 4.5), px(y1)], fill=(8, 8, 8))
        d.rectangle([px(X0), px(y0), px(X1), px(y1)], outline=T["grey"], width=px(2))
    text(d, X0, 520, "400 nm", anchor="lm")
    text(d, X1, 520, "700 nm", anchor="rm")
    text(d, 505, 520, "Wavelength", fill=T["grey"])
    save(im, "chem_u02_s2.5_spectra_types.png")


# ---------------------------------------------------------------- figure 5: pre-built table
def fig_table():
    im, d = new()
    cols = {"drop": 40, "dE": 240, "lam": 520, "sw": 800}
    hy = 52
    text(d, cols["drop"], hy, "Drop", f=F_BOLD, anchor="lm", fill=T["grey"])
    text(d, cols["dE"], hy, "ΔE (J)", anchor="lm", fill=T["grey"])
    text(d, cols["lam"], hy, "λ (nm)", anchor="lm", fill=T["grey"])
    d.line([(px(X0), px(92)), (px(X1), px(92))], fill=T["grey"], width=px(3))
    for i, n in enumerate((3, 4, 5, 6)):
        cy = 150 + i * 106
        text(d, cols["drop"], cy, f"{n} → 2", f=F_BOLD, anchor="lm")
        mant, exp = f"{delta_e(n):.2e}".split("e")
        text(d, cols["dE"], cy, f"{mant}e{int(exp)}", f=F_BOLD, anchor="lm")
        text(d, cols["lam"], cy, f"{round(LINES[n])}", f=F_BOLD, anchor="lm")
        d.rounded_rectangle([px(cols["sw"]), px(cy - 34), px(cols["sw"] + 170), px(cy + 34)],
                            radius=px(8), fill=rgb(LINES[n]), outline=T["grey"], width=px(2))
        if i < 3:
            d.line([(px(X0), px(cy + 53)), (px(X1), px(cy + 53))], fill=T["rule"], width=px(2))
    save(im, "chem_u02_s2.5_balmer_table.png")


# ---------------------------------------------------------------- figures 6-7: flame colours
# Widely taught colours only. Swatches are illustrations of the colour named, not photographs.
FLAME = {
    "Li": ("+", "crimson red", (200, 30, 60)),
    "Na": ("+", "yellow-orange", (250, 170, 20)),
    "K":  ("+", "lilac", (185, 140, 225)),
    "Cu": ("2+", "blue-green", (20, 165, 150)),
    "Ca": ("2+", "orange-red", (235, 95, 30)),
    "Sr": ("2+", "red", (215, 35, 35)),
    "Ba": ("2+", "pale green", (170, 215, 120)),
}


def fig_flame(keys, name):
    im, d = new()
    n = len(keys)
    step = 128
    y_start = 300 - step * (n - 1) / 2
    for i, k in enumerate(keys):
        cy = y_start + i * step
        chg, label, col = FLAME[k]
        d.ellipse([px(50), px(cy - 42), px(134), px(cy + 42)], fill=col, outline=T["grey"], width=px(2))
        ion(d, 175, cy, k, chg)
        text(d, 395, cy, label, f=F_LAB, anchor="lm")
        if i < n - 1:
            d.line([(px(X0), px(cy + step / 2)), (px(X1), px(cy + step / 2))], fill=T["rule"], width=px(2))
    save(im, name)


def main():
    fig_visible()
    fig_h_lines()
    fig_levels()
    fig_types()
    fig_table()
    fig_flame(["Li", "Na", "K", "Cu"], "chem_u02_s2.5_flame_colors_1.png")
    fig_flame(["Ca", "Sr", "Ba"], "chem_u02_s2.5_flame_colors_2.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
