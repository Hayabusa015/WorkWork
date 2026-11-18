"""One-time build: Physics 3.2 practice set, Net Force. Not a precedent; no builder file is edited.

Matt asked for 2 pages with the three parts running together, so the spec is ONE section of 12
questions. Two in-memory overrides, for this call only:
  1. RAMP["physics"] = 2 warm-up / 4 practice / 5 challenge / 1 multi-topic (the standard is
     2/2/1/1 per section), the same mechanism as build_phys_u03_fbd_problem_set_1.py.
  2. render_questions() (student) and answer_block() (key) also draw a part sub-heading before any
     question carrying "partHeading": [title, one-line note]. Numbering stays continuous, 1-12.
     The key starts each part on a new page.
Name: document_name(..., descriptor="Net Force") - Matt's choice (3.2 has no short title row)."""
import os, sys
REPO = "/home/user/WorkWork"
WS = os.path.join(REPO, "templates", "worksheet")
sys.path.insert(0, WS); sys.path.insert(0, os.path.join(REPO, "templates"))
from _shull_name import document_name
SPEC = os.path.join(WS, "specs", "phys_u03_s03.2_net_force.json")
OUT = os.path.join(REPO, "output", "physics", "u03")
stu = os.path.join(OUT, document_name("Practice_Set", ["3.2"], 3, descriptor="Net Force"))
key = os.path.join(OUT, document_name("Practice_Set", ["3.2"], 3, descriptor="Net Force", key=True))

import build_worksheet_docx as b
from _shull_docx import one_cell, borders, para, gap, fix_widths, no_split


def part_heading(container_doc, pal, head):
    c = one_cell(container_doc)
    borders(c, pal.display, sz=8, edges=("bottom",))
    p = para(c, head[0], 11, bold=True, color=pal.ink, first=True)
    p.paragraph_format.keep_with_next = True
    if len(head) > 1:
        q = para(c, head[1], 8.5, color=pal.label)
        q.paragraph_format.keep_with_next = True
    gap(container_doc, 3)


def render_questions(doc, questions, pal, course, base_dir):
    """The builder's render_questions, one card per question, plus the part sub-headings."""
    for i, q in enumerate(questions):
        if q.get("partHeading"):
            if i:
                gap(doc, 4)
            part_heading(doc, pal, q["partHeading"])
        t = doc.add_table(rows=1, cols=1)
        fix_widths(t, [b.TEXT_W_IN])
        no_split(t.rows[0])
        b.question_card(t.rows[0].cells[0], q, i + 1, pal, course, base_dir, b.TEXT_W_IN)
        gap(doc, 3)


b.RAMP["physics"] = {"warm-up": 2, "practice": 4, "challenge": 5, "multi-topic": 1}
b.render_questions = render_questions
sys.argv = ["build_worksheet_docx.py", SPEC, stu]
assert b.main() == 0

import build_worksheet_key_docx as k
_answer_block = k.answer_block


def answer_block(doc, n, q, pal):
    if q.get("partHeading"):
        if n > 1:
            k.page_break(doc)          # the key starts each part on a new page, so no heading strands
        part_heading(doc, pal, q["partHeading"][:1])
    return _answer_block(doc, n, q, pal)


k.answer_block = answer_block
sys.argv = ["build_worksheet_key_docx.py", SPEC, key]
assert k.main() == 0
print(stu); print(key)
