"""The Unit 2 equation sheets, set with real subscripts and grouped by direction.

    vector_block(doc, pal)      components / adding / resultant
    projectile_block(doc, pal)  x (horizontal) / y (vertical) / solving for t

Markup in a line: _{ix} is a subscript, ^{2} a superscript. One source for the Day 2 written test and the
study guide, so the two cannot drift.
"""
import os, re, sys
from docx.shared import Pt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _shull_docx import borders, para, run, fix_widths, gap, one_cell, tight_cells   # noqa: E402

TOKEN = re.compile(r"(_\{[^}]*\}|\^\{[^}]*\})")

VECTOR = [
    ("COMPONENTS", ["R_{x} = R cos(angle)", "R_{y} = R sin(angle)"]),
    ("ADDING", ["R_{x} = A_{x} + B_{x}", "R_{y} = A_{y} + B_{y}"]),
    ("RESULTANT", ["R^{2} = R_{x}^{2} + R_{y}^{2}", "tan(angle) = R_{y} / R_{x}"]),
]
PROJECTILE = [
    ("x  ·  HORIZONTAL", ["v_{ix} = v_{i} cos(angle)", "Δx = v_{ix} t", "a_{x} = 0,  so v_{x} is constant"]),
    ("y  ·  VERTICAL", ["v_{iy} = v_{i} sin(angle)", "v_{y} = v_{iy} − g t", "Δy = v_{iy} t − ½ g t^{2}"]),
    ("SOLVING FOR t", ["t = [−b ± √(b^{2} − 4ac)] / 2a", "g = 9.8 m/s^{2},  up is +y"]),
]


def mark(paragraph, text, size, color=None, bold=True):
    """Write `text` into the paragraph, turning _{..} and ^{..} into subscript and superscript runs."""
    for part in TOKEN.split(text):
        if not part:
            continue
        if part.startswith("_{"):
            r = run(paragraph, part[2:-1], size, bold=bold, color=color); r.font.subscript = True
        elif part.startswith("^{"):
            r = run(paragraph, part[2:-1], size, bold=bold, color=color); r.font.superscript = True
        else:
            run(paragraph, part, size, bold=bold, color=color)


def _block(doc, pal, label, groups):
    c = one_cell(doc, 7.5)
    para(c, label, 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    t = c.add_table(rows=1, cols=3)
    fix_widths(t, [2.2, 2.4, 2.7])
    tight_cells(t, top=10, bottom=20, left=60, right=40)
    for i, (head, lines) in enumerate(groups):
        cell = t.rows[0].cells[i]
        borders(cell, pal.hair, sz=6, edges=("top",) if False else ("left",) if i else ())
        para(cell, head, 7.5, bold=True, color=pal.label, caps_track=True, first=True)
        for ln in lines:
            p = para(cell, "", 10.5)
            p.paragraph_format.space_after = Pt(3)
            mark(p, ln, 10.5, color=pal.ink)
    return c


def vector_block(doc, pal):
    return _block(doc, pal, "VECTOR EQUATIONS", VECTOR)


def projectile_block(doc, pal):
    return _block(doc, pal, "PROJECTILE EQUATIONS", PROJECTILE)
