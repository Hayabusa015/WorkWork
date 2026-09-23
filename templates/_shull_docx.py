#!/usr/bin/env python3
"""The .docx primitives every SHULL print builder shares.

Guided notes and worksheets are the same design system on paper. When they each
owned a copy of "how a work box is drawn", the copies drifted within a day: the
notes builder learned that `cantSplit` holds a row and the worksheet builder did
not. A fact lives in exactly one place, and the drawing of a work box is a fact.

Nothing here decides *what* goes on a page. Callers pass their own widths, so a
Cornell notes column and a full-width worksheet share the drawing and not the
geometry.

    from _shull_docx import palette, para, work_box, equation_bar

Colour is read from brand/tokens.json. No hex is typed in this file or in any
file that imports it.
"""
import json, os, re
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
COURSE_CODE = {"chemistry": "CHEM", "physics": "PHYS", "geology": "GEO"}

T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
G = T["ground"]
FONT = T["typography"]["stack"].split(",")[0].strip().strip('"')
FLOOR = T["typography"]["floors"]["printBody"]["pt"]
FOOTER_FLOOR = T["typography"]["floors"]["printFooter"]["pt"]

BULLETS = "•·▸►‣-–— "


def debullet(x):
    """The source packets wrote their own bullets into the text; we supply one."""
    return str(x).lstrip(BULLETS).strip()


def hexof(h):
    return h.lstrip("#").upper()


class Palette:
    """The eight colours a print builder is allowed to use, resolved once.

    `accent` is the text-safe deep course colour; `display` is the brighter one and
    is for rules and borders only - it does not clear contrast as body text.
    """

    def __init__(self, course):
        self.course = course
        self.accent = T["courses"][course]["primaryDeep"]["hex"]
        self.display = T["courses"][course]["primary"]["hex"]
        self.ink = G["asphalt"]["hex"]
        self.hair = G["ruleHairline"]["hex"]
        self.surface = G["parchment"]["hex"]
        self.label = G["label"]["hex"]
        self.footer = G["footer"]["hex"]
        self.white = G["white"]["hex"]

    @property
    def watermark(self):
        """A watermark is defined by ink coverage, not by a colour someone picked.

        `print.watermarkOpacityPct` in tokens.json is the standard; this converts the
        normal band's low end to the grey that puts that much ink on white paper, so
        the number in the design system is the number on the page.
        """
        pct = T["print"]["watermarkOpacityPct"]["normal"][0]
        v = round(255 * (1 - pct / 100.0))
        return "#{0:02X}{0:02X}{0:02X}".format(v)


def known_sections(course):
    text = open(os.path.join(REPO, "courses", course, "DECISIONS.md")).read()
    end = text.find("## Course sequencing rules")
    return set(re.findall(r"(?<![\d.])\d{1,2}\.\d(?![\d])", text[:end] if end > 0 else text))


def unit_title(course, unit):
    """The unit's name, read from that course's DECISIONS.md.

    It is a course fact, so it lives in exactly one place and a spec does not get to
    type it - `validate_layers.py` refuses a spec that does. The three roadmaps are
    formatted differently ("**U7 The Mole...** (7 sections)", "**U1 · Motion...** — 4
    sections", "### U1 · The Universe... — 6 sections"), so all three shapes are read
    rather than one being imposed on files that were correct already.
    """
    text = open(os.path.join(REPO, "courses", course, "DECISIONS.md")).read()
    pat = re.compile(r"^(?:#+\s*)?\*{0,2}U0*%d\b[ ·:—-]*([^*\n(]+?)\*{0,2}\s*(?:\(|—|$)"
                     % int(unit), re.M)
    m = pat.search(text)
    if not m:
        raise SystemExit(f"unit_title: no U{unit} heading in courses/{course}/DECISIONS.md")
    return m.group(1).strip(" ·—-")


def shade(cell, hexval):
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear"); el.set(qn("w:fill"), hexof(hexval))
    cell._tc.get_or_add_tcPr().append(el)


# OOXML fixes the order of the children of w:tcBorders. A file that lists them in
# another order is schema-invalid, and Word repairs it silently while LibreOffice
# may not - so the order is written down once and the merge below respects it.
_BORDER_ORDER = ("top", "start", "left", "bottom", "end", "right", "insideH", "insideV",
                 "tl2br", "tr2bl")


def borders(cell, hexval, sz=6, edges=("top", "left", "bottom", "right"), val="single"):
    """A cell border. `val="dashed"` is the cut line on a cut-and-glue activity - the
    dash is the instruction, so it has to be the border style and not a drawn shape.

    Calls STACK. Two calls on one cell used to append two `w:tcBorders` elements,
    which is invalid - readers were free to take either, and the second call only
    appeared to work because both renderers happened to merge them. It now merges
    into the one element, replacing an edge already set, so a weight ladder can be
    built the obvious way: the hairline box first, then the heavier accent edge.

        borders(cue, pal.hair, sz=8)                       # the box
        borders(cue, pal.display, sz=12, edges=("left",))  # the rail on top of it
    """
    tcPr = cell._tc.get_or_add_tcPr()
    b = tcPr.find(qn("w:tcBorders"))
    if b is None:
        b = OxmlElement("w:tcBorders")
        tcPr.append(b)
    for e in edges:
        old = b.find(qn(f"w:{e}"))
        if old is not None:
            b.remove(old)
        x = OxmlElement(f"w:{e}")
        x.set(qn("w:val"), val); x.set(qn("w:sz"), str(sz))
        x.set(qn("w:color"), hexof(hexval))
        b.append(x)
    order = {n: i for i, n in enumerate(_BORDER_ORDER)}
    for child in sorted(list(b), key=lambda c: order.get(c.tag.split("}")[-1], 99)):
        b.append(child)


def checkbox(paragraph, pal, size=9):
    """An empty tick box, drawn in the brand face rather than borrowed from another.

    U+2610 ☐ is not in Archivo. Setting it pulls DejaVu into the PDF, and the box a
    student actually ticks is then drawn by a font nobody chose - the same failure the
    lab template hit with U+25AA. A bordered run of spaces is a real square in Archivo
    metrics, so the file renders in one face. The space count is measured, not guessed,
    so the box stays square if the size changes.
    """
    sp = " " * max(2, round(size / (text_width_in(" ", size) * 72.0)))
    r = paragraph.add_run(sp)
    r.font.name = FONT
    r.font.size = Pt(size)
    bdr = OxmlElement("w:bdr")
    bdr.set(qn("w:val"), "single"); bdr.set(qn("w:sz"), "6")
    bdr.set(qn("w:space"), "0"); bdr.set(qn("w:color"), hexof(pal.ink))
    r._element.get_or_add_rPr().append(bdr)
    return r


def check_item(cell, text, pal, size=9):
    """A checklist line: a drawn box, then the text."""
    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(0)
    checkbox(p, pal, size)
    run(p, "   " + text, size, color=pal.ink)
    return p


def run(paragraph, text, size, *, bold=False, color=None, italic=False):
    r = paragraph.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = RGBColor.from_string(hexof(color))
    return r


def para(cell, text, size, *, bold=False, color=None, spacing=0.14, caps_track=False, first=False):
    p = cell.paragraphs[0] if first else cell.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(0)
    r = p.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.bold = bold
    if color:
        r.font.color.rgb = RGBColor.from_string(hexof(color))
    if caps_track:
        # True is the standard label tracking; an int is a looser or tighter one, for
        # a label that has to read as quieter than the headings around it. Tracking is
        # part of how loud a caps label is, so demoting one means turning this down as
        # well as the size and the colour.
        val = 26 if caps_track is True else int(caps_track)
        el = OxmlElement("w:spacing"); el.set(qn("w:val"), str(val))
        r._element.get_or_add_rPr().append(el)
    return p


def rule_lines(cell, n, hexval):
    for _ in range(n):
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        pPr = p._p.get_or_add_pPr()
        b = OxmlElement("w:pBdr"); x = OxmlElement("w:bottom")
        x.set(qn("w:val"), "single"); x.set(qn("w:sz"), "4"); x.set(qn("w:color"), hexof(hexval))
        b.append(x); pPr.append(b)


def fix_widths(table, widths):
    """Word autofits tables and will happily discard the column widths python-docx
    sets. Every split in this system is deliberate, so it is pinned: autofit off, a
    fixed layout, and the width written on every cell."""
    table.autofit = False
    tblPr = table._tbl.tblPr
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    for row in table.rows:
        for cell, w in zip(row.cells, widths):
            cell.width = Inches(w)
    for col, w in zip(table.columns, widths):
        col.width = Inches(w)


def gap(doc, pt=6):
    """A vertical gap of exactly `pt` points.

    `doc.add_paragraph()` with a space_after is not a gap of that size - it is a full
    empty body line PLUS the space after it, so a 3pt spacer actually costs about 16pt.
    Six of them between the questions of one section is most of an inch of nothing, and
    on a one-page-per-section sheet that inch is what pushes the closing checklist onto
    a second sheet of paper. Pinning the line makes the gap the size it says it is.
    """
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:before"), "0"); sp.set(qn("w:after"), "0")
    sp.set(qn("w:line"), str(int(pt * 20))); sp.set(qn("w:lineRule"), "exact")
    pPr.append(sp)
    r = p.add_run()
    r.font.name = FONT
    r.font.size = Pt(max(1, pt - 2))
    return p


def trim_tail(doc):
    """Make sure the body ends with a paragraph, and that the paragraph is 1pt.

    OOXML requires the document body to end with a paragraph, and a body built entirely
    out of tables does not have one - python-docx will happily write `</w:tbl></w:body>`.
    Word and LibreOffice both repair that by inserting a paragraph of their own, at full
    body height, and when the content already reaches the bottom of the page that
    inserted paragraph does not fit: the file gains a completely blank final page
    carrying nothing but the running footer.

    So the paragraph is written deliberately and pinned to a 1pt exact line. The file
    becomes valid and the page count is the content's, rather than an artefact of how
    the file had to be built.
    """
    body = doc.element.body
    last = None
    for el in body:
        if el.tag.split("}")[-1] != "sectPr":
            last = el
    def pin(el):
        pPr = el.get_or_add_pPr()
        sp = OxmlElement("w:spacing")
        sp.set(qn("w:before"), "0"); sp.set(qn("w:after"), "0")
        sp.set(qn("w:line"), "20"); sp.set(qn("w:lineRule"), "exact")
        pPr.append(sp)
        rPr = OxmlElement("w:rPr")
        for name in ("w:sz", "w:szCs"):
            e = OxmlElement(name); e.set(qn("w:val"), "2"); rPr.append(e)
        pPr.append(rPr)

    if last is not None and last.tag.split("}")[-1] == "p" \
            and not "".join(last.itertext()).strip():
        pin(last)
        return
    p = doc.add_paragraph()
    pin(p._p)
    sect = body.find(qn("w:sectPr"))
    if sect is not None:
        body.remove(p._p)
        sect.addprevious(p._p)


def cell_margins(cell, top=0, bottom=0, left=40, right=40):
    """Margins on ONE cell, in twentieths of a point.

    Applying them to a whole table is the usual case, but not always the right one: a
    right-aligned tag needs no margin on its left and a real gap on its right, and
    zeroing the row wholesale ran the tag straight into the text it labels.
    """
    mar = OxmlElement("w:tcMar")
    for edge, v in (("top", top), ("bottom", bottom), ("left", left), ("right", right)):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:w"), str(int(v))); e.set(qn("w:type"), "dxa")
        mar.append(e)
    cell._tc.get_or_add_tcPr().append(mar)


def tight_cells(t, top=0, bottom=0, left=40, right=40):
    for row in t.rows:
        for c in row.cells:
            cell_margins(c, top, bottom, left, right)


def one_cell(doc, width=7.5, protect=False):
    """`protect=True` holds the whole block together across a page break (cantSplit) -
    for a box like the section summary, where one orphaned line stranded on an
    otherwise-blank page is worse than the whole box moving down as a unit."""
    t = doc.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.LEFT
    fix_widths(t, [width])
    if protect:
        no_split(t.rows[0])
    return t.rows[0].cells[0]


def no_split(row, height_in=None):
    """Hold a table row together across a page break, and optionally floor its height.

    hRule "atLeast" means the box grows with what a student writes into it and never
    shrinks below the floor. cantSplit holds ONE row - it does nothing across two, so
    anything that must stay together goes in a single row.
    """
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:cantSplit"))
    if height_in is not None:
        h = OxmlElement("w:trHeight")
        h.set(qn("w:val"), str(int(float(height_in) * 1440)))
        h.set(qn("w:hRule"), "atLeast")
        trPr.append(h)


# The fraction bar has to be at least as wide as the widest of numerator and
# denominator or the term wraps inside the fraction, which is worse than a loose bar.
# A character-count guess has to be padded for that safety; the shipped Archivo files
# say exactly how wide the term is, so the pad can be the small optical one a fraction
# bar wants and nothing more.
_FONTS = {}


def text_width_in(text, size_pt, bold=False):
    key = "Bold" if bold else "Regular"
    if key not in _FONTS:
        from fontTools.ttLib import TTFont
        tt = TTFont(os.path.join(REPO, "brand", "fonts", f"Archivo-{key}.ttf"))
        _FONTS[key] = (tt.getBestCmap(), tt["hmtx"], tt["head"].unitsPerEm)
    cmap, hmtx, upem = _FONTS[key]
    total = 0
    for ch in text:
        g = cmap.get(ord(ch))
        total += hmtx[g][0] if g else upem // 2
    return total * size_pt / upem / 72.0


def unpad_cell(cell):
    """Strip the blank paragraphs python-docx leaves around a nested table.

    A cell that gets a table starts with an empty paragraph above it and python-docx
    adds another below (Word requires a cell to end with one). Both are full-size and
    both count toward the row height, so a vertically centred neighbour - the "v  ="
    beside a fraction - centres against that padding and lands above the fraction bar
    instead of on it. The leading blank can go outright; the trailing one has to stay,
    so it is collapsed to 1pt.
    """
    body = cell._tc
    kids = list(body)
    tags = [k.tag.split("}")[-1] for k in kids]
    if "tbl" not in tags:
        return
    first_tbl = tags.index("tbl")
    for k, tag in list(zip(kids, tags))[:first_tbl]:
        if tag == "p" and not "".join(k.itertext()).strip():
            body.remove(k)
    for k, tag in reversed(list(zip(list(body), [x.tag.split("}")[-1] for x in body]))):
        if tag != "p":
            break
        if "".join(k.itertext()).strip():
            break
        pPr = k.get_or_add_pPr()
        rPr = OxmlElement("w:rPr")
        for name in ("w:sz", "w:szCs"):
            e = OxmlElement(name); e.set(qn("w:val"), "2"); rPr.append(e)
        pPr.append(rPr)
        sp = OxmlElement("w:spacing")
        sp.set(qn("w:after"), "0"); sp.set(qn("w:before"), "0")
        sp.set(qn("w:line"), "20"); sp.set(qn("w:lineRule"), "exact")
        pPr.append(sp)
        break


# A stacked fraction, never a/b inline. SHULL_DESIGN_SYSTEM section 8, SHULL-CHG-0017.
# Built as a ruled two-row table rather than Word's own equation objects (OMML):
# OMML is valid and Word renders it, but LibreOffice will not import it from .docx, so
# nothing in this pipeline could see what shipped. A ruled table renders identically in
# Word, LibreOffice, Google Docs and print, and can be checked.
def stacked_frac(cell, num, den, ink_hex, rule_hex, size=10.5):
    t = cell.add_table(rows=2, cols=1)
    tight_cells(t)
    term = max(text_width_in(num, size), text_width_in(den, size))
    fix_widths(t, [max(0.40, round(term + 0.16, 3))])
    top, bot = t.rows[0].cells[0], t.rows[1].cells[0]
    borders(top, rule_hex, sz=6, edges=("bottom",))
    for c, txt in ((top, num), (bot, den)):
        p = para(c, txt, size, color=ink_hex, first=True)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)
    unpad_cell(cell)
    return t


def equation_bar(doc, equations, pal, label, width=7.5):
    """The equations students may reference, at the top of the page.

    His rule: on any Physics or Chemistry sheet with math, the equations go at the top
    so students know what they are allowed to reach for. Two across, no box around the
    block - the only rules on it are the fraction bars, which are the point of it.
    """
    c = one_cell(doc, width)
    para(c, label, 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    cols = 2
    half = round(width / 2 - 0.13, 2)
    rows = (len(equations) + cols - 1) // cols
    t = c.add_table(rows=rows, cols=cols)
    fix_widths(t, [half, half])
    tight_cells(t, top=30, bottom=40, left=0, right=60)
    for i, eq in enumerate(equations):
        cell = t.rows[i // cols].cells[i % cols]
        if eq.get("note"):
            p = para(cell, eq["note"], 7.5, bold=True, color=pal.accent,
                     caps_track=True, first=True)
            p.paragraph_format.space_after = Pt(1)
        if eq.get("num") and eq.get("den"):
            # lhs and the fraction side by side. A nested table always starts its own
            # line, so the equals sign needs its own cell to sit beside the bar.
            inner = cell.add_table(rows=1, cols=2)
            fix_widths(inner, [0.80, half - 1.02])
            tight_cells(inner, left=0, right=0)
            lc, fc = inner.rows[0].cells
            # Middle-aligned so the equals sign lands on the fraction bar, not above it.
            lc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            para(lc, (eq.get("lhs", "") + "  =") if eq.get("lhs") else "", 10.5,
                 bold=True, first=True).alignment = WD_ALIGN_PARAGRAPH.RIGHT
            stacked_frac(fc, eq["num"], eq["den"], pal.ink, pal.hair)
            unpad_cell(cell)
        else:
            para(cell, eq.get("plain", ""), 10.5, bold=True, first=not eq.get("note"))
    return c


def work_box(cell, label, pal, height_in=1.4, width=5.06, watermark=None):
    """An open bordered box a student solves a problem in.

    Ruled lines are for prose; open boxes are for math. The box grows with the work
    and never breaks across a page.

    `watermark` puts a faint centred instruction in the empty space - his ask for the
    Chemistry sheets, "a watermark that says Show work here in the area". Its grey
    comes from print.watermarkOpacityPct in tokens.json, so the ink standard and the
    page agree by construction.
    """
    t = cell.add_table(rows=1, cols=1)
    fix_widths(t, [width])
    no_split(t.rows[0], height_in)
    inner = t.rows[0].cells[0]
    borders(inner, pal.hair, sz=6)
    # The label is read; the border is not. Hairline on white measures 1.6:1.
    if label:
        para(inner, label, 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    if watermark:
        p = para(inner, watermark, 12, color=pal.watermark, caps_track=True,
                 first=not label)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(int(max(6, height_in * 72 * 0.32)))
    return inner


def given_need(cell, given, need, pal, inner_w):
    t = cell.add_table(rows=2, cols=2)
    fix_widths(t, [0.72, inner_w - 0.72])
    for ri, (lab, val) in enumerate((("GIVEN", given), ("NEED", need))):
        a, b = t.rows[ri].cells
        borders(a, pal.hair, sz=4); borders(b, pal.hair, sz=4)
        para(a, lab, 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
        para(b, val, 9.5, first=True)


def fillin_table(cell, spec, pal, inner_w):
    """A small comparison table a student fills in by hand.

    His example: charge/mass/location for proton, neutron, electron was three
    separate "what's the charge, mass, and location of X" questions, asked once per
    particle, each with its own blank lines - the same three-part question in disguise
    three times over. When several open questions are really one row of a comparison
    table, this draws the table instead: one header row naming what belongs in each
    column, then one bordered, hand-writeable row per item.

    `spec` is `{"headers": [...], "rows": [[...], ...], "widths": [...]}`. `widths` is
    optional column fractions of `inner_w` (must sum to ~1); omitted, the first column
    (the row's own label - "Proton", "Cl-35") gets a narrower share than the rest. An
    empty string in a cell is a blank for the student to write in; text there is the
    key's answer, and the key's answers are bold - the same distinction a must-write
    line marks with its rule, made here with weight instead of a line, because a table
    cell has no left edge to draw one on.

    No cell fill anywhere - hairline borders only, the same print-ink rule as
    `given_need` and `diagram_block`. Every body row is `no_split` and floored tall
    enough to hand-write a word or a number into, because a table with zero-height
    blank cells is not a graphic organizer, it is a smaller way to fail a student.
    """
    headers = spec["headers"]
    rows = spec["rows"]
    ncols = len(headers)
    widths = spec.get("widths")
    if widths:
        widths = [round(inner_w * w, 3) for w in widths]
    else:
        label_w = min(round(inner_w * 0.22, 3), 1.15)
        rest_w = round((inner_w - label_w) / (ncols - 1), 3)
        widths = [label_w] + [rest_w] * (ncols - 1)

    t = cell.add_table(rows=1 + len(rows), cols=ncols)
    fix_widths(t, widths)
    tight_cells(t, top=24, bottom=24, left=50, right=50)

    for ci, h in enumerate(headers):
        c = t.rows[0].cells[ci]
        borders(c, pal.hair, sz=4)
        para(c, h, 7.5, bold=True, color=pal.accent, caps_track=True, first=True)

    row_h = float(spec.get("rowHeightIn", 0.34))
    for ri, vals in enumerate(rows):
        tr = t.rows[ri + 1]
        no_split(tr, row_h)
        for ci, val in enumerate(vals):
            c = tr.cells[ci]
            borders(c, pal.hair, sz=4)
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            if ci == 0:
                para(c, val, 9, bold=True, color=pal.ink, first=True)
            else:
                filled = bool(str(val).strip())
                para(c, val, 9.5, bold=filled, color=pal.ink, first=True)
    return t


def diagram_block(cell, dgm, pal, inner_w, base_dir=HERE):
    """A figure students label.

    His example: the layers of the Earth, or a plate boundary with the trench and the
    mid-ocean ridge to identify. The figure gets real room and the label lines are
    numbered beside it, so a student writes on the sheet rather than in a margin.

    The heading and caption live INSIDE the non-splitting row. cantSplit holds ONE row
    and does nothing across two, so kept outside it the heading stranded on the
    previous page while the figure moved to the next - a box with no instruction above
    it, which is worse than no heading at all.
    """
    fig_w = inner_w * 0.61
    t = cell.add_table(rows=1, cols=2)
    fix_widths(t, [fig_w, inner_w * 0.39])
    fig, labels = t.rows[0].cells
    para(fig, dgm.get("label", "LABEL THIS DIAGRAM"), 7.5, bold=True, color=pal.accent,
         caps_track=True, first=True)
    if dgm.get("caption"):
        para(fig, dgm["caption"], 9)
    borders(fig, pal.hair, sz=4)
    no_split(t.rows[0], float(dgm.get("heightIn", 3.0)))
    img = dgm.get("image")
    path = os.path.join(base_dir, img) if img else None
    if path and os.path.exists(path):
        r = fig.add_paragraph().add_run()
        r.add_picture(path, width=Inches(fig_w - 0.20))
        fig.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        # NOT first=True. The heading already claimed paragraph 0, and passing it twice
        # appends a run to the same paragraph instead of making a new one - the heading
        # and the figure note ran together as one line.
        p = para(fig, dgm.get("figureNote", "[ FIGURE ]"), 9, color=pal.hair, caps_track=True)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(10)
    para(labels, "LABEL", 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    for i in range(int(dgm.get("labelSlots", 6))):
        # Just the number. No box, no square, no circle. SHULL-CHG-0015, no exceptions.
        para(labels, f"{i + 1}", 9.5, bold=True, color=pal.ink)
        rule_lines(labels, 1, pal.hair)
    return cell


def page_setup(doc, margin_lr=0.5, margin_tb=0.44, base_pt=10):
    st = doc.styles["Normal"]
    st.font.name = FONT
    st.font.size = Pt(base_pt)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    s = doc.sections[0]
    s.page_width, s.page_height = Inches(8.5), Inches(11)
    s.left_margin = s.right_margin = Inches(margin_lr)
    s.top_margin = s.bottom_margin = Inches(margin_tb)
    return s


def running_footer(section, text, pal, with_page_numbers=False):
    """The footer every printed page carries.

    Outlined and small: printFooter in tokens.json is the only floor a student page is
    allowed below printBody, and this is the exception it exists for.
    """
    f = section.footer.paragraphs[0]
    f.text = text
    for r in f.runs:
        r.font.name = FONT
        r.font.size = Pt(FOOTER_FLOOR)
        r.font.color.rgb = RGBColor.from_string(hexof(pal.footer))
    if with_page_numbers:
        r = f.add_run("          PAGE ")
        r.font.name = FONT; r.font.size = Pt(FOOTER_FLOOR)
        r.font.color.rgb = RGBColor.from_string(hexof(pal.footer))
        _field(f, "PAGE", pal)
        r = f.add_run(" OF ")
        r.font.name = FONT; r.font.size = Pt(FOOTER_FLOOR)
        r.font.color.rgb = RGBColor.from_string(hexof(pal.footer))
        _field(f, "NUMPAGES", pal)
    return f


def fade_to_ink(image_path, target_pct):
    """Wash an image toward white until its darkest tone lays down `target_pct` ink.

    A watermark is defined by ink coverage, not by how someone happened to prepare the
    PNG - the same rule `Palette.watermark` already applies to the text watermark. So
    the template measures the file and washes it to the standard rather than trusting
    it, which has two consequences worth stating:

    - Any course can drop in any image and get the same whisper. The first Chemistry
      watermark was prepared by hand at 15% and printed as a competing graphic behind
      the matter flowchart; nothing in the build could have caught that, because the
      ink level lived in a PNG.
    - It is idempotent. An already-faded file measures at or under target and is
      returned untouched, so re-running a build does not wash the image away one pass
      at a time - the failure mode of doing this with a fixed blend factor.

    The darkest tone is read at the 0.05th percentile, not the outright minimum, so one
    stray dark pixel or a JPEG ringing artefact cannot decide the exposure of the whole
    image. Returns a PNG stream for `add_picture`, or None if no fade was needed.
    """
    from PIL import Image
    im = Image.open(image_path)
    if im.mode in ("RGBA", "LA", "P"):
        im = Image.alpha_composite(
            Image.new("RGBA", im.size, (255, 255, 255, 255)), im.convert("RGBA"))
    im = im.convert("RGB")

    hist = im.convert("L").histogram()
    n = sum(hist)
    floor_n = max(1, int(n * 0.0005))
    seen, darkest = 0, 255
    for v, k in enumerate(hist):
        seen += k
        if seen >= floor_n:
            darkest = v
            break
    have = (255 - darkest) / 255.0 * 100.0
    if have <= target_pct + 0.5:
        return None
    f = target_pct / have
    washed = Image.eval(im, lambda v: int(round(255 - (255 - v) * f)))
    import io
    buf = io.BytesIO()
    washed.save(buf, format="PNG")
    buf.seek(0)
    return buf


def add_watermark(section, image_path, width_in, *, ink_pct=None, vert_frac=0.5):
    """A faint background image, floating behind the text, repeating on every page.

    `ink_pct` is the darkest tone the watermark is allowed to print, defaulting to the
    low end of print.watermarkOpacityPct.denseTable in tokens.json - every print
    template this system has is a page of ruled tables, and the design system says a
    watermark on one is reduced rather than normal.

    `vert_frac` is where the picture's CENTRE sits down the page, as a fraction of page
    height. 0.5 is dead centre, which is where content is: centred, the Chemistry atom
    ran through the matter flowchart, the work box and the fill-in prompts on three
    different pages. Lower than centre puts it in the quiet bottom third of a page
    whose weight is at the top, so it reads as a ground rather than as a second layer
    of drawing competing with the first.

    python-docx has no watermark API. `header.paragraphs[0].add_run().add_picture()`
    only produces an INLINE picture - in the header's text flow, not floating and not
    behind the body - so it would push the header down rather than sit under the page.
    The reliable recipe, and the one that survives `soffice --headless --convert-to
    pdf` (this pipeline's PDF path) as well as Word: insert the picture the normal
    inline way, then rewrite the `<wp:inline>` that call produced into a `<wp:anchor>`
    carrying `behindDoc="1"`, reusing the same `<a:graphic>` payload rather than
    re-embedding the image. Centred on the page in both axes, so it does not have to
    be re-measured against the page size if that ever changes.

    One header holds every page a document doesn't split into a new section - this
    template never does - so this is called once per document, not once per page.

    Position is an explicit offset, in EMU, computed from the page size and the
    picture's own rendered extent, rather than `<wp:align>center</wp:align>` - the
    same centred position, measured instead of named.

    `header_distance` is pulled in to the body's own top margin before anything is
    added. python-docx's default header distance (0.5in) is WIDER than this
    template's 0.44in top margin, and that gap is invisible with an empty header -
    but the moment the header holds real content, LibreOffice's DOCX import reads it
    as real space the body must clear, shaving a few points off every page's usable
    height. On a page that already lands its last line at the very bottom - this
    template's title page does - that was enough to overflow a single trailing
    paragraph onto a page of its own, and the whole document gained a spurious blank
    page. Pulling the header in under the margin removes the gap it was measuring.
    """
    header = section.header
    if section.header_distance > section.top_margin:
        section.header_distance = section.top_margin
    p = header.paragraphs[0]
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    if ink_pct is None:
        ink_pct = T["print"]["watermarkOpacityPct"]["denseTable"][0]
    src = fade_to_ink(image_path, ink_pct) or image_path
    pic = run.add_picture(src, width=Inches(width_in))
    inline = pic._inline
    extent, graphic = inline.extent, inline.graphic
    docPr = inline.docPr
    docPr.set("id", "1")
    docPr.set("name", "Watermark")
    frame_locks = inline.find(qn("wp:cNvGraphicFramePr"))

    page_w = section.page_width
    page_h = section.page_height
    off_x = max(0, (page_w - extent.cx) // 2)
    off_y = int(min(max(0, page_h * vert_frac - extent.cy / 2), max(0, page_h - extent.cy)))

    anchor = OxmlElement("wp:anchor")
    for k, v in (("behindDoc", "1"), ("distT", "0"), ("distB", "0"), ("distL", "0"),
                 ("distR", "0"), ("simplePos", "0"), ("locked", "0"),
                 ("layoutInCell", "1"), ("allowOverlap", "1"), ("relativeHeight", "1")):
        anchor.set(k, v)

    simple_pos = OxmlElement("wp:simplePos")
    simple_pos.set("x", "0"); simple_pos.set("y", "0")

    pos_h = OxmlElement("wp:positionH"); pos_h.set("relativeFrom", "page")
    off_h = OxmlElement("wp:posOffset"); off_h.text = str(int(off_x)); pos_h.append(off_h)
    pos_v = OxmlElement("wp:positionV"); pos_v.set("relativeFrom", "page")
    off_v = OxmlElement("wp:posOffset"); off_v.text = str(int(off_y)); pos_v.append(off_v)

    new_extent = OxmlElement("wp:extent")
    new_extent.set("cx", str(extent.cx)); new_extent.set("cy", str(extent.cy))
    effect_extent = OxmlElement("wp:effectExtent")
    for e in ("l", "t", "r", "b"):
        effect_extent.set(e, "0")
    wrap_none = OxmlElement("wp:wrapNone")

    for el in (simple_pos, pos_h, pos_v, new_extent, effect_extent, wrap_none,
               docPr, frame_locks, graphic):
        if el is not None:
            anchor.append(el)

    inline.getparent().replace(inline, anchor)
    return anchor


def study_recap_page(doc, recap, pal, width=7.5, row_height_in=4.4):
    """The standing last page: a 2x2 grid of outlined boxes a student studies from.

    His ask: "a nice little recap infographic ... topic breakdown, key points,
    notable confusing points, things to remember" on the last page, every unit. In
    this design system an infographic is structure and type hierarchy, not colour or
    fill - hairline borders, no cell shading, the same print-ink rule as every other
    page. `recap` is `{"title", "topics", "keyPoints", "confusingPoints", "remember"}`,
    each list a handful of short strings.

    Callers add the page break that puts this on its own page and call it last, so
    nothing this system builds ever follows the recap.
    """
    doc.add_page_break()
    gap(doc, 10)
    c = one_cell(doc, width)
    borders(c, pal.ink, sz=12, edges=("top",))
    borders(c, pal.display, sz=18, edges=("bottom",))
    cell_margins(c, top=70, bottom=70, left=40, right=40)
    para(c, recap.get("title", "STUDY RECAP"), 15, bold=True, color=pal.ink, first=True)

    gap(doc, 7)
    half = round(width / 2 - 0.06, 2)
    boxes = [
        ("TOPIC BREAKDOWN", recap.get("topics", [])),
        ("KEY POINTS", recap.get("keyPoints", [])),
        ("WATCH OUT FOR", recap.get("confusingPoints", [])),
        ("REMEMBER", recap.get("remember", [])),
    ]
    t = doc.add_table(rows=2, cols=2)
    fix_widths(t, [half, half])
    tight_cells(t, top=60, bottom=60, left=70, right=70)
    # The recap is a page, not a block that happens to land last. Sized only by its
    # own text it filled the top 40% of the sheet and left the rest blank, which
    # reads as an unfinished page rather than a composed one - and gave a student
    # nowhere to add a line of their own to a box they are supposed to study from.
    # Each half takes the height that is actually there. hRule "atLeast", so a course
    # with more recap content than this one still grows past the floor.
    for r in t.rows:
        no_split(r, float(row_height_in))
    for i, (lab, items) in enumerate(boxes):
        cell = t.rows[i // 2].cells[i % 2]
        borders(cell, pal.hair, sz=6)
        # The same rail the cue column carries, so the recap reads as the last page
        # of THIS packet rather than a generic four-box organizer.
        borders(cell, pal.display, sz=12, edges=("left",))
        para(cell, lab, 8.5, bold=True, color=pal.accent, caps_track=True, first=True)
        for x in items:
            para(cell, "•  " + debullet(x), 9.5, color=pal.ink)
    return t


def _field(paragraph, instr, pal):
    """A Word field. Page numbers have to be computed by the reader, not by us -
    a worksheet that says "page 2 of 3" in fixed text lies the moment it is edited."""
    r = paragraph.add_run()
    r.font.name = FONT; r.font.size = Pt(FOOTER_FLOOR)
    r.font.color.rgb = RGBColor.from_string(hexof(pal.footer))
    beg = OxmlElement("w:fldChar"); beg.set(qn("w:fldCharType"), "begin")
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve")
    it.text = f" {instr} "
    end = OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"), "end")
    r._r.append(beg); r._r.append(it); r._r.append(end)
    return r
