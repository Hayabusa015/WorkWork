#!/usr/bin/env python3
"""Draw the seven hand-built figures for CHEM U02 S2.4 (Electron Stability & Valence Electrons).

Hand-built, not generated. Every figure here carries electron counts, and a generated
one would have a plausible-looking wrong count that nobody catches at a glance. Each
figure is defined from data and every count shown is re-added by an assertion BEFORE
anything is drawn: if a configuration does not sum to Z minus the charge, this script
stops and writes nothing.

Colours come from brand/tokens.json. Type comes from the shipped Archivo files.
Canvas is 1010 x 600 logical px, the same aspect as layout 08's diagram slot
(5.05 x 3.00 in), so one logical px = 0.005 in and 16 pt = 44.4 px. Nothing is set
below 46 px, so every label clears the 16 pt floor at projected size.

Charge signs: drawn with a stroke (the bare superscript minus is a hairline); charge
columns are set large and plain, e.g. 2\u2212.
Notation in the figures: filling order, e.g. [Ar] 4s2 3d6, with true superscripts.

    python3 scripts/build_diagram_u02_s02.4_stability_valence_ions.py
"""
import json, os, re, sys
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(REPO, "templates", "slide", "assets")
SCALE = 4
W, H = 1010, 600
MIN_PX = 46          # 16 pt at 200 px/in


def tokens():
    t = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
    g = t["ground"]
    return dict(white=g["white"]["hex"], asphalt=g["asphalt"]["hex"], graphite=g["graphite"]["hex"],
                rule=g["ruleHairline"]["hex"], accent=t["courses"]["chemistry"]["primaryDeep"]["hex"])


C = tokens()
_fonts = {}


def font(name, px):
    assert px >= MIN_PX, f"{px}px is under the 16 pt floor ({MIN_PX}px)"
    key = (name, px)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(os.path.join(REPO, "brand", "fonts", name), int(px * SCALE))
    return _fonts[key]


S = SCALE


class Canvas:
    def __init__(self):
        self.im = Image.new("RGB", (W * S, H * S), C["white"])
        self.d = ImageDraw.Draw(self.im)

    # ---- text with ^{...} superscripts; x,y is the baseline start (anchor 'ls') ----
    def runs(self, text):
        out = []
        for part in re.split(r"(\^[^\s^]+)", text):
            if not part:
                continue
            out.append((part[1:].replace("-", "\u2212"), True) if part.startswith("^") else (part, False))
        return out

    def width(self, text, face, px):
        f = font(face, px)
        total = 0
        for s, sup in self.runs(text):
            total += self.d.textlength(s, font=f if not sup else font(face, max(MIN_PX, int(px * 0.66))))
        return total / S

    def text(self, x, y, text, face="Archivo-SemiBold.ttf", px=56, fill=None, align="l"):
        fill = fill or C["asphalt"]
        w = self.width(text, face, px)
        if align == "c":
            x -= w / 2
        elif align == "r":
            x -= w
        for s, sup in self.runs(text):
            if sup:
                spx = max(MIN_PX, int(px * 0.66))
                f = font(face, spx)
                # charge signs get a stroke: the bare superscript minus is a hairline
                sw = int(S * 1.6) if any(c in s for c in "+\u2212") else 0
                self.d.text((x * S, (y - px * 0.36) * S), s, font=f, fill=fill, anchor="ls",
                            stroke_width=sw, stroke_fill=fill)
                x += self.d.textlength(s, font=f) / S
            else:
                f = font(face, px)
                self.d.text((x * S, y * S), s, font=f, fill=fill, anchor="ls")
                x += self.d.textlength(s, font=f) / S
        return x

    def line(self, x1, y1, x2, y2, fill, w=2):
        self.d.line([(x1 * S, y1 * S), (x2 * S, y2 * S)], fill=fill, width=int(w * S))

    def rect(self, x, y, w, h, outline, width=3, dashed=False):
        if not dashed:
            self.d.rectangle([x * S, y * S, (x + w) * S, (y + h) * S], outline=outline, width=int(width * S))
            return
        seg, gap = 14, 9
        for (ax, ay, bx, by) in [(x, y, x + w, y), (x + w, y, x + w, y + h),
                                 (x + w, y + h, x, y + h), (x, y + h, x, y)]:
            L = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
            ux, uy = (bx - ax) / L, (by - ay) / L
            t = 0
            while t < L:
                e = min(t + seg, L)
                self.line(ax + ux * t, ay + uy * t, ax + ux * e, ay + uy * e, outline, width)
                t += seg + gap

    def arrow(self, cx, top, bot, up, fill):
        """Electron spin arrow in a box. up=True points up."""
        self.line(cx, top, cx, bot, fill, 5)
        head = 15
        if up:
            pts = [(cx, top - 4), (cx - head * 0.7, top + head), (cx + head * 0.7, top + head)]
        else:
            pts = [(cx, bot + 4), (cx - head * 0.7, bot - head), (cx + head * 0.7, bot - head)]
        self.d.polygon([(px * S, py * S) for px, py in pts], fill=fill)

    def box(self, x, y, size, electrons, outline, width=3, dashed=False, ink=None, down_ink=None):
        """One orbital box holding 0, 1 or 2 electrons. Returns the count drawn."""
        ink = ink or C["asphalt"]
        self.rect(x, y, size, size, outline, width, dashed)
        top, bot = y + 16, y + size - 16
        if electrons == 2:
            self.arrow(x + size * 0.33, top, bot, True, ink)
            self.arrow(x + size * 0.67, top, bot, False, down_ink or ink)
        elif electrons == 1:
            self.arrow(x + size * 0.5, top, bot, True, ink)
        return electrons

    def save(self, name):
        os.makedirs(ASSETS, exist_ok=True)
        path = os.path.join(ASSETS, name)
        self.im.save(path)
        print(f"wrote {os.path.relpath(path, REPO)}  {self.im.width}x{self.im.height}")


def total_e(parts, core_z=0):
    return core_z + sum(n for _, n in parts)


# ---------------------------------------------------------------- A: core vs valence, Cl
def fig_core_valence():
    Z = 17
    core = [("1s", 2), ("2s", 2), ("2p", 6)]
    val = [("3s", 2), ("3p", 5)]
    nc, nv = sum(n for _, n in core), sum(n for _, n in val)
    assert nc == 10 and nv == 7 and nc + nv == Z, (nc, nv)
    # valence = everything in the highest n
    assert all(s[0] == "3" for s, _ in val) and all(s[0] != "3" for s, _ in core)

    cv = Canvas()
    f, px = "Archivo-Bold.ttf", 58
    cfg = lambda parts: "  ".join(f"{s}^{n}" for s, n in parts)
    core_txt, val_txt = cfg(core), cfg(val)
    gap = 44
    wc, wv = cv.width(core_txt, f, px), cv.width(val_txt, f, px)
    label_w = cv.width("Cl", f, px) + 34
    x0 = (W - (label_w + wc + gap + wv)) / 2
    y = 190
    cv.text(x0, y, "Cl", f, px)
    xc = x0 + label_w
    xv = xc + wc + gap
    cv.text(xc, y, core_txt, f, px)
    cv.text(xv, y, val_txt, f, px, fill=C["accent"])

    def bracket(x1, x2, colour):
        yb = y + 34
        cv.line(x1, yb, x2, yb, colour, 4)
        cv.line(x1, yb - 14, x1, yb, colour, 4)
        cv.line(x2, yb - 14, x2, yb, colour, 4)
        return yb

    bracket(xc, xc + wc, C["graphite"])
    bracket(xv, xv + wv, C["accent"])
    cv.text(xc + wc / 2, y + 112, "CORE", "Archivo-SemiBold.ttf", 52, C["graphite"], "c")
    cv.text(xc + wc / 2, y + 168, f"{nc} electrons", "Archivo-SemiBold.ttf", 50, C["graphite"], "c")
    cv.text(xv + wv / 2, y + 112, "VALENCE", "Archivo-SemiBold.ttf", 52, C["accent"], "c")
    cv.text(xv + wv / 2, y + 168, f"{nv} electrons", "Archivo-SemiBold.ttf", 50, C["accent"], "c")
    cv.line(150, 440, W - 150, 440, C["rule"], 2)
    cv.text(W / 2, 520, f"{nc} + {nv} = {Z}", "Archivo-Bold.ttf", 64, C["asphalt"], "c")
    cv.save("chem_u02_s2.4_core_valence_cl.png")


# ---------------------------------------------------------------- B: valence from group
def fig_valence_by_group():
    # period 3, main group: (group, symbol, valence)
    cols = [(1, "Na", 1), (2, "Mg", 2), (13, "Al", 3), (14, "Si", 4),
            (15, "P", 5), (16, "S", 6), (17, "Cl", 7), (18, "Ar", 8)]
    for g, _, v in cols:
        assert v == (g if g <= 2 else g - 10), (g, v)
    assert [v for _, _, v in cols] == list(range(1, 9))
    # He check, kept separate on purpose: group 18 but 2, not 8
    He_valence = 2
    assert He_valence == 2

    cv = Canvas()
    x_lab, cw = 20, 100
    x0 = 205
    rows = [("Group", 90, "Archivo-SemiBold.ttf", 50, C["graphite"]),
            ("Atom", 210, "Archivo-Bold.ttf", 60, C["asphalt"]),
            ("Valence", 330, "Archivo-Bold.ttf", 66, C["accent"])]
    for lab, y, face, px, colr in rows:
        cv.text(x_lab, y, lab, "Archivo-SemiBold.ttf", 50, C["graphite"])
    for i, (g, sym, v) in enumerate(cols):
        cx = x0 + cw * i + cw / 2
        cv.text(cx, 90, str(g), "Archivo-SemiBold.ttf", 52, C["graphite"], "c")
        cv.text(cx, 210, sym, "Archivo-Bold.ttf", 54, C["asphalt"], "c")
        cv.text(cx, 330, str(v), "Archivo-Bold.ttf", 66, C["accent"], "c")
    cv.line(x_lab, 125, W - 20, 125, C["rule"], 2)
    cv.line(x_lab, 245, W - 20, 245, C["rule"], 2)
    # gap marker between group 2 and 13 (groups 3 to 12 are not shown)
    gx = x0 + cw * 2
    cv.line(gx, 45, gx, 360, C["rule"], 2)
    cv.line(x_lab, 405, W - 20, 405, C["graphite"], 2)
    cv.text(W / 2, 480, "Helium: group 18, but 2 valence electrons", "Archivo-Bold.ttf", 48, C["asphalt"], "c")
    cv.text(W / 2, 550, "Period 3 shown. Groups 3 to 12 skipped.", "Archivo-SemiBold.ttf", 46, C["graphite"], "c")
    cv.save("chem_u02_s2.4_valence_by_group.png")


# ---------------------------------------------------------------- C: noble gas configurations
def fig_noble_gas():
    Z = {"He": 2, "Ne": 10, "Ar": 18, "Kr": 36}
    # (symbol, core shorthand, core electron count, [(sublevel, n)])
    rows = [("He", "", 0, [("1s", 2)]),
            ("Ne", "[He]", 2, [("2s", 2), ("2p", 6)]),
            ("Ar", "[Ne]", 10, [("3s", 2), ("3p", 6)]),
            ("Kr", "[Ar]", 18, [("4s", 2), ("3d", 10), ("4p", 6)])]
    outer_sp = {}
    for sym, _, cz, parts in rows:
        assert cz + sum(n for _, n in parts) == Z[sym], sym
        top_n = max(int(s[0]) for s, _ in parts)
        outer_sp[sym] = sum(n for s, n in parts if s[1] in "sp" and int(s[0]) == top_n)
    assert outer_sp == {"He": 2, "Ne": 8, "Ar": 8, "Kr": 8}, outer_sp

    cv = Canvas()
    cv.text(985, 70, "Outer s, p", "Archivo-SemiBold.ttf", 46, C["graphite"], "r")
    cv.line(20, 95, W - 20, 95, C["rule"], 2)
    for i, (sym, short, cz, parts) in enumerate(rows):
        y = 175 + i * 125
        cv.text(25, y, sym, "Archivo-Bold.ttf", 60, C["asphalt"])
        txt = ((short + " ") if short else "") + "  ".join(f"{s}^{n}" for s, n in parts)
        cv.text(135, y, txt, "Archivo-SemiBold.ttf", 54, C["asphalt"])
        cv.text(930, y, str(outer_sp[sym]), "Archivo-Bold.ttf", 64, C["accent"], "c")
        if i < 3:
            cv.line(20, y + 40, W - 20, y + 40, C["rule"], 1)
    cv.save("chem_u02_s2.4_noble_gas_configs.png")


# ---------------------------------------------------------------- orbital-row helper
def orbital_row(cv, y, label, groups, size=90, x_label=20, x_start=150, gap=22, dashed_idx=(),
                accent_idx=(), added_down=None):
    """groups = list of (sublevel label, [electron count per box]). Returns electrons drawn."""
    x = x_start
    n = 0
    i = 0
    for _, boxes in groups:
        for e in boxes:
            dashed = i in dashed_idx
            acc = i in accent_idx
            outline = C["accent"] if (dashed or acc) else C["graphite"]
            ink = C["asphalt"]
            down = C["accent"] if (added_down == i) else ink
            n += cv.box(x, y, size, e, outline, 5 if acc else 3, dashed, ink, down)
            x += size
            i += 1
        x += gap
    return n


def group_x(groups, size=90, x_start=150, gap=22):
    """x centre of each group, for the sublevel header labels."""
    xs, x = [], x_start
    for _, boxes in groups:
        w = size * len(boxes)
        xs.append(x + w / 2)
        x += w + gap
    return xs


# ---------------------------------------------------------------- D: Na -> Na+ and Cl -> Cl-
def fig_na_cl_ions():
    na = [("2s", [2]), ("2p", [2, 2, 2]), ("3s", [1])]
    na_ion = [("2s", [2]), ("2p", [2, 2, 2]), ("3s", [0])]
    cl = [("3s", [2]), ("3p", [2, 2, 1])]
    cl_ion = [("3s", [2]), ("3p", [2, 2, 2])]
    cnt = lambda g: sum(sum(b) for _, b in g)
    core = 2                                   # 1s2 not drawn (Na rows); Cl rows also omit n=1,2 (10)
    assert core + cnt(na) == 11 and core + cnt(na_ion) == 10 == 11 - 1
    assert 10 + cnt(cl) == 17 and 10 + cnt(cl_ion) == 18 == 17 - (-1)
    assert cnt(na_ion) == cnt(na) - 1 and cnt(cl_ion) == cnt(cl) + 1

    cv = Canvas()
    size, gap, xs0 = 70, 14, 170
    def header(y):
        cv.text(700, y, "Electrons", "Archivo-SemiBold.ttf", 46, C["graphite"], "c")
        cv.text(900, y, "Charge", "Archivo-SemiBold.ttf", 46, C["graphite"], "c")
    # pair A: sodium
    for (lab, _), cx in zip(na, group_x(na, size=size, x_start=xs0, gap=gap)):
        cv.text(cx, 48, lab, "Archivo-SemiBold.ttf", 46, C["graphite"], "c")
    header(48)
    yA1, yA2 = 66, 150
    cv.text(20, yA1 + 52, "Na", "Archivo-Bold.ttf", 54)
    cv.text(20, yA2 + 52, "Na^+", "Archivo-Bold.ttf", 54)
    orbital_row(cv, yA1, "Na", na, size=size, gap=gap, x_start=xs0, accent_idx=(4,))
    orbital_row(cv, yA2, "Na+", na_ion, size=size, gap=gap, x_start=xs0, dashed_idx=(4,))
    for y, e, q in ((yA1, 11, "0"), (yA2, 10, "1+")):
        cv.text(700, y + 52, str(e), "Archivo-Bold.ttf", 58, C["accent"], "c")
        cv.text(900, y + 52, q, "Archivo-Bold.ttf", 62, C["asphalt"], "c")
    cv.line(20, 250, W - 20, 250, C["rule"], 2)
    # pair B: chlorine
    for (lab, _), cx in zip(cl, group_x(cl, size=size, x_start=xs0, gap=gap)):
        cv.text(cx, 308, lab, "Archivo-SemiBold.ttf", 46, C["graphite"], "c")
    header(308)
    yB1, yB2 = 326, 410
    cv.text(20, yB1 + 52, "Cl", "Archivo-Bold.ttf", 54)
    cv.text(20, yB2 + 52, "Cl^-", "Archivo-Bold.ttf", 54)
    orbital_row(cv, yB1, "Cl", cl, size=size, gap=gap, x_start=xs0)
    orbital_row(cv, yB2, "Cl-", cl_ion, size=size, gap=gap, x_start=xs0, accent_idx=(3,), added_down=3)
    for y, e, q in ((yB1, 17, "0"), (yB2, 18, "1\u2212")):
        cv.text(700, y + 52, str(e), "Archivo-Bold.ttf", 58, C["accent"], "c")
        cv.text(900, y + 52, q, "Archivo-Bold.ttf", 62, C["asphalt"], "c")
    cv.line(20, 505, W - 20, 505, C["rule"], 2)
    cv.text(W / 2, 570, "11 \u2212 1 = 10          17 + 1 = 18", "Archivo-Bold.ttf", 54, C["asphalt"], "c")
    cv.save("chem_u02_s2.4_na_cl_ions.png")


# ---------------------------------------------------------------- D2: charge from valence electrons
def fig_charge_by_group():
    NOBLE_Z = {"He": 2, "Ne": 10, "Ar": 18, "Kr": 36}
    # (group, atom, Z, valence, move, charge); move < 0 lose, > 0 gain, None = not predicted here
    rows = [(1, "Na", 11, 1, -1, 1), (2, "Mg", 12, 2, -2, 2), (13, "Al", 13, 3, -3, 3),
            (14, "Si", 14, 4, None, None),
            (15, "P", 15, 5, 3, -3), (16, "S", 16, 6, 2, -2), (17, "Cl", 17, 7, 1, -1),
            (18, "Ar", 18, 8, 0, 0)]
    for g, sym, z, v, mv, q in rows:
        assert v == (g if g <= 2 else g - 10), (g, v)
        if mv is None:
            assert g == 14 and v == 4 and 8 - v == v      # 4 lost or 4 gained: no 'fewest'
            continue
        if g in (1, 2, 13):
            assert mv == -v and q == v                    # lose all valence electrons
        elif g in (15, 16, 17):
            assert mv == 8 - v and q == -(8 - v)          # gain up to 8
        else:
            assert mv == 0 and q == 0
        assert z - q in (10, 18)                          # ends at [Ne] or [Ar]
    # the concept-slide and worked-example ions, re-added from Z
    assert 20 - 2 == NOBLE_Z["Ar"]                        # Ca 2+ -> [Ar]
    assert 20 - 2 == 18 and 20 == 18 + 2
    assert 12 - 2 == NOBLE_Z["Ne"] and 13 - 3 == NOBLE_Z["Ne"]   # Mg2+, Al3+ -> [Ne]
    assert 16 + 2 == NOBLE_Z["Ar"] and 35 + 1 == NOBLE_Z["Kr"]   # S2-, Br- -> [Ar], [Kr]
    assert 8 + 2 == NOBLE_Z["Ne"] and 19 - 1 == NOBLE_Z["Ar"] and 34 + 2 == NOBLE_Z["Kr"]  # O2-, K+, Se2-

    cv = Canvas()
    hd = "Archivo-SemiBold.ttf"
    for x, t, al in ((85, "Group", "c"), (225, "Atom", "c"), (385, "Valence", "c"),
                     (520, "Move", "l"), (900, "Charge", "c")):
        cv.text(x, 52, t, hd, 46, C["graphite"], al)
    cv.line(20, 70, W - 20, 70, C["graphite"], 2)
    for i, (g, sym, z, v, mv, q) in enumerate(rows):
        y = 130 + 62 * i
        ink = C["graphite"] if mv is None else C["asphalt"]
        cv.text(85, y, str(g), "Archivo-Bold.ttf", 54, ink, "c")
        cv.text(225, y, sym, "Archivo-Bold.ttf", 54, ink, "c")
        cv.text(385, y, str(v), "Archivo-Bold.ttf", 56, C["accent"], "c")
        if mv is None:
            move, charge = "not predicted", "\u2014"
        elif mv < 0:
            move, charge = f"lose {-mv}", f"{q}+"
        elif mv > 0:
            move, charge = f"gain {mv}", f"{-q}\u2212"
        else:
            move, charge = "none", "0"
        cv.text(520, y, move, hd, 52, ink)
        cv.text(900, y, charge, "Archivo-Bold.ttf", 60, ink, "c")
        if i < len(rows) - 1 and g not in (13, 14):
            cv.line(20, y + 14, W - 20, y + 14, C["rule"], 1)
    y14 = 130 + 62 * 3
    cv.rect(20, y14 - 46, W - 40, 62, C["graphite"], 2, dashed=True)
    cv.save("chem_u02_s2.4_charge_by_group.png")


# ---------------------------------------------------------------- E: isoelectronic
def fig_isoelectronic():
    # (symbol markup, protons, charge)
    sp = [("O^2-", 8, -2), ("F^-", 9, -1), ("Ne", 10, 0), ("Na^+", 11, 1), ("Mg^2+", 12, 2), ("Al^3+", 13, 3)]
    for s, p, q in sp:
        assert p - q == 10, s            # electrons = protons - charge
    cv = Canvas()
    cw = (W - 40) / 6
    for i, (s, p, q) in enumerate(sp):
        cx = 20 + cw * i + cw / 2
        cv.text(cx, 130, s, "Archivo-Bold.ttf", 62, C["asphalt"], "c")
        cv.text(cx, 290, f"{p} p", "Archivo-SemiBold.ttf", 54, C["asphalt"], "c")
        cv.text(cx, 420, f"{p - q} e", "Archivo-Bold.ttf", 58, C["accent"], "c")
        if i:
            cv.line(20 + cw * i, 60, 20 + cw * i, 460, C["rule"], 1)
    cv.line(20, 190, W - 20, 190, C["rule"], 2)
    cv.line(20, 340, W - 20, 340, C["rule"], 2)
    cv.text(W / 2, 540, "p = protons      e = electrons", "Archivo-SemiBold.ttf", 48, C["graphite"], "c")
    cv.save("chem_u02_s2.4_isoelectronic_10.png")


# ---------------------------------------------------------------- F: iron and its ions
def fig_fe_ions():
    fe = [("4s", [2]), ("3d", [2, 1, 1, 1, 1])]
    fe2 = [("4s", [0]), ("3d", [2, 1, 1, 1, 1])]
    fe3 = [("4s", [0]), ("3d", [1, 1, 1, 1, 1])]
    cnt = lambda g: sum(sum(b) for _, b in g)
    assert (cnt(fe), cnt(fe2), cnt(fe3)) == (8, 6, 5)
    assert 18 + cnt(fe) == 26 and 18 + cnt(fe2) == 24 == 26 - 2 and 18 + cnt(fe3) == 23 == 26 - 3
    # 3d6 / 3d5 as the configuration text on the slide
    assert sum(fe2[1][1]) == 6 and sum(fe3[1][1]) == 5

    cv = Canvas()
    size = 88
    xs = group_x(fe, size=size, x_start=170)
    for (lab, _), cx in zip(fe, xs):
        cv.text(cx, 62, lab, "Archivo-SemiBold.ttf", 52, C["graphite"], "c")
    cv.text(985, 62, "Total", "Archivo-SemiBold.ttf", 46, C["graphite"], "r")
    ys = [90, 245, 400]
    for y, lab, g, tot, kw in ((ys[0], "Fe", fe, 26, {}),
                               (ys[1], "Fe^2+", fe2, 24, dict(dashed_idx=(0,))),
                               (ys[2], "Fe^3+", fe3, 23, dict(accent_idx=(1,)))):
        cv.text(20, y + 60, lab, "Archivo-Bold.ttf", 54)
        orbital_row(cv, y, lab, g, size=size, x_start=170, **kw)
        cv.text(930, y + 62, str(tot), "Archivo-Bold.ttf", 60, C["accent"], "c")
    cv.text(W / 2, 545, "Dashed box: 4s electrons removed first", "Archivo-SemiBold.ttf", 48, C["asphalt"], "c")
    cv.save("chem_u02_s2.4_fe_ions_orbitals.png")


def main():
    for fn in (fig_core_valence, fig_valence_by_group, fig_noble_gas, fig_na_cl_ions,
               fig_charge_by_group, fig_isoelectronic, fig_fe_ions):
        fn()
    return 0


if __name__ == "__main__":
    sys.exit(main())
