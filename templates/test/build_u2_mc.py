#!/usr/bin/env python3
"""Build the Physics Unit 2 Day 1 multiple-choice test (versions A, B, C) and answer keys.

    python3 templates/test/build_u2_mc.py OUTDIR

30 questions per version, 1 point each, in three sections (S2.1 7, S2.2 10, S2.3 13). All three
versions follow the same blueprint: the same skill is tested in the same section, with different
numbers or a different scenario, a different question order inside each section, and the correct
answer spread across A-D. Every wrong choice carries the mistake it stands for; the key prints it.
"""
import os, sys
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
for p in (HERE, os.path.join(REPO, "templates"), os.path.join(REPO, "templates", "quiz")):
    sys.path.insert(0, p)
import u2_data as D                                                    # noqa: E402
import build_quiz_docx as Q                                            # noqa: E402
import build_u2_written as W                                           # noqa: E402
from _shull_name import document_name                                  # noqa: E402
from _shull_docx import (Palette, borders, para, fix_widths, gap, one_cell, equation_bar,  # noqa: E402
                         tight_cells, no_split)

KEY_INK = Q.KEY_INK
LET = "ABCD"
DIRECTIONS = ("Choose the best answer and write its letter on the line. Use scratch paper for any work. Up is +y, "
              "g = 9.8 m/s², and air resistance is ignored. Angles on the 0–360° scale start at east and run "
              "counterclockwise.")
EQ = [{"plain": "Rx = R cos(angle)"}, {"plain": "Ry = R sin(angle)"}, {"plain": "tan(angle) = Ry / Rx"},
      {"plain": "R² = Rx² + Ry²"}, {"plain": "vix = vi cos(angle)"}, {"plain": "viy = vi sin(angle)"},
      {"plain": "Δx = vix t"}, {"plain": "vy = viy − g t"}]


def keep(cell_paras):
    for p in cell_paras:
        p.paragraph_format.keep_with_next = True


def section_label(doc, pal, text):
    gap(doc, 6)
    c = one_cell(doc, 7.4)
    borders(c, pal.display, sz=12, edges=("bottom",))
    para(c, text, 8.5, bold=True, color=pal.accent, caps_track=True, first=True)
    keep(c.paragraphs)


def question(doc, pal, q):
    """Four choices across one row when they are short, two rows of two when they are not."""
    short = max(len(c[0]) for c in q["choices"]) <= 20
    rows = 2 if short else 3
    t = doc.add_table(rows=rows, cols=5)
    fix_widths(t, [0.85, 1.64, 1.64, 1.64, 1.63])
    tight_cells(t, top=8, bottom=8, left=40, right=40)
    top = t.rows[0].cells[1].merge(t.rows[0].cells[4])
    para(t.rows[0].cells[0], f"____  {q['n']}.", 10, bold=True, color=pal.ink, first=True)
    para(top, q["stem"], 10, first=True)
    for k, (text, _) in enumerate(q["choices"]):
        if short:
            cell = t.rows[1].cells[1 + k]
        else:
            r = t.rows[1 + k // 2]
            cell = r.cells[1].merge(r.cells[2]) if k % 2 == 0 else r.cells[3].merge(r.cells[4])
        para(cell, f"{LET[k]}.  {text}", 10, first=True)
    for row in t.rows:
        no_split(row)
    for row in t.rows[:-1]:
        for c in row.cells:
            keep(c.paragraphs)
    gap(doc, 1)


def student(L, out):
    pal = Palette("physics")
    doc = Q.new_doc(pal, f"SHULL SCIENCE / PHYSICS / UNIT 02 / TEST {L} / DAY 1 MULTIPLE CHOICE")
    W.header(doc, pal, f"UNIT 2 TEST  ·  DAY 1 MULTIPLE CHOICE  ·  VERSION {L}")
    W.TOTAL = 30
    W.fields_row(doc, pal)
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, DIRECTIONS, 8.5, color=pal.ink, first=True)
    gap(doc, 3)
    equation_bar(doc, EQ, pal, "EQUATIONS YOU MAY USE")
    qs = D.build_mc(L)
    for lo, hi, label in D.MC_SECTIONS:
        section_label(doc, pal, label)
        for q in qs[lo:hi]:
            question(doc, pal, q)
    Q.finish(doc, out)


def key_doc(L, out):
    pal = Palette("physics")
    doc = Q.new_doc(pal, f"SHULL SCIENCE / PHYSICS / UNIT 02 / TEST {L} / DAY 1 MULTIPLE CHOICE / TEACHER KEY")
    W.header(doc, pal, f"UNIT 2 TEST  ·  DAY 1 MULTIPLE CHOICE  ·  VERSION {L}", key=True)
    qs = D.build_mc(L)
    gap(doc, 5)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "ANSWERS", 8, bold=True, color=pal.accent, caps_track=True, first=True)
    t = c.add_table(rows=6, cols=5)
    fix_widths(t, [1.45] * 5)
    tight_cells(t, top=20, bottom=20, left=40, right=40)
    for q in qs:
        r, col = (q["n"] - 1) % 6, (q["n"] - 1) // 6
        para(t.rows[r].cells[col], f"{q['n']:>2}.  {LET[q['answer']]}", 11, bold=True, color=KEY_INK, first=True)
    para(c, "1 point each, 30 total. Section totals: S2.1 questions 1–7 · S2.2 questions 8–17 · S2.3 questions 18–30.",
         8, color=pal.label)
    gap(doc, 6)
    c = one_cell(doc); borders(c, pal.hair)
    para(c, "WHY EACH WRONG CHOICE IS WRONG", 8, bold=True, color=pal.accent, caps_track=True, first=True)
    para(c, "Each distractor stands for a mistake students make. A pattern of the same wrong letter across a section tells you "
            "which skill to reteach.", 8, color=pal.label)
    t = c.add_table(rows=len(qs), cols=4)
    fix_widths(t, [0.35, 0.5, 2.15, 4.3])
    tight_cells(t, top=18, bottom=18, left=40, right=40)
    for q, row in zip(qs, t.rows):
        no_split(row)
        for cell in row.cells:
            borders(cell, pal.hair, sz=4, edges=("bottom",))
        para(row.cells[0], str(q["n"]), 8, bold=True, first=True)
        para(row.cells[1], f"{LET[q['answer']]}  {q['std']}", 8, bold=True, color=KEY_INK, first=True)
        para(row.cells[2], q["choices"][q["answer"]][0], 8, color=KEY_INK, first=True)
        first = True
        for k, (text, why) in enumerate(q["choices"]):
            if k == q["answer"]:
                continue
            para(row.cells[3], f"{LET[k]}  {why}", 7.5, color=pal.ink, first=first)
            first = False
    Q.finish(doc, out)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    bad = 0
    for L in D.VERS:
        for key in (False, True):
            p = os.path.join(outdir, document_name("Test", ["2.1", "2.2", "2.3"], 2, version=L, key=key, descriptor="Day 1 Multiple Choice"))
            (key_doc if key else student)(L, p) if False else (key_doc(L, p) if key else student(L, p))
            n = Q.pages(p)
            ok = n <= (4 if key else 3)
            print("ok " if ok else "BAD", n, "page", os.path.basename(p))
            bad += not ok
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
