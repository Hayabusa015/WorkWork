#!/usr/bin/env python3
"""Build a SHULL quiz (the student copy) from a spec.

    python3 templates/quiz/build_quiz_docx.py <spec.json> <out.docx>

A quiz is not a practice set. A practice set sends students to their notebooks, so the practice-set
builder carries no work space and a card per question. A quiz is written on, so the cards here
are the work space, and short questions share a row so the page is not mostly margin.

Same masthead, palette, fonts and footer as every other SHULL print document. The answer key is
built by build_worksheet_key_docx.py from the same spec, so the two cannot drift.

Spec, one section:
    code, title, directions         plain text; no label, no box
    equations                       short strings; "_x" is a subscript, "^2" a superscript,
                                    "θ" is drawn (the brand face has no theta glyph)
    questions[]                     points, prompt, and either
        inRow: true                 shares one row with the other inRow questions; answerLines
                                    ruled lines under the prompt
        cardHeightIn                the card is this tall, and the blank space is the work area

Theta. The brand face (Archivo) has no Greek, and standards/QA_GATE.md fails a PDF that falls back
to a second font. So theta is set as a small inline picture cut from a Greek-capable face and sized
to the equation text. A picture is not a font, so the page is still Archivo only.
"""
import json, os, sys, tempfile
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from _shull_docx import (          # noqa: E402
    COURSE_CODE, Palette, known_sections, unit_title, borders, para, run, fix_widths,
    no_split, page_setup, running_footer, cell_margins, gap, trim_tail, tight_cells,
    unpad_cell, rule_lines,
)

THETA_FACE = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
THETA_CAP = 0.74            # theta stands about this tall as a fraction of the type size
_TMP = tempfile.mkdtemp(prefix="shull_quiz_")


def refuse(msg):
    print(f"build_quiz_docx: {msg}", file=sys.stderr)
    return 1


def theta_png():
    path = os.path.join(_TMP, "theta.png")
    if not os.path.exists(path):
        from PIL import Image, ImageDraw, ImageFont
        f = ImageFont.truetype(THETA_FACE, 900)
        im = Image.new("L", (1400, 1400), 0)
        ImageDraw.Draw(im).text((200, 200), "θ", font=f, fill=255)
        box = im.getbbox()
        im = im.crop(box)
        out = Image.new("RGBA", im.size, (0, 0, 0, 0))
        out.putalpha(im)
        out.save(path)
        theta_png.aspect = im.width / im.height
    return path


def marked(paragraph, text, size, *, bold=True, color=None):
    """Write `text` into a paragraph, turning _x, ^2 and θ into subscripts, superscripts and a
    drawn theta."""
    buf = ""
    i = 0

    def flush():
        nonlocal buf
        if buf:
            run(paragraph, buf, size, bold=bold, color=color)
            buf = ""

    while i < len(text):
        ch = text[i]
        if ch == "θ":
            flush()
            png = theta_png()
            h = size * THETA_CAP
            pic = paragraph.add_run().add_picture(png, height=Pt(h))
            for att in ("distT", "distB", "distL", "distR"):   # LibreOffice pads an inline picture
                pic._inline.set(att, "0")                       # unless the margins are stated
        elif ch in "_^" and i + 1 < len(text):
            flush()
            r = run(paragraph, text[i + 1], size, bold=bold, color=color)
            if ch == "_":
                r.font.subscript = True
            else:
                r.font.superscript = True
            i += 1
        else:
            buf += ch
        i += 1
    flush()


def masthead(doc, spec, sec, pal):
    unit = f"U{int(spec['unit']):02d}"
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [5.55, 1.95])
    h, hr = t.rows[0].cells
    for cc in (h, hr):
        borders(cc, pal.hair, sz=4, edges=("top", "bottom"))
    borders(h, pal.display, sz=30, edges=("left",))
    cell_margins(h, top=80, bottom=80, left=160, right=80)
    cell_margins(hr, top=80, bottom=80, left=80, right=60)
    para(h, f"UNIT {int(spec['unit'])} — {unit_title(spec['course'], spec['unit']).upper()}", 7.5,
         bold=True, color=pal.accent, caps_track=True, first=True)
    para(h, sec["title"], 15, bold=True, color=pal.ink)
    pp = para(hr, f"{unit} / S{sec['code']}", 11, bold=True, color=pal.accent,
              caps_track=True, first=True)
    pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pp = para(hr, spec.get("docType", "Quiz").replace("_", " ").upper(), 6.5, color=pal.label,
              caps_track=True)
    pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT


def name_row(doc, total, pal):
    gap(doc, 5)
    widths = [3.05, 1.75, 1.10, 1.60]
    t = doc.add_table(rows=1, cols=4)
    fix_widths(t, widths)
    for cc, lab in zip(t.rows[0].cells, ("NAME", "DATE", "PERIOD", "SCORE")):
        borders(cc, pal.ink, sz=4, edges=("bottom",))
        cell_margins(cc, top=0, bottom=40, left=0, right=120)
        p = para(cc, lab, 6.5, bold=True, color=pal.label, caps_track=True, first=True)
        if lab == "SCORE":
            p.paragraph_format.tab_stops.add_tab_stop(Inches(widths[3] - 0.10), WD_TAB_ALIGNMENT.RIGHT)
            run(p, "\t", 9)
            run(p, f"/  {total}", 10, bold=True, color=pal.ink)


def equations(doc, eqs, pal, width=7.5, per_row=3):
    gap(doc, 5)
    t = doc.add_table(rows=1, cols=1)
    fix_widths(t, [width])
    c = t.rows[0].cells[0]
    borders(c, pal.hair, sz=4, edges=("top", "bottom"))
    cell_margins(c, top=60, bottom=40, left=0, right=0)
    p = para(c, "Equations you may use", 9.5, bold=True, color=pal.ink, first=True)
    p.paragraph_format.space_after = Pt(3)
    rows = (len(eqs) + per_row - 1) // per_row
    g = c.add_table(rows=rows, cols=per_row)
    colw = round(width / per_row - 0.02, 2)
    fix_widths(g, [colw] * per_row)
    tight_cells(g, top=20, bottom=30, left=0, right=60)
    for i, eq in enumerate(eqs):
        cell = g.rows[i // per_row].cells[i % per_row]
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        marked(p, eq, 11, bold=True, color=pal.ink)
    unpad_cell(c)


def card(cell, q, n, pal, inner):
    borders(cell, pal.hair, sz=6)
    cell_margins(cell, top=60, bottom=60, left=110, right=110)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(inner), WD_TAB_ALIGNMENT.RIGHT)
    run(p, f"{n}.", 10.5, bold=True, color=pal.ink)
    run(p, "\t", 8)
    run(p, f"{q['points']} pts", 8, color=pal.label)
    lines = int(q.get("answerLines", 0))
    if not lines:
        para(cell, q["prompt"], 10, color=pal.ink)
        return
    # Fixed rows, so the answer lines sit at the same height in every card of the row, whatever
    # the prompt does. (Adjacent ruled paragraphs merge into one line in Word and LibreOffice.)
    inner_t = cell.add_table(rows=1 + lines, cols=1)
    fix_widths(inner_t, [inner])
    tight_cells(inner_t, left=0, right=0)
    no_split(inner_t.rows[0], 0.50)
    para(inner_t.rows[0].cells[0], q["prompt"], 10, color=pal.ink, first=True)
    for r in inner_t.rows[1:]:
        no_split(r, 0.34)
        borders(r.cells[0], pal.hair, sz=4, edges=("bottom",))


def questions(doc, qs, pal):
    n = 0
    row_qs = []
    while n < len(qs) and qs[n].get("inRow"):
        row_qs.append(qs[n]); n += 1
    if row_qs:
        k = len(row_qs)
        gut = 0.10
        colw = round((7.5 - gut * (k - 1)) / k, 3)
        widths = []
        for i in range(k):
            widths.append(colw)
            if i < k - 1:
                widths.append(gut)
        t = doc.add_table(rows=1, cols=len(widths))
        fix_widths(t, widths)
        no_split(t.rows[0], max(float(q.get("cardHeightIn", 1.5)) for q in row_qs))
        for i, q in enumerate(row_qs):
            card(t.rows[0].cells[i * 2], q, i + 1, pal, round(colw - 0.2, 2))
        gap(doc, 6)
    for q in qs[n:]:
        n += 1
        t = doc.add_table(rows=1, cols=1)
        fix_widths(t, [7.5])
        no_split(t.rows[0], q.get("cardHeightIn", 2.5))
        card(t.rows[0].cells[0], q, n, pal, 7.3)
        gap(doc, 6)


def main():
    if len(sys.argv) < 3:
        return refuse("usage: build_quiz_docx.py <spec.json> <out.docx>")
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    course = spec["course"]
    if course not in COURSE_CODE:
        return refuse(f"unknown course {course!r}.")
    bad = [s for s in spec["sections"] if s not in known_sections(course)]
    if bad:
        return refuse(f"section(s) {', '.join(bad)} are not in courses/{course}/DECISIONS.md.")
    sec = spec["sectionsContent"][0]
    pal = Palette(course)
    qs = sec["questions"]
    total = sum(int(q["points"]) for q in qs)

    doc = Document()
    s = page_setup(doc)
    masthead(doc, spec, sec, pal)
    name_row(doc, total, pal)
    gap(doc, 5)
    c = doc.add_table(rows=1, cols=1); fix_widths(c, [7.5])
    cell = c.rows[0].cells[0]
    cell_margins(cell, top=0, bottom=0, left=0, right=0)
    para(cell, sec["directions"], 9.5, color=pal.ink, first=True)
    if sec.get("equations"):
        equations(doc, sec["equations"], pal)
    gap(doc, 6)
    questions(doc, qs, pal)
    unit = f"U{int(spec['unit']):02d}"
    running_footer(s, f"SHULL SCIENCE          {unit} · S{sec['code']} · {sec['title'].upper()}", pal,
                   with_page_numbers=True)
    trim_tail(doc)
    doc.save(sys.argv[2])
    print(f"wrote {sys.argv[2]}  —  {COURSE_CODE[course]} {unit} S{sec['code']} QUIZ, {len(qs)} question(s), {total} points")
    return 0


if __name__ == "__main__":
    sys.exit(main())
