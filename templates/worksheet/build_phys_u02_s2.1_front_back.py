#!/usr/bin/env python3
"""One-off custom layout for SHULL_PHYS_Practice_Set_U02_S02.1.docx.

Matt's exact spec: a strict two-page, front/back sheet.
  Front (Section A) - 6 small square boxes: 1 worked example + 5 draw-tip-to-tail questions.
  Back  (Section B) - 6 small square boxes: 1 worked example + 5 describe-two-other-ways
                       questions, with the angle reference circle off to the side.

The shared build_worksheet_docx.py renders content as sequential full-width blocks and
has no two-column (squares beside a reference image) layout, and its `draw` block panels
are always blank - neither fits "an example already filled in, in the same small square."
Both needs are handled here by calling the same shared primitives (_shull_docx, and
draw_block itself) directly, then placing a picture / worked text into panel 1 of each
grid after the fact. Same visual system, custom page composition.
"""
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

import sys
sys.path.insert(0, REPO)
from _shull_docx import (                      # noqa: E402
    Palette, borders, para, run, fix_widths, one_cell, no_split,
    equation_bar, page_setup, running_footer, cell_margins, gap, shade, unpad_cell, hexof,
)
sys.path.insert(0, HERE)
from build_worksheet_docx import draw_block, label, TEXT_W_IN   # noqa: E402

pal = Palette("physics")
OUT = os.path.join(HERE, "SHULL_PHYS_Practice_Set_U02_S02.1.docx")

doc = Document()
s = page_setup(doc)


def header(unit_title, sec_title, code, first_page):
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [5.55, 1.95])
    h, hr = t.rows[0].cells
    for cc in (h, hr):
        borders(cc, pal.hair, sz=4, edges=("top", "bottom"))
    borders(h, pal.display, sz=30, edges=("left",))
    cell_margins(h, top=80, bottom=80, left=160, right=80)
    cell_margins(hr, top=80, bottom=80, left=80, right=60)
    para(h, unit_title, 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    para(h, sec_title, 15, bold=True, color=pal.ink)
    pp = para(hr, code, 11, bold=True, color=pal.accent, caps_track=True, first=True)
    pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pp = para(hr, "PRACTICE SET", 6.5, color=pal.label, caps_track=True)
    pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    if first_page:
        gap(doc, 5)
        widths = [3.05, 1.75, 1.10, 1.60]
        t2 = doc.add_table(rows=1, cols=4)
        fix_widths(t2, widths)
        for cc, lab in zip(t2.rows[0].cells, ("NAME", "DATE", "PERIOD", "SCORE")):
            borders(cc, pal.ink, sz=4, edges=("bottom",))
            cell_margins(cc, top=0, bottom=40, left=0, right=120)
            p = para(cc, lab, 6.5, bold=True, color=pal.label, caps_track=True, first=True)
            if lab == "SCORE":
                p.paragraph_format.tab_stops.add_tab_stop(Inches(widths[3] - 0.10), WD_TAB_ALIGNMENT.RIGHT)
                run(p, "\t", 9)
                run(p, "/  20", 10, bold=True, color=pal.ink)


def remember(summary, key_ideas):
    gap(doc, 5)
    c = one_cell(doc)
    borders(c, pal.hair, sz=4)
    borders(c, pal.display, sz=24, edges=("left",))
    shade(c, pal.surface)
    cell_margins(c, top=65, bottom=65, left=130, right=130)
    label(c, "REMEMBER", pal, first=True)
    para(c, summary, 9.5)
    for k in key_ideas:
        para(c, "•  " + k, 9.5)


def directions(text):
    gap(doc, 3)
    c = one_cell(doc)
    borders(c, pal.ink, sz=8, edges=("top",))
    label(c, "DIRECTIONS", pal, first=True)
    para(c, text, 9.5)


# =============================================================== PAGE 1 — SECTION A
header("UNIT 2 — MOTION IN TWO DIMENSIONS", "Section A — Draw the Vectors, Tip-to-Tail",
       "U02 / S02.1", first_page=True)
remember(
    "A vector is a quantity with both magnitude and direction, drawn as an arrow. "
    "Tip-to-tail: each new vector's tail starts exactly at the arrowhead of the one before it.",
    ["Draw every vector in the order it's listed — a, then b, then c.",
     "Label each arrow as you draw it."],
)
directions("Box 1 is done for you. In boxes 2–6, draw tip-to-tail, starting at the dot, "
           "every vector listed. Label each arrow.")

gap(doc, 4)
blockA = {
    "panels": 6, "across": 3, "panelHeightIn": 2.0,
    "captions": [
        "EXAMPLE",
        "a = 3 cm east\nb = 2 cm north",
        "a = 2 cm north\nb = 3 cm east\nc = 1 cm south",
        "a = 40 N at 0°\nb = 30 N at 90°\nc = 20 N at 180°",
        "a = 5 m at 45°\nb = 3 m at 135°",
        "a = 4 cm at 30°\nb = 3 cm at 160°\nc = 2 cm at 250°",
    ],
}
tblA = draw_block(one_cell(doc), blockA, pal, TEXT_W_IN - 0.3)

# Drop the examplee image into panel 1 (row 0, col 0) and relabel its caption.
panel1 = tblA.rows[0].cells[0]
pic_p = panel1.add_paragraph()
pic_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
pic_p.add_run().add_picture(
    os.path.join(HERE, "assets", "phys_vector_tip_to_tail_example.png"), height=Inches(1.55))
cap1 = tblA.rows[1].cells[0]
cap1.paragraphs[0].runs[0].text = "a = 3 east, b = 2 north — b starts at a's tip"

# =============================================================== PAGE 2 — SECTION B
doc.add_page_break()
header("UNIT 2 — MOTION IN TWO DIMENSIONS", "Section B — Describe the Vector, Two Other Ways",
       "U02 / S02.1", first_page=False)
remember(
    "Every vector's direction can be written three equivalent ways — a positive course angle "
    "(0° to 360°, counterclockwise from East), that angle written as a negative number, or a "
    "compass phrase like ‘35° North of East.’ Given any one, you can always find the other two.",
    ["A compass phrase has two valid phrasings for the same direction — they always add to 90°.",
     "Use the reference circle at right to check your work."],
)
directions("Box 1 is done for you. In boxes 2–6, write the vector's other two correct "
           "descriptions.")

gap(doc, 4)
outer = doc.add_table(rows=1, cols=2)
fix_widths(outer, [4.55, 2.65])
left_cell, right_cell = outer.rows[0].cells
cell_margins(left_cell, top=0, bottom=0, left=0, right=60)
cell_margins(right_cell, top=0, bottom=0, left=60, right=0)

blockB = {
    "panels": 6, "across": 2, "panelHeightIn": 1.35,
    "captions": [
        "EXAMPLE",
        "Given: 40° North of East",
        "Given: a course of 70°",
        "Given: a course of 162°",
        "Given: a course of −225°",
        "Given: a course of 315°",
    ],
}
tblB = draw_block(left_cell, blockB, pal, 4.35)

panel1b = tblB.rows[0].cells[0]
p2 = panel1b.add_paragraph()
run(p2, "Course angle = 50°", 8.5, color=pal.ink)
p3 = panel1b.add_paragraph()
run(p3, "Negative form = −310°", 8.5, color=pal.ink)
cap1b = tblB.rows[1].cells[0]
cap1b.paragraphs[0].runs[0].text = "Given: 50° North of East"

label(right_cell, "REFERENCE CIRCLE", pal, first=True)
para(right_cell, "Every course angle and its negative form.", 8.5)
pic_p2 = right_cell.add_paragraph()
pic_p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
pic_p2.add_run().add_picture(
    os.path.join(HERE, "assets", "phys_vector_angle_reference_circle.png"), width=Inches(2.55))

running_footer(s, "SHULL SCIENCE          U02 · S02.1", pal, with_page_numbers=True)
doc.save(OUT)
print("wrote", OUT)
