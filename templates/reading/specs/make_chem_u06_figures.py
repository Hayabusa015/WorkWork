#!/usr/bin/env python3
"""Figures 6.1-6.6 for the Chemistry U6 unit reading (Chemical Nomenclature).

    python3 templates/reading/specs/make_chem_u06_figures.py OUT_DIR

Drawn with matplotlib at the size they print: FIG_IN wide (the builder places every
figure at FIG_W_IN = 3.0 in), so a 8.5 pt label is 8.5 pt on paper. Every name, formula
and charge total traces to reports/chem_u06_reading_dossier.md section B; the charge
totals on Figures 6.4 and 6.5 are computed here and checked, and a mismatch stops the
build.

Figure 6.1 is a formula panel, not the shared molecule builder. The builder
(scripts/build_diagram_molecule.py --explicit-h --label-carbons --no-caption) was tried
for CO on 2026-11-25: "[C-]#[O+]" draws O+ and drops the C- label, a misleading formal
charge; "[C]=O" draws a double bond and a lone pair on carbon. CO2 ("O=C=O") drew
correctly, but one molecule drawn by the builder beside one drawn by hand would compare
two drawing styles, not two molecules. So both are drawn here as labelled atom counts,
with no bonds, no charges and no sizes claimed.

Print discipline (brand/SHULL_DESIGN_SYSTEM.md section 8): outlines only, no fills.
Distinctions are carried by line style and label, never by hue alone. Type is Archivo.
Colour is read from brand/tokens.json; no hex is typed here.
"""
import json, os, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                   # noqa: E402
from matplotlib import font_manager                               # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
FONTS = os.path.join(REPO, "brand", "fonts")
for f in ("Archivo-Regular.ttf", "Archivo-Bold.ttf", "Archivo-SemiBold.ttf"):
    font_manager.fontManager.addfont(os.path.join(FONTS, f))
plt.rcParams.update({
    "font.family": "Archivo", "mathtext.fontset": "custom", "mathtext.rm": "Archivo",
    "mathtext.it": "Archivo", "mathtext.bf": "Archivo:bold", "mathtext.cal": "Archivo",
    "mathtext.sf": "Archivo", "mathtext.tt": "Archivo", "mathtext.fallback": None, "axes.unicode_minus": True,
    "svg.fonttype": "none",
})

DPI = 300
FIG_IN = 3.0
INK = T["ground"]["asphalt"]["hex"]
LABEL = T["ground"]["label"]["hex"]
HAIR = T["ground"]["ruleHairline"]["hex"]
ACCENT = T["courses"]["chemistry"]["primaryDeep"]["hex"]    # type on white
DISPLAY = T["courses"]["chemistry"]["primary"]["hex"]       # rules only, never type


def m(s):
    """'SO_{4}^{2-}' -> mathtext in the text face. Plain text passes through."""
    if "_{" not in s and "^{" not in s:
        return s
    out, i = "", 0
    while i < len(s):
        if s.startswith("_{", i) or s.startswith("^{", i):
            j = s.index("}", i)
            out += "$" + s[i] + "{\\mathregular{" + s[i + 2:j].replace("-", "{-}").replace("+", "{+}") + "}}$"
            i = j + 1
        else:
            out += s[i]
            i += 1
    return out.replace("$$", "")


def canvas(h_in):
    fig = plt.figure(figsize=(FIG_IN, h_in), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FIG_IN); ax.set_ylim(0, h_in); ax.axis("off")
    return fig, ax


def text(ax, x, y, s, size=8.5, weight="regular", color=INK, ha="center", va="center"):
    ax.text(x, y, m(s), fontsize=size, fontweight=weight, color=color, ha=ha, va=va)


def box(ax, x, y, w, h, *, color=INK, lw=0.9, ls="-", round_=True):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.05" if round_ else "square,pad=0",
                       fill=False, edgecolor=color, linewidth=lw, linestyle=ls)
    ax.add_patch(p)


def arrow(ax, a, b, color=INK, lw=0.9):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>,head_length=4,head_width=2.4", mutation_scale=1,
                                 color=color, linewidth=lw, shrinkA=0, shrinkB=0))


def save(fig, out):
    fig.savefig(out, dpi=DPI, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------------------------
def fig_co_co2(out):
    """6.1: CO and CO2 as atom counts. Same two elements, different ratio, different
    substance. No bonds or charges are drawn (see the module note)."""
    fig, ax = canvas(1.42)
    r = 0.17
    panels = [(0.75, ["C", "O"], "CO", "carbon monoxide", "1 C + 1 O"),
              (2.25, ["O", "C", "O"], "CO_{2}", "carbon dioxide", "1 C + 2 O")]
    for cx, atoms, formula, name, count in panels:
        n = len(atoms)
        x0 = cx - (n - 1) * r * 2.08 / 2
        for k, a in enumerate(atoms):
            x = x0 + k * r * 2.08
            ax.add_patch(Circle((x, 1.08), r, fill=False, edgecolor=INK,
                                linewidth=1.3 if a == "C" else 0.9, linestyle="-" if a == "C" else (0, (3, 1.6))))
            text(ax, x, 1.08, a, 9.5, "bold")
        text(ax, cx, 0.68, formula, 12, "bold")
        text(ax, cx, 0.40, name, 8.5, "semibold", ACCENT)
        text(ax, cx, 0.17, count, 8, "regular", LABEL)
    ax.plot([1.5, 1.5], [0.12, 1.32], color=HAIR, linewidth=0.8)
    save(fig, out)


def fig_sort(out):
    """6.2: which naming system? Acid first, then ions, then two nonmetals (deck slide 3,
    'Check for an acid first. Then look for ions or two nonmetals.')."""
    fig, ax = canvas(2.66)
    qx, qw, rx, rw, h = 0.04, 1.42, 1.70, 1.26, 0.56
    rows = [(1.80, "Starts with H and", "is written (aq)?", "ACID", "Section 6.4", "HCl(aq)"),
            (1.02, "Contains a metal", "or NH_{4}^{+}?", "IONIC", "Sections 6.2, 6.3", "CaCl_{2}"),
            ]
    text(ax, qx + qw / 2, 2.57, "Look at the formula", 8.5, "bold")
    arrow(ax, (qx + qw / 2, 2.48), (qx + qw / 2, 1.80 + h + 0.01))
    for y, q1, q2, kind, where, ex in rows:
        box(ax, qx, y, qw, h, color=INK, lw=0.9)
        text(ax, qx + qw / 2, y + h * 0.66, q1, 8.5)
        text(ax, qx + qw / 2, y + h * 0.30, q2, 8.5)
        arrow(ax, (qx + qw + 0.02, y + h / 2), (rx - 0.02, y + h / 2))
        text(ax, (qx + qw + rx) / 2, y + h / 2 + 0.09, "yes", 8, "semibold", LABEL)
        box(ax, rx, y, rw, h, color=DISPLAY, lw=1.4)
        text(ax, rx + rw / 2, y + h * 0.74, kind, 8.5, "bold")
        text(ax, rx + rw / 2, y + h * 0.48, where, 8, "regular", ACCENT)
        text(ax, rx + rw / 2, y + h * 0.20, ex, 8.5, "semibold")
        arrow(ax, (qx + qw / 2, y - 0.01), (qx + qw / 2, y - 0.21))
        text(ax, qx + qw / 2 + 0.10, y - 0.11, "no", 8, "semibold", LABEL, ha="left")
    # the last stop: only nonmetals
    y = 0.24
    box(ax, qx, y, qw + (rx - qx - qw) + rw, h, color=DISPLAY, lw=1.4)
    text(ax, qx + 0.12, y + h * 0.70, "COVALENT", 8.5, "bold", ha="left")
    text(ax, qx + 0.12, y + h * 0.30, "only nonmetals: prefixes count atoms", 8, ha="left")
    text(ax, rx + rw / 2, y + h * 0.70, "Section 6.1", 8, "regular", ACCENT)
    text(ax, rx + rw / 2, y + h * 0.30, "CO_{2}", 8.5, "semibold")
    text(ax, FIG_IN / 2, 0.08, "Ionic names never use prefixes; the charges set the ratio.", 8, "regular", LABEL)
    save(fig, out)


def fig_ladder(out):
    """6.3: the chlorine oxyanion ladder, all 1- (sheet 6; dossier 6.2-h). O count and
    charge are printed as labels; chlorate, the starred ion, has the heavy box."""
    rows = [("per-  -ate", "perchlorate", "ClO_{4}^{-}", 4),
            ("-ate", "chlorate", "ClO_{3}^{-}", 3),
            ("-ite", "chlorite", "ClO_{2}^{-}", 2),
            ("hypo-  -ite", "hypochlorite", "ClO^{-}", 1)]
    fig, ax = canvas(1.52)
    cols = [0.06, 0.84, 1.80, 2.42]           # left edges: prefix/ending, name, formula, O
    heads = ["ENDING", "NAME", "FORMULA", "O ATOMS"]
    top = 1.42
    for x, hd in zip(cols, heads):
        text(ax, x + (0.0 if x < 1.7 else 0.25), top, hd, 8, "bold", ACCENT,
             ha="left" if x < 1.7 else "center")
    ax.plot([0.04, 2.96], [top - 0.10, top - 0.10], color=INK, linewidth=0.8)
    rh = 0.25
    for i, (end, name, f, n) in enumerate(rows):
        y = top - 0.24 - i * rh
        text(ax, cols[0], y, end, 8.5, "regular", LABEL, ha="left")
        text(ax, cols[1], y, name, 8.5, "bold" if name == "chlorate" else "regular", ha="left")
        text(ax, cols[2] + 0.25, y, f, 9.5, "bold")
        text(ax, cols[3] + 0.25, y, str(n), 9.5, "bold")
        if name == "chlorate":
            box(ax, 0.03, y - rh / 2 + 0.02, 2.93, rh - 0.04, color=DISPLAY, lw=1.6, round_=False)
        elif i < len(rows) - 1 and name != "perchlorate":
            ax.plot([0.04, 2.96], [y - rh / 2, y - rh / 2], color=HAIR, linewidth=0.6)
    yb = top - 0.24 - 3 * rh - rh / 2
    ax.plot([0.04, 2.96], [yb, yb], color=INK, linewidth=0.8)
    text(ax, 0.06, yb - 0.13, "All four have a 1− charge. Heavy box: chlorate (starred).",
         7.6, "regular", LABEL, ha="left")
    save(fig, out)


def tiles(ax, y, specs, unit, x0, h=0.34):
    """A row of charge tiles, each `abs(charge)` units long. Positive tiles: solid outline;
    negative: dashed. Returns the right edge."""
    x = x0
    for lab, q, shown in specs:
        w = abs(q) * unit
        box(ax, x + 0.015, y, w - 0.03, h, color=INK, lw=1.1, ls="-" if q > 0 else (0, (3.5, 1.8)), round_=False)
        text(ax, x + w / 2, y + h * 0.66, lab, 8.5, "bold")
        text(ax, x + w / 2, y + h * 0.26, shown, 8, "semibold", ACCENT)
        x += w
    return x


def fig_al2o3(out):
    """6.4: two Al3+ tiles against three O2- tiles; each row totals 6 units (dossier B)."""
    al, o = ("Al", 3), ("O", -2)
    n_al, n_o = 2, 3
    tot_p, tot_n = n_al * al[1], n_o * o[1]
    if tot_p + tot_n != 0 or (tot_p, tot_n) != (6, -6):
        sys.exit(f"figure 6.4: charges {tot_p} and {tot_n} do not match the dossier (+6, -6)")
    fig, ax = canvas(1.46)
    unit, x0 = 0.36, 0.08
    tiles(ax, 0.92, [("Al^{3+}", 3, "+3")] * n_al, unit, x0)
    tiles(ax, 0.46, [("O^{2-}", -2, "−2")] * n_o, unit, x0)
    xr = x0 + 6 * unit + 0.10
    text(ax, xr, 0.92 + 0.17, "+6", 10, "bold", ha="left")
    text(ax, xr, 0.46 + 0.17, "−6", 10, "bold", ha="left")
    ax.plot([x0, x0 + 6 * unit], [0.36, 0.36], color=HAIR, linewidth=0.6)
    text(ax, x0, 0.18, "(+6) + (−6) = 0", 8.5, "regular", LABEL, ha="left")
    text(ax, x0 + 6 * unit + 0.48, 0.18, "Al_{2}O_{3}", 11, "bold", ha="right")
    text(ax, x0, 1.37, "SAME LENGTH = CHARGES CANCEL", 8, "bold", ACCENT, ha="left")
    save(fig, out)


def fig_fe2o3(out):
    """6.5: work back from the anion. Three O2- = -6, so two Fe share +6: +3 each."""
    n_o, q_o, n_fe = 3, -2, 2
    total = -(n_o * q_o)
    if total % n_fe or total // n_fe != 3:
        sys.exit("figure 6.5: Fe charge does not come out +3 (dossier B)")
    each = total // n_fe
    fig, ax = canvas(1.78)
    unit, x0 = 0.36, 0.08
    text(ax, x0, 1.68, "1  START WITH THE ANION YOU KNOW", 8, "bold", ACCENT, ha="left")
    tiles(ax, 1.18, [("O^{2-}", q_o, "−2")] * n_o, unit, x0)
    text(ax, x0 + 6 * unit + 0.10, 1.35, f"−{total}", 10, "bold", ha="left")
    text(ax, x0, 1.00, "2  THE IRON MUST CANCEL IT: +6 SHARED BY 2", 8, "bold", ACCENT, ha="left")
    tiles(ax, 0.50, [("Fe", each, "?")] * n_fe, unit, x0)
    text(ax, x0 + 6 * unit + 0.10, 0.67, f"+{total}", 10, "bold", ha="left")
    text(ax, x0, 0.30, f"3  +{total} ÷ {n_fe} = +{each} on each Fe", 8, "bold", ACCENT, ha="left")
    text(ax, x0, 0.10, "Fe_{2}O_{3}  =  iron(III) oxide", 10, "bold", ha="left")
    save(fig, out)


def fig_acids(out):
    """6.6: acid names come from the anion's ending (deck slides 31, 33; A-5)."""
    rows = [("-ide", "hydro- + root + -ic acid", "chloride → hydrochloric acid"),
            ("-ate", "root + -ic acid", "nitrate → nitric acid"),
            ("-ite", "root + -ous acid", "nitrite → nitrous acid")]
    fig, ax = canvas(2.02)
    text(ax, 0.06, 1.92, "ANION ENDS IN", 8, "bold", ACCENT, ha="left")
    text(ax, 1.00, 1.92, "ACID NAME", 8, "bold", ACCENT, ha="left")
    h = 0.42
    for i, (end, rule, ex) in enumerate(rows):
        y = 1.36 - i * 0.52
        box(ax, 0.04, y, 0.62, h, color=INK, lw=1.0)
        text(ax, 0.35, y + h / 2, end, 10, "bold")
        arrow(ax, (0.70, y + h / 2), (0.94, y + h / 2))
        box(ax, 0.98, y, 1.98, h, color=DISPLAY, lw=1.3)
        text(ax, 1.06, y + h * 0.68, rule, 8.5, "bold", ha="left")
        text(ax, 1.06, y + h * 0.28, ex, 8, "regular", LABEL, ha="left")
    ax.plot([0.04, 2.96], [0.22, 0.22], color=HAIR, linewidth=0.6)
    text(ax, 0.06, 0.10, "Formula: one H^{+} for each negative charge on the anion.", 8, "regular", INK, ha="left")
    save(fig, out)


FIGS = {"fig6_1_co_co2.png": fig_co_co2, "fig6_2_sort.png": fig_sort, "fig6_3_ladder.png": fig_ladder,
        "fig6_4_al2o3.png": fig_al2o3, "fig6_5_fe2o3.png": fig_fe2o3, "fig6_6_acids.png": fig_acids}


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "build", "chem_u06_reading", "fig")
    os.makedirs(out, exist_ok=True)
    for name, fn in FIGS.items():
        fn(os.path.join(out, name))
        print("wrote", os.path.join(out, name))


if __name__ == "__main__":
    main()
