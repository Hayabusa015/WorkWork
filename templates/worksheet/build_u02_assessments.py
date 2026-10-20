#!/usr/bin/env python3
"""Chemistry U02 assessments: the Friday quiz (versions A, B, C, each with a key).

    python3 templates/worksheet/build_u02_assessments.py OUTDIR

Blueprint (Matt, 2026-10-20): two longhand configurations with orbital diagrams (one near
4p, one in 3s/3p), two noble-gas shorthand configurations (no f sublevel), four ion charges.
No Cr or Cu exceptions. Every answer is computed from the Aufbau generator in
build_electron_set.py and checked against a hand-written answer table before anything is
written, so a version cannot ship with a key that disagrees with its own question.

Keys follow standards/ANSWER_KEYS.md: written answers in the key-handwriting face in the pen
ink, the final answer boxed in the box ink, notes in the arrow ink. Faces and inks come from
brand/tokens.json; no font name or hex is typed here.
"""
import os, sys
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "templates"))
sys.path.insert(0, os.path.join(REPO, "templates", "notes"))
from build_electron_set import (                                  # noqa: E402
    SYMBOLS, config, shorthand, valence, arrows, NOBLE_SYM, new_doc, header, label,
    write_line, pin_tail, pin_first, Palette, COURSE, UNIT,
)
from _shull_docx import (                                          # noqa: E402
    T, hexof, borders, para, fix_widths, one_cell, no_split, gap, running_footer, trim_tail,
)
from build_notes_packet import Ctx, rich, spacer, cell_margins, _run, page_break_before   # noqa: E402
from _shull_name import document_name                              # noqa: E402

HAND = T["typography"]["keyHandwriting"]["family"]
# ANSWER_KEYS.md section 7: a character that could be misread falls back to the face's named
# fallback. In this face 1 reads as I and 6 reads as b, so every digit takes the fallback.
import re as _re
HAND_FALLBACK = _re.search(r"Fallback for any missing glyph: ([^.]+)\.",
                           T["typography"]["keyHandwriting"]["note"]).group(1).strip()
INK = {k: T["keyInk"][k]["hex"] for k in ("pencil", "pen", "box", "arrow")}

NAMES = {3: "Lithium", 8: "Oxygen", 9: "Fluorine", 11: "Sodium", 12: "Magnesium",
         15: "Phosphorus", 16: "Sulfur", 17: "Chlorine", 19: "Potassium", 20: "Calcium",
         25: "Manganese", 26: "Iron", 27: "Cobalt", 33: "Arsenic", 34: "Selenium",
         35: "Bromine", 38: "Strontium", 50: "Tin", 51: "Antimony", 52: "Tellurium",
         53: "Iodine"}

# Version blueprints. Q1 near 4p, Q2 in 3p, Q3 a 4th-row d-block, Q4 a 5th-row p-block,
# Q5-8 one each of group 1, 2, 16, 17, in a different order per version.
VERSIONS = {
    "A": {"long": [34, 15], "short": [26, 50], "ions": [11, 8, 12, 17]},
    "B": {"long": [33, 17], "short": [27, 51], "ions": [16, 19, 9, 20]},
    "C": {"long": [35, 16], "short": [25, 52], "ions": [38, 53, 3, 34]},
}

# Hand-written answers, used only to check the generator. A mismatch stops the build.
EXPECT_LONG = {
    34: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4", 33: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3",
    35: "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5", 15: "1s2 2s2 2p6 3s2 3p3",
    17: "1s2 2s2 2p6 3s2 3p5", 16: "1s2 2s2 2p6 3s2 3p4",
}
EXPECT_SHORT = {26: "[Ar] 4s2 3d6", 27: "[Ar] 4s2 3d7", 25: "[Ar] 4s2 3d5",
                50: "[Kr] 5s2 4d10 5p2", 51: "[Kr] 5s2 4d10 5p3", 52: "[Kr] 5s2 4d10 5p4"}
EXPECT_ION = {11: "1+", 19: "1+", 3: "1+", 12: "2+", 20: "2+", 38: "2+",
              8: "2−", 16: "2−", 34: "2−", 17: "1−", 9: "1−", 53: "1−"}
EXPECT_UNPAIRED = {34: 2, 33: 3, 35: 1, 15: 3, 17: 1, 16: 2}

POINTS = {"long": 4, "short": 2, "ion": 1}


def flat(subs):
    return " ".join(f"{n}{l}{c}" for n, l, c in subs)


def ion_charge(z):
    v = valence(z)[1]
    return f"{v}+" if v <= 3 else f"{8 - v}−"


def unpaired(z):
    return sum(sum(1 for m in arrows(c, {"s": 1, "p": 3, "d": 5}[l]) if m == "↑")
               for n, l, c in config(z))


def check():
    for v in VERSIONS.values():
        for z in v["long"]:
            assert flat(config(z)) == EXPECT_LONG[z], (z, flat(config(z)))
            assert unpaired(z) == EXPECT_UNPAIRED[z], (z, unpaired(z))
            assert sum(c for *_, c in config(z)) == z
        for z in v["short"]:
            core, rest = shorthand(z)
            got = f"[{NOBLE_SYM[core]}] " + flat(rest)
            assert got == EXPECT_SHORT[z], (z, got)
            assert core + sum(c for *_, c in rest) == z
            assert not any(l == "f" for _, l, _ in rest)
        for z in v["ions"]:
            assert ion_charge(z) == EXPECT_ION[z], (z, ion_charge(z))
    print("quiz answers re-solved for A, B and C: all match")


# ---------------------------------------------------------------------------------------
def hand(p, text, size=13, ink="pen", sup=False, boxed=False):
    """Key handwriting. Digits are split out into the fallback face (legibility rule)."""
    parts = _re.split(r"(\d+)", text)
    last = None
    for part in parts:
        if part:
            last = _hand_run(p, part, size, ink, sup, boxed,
                             HAND_FALLBACK if part.isdigit() else HAND)
    return last


def _hand_run(p, text, size, ink, sup, boxed, face):
    r = p.add_run(text)
    r.font.name = face
    r._element.get_or_add_rPr()
    r.font.size = Pt(size)
    r.font.color.rgb = RGBColor.from_string(hexof(INK[ink]))
    if sup:
        r.font.superscript = True
    if boxed:
        rPr = r._element.get_or_add_rPr()
        b = OxmlElement("w:bdr")
        b.set(qn("w:val"), "single"); b.set(qn("w:sz"), "8"); b.set(qn("w:space"), "1")
        b.set(qn("w:color"), hexof(INK["box"]))
        rPr.append(b)
    return r


def hand_config(p, z, short=False, size=13):
    if short:
        core, subs = shorthand(z)
        hand(p, f"[{NOBLE_SYM[core]}] ", size, boxed=True)
    else:
        subs = config(z)
    for i, (n, l, c) in enumerate(subs):
        hand(p, f"{n}{l}", size, boxed=True)
        hand(p, str(c), size, sup=True, boxed=True)
        if i < len(subs) - 1:
            hand(p, " ", size, boxed=True)


def key_strip(cell, pal, z, lab_w=0.30, box_w=0.25):
    """The filled orbital diagram on the key: every sublevel the atom uses, arrows in pen
    ink. Arrows are set in the brand face, which the key-face fallback rule allows."""
    subs = config(z)
    widths = []
    for n, l, c in subs:
        widths += [lab_w] + [box_w] * {"s": 1, "p": 3, "d": 5}[l]
    t = cell.add_table(rows=1, cols=len(widths))
    fix_widths(t, widths)
    no_split(t.rows[0], 0.30)
    ci = 0
    for n, l, c in subs:
        lc = t.rows[0].cells[ci]; ci += 1
        lc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        cell_margins(lc, top=0, bottom=0, left=0, right=10)
        p = lc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        _run(p, f"{n}{l}", 8, bold=True, color=pal.label)
        for m in arrows(c, {"s": 1, "p": 3, "d": 5}[l]):
            bc = t.rows[0].cells[ci]; ci += 1
            borders(bc, INK["pencil"], sz=6)
            bc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            cell_margins(bc, top=0, bottom=0, left=0, right=0)
            p = bc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            _run(p, m, 10, bold=True, color=INK["pen"])
    pin_tail(cell)


def qhead(cell, n, text, pts, pal, first=True):
    p = cell.paragraphs[0] if first else cell.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(7.1), WD_TAB_ALIGNMENT.RIGHT)
    _run(p, f"{n}   ", 10.5, bold=True, color=pal.accent)
    _run(p, text, 10.5, bold=True, color=pal.ink)
    _run(p, "\t", 9)
    _run(p, f"{pts} pts" if pts > 1 else "1 pt", 8, bold=True, color=pal.label)
    return p


def name_of(z):
    return f"{NAMES.get(z, SYMBOLS[z - 1])}, {SYMBOLS[z - 1]}"


# Multiple choice (Matt, 2026-10-20: "add maybe 5"). Each version asks the same five skills
# with a different case; distractors are the usual mistakes. The correct option is listed
# first here and placed by MC_ORDER, so the answer letter moves between versions.
MC = {
    "A": [
        ("Which rule says electrons fill the lowest-energy sublevel first?",
         ["Aufbau principle", "Pauli exclusion", "Hund's rule", "Bohr model"],
         "Aufbau, lowest energy first"),
        ("Which orbital diagram for nitrogen's 2p^3^ follows Hund's rule?",
         ["[↑] [↑] [↑]", "[↑↓] [↑] [   ]", "[↑] [↓] [↑]",
          "[↑↓] [   ] [↑]"], "one in each box, same direction"),
        ("How many electrons can a p sublevel hold?", ["6", "3", "2", "10"],
         "3 orbitals x 2 = 6"),
        ("An atom gains 2 electrons. What is the charge of its ion?", ["2−", "2+", "0", "6−"],
         "more electrons than protons, so negative"),
        ("Which sublevel fills right after 4s?", ["3d", "4p", "4d", "5s"], "4s, then 3d"),
    ],
    "B": [
        ("Which rule says two electrons in one orbital must have opposite spins?",
         ["Pauli exclusion", "Aufbau principle", "Hund's rule", "Bohr model"],
         "Pauli, 2 per orbital, opposite"),
        ("Which orbital diagram for oxygen's 2p^4^ follows Hund's rule?",
         ["[↑↓] [↑] [↑]", "[↑↓] [↑↓] [   ]", "[↑] [↑] [↑]",
          "[↑↓] [↑] [↓]"], "spread out, then pair the 4th"),
        ("How many electrons can a d sublevel hold?", ["10", "5", "6", "14"],
         "5 orbitals x 2 = 10"),
        ("An atom loses 3 electrons. What is the charge of its ion?", ["3+", "3−", "0", "5+"],
         "more protons than electrons, so positive"),
        ("Which sublevel fills right after 3d?", ["4p", "4s", "4d", "3f"], "3d, then 4p"),
    ],
    "C": [
        ("Which rule says put one electron in each box before pairing?",
         ["Hund's rule", "Aufbau principle", "Pauli exclusion", "Bohr model"],
         "Hund, one in each before pairing"),
        ("Which orbital diagram for carbon's 2p^2^ follows Hund's rule?",
         ["[↑] [↑] [   ]", "[↑↓] [   ] [   ]", "[↑] [↓] [   ]",
          "[   ] [↑↓] [   ]"], "one in each box, same direction"),
        ("How many orbitals are in a d sublevel?", ["5", "10", "3", "7"],
         "d has 5 orbitals (holds 10 electrons)"),
        ("An atom gains 1 electron. What is the charge of its ion?", ["1−", "1+", "0", "7−"],
         "more electrons than protons, so negative"),
        ("Which sublevel fills right after 4p?", ["5s", "4d", "5p", "4f"], "4p, then 5s"),
    ],
}
# Position of the correct option (0 = A) for each question, per version.
MC_ORDER = {"A": [0, 2, 1, 3, 1], "B": [2, 0, 3, 1, 2], "C": [1, 3, 0, 2, 3]}
LETTERS = "ABCD"


def mc_options(ver, i):
    q, opts, why = MC[ver][i]
    pos = MC_ORDER[ver][i]
    rest = opts[1:]
    out = rest[:pos] + [opts[0]] + rest[pos:]
    return q, out, pos, why


def check_mc():
    for ver in MC:
        letters = []
        for i in range(5):
            q, out, pos, why = mc_options(ver, i)
            assert out[pos] == MC[ver][i][1][0] and len(set(out)) == 4, (ver, i)
            letters.append(LETTERS[pos])
        assert len(set(letters)) >= 3, (ver, letters)    # answers are spread out
    print("multiple choice: one correct option each, answer letters spread:",
          {v: "".join(LETTERS[p] for p in MC_ORDER[v]) for v in MC})


def cellfmt(cc, pal, line=True, top=40, bottom=40, left=60, right=60):
    """Left-aligned, vertically centred: the one cell style used on the whole quiz."""
    cc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    cell_margins(cc, top=top, bottom=bottom, left=left, right=right)
    if line:
        borders(cc, pal.hair, sz=4, edges=("bottom",))
    p = cc.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return p


def part_bar(doc, pal, text, pts):
    gap(doc, 6)
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [6.3, 1.2])
    a, b = t.rows[0].cells
    for x in (a, b):
        borders(x, pal.ink, sz=12, edges=("top",))
        borders(x, pal.display, sz=18, edges=("bottom",))
    pa = cellfmt(a, pal, line=False, top=30, bottom=30, left=0)
    _run(pa, text, 9, bold=True, color=pal.ink)
    pb = cellfmt(b, pal, line=False, top=30, bottom=30)
    pb.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    _run(pb, f"{pts} pts", 8.5, bold=True, color=pal.label)
    for x in (a, b):
        x.paragraphs[0].paragraph_format.keep_with_next = True


NUM_W = 0.45


def build_quiz(out, ver, key):
    pal = Palette(COURSE)
    ctx = Ctx(pal, key)
    v = VERSIONS[ver]
    total = 5 + 2 * POINTS["long"] + 2 * POINTS["short"] + 4 * POINTS["ion"]
    doc, s = new_doc()
    header(doc, pal, f"QUIZ  ·  VERSION {ver}  ·  ELECTRON CONFIGURATIONS AND IONS" +
           ("  ·  TEACHER KEY" if key else ""), f"Unit 2 Quiz {ver}", score=total)
    gap(doc, 3)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    p = cellfmt(c, pal, line=False, top=30, bottom=30)
    _run(p, "You may use your periodic table. Circle one letter for each multiple-choice "
            "question. Draw an arrow for every electron in the orbital diagrams.", 9.5,
         color=pal.ink)

    # ---- Part 1: multiple choice ----
    part_bar(doc, pal, "PART 1  ·  MULTIPLE CHOICE", 5)
    for i in range(5):
        q, opts, pos, why = mc_options(ver, i)
        t = doc.add_table(rows=2, cols=5)
        fix_widths(t, [NUM_W, 1.76, 1.76, 1.76, 1.77])
        no_split(t.rows[0]); no_split(t.rows[1])
        num = t.cell(0, 0).merge(t.cell(1, 0))
        pn = cellfmt(num, pal, top=40)
        pn.paragraph_format.keep_with_next = True
        _run(pn, str(i + 1), 11, bold=True, color=pal.accent)
        qc = t.cell(0, 1).merge(t.cell(0, 4))
        pq = cellfmt(qc, pal, line=False, top=50, bottom=20)
        pq.paragraph_format.keep_with_next = True
        rich(pq, q, 10, ctx, bold=True)
        if key:
            hand(pq, "   " + LETTERS[pos], 13, boxed=True)
            hand(pq, "  " + why, 10, ink="arrow")
        for k, o in enumerate(opts):
            oc = t.cell(1, 1 + k)
            po = cellfmt(oc, pal, top=20, bottom=60)
            _run(po, f"{LETTERS[k]}   ", 10, bold=True, color=pal.accent)
            rich(po, o, 10, ctx, bold=(key and k == pos))

    # ---- Part 2: longhand + orbital diagram ----
    part_bar(doc, pal, "PART 2  ·  LONGHAND CONFIGURATION AND ORBITAL DIAGRAM",
             2 * POINTS["long"])
    for i, z in enumerate(v["long"], 6):
        t = doc.add_table(rows=3, cols=3)
        fix_widths(t, [NUM_W, 1.75, 5.3])
        for r in t.rows:
            no_split(r)
        num = t.cell(0, 0).merge(t.cell(2, 0))
        pn = cellfmt(num, pal)
        _run(pn, str(i), 11, bold=True, color=pal.accent)
        el = t.cell(0, 1).merge(t.cell(0, 2))
        pe = cellfmt(el, pal, line=False, top=50, bottom=10)
        pe.paragraph_format.keep_with_next = True
        _run(pe, name_of(z), 10.5, bold=True, color=pal.ink)
        _run(pe, f"     {POINTS['long']} pts: 2 configuration, 2 diagram", 8, color=pal.label)
        for r, lab in ((1, "Electron configuration"), (2, "Orbital diagram")):
            lc = t.cell(r, 1)
            pl = cellfmt(lc, pal, line=False)
            pl.paragraph_format.keep_with_next = (r == 1)
            _run(pl, lab, 9, bold=True, color=pal.ink)
            ac = t.cell(r, 2)
            pa = cellfmt(ac, pal, line=(r == 1), top=40, bottom=40)
            if r == 2:
                borders(ac, pal.hair, sz=4)
                no_split(t.rows[2], 0.85)
                if key:
                    pin_first(ac)
                    key_strip(ac, pal, z, lab_w=0.22, box_w=0.19)
                    q = ac.add_paragraph(); q.paragraph_format.space_after = Pt(0)
                    hand(q, f"→ one arrow in each box before pairing, "
                            f"{EXPECT_UNPAIRED[z]} unpaired", 10, ink="arrow")
            elif key:
                hand_config(pa, z, size=12)
        gap(doc, 2)

    # ---- Part 3: shorthand ----
    part_bar(doc, pal, "PART 3  ·  NOBLE-GAS SHORTHAND", 2 * POINTS["short"])
    t = doc.add_table(rows=2, cols=3)
    fix_widths(t, [NUM_W, 1.75, 5.3])
    for r, z in enumerate(v["short"]):
        no_split(t.rows[r], 0.45)
        pn = cellfmt(t.cell(r, 0), pal)
        _run(pn, str(8 + r), 11, bold=True, color=pal.accent)
        pe = cellfmt(t.cell(r, 1), pal)
        _run(pe, name_of(z), 10.5, bold=True, color=pal.ink)
        pa = cellfmt(t.cell(r, 2), pal)
        if key:
            hand_config(pa, z, short=True, size=12)

    # ---- Part 4: ion charges ----
    part_bar(doc, pal, "PART 4  ·  CHARGE OF THE ION EACH ATOM FORMS", 4 * POINTS["ion"])
    t = doc.add_table(rows=2, cols=6)
    fix_widths(t, [NUM_W, 1.55, 1.75, NUM_W, 1.55, 1.75])
    for k, z in enumerate(v["ions"]):
        r, side = k // 2, (k % 2) * 3
        no_split(t.rows[r], 0.45)
        pn = cellfmt(t.cell(r, side), pal)
        _run(pn, str(10 + k), 11, bold=True, color=pal.accent)
        pe = cellfmt(t.cell(r, side + 1), pal)
        _run(pe, name_of(z), 10.5, bold=True, color=pal.ink)
        pa = cellfmt(t.cell(r, side + 2), pal)
        _run(pa, "charge  ", 8.5, color=pal.label)
        if key:
            vcount = valence(z)[1]
            hand(pa, ion_charge(z), 13, boxed=True)
            hand(pa, f"  {vcount} val. e-", 9, ink="arrow")

    running_footer(s, f"SHULL SCIENCE          {UNIT}  ·  QUIZ {ver}" +
                   ("          TEACHER KEY" if key else ""), pal, with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)


# =======================================================================================
# Shared item helpers for the spectra sheet and the study guide
# =======================================================================================
def item(doc, pal, n, prompt, key, answer=None, lines=1, line_h=0.32, label_w=0.0,
         ctx=None, width=7.5):
    """A numbered prompt with ruled answer lines. The key writes the answer on the first line."""
    c = one_cell(doc, width); borders(c, pal.hair, sz=4, edges=("bottom",))
    cell_margins(c, top=30, bottom=30, left=40, right=40)
    p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.first_line_indent = Inches(-0.25)
    _run(p, f"{n}   ", 10, bold=True, color=pal.accent)
    rich(p, prompt, 10, ctx)
    for i in range(lines):
        t = c.add_table(rows=1, cols=1)
        fix_widths(t, [width - 0.45])
        no_split(t.rows[0], line_h)
        cc = t.rows[0].cells[0]
        cc.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
        borders(cc, pal.hair, sz=6, edges=("bottom",))
        cell_margins(cc, top=0, bottom=10, left=60, right=0)
        q = cc.paragraphs[0]; q.paragraph_format.space_after = Pt(0)
        if key and answer is not None and i == 0:
            if callable(answer):
                answer(q)
            else:
                hand(q, answer, 12)
    pin_tail(c)
    return c


def section_bar(doc, pal, text, width=7.5, new_page=False):
    if new_page:
        page_break_before(doc)
    else:
        gap(doc, 4)
    c = one_cell(doc, width); borders(c, pal.ink, sz=12, edges=("top",))
    borders(c, pal.display, sz=18, edges=("bottom",))
    para(c, text, 8.5, bold=True, color=pal.ink, caps_track=True, first=True)
    c.paragraphs[0].paragraph_format.keep_with_next = True


def keep_together(t):
    """Keep a short table on one page: every row except the last keeps with the next."""
    for row in t.rows[:-1]:
        for cc in row.cells:
            for q in cc.paragraphs:
                q.paragraph_format.keep_with_next = True


def small_table(doc, pal, heads, rows, answers, key, widths, ctx, row_h=0.32):
    t = doc.add_table(rows=1 + len(rows), cols=len(heads))
    fix_widths(t, widths)
    for i, h in enumerate(heads):
        cc = t.rows[0].cells[i]
        borders(cc, pal.display, sz=12, edges=("bottom",))
        cc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        cell_margins(cc, top=20, bottom=20, left=60, right=40)
        q = cc.paragraphs[0]; q.paragraph_format.space_after = Pt(0)
        rich(q, h, 8, ctx, bold=True, color=pal.accent)
    for ri, row in enumerate(rows, start=1):
        no_split(t.rows[ri], row_h)
        for ci, val in enumerate(row):
            cc = t.rows[ri].cells[ci]
            borders(cc, pal.hair, sz=4)
            cc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            cell_margins(cc, top=10, bottom=10, left=60, right=40)
            q = cc.paragraphs[0]; q.paragraph_format.space_after = Pt(0)
            if val is not None:
                rich(q, val, 10, ctx, bold=(ci == 0))
            elif key:
                hand(q, answers[ri - 1][ci], 12)
    keep_together(t)
    return t


def ladder_png(path, drops=()):
    """Hydrogen energy levels n = 1 to 6, drawn to scale (E = -13.6 / n^2 eV), with the
    ionization limit. Optional arrows for the key."""
    from PIL import Image, ImageDraw, ImageFont
    W, H = 2400, 1000
    im = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(os.path.join(REPO, "brand", "fonts", "Archivo-Bold.ttf"), 34)
    top, bot = 70, 1040

    # Not to scale: the real n=1 to n=2 gap is three quarters of the whole ladder, which
    # crowds n=3 to n=6 into a strip too thin to draw in. The order and the shrinking gaps
    # are kept, and the figure says so.
    frac = {1: 0.0, 2: 0.42, 3: 0.62, 4: 0.75, 5: 0.84, 6: 0.90, 0: 1.0}

    def y(n):
        return bot - frac[n] * (bot - top)
    ink = (60, 60, 60)
    for n in range(1, 7):
        d.line((260, y(n), 2300, y(n)), fill=ink, width=4)
        d.text((130, y(n) - 20), f"n = {n}", font=f, fill=ink)
    d.line((260, y(0), 2300, y(0)), fill=(150, 150, 150), width=3)
    d.text((1900, bot - 60), "not to scale", font=f, fill=(120, 120, 120))
    d.text((300, y(0) - 50), "ionization limit", font=f, fill=(120, 120, 120))
    d.line((80, bot, 80, top), fill=ink, width=4)
    d.polygon([(80, top - 10), (65, top + 25), (95, top + 25)], fill=ink)
    d.text((95, top + 30), "Energy", font=f, fill=ink)
    pen = tuple(int(hexof(INK["pen"])[i:i + 2], 16) for i in (0, 2, 4))
    for i, (a, b) in enumerate(drops):
        x = 700 + i * 380
        d.line((x, y(a), x, y(b) - 26), fill=pen, width=6)
        d.polygon([(x, y(b)), (x - 16, y(b) - 32), (x + 16, y(b) - 32)], fill=pen)
        d.text((x - 50, y(b) + 12), f"{a}→{b}", font=f, fill=pen)
    im.save(path)


# =======================================================================================
# Optional practice: atomic spectra (S2.5). No wave math (Matt, 2026-10-20).
# =======================================================================================
H_LINES = [((3, 2), "656", "red"), ((4, 2), "486", "blue-green"),
           ((5, 2), "434", "blue-violet"), ((6, 2), "410", "violet")]


def build_spectra(out, key, tmp):
    pal = Palette(COURSE)
    ctx = Ctx(pal, key)
    doc, s = new_doc()
    header(doc, pal, "OPTIONAL PRACTICE  ·  ATOMIC & ELECTRON SPECTRA" +
           ("  ·  TEACHER KEY" if key else ""), "Light from Electron Drops")
    gap(doc, 3)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "When an electron drops to a lower energy level, the atom gives off a photon. The "
            "bigger the drop, the more energy the photon carries. Use your notes from S2.5.",
         9.5, first=True)

    section_bar(doc, pal, "PART A  ·  HYDROGEN'S VISIBLE LINES")
    img = os.path.join(tmp, "ladder_key.png" if key else "ladder.png")
    ladder_png(img, [l[0] for l in H_LINES] if key else ())
    c = one_cell(doc)
    p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(3)
    _run(p, "1   ", 10, bold=True, color=pal.accent)
    rich(p, "On the energy ladder, draw an arrow for each drop: 3 \u2192 2, 4 \u2192 2, "
            "5 \u2192 2 and 6 \u2192 2.", 10, ctx)
    q = c.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.CENTER
    q.add_run().add_picture(img, width=Inches(6.6))
    p = c.add_paragraph(); p.paragraph_format.space_after = Pt(3)
    _run(p, "2   ", 10, bold=True, color=pal.accent)
    rich(p, "Fill in the wavelength and color of each line.", 10, ctx)
    no_split(doc.tables[-1].rows[0])
    gap(doc, 2)
    small_table(doc, pal, ["DROP", "WAVELENGTH (nm)", "COLOR"],
                [[f"n = {x} \u2192 {y_}", None, None] for (x, y_), wl, col in H_LINES],
                [[None, wl, col] for (x, y_), wl, col in H_LINES], key, [2.5, 2.5, 2.5], ctx)

    item(doc, pal, 3, "Rank the four drops from least energy to most energy.", key,
         "3→2,  4→2,  5→2,  6→2", ctx=ctx)
    item(doc, pal, 4, "Use the ladder to explain why the 6 → 2 photon has the most energy "
         "and the shortest wavelength of the four.", key,
         "It is the biggest gap, so the photon carries the most energy.", lines=2, ctx=ctx)

    section_bar(doc, pal, "PART B  ·  IN OR OUT", new_page=True)
    gap(doc, 2)
    small_table(doc, pal, ["ELECTRON MOVES", "ABSORBS OR EMITS", "PHOTON IN OR OUT"],
                [["n = 1 → 3", None, None], ["n = 4 → 2", None, None],
                 ["n = 2 → 6", None, None], ["n = 5 → 1", None, None]],
                [[None, "absorbs", "in"], [None, "emits", "out"],
                 [None, "absorbs", "in"], [None, "emits", "out"]],
                key, [2.4, 2.55, 2.55], ctx)
    item(doc, pal, 6, "Which drop gives off more energy, 3 → 1 or 3 → 2? Use the "
         "size of the gap in your answer.", key,
         "3→1. It is a bigger gap than 3→2.", lines=2, ctx=ctx)

    section_bar(doc, pal, "PART C  ·  THREE KINDS OF SPECTRA")
    gap(doc, 2)
    small_table(doc, pal, ["WHAT YOU SEE", "KIND OF SPECTRUM"],
                [["Every color, with no gaps", None],
                 ["Bright colored lines on a dark background", None],
                 ["Dark lines across a full rainbow", None]],
                [[None, "continuous"], [None, "emission"], [None, "absorption"]],
                key, [4.6, 2.9], ctx)

    section_bar(doc, pal, "PART D  ·  FLAME TESTS")
    gap(doc, 2)
    small_table(doc, pal, ["FLAME COLOR", "ION IT POINTS TO"],
                [["Yellow", None], ["Lilac", None], ["Blue-green", None]],
                [[None, "Na+"], [None, "K+"], [None, "Cu2+"]],
                key, [3.75, 3.75], ctx)
    item(doc, pal, 9, "Li^+^ and Sr^2+^ both give a red flame. Why is a flame color only a "
         "clue, not proof of which ion is there?", key,
         "Different ions can give similar colors, so another test is needed.", lines=2, ctx=ctx)

    running_footer(s, f"SHULL SCIENCE          {UNIT} · S02.5" +
                   ("          TEACHER KEY" if key else ""), pal, with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)


# =======================================================================================
# Unit 2 study guide: two pages plus key. Practises the same skills as the quiz and test
# without reusing any quiz element (checked in check_study_guide).
# =======================================================================================
SG_IONS = [(13, "Aluminum, Al"), (56, "Barium, Ba"), (7, "Nitrogen, N"), (37, "Rubidium, Rb")]
SG_ION_ANS = {13: ("3", "Al^3+^"), 56: ("2", "Ba^2+^"), 7: ("5", "N^3−^"),
              37: ("1", "Rb^+^")}


def check_study_guide():
    quiz = set()
    for v in VERSIONS.values():
        quiz |= set(v["long"]) | set(v["short"]) | set(v["ions"])
    used = {31, 40, 7, 6, 24, 30} | {z for z, _ in SG_IONS}
    clash = quiz & used
    assert not clash, f"study guide reuses quiz elements: {sorted(clash)}"
    assert flat(config(31)) == "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1"
    core, rest = shorthand(40); assert (core, flat(rest)) == (36, "5s2 4d2")
    core, rest = shorthand(24); assert (core, flat(rest)) == (18, "4s1 3d5")
    for z, (v, _) in SG_ION_ANS.items():
        assert str(valence(z)[1]) == v, (z, valence(z))
    print("study guide answers re-solved; no quiz element reused")


def build_study_guide(out, key):
    pal = Palette(COURSE)
    ctx = Ctx(pal, key)
    doc, s = new_doc()
    header(doc, pal, "STUDY GUIDE  ·  UNIT 2  ·  S2.1 – S2.5" +
           ("  ·  TEACHER KEY" if key else ""), "Unit 2 Study Guide: Electrons & Atomic Theory")
    gap(doc, 3)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "Work each section, then check it against your notes. Anything you miss tells you "
            "what to practise before the test.", 9.5, first=True)

    section_bar(doc, pal, "S2.1  ·  THE BOHR MODEL")
    item(doc, pal, 1, "What does quantized mean for an electron's energy?", key,
         "Set amounts only. It cannot sit between levels.", ctx=ctx)
    item(doc, pal, 2, "Hydrogen's electron is in n = 1. Name that state, and name the state "
         "when it is in n = 3.", key, "n=1 ground state; n=3 excited state", ctx=ctx)

    section_bar(doc, pal, "S2.2  ·  ENERGY LEVELS, SUBLEVELS & ORBITALS")
    item(doc, pal, 3, "List the sublevels in n = 4.", key, "4s, 4p, 4d, 4f", ctx=ctx)
    item(doc, pal, 4, "How many electrons fit in one d sublevel? How many fit in all of n = 2?",
         key, "d holds 10.  n=2 holds 8.", ctx=ctx)

    section_bar(doc, pal, "S2.3  ·  ELECTRON CONFIGURATIONS")
    item(doc, pal, 5, "Write the longhand configuration for gallium, Ga.", key,
         lambda q: hand_config(q, 31, size=12), ctx=ctx)
    item(doc, pal, 6, "Write the noble-gas shorthand for zirconium, Zr.", key,
         lambda q: hand_config(q, 40, short=True, size=12), ctx=ctx)
    c = item(doc, pal, 7, "Draw the orbital diagram for nitrogen, N, and count its unpaired "
             "electrons.", key, None, lines=0, ctx=ctx)
    if key:
        key_strip(c, pal, 7)
        q = c.add_paragraph(); hand(q, "3 unpaired", 12, boxed=True)
    else:
        spacer(c, 46)
    item(doc, pal, 8, "A student draws carbon's 2p as [↑↓] [   ] [   ]. Which rule "
         "did they break?", key, "Hund rule. It should be [↑] [↑] [   ].", ctx=ctx)
    item(doc, pal, 9, "Write chromium's actual shorthand configuration. Why is it an "
         "exception?", key,
         lambda q: (hand_config(q, 24, short=True, size=12),
                    hand(q, "   4s and 3d are close; this has less energy", 11, ink="arrow")),
         lines=2, ctx=ctx)

    section_bar(doc, pal, "S2.4  ·  VALENCE ELECTRONS & IONS", new_page=True)
    gap(doc, 2)
    small_table(doc, pal, ["ATOM", "VALENCE e^−^", "ION IT FORMS"],
                [[nm, None, None] for _, nm in SG_IONS],
                [[None, SG_ION_ANS[z][0], SG_ION_ANS[z][1].replace("^", "")]
                 for z, _ in SG_IONS], key, [2.5, 2.5, 2.5], ctx)
    item(doc, pal, 11, "Name two ions that have the same electron arrangement as neon.", key,
         "any two of Na+, Mg2+, Al3+, F-, O2-, N3-", ctx=ctx)
    item(doc, pal, 12, "Write the configuration of Zn^2+^. Which electrons left first?", key,
         "[Ar] 3d10. The two 4s electrons left first.", ctx=ctx)

    section_bar(doc, pal, "S2.5  ·  ATOMIC & ELECTRON SPECTRA")
    item(doc, pal, 13, "An electron moves from n = 2 to n = 5. Does the atom absorb or emit "
         "a photon?", key, "Absorbs. It moves up, so energy goes in.", ctx=ctx)
    item(doc, pal, 14, "Which photon has more energy, 486 nm or 656 nm?", key,
         "486 nm. Shorter wavelength, more energy.", ctx=ctx)
    item(doc, pal, 15, "Why does every element give off its own pattern of lines?", key,
         "Only certain energy gaps exist, and each element's gaps are different.", ctx=ctx)

    running_footer(s, f"SHULL SCIENCE          {UNIT} · S2.1-S2.5" +
                   ("          TEACHER KEY" if key else ""), pal, with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(outdir, exist_ok=True)
    check()
    check_mc()
    for ver in VERSIONS:
        for key in (False, True):
            name = document_name("Quiz", ["2.3", "2.4"], 2, version=ver, key=key)
            build_quiz(os.path.join(outdir, name), ver, key)
            print("wrote", name)
    tmp = os.path.join(outdir, ".dots"); os.makedirs(tmp, exist_ok=True)
    for key in (False, True):
        name = document_name("Practice_Set", ["2.5"], 2, key=key)
        build_spectra(os.path.join(outdir, name), key, tmp)
        print("wrote", name)
    check_study_guide()
    for key in (False, True):
        name = document_name("Study_Guide", ["2.1", "2.2", "2.3", "2.4", "2.5"], 2, key=key)
        build_study_guide(os.path.join(outdir, name), key)
        print("wrote", name)


if __name__ == "__main__":
    main()
