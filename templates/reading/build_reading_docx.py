#!/usr/bin/env python3
"""Build a unit reading (textbook-style chapter) and its answer key as .docx, then PDF.

    python3 templates/reading/build_reading_docx.py templates/reading/specs/<spec>.json OUT_DIR
        [--no-pdf] [--no-figures]

PILOT DOCUMENT TYPE. standards/NAMING.md has no "Reading" type yet; the spec carries the
working filenames Matt gave until a NAMING proposal settles it.

What it makes, from one spec so the student copy and the key cannot drift:

    student   page 1: the shared print header (SHULL-CHG-0101), Name/Date/Period, how to
              read the chapter, a vocabulary self-rating table. Then the chapter in two
              columns (SHULL-CHG-0023 line length): section heads, sub-heads, prose with
              bold defined terms, numbered figures with captions, Example boxes, and a
              boxed Reading Check closing every section. Then, on new pages, the three
              questions (Day 1 answer | End-of-unit revision) and vocabulary in your own
              words.
    key       the shared header, teacher notes, then every Reading Check answer, the
              exemplar answers to the questions, and the accepted vocabulary definitions.
              Answers are in the key-handwriting face and keyInk.pen
              (standards/ANSWER_KEYS.md section 2), digits in the face's fallback
              (section 7, legibility).

Spec markup in text: **bold**, *italic*, _{subscript}, ^{superscript}.

Colour comes from brand/tokens.json through _shull_docx.Palette; no hex is typed here.
Course colour is a thin accent only: rules and box edges in the course `primary`, label
type in the text-safe `primaryDeep`. Fills: none.
"""
import json, os, re, shutil, subprocess, sys, tempfile

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.dirname(HERE)
sys.path.insert(0, TEMPLATES)
sys.path.insert(0, os.path.join(TEMPLATES, "notes"))
from _shull_docx import (  # noqa: E402
    T, FONT, NARROW, REPO, Palette, unit_title, hexof, known_sections, borders, fix_widths, cell_margins,
    no_split, page_setup, print_header, checkbox, apply_binding, schema_order, trim_tail,
    text_width_in, TEXT_W_IN,
)
from build_notes_docx import _spacing, footer as notes_footer, pin  # noqa: E402

# ---------------------------------------------------------------------------------
# Geometry and type. Body size is printScale.body from tokens.json. The column gap is set
# so a body line lands inside the 50-75 character band; main() measures it and refuses a
# build outside the band.
COL_GAP_IN = 0.30
COL_W_IN = round((TEXT_W_IN - COL_GAP_IN) / 2, 3)
FIG_W_IN = 3.30
DIRECTIONS_W_IN = 4.40          # full-width directions held under ~75 characters a line
MARGIN_TOP_IN = 0.45
MARGIN_BOTTOM_IN = 0.64          # the ruled running footer lives in here (notes geometry)

BODY = T["typography"]["printScale"]["body"]
BODY_LINE = round(BODY * 1.26, 1)   # tightened from 1.33 when the Connection boxes were added (QA_GATE §2 order)
SUB = 10.5
SEC_NUM, SEC_TITLE = 15, 15
CAPTION, CAPTION_LINE = 8.5, 11
LABEL = 8                        # caps labels sit on the print floor, never under it
WRITE_LINE_PT = 22               # one handwriting line
W_HAIR = 6                       # eighths of a point: 0.75 pt, print.weights.writingLine
W_ACCENT = 18                    # the course rule under a section head, 2.25 pt

HAND = T["typography"]["keyHandwriting"]["family"]
HAND_FALLBACK = re.search(r"Fallback for any missing glyph: ([^.]+)\.",
                          T["typography"]["keyHandwriting"]["note"]).group(1).strip()
PEN = T["keyInk"]["pen"]["hex"]

# ---------------------------------------------------------------------------------
# Text with markup.
_TOK = re.compile(r"(\*\*.+?\*\*|\*[^*]+?\*|_\{[^}]*\}|\^\{[^}]*\})")


def tokens(text):
    """-> [(chunk, bold, italic, vert)] where vert is None / 'subscript' / 'superscript'.
    Bold may contain sub/superscripts ("**18.02 g/mol**", "**2.00 mol H_{2}O**")."""
    out = []

    def plain(s, b=False, i=False):
        for part in re.split(r"(_\{[^}]*\}|\^\{[^}]*\})", s):
            if not part:
                continue
            if part.startswith("_{"):
                out.append((part[2:-1], b, i, "subscript"))
            elif part.startswith("^{"):
                out.append((part[2:-1], b, i, "superscript"))
            else:
                out.append((part, b, i, None))

    for piece in re.split(r"(\*\*.+?\*\*)", str(text)):
        if piece.startswith("**") and piece.endswith("**") and len(piece) > 4:
            plain(piece[2:-2], b=True)
        else:
            for sub in re.split(r"((?<!\*)\*[^*\s][^*]*?\*(?!\*))", piece):
                if sub.startswith("*") and sub.endswith("*") and len(sub) > 2:
                    plain(sub[1:-1], i=True)
                else:
                    plain(sub)
    return out


def _font(r, face):
    r.font.name = face
    rpr = r._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), face)


def add(p, text, size, *, color=None, bold=False, italic=False, face=None, track=None):
    last = None
    for chunk, b, i, vert in tokens(text):
        r = p.add_run(chunk)
        _font(r, face or FONT)
        r.font.size = Pt(size)
        r.bold = bold or b
        r.italic = italic or i
        if vert == "subscript":
            r.font.subscript = True
        elif vert == "superscript":
            r.font.superscript = True
        if color:
            r.font.color.rgb = RGBColor.from_string(hexof(color))
        if track:
            el = OxmlElement("w:spacing"); el.set(qn("w:val"), str(int(track)))
            r._element.get_or_add_rPr().append(el)
        last = r
    return last


def plain_text(text):
    return "".join(c for c, *_ in tokens(text))


def keep_next(p, on=True):
    p.paragraph_format.keep_with_next = on
    return p


def bottom_rule(p, color, sz=W_HAIR, space=1):
    pPr = p._p.get_or_add_pPr()
    b = pPr.find(qn("w:pBdr"))
    if b is None:
        b = OxmlElement("w:pBdr"); pPr.append(b)
    x = OxmlElement("w:bottom")
    x.set(qn("w:val"), "single"); x.set(qn("w:sz"), str(sz))
    x.set(qn("w:space"), str(space)); x.set(qn("w:color"), hexof(color))
    b.append(x)


def para_in(container, first=False):
    if first and container.paragraphs and not container.paragraphs[0].runs:
        return container.paragraphs[0]
    return container.add_paragraph()


def label(container, text, pal, *, first=False, before=0, after=2):
    p = para_in(container, first)
    _spacing(p, before, after, LABEL * 1.35)
    add(p, text.upper(), LABEL, color=pal.accent, bold=True, track=26)
    return p


def body_p(container, text, pal, *, first=False, before=0, after=5, size=BODY, line=BODY_LINE,
           color=None, align=None):
    p = para_in(container, first)
    _spacing(p, before, after, line)
    add(p, text, size, color=color or pal.ink)
    if align is not None:
        p.alignment = align
    return p


def write_lines(cell, n, pal, first=False, width=None):
    """N writing lines as the rows of a table, each row exactly one handwriting line tall
    with a hairline under it. Ruled paragraphs do not work: consecutive paragraphs with
    the same bottom border are one border group, and both readers draw only the last."""
    if first and cell.paragraphs and not cell.paragraphs[0].runs:
        pin(cell.paragraphs[0], 1)
    t = cell.add_table(rows=n, cols=1)
    if width:
        fix_widths(t, [width])
    for row in t.rows:
        tr = row._tr.get_or_add_trPr()
        h = OxmlElement("w:trHeight")
        h.set(qn("w:val"), str(int(WRITE_LINE_PT * 20))); h.set(qn("w:hRule"), "exact")
        tr.append(h)
        c = row.cells[0]
        cell_margins(c, 0, 0, 0, 0)
        borders(c, pal.hair, sz=W_HAIR, edges=("bottom",))
        pin(c.paragraphs[0], 1)
    return t


def box_check(cell, pal, side_in=0.15):
    """An empty tick box: a tiny bordered table centred in the cell. Not U+2610 (not in
    Archivo, it pulls in a second font) and not a bordered run of spaces
    (_shull_docx.checkbox): LibreOffice drew nothing for that run in a centred cell."""
    t = cell.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    fix_widths(t, [side_in])
    row = t.rows[0]
    tr = row._tr.get_or_add_trPr()
    h = OxmlElement("w:trHeight")
    h.set(qn("w:val"), str(int(side_in * 1440))); h.set(qn("w:hRule"), "exact")
    tr.append(h)
    c = row.cells[0]
    cell_margins(c, 0, 0, 0, 0)
    borders(c, pal.ink, sz=6)
    pin(c.paragraphs[0], 1)
    end_cell(cell)
    return t


def end_cell(cell):
    """A cell must end with a paragraph; after a nested table python-docx leaves a full
    body line. Pin it to 1 pt so it costs nothing."""
    last = cell.paragraphs[-1]
    if not last.runs and not last.text:
        pin(last, 1)


# ---------------------------------------------------------------------------------
# Hand-written key text (standards/ANSWER_KEYS.md). Each character goes to the key face
# unless it is a digit (legibility, section 7) or the face lacks it; then the named
# fallback; then the brand face as a last resort.
_CMAPS = {}


def _cmap(face_file):
    if face_file not in _CMAPS:
        from fontTools.ttLib import TTFont
        _CMAPS[face_file] = set(TTFont(os.path.join(REPO, "brand", "fonts", face_file)).getBestCmap())
    return _CMAPS[face_file]


# Characters this face renders ambiguously, found on the first rendered key (ANSWER_KEYS.md
# section 7): M reads as H ("Holar mass"), the colon prints as a heavy dot, the hyphen
# sits high like a macron, and the times sign is a letter x.
HAND_AMBIGUOUS = set("M:;-%\u00d7")


def _face_for(ch):
    if ch.isspace():
        return HAND
    if not ch.isdigit() and ch not in HAND_AMBIGUOUS and ord(ch) in _cmap(HAND.replace(" ", "") + ".ttf"):
        return HAND
    if ord(ch) in _cmap(HAND_FALLBACK.replace(" ", "") + "-Regular.ttf"):
        return HAND_FALLBACK
    return FONT


def hand(p, text, size=12):
    for chunk, b, i, vert in tokens(text):
        groups, cur, face = [], "", None
        # element symbols whose lowercase l reads as I in the key face (NaCl, Cl-)
        forced = {k for m in re.finditer(r"Cl(?![a-z])", chunk) for k in (m.start(), m.start() + 1)}
        for idx, ch in enumerate(chunk):
            f = HAND_FALLBACK if idx in forced else _face_for(ch)
            if face is not None and f != face and not ch.isspace():
                groups.append((cur, face)); cur = ""
            if not ch.isspace() or face is None:
                face = f if not ch.isspace() or face is None else face
            cur += ch
        if cur:
            groups.append((cur, face or HAND))
        for s, f in groups:
            r = p.add_run(s)
            _font(r, f)
            r.font.size = Pt(size)
            r.font.color.rgb = RGBColor.from_string(hexof(PEN))
            if vert == "subscript":
                r.font.subscript = True
            elif vert == "superscript":
                r.font.superscript = True


# ---------------------------------------------------------------------------------
# Building blocks.

def stacked(cell, num, den, pal, size=BODY):
    """A stacked fraction (SHULL_DESIGN_SYSTEM section 8, SHULL-CHG-0017), the shared
    ruled two-row construction from _shull_docx.stacked_frac, with markup in the terms."""
    t = cell.add_table(rows=2, cols=1)
    for row in t.rows:
        for c in row.cells:
            cell_margins(c, 0, 0, 30, 30)
    w = max(text_width_in(plain_text(num), size), text_width_in(plain_text(den), size))
    fix_widths(t, [max(0.40, round(w + 0.16, 3))])
    top, bot = t.rows[0].cells[0], t.rows[1].cells[0]
    borders(top, pal.ink, sz=6, edges=("bottom",))
    for c, txt in ((top, num), (bot, den)):
        p = c.paragraphs[0]
        _spacing(p, 0, 0, size * 1.45)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add(p, txt, size, color=pal.ink)
    return t


def math_row(container, parts, pal, width, size=BODY):
    """text | fraction | text on one line, centred in `width`. A nested table always
    starts its own line, so each part has its own cell."""
    widths = []
    for part in parts:
        if isinstance(part, dict):
            widths.append(max(text_width_in(plain_text(part["num"]), size),
                              text_width_in(plain_text(part["den"]), size)) + 0.30)
        else:
            widths.append(text_width_in(plain_text(part), size, bold="**" in part) + 0.16)
    total = sum(widths)
    if total > width:
        raise SystemExit(f"math row {parts!r} is {total:.2f} in, wider than {width:.2f} in")
    t = container.add_table(rows=1, cols=len(parts))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    fix_widths(t, widths)
    for c, part in zip(t.rows[0].cells, parts):
        cell_margins(c, 0, 0, 20, 20)
        c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        if isinstance(part, dict):
            p = c.paragraphs[0]
            stacked(c, part["num"], part["den"], pal, size)
            pin(p, 1)
            end_cell(c)
        else:
            p = c.paragraphs[0]
            _spacing(p, 0, 0, size * 1.45)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add(p, part.replace("  ", "  "), size, color=pal.ink)
    no_split(t.rows[0])
    return t


def section_head(doc, blk, pal):
    p = doc.add_paragraph()
    _spacing(p, 9, 5, SEC_TITLE * 1.25)
    keep_next(p)
    p.paragraph_format.keep_together = True
    r = add(p, blk["code"] + "  ", SEC_NUM, color=pal.accent, bold=True, face=NARROW)
    add(p, blk["title"], SEC_TITLE, color=pal.ink, bold=True, face=NARROW)
    bottom_rule(p, pal.display, W_ACCENT, 2)
    return p


def sub_head(doc, text, pal):
    p = doc.add_paragraph()
    _spacing(p, 5, 2, SUB * 1.3)
    keep_next(p)
    add(p, text, SUB, color=pal.ink, bold=True)
    return p


def figure(doc, blk, pal, fig_dir):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(2)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    keep_next(p)
    path = os.path.join(fig_dir, blk["image"])
    r = p.add_run()
    # FIG_W_IN, not the full column: at 3.50 in LibreOffice let Figure 7.2 run 0.08 in into
    # the binding margin of an even page (audit #3). check_margins() measures every image.
    r.add_picture(path, width=Inches(FIG_W_IN))
    c = doc.add_paragraph()
    _spacing(c, 0, 6, CAPTION_LINE)
    add(c, f"Figure {blk['n']} — ", CAPTION, color=pal.ink, bold=True)
    add(c, blk["caption"], CAPTION, color=pal.label)
    return c


def box(doc, pal, accent=False):
    t = doc.add_table(rows=1, cols=1)
    fix_widths(t, [COL_W_IN])
    c = t.rows[0].cells[0]
    borders(c, pal.hair, sz=W_HAIR)
    if accent:
        borders(c, pal.display, sz=W_ACCENT, edges=("left",))
    cell_margins(c, top=70, bottom=90, left=140, right=110)
    no_split(t.rows[0])
    return c


def after_box(doc, pt_=7):
    p = doc.add_paragraph()
    pin(p, pt_)


def example(doc, blk, pal):
    c = box(doc, pal)
    label(c, f"Example {blk['n']}", pal, first=True)
    p = para_in(c)
    _spacing(p, 0, 4, 13)
    add(p, blk["title"], BODY, color=pal.ink, bold=True)
    inner = COL_W_IN - (140 + 110) / 1440
    if blk.get("intro"):
        body_p(c, blk["intro"], pal, after=4, size=9.5, line=12.5)
    if blk.get("rows"):
        widths = [0.50, 1.60, 0.22, inner - 0.50 - 1.60 - 0.22 - 0.02]
        t = c.add_table(rows=len(blk["rows"]), cols=4)
        fix_widths(t, widths)
        for ri, row in enumerate(blk["rows"]):
            for cc, txt in zip(t.rows[ri].cells, row):
                cell_margins(cc, 30, 30, 20, 20)
                cc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                q = cc.paragraphs[0]
                _spacing(q, 0, 0, 13)
                q.alignment = WD_ALIGN_PARAGRAPH.CENTER          # SHULL-CHG-0105
                add(q, txt, 9.5, color=pal.ink)
                if ri == len(blk["rows"]) - 1:
                    borders(cc, pal.ink, sz=6, edges=("top",))
                else:
                    borders(cc, pal.hair, sz=4, edges=("bottom",))
    if blk.get("math"):
        math_row(c, blk["math"], pal, inner, size=9.5)
        pin(c.paragraphs[-1], 1)        # the paragraph python-docx adds after a nested table
    if blk.get("after"):
        body_p(c, blk["after"], pal, before=4, after=0, size=9.5, line=12.5)
    end_cell(c)
    after_box(doc)


def opener(doc, blk, pal):
    """The chapter opener ("Why It Matters"): a caps label and one paragraph a little
    larger than the body. No box - it is the chapter's introduction, not a task."""
    label(doc, blk["title"], pal, before=2, after=3)
    p = body_p(doc, blk["text"], pal, size=BODY + 0.5, line=round((BODY + 0.5) * 1.33, 1), after=4)
    bottom_rule(p, pal.display, 12, 6)
    q = doc.add_paragraph(); pin(q, 6)


def connection(doc, blk, pal):
    """A real-world sidebar. Told apart from the Reading Check by shape, not only by
    colour: the Check is a closed box with a course rail on the left and writing lines;
    a Connection is open at the sides, a course rule above and a hairline below, and
    smaller type with no lines to write on."""
    t = doc.add_table(rows=1, cols=1)
    fix_widths(t, [COL_W_IN])
    c = t.rows[0].cells[0]
    borders(c, pal.display, sz=12, edges=("top",))
    borders(c, pal.hair, sz=W_HAIR, edges=("bottom",))
    cell_margins(c, top=60, bottom=80, left=0, right=0)
    no_split(t.rows[0])
    q = label(c, "Connection", pal, first=True, after=1)
    add(q, "   " + blk["title"], 9, color=pal.ink, bold=True)
    body_p(c, blk["text"], pal, after=0, size=9.5, line=12.6)
    end_cell(c)
    after_box(doc, 6)


def reading_check(doc, blk, pal):
    c = box(doc, pal, accent=True)
    label(c, f"Reading Check {blk['n']}", pal, first=True)
    body_p(c, blk["q"], pal, after=0, size=BODY, line=BODY_LINE)
    write_lines(c, int(blk.get("lines", 3)), pal, width=COL_W_IN - (140 + 110) / 1440)
    end_cell(c)
    after_box(doc, 6)


def steps(doc, blk, pal):
    for i, s in enumerate(blk["items"], 1):
        p = doc.add_paragraph()
        _spacing(p, 0, 3, BODY_LINE)
        pf = p.paragraph_format
        pf.left_indent = Inches(0.24)
        pf.first_line_indent = Inches(-0.24)
        pf.tab_stops.add_tab_stop(Inches(0.24))
        add(p, f"{i}.\t", BODY, color=pal.ink, bold=True)     # just the number, SHULL-CHG-0015
        add(p, s, BODY, color=pal.ink)
    doc.paragraphs[-1].paragraph_format.space_after = Pt(6)


def equation(doc, blk, pal):
    p = doc.add_paragraph()
    _spacing(p, 3, 6, 16)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add(p, blk["text"].replace("  ", "  "), 11.5, color=pal.ink, bold=True)


# ---------------------------------------------------------------------------------
# Sections and columns.

def set_cols(section, n, space_in=COL_GAP_IN):
    sp = section._sectPr
    cols = sp.find(qn("w:cols"))
    if cols is None:
        cols = OxmlElement("w:cols")
        # after pgNumType / before docGrid; schema position is checked below
        dg = sp.find(qn("w:docGrid"))
        (dg.addprevious(cols) if dg is not None else sp.append(cols))
    cols.set(qn("w:num"), str(n))
    cols.set(qn("w:space"), str(int(space_in * 1440)))
    if n > 1:
        cols.set(qn("w:equalWidth"), "1")


def footers(doc, ctx):
    for i, s in enumerate(doc.sections):
        if i:
            s.footer.is_linked_to_previous = False
        notes_footer(s, ctx)


def name_row(doc, pal):
    t = doc.add_table(rows=1, cols=6)
    widths = [0.50, 3.40, 0.45, 1.35, 0.62, 1.06]
    fix_widths(t, widths)
    for i, (c, txt) in enumerate(zip(t.rows[0].cells, ["NAME", "", "DATE", "", "PERIOD", ""])):
        cell_margins(c, 0, 20, 0, 40)
        c.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
        p = c.paragraphs[0]
        _spacing(p, 0, 0, 14)
        if txt:
            add(p, txt, LABEL, color=pal.label, bold=True, track=26)
        else:
            borders(c, pal.label, sz=6, edges=("bottom",))
    return t


def vocab_preview(doc, spec, pal):
    fr = spec["front"]
    terms = [v["term"] for v in spec["vocab"]]
    half = (len(terms) + 1) // 2
    cols3 = fr["vocabColumns"]
    gap = 0.20
    side = (TEXT_W_IN - gap) / 2
    cw = 0.68
    widths = [side - 3 * cw] + [cw] * 3 + [gap] + [side - 3 * cw] + [cw] * 3
    t = doc.add_table(rows=half + 1, cols=9)
    fix_widths(t, widths)
    for ri, row in enumerate(t.rows):
        no_split(row)
        for ci, c in enumerate(row.cells):
            cell_margins(c, 14, 14, 30, 30)
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER          # SHULL-CHG-0105
            _spacing(p, 0, 0, 12)
            if ci == 4:
                continue
            k = ci if ci < 4 else ci - 5
            idx = (ri - 1) + (0 if ci < 4 else half)
            edges = ("bottom",)
            if ri == 0:
                txt = "Term" if k == 0 else cols3[k - 1]
                add(p, txt.upper(), LABEL, color=pal.accent, bold=True, track=0)
                borders(c, pal.ink, sz=6, edges=edges)
                continue
            borders(c, pal.hair, sz=4, edges=edges)
            if idx >= len(terms):
                continue
            if k == 0:
                add(p, terms[idx], 9, color=pal.ink, bold=True)
            else:
                pin(p, 1)
                box_check(c, pal)
    return t


def front(doc, spec, pal):
    fr = spec["front"]
    name_row(doc, pal)
    p = doc.add_paragraph(); pin(p, 7)
    t = doc.add_table(rows=1, cols=1)
    fix_widths(t, [TEXT_W_IN])
    c = t.rows[0].cells[0]
    cell_margins(c, 0, 0, 0, 0)
    label(c, fr["howTitle"], pal, first=True, after=3)
    # the how-to note reads across the full width; two short paragraphs side by side
    # would keep it near 60 characters a line, so it is set as two columns of its own
    inner = c.add_table(rows=1, cols=2)
    fix_widths(inner, [COL_W_IN, TEXT_W_IN - COL_W_IN])
    for i, (cc, txt) in enumerate(zip(inner.rows[0].cells, fr["how"])):
        cell_margins(cc, 0, 0, 0 if i == 0 else int(COL_GAP_IN * 1440), 0)
        body_p(cc, txt, pal, first=True, after=0, size=9.5, line=12.6)
    end_cell(c)
    p = doc.add_paragraph(); pin(p, 6)
    t2 = doc.add_table(rows=1, cols=1)
    fix_widths(t2, [TEXT_W_IN])
    c2 = t2.rows[0].cells[0]
    cell_margins(c2, 0, 0, 0, 0)
    q = label(c2, fr["vocabTitle"], pal, first=True, after=0)
    add(q, "   " + fr["vocabDirections"], 9, color=pal.label)
    end_cell(c2)
    vocab_preview(doc, spec, pal)
    p = doc.add_paragraph(); pin(p, 4)


def back_pages(doc, spec, pal):
    bk = spec["back"]
    p = doc.add_paragraph()
    _spacing(p, 0, 2, SEC_TITLE * 1.25)
    add(p, bk["questionsTitle"], SEC_TITLE, color=pal.ink, bold=True, face=NARROW)
    bottom_rule(p, pal.display, W_ACCENT, 2)
    q = body_p(doc, bk["questionsDirections"], pal, before=4, after=8, size=9.5, line=12.6)
    q.paragraph_format.right_indent = Inches(TEXT_W_IN - DIRECTIONS_W_IN)
    half = (TEXT_W_IN - 0.25) / 2
    for i, q in enumerate(bk["questions"], 1):
        t = doc.add_table(rows=1, cols=1)
        fix_widths(t, [TEXT_W_IN])
        c = t.rows[0].cells[0]
        cell_margins(c, 0, 0, 0, 0)
        no_split(t.rows[0])
        qp = para_in(c, first=True)
        _spacing(qp, 0, 4, BODY_LINE)
        qp.paragraph_format.left_indent = Inches(0.26)
        qp.paragraph_format.first_line_indent = Inches(-0.26)
        qp.paragraph_format.tab_stops.add_tab_stop(Inches(0.26))
        add(qp, f"{i}.\t", BODY, color=pal.ink, bold=True)
        add(qp, q["q"], BODY, color=pal.ink)
        qp.paragraph_format.right_indent = Inches(TEXT_W_IN - DIRECTIONS_W_IN - 0.4)   # R2-2
        inner = c.add_table(rows=1, cols=3)
        fix_widths(inner, [half, 0.25, half])
        for j, cc in enumerate((inner.rows[0].cells[0], inner.rows[0].cells[2])):
            cell_margins(cc, 0, 0, 0, 0)
            label(cc, bk["columns"][j], pal, first=True, after=0)
            write_lines(cc, int(q["lines"]), pal, width=half)
        cell_margins(inner.rows[0].cells[1], 0, 0, 0, 0)
        end_cell(c)
        p = doc.add_paragraph(); pin(p, 12)
    # vocabulary page
    from docx.enum.text import WD_BREAK
    p = doc.add_paragraph(); pin(p, 1)
    p.runs[0].add_break(WD_BREAK.PAGE)
    p = doc.add_paragraph()
    _spacing(p, 0, 2, SEC_TITLE * 1.25)
    add(p, bk["vocabTitle"], SEC_TITLE, color=pal.ink, bold=True, face=NARROW)
    bottom_rule(p, pal.display, W_ACCENT, 2)
    q = body_p(doc, bk["vocabDirections"], pal, before=4, after=8, size=9.5, line=12.6)
    q.paragraph_format.right_indent = Inches(TEXT_W_IN - DIRECTIONS_W_IN)
    terms = spec["vocab"]
    rows = (len(terms) + 1) // 2
    t = doc.add_table(rows=rows, cols=3)
    fix_widths(t, [half, 0.25, half])
    for ri in range(rows):
        no_split(t.rows[ri])
        for j, ci in enumerate((0, 2)):
            idx = ri + j * rows
            cc = t.rows[ri].cells[ci]
            cell_margins(cc, 0, 140, 0, 0)
            if idx >= len(terms):
                continue
            p = para_in(cc, first=True)
            _spacing(p, 0, 0, 13)
            add(p, terms[idx]["term"], BODY, color=pal.ink, bold=True)
            add(p, f"   {terms[idx]['section']}", 8, color=pal.label)
            write_lines(cc, int(bk.get("vocabLines", 2)), pal, width=half)


# ---------------------------------------------------------------------------------

def check_spec(spec):
    course = spec["course"]
    known = known_sections(course)
    for s in spec["sections"]:
        if s not in known:
            raise SystemExit(f"section {s} is not in courses/{course}/DECISIONS.md - stop and ask")
    for blk in spec["body"]:
        if blk["type"] == "section" and blk["code"] not in spec["sections"]:
            raise SystemExit(f"section head {blk['code']} is not in the spec's sections")
    text = json.dumps(spec)
    for banned in ("22.4", "STP", "molar volume"):
        if banned in text.replace("Molar volume, STP", ""):
            raise SystemExit(f"'{banned}' appears in the spec; molar volume is 11.5, out of U7")
    # every bold term in the body is a vocabulary term, and every vocabulary term is bolded
    bolded = set()
    for blk in spec["body"]:
        if blk["type"] == "p":
            bolded |= {m.lower() for m in re.findall(r"\*\*(.+?)\*\*", blk["text"])}
    vocab = {v["term"].lower() for v in spec["vocab"]}
    if bolded != vocab:
        raise SystemExit(f"bold terms and vocabulary disagree: bold-only {sorted(bolded - vocab)}, "
                         f"vocab-only {sorted(vocab - bolded)}")
    # every section closes with a reading check
    cur = None
    for blk in spec["body"] + [{"type": "section", "code": "end"}]:
        if blk["type"] == "section":
            if cur is not None and not cur:
                raise SystemExit("a section has no Reading Check")
            cur = False
        elif blk["type"] == "check":
            cur = True
    secs = [b["code"] for b in spec["body"] if b["type"] == "section"]
    conns = []
    cur_sec = None
    for b in spec["body"]:
        if b["type"] == "section":
            cur_sec = b["code"]
        elif b["type"] == "connection":
            conns.append(cur_sec)
    if conns and sorted(conns) != sorted(secs):
        raise SystemExit(f"every section needs exactly one Connection box: {conns} vs {secs}")
    for b in spec["body"]:
        if b["type"] in ("opener", "connection") and "**" in b["text"]:
            raise SystemExit(f"{b['type']} carries a bold term; bold stays at the defining sentence")


def chars_per_line(size):
    sample = ("Every measurement comes from a tool, and every tool has a limit. A bathroom scale "
              "might say you weigh 150 lb. It reads in whole pounds, so it can't tell them apart.")
    per_char = text_width_in(sample, size) / len(sample)
    return COL_W_IN / per_char


def build_student(spec, out_path, fig_dir):
    pal = Palette(spec["course"])
    doc = Document()
    s = page_setup(doc, base_pt=BODY)
    s.top_margin, s.bottom_margin = Inches(MARGIN_TOP_IN), Inches(MARGIN_BOTTOM_IN)
    unit = int(spec["unit"])
    code = f"U{unit:02d} / S{spec['sections'][0]}\u2013S{spec['sections'][-1]}"
    print_header(doc, pal, unit=unit, code=code, kind=spec["kind"], title=unit_title(spec["course"], spec["unit"]),
                 width=TEXT_W_IN)
    p = doc.add_paragraph(); pin(p, 8)
    front(doc, spec, pal)
    # chapter: two columns, continuing on page 1
    sec = doc.add_section(WD_SECTION.CONTINUOUS)
    set_cols(sec, 2)
    first = True
    body = spec["body"]
    for bi, blk in enumerate(body):
        t = blk["type"]
        if t == "section":
            hp = section_head(doc, blk, pal)
            if first:
                _spacing(hp, 4, 6, SEC_TITLE * 1.25); first = False
        elif t == "sub":
            sub_head(doc, blk["text"], pal)
        elif t == "p":
            bp = body_p(doc, blk["text"], pal)
            # a sentence that introduces a display ("…so it cancels:") stays with it (R2-1)
            if bi + 1 < len(body) and body[bi + 1]["type"] in ("math", "equation"):
                keep_next(bp)
        elif t == "opener":
            opener(doc, blk, pal)
        elif t == "connection":
            connection(doc, blk, pal)
        elif t == "figure":
            figure(doc, blk, pal, fig_dir)
        elif t == "math":
            math_row(doc, blk["parts"], pal, COL_W_IN)
            after_box(doc, 6)
        elif t == "equation":
            equation(doc, blk, pal)
        elif t == "example":
            example(doc, blk, pal)
        elif t == "check":
            reading_check(doc, blk, pal)
        elif t == "steps":
            steps(doc, blk, pal)
        else:
            raise SystemExit(f"unknown block type {t!r}")
    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    set_cols(sec, 1)
    back_pages(doc, spec, pal)
    ctx = {"pal": pal, "footer": f"SHULL SCIENCE / {spec['course'].upper()} / UNIT {unit:02d} / READING"}
    footers(doc, ctx)
    trim_tail(doc)
    apply_binding(doc)
    schema_order(doc)
    doc.save(out_path)


def build_key(spec, out_path):
    pal = Palette(spec["course"])
    doc = Document()
    s = page_setup(doc, base_pt=BODY)
    s.top_margin, s.bottom_margin = Inches(MARGIN_TOP_IN), Inches(MARGIN_BOTTOM_IN)
    unit = int(spec["unit"])
    code = f"U{unit:02d} / S{spec['sections'][0]}\u2013S{spec['sections'][-1]}"
    print_header(doc, pal, unit=unit, code=code, kind=spec["kind"] + " · Answer Key",
                 title=unit_title(spec["course"], spec["unit"]), width=TEXT_W_IN)
    p = doc.add_paragraph(); pin(p, 8)
    # two columns under the header, so key prose keeps the body line length (audit #8)
    sec = doc.add_section(WD_SECTION.CONTINUOUS)
    set_cols(sec, 2)

    # teacher notes: one outlined box, brand face
    t = doc.add_table(rows=1, cols=1)
    fix_widths(t, [COL_W_IN])
    c = t.rows[0].cells[0]
    borders(c, pal.hair, sz=W_HAIR)
    cell_margins(c, 80, 100, 140, 140)
    label(c, "Teacher notes", pal, first=True, after=3)
    for n in spec["key"]["teacherNotes"]:
        body_p(c, n, pal, after=4, size=9, line=11.8)
    end_cell(c)

    def head(text, first=False):
        p = doc.add_paragraph()
        _spacing(p, 4 if first else 12, 4, 15)
        keep_next(p)
        add(p, text, 13, color=pal.ink, bold=True, face=NARROW)
        bottom_rule(p, pal.display, 12, 2)

    def qa(num, question, answer, extra=None):
        tt = doc.add_table(rows=1, cols=1)
        fix_widths(tt, [COL_W_IN])
        cc = tt.rows[0].cells[0]
        cell_margins(cc, 20, 60, 0, 0)
        no_split(tt.rows[0])
        qp = para_in(cc, first=True)
        _spacing(qp, 0, 1, 12.6)
        qp.paragraph_format.left_indent = Inches(0.34)
        qp.paragraph_format.first_line_indent = Inches(-0.34)
        qp.paragraph_format.tab_stops.add_tab_stop(Inches(0.34))
        add(qp, f"{num}\t", 9.5, color=pal.accent, bold=True)
        add(qp, question, 9.5, color=pal.ink)
        ap = cc.add_paragraph()
        _spacing(ap, 0, 0, 17)
        ap.paragraph_format.left_indent = Inches(0.34)
        hand(ap, answer, 12.5)
        if extra:
            ep = cc.add_paragraph()
            _spacing(ep, 1, 0, 11.5)
            ep.paragraph_format.left_indent = Inches(0.34)
            add(ep, extra, 8.5, color=pal.label, italic=True)

    head("Reading Checks")
    for blk in spec["body"]:
        if blk["type"] == "check":
            qa(blk["n"], blk["q"], blk["answer"])
    head(f"Questions (page {spec['key']['questionsPage']}) — exemplar answers")
    for i, q in enumerate(spec["back"]["questions"], 1):
        qa(f"{i}.", q["q"], q["answer"],
           " ".join(x for x in (q.get("accept"), "Accept any answer that makes the same points "
                                "in the student's own words.") if x))
    head("Vocabulary — accepted definitions")
    for v in spec["vocab"]:
        tt = doc.add_table(rows=1, cols=1)
        fix_widths(tt, [COL_W_IN])
        cc = tt.rows[0].cells[0]
        cell_margins(cc, 10, 30, 0, 0)
        no_split(tt.rows[0])
        p = para_in(cc, first=True)
        _spacing(p, 0, 0, 16.5)
        add(p, v["term"], 9.5, color=pal.ink, bold=True)
        add(p, f"  {v['section']}   ", 8, color=pal.label)
        hand(p, v["def"], 12)
        if v.get("accept"):
            ep = cc.add_paragraph()
            _spacing(ep, 0, 0, 11.5)
            add(ep, v["accept"], 8.5, color=pal.label, italic=True)
    ctx = {"pal": pal, "footer": f"SHULL SCIENCE / {spec['course'].upper()} / UNIT {unit:02d} / READING / TEACHER KEY"}
    footers(doc, ctx)
    trim_tail(doc)
    apply_binding(doc)
    schema_order(doc)
    doc.save(out_path)


def check_margins(pdf_path):
    """Every image stays inside the text block: nothing enters the binding margin
    (SHULL-CHG-0103), on odd pages (inside left) or even (inside right). Returns problems."""
    import fitz
    from _shull_print import BINDING
    inside, outside = BINDING.inside_in * 72, 0.50 * 72
    bad = []
    with fitz.open(pdf_path) as d:
        for i, page in enumerate(d, 1):
            w = page.rect.width
            lo, hi = (inside, w - outside) if i % 2 else (outside, w - inside)
            for info in page.get_image_info():
                x0, _, x1, _ = info["bbox"]
                if x0 < lo - 0.5 or x1 > hi + 0.5:
                    bad.append(f"p{i}: image x {x0:.1f}-{x1:.1f} pt outside {lo:.1f}-{hi:.1f}")
    return bad


def to_pdf(docx_path, out_dir):
    soffice = shutil.which("soffice")
    if not soffice:
        raise SystemExit("soffice not found: run scripts/setup-environment.sh")
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", td, docx_path],
                       check=True, capture_output=True)
        src = os.path.join(td, os.path.splitext(os.path.basename(docx_path))[0] + ".pdf")
        dst = os.path.join(out_dir, os.path.basename(src))
        shutil.move(src, dst)
    import fitz
    with fitz.open(dst) as d:
        return dst, d.page_count


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if len(args) != 2:
        print(__doc__.strip(), file=sys.stderr); return 2
    spec_path, out_dir = args
    spec = json.load(open(spec_path))
    check_spec(spec)
    cpl = chars_per_line(BODY)
    if not 50 <= cpl <= 75:
        raise SystemExit(f"column measure is {cpl:.0f} characters a line; the band is 50-75")
    print(f"column {COL_W_IN:.2f} in at {BODY} pt: about {cpl:.0f} characters a line")
    os.makedirs(out_dir, exist_ok=True)
    fig_dir = os.path.join(out_dir, spec["figures"]["dir"])
    if "--no-figures" not in flags:
        subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(spec_path)),
                        spec["figures"]["script"]), fig_dir], check=True, capture_output=True)
    names = spec["workingFilename"]
    stu = os.path.join(out_dir, names["student"] + ".docx")
    key = os.path.join(out_dir, names["key"] + ".docx")
    build_student(spec, stu, fig_dir)
    build_key(spec, key)
    print("wrote", stu); print("wrote", key)
    if "--no-pdf" in flags:
        return 0
    budget = spec.get("pageBudget", {})
    ok = True
    for path, is_key in ((stu, False), (key, True)):
        pdf, n = to_pdf(path, out_dir)
        print(f"wrote {pdf}  ({n} pages)")
        for b in check_margins(pdf):
            print("  MARGIN:", b); ok = False
        if not is_key:
            if n > budget.get("max", 99):
                print(f"  OVER BUDGET: {n} pages, cap {budget['max']}"); ok = False
            if budget.get("even") and n % 2:
                print(f"  ODD PAGE COUNT: {n} (duplex needs even)"); ok = False
        elif n % 2:
            print(f"  ODD PAGE COUNT on key: {n}"); ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
