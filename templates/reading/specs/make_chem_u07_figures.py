#!/usr/bin/env python3
"""Figures 7.1-7.7 for the Chemistry U7 unit reading.

    python3 templates/reading/specs/make_chem_u07_figures.py OUT_DIR

Formulas, molar masses and percentages on the molecule figures (7.3, 7.5, 7.7) are
computed, not typed: element counts come from the RDKit molecule (or, for graphite and
sodium chloride, from the formula), and atomic masses from the student periodic table,
templates/reference/chem_data.py (2 decimals). Each computed value is checked against
the source dossier, reports/chem_u07_reading_dossier.md section B, and a
mismatch stops the build.

Molecules (Figures 7.5 and 7.7) are drawn by the shared builder,
scripts/build_diagram_molecule.py, with --explicit-h --label-carbons --no-caption
(SHULL-CHG-0042, SHULL-CHG-0115), and placed at one common scale. Its 2D layout draws
water near 120 degrees; Figure 7.5 is about atom count versus mass, so no angle is
labelled or claimed. RDKit is also used, without drawing, to count atoms from SMILES.

Print discipline (brand/SHULL_DESIGN_SYSTEM.md section 8): outlines and hatching only,
no tinted areas. Colour is read from brand/tokens.json; no hex is typed here.
Each figure is drawn for one column of the two-column reading (COL_IN wide) at 300 dpi.
"""
import io, json, os, sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
FONTS = os.path.join(REPO, "brand", "fonts")

DPI = 300
COL_IN = 3.50
W = int(COL_IN * DPI)


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


INK = rgb(T["ground"]["asphalt"]["hex"])
GRAPH = rgb(T["ground"]["graphite"]["hex"])
LABEL = rgb(T["ground"]["label"]["hex"])
HAIR = rgb(T["ground"]["ruleHairline"]["hex"])
WHITE = rgb(T["ground"]["white"]["hex"])
ACCENT = rgb(T["courses"]["chemistry"]["primaryDeep"]["hex"])   # type on white
DISPLAY = rgb(T["courses"]["chemistry"]["primary"]["hex"])      # rules only, never type

sys.path.insert(0, os.path.join(REPO, "templates", "reference"))
from chem_data import ELEMENTS                                    # noqa: E402
MASS = {sym: float(m) for _, sym, _, m in ELEMENTS if not m.startswith("[")}

# The verified values (dossier section B). A computed label must equal these.
BRIEF = {"C": 12.01, "H2O": 18.02, "NaCl": 58.44, "C2H2": 26.04, "C6H6": 78.12, "CH": 13.02,
         "H2O %H": 11.2, "H2O %O": 88.8}


def counts_of(smiles=None, formula=None):
    """{element: count} from a SMILES (RDKit, explicit H kept) or a plain formula."""
    import re as _re
    if smiles:
        from rdkit import Chem
        ps = Chem.SmilesParserParams(); ps.removeHs = False
        mol = Chem.MolFromSmiles(smiles, ps)
        out = {}
        for a in mol.GetAtoms():
            out[a.GetSymbol()] = out.get(a.GetSymbol(), 0) + 1
            if a.GetTotalNumHs():
                out["H"] = out.get("H", 0) + a.GetTotalNumHs()
        return out
    out = {}
    for sym, n in _re.findall(r"([A-Z][a-z]?)(\d*)", formula):
        out[sym] = out.get(sym, 0) + int(n or 1)
    return out


def molar_mass(counts):
    return round(sum(MASS[e] * n for e, n in counts.items()), 2)


def hill(counts, markup=True):
    """Formula in Hill order (C, H, then alphabetical); _{n} subscripts when markup."""
    keys = (["C", "H"] if "C" in counts else []) + sorted(k for k in counts if not ("C" in counts and k in "CH" and len(k) == 1))
    parts = []
    for k in keys:
        n = counts[k]
        parts.append(k + (("_{%d}" % n if markup else str(n)) if n > 1 else ""))
    return "".join(parts)


def check(key, value):
    if abs(value - BRIEF[key]) > 1e-9:
        sys.exit(f"figure value {key} = {value} disagrees with the verified brief ({BRIEF[key]})")
    return value


def pt(p):
    """Points to pixels at DPI: a 9 pt label is 9 pt when the figure is placed at COL_IN."""
    return int(round(p * DPI / 72))


def font(p, w="Regular"):
    return ImageFont.truetype(os.path.join(FONTS, f"Archivo-{w}.ttf"), pt(p))


def runs(text):
    """'C_{6}H_{12}O_{6} and 10^{23}' -> [(chunk, 0|-1|+1)] : 0 base, -1 sub, +1 sup."""
    out, i = [], 0
    while i < len(text):
        if text.startswith("_{", i) or text.startswith("^{", i):
            j = text.index("}", i)
            out.append((text[i + 2:j], -1 if text[i] == "_" else 1))
            i = j + 1
        else:
            j = i
            while j < len(text) and not (text.startswith("_{", j) or text.startswith("^{", j)):
                j += 1
            out.append((text[i:j], 0))
            i = j
    return out


def text_w(d, text, p, w="Regular"):
    f, fs = font(p, w), font(p * 0.68, w)
    return sum(d.textlength(c, font=fs if k else f) for c, k in runs(text))


def draw_text(d, xy, text, p, w="Regular", fill=INK, anchor="l"):
    """Text with sub/superscripts. anchor l / m / r on x; y is the top of the base line box."""
    x, y = xy
    tw = text_w(d, text, p, w)
    if anchor == "m":
        x -= tw / 2
    elif anchor == "r":
        x -= tw
    f, fs = font(p, w), font(p * 0.68, w)
    for c, k in runs(text):
        if k == 0:
            d.text((x, y), c, font=f, fill=fill)
            x += d.textlength(c, font=f)
        else:
            dy = pt(p) * 0.42 if k < 0 else -pt(p) * 0.12
            d.text((x, y + dy), c, font=fs, fill=fill)
            x += d.textlength(c, font=fs)
    return tw


def canvas(h_in):
    im = Image.new("RGB", (W, int(h_in * DPI)), WHITE)
    return im, ImageDraw.Draw(im)


def hatch(d, box, step=14, fill=GRAPH, width=2):
    """45-degree hatching clipped to a rectangle. Chart areas are hatched, not tinted."""
    x0, y0, x1, y1 = box
    h = y1 - y0
    k = x0 - h
    while k < x1:
        # line from (k, y1) to (k + h, y0), clipped to [x0, x1]
        ax, ay, bx, by = k, y1, k + h, y0
        if ax < x0:
            ay -= (x0 - ax); ax = x0
        if bx > x1:
            by += (bx - x1); bx = x1
        if bx > ax:
            d.line([(ax, ay), (bx, by)], fill=fill, width=width)
        k += step


def arrow(d, a, b, fill=INK, width=4, head=18):
    import math
    d.line([a, b], fill=fill, width=width)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    for s in (-1, 1):
        d.line([b, (b[0] - head * math.cos(ang + s * 0.45), b[1] - head * math.sin(ang + s * 0.45))],
               fill=fill, width=width)


MOL_SCALE = 0.30     # builder px -> figure px: its 136 px atom labels land at about 9.8 pt
MOLECULE_SCRIPT = os.path.join(REPO, "scripts", "build_diagram_molecule.py")


def molecule(smiles, expect):
    """A structure drawn by the shared builder, scripts/build_diagram_molecule.py
    (SHULL-CHG-0042), with every hydrogen and every carbon shown and no caption
    (SHULL-CHG-0115). The page captions it. Every molecule is placed at the same
    MOL_SCALE so atom labels match across figures. The builder prints the formula it
    drew; that must equal `expect`, the formula this figure labels."""
    import subprocess, tempfile, re as _re
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "m.png")
        r = subprocess.run([sys.executable, MOLECULE_SCRIPT, "--smiles", smiles, "--explicit-h",
                            "--label-carbons", "--no-caption", "--course", "chemistry",
                            "--out", out], check=True, capture_output=True, text=True)
        m = _re.search(r"\d+x\d+\s+(\S+)\s+[\d.]+ g/mol", r.stdout)
        if not m or m.group(1) != expect:
            sys.exit(f"molecule builder drew {m.group(1) if m else '?'} for {smiles!r}, expected {expect}")
        im = Image.open(out).convert("RGB")
        im.load()
    return im.resize((int(im.width * MOL_SCALE), int(im.height * MOL_SCALE)), Image.LANCZOS)


# ---------------------------------------------------------------------------------
def fig_rulers(out):
    """7.1: one pencil tip, two rulers. Tip at 4.63 cm: 4.6 on the cm ruler, 4.63 on the mm ruler."""
    im, d = canvas(1.68)
    x0, x1 = 60, W - 60
    cm = (x1 - x0) / 6.0
    tip = 4.63

    def panel(top, mm, title, reading, note):
        draw_text(d, (x0 - 36, top), title, 8.5, "Bold", LABEL)
        py = top + pt(14)
        # pencil: outline body, sharpened cone, graphite point at `tip`
        tx = x0 + tip * cm
        body_l = x0                     # the pencil starts at the zero mark (audit A-1)
        d.rectangle([body_l, py, tx - 70, py + 30], outline=INK, width=3)
        d.line([(body_l, py + 15), (tx - 70, py + 15)], fill=HAIR, width=2)
        d.polygon([(tx - 70, py), (tx, py + 15), (tx - 70, py + 30)], outline=INK, width=3)
        d.polygon([(tx - 22, py + 10), (tx, py + 15), (tx - 22, py + 20)], fill=INK)
        ry = py + 44
        d.rectangle([x0 - 36, ry, x1 + 36, ry + 80], outline=INK, width=3)
        for i in range(0, 61 if mm else 7):
            v = i / 10 if mm else i
            x = x0 + v * cm
            if mm and i % 10:
                ln = 30 if i % 5 == 0 else 20
                d.line([(x, ry), (x, ry + ln)], fill=INK, width=2)
            else:
                d.line([(x, ry), (x, ry + 40)], fill=INK, width=4)
                d.text((x, ry + 44), str(int(v)), font=font(8.5, "SemiBold"), fill=INK, anchor="ma")
        d.line([(tx, py + 15), (tx, ry + 80)], fill=ACCENT, width=2)
        draw_text(d, (x0 - 36, ry + 88), reading, 9, "Bold", INK)
        draw_text(d, (x0 - 36 + text_w(d, reading, 9, "Bold") + 18, ry + 88), note, 8.5, "Regular", LABEL)
        return ry + 88 + pt(12)

    y = panel(10, False, "CENTIMETER MARKS ONLY", "4.6 cm", "4 is certain, 6 is estimated")
    panel(y + 14, True, "CENTIMETER AND MILLIMETER MARKS", "4.63 cm", "4.6 is certain, 3 is estimated")
    im.save(out, dpi=(DPI, DPI))


def fig_ladder(out):
    """7.2: pair, dozen, mole as a staircase of counting words. (No ream: the dossier
    lists "ream = 500 sheets" as unsourced, section F.)"""
    rows = [("pair", "2", "shoes", 2), ("dozen", "12", "eggs", 12),
            ("mole", "6.022 × 10^{23}", "particles", "mole")]
    im, d = canvas(1.46)
    rh, gap = 128, 14
    for i, (word, num, what, icon) in enumerate(rows):
        y = 8 + i * (rh + gap)
        indent = i * 46
        box = [8 + indent, y, W - 8, y + rh]
        d.rectangle(box, outline=DISPLAY if word == "mole" else HAIR, width=5 if word == "mole" else 3)
        draw_text(d, (box[0] + 22, y + 18), word, 11, "Bold", INK)
        draw_text(d, (box[0] + 22, y + 18 + pt(14)), f"= {num}", 9.5, "SemiBold", ACCENT)
        ix = box[0] + 360
        cy = y + rh // 2
        if isinstance(icon, int):
            per = 6 if icon > 6 else icon
            for k in range(icon):
                cx = ix + (k % per) * 40
                yy = cy - 18 + (k // per) * 40 if icon > 6 else cy
                d.ellipse([cx - 14, yy - 14, cx + 14, yy + 14], outline=INK, width=3)
            draw_text(d, (ix + per * 40 + 10, cy - pt(5)), what, 8.5, "Regular", LABEL)
        elif icon is None:
            for k in range(7):
                d.line([(ix, cy - 30 + k * 10), (ix + 200, cy - 30 + k * 10)], fill=INK, width=2)
            draw_text(d, (ix + 220, cy - pt(5)), what, 8.5, "Regular", LABEL)
        else:
            for k in range(4):
                cx = ix + k * 40
                d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], outline=INK, width=3)
            draw_text(d, (ix + 4 * 40 - 10, cy - pt(6)), "…", 11, "Bold", INK)
            draw_text(d, (ix + 4 * 40 + 62, cy - pt(5)), "atoms, molecules,", 8.5, "Regular", LABEL)
            draw_text(d, (ix + 4 * 40 + 62, cy - pt(5) + pt(11)), "or formula units", 8.5, "Regular", LABEL)
    im.save(out, dpi=(DPI, DPI))


def fig_one_mole(out):
    """7.3: one mole of carbon, water, sodium chloride. Values from the student table."""
    im, d = canvas(1.62)
    mc = check("C", molar_mass(counts_of(formula="C")))
    mw = check("H2O", molar_mass(counts_of(smiles="O")))
    ms = check("NaCl", molar_mass(counts_of(formula="NaCl")))
    cols = [("Carbon", "(graphite)", f"{mc:.2f} g", None, "atoms"),
            ("Water", "", f"{mw:.2f} g", "about 18 mL", "molecules"),
            ("Sodium chloride", "(table salt)", f"{ms:.2f} g", None, "formula units")]
    cw = W / 3
    base = 180
    for i, (name, sub, mass, extra, part) in enumerate(cols):
        cx = cw * i + cw / 2
        if i == 0:     # a lump of graphite: outlined, hatched
            pts = [(cx - 70, base), (cx - 85, base - 50), (cx - 40, base - 95), (cx + 30, base - 88),
                   (cx + 80, base - 45), (cx + 70, base)]
            d.polygon(pts, outline=INK, width=4)
            hatch_poly = Image.new("L", im.size, 0)
            ImageDraw.Draw(hatch_poly).polygon(pts, fill=255)
            layer = Image.new("RGB", im.size, WHITE)
            hatch(ImageDraw.Draw(layer), (cx - 90, base - 100, cx + 90, base), step=16)
            im.paste(layer, (0, 0), hatch_poly)
            d.polygon(pts, outline=INK, width=4)
        elif i == 1:   # a beaker with ~18 mL of water: outlined glass, hatched liquid
            bl, br, top = cx - 60, cx + 60, base - 150
            d.line([(bl, top), (bl, base), (br, base), (br, top)], fill=INK, width=4)
            d.line([(bl - 12, top), (bl, top)], fill=INK, width=4)
            lvl = base - 62
            hatch(d, (bl + 3, lvl, br - 3, base - 3), step=16)
            d.line([(bl, lvl), (br, lvl)], fill=INK, width=3)
        else:          # a small pile of salt crystals: outlined squares
            s = 26
            for row, n in enumerate((5, 4, 3, 2)):
                for k in range(n):
                    x = cx - n * s / 2 + k * s
                    y = base - (row + 1) * s
                    d.rectangle([x, y, x + s - 4, y + s - 4], outline=INK, width=3)
        d.line([(cx - cw / 2 + 20, base + 6), (cx + cw / 2 - 20, base + 6)], fill=HAIR, width=3)
        y = base + 22
        draw_text(d, (cx, y), name, 9, "Bold", INK, "m"); y += pt(11.5)
        if sub:
            draw_text(d, (cx, y), sub, 8, "Regular", LABEL, "m")
        y += pt(11)
        draw_text(d, (cx, y), mass, 10.5, "Bold", ACCENT, "m"); y += pt(13)
        if extra:
            draw_text(d, (cx, y), f"({extra})", 8, "Regular", LABEL, "m")
        y += pt(11)
        draw_text(d, (cx, y), "6.022 × 10^{23}", 8.5, "SemiBold", INK, "m"); y += pt(11)
        draw_text(d, (cx, y), part, 8.5, "Regular", INK, "m")
    im.save(out, dpi=(DPI, DPI))


def fig_map(out):
    """7.4: GRAMS - MOLES - PARTICLES, labels and arrows only (the factors are the
    worksheet's fill-in; the text supplies them)."""
    im, d = canvas(1.02)
    bw, bh, y = 276, 120, 150
    xs = [6, (W - bw) / 2, W - 6 - bw]
    names = [("GRAMS", "(g)"), ("MOLES", "(mol)"), ("PARTICLES", "(count)")]
    for x, (n, u) in zip(xs, names):
        mole = n == "MOLES"
        d.rectangle([x, y, x + bw, y + bh], outline=DISPLAY if mole else INK, width=7 if mole else 4)
        draw_text(d, (x + bw / 2, y + 22), n, 9.5, "Bold", INK, "m")
        draw_text(d, (x + bw / 2, y + 22 + pt(13)), u, 8.5, "Regular", LABEL, "m")
    for a, b in ((0, 1), (1, 2)):
        l, r = xs[a] + bw + 12, xs[b] - 12
        arrow(d, (l, y + 42), (r, y + 42))
        arrow(d, (r, y + bh - 42), (l, y + bh - 42))
    # the path that does not exist: a dashed arc over the top, crossed out
    lx, rx = xs[0] + bw / 2, xs[2] + bw / 2
    top = 66
    import math
    pts = []
    for k in range(0, 41):
        t = k / 40
        pts.append((lx + (rx - lx) * t, y - 8 - (y - 8 - top) * math.sin(math.pi * t)))
    for k in range(0, 40, 2):
        d.line([pts[k], pts[k + 1]], fill=LABEL, width=3)
    mx, my = (lx + rx) / 2, top
    d.line([(mx - 16, my - 16), (mx + 16, my + 16)], fill=INK, width=5)
    d.line([(mx - 16, my + 16), (mx + 16, my - 16)], fill=INK, width=5)
    draw_text(d, (mx, 2), "no direct path", 8, "Regular", LABEL, "m")
    im.save(out, dpi=(DPI, DPI))


def fig_water_percent(out):
    """7.5: water by atom count (2 of 3 = 67 % H) vs by mass (11.2 % H, 88.8 % O)."""
    mol = molecule("O", "H2O")
    im, d = canvas(round((mol.height + 30) / DPI + 1.42, 2))
    im.paste(mol, (int((W - mol.width) / 2), 0))
    top = mol.height + 30
    x0, x1 = 30, W - 30
    bh = 74

    def bar(y, label, parts):
        draw_text(d, (x0, y), label, 8.5, "Bold", LABEL)
        y += pt(12)
        x = x0
        for name, frac, txt in parts:
            w = (x1 - x0) * frac
            box = (x, y, x + w, y + bh)
            if name == "O":
                hatch(d, (x + 2, y + 2, x + w - 2, y + bh - 2), step=18, fill=HAIR, width=3)
            d.rectangle(box, outline=INK, width=4 if name == "O" else 3)
            tw = text_w(d, txt, 8.5, "Bold")
            if w > tw + 16:
                # a white plate behind the label keeps it legible over the hatching
                cx = x + w / 2
                d.rectangle([cx - tw / 2 - 8, y + bh / 2 - pt(6), cx + tw / 2 + 8, y + bh / 2 + pt(6)],
                            fill=WHITE)
                draw_text(d, (cx, y + bh / 2 - pt(5)), txt, 8.5, "Bold", INK, "m")
            else:
                draw_text(d, (x + w / 2, y + bh + 8), txt, 8.5, "Bold", INK, "m")
            x += w
        return y + bh

    c = counts_of(smiles="O")
    total = molar_mass(c)
    ph = check("H2O %H", round(100 * c["H"] * MASS["H"] / total, 1))
    po = check("H2O %O", round(100 * c["O"] * MASS["O"] / total, 1))
    n_atoms = sum(c.values())
    y = bar(top, "BY NUMBER OF ATOMS", [("H", 1 / n_atoms, "H")] * c["H"] + [("O", 1 / n_atoms, "O")] * c["O"])
    draw_text(d, (x1, y + 6), f"{c['H']} of {n_atoms} atoms are H ({round(100 * c['H'] / n_atoms)}%)",
              8, "Regular", LABEL, "r")
    y = bar(y + 60, "BY MASS", [("H", ph / 100, "H"), ("O", po / 100, f"O  {po:.1f}%")])
    draw_text(d, (x0 + (x1 - x0) * ph / 100 + 14, y + 6), f"H  {ph:.1f}%", 8.5, "Bold", INK)
    im.save(out, dpi=(DPI, DPI))


def fig_reduce(out):
    """7.6: C6H12O6 reduces to CH2O; glucose, acetic acid and formaldehyde share it."""
    im, d = canvas(2.02)
    y = 20
    draw_text(d, (W * 0.22, y), "C_{6}H_{12}O_{6}", 15, "Bold", INK, "m")
    arrow(d, (W * 0.42, y + pt(9)), (W * 0.60, y + pt(9)), width=4)
    draw_text(d, (W * 0.51, y + pt(9) + 10), "divide every", 8, "Regular", LABEL, "m")
    draw_text(d, (W * 0.51, y + pt(9) + 10 + pt(10)), "subscript by 6", 8, "Regular", LABEL, "m")
    draw_text(d, (W * 0.80, y), "CH_{2}O", 15, "Bold", ACCENT, "m")
    d.line([(20, 175), (W - 20, 175)], fill=HAIR, width=3)
    bw = (W - 80) / 3
    items = [("glucose", "C_{6}H_{12}O_{6}"), ("acetic acid", "C_{2}H_{4}O_{2}"), ("formaldehyde", "CH_{2}O")]
    by = 200
    for i, (n, f) in enumerate(items):
        x = 20 + i * (bw + 20)
        d.rectangle([x, by, x + bw, by + 120], outline=INK, width=3)
        draw_text(d, (x + bw / 2, by + 16), n, 8.5, "Regular", LABEL, "m")
        draw_text(d, (x + bw / 2, by + 16 + pt(12)), f, 11, "Bold", INK, "m")
        arrow(d, (x + bw / 2, by + 128), (W / 2 + (i - 1) * 60, by + 228), width=3, head=16)
    tb = [W / 2 - 150, by + 236, W / 2 + 150, by + 372]
    d.rectangle(tb, outline=DISPLAY, width=6)
    draw_text(d, (W / 2, tb[1] + 12), "empirical formula", 8, "Regular", LABEL, "m")
    draw_text(d, (W / 2, tb[1] + 12 + pt(11)), "CH_{2}O", 12, "Bold", INK, "m")
    im.save(out, dpi=(DPI, DPI))


def fig_ch(out):
    """7.7: acetylene and benzene share empirical formula CH (13.02 g/mol). Stacked, so
    acetylene, which the builder lays out long and flat, can use the full column at the
    common molecule scale."""
    import math
    smiles = {"Acetylene": ("C#C", "C2H2"), "Benzene": ("c1ccccc1", "C6H6")}
    data, pics = {}, {}
    for name, (smi, f) in smiles.items():
        c = counts_of(smiles=smi)
        g = math.gcd(*c.values())
        emp = {e: n // g for e, n in c.items()}
        data[name] = (c, molar_mass(c), emp, molar_mass(emp), g)
        pics[name] = molecule(smi, f)
    (ca, ma, ea, mea, ga), (cb, mb, eb, meb, gb) = data["Acetylene"], data["Benzene"]
    if ea != eb:
        sys.exit("figure 7.7: the two molecules do not share an empirical formula")
    check("C2H2", ma); check("C6H6", mb); check("CH", mea)
    a, b = pics["Acetylene"], pics["Benzene"]
    if a.width > W - 20:
        sys.exit(f"figure 7.7: acetylene is {a.width} px, wider than the column")
    h = 100 + 26 + a.height + pt(30) + 24 + b.height + 10
    im, d = canvas(h / DPI)
    d.rectangle([20, 6, W - 20, 96], outline=DISPLAY, width=6)
    draw_text(d, (W / 2, 6 + 26), f"Empirical formula of both:  {hill(ea)},  {mea:.2f} g/mol",
              9.5, "Bold", INK, "m")

    def caption(x, y, name, anchor):
        c, m, emp, me, g = data[name]
        draw_text(d, (x, y), f"{name}, {hill(c)}", 9.5, "Bold", INK, anchor)
        draw_text(d, (x, y + pt(13)), f"{m:.2f} g/mol", 9.5, "Bold", ACCENT, anchor)
        draw_text(d, (x, y + pt(25)), f"= {g} × {me:.2f}", 8.5, "Regular", LABEL, anchor)

    y = 126
    im.paste(a, (int((W - a.width) / 2), y))
    y += a.height + 8
    draw_text(d, (W / 2, y), f"Acetylene, {hill(ca)}   ", 9.5, "Bold", INK, "r")
    draw_text(d, (W / 2, y), f"{ma:.2f} g/mol = {ga} × {mea:.2f}", 9.5, "Bold", ACCENT, "l")
    y += pt(16)
    d.line([(20, y), (W - 20, y)], fill=HAIR, width=3)
    y += 24
    im.paste(b, (10, y))
    caption(b.width + 60, y + b.height / 2 - pt(18), "Benzene", "l")
    im.save(out, dpi=(DPI, DPI))


FIGS = {"fig7_1_rulers.png": fig_rulers, "fig7_2_ladder.png": fig_ladder,
        "fig7_3_one_mole.png": fig_one_mole, "fig7_4_map.png": fig_map,
        "fig7_5_water_percent.png": fig_water_percent, "fig7_6_reduce.png": fig_reduce,
        "fig7_7_ch.png": fig_ch}


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "build", "chem_u07_reading", "fig")
    os.makedirs(out, exist_ok=True)
    for name, fn in FIGS.items():
        fn(os.path.join(out, name))
        print("wrote", os.path.join(out, name))


if __name__ == "__main__":
    main()
