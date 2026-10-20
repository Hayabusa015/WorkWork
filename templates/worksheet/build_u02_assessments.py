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
from build_notes_packet import Ctx, rich, spacer, cell_margins, _run   # noqa: E402
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


def key_strip(cell, pal, z):
    """The filled orbital diagram on the key: every sublevel the atom uses, arrows in pen
    ink. Arrows are set in the brand face, which the key-face fallback rule allows."""
    subs = config(z)
    widths = []
    for n, l, c in subs:
        widths += [0.30] + [0.25] * {"s": 1, "p": 3, "d": 5}[l]
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


def build_quiz(out, ver, key):
    pal = Palette(COURSE)
    v = VERSIONS[ver]
    total = 2 * POINTS["long"] + 2 * POINTS["short"] + 4 * POINTS["ion"]
    doc, s = new_doc()
    header(doc, pal, f"QUIZ  ·  VERSION {ver}  ·  ELECTRON CONFIGURATIONS AND IONS" +
           ("  ·  TEACHER KEY" if key else ""), f"Unit 2 Quiz {ver}", score=total)
    gap(doc, 3)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "You may use your periodic table. Draw an arrow for every electron in the orbital "
            "diagrams.", 9.5, first=True)

    # ---- Part 1: longhand + orbital diagram ----
    gap(doc, 5)
    c = one_cell(doc); borders(c, pal.ink, sz=12, edges=("top",))
    label(c, "PART 1  ·  LONGHAND CONFIGURATION AND ORBITAL DIAGRAM", pal, first=True)
    for i, z in enumerate(v["long"], 1):
        gap(doc, 4)
        c = one_cell(doc); borders(c, pal.hair)
        qhead(c, i, name_of(z), POINTS["long"], pal)
        write_line(c, "Electron configuration", pal, lambda p, z=z: hand_config(p, z), key,
                   label_w=1.6, total_w=7.1, height=0.36)
        spacer(c, 4)
        para(c, "Orbital diagram", 8.5, bold=True, color=pal.label)
        if key:
            key_strip(c, pal, z)
            p = c.add_paragraph(); p.paragraph_format.space_after = Pt(2)
            hand(p, f"→ Hund rule, one arrow in each box before pairing. "
                    f"{EXPECT_UNPAIRED[z]} unpaired.", 11, ink="arrow")
            hand(p, "   2 pts configuration, 2 pts diagram", 10, ink="pencil")
        else:
            spacer(c, 84)
        no_split(doc.tables[-1].rows[0])

    # ---- Part 2: shorthand ----
    gap(doc, 6)
    c = one_cell(doc); borders(c, pal.ink, sz=12, edges=("top",))
    label(c, "PART 2  ·  NOBLE-GAS SHORTHAND", pal, first=True)
    for i, z in enumerate(v["short"], 3):
        gap(doc, 4)
        c = one_cell(doc); borders(c, pal.hair)
        qhead(c, i, name_of(z), POINTS["short"], pal)
        write_line(c, "Shorthand", pal, lambda p, z=z: hand_config(p, z, short=True), key,
                   label_w=1.1, total_w=7.1, height=0.38)
        spacer(c, 3)
        no_split(doc.tables[-1].rows[0])

    # ---- Part 3: ion charges ----
    gap(doc, 6)
    c = one_cell(doc); borders(c, pal.ink, sz=12, edges=("top",))
    label(c, "PART 3  ·  CHARGE OF THE ION EACH ATOM FORMS", pal, first=True)
    gap(doc, 4)
    t = doc.add_table(rows=2, cols=2)
    fix_widths(t, [3.75, 3.75])
    for k, z in enumerate(v["ions"]):
        cc = t.rows[k // 2].cells[k % 2]
        borders(cc, pal.hair)
        cell_margins(cc, top=40, bottom=40, left=80, right=80)
        no_split(t.rows[k // 2], 0.62)
        qhead(cc, 5 + k, name_of(z), POINTS["ion"], pal)
        p = cc.add_paragraph(); p.paragraph_format.space_after = Pt(0)
        _run(p, "Charge of its ion  ", 9, bold=True, color=pal.ink)
        if key:
            ch = ion_charge(z)
            hand(p, ch, 14, boxed=True)
            vcount = valence(z)[1]
            why = f"{vcount} valence e⁻ → " + (f"loses {vcount}" if vcount <= 3
                                                      else f"gains {8 - vcount}")
            hand(p, "   " + why.replace("⁻", "-"), 10, ink="arrow")
        else:
            _run(p, "__________", 10, color=pal.ink)

    running_footer(s, f"SHULL SCIENCE          {UNIT}  ·  QUIZ {ver}" +
                   ("          TEACHER KEY" if key else ""), pal, with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(outdir, exist_ok=True)
    check()
    for ver in VERSIONS:
        for key in (False, True):
            name = document_name("Quiz", ["2.3", "2.4"], 2, version=ver, key=key)
            build_quiz(os.path.join(outdir, name), ver, key)
            print("wrote", name)


if __name__ == "__main__":
    main()
