#!/usr/bin/env python3
"""Chemistry U02 electron practice set: four print documents from one element table.

    python3 templates/worksheet/build_electron_set.py OUTDIR

  Longhand practice set    orbital diagram, then the configuration, with a worked example
  Shorthand practice set   noble-gas configuration, with a worked example
  Valence electron table   Z = 1-36: protons, electrons, configuration, valence, dot diagram,
                           then a blank periodic table (periods 1-4) for the dot diagrams
  Electron Battleship      rules on the front, two periodic tables on the back

Configurations are generated from the Aufbau order, with the two real exceptions in
Z <= 36 (Cr, Cu) written in, so no configuration is typed by hand. Colour comes from
brand/tokens.json through the shared Palette; the fonts are the brand Archivo files.
"""
import os, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "templates"))
sys.path.insert(0, os.path.join(REPO, "templates", "notes"))
from _shull_docx import (                                   # noqa: E402
    FONT, Palette, hexof, borders, para, fix_widths, one_cell, no_split, gap,
    page_setup, running_footer, trim_tail, rule_lines,
)
from build_notes_packet import (                            # noqa: E402
    Ctx, rich, rpara, spacer, cell_margins, _run, page_break_before,
)

COURSE = "chemistry"
UNIT = "U02"

SYMBOLS = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn "
           "Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba "
           "La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb "
           "Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs "
           "Mt Ds Rg Cn Nh Fl Mc Lv Ts Og").split()
NAMES = {1: "Hydrogen", 3: "Lithium", 7: "Nitrogen", 10: "Neon", 12: "Magnesium", 14: "Silicon",
         16: "Sulfur", 17: "Chlorine", 19: "Potassium", 20: "Calcium", 23: "Vanadium",
         30: "Zinc", 33: "Arsenic", 34: "Selenium", 11: "Sodium", 25: "Manganese",
         37: "Rubidium", 50: "Tin", 53: "Iodine", 60: "Neodymium"}
ORDER = [(1, "s"), (2, "s"), (2, "p"), (3, "s"), (3, "p"), (4, "s"), (3, "d"), (4, "p"),
         (5, "s"), (4, "d"), (5, "p"), (6, "s"), (4, "f"), (5, "d"), (6, "p"), (7, "s"),
         (5, "f"), (6, "d"), (7, "p")]
CAP = {"s": 2, "p": 6, "d": 10, "f": 14}
EXCEPTIONS = {24: {(4, "s"): 1, (3, "d"): 5}, 29: {(4, "s"): 1, (3, "d"): 10}}
NOBLE = [2, 10, 18, 36, 54, 86]
NOBLE_SYM = {2: "He", 10: "Ne", 18: "Ar", 36: "Kr", 54: "Xe", 86: "Rn"}


def config(z):
    """[(n, l, electrons)] in fill order for a neutral atom."""
    subs, left = [], z
    for n, l in ORDER:
        if left <= 0:
            break
        c = min(CAP[l], left)
        subs.append([n, l, c]); left -= c
    for s in subs:
        if (s[0], s[1]) in EXCEPTIONS.get(z, {}):
            s[2] = EXCEPTIONS[z][(s[0], s[1])]
    # exception atoms list every sublevel they use
    for key, c in EXCEPTIONS.get(z, {}).items():
        if not any((s[0], s[1]) == key for s in subs):
            subs.append([key[0], key[1], c])
    return [tuple(s) for s in subs]


def shorthand(z):
    core = max((g for g in NOBLE if g < z), default=0)
    rest, taken = [], 0
    for n, l, c in config(z):
        if taken < core:
            taken += c
            continue
        rest.append((n, l, c))
    return core, rest


def valence(z):
    subs = config(z)
    top = max(n for n, l, c in subs)
    return top, sum(c for n, l, c in subs if n == top)


def put_config(p, subs, size, color, *, bold=False, underline_top=False):
    top = max(n for n, l, c in subs) if subs else 0
    for i, (n, l, c) in enumerate(subs):
        u = underline_top and n == top
        _run(p, f"{n}{l}", size, bold=bold, color=color, underline=u)
        _run(p, str(c), size, bold=bold, color=color, sup=True, underline=u)
        if i < len(subs) - 1:
            _run(p, " ", size, bold=bold, color=color)


def put_short(p, z, size, color, *, bold=True):
    core, rest = shorthand(z)
    _run(p, f"[{NOBLE_SYM[core]}] ", size, bold=bold, color=color)
    put_config(p, rest, size, color, bold=bold)


def arrows(c, k):
    """Hund then Pauli: one up arrow in each box, then pair. Returns a list of k strings."""
    boxes = ["" for _ in range(k)]
    for i in range(min(c, k)):
        boxes[i] = "↑"
    for i in range(max(0, c - k)):
        boxes[i] = "↑↓"
    return boxes


# ---------------------------------------------------------------------------------------
# shared page furniture
# ---------------------------------------------------------------------------------------
def new_doc(landscape=False):
    doc = Document()
    s = page_setup(doc)
    if landscape:
        s.orientation = WD_ORIENT.LANDSCAPE
        s.page_width, s.page_height = Inches(11), Inches(8.5)
    return doc, s


def header(doc, pal, kicker, title, width=7.5, fields=True, score=None):
    c = one_cell(doc, width); borders(c, pal.display, sz=18, edges=("bottom",))
    para(c, "SHULL SCIENCE  ·  JAMES A. GARFIELD LOCAL SCHOOLS", 7.5, bold=True,
         color=pal.accent, caps_track=True, first=True)
    para(c, title.upper(), 18, bold=True, color=pal.ink)
    para(c, kicker, 7.5, color=pal.label, caps_track=True)
    if fields:
        c = one_cell(doc, width); borders(c, pal.hair)
        txt = "NAME  ______________________________________   DATE  ______________   PERIOD  _______"
        if score:
            txt += f"   SCORE  _____ / {score}"
        para(c, txt, 9, color=pal.label, first=True)


def label(cell, text, pal, first=False):
    return para(cell, text, 7.5, bold=True, color=pal.accent, caps_track=True, first=first)


def sublevel_strip(cell, pal, key, z, width_in=7.2):
    """The eight sublevels through 4p as labeled boxes in one row. The student draws the
    arrows; the key has them. Pre-printing every box (not just the ones an atom uses)
    keeps the choice of where to stop with the student."""
    subs = [(1, "s", 1), (2, "s", 1), (2, "p", 3), (3, "s", 1), (3, "p", 3),
            (4, "s", 1), (3, "d", 5), (4, "p", 3)]
    have = {(n, l): c for n, l, c in config(z)} if key else {}
    widths = []
    for n, l, k in subs:
        widths += [0.30] + [0.265] * k
    t = cell.add_table(rows=1, cols=len(widths))
    fix_widths(t, widths)
    no_split(t.rows[0], 0.34)
    ci = 0
    for n, l, k in subs:
        lc = t.rows[0].cells[ci]; ci += 1
        lc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        cell_margins(lc, top=0, bottom=0, left=0, right=10)
        p = lc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        _run(p, f"{n}{l}", 8, bold=True, color=pal.label)
        marks = arrows(have.get((n, l), 0), k)
        for b in range(k):
            bc = t.rows[0].cells[ci]; ci += 1
            borders(bc, pal.accent, sz=8)
            bc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            cell_margins(bc, top=0, bottom=0, left=0, right=0)
            p = bc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if marks[b]:
                _run(p, marks[b], 10, bold=True, color=pal.accent)
    return t


def write_line(cell, text_label, pal, key_fn, key, *, label_w=1.6, total_w=7.2, height=0.34):
    t = cell.add_table(rows=1, cols=2)
    fix_widths(t, [label_w, total_w - label_w])
    no_split(t.rows[0], height)
    a, b = t.rows[0].cells
    for x in (a, b):
        x.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
        cell_margins(x, top=0, bottom=10, left=0, right=0)
    borders(b, pal.hair, sz=6, edges=("bottom",))
    p = a.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    _run(p, text_label, 9, bold=True, color=pal.ink)
    p = b.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
    if key:
        key_fn(p)
    return t


# ---------------------------------------------------------------------------------------
# Item 1 and 2: practice sets
# ---------------------------------------------------------------------------------------
LONGHAND = [3, 7, 10, 12, 14, 16, 19, 23, 30, 33]
SHORT = [12, 17, 20, 25, 30, 33, 37, 50, 53, 60]


def element_name(z):
    return NAMES.get(z, SYMBOLS[z - 1])


def build_longhand(out, key):
    pal = Palette(COURSE)
    doc, s = new_doc()
    header(doc, pal, "PRACTICE SET  ·  ELECTRON CONFIGURATIONS  ·  LONGHAND" +
           ("  ·  TEACHER KEY" if key else ""), "Longhand Electron Configurations", score=5)
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    label(c, "DIRECTIONS", pal, first=True)
    para(c, "For each element: write how many electrons a neutral atom has, draw the arrows in "
            "the orbital diagram, then write the configuration underneath. Stop at the last "
            "arrow you drew. Use your periodic table.", 9.5)

    gap(doc, 6)
    c = one_cell(doc); borders(c, pal.accent)
    label(c, "EXAMPLE  —  CHLORINE, Cl", pal, first=True)
    para(c, "Neutral chlorine has 17 electrons (atomic number 17).", 9.5)
    ex = [
        "Fill the lowest-energy sublevel first: 1s, 2s, 2p, 3s, 3p.",
        "One electron in each box of a sublevel first. All arrows start pointing up.",
        "Then pair up with an arrow pointing down.",
        "The raised numbers add to 17.",
    ]
    for i, x in enumerate(ex, 1):
        para(c, f"{i}   {x}", 9)
    spacer(c, 3)
    sublevel_strip(c, pal, True, 17)
    spacer(c, 4)
    write_line(c, "Electron configuration", pal,
               lambda p: put_config(p, config(17), 10.5, pal.accent, bold=True), True)
    spacer(c, 2)

    for i, z in enumerate(LONGHAND, 1):
        gap(doc, 6)
        c = one_cell(doc); borders(c, pal.hair)
        t = c.add_table(rows=1, cols=2)
        fix_widths(t, [4.3, 2.9])
        no_split(t.rows[0])
        a, b = t.rows[0].cells
        for x in (a, b):
            cell_margins(x, top=0, bottom=0, left=0, right=0)
        p = a.paragraphs[0]; p.paragraph_format.space_after = Pt(2)
        _run(p, f"{i}   ", 10, bold=True, color=pal.accent)
        _run(p, f"{element_name(z)}, {SYMBOLS[z - 1]}", 10.5, bold=True, color=pal.ink)
        p = b.paragraphs[0]; p.paragraph_format.space_after = Pt(2)
        _run(p, "Electrons  ", 9, bold=True, color=pal.ink)
        if key:
            _run(p, str(z), 10.5, bold=True, color=pal.accent, underline=True)
        else:
            _run(p, "_________", 10, color=pal.ink)
        spacer(c, 3)
        sublevel_strip(c, pal, key, z)
        spacer(c, 4)
        write_line(c, "Electron configuration", pal,
                   lambda p, z=z: put_config(p, config(z), 10.5, pal.accent, bold=True), key)
        spacer(c, 2)
        no_split(doc.tables[-1].rows[0])

    running_footer(s, f"SHULL SCIENCE          {UNIT} · S02.3" +
                   ("          TEACHER KEY" if key else ""), pal, with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)


def build_shorthand(out, key):
    pal = Palette(COURSE)
    doc, s = new_doc()
    header(doc, pal, "PRACTICE SET  ·  ELECTRON CONFIGURATIONS  ·  NOBLE-GAS SHORTHAND" +
           ("  ·  TEACHER KEY" if key else ""), "Shorthand Electron Configurations", score=5)
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    label(c, "DIRECTIONS", pal, first=True)
    para(c, "Write the noble-gas shorthand configuration for each element. Use your periodic "
            "table. Check that the electrons in the brackets plus the raised numbers add up to "
            "the atomic number.", 9.5)

    gap(doc, 6)
    c = one_cell(doc); borders(c, pal.accent)
    label(c, "EXAMPLE  —  SELENIUM, Se", pal, first=True)
    para(c, "Selenium is atomic number 34.", 9.5)
    for i, x in enumerate([
            "Find the noble gas that comes before selenium: argon, Ar, atomic number 18.",
            "Write it in brackets: [Ar]. Those brackets stand for 18 electrons.",
            "Count what is left: 34 − 18 = 16 electrons.",
            "Fill the rest in order: 4s² (2), 3d¹⁰ (10), 4p⁴ (4). 2 + 10 + 4 = 16."], 1):
        para(c, f"{i}   {x}", 9)
    spacer(c, 4)
    write_line(c, "Shorthand", pal, lambda p: put_short(p, 34, 10.5, pal.accent), True,
               label_w=1.0)
    spacer(c, 2)

    gap(doc, 8)
    t = doc.add_table(rows=len(SHORT), cols=3)
    fix_widths(t, [0.4, 2.1, 5.0])
    for i, z in enumerate(SHORT):
        no_split(t.rows[i], 0.58)
        for cc in t.rows[i].cells:
            cc.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
            cell_margins(cc, top=0, bottom=30, left=40, right=40)
        a, b, w = t.rows[i].cells
        borders(w, pal.hair, sz=6, edges=("bottom",))
        p = a.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        _run(p, str(i + 1), 10, bold=True, color=pal.accent)
        p = b.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        _run(p, f"{element_name(z)}, {SYMBOLS[z - 1]}", 10.5, bold=True, color=pal.ink)
        p = w.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        if key:
            put_short(p, z, 10.5, pal.accent)

    running_footer(s, f"SHULL SCIENCE          {UNIT} · S02.3" +
                   ("          TEACHER KEY" if key else ""), pal, with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)


# ---------------------------------------------------------------------------------------
# Item 3: valence electron table + blank periodic table
# ---------------------------------------------------------------------------------------
def dot_image(path, sym, n):
    """Lewis dot diagram on a transparent square. Two electrons sit together on one side;
    otherwise one dot on each side first (top, right, bottom, left), then pair up."""
    S = 320
    im = Image.new("RGBA", (S, S), (255, 255, 255, 0))
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join(REPO, "brand", "fonts", "Archivo-Bold.ttf"), 120)
    bb = d.textbbox((0, 0), sym, font=font)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    cx, cy = S // 2, S // 2
    d.text((cx - tw // 2 - bb[0], cy - th // 2 - bb[1]), sym, font=font, fill=(33, 33, 33, 255))
    r, gap_, off = 12, 20, 30
    top, bot = cy - th // 2 - off, cy + th // 2 + off
    lef, rig = cx - tw // 2 - off, cx + tw // 2 + off
    counts = {"T": 0, "R": 0, "B": 0, "L": 0}
    if n == 2:
        counts["T"] = 2
    else:
        sides = ["T", "R", "B", "L"]
        for i in range(n):
            counts[sides[i % 4]] += 1
    for side, c in counts.items():
        for j in range(c):
            o = (j - (c - 1) / 2) * 2 * gap_ * 0.75
            if side == "T": x, y = cx + o, top
            elif side == "B": x, y = cx + o, bot
            elif side == "L": x, y = lef, cy + o
            else: x, y = rig, cy + o
            d.ellipse((x - r, y - r, x + r, y + r), fill=(77, 115, 14, 255))
    im.save(path)


def build_valence(out, key, tmp):
    pal = Palette(COURSE)
    doc, s = new_doc(landscape=True)
    W = 10.0
    cols = [0.75, 0.75, 0.9, 0.95, 4.35, 0.95, 1.35]
    heads = ["ATOMIC #", "SYMBOL", "PROTONS", "ELECTRONS", "ELECTRON CONFIGURATION",
             "VALENCE e^−^", "ELECTRON DOT"]
    ctx = Ctx(pal, key)
    per_page = [10, 13, 13]
    z = 1
    for pi, n in enumerate(per_page):
        if pi:
            page_break_before(doc)
        if pi == 0:
            header(doc, pal, "ORGANIZER  ·  ELEMENTS 1–36" + ("  ·  TEACHER KEY" if key else ""),
                   "Valence Electron Table", width=W)
            gap(doc, 3)
            c = one_cell(doc, W); borders(c, pal.display, sz=18, edges=("left",))
            para(c, "1   Fill in the protons, electrons and configuration for each element.   "
                    "2   Underline the electrons in the highest energy level. Those are the "
                    "valence electrons.   3   Count them, then draw the dot diagram.",
                 9, first=True)
            gap(doc, 3)
        t = doc.add_table(rows=1 + n, cols=len(cols))
        fix_widths(t, cols)
        for i, h in enumerate(heads):
            cc = t.rows[0].cells[i]
            borders(cc, pal.display, sz=12, edges=("bottom",))
            cc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            cell_margins(cc, top=40, bottom=40)
            p = cc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            rich(p, h, 8, ctx, bold=True, color=pal.accent)
        for r in range(n):
            row = t.rows[1 + r]
            no_split(row, 0.50)
            sym = SYMBOLS[z - 1]
            for ci, cc in enumerate(row.cells):
                borders(cc, pal.hair, sz=4)
                cc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                cell_margins(cc, top=20, bottom=20, left=80, right=60)
                p = cc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            c0, c1, c2, c3, c4, c5, c6 = row.cells
            _run(c0.paragraphs[0], str(z), 11, bold=True, color=pal.ink)
            _run(c1.paragraphs[0], sym, 11, bold=True, color=pal.ink)
            if key:
                _run(c2.paragraphs[0], str(z), 11, bold=True, color=pal.accent)
                _run(c3.paragraphs[0], str(z), 11, bold=True, color=pal.accent)
                put_config(c4.paragraphs[0], config(z), 10.5, pal.accent, bold=True,
                           underline_top=True)
                _run(c5.paragraphs[0], str(valence(z)[1]), 11, bold=True, color=pal.accent)
                img = os.path.join(tmp, f"dot_{z}.png")
                if not os.path.exists(img):
                    dot_image(img, sym, valence(z)[1])
                c6.paragraphs[0].add_run().add_picture(img, width=Inches(0.42))
            else:
                # the dot cell carries the symbol, faint, so the dots have a place to go
                p = c6.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                _run(p, sym, 11, bold=True, color=pal.hair)
            z += 1

    # ---- blank periodic table, periods 1-4 ----
    page_break_before(doc)
    header(doc, pal, "ORGANIZER  ·  ELEMENTS 1–36" + ("  ·  TEACHER KEY" if key else ""),
           "Periodic Table of Dot Diagrams", width=W, fields=False)
    gap(doc, 3)
    c = one_cell(doc, W)
    para(c, "Draw each element's electron dot diagram in its box. Check that the elements in "
            "each group have the same number of dots.", 9, first=True)
    gap(doc, 4)
    grid = periodic_layout(4)
    cw = W / 18
    t = doc.add_table(rows=1 + 4, cols=18)
    fix_widths(t, [cw] * 18)
    for g in range(18):
        cc = t.rows[0].cells[g]
        cell_margins(cc, top=0, bottom=20, left=0, right=0)
        p = cc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        _run(p, str(g + 1), 8, bold=True, color=pal.accent)
    for r in range(4):
        no_split(t.rows[1 + r], 1.12)
        for g in range(18):
            zz = grid[r][g]
            cc = t.rows[1 + r].cells[g]
            cell_margins(cc, top=20, bottom=0, left=30, right=0)
            if not zz:
                continue
            borders(cc, pal.hair, sz=6)
            p = cc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            _run(p, str(zz), 8, color=pal.label)
            if key:
                img = os.path.join(tmp, f"dot_{zz}.png")
                if not os.path.exists(img):
                    dot_image(img, SYMBOLS[zz - 1], valence(zz)[1])
                q = cc.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.CENTER
                q.paragraph_format.space_after = Pt(0)
                q.add_run().add_picture(img, width=Inches(0.50))
            else:
                q = cc.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.CENTER
                q.paragraph_format.space_before = Pt(18)
                _run(q, SYMBOLS[zz - 1], 11, bold=True, color=pal.hair)

    running_footer(s, f"SHULL SCIENCE          {UNIT} · S02.4" +
                   ("          TEACHER KEY" if key else ""), pal, with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)


def periodic_layout(rows, f_rows=False):
    """18-column grid of atomic numbers (0 = empty) for periods 1..rows."""
    lens = [2, 8, 8, 18, 18, 32, 32]
    grid, z = [], 0
    for r in range(rows):
        row = [0] * 18
        if r == 0:
            row[0] = 1; row[17] = 2
        elif r in (1, 2):
            base = 3 if r == 1 else 11
            for g in range(2):
                row[g] = base + g
            for g in range(13, 18):
                row[g] = base + 2 + (g - 13)
        elif r in (3, 4):
            base = 19 if r == 3 else 37
            for g in range(18):
                row[g] = base + g
        elif r == 5:
            for g in range(2):
                row[g] = 55 + g
            row[2] = 0
            for g in range(3, 18):
                row[g] = 72 + (g - 3)
        elif r == 6:
            for g in range(2):
                row[g] = 87 + g
            for g in range(3, 18):
                row[g] = 104 + (g - 3)
        grid.append(row)
    return grid


# ---------------------------------------------------------------------------------------
# Item 4: Electron Battleship
# ---------------------------------------------------------------------------------------
def build_battleship(out):
    pal = Palette(COURSE)
    doc, s = new_doc()
    header(doc, pal, "ACTIVITY  ·  ELECTRON CONFIGURATIONS  ·  TWO PLAYERS",
           "Electron Battleship")
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    label(c, "THE GAME", pal, first=True)
    para(c, "Battleship with a periodic table. Instead of calling a grid square, you call an "
            "element by its electron configuration. 30 minutes or more, one against one.", 9.5)

    gap(doc, 6)
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [3.75, 3.75])
    a, b = t.rows[0].cells
    borders(a, pal.hair); borders(b, pal.hair)
    label(a, "YOU NEED", pal, first=True)
    for x in ["This sheet, front and back", "2 markers or colored pencils, 2 different colors",
              "1 coin", "A binder or book to stand between you and your partner",
              "Only the aids you are allowed on a test"]:
        para(a, "•  " + x, 9.5)
    label(b, "YOUR FLEET", pal, first=True)
    para(b, "Draw each ship on MY SHIPS in a straight line, across or down, on boxes of "
            "its own block.", 9)
    for shp, blk, n in [("Destroyer", "s block", 2), ("Cruiser", "p block", 3),
                        ("Battleship", "d block", 4)]:
        para(b, f"•  {shp}  —  {blk}  —  {n} boxes", 9.5, bold=False)

    gap(doc, 6)
    c = one_cell(doc); borders(c, pal.hair)
    label(c, "HOW TO PLAY", pal, first=True)
    steps = [
        "Hide your sheet behind the divider. Draw your 3 ships on MY SHIPS in one color.",
        "Player 1 flips the coin. Heads: call the element in full configuration. Tails: call "
        "it in noble-gas shorthand. Say the configuration out loud, like 1s² 2s² 2p⁴.",
        "Player 2 works out which element it is, says its name, and answers HIT, MISS or SUNK.",
        "Player 1 marks the shot on MY SHOTS: X for a hit, O for a miss, in the second color.",
        "Player 2 marks that shot on MY SHIPS with an X or O in the other color, so you can "
        "see where you have been fired on.",
        "Switch roles. A ship is sunk when every box on it has been hit.",
        "If you and your partner disagree about which element a configuration names, check "
        "the periodic table together before the shot counts.",
        "The first player to sink all 3 of the other player's ships wins.",
    ]
    for i, x in enumerate(steps, 1):
        p = para(c, f"{i}   {x}", 9.5)
        p.paragraph_format.left_indent = Inches(0.22)
        p.paragraph_format.first_line_indent = Inches(-0.22)

    gap(doc, 6)
    t = doc.add_table(rows=1, cols=3)
    fix_widths(t, [2.5, 2.5, 2.5])
    for i, (h, body) in enumerate([
            ("HIT = X", "A shot that lands on a box of one of the ships."),
            ("MISS = O", "A shot that lands on open water."),
            ("SUNK", "Every box of that ship has an X.")]):
        cc = t.rows[0].cells[i]; borders(cc, pal.hair)
        label(cc, h, pal, first=True)
        para(cc, body, 9)

    gap(doc, 6)
    c = one_cell(doc); borders(c, pal.hair)
    label(c, "SHIPS SUNK", pal, first=True)
    para(c, "My ships sunk   Destroyer ____   Cruiser ____   Battleship ____          "
            "Their ships sunk   Destroyer ____   Cruiser ____   Battleship ____", 9)

    # ---- back: two full periodic tables ----
    page_break_before(doc)
    for title, sub, k in [("MY SHIPS", "Draw your 3 ships here. Mark each shot your partner "
                           "fires at you.", 0),
                          ("MY SHOTS", "Mark each shot you fire. X for a hit, O for a miss.", 1)]:
        c = one_cell(doc); borders(c, pal.ink, sz=12, edges=("top",))
        borders(c, pal.display, sz=18, edges=("bottom",))
        p = para(c, title, 10, bold=True, color=pal.ink, caps_track=True, first=True)
        _run(p, "     " + sub, 8.5, color=pal.label)
        gap(doc, 2)
        full_table(doc, pal)
        gap(doc, 8)

    running_footer(s, f"SHULL SCIENCE          {UNIT} · S02.3", pal, with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)


def full_table(doc, pal):
    """The whole periodic table, 18 columns, with the f-block beneath. Each box has the
    atomic number and the symbol, and room to mark a ship or a shot."""
    cw = 7.5 / 18
    grid = periodic_layout(7)
    f_row1 = list(range(57, 72)); f_row2 = list(range(89, 104))
    rows = 7 + 2
    t = doc.add_table(rows=rows, cols=18)
    fix_widths(t, [cw] * 18)

    def cell(cc, z):
        cell_margins(cc, top=10, bottom=0, left=20, right=0)
        borders(cc, pal.hair, sz=6)
        cc.vertical_alignment = WD_ALIGN_VERTICAL.TOP
        p = cc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        _run(p, str(z), 8, color=pal.label)
        q = cc.add_paragraph(); q.paragraph_format.space_after = Pt(0)
        q.alignment = WD_ALIGN_PARAGRAPH.CENTER
        _run(q, SYMBOLS[z - 1], 9, bold=True, color=pal.ink)

    for r in range(7):
        no_split(t.rows[r], 0.46)
        for g in range(18):
            z = grid[r][g]
            if z:
                cell(t.rows[r].cells[g], z)
    # La/Ac placeholders in group 3 of periods 6 and 7 are left empty on purpose;
    # the f-block sits underneath, starting under group 3 + 1.
    for i, series in enumerate((f_row1, f_row2)):
        r = 7 + i
        no_split(t.rows[r], 0.46)
        for j, z in enumerate(series):
            cell(t.rows[r].cells[2 + j], z)
    return t


# ---------------------------------------------------------------------------------------
def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(outdir, exist_ok=True)
    tmp = os.path.join(outdir, ".dots")
    os.makedirs(tmp, exist_ok=True)
    jobs = [
        ("SHULL_CHEM_Practice_Set_U02_S02.3_Longhand", build_longhand),
        ("SHULL_CHEM_Practice_Set_U02_S02.3_Shorthand", build_shorthand),
    ]
    for base, fn in jobs:
        fn(os.path.join(outdir, base + ".docx"), False)
        fn(os.path.join(outdir, base + "_Key.docx"), True)
    base = "SHULL_CHEM_Organizer_U02_S02.4_Valence_Electrons"
    build_valence(os.path.join(outdir, base + ".docx"), False, tmp)
    build_valence(os.path.join(outdir, base + "_Key.docx"), True, tmp)
    build_battleship(os.path.join(outdir, "SHULL_CHEM_Activity_U02_S02.3_Electron_Battleship.docx"))
    print("wrote 7 files to", outdir)


if __name__ == "__main__":
    main()
