#!/usr/bin/env python3
"""Build the Physics S2.2 quizzes, keys and grader sheet as one-page .docx files.

    python3 templates/quiz/build_quiz_docx.py OUTDIR

Writes, named per standards/NAMING.md (templates/_shull_name.py):
    2.2 Quiz A.docx  /  B  /  C                 student copies
    2.2 Quiz A Key.docx  /  B  /  C             teacher keys, key text in keyInk.pen
    2.2 Quiz - Grade Sheet.docx                 final answers for all three versions

Every answer comes from vectors_22.py, which solves it in code. Colour is read from
brand/tokens.json; none is typed here. Every file is one page: the builder converts each with
LibreOffice and stops if a file runs to two.
"""
import os, subprocess, sys, tempfile
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
import vectors_22 as V                                            # noqa: E402
from _shull_name import document_name                             # noqa: E402
from _shull_docx import (T, FONT, Palette, hexof, borders, para, rule_lines, fix_widths, gap,  # noqa: E402
                         one_cell, equation_bar, work_box, page_setup, running_footer,
                         trim_tail, schema_order, tight_cells)

KEY_INK = T["keyInk"]["pen"]["hex"]          # written answers on a key (standards/ANSWER_KEYS.md)
DIRECTIONS = ("Show your work in the boxes and write questions 1–3 on the lines. Box your final answers with units. Round calculations "
              "to two significant figures. Angles on the 0–360° scale start at east and run "
              "counterclockwise: north is 90°, west is 180°, south is 270°. A negative angle runs "
              "clockwise from east. Any correct way of writing a direction counts.")
EQUATIONS = [
    {"plain": "Rx = R cos(angle)"}, {"plain": "Ry = R sin(angle)"},
    {"plain": "tan(angle) = Ry / Rx"}, {"plain": "R² = Rx² + Ry²"},
    {"plain": "Rx = Ax + Bx"}, {"plain": "Ry = Ay + By"},
]
POINTS = (2, 2, 2, 5, 5)


def new_doc(pal, footer_text):
    doc = Document()
    sec = page_setup(doc, margin_lr=0.5, margin_tb=0.44, base_pt=10)
    running_footer(sec, footer_text, pal)
    return doc


def header(doc, pal, subtitle, key=False, right="U02 / S02.2"):
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [5.6, 1.9])
    a, b = t.rows[0].cells
    for c in (a, b):
        borders(c, pal.display, sz=18, edges=("bottom",))
    para(a, "SHULL SCIENCE  ·  JAMES A. GARFIELD LOCAL SCHOOLS", 7.5, bold=True, color=pal.type_accent
         if hasattr(pal, "type_accent") else pal.accent, caps_track=True, first=True)
    para(a, V.TITLE_LINES[0], 15, bold=True, color=pal.ink)
    para(a, subtitle + ("  ·  TEACHER KEY" if key else ""), 8.5, bold=True,
         color=KEY_INK if key else pal.label, caps_track=True)
    p = para(b, right, 9, bold=True, color=pal.accent, caps_track=True, first=True)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    return t


def fields_row(doc, pal):
    gap(doc, 4)
    t = doc.add_table(rows=1, cols=4)
    fix_widths(t, [3.0, 1.7, 1.3, 1.5])
    for c, lab in zip(t.rows[0].cells, ("NAME", "DATE", "PERIOD", f"SCORE        / {V.TOTAL}")):
        borders(c, pal.hair, sz=6)
        para(c, lab, 8.5, bold=True, color=pal.label, caps_track=True, first=True)
        c.paragraphs[0].paragraph_format.space_after = Pt(9)


def directions(doc, pal):
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, DIRECTIONS, 8.5, color=pal.ink, first=True)


def q_block(doc, pal, n, pts, text, box_in, label=None):
    gap(doc, 5)
    c = one_cell(doc)
    p = para(c, f"{n}.   {pts} pts", 8, bold=True, color=pal.accent, caps_track=True, first=True)
    para(c, text, 10)
    work_box(c, "", pal, box_in, 7.2)
    return c


# ---- student quiz -----------------------------------------------------------------------

def student(L, d, out):
    pal = Palette("physics")
    doc = new_doc(pal, f"SHULL SCIENCE / PHYSICS / UNIT 02 / QUIZ {L}")
    header(doc, pal, f"{V.TITLE_LINES[1]}, VERSION {L}")
    fields_row(doc, pal)
    directions(doc, pal)
    gap(doc, 3)
    equation_bar(doc, EQUATIONS, pal, "EQUATIONS YOU MAY USE")
    gap(doc, 5)
    t = doc.add_table(rows=1, cols=3)
    fix_widths(t, [2.5, 2.5, 2.5])
    tight_cells(t, top=30, bottom=30, left=60, right=60)
    for c, it in zip(t.rows[0].cells, d["restate"]):
        borders(c, pal.hair, sz=6)
        para(c, f"{it['n']}.   2 pts", 8, bold=True, color=pal.accent, caps_track=True, first=True)
        para(c, f"Restate {it['given']} in two other ways.", 10)
        rule_lines(c, 2, pal.hair)
    q_block(doc, pal, 4, 5, d["v"]["q4"]["text"], 1.8)
    q_block(doc, pal, 5, 5, d["v"]["q5"]["text"], 2.85)
    finish(doc, out)


# ---- teacher key ------------------------------------------------------------------------

def kp(cell, text, size=8.5, bold=False, key=True, first=False, pal=None):
    return para(cell, text, size, bold=bold, color=KEY_INK if key else pal.ink, first=first)


def sgn(x, nd=2):
    return f"{x:.{nd}f}".replace("-", "−")


def term(x, nd=2):
    """A term in a sum: negatives are bracketed, positives are not."""
    return f"({sgn(x, nd)})" if x < 0 else sgn(x, nd)


def key_doc(L, d, out):
    pal = Palette("physics")
    doc = new_doc(pal, f"SHULL SCIENCE / PHYSICS / UNIT 02 / QUIZ {L} / TEACHER KEY")
    header(doc, pal, f"{V.TITLE_LINES[1]}, VERSION {L}", key=True)
    gap(doc, 4)
    c = one_cell(doc); borders(c, pal.hair)
    para(c, "Q1–3: one point for each correct restatement, two needed. Accept the 0–360 form, the negative "
            "form, or either compass form. Q4–5: points listed per question. Round to two significant "
            "figures; a missing unit or reference axis costs the point shown.", 8, color=pal.label, first=True)
    gap(doc, 4)
    t = doc.add_table(rows=1, cols=3)
    fix_widths(t, [2.5, 2.5, 2.5])
    tight_cells(t, top=30, bottom=30, left=60, right=60)
    for c, it in zip(t.rows[0].cells, d["restate"]):
        borders(c, pal.hair, sz=6)
        para(c, f"{it['n']}.   2 pts", 8, bold=True, color=pal.accent, caps_track=True, first=True)
        para(c, f"Restate {it['given']}.", 9.5, color=pal.ink)
        e = it["eq"]
        kp(c, "Accept any two of:", 8, bold=True)
        for k in ("deg", "neg", "c1", "c2"):
            if k != it["given_key"]:
                kp(c, "•  " + e[k])
    q4, q5 = d["q4"], d["q5"]
    v4, v5 = d["v"]["q4"], d["v"]["q5"]
    u4, u5 = v4["unit"], v5["unit"]
    # Q4
    gap(doc, 5)
    c = one_cell(doc)
    para(c, "4.   5 pts", 8, bold=True, color=pal.accent, caps_track=True, first=True)
    para(c, v4["text"], 9.5, color=pal.ink)
    x, y = v4["x"], v4["y"]
    lab = (lambda v: f"{abs(v):.1f}") if u4 == "m/s" else (lambda v: f"{abs(v):g}")
    kp(c, f"R² = Rx² + Ry² = ({lab(x)})² + ({lab(y)})²,  so  R = {q4['R']:.2f}, round to {V.two_sf(q4['R'])} {u4}")
    if v4.get("frame") == "v":      # direction told from the north axis
        import math
        ang = math.degrees(math.atan(abs(x) / abs(y)))
        kp(c, f"tan(angle) = {lab(x)} / {lab(y)} measured from north, so the angle is {ang:.1f}, round to {ang:.0f}°")
    else:
        kp(c, f"tan(angle) = {lab(y)} / {lab(x)}, so the reference angle is {q4['ref']:.1f}, round to {q4['ref']:.0f}°")
    other = q4["eq"]["c1"] if v4.get("frame") == "v" else q4["eq"]["c2"]
    kp(c, f"Answer: {V.two_sf(q4['R'])} {u4} at {q4['stated']}.  Also correct: {q4['eq']['deg']}, {q4['eq']['neg']}, "
          f"{other}.", bold=True)
    para(c, "Points: 1 setup for R · 1 R with units · 1 angle setup · 1 angle value · 1 direction named "
            "(axis or 0–360).", 7.5, color=pal.label)
    # Q5
    gap(doc, 5)
    c = one_cell(doc)
    para(c, "5.   5 pts", 8, bold=True, color=pal.accent, caps_track=True, first=True)
    para(c, v5["text"], 9.5, color=pal.ink)
    for (m, th), (ax, ay), name in zip(q5["vs"], q5["parts"], ("A", "B")):
        kp(c, f"{name} = {m:g} {u5} at {th:.0f}°:   {name}x = {m:g} cos {th:.0f}° = {sgn(ax)} {u5}      "
              f"{name}y = {m:g} sin {th:.0f}° = {sgn(ay)} {u5}")
    kp(c, f"Rx = {term(q5['parts'][0][0])} + {term(q5['parts'][1][0])} = {sgn(q5['rx'])} {u5}      "
          f"Ry = {term(q5['parts'][0][1])} + {term(q5['parts'][1][1])} = {sgn(q5['ry'])} {u5}")
    ref = abs(__import__("math").degrees(__import__("math").atan(abs(q5["ry"]) / abs(q5["rx"]))))
    kp(c, f"R = √({term(q5['rx'])}² + {term(q5['ry'])}²) = {q5['R']:.2f}, round to {V.two_sf(q5['R'])} {u5}.   "
          f"Reference angle = arctan({abs(q5['ry']):.2f} / {abs(q5['rx']):.2f}) = {ref:.1f}°")
    kp(c, f"Answer: {V.two_sf(q5['R'])} {u5} at {q5['stated']}.  Also correct: {q5['eq']['deg']}, {q5['eq']['neg']}, "
          f"{q5['eq']['c2']}.", bold=True)
    para(c, "Points: 1 components of A · 1 components of B · 1 Rx and Ry sums · 1 R with units · 1 direction "
            "with a named reference.", 7.5, color=pal.label)
    gap(doc, 5)
    c = one_cell(doc); borders(c, pal.hair)
    para(c, "Common errors: dropping the sign of a component in the 2nd–4th quadrants · giving R with no direction · "
            "calling a 3rd-quadrant result “north of west” · rounding the components too early. Judgment calls: give "
            "full credit for a direction stated from either axis if the reference is named.", 8, color=pal.label, first=True)
    finish(doc, out)


# ---- grader sheet -----------------------------------------------------------------------

def grade_sheet(data, out):
    pal = Palette("physics")
    doc = new_doc(pal, "SHULL SCIENCE / PHYSICS / UNIT 02 / QUIZ GRADE SHEET / TEACHER USE ONLY")
    header(doc, pal, "QUIZ GRADE SHEET", key=True)
    gap(doc, 4)
    c = one_cell(doc)
    para(c, f"Forms A / B / C · 5 questions · {V.TOTAL} points per version. Final answers only, for fast "
            "grading against a stack of papers. Any correct form of a direction earns the point. "
            "Point-by-point work is in the separate Key files.", 8.5, color=pal.ink, first=True)
    gap(doc, 5)
    cols = [0.35, 1.2, 0.45, 1.83, 1.83, 1.84]
    t = doc.add_table(rows=1 + len(POINTS), cols=6)
    fix_widths(t, cols)
    tight_cells(t, top=40, bottom=40, left=60, right=60)
    heads = ("Q", "TOPIC", "PTS", "VERSION A", "VERSION B", "VERSION C")
    for c, h in zip(t.rows[0].cells, heads):
        borders(c, pal.ink, sz=8, edges=("bottom",))
        para(c, h, 8, bold=True, color=pal.accent, caps_track=True, first=True)
    topics = ("Restate a direction", "Restate a direction", "Restate a direction",
              "Add perpendicular vectors", "Add two vectors at angles")
    for qi in range(5):
        row = t.rows[1 + qi].cells
        for c in row:
            borders(c, pal.hair, sz=4, edges=("bottom",))
        para(row[0], str(qi + 1), 10, bold=True, color=pal.ink, first=True)
        para(row[1], topics[qi], 8.5, color=pal.ink, first=True)
        para(row[2], str(POINTS[qi]), 9, color=pal.ink, first=True)
        for ci, L in enumerate("ABC"):
            d, cell = data[L], row[3 + ci]
            if qi < 3:
                it = d["restate"][qi]; e = it["eq"]
                forms = [e[k + "s"] if k in ("c1", "c2") else e[k]
                         for k in ("deg", "neg", "c1", "c2") if k != it["given_key"]]
                para(cell, f"given {it['given']}", 7.5, color=pal.label, first=True)
                para(cell, "  ·  ".join(forms), 8.5, bold=True, color=KEY_INK)
            elif qi == 3:
                q = d["q4"]; u = d["v"]["q4"]["unit"]
                para(cell, f"{V.two_sf(q['R'])} {u}", 10, bold=True, color=KEY_INK, first=True)
                para(cell, f"{q['stated']}", 8.5, bold=True, color=KEY_INK)
                para(cell, f"= {q['eq']['deg']} = {q['eq']['neg']}", 8, color=KEY_INK)
            else:
                q = d["q5"]; u = d["v"]["q5"]["unit"]
                para(cell, f"{V.two_sf(q['R'])} {u}", 10, bold=True, color=KEY_INK, first=True)
                para(cell, f"{q['stated']}", 8.5, bold=True, color=KEY_INK)
                para(cell, f"= {q['eq']['deg']} = {q['eq']['neg']}", 8, color=KEY_INK)
    gap(doc, 6)
    c = one_cell(doc)
    para(c, f"TOTAL {V.TOTAL} PTS PER VERSION", 8, bold=True, color=pal.accent, caps_track=True, first=True)
    gap(doc, 5)
    c = one_cell(doc)
    para(c, "SCORE TO PERCENT", 8, bold=True, color=pal.accent, caps_track=True, first=True)
    n = V.TOTAL + 1
    t2 = c.add_table(rows=2, cols=n)
    fix_widths(t2, [round(7.3 / n, 3)] * n)
    tight_cells(t2, top=30, bottom=30, left=20, right=20)
    for i in range(n):
        pts = V.TOTAL - i
        for r, txt, bold in ((0, str(pts), True), (1, f"{int(100 * pts / V.TOTAL + 0.5)}", False)):
            cell = t2.rows[r].cells[i]
            borders(cell, pal.hair, sz=4)
            p = para(cell, txt, 8.5, bold=bold, color=pal.ink, first=True)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para(c, "Top row: points earned out of 16. Bottom row: percent, rounded half up.", 7.5, color=pal.label)
    finish(doc, out)


# ---- output -----------------------------------------------------------------------------

def finish(doc, out):
    trim_tail(doc)
    schema_order(doc)
    doc.save(out)


def pages(path):
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", td, path],
                       check=True, capture_output=True)
        pdf = os.path.join(td, os.path.splitext(os.path.basename(path))[0] + ".pdf")
        out = subprocess.run(["pdfinfo", pdf], check=True, capture_output=True, text=True).stdout
    return int([l for l in out.splitlines() if l.startswith("Pages")][0].split()[1])


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
    os.makedirs(outdir, exist_ok=True)
    data = V.build()
    made = []
    for L in "ABC":
        p = os.path.join(outdir, document_name("Quiz", ["2.2"], 2, version=L)); student(L, data[L], p); made.append(p)
        p = os.path.join(outdir, document_name("Quiz", ["2.2"], 2, version=L, key=True)); key_doc(L, data[L], p); made.append(p)
    p = os.path.join(outdir, document_name("Quiz", ["2.2"], 2, descriptor="Grade Sheet")); grade_sheet(data, p); made.append(p)
    bad = 0
    for p in made:
        n = pages(p)
        print(f"{'ok ' if n == 1 else 'BAD'} {n} page  {os.path.basename(p)}")
        bad += n != 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
