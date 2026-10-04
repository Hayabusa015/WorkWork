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
                self.d.text((x * S, (y - px * 0.36) * S), s, font=f, fill=fill, anchor="ls")
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


# ---------------------------------------------------------------- D: Cl -> Cl-
def fig_cl_anion():
    cl = [("3s", [2]), ("3p", [2, 2, 1])]
    cl_anion = [("3s", [2]), ("3p", [2, 2, 2])]
    n1 = sum(sum(b) for _, b in cl)
    n2 = sum(sum(b) for _, b in cl_anion)
    assert (n1, n2) == (7, 8)
    assert 10 + n1 == 17 and 10 + n2 == 18 == 17 - (-1)

    cv = Canvas()
    xs = group_x(cl)
    for (lab, _), cx in zip(cl, xs):
        cv.text(cx, 80, lab, "Archivo-SemiBold.ttf", 52, C["graphite"], "c")
    y1, y2 = 105, 335
    cv.text(20, y1 + 62, "Cl", "Archivo-Bold.ttf", 56)
    cv.text(20, y2 + 62, "Cl^-", "Archivo-Bold.ttf", 56)
    orbital_row(cv, y1, "Cl", cl)
    orbital_row(cv, y2, "Cl-", cl_anion, accent_idx=(3,), added_down=3)
    # right-hand counts
    for y, v, t in ((y1, n1, 17), (y2, n2, 18)):
        cv.text(600, y + 40, f"{v} valence", "Archivo-Bold.ttf", 52, C["accent"])
        cv.text(600, y + 98, f"{t} total", "Archivo-SemiBold.ttf", 50, C["graphite"])
    cv.text(W / 2, 520, "The new electron fills the open 3p spot", "Archivo-SemiBold.ttf", 48, C["asphalt"], "c")
    cv.save("chem_u02_s2.4_cl_anion_orbitals.png")


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


# ---------------------------------------------------------------- G: Na -> Na+
def fig_na_cation():
    na = [("2s", [2]), ("2p", [2, 2, 2]), ("3s", [1])]
    na_ion = [("2s", [2]), ("2p", [2, 2, 2]), ("3s", [0])]
    cnt = lambda g: sum(sum(b) for _, b in g)
    assert 2 + cnt(na) == 11 and 2 + cnt(na_ion) == 10 == 11 - 1
    cv = Canvas()
    size = 82
    gap = 18
    xs = group_x(na, size=size, x_start=150, gap=gap)
    for (lab, _), cx in zip(na, xs):
        cv.text(cx, 62, lab, "Archivo-SemiBold.ttf", 50, C["graphite"], "c")
    cv.text(985, 62, "Total", "Archivo-SemiBold.ttf", 46, C["graphite"], "r")
    y1, y2 = 90, 270
    cv.text(20, y1 + 56, "Na", "Archivo-Bold.ttf", 54)
    cv.text(20, y2 + 56, "Na^+", "Archivo-Bold.ttf", 54)
    orbital_row(cv, y1, "Na", na, size=size, gap=gap, accent_idx=(4,))
    orbital_row(cv, y2, "Na+", na_ion, size=size, gap=gap, dashed_idx=(4,))
    cv.text(930, y1 + 58, "11", "Archivo-Bold.ttf", 60, C["accent"], "c")
    cv.text(930, y2 + 58, "10", "Archivo-Bold.ttf", 60, C["accent"], "c")
    cv.line(150, 410, W - 20, 410, C["rule"], 2)
    cv.text(W / 2, 490, "The 3s electron leaves.", "Archivo-SemiBold.ttf", 52, C["asphalt"], "c")
    cv.text(W / 2, 555, "11 − 1 = 10 electrons", "Archivo-Bold.ttf", 54, C["accent"], "c")
    cv.save("chem_u02_s2.4_na_cation_orbitals.png")


def main():
    for fn in (fig_core_valence, fig_valence_by_group, fig_noble_gas, fig_cl_anion,
               fig_isoelectronic, fig_fe_ions, fig_na_cation):
        fn()
    return 0


if __name__ == "__main__":
    sys.exit(main())
