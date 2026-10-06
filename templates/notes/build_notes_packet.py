#!/usr/bin/env python3
"""Build a multi-section guided-notes PACKET as .docx: cover, sections, review page.

An extension of build_notes_docx.py, not a replacement. It reuses every primitive from
templates/_shull_docx.py and the recall rule from recall.py, and adds what a whole-unit
packet needs that the single-header builder does not have:

  - a cover page with the unit at a glance (no difficulty ratings)
  - every section starts on a new page
  - a slide tag on each row, so notes are keyed to the deck's footer numbers
  - table blocks and orbital-diagram blocks
  - a review page that closes the packet
  - two outputs from one spec: the student copy (blanks) and the key (answers)

Blanks are written in the spec as {{answer}}. The student copy draws a ruled blank sized
to the answer; the key prints the answer. Superscripts are ^x^.

    python3 templates/notes/build_notes_packet.py specs/<spec>.json student.docx key.docx
"""
import json, os, re, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recall                                         # noqa: E402
sys.path.insert(0, os.path.dirname(HERE))
from _shull_docx import (                              # noqa: E402
    FONT, COURSE_CODE, Palette, hexof, debullet, known_sections, unit_title,
    borders, check_item, rule_lines, fix_widths, one_cell, no_split, gap,
    diagram_block, page_setup, running_footer, trim_tail, para,
)

TEXT_W_IN = 7.50
CUE_W_IN = 1.28
NOTES_W_IN = TEXT_W_IN - CUE_W_IN
NOTES_INNER_IN = round(NOTES_W_IN - 0.56, 2)

TOKEN = re.compile(r"(\{\{.*?\}\}|\^[^^]*\^)")


def plain(text):
    return re.sub(r"\^([^^]*)\^", r"\1", re.sub(r"\{\{(.*?)\}\}", r"\1", text))


class Ctx:
    def __init__(self, pal, key):
        self.pal, self.key = pal, key
        self.empty = False      # table cells: no ruled blank, the cell is the place to write


def _run(p, text, size, *, bold=False, color=None, sup=False, underline=False):
    r = p.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.bold = bold
    r.underline = underline
    if sup:
        r.font.superscript = True
    if color:
        r.font.color.rgb = RGBColor.from_string(hexof(color))
    return r


def rich(p, text, size, ctx, *, bold=False, color=None, inblank=False):
    """Write marked-up text into paragraph p. {{x}} is a blank; ^x^ is a superscript."""
    color = color or ctx.pal.ink
    parts = [x for x in TOKEN.split(text) if x]
    for i, part in enumerate(parts):
        nxt = parts[i + 1] if i + 1 < len(parts) else ""
        if part.startswith("{{"):
            ans = part[2:-2]
            if ctx.key:
                rich(p, ans, size, ctx, bold=True, color=ctx.pal.accent, inblank=True)
            elif ctx.empty:
                continue
            else:
                n = max(6, int(round(len(plain(ans)) * 1.1)) + 1)
                tail = "" if nxt[:1] in ("-", ".", ",", ";", ")", "") else " "
                _run(p, " " + "_" * n + tail, size, color=color)
        elif part.startswith("^"):
            _run(p, part[1:-1], size, bold=bold or inblank and ctx.key, color=color, sup=True)
        else:
            _run(p, part, size, bold=bold or (inblank and ctx.key), color=color,
                 underline=(inblank and ctx.key))
    return p


def rpara(cell, text, size, ctx, *, first=False, bold=False, color=None, after=2):
    p = cell.paragraphs[0] if first else cell.add_paragraph()
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.space_before = Pt(0)
    rich(p, text, size, ctx, bold=bold, color=color)
    return p


def spacer(cell, pt=3):
    """A gap of exactly pt points inside a cell. An empty para() costs a full body line."""
    p = cell.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:before"), "0"); sp.set(qn("w:after"), "0")
    sp.set(qn("w:line"), str(int(pt * 20))); sp.set(qn("w:lineRule"), "exact")
    pPr.append(sp)
    r = p.add_run(); r.font.size = Pt(1); r.font.name = FONT


def must_write(p, pal):
    pPr = p._p.get_or_add_pPr()
    bd = OxmlElement("w:pBdr"); x = OxmlElement("w:left")
    x.set(qn("w:val"), "single"); x.set(qn("w:sz"), "18")
    x.set(qn("w:space"), "6"); x.set(qn("w:color"), hexof(pal.display))
    bd.append(x)
    sp = pPr.find(qn("w:spacing"))          # schema order: pBdr comes before spacing
    if sp is not None:
        sp.addprevious(bd)
    else:
        pPr.append(bd)


def page_break_before(doc):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.page_break_before = True
    pPr = p._p.get_or_add_pPr()
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:before"), "0"); sp.set(qn("w:after"), "0")
    sp.set(qn("w:line"), "20"); sp.set(qn("w:lineRule"), "exact")
    pPr.append(sp)
    r = p.add_run(); r.font.size = Pt(1); r.font.name = FONT


def cell_margins(cell, top=40, bottom=40, left=70, right=70):
    tcPr = cell._tc.get_or_add_tcPr()
    m = OxmlElement("w:tcMar")
    for k, v in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        e = OxmlElement(f"w:{k}"); e.set(qn("w:w"), str(v)); e.set(qn("w:type"), "dxa"); m.append(e)
    tcPr.append(m)


def data_table(cell, tbl, ctx, inner_w):
    """A bordered table nested in a notes cell. Header row is ruled, never filled."""
    pal = ctx.pal
    hdr, rows = tbl["headers"], tbl["rows"]
    widths = tbl.get("widths") or [inner_w / len(hdr)] * len(hdr)
    scale = inner_w / sum(widths)
    widths = [w * scale for w in widths]
    t = cell.add_table(rows=1 + len(rows), cols=len(hdr))
    fix_widths(t, widths)
    ctx.empty = True
    for i, h in enumerate(hdr):
        c = t.rows[0].cells[i]
        borders(c, pal.display, sz=12, edges=("bottom",))
        cell_margins(c)
        p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        rich(p, h, 8.5, ctx, bold=True, color=pal.accent)
    no_split(t.rows[0])
    for ri, row in enumerate(rows, start=1):
        no_split(t.rows[ri], 0.25)
        for ci, txt in enumerate(row):
            c = t.rows[ri].cells[ci]
            borders(c, pal.hair, sz=4)
            cell_margins(c, top=30, bottom=30)
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            rich(p, txt, 9.5, ctx, bold=(ci == 0 and len(hdr) <= 4))
    ctx.empty = False
    spacer(cell, 4)
    return t


def orbital_block(cell, ob, ctx, inner_w):
    """Boxes with arrows: one row per sublevel, one bordered box per orbital."""
    pal = ctx.pal
    para(cell, ob.get("label", "ORBITAL DIAGRAM"), 7.5, bold=True, color=pal.accent,
         caps_track=True)
    box_w = 0.46
    name_w = 1.35
    maxb = max(r["boxes"] for r in ob["rows"])
    t = cell.add_table(rows=len(ob["rows"]), cols=1 + maxb)
    fix_widths(t, [name_w] + [box_w] * maxb)
    for ri, row in enumerate(ob["rows"]):
        no_split(t.rows[ri], 0.36)
        nc = t.rows[ri].cells[0]
        nc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = nc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        _run(p, row["name"], 9.5, bold=True, color=pal.ink)
        for bi in range(maxb):
            c = t.rows[ri].cells[1 + bi]
            if bi >= row["boxes"]:
                continue
            borders(c, pal.accent, sz=8)
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            fill = row["fill"][bi] if bi < len(row["fill"]) else ""
            if ctx.key and fill:
                _run(p, fill, 12, bold=True, color=pal.accent)
    spacer(cell, 4)


def space_block(cell, sp, ctx):
    """Room to write. Student copy: ruled lines. Key: the expected notes."""
    if ctx.key:
        for line in sp["key"]:
            rpara(cell, line, 9.5, ctx, bold=True, color=ctx.pal.accent)
    else:
        rule_lines(cell, sp["lines"], ctx.pal.hair)


def sketch_block(cell, sk, ctx, inner_w):
    pal = ctx.pal
    para(cell, sk["label"], 7.5, bold=True, color=pal.accent, caps_track=True)
    t = cell.add_table(rows=1, cols=1)
    fix_widths(t, [inner_w])
    no_split(t.rows[0], sk.get("heightIn", 1.7))
    c = t.rows[0].cells[0]; borders(c, pal.hair, sz=6)
    p = c.paragraphs[0]
    if ctx.key:
        _run(p, sk["key"], 9, bold=True, color=pal.accent)
    spacer(cell, 4)


def figure_block(cell, dgm, ctx, inner_w):
    """The figure students sketch, with numbered label lines. Key prints the labels."""
    pal = ctx.pal
    diagram_block(cell, dgm, pal, inner_w, HERE)
    if ctx.key and dgm.get("labels"):
        # The label slots are in the last nested table; write the answers beside the numbers.
        t = cell.tables[-1]
        lab = t.rows[0].cells[1]
        paras = [p for p in lab.paragraphs if p.text.strip().isdigit()]
        for p, txt in zip(paras, dgm["labels"]):
            _run(p, "  " + txt, 8.5, bold=True, color=pal.accent)


def build(spec, out, key):
    course = spec["course"]
    pal = Palette(course)
    ctx = Ctx(pal, key)
    unit = f"U{int(spec['unit']):02d}"
    code = COURSE_CODE[course]
    secs = spec["sections"]
    span = f"S{int(secs[0].split('.')[0]):02d}.{secs[0].split('.')[1]}-S{int(secs[-1].split('.')[0]):02d}.{secs[-1].split('.')[1]}"
    ut = unit_title(course, spec["unit"])

    doc = Document()
    s = page_setup(doc)

    # ---------------- Cover ----------------
    c = one_cell(doc); borders(c, pal.display, sz=24, edges=("bottom",))
    para(c, "SHULL SCIENCE  ·  JAMES A. GARFIELD LOCAL SCHOOLS", 8, bold=True,
         color=pal.accent, caps_track=True, first=True)
    para(c, f"CHEMISTRY  ·  UNIT {int(spec['unit'])}", 11, bold=True, color=pal.label, caps_track=True)
    para(c, ut.upper(), 30, bold=True, color=pal.ink)
    para(c, spec["kicker"] + ("  ·  TEACHER KEY" if key else ""), 8, color=pal.label, caps_track=True)
    gap(doc, 6)
    c = one_cell(doc); borders(c, pal.hair)
    para(c, spec["fields"], 9, color=pal.label, first=True)

    gap(doc, 10)
    c = one_cell(doc); borders(c, pal.ink, sz=12, edges=("top",))
    borders(c, pal.display, sz=18, edges=("bottom",))
    para(c, "UNIT AT A GLANCE", 9, bold=True, color=pal.ink, caps_track=True, first=True)
    g = doc.add_table(rows=1 + len(spec["glance"]), cols=4)
    widths = [0.75, 2.55, 0.85, 3.35]
    fix_widths(g, widths)
    for i, h in enumerate(["SECTION", "TOPIC", "SLIDES", "YOU WILL RECORD"]):
        cc = g.rows[0].cells[i]; borders(cc, pal.hair, sz=4, edges=("bottom",))
        cell_margins(cc, top=60, bottom=60)
        p = cc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        _run(p, h, 7.5, bold=True, color=pal.accent)
    for ri, row in enumerate(spec["glance"], start=1):
        no_split(g.rows[ri], 0.62)
        vals = [row["code"], row["title"], row["slides"], row["record"]]
        for ci, v in enumerate(vals):
            cc = g.rows[ri].cells[ci]; borders(cc, pal.hair, sz=4, edges=("bottom",))
            cc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            cell_margins(cc, top=70, bottom=70)
            p = cc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            _run(p, v, 11 if ci == 0 else 10, bold=(ci < 2), color=pal.accent if ci == 0 else pal.ink)

    gap(doc, 12)
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [3.75, 3.75])
    for i, (lab, items) in enumerate([("UNIT LEARNING TARGETS", spec["unitTargets"]),
                                      ("KEY TERMS", spec["keyTerms"])]):
        cell = t.rows[0].cells[i]; borders(cell, pal.hair)
        para(cell, lab, 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
        for x in items:
            para(cell, "•  " + debullet(x), 9.5)

    gap(doc, 8)
    c = one_cell(doc); borders(c, pal.display, sz=18, edges=("left",))
    para(c, "HOW THESE NOTES WORK", 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    for x in spec["howItWorks"]:
        para(c, "•  " + debullet(x), 9.5)

    # ---------------- Opener + sections ----------------
    def head_bar(title, code=None, slides=None):
        t = doc.add_table(rows=1, cols=2)
        fix_widths(t, [5.63, 1.87])
        a, b = t.rows[0].cells
        for cell in (a, b):
            borders(cell, pal.ink, sz=12, edges=("top",))
            borders(cell, pal.display, sz=18, edges=("bottom",))
        para(a, title, 14, bold=True, color=pal.ink, first=True)
        first = True
        if code:
            p = para(b, code, 8.5, bold=True, color=pal.accent, caps_track=True, first=True)
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            first = False
        p = para(b, slides.upper(), 7.5, bold=True, color=pal.label, caps_track=True, first=first)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    def rows_table(rows):
        t = doc.add_table(rows=len(rows), cols=2)
        fix_widths(t, [CUE_W_IN, NOTES_W_IN])
        for ri, row in enumerate(rows):
            no_split(t.rows[ri])
            cue, notes = t.rows[ri].cells
            borders(cue, pal.hair); borders(notes, pal.hair)
            tag = "SLIDE " + row["slides"] if "–" not in row["slides"] else "SLIDES " + row["slides"]
            para(cue, tag, 7.5, bold=True, color=pal.ink, first=True)
            para(cue, row["cueLabel"], 7, bold=True, color=pal.accent)
            for q in row["cues"]:
                rpara(cue, q, 8.5, ctx)
            para(notes, row["notesLabel"], 7.5, bold=True, color=pal.accent,
                 caps_track=True, first=True)
            if row.get("space"):
                space_block(notes, row["space"], ctx)
            if row.get("table"):
                data_table(notes, row["table"], ctx, NOTES_INNER_IN)
            if row.get("sketch"):
                sketch_block(notes, row["sketch"], ctx, NOTES_INNER_IN)
            if row.get("orbitals"):
                orbital_block(notes, row["orbitals"], ctx, NOTES_INNER_IN)

    op = spec.get("opener")
    if op:
        page_break_before(doc)
        head_bar(op["title"], None, op["slidesRange"])
        gap(doc, 2)
        rows_table(op["rows"])

    for si, sec in enumerate(spec["sectionsContent"]):
        if op and si == 0:
            gap(doc, 10)           # the opener is part of the unit, not a section of its own
        else:
            page_break_before(doc)
        head_bar(sec["title"], sec["code"], sec["slidesRange"])
        c = one_cell(doc); borders(c, pal.hair)
        p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(2)
        _run(p, "LEARNING TARGET   ", 7.5, bold=True, color=pal.accent)
        _run(p, sec["learningTarget"], 9.5, color=pal.ink)
        rows_table(sec["rows"])

        gap(doc, 6)
        c = one_cell(doc); borders(c, pal.accent)
        para(c, "SECTION SUMMARY — the big ideas, in your own words", 7.5,
             bold=True, color=pal.accent, caps_track=True, first=True)
        space_block(c, sec["summary"], ctx)
        no_split(doc.tables[-1].rows[0])

    # ---------------- Review page ----------------
    rv = spec["review"]
    page_break_before(doc)
    c = one_cell(doc); borders(c, pal.ink, sz=12, edges=("top",))
    borders(c, pal.display, sz=18, edges=("bottom",))
    para(c, rv["banner"], 10, bold=True, color=pal.ink, caps_track=True, first=True)
    gap(doc, 4)
    t = doc.add_table(rows=1 + len(rv["rows"]), cols=3)
    fix_widths(t, [0.65, 2.0, 4.85])
    for i, h in enumerate(["SECTION", "RECALL", "WRITE IT"]):
        cc = t.rows[0].cells[i]; borders(cc, pal.display, sz=12, edges=("bottom",))
        cell_margins(cc)
        p = cc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        _run(p, h, 7.5, bold=True, color=pal.accent)
    for ri, row in enumerate(rv["rows"], start=1):
        no_split(t.rows[ri], 0.52)
        for ci, v in enumerate(row):
            cc = t.rows[ri].cells[ci]; borders(cc, pal.hair, sz=4)
            cell_margins(cc, top=60, bottom=60)
            cc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cc.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
            if ci == 0:
                _run(p, v, 8.5, bold=True, color=pal.accent)
            elif ci == 1:
                _run(p, v, 9, bold=True, color=pal.ink)
            elif ctx.key:
                rich(p, v, 9.5, ctx, bold=True, color=pal.accent)
    gap(doc, 8)
    c = one_cell(doc); borders(c, pal.hair)
    para(c, rv["fuzzyLabel"], 8.5, bold=True, color=pal.accent, caps_track=True, first=True)
    rule_lines(c, 3, pal.hair)

    running_footer(s, f"SHULL SCIENCE          {unit} · {span}" + ("          TEACHER KEY" if key else ""),
                   pal, with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)
    print(f"wrote {out}")


def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    valid = known_sections(spec["course"])
    bad = [x for x in spec["sections"] if x not in valid]
    if bad:
        print(f"build_notes_packet: {', '.join(bad)} not in courses/{spec['course']}/DECISIONS.md",
              file=sys.stderr)
        return 1
    if recall.check(spec, "build_notes_packet"):
        return 1
    build(spec, sys.argv[2], key=False)
    build(spec, sys.argv[3], key=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
