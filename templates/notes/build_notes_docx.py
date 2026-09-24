#!/usr/bin/env python3
"""Build a guided/Cornell notes packet as .docx from a JSON spec. Option A.

    python3 templates/notes/build_notes_docx.py specs/<spec>.json out.docx [--verify]

The packet is a set of designed pages, and each one is meant to be one sheet of paper:

    cover            the SHULL-CHG-0014 packet opening (school line, unit title, kicker,
                     Name/Date/Period, unit targets | key terms, how these notes work,
                     sections checklist with difficulty), plus the cover image and the
                     equation toolbox - SHULL-CHG-0030
    content pages    a new page per section. The first page of a section opens with the
                     0014 section title bar (title, U## / S##.# code, course-accent rule)
                     and its LEARNING TARGET line; continuation pages carry no head.
                     Each page holds about three blocks. A block is two open columns
                     split by one thin rule: the cue side (course-colour cue label, cue
                     questions) and the capture side (course-colour notes heading,
                     prompts, tables, flowchart, worked example, must-write lines),
                     closed by one "Extra notes" line. Each section ends with a RECALL
                     block.
    concept review   the standing last page: per-section explanation, a watch-out line,
                     and quick-recall questions.

A .docx has no layout of its own - the reader lays it out - so "one designed page is
one sheet" is predicted, not assumed: every paragraph here is pinned to an exact line
height, `estimate_height()` measures what was written, and each page's spare height is
shared out across its blocks so the blocks fill the sheet and stop at its foot.
`--verify` converts with LibreOffice and fails if any designed page spilled.

The spec schema is documented in templates/notes/README.md. Older flat specs (rows
straight under each section, no `pages`) are upgraded at build time by
`normalize_legacy()`, so they keep building without being rewritten by hand.

Colour comes from brand/tokens.json. No hex is typed in this file. Course colour is a
thin accent only (SHULL_DESIGN_SYSTEM section 8): the header rules in the course
`primary`, and label type in the text-safe `primaryDeep`. Everything else is greyscale.
"""
import copy, io, json, os, re, shutil, subprocess, sys, tempfile
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Every primitive on this page - how a work box is drawn, how a fraction stacks, how a
# diagram block holds together across a page break - is shared with the worksheet
# builder. It lives in one file so the two cannot drift.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _shull_docx import (          # noqa: E402
    FONT, FOOTER_FLOOR, COURSE_CODE, REPO, Palette, hexof, debullet, known_sections,
    unit_title, unit_phase, shade, borders, checkbox, fix_widths, stacked_frac, work_box,
    diagram_block, fillin_table, cell_margins, trim_tail, field, page_number_format,
    schema_order, estimate_height, text_width_in,
)

HERE = os.path.dirname(os.path.abspath(__file__))
SCHOOL = "James A. Garfield Local Schools"


# ---------------------------------------------------------------------------------
# Geometry.
#
# The Cornell split is SHULL-CHG-0018's and is decided here once: a 1.28 in cue column
# and 6.22 in capture column on a 7.50 in text block. Everything on the capture side is
# measured off NOTES_INNER_IN, so moving the split moves every table, work box and
# figure with it.
TEXT_W_IN = 7.50
CUE_W_IN = 1.28
NOTES_W_IN = TEXT_W_IN - CUE_W_IN           # 6.22
CUE_PAD_R_IN = 0.08                         # air between cue text and the column rule
NOTES_PAD_L_IN = 0.20                       # air between the column rule and the notes
CUE_INNER_IN = round(CUE_W_IN - CUE_PAD_R_IN, 2)      # 1.20
NOTES_INNER_IN = round(NOTES_W_IN - NOTES_PAD_L_IN, 2)  # 6.02

PAGE_W_IN, PAGE_H_IN = 8.5, 11.0
MARGIN_LR_IN = 0.50
MARGIN_TOP_IN = 0.42
MARGIN_BOTTOM_IN = 0.72                     # the ruled footer lives in here
FOOTER_DIST_IN = 0.30
BODY_H_PT = (PAGE_H_IN - MARGIN_TOP_IN - MARGIN_BOTTOM_IN) * 72
# What the height prediction is allowed to be wrong by before a page spills. Word and
# LibreOffice round row heights and border widths differently; this is the room for it.
SAFETY_PT = 14
MAX_STRETCH_PT = 90

# SHULL-CHG-0016: a problem to solve gets a bordered box to solve it in. hRule
# "atLeast", so it grows with the work and never shrinks below this.
WORK_BOX_MIN_IN = 1.4
WORK_LABEL = "WORK / show your reasoning and units"

# Rules, in eighths of a point (what w:sz counts). The page is open: no outer box and
# no cell borders around a block, so these few rules are the structure.
W_RULE = 6          # the rule between blocks, the column rule, hairlines
W_LINE = 6          # a writing line - print.weights.writingLine is 0.75 pt minimum
W_MUST = 12         # the grey rule down the left of a must-write line
W_TABLE = 4         # inside a fill-in table
# SHULL-CHG-0030 restores the SHULL-CHG-0014 header rules at 0014's weights: an ink
# rule above a head and a heavy course-accent rule below it. A rule, not a band - 2.25
# pt is a line's worth of toner (SHULL_DESIGN_SYSTEM section 8).
W_HEAD_TOP = 12
W_HEAD_ACCENT = 18

# The type ladder, in points. Nothing on a student page is under the 8 pt print floor
# except the running footer, which is what printFooter exists for.
CUE = 8.5
BODY, BODY_LINE = 10, 13
LABEL = 8
CHIP = 8

# SHULL-CHG-0030: the 0014 header sizes, from the 0f3b078 builder. 0014 set its labels
# at 7 and 7.5 pt; they are raised to the 8 pt print floor (typography.floors.printBody),
# the only size that moved. Tracking is 0014's: 26 on caps labels, none on the cue
# label - "tracking is what made DISTANCE VS. DISPLACEMENT wrap" in the cue column.
UNIT_TITLE_PT = 15          # the unit title on the cover, in caps
BAR_TITLE_PT = 12.5         # the section title bar
BAR_CODE_PT = 8.5           # U01 / S01.2 at the right of the bar
TRACK = 26                  # 0014's caps_track

PROBLEM_WORDS = ("EXAMPLE", "PRACTICE", "PROBLEM", "SOLVE", "CALCULATE", "YOUR TURN")
TAGGED = ("recall", "recap", "review")   # blocks that open with a tag
CAPTURE = ("notes", "problem", "table", "flowchart", "diagram")


class GreyPalette(Palette):
    """The notes body is greyscale. The shared primitives colour their labels with
    `accent` and their rules with `display`; here those resolve to ink and label grey,
    so a work box or fill-in table drawn by the same code the worksheet uses comes out
    in the notes' voice without a second copy of the drawing.

    The course colours are kept under their own names for the SHULL-CHG-0030 headers
    and row labels, the only places they are used: `type_accent` is the course
    `primaryDeep` (text-safe on white, for label type) and `rule_accent` is the course
    `primary` (NOT type - rules only, per its measured onWhiteVerdict)."""

    def __init__(self, course):
        super().__init__(course)
        self.type_accent = self.accent
        self.rule_accent = self.display
        self.accent = self.ink
        self.display = self.label


# ---------------------------------------------------------------------------------
# Text. Every paragraph this file writes is pinned to an exact line height. That is
# what makes the page predictable: at "single" spacing Word sizes a line from
# Archivo's Windows metrics (1.51 x the point size) and LibreOffice from its hhea
# metrics (1.09 x), so the same file is a third taller in one reader than the other.
# An exact line is the same in both.

_MARK = re.compile(r"(\*\*.+?\*\*)")


def segments(text):
    """`**bold**` inline markup -> [(text, bold)]."""
    out = []
    for part in _MARK.split(str(text)):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            out.append((part[2:-2], True))
        else:
            out.append((part, False))
    return out


def _spacing(p, before=0, after=0, line=None):
    pPr = p._p.get_or_add_pPr()
    sp = pPr.find(qn("w:spacing"))
    if sp is None:
        sp = OxmlElement("w:spacing")
        pPr.append(sp)
    sp.set(qn("w:before"), str(int(round(before * 20))))
    sp.set(qn("w:after"), str(int(round(after * 20))))
    if line is not None:
        sp.set(qn("w:line"), str(int(round(line * 20))))
        sp.set(qn("w:lineRule"), "exact")


def _run(p, text, size, *, bold=False, color=None, track=None):
    r = p.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.bold = bold
    if color:
        r.font.color.rgb = RGBColor.from_string(hexof(color))
    if track:
        el = OxmlElement("w:spacing"); el.set(qn("w:val"), str(int(track)))
        r._element.get_or_add_rPr().append(el)
    return r


def _bottom_rule(p, color, sz=W_RULE, space=1):
    pPr = p._p.get_or_add_pPr()
    b = pPr.find(qn("w:pBdr"))
    if b is None:
        b = OxmlElement("w:pBdr"); pPr.append(b)
    x = OxmlElement("w:bottom")
    x.set(qn("w:val"), "single"); x.set(qn("w:sz"), str(sz))
    x.set(qn("w:space"), str(space)); x.set(qn("w:color"), hexof(color))
    b.append(x)


def _top_rule(p, color, sz=W_RULE, space=4):
    pPr = p._p.get_or_add_pPr()
    b = pPr.find(qn("w:pBdr"))
    if b is None:
        b = OxmlElement("w:pBdr"); pPr.append(b)
    x = OxmlElement("w:top")
    x.set(qn("w:val"), "single"); x.set(qn("w:sz"), str(sz))
    x.set(qn("w:space"), str(space)); x.set(qn("w:color"), hexof(color))
    b.append(x)


def write(p, text, size, *, line=None, bold=False, color=None, before=0, after=0,
          align=None, track=None):
    """Fill paragraph `p` with marked-up text at an exact line height."""
    _spacing(p, before, after, line or round(size * 1.3, 1))
    for seg, b in segments(text):
        _run(p, seg, size, bold=bold or b, color=color, track=track)
    if align:
        p.alignment = align
    return p


def pin(p, pt):
    """An empty paragraph exactly `pt` tall - a spacer that is the size it says."""
    _spacing(p, 0, 0, max(pt, 1))
    r = p.add_run()
    r.font.size = Pt(1)
    return p


_ISOTOPE = re.compile(r"(?<=[A-Za-z])-(?=\d)")


def nobreak_hyphens(root):
    """Cl-35, Cu-63, Iron-56: an isotope name must not break at its hyphen - "Cl-" at
    the end of one line and "35" at the start of the next reads as two things. The
    hyphen becomes U+2011, the non-breaking hyphen, which Archivo carries."""
    for t in root.iter(qn("w:t")):
        if t.text and "-" in t.text:
            t.text = _ISOTOPE.sub("\u2011", t.text)


def pin_all(el):
    """Give every paragraph that still has reader-default spacing (the shared
    primitives write some) an exact line of 1.25 x its largest run. A paragraph
    holding a picture is left alone - an exact line would crop the picture to it."""
    for p in el.iter(qn("w:p")):
        if p.find(".//" + qn("w:drawing")) is not None:
            continue
        pPr = p.find(qn("w:pPr"))
        sp = pPr.find(qn("w:spacing")) if pPr is not None else None
        if sp is not None and sp.get(qn("w:lineRule")) == "exact":
            continue
        sizes = [int(s.get(qn("w:val"))) / 2.0 for s in p.iter(qn("w:sz"))]
        size = max(sizes or [10])
        if pPr is None:
            pPr = OxmlElement("w:pPr"); p.insert(0, pPr)
        if sp is None:
            sp = OxmlElement("w:spacing"); pPr.append(sp)
        sp.set(qn("w:line"), str(int(round(size * 1.25 * 20))))
        sp.set(qn("w:lineRule"), "exact")


class Col:
    """One table cell being filled top to bottom.

    python-docx starts a cell with an empty paragraph and appends another after every
    nested table (Word needs a cell to END with one). Left alone, each is a full body
    line of nothing - on a page budgeted to the point, that is how a block spills.
    This owns those paragraphs: the first is used for the first line of content or
    removed if a table comes first, the trailing one after a table is removed, and
    `finish()` writes the one Word needs, 1 pt tall.
    """

    def __init__(self, cell, width_in, pal):
        self.cell, self.w, self.pal = cell, width_in, pal
        self._fresh = True

    def para(self):
        if self._fresh:
            self._fresh = False
            return self.cell.paragraphs[0]
        return self.cell.add_paragraph()

    def text(self, text, size=BODY, **kw):
        kw.setdefault("color", self.pal.ink)
        return write(self.para(), text, size, **kw)

    def gap(self, pt):
        return pin(self.para(), pt)

    def line(self, height=17, after=8, color=None):
        """A writing line: an empty paragraph with a rule along its foot.

        The space under it is a separate 1-line spacer, not space-after. Both readers
        group consecutive paragraphs that carry the same border and draw only the
        outer edge of the group - two writing lines in a row printed as one."""
        p = self.para()
        _spacing(p, 0, 0, height)
        _bottom_rule(p, color or self.pal.hair, W_LINE, 1)
        if after:
            self.gap(after)
        return p

    def after_table(self):
        tc = self.cell._tc
        kids = [k for k in tc if k.tag in (qn("w:p"), qn("w:tbl"))]
        last = kids[-1]
        if last.tag == qn("w:p") and not "".join(last.itertext()).strip() \
                and len(kids) > 1 and kids[-2].tag == qn("w:tbl"):
            tc.remove(last)
        if self._fresh:
            first = kids[0]
            if first.tag == qn("w:p") and not "".join(first.itertext()).strip():
                tc.remove(first)
            self._fresh = False

    def finish(self):
        tc = self.cell._tc
        kids = [k for k in tc if k.tag in (qn("w:p"), qn("w:tbl"))]
        if not kids or kids[-1].tag == qn("w:tbl"):
            pin(self.cell.add_paragraph(), 1)


def table(container, widths, rows=1):
    """A layout table. Its default cell margins are zeroed at the table level as well
    as per cell: readers place a table's edge one default margin (0.075 in) left of
    the text margin, so without this every ruled table on the page started a hair
    left of the paragraphs and the footer rule under it."""
    t = container.add_table(rows=rows, cols=len(widths))
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    fix_widths(t, widths)
    tblPr = t._tbl.tblPr
    m = OxmlElement("w:tblCellMar")
    for edge in ("top", "left", "bottom", "right"):
        e = OxmlElement(f"w:{edge}"); e.set(qn("w:w"), "0"); e.set(qn("w:type"), "dxa")
        m.append(e)
    tblPr.append(m)
    return t


def add_row(t, widths):
    r = t.add_row()
    for c, w in zip(r.cells, widths):
        c.width = Inches(w)
    return r


def row_height(row, pt, rule="atLeast"):
    trPr = row._tr.get_or_add_trPr()
    for old in trPr.findall(qn("w:trHeight")):
        trPr.remove(old)
    h = OxmlElement("w:trHeight")
    h.set(qn("w:val"), str(int(round(pt * 20))))
    h.set(qn("w:hRule"), rule)
    trPr.append(h)


def cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn("w:cantSplit")) is None:
        trPr.insert(0, OxmlElement("w:cantSplit"))


def mar(cell, top=0, bottom=0, left=0, right=0):
    """Cell margins in points."""
    cell_margins(cell, top * 20, bottom * 20, left * 20, right * 20)


def break_before(doc):
    """Start a new sheet. A page-break-before on a 1 pt paragraph, not a `w:br` run: a
    break run leaves the rest of its paragraph - a full empty line - at the top of the
    new page."""
    p = doc.add_paragraph()
    pin(p, 1)
    p.paragraph_format.page_break_before = True
    return p


def chip(col, text, pal):
    """A small tag - RECALL, RECAP, REVIEW - tinted with the design system's light
    callout surface. Section 8: "chips and border-tab labels stay outlined or
    light-fill". Sized to its word, so it can never grow into a band."""
    w = round(text_width_in(text, CHIP, True) + 0.018 * len(text) + 0.16, 2)
    t = col.cell.add_table(rows=1, cols=1)
    fix_widths(t, [w])
    c = t.rows[0].cells[0]
    shade(c, pal.surface)
    mar(c, 1.5, 1.5, 4, 4)
    write(c.paragraphs[0], text, CHIP, line=10.5, bold=True, color=pal.ink, track=10)
    col.after_table()
    return t


# ---------------------------------------------------------------------------------
# A branching flowchart - one root, two branches, four leaves (the S1.1 matter chart
# is the first). Guided notes capture what goes up on the board, so the student labels
# it as it is drawn. Word cannot draw a diagonal connector inside a table reliably, so
# the chart is a picture - Archivo from brand/fonts, ink only, hairline boxes, thin
# diagonal connectors - in two variants with one geometry: only the root printed
# (student) and every box labelled (key). The labels come from the spec.
FLOW_H_IN = 1.80
_FLOW = {
    # (x0, x1) as fractions of the width; (y0, y1) in inches
    "top": ((0.329, 0.673), (0.02, 0.36)),
    "l2": [((0.006, 0.457), (0.66, 1.08)), ((0.540, 0.990), (0.66, 1.08))],
    "leaf": [((0.004, 0.216), (1.36, 1.78)), ((0.254, 0.470), (1.36, 1.78)),
             ((0.539, 0.755), (1.36, 1.78)), ((0.780, 0.996), (1.36, 1.78))],
}


def flowchart_labels(fc):
    """The chart's words come from the spec - they are content, not template. The
    template owns only the shape: one root, two branches, two leaves under each."""
    if not isinstance(fc, dict) or not fc.get("root") or len(fc.get("branches", [])) != 2 \
            or len(fc.get("leaves", [])) != 4:
        raise SystemExit('build_notes_docx: "flowchart" needs {"root": "…", "branches": '
                         '[2 labels], "leaves": [4 labels, two under each branch]}.')
    return fc["root"], fc["branches"], fc["leaves"]


def flowchart_png(pal, width_in, fc, filled, dpi=300):
    from PIL import Image, ImageDraw, ImageFont
    W, H = int(width_in * dpi), int(FLOW_H_IN * dpi)
    rgb = lambda h: tuple(int(hexof(h)[i:i + 2], 16) for i in (0, 2, 4))
    im = Image.new("RGB", (W, H), rgb(pal.white))
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join(REPO, "brand", "fonts", "Archivo-Bold.ttf"),
                              int(round(9.5 / 72 * dpi)))
    box_w = max(2, int(round(0.6 / 72 * dpi)))
    link_w = max(2, int(round(0.6 / 72 * dpi)))

    def rect(spec):
        (x0, x1), (y0, y1) = spec
        return (int(x0 * W), int(y0 * dpi), int(x1 * W) - 1, int(y1 * dpi))

    def box(spec, text):
        r = rect(spec)
        d.rectangle(r, outline=rgb(pal.label), width=box_w)
        if text:
            tw = d.textlength(text, font=font)
            asc, desc = font.getmetrics()
            d.text(((r[0] + r[2]) / 2 - tw / 2, (r[1] + r[3]) / 2 - (asc + desc) / 2 + 2),
                   text, font=font, fill=rgb(pal.ink))

    def link(a, b):
        ra, rb = rect(a), rect(b)
        d.line([((ra[0] + ra[2]) / 2, ra[3]), ((rb[0] + rb[2]) / 2, rb[1])],
               fill=rgb(pal.hair), width=link_w)

    for l2 in _FLOW["l2"]:
        link(_FLOW["top"], l2)
    for i, leaf in enumerate(_FLOW["leaf"]):
        link(_FLOW["l2"][i // 2], leaf)
    root, branches, leaves = flowchart_labels(fc)
    box(_FLOW["top"], root)
    for spec, text in zip(_FLOW["l2"], branches):
        box(spec, text if filled else "")
    for spec, text in zip(_FLOW["leaf"], leaves):
        box(spec, text if filled else "")
    buf = io.BytesIO()
    im.save(buf, format="PNG", dpi=(dpi, dpi))
    buf.seek(0)
    return buf


# ---------------------------------------------------------------------------------
# Section codes. Specs write them several ways ("1.1", "S01.1", "U01 / S01.1",
# "U1 / S1.2"); the build uses the bare number for validation and prints S##.#,
# zero-padded - standards/NAMING.md - or U## / S##.# on the section title bar.

def sec_num(code):
    m = re.search(r"S?0*(\d{1,2})\.(\d)\s*$", str(code).strip())
    if not m:
        raise SystemExit(f"build_notes_docx: cannot read a section number from {code!r}")
    return f"{int(m.group(1))}.{m.group(2)}"


def sec_label(code):
    u, s = sec_num(code).split(".")
    return f"S{int(u):02d}.{s}"


def bar_code(code):
    """The section title bar's code: 0014's "U1 / S1.2" shape, zero-padded as
    SHULL-CHG-0007 requires - "U01 / S01.2"."""
    u, s = sec_num(code).split(".")
    return f"U{int(u):02d} / S{int(u):02d}.{s}"


_BARE_CODE = re.compile(r"\bS(\d)\.(\d)\b")


def pad_codes(text):
    """An old spec writes "S1.2" in running text (its kicker, its section list). The
    build prints codes zero-padded everywhere else (SHULL-CHG-0007), so these are
    padded too. Only the code's format changes."""
    return _BARE_CODE.sub(lambda m: f"S0{m.group(1)}.{m.group(2)}", str(text))


def label_of(row, which):
    """The cue label or the notes heading of a block (SHULL-CHG-0030).

    An old spec names both (`cueLabel` "BASICS", `notesLabel` "THE BIG BANG"). A paged
    spec's block has a `title` and at most a `notesLabel`; its title, in caps, stands
    in for whichever label is missing, so it is used for both when neither is given.
    A label the spec wrote is printed as written - never upper-cased here: that turned
    the Physics variable "a" into "A" in "COMPARING THE SIGN OF a TO THE SIGN OF v"."""
    given = row.get(which)
    if given:
        return given
    return str(row.get("title", "")).upper()


# ---------------------------------------------------------------------------------
# Blocks.

def render_cue(col, row, pal):
    """The cue side: a tag on a RECALL / RECAP / REVIEW block, the course-colour cue
    label (SHULL-CHG-0030; 0014's bold untracked caps), then the cue questions. No
    block number - the user dropped the 01, 02 (0030 choice d)."""
    kind = row.get("kind", "notes")
    if kind in TAGGED:
        chip(col, kind.upper(), pal)
        col.gap(6)
    col.text(label_of(row, "cueLabel"), LABEL, line=10.5, bold=True,
             color=pal.type_accent, after=6)
    for q in row.get("cues", []):
        col.text(q, CUE, line=10.5, color=pal.label, after=5)


def render_prompt(col, text, answer, lines, key, pal):
    col.text(text, BODY, line=BODY_LINE)
    if answer:
        col.text(answer, BODY, line=BODY_LINE, bold=True, before=4, after=8)
    else:
        for _ in range(lines):
            col.line()


def render_must_write(col, text, pal):
    """A line the student must have in their notes - lime on the slide. A grey rule
    down its left edge, drawn as a cell border: a paragraph border inside a nested
    cell is valid OOXML that LibreOffice does not paint."""
    col.gap(3)
    t = col.cell.add_table(rows=1, cols=1)
    fix_widths(t, [col.w])
    c = t.rows[0].cells[0]
    borders(c, pal.label, sz=W_MUST, edges=("left",))
    mar(c, 3, 3, 8, 0)
    row_height(t.rows[0], 30)
    cant_split(t.rows[0])
    write(c.paragraphs[0], text, BODY, line=BODY_LINE, bold=True, color=pal.ink)
    col.after_table()
    col.gap(6)


def render_problem(col, prob, key, pal):
    if prob.get("statement"):
        col.text(prob["statement"], BODY, line=BODY_LINE, after=3)
    given = prob.get("given")
    if given:
        given = given if isinstance(given, list) else [given]
        col.text("**Given:** " + given[0], BODY, line=BODY_LINE)
        for g in given[1:]:
            col.text(g, BODY, line=BODY_LINE)
    if prob.get("find"):
        col.text("**Find:** " + prob["find"], BODY, line=BODY_LINE, before=3)
    col.gap(5)
    # A spec may ask for a taller box, never a shorter one: 1.4 in is SHULL-CHG-0016's
    # floor, and a page that cannot hold it is re-balanced, not given a smaller box.
    height = max(float(prob.get("workHeightIn", WORK_BOX_MIN_IN)), WORK_BOX_MIN_IN)
    inner = work_box(col.cell, prob.get("workLabel", WORK_LABEL), pal, height, col.w,
                     label_size=LABEL, label_bold=False, label_caps=False,
                     label_color=pal.label)
    mar(inner, 3, 3, 6, 6)
    if key:
        for s in prob.get("solution", []):
            write(inner.add_paragraph(), s, BODY, line=BODY_LINE, color=pal.ink,
                  before=2)
    col.after_table()
    if prob.get("answer"):
        col.text(prob["answer"], BODY, line=BODY_LINE, bold=key, before=8)


def render_notes(col, row, key, pal, base_dir):
    kind = row.get("kind", "notes")
    # The notes heading, in course colour with 0014's caps tracking (SHULL-CHG-0030).
    # A heading derived from the title that only repeats the cue label beside it is
    # left out; an explicit notesLabel, or one that differs, is printed.
    heading = label_of(row, "notesLabel")
    if row.get("notesLabel") or heading != label_of(row, "cueLabel"):
        col.text(heading, LABEL, line=10.5, bold=True, after=6,
                 color=pal.type_accent, track=TRACK)
    if row.get("diagram"):
        diagram_block(col.cell, row["diagram"], pal, col.w, base_dir)
        col.after_table()
        col.gap(4)
    if row.get("table"):
        spec = dict(row["table"])
        fillin_table(col.cell, spec, pal, col.w, header_fill=pal.surface,
                     header_caps=False, label_bold=False, header_size=LABEL,
                     body_size=9.5)
        col.after_table()
        col.gap(6)
    if row.get("flowchart"):
        p = col.para()
        _spacing(p, 0, 4)
        w = round(col.w - 0.15, 2)
        p.add_run().add_picture(flowchart_png(pal, w, row["flowchart"], key),
                                width=Inches(w))
    if row.get("problem"):
        render_problem(col, row["problem"], key, pal)

    if kind == "recall":
        col.text(row.get("prompt", ""), BODY, line=BODY_LINE)
        # Ruled room sized to the answer the key gives (two or three lines), rather
        # than a stretched blank under the checklist.
        if key and row.get("answer"):
            col.text(row["answer"], BODY, line=BODY_LINE, bold=True, before=4, after=6)
        else:
            col.gap(2)
            for _ in range(int(row.get("lines", 3))):
                col.line()
        col.gap(4)
        for x in row.get("selfCheck", []):
            check(col, x, pal)
    if kind == "review":
        if row.get("bigPicture"):
            col.text("**Big picture:** " + row["bigPicture"], BODY, line=BODY_LINE,
                     after=8)
        for x in row.get("checklist", []):
            check(col, x, pal)
        if row.get("fuzzyLabel"):
            col.text(row["fuzzyLabel"], BODY, line=BODY_LINE, bold=True, before=8)
            col.line(height=22)

    for n in row.get("notes", []):
        if isinstance(n, dict):
            if "prompt" in n:
                render_prompt(col, n["prompt"], n.get("answer") if key else None,
                              int(n.get("lines", 1)), key, pal)
            elif "text" in n:
                col.text(n["text"], BODY, line=BODY_LINE + 1, after=n.get("after", 3))
            elif "check" in n:
                check(col, n["check"], pal)
            elif "label" in n:
                col.text(n["label"], BODY, line=BODY_LINE, bold=True, before=6)
            elif "lines" in n:
                for _ in range(int(n["lines"])):
                    col.line()
            continue
        if n.startswith(("*", "✎")):
            render_must_write(col, n.lstrip("*✎").strip(), pal)
        else:
            body = n.strip()
            render_prompt(col, body, None, 2 if body.rstrip().endswith("?") else 1,
                          key, pal)


def check(col, text, pal):
    p = col.para()
    _spacing(p, 0, 5, 13)
    checkbox(p, pal, 9)
    for seg, b in segments("   " + text):
        _run(p, seg, 9.5, bold=b, color=pal.ink)
    return p


def extra_notes(cell, pal):
    """The quiet catch-all at the foot of every block: whatever goes up on the board
    that the prompts above did not plan for. A small grey label and one line."""
    col = Col(cell, NOTES_INNER_IN, pal)
    t = cell.add_table(rows=1, cols=2)
    fix_widths(t, [0.78, NOTES_INNER_IN - 0.78])
    a, b = t.rows[0].cells
    mar(a, 0, 1, 0, 0); mar(b, 0, 1, 0, 0)
    a.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
    write(a.paragraphs[0], "Extra notes:", LABEL, line=11, color=pal.label)
    borders(b, pal.hair, sz=W_LINE, edges=("bottom",))
    pin(b.paragraphs[0], 11)
    col.after_table()
    col.finish()


def spacer(row, pt, rule_color=None):
    row_height(row, pt, "exact")
    for c in row.cells:
        mar(c)
        pin(c.paragraphs[0], 1)
        if rule_color:
            borders(c, rule_color, sz=W_RULE, edges=("bottom",))


def render_blocks(t, rows, ctx):
    """Append one page's blocks to table `t`. Returns [(content_row, extra_pt)] so the
    caller can share out the page's spare height."""
    pal = ctx["pal"]
    widths = [CUE_W_IN, NOTES_W_IN]
    out = []
    for i, row in enumerate(rows):
        spacer(add_row(t, widths), 10 if i == 0 else 9)
        r = add_row(t, widths)
        cant_split(r)
        cue, notes = r.cells
        mar(cue, 0, 0, 0, CUE_PAD_R_IN * 72)
        mar(notes, 0, 0, NOTES_PAD_L_IN * 72, 0)
        borders(notes, pal.hair, sz=W_RULE, edges=("left",))
        cc = Col(cue, CUE_INNER_IN, pal)
        render_cue(cc, row, pal)
        cc.finish()
        nc = Col(notes, NOTES_INNER_IN, pal)
        render_notes(nc, row, ctx["key"], pal, ctx["base_dir"])
        nc.gap(8)
        nc.finish()
        extra = 0.0
        if row.get("extraNotes", row.get("kind", "notes") in ("notes", "example", "recap")):
            e = add_row(t, widths)
            cant_split(e)
            ec, en = e.cells
            mar(ec); mar(en, 0, 0, NOTES_PAD_L_IN * 72, 0)
            borders(en, pal.hair, sz=W_RULE, edges=("left",))
            pin(ec.paragraphs[0], 1)
            extra_notes(en, pal)
            row_height(e, 22)
            extra = 22.0
        last = i == len(rows) - 1
        if not last:
            spacer(add_row(t, widths), 9, pal.hair)
        # A RECALL block is not stretched: its writing room is ruled lines, and blank
        # space under a checklist reads as an unfinished box.
        out.append((r, extra, row.get("kind", "notes") != "recall"))
    return out


def head_height(ctx, sec):
    """Height of a section's title bar and learning target, in points, measured the
    same way as a block. Only a section's first page has one."""
    d = Document()
    t = section_bar(d, ctx, sec["title"], bar_code(sec["code"]), sec.get("learningTarget"))
    pin_all(t._tbl)
    return estimate_height(t._tbl, TEXT_W_IN) + 2


def block_height(row, ctx):
    """Natural height of one block, in points - measured by rendering it into a
    scratch document. Used to pack an old flat spec's rows into pages."""
    d = Document()
    t = table(d, [CUE_W_IN, NOTES_W_IN], rows=0)
    render_blocks(t, [row], ctx)
    pin_all(t._tbl)
    return estimate_height(t._tbl, TEXT_W_IN)


# ---------------------------------------------------------------------------------
# Section title bar and footer.

BAR_CODE_W_IN = 1.67        # 0014's split: 5.83 in title, 1.67 in code


def section_bar(doc, ctx, title, code, target=None, target_label="LEARNING TARGET",
                target_color=None):
    """SHULL-CHG-0030: the SHULL-CHG-0014 section title bar, as the 0f3b078 builder drew
    it. The section title at the left, the code at the right in the course's text-safe
    colour, an ink rule above and a heavy course-accent rule below - ruled, never
    filled. Under it the LEARNING TARGET line, closed by a hairline. 0014 boxed that
    line in hairlines because its rows were boxed; the paged page is open, so only the
    closing hairline is kept.

    It opens a section. Continuation pages carry no head (0030 choice c)."""
    pal = ctx["pal"]
    t = table(doc, [TEXT_W_IN - BAR_CODE_W_IN, BAR_CODE_W_IN], rows=2 if target else 1)
    a, b = t.rows[0].cells
    for c in (a, b):
        mar(c, 4, 4, 0, 0)
        borders(c, pal.ink, sz=W_HEAD_TOP, edges=("top",))
        borders(c, pal.rule_accent, sz=W_HEAD_ACCENT, edges=("bottom",))
        c.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
    write(a.paragraphs[0], title, BAR_TITLE_PT, line=16, bold=True, color=pal.ink)
    write(b.paragraphs[0], code, BAR_CODE_PT, line=16, bold=True, color=pal.type_accent,
          track=TRACK, align=WD_ALIGN_PARAGRAPH.RIGHT)
    if target:
        c = t.rows[1].cells[0].merge(t.rows[1].cells[1])
        mar(c, 5, 6, 0, 0)
        borders(c, pal.hair, sz=W_RULE, edges=("bottom",))
        p = c.paragraphs[0]
        _spacing(p, 0, 0, 13)
        if target_label:
            _run(p, target_label + "   ", LABEL, bold=True, color=pal.type_accent)
        for seg, bb in segments(target):
            _run(p, seg, 9.5, bold=bb, color=target_color or pal.ink)
    pin(doc.add_paragraph(), 1)
    return t


def footer(section, ctx):
    pal = ctx["pal"]
    section.footer_distance = Inches(FOOTER_DIST_IN)
    p = section.footer.paragraphs[0]
    _spacing(p, 0, 0, 12)
    _top_rule(p, pal.hair, W_RULE, 6)
    # The stock Footer style carries a centre tab at 3.25 in and a right tab at 6.5 in
    # (a 6.5 in text block); the page number jumped to the first of them. Clear both,
    # then set one right tab a hair inside the margin - LibreOffice drops a tab stop
    # that sits exactly on it.
    ts = p.paragraph_format.tab_stops
    for pos in (3.25, 6.5):
        ts.add_tab_stop(Inches(pos), WD_TAB_ALIGNMENT.CLEAR)
    ts.add_tab_stop(Inches(TEXT_W_IN - 0.02), WD_TAB_ALIGNMENT.RIGHT)
    _run(p, ctx["footer"], FOOTER_FLOOR, color=pal.footer, track=6)
    _run(p, "\t", FOOTER_FLOOR)
    # Two digits, computed by the reader so it stays right after an edit. The field
    # switch is for Word; the section format is what LibreOffice honours.
    field(p, 'PAGE \\# "00"', pal, size=8, bold=True, color=pal.ink)
    page_number_format(section, "decimalZero")


# ---------------------------------------------------------------------------------
# Pages.

def fit_page(ctx, label, head_tbl, blocks_tbl, parts):
    """Share a page's spare height out across its blocks, evenly: every block is
    raised to a common floor, so the page fills to its foot and no block is left
    short while another is stretched. Returns the predicted overflow (0 if it fits)."""
    pin_all(blocks_tbl._tbl)
    avail = BODY_H_PT - SAFETY_PT - 2  # the 1 pt page-break paragraph and the one after a head
    used = estimate_height(blocks_tbl._tbl, TEXT_W_IN)
    if head_tbl is not None:
        pin_all(head_tbl._tbl)
        used += estimate_height(head_tbl._tbl, TEXT_W_IN)
    naturals = []
    for r, extra, _ in parts:
        tbl = OxmlElement("w:tbl"); tbl.append(copy.deepcopy(r._tr))
        naturals.append(estimate_height(tbl, TEXT_W_IN) + extra)
    slack = avail - used
    ctx["report"].append((label, round(used / 72, 2), round(avail / 72, 2)))
    if slack < 0:
        return -slack
    # Water-fill: find the level L with sum(max(n, L)) - sum(n) == slack.
    stretch = [n for (_, _, st), n in zip(parts, naturals) if st]
    if not stretch:
        return 0.0
    level, s = 0.0, sorted(stretch)
    total = sum(stretch) + slack
    for k in range(len(s), 0, -1):
        level = (total - sum(s[k:])) / k
        if level >= s[k - 1]:
            break
    # A block is stretched to the common level, but never by more than MAX_STRETCH_PT:
    # a page that holds one short block (an old spec's RECALL on its own sheet) keeps
    # white space at its foot rather than becoming one seven-inch box.
    for (r, extra, st), n in zip(parts, naturals):
        if st:
            row_height(r, min(max(n, level), n + MAX_STRETCH_PT) - extra)
    return 0.0


def content_page(doc, ctx, sec, page):
    """One sheet of a section. Its first sheet opens with the section title bar and
    learning target (SHULL-CHG-0030); a continuation sheet starts straight on its
    blocks. A page's own `subtitle`, which 0025's per-page head printed, is not drawn."""
    break_before(doc)
    head = None
    if page["_n"] == 1:
        head = section_bar(doc, ctx, sec["title"], bar_code(sec["code"]),
                           sec.get("learningTarget"))
    t = table(doc, [CUE_W_IN, NOTES_W_IN], rows=0)
    parts = render_blocks(t, page["rows"], ctx)
    over = fit_page(ctx, f"{sec_label(sec['code'])} p{page['_n']}", head, t, parts)
    if over:
        ctx["overfull"].append(f"{sec_label(sec['code'])} page {page['_n']}: "
                               f"predicted {over / 72:.2f} in too tall")


def label_para(doc, text, pal, before=14, after=8):
    """A cover label: 0014's bold tracked caps in the course's text-safe colour."""
    return write(doc.add_paragraph(), text.upper(), LABEL, line=10.5, bold=True,
                 color=pal.type_accent, before=before, after=after, track=TRACK)


def cell_label(cell_or_col, text, pal, first=True, after=4):
    p = cell_or_col.paragraphs[0] if first else cell_or_col.add_paragraph()
    return write(p, text.upper(), LABEL, line=10.5, bold=True, color=pal.type_accent,
                 after=after, track=TRACK)


def rule_para(doc, pal, before=0, after=0):
    p = doc.add_paragraph()
    _spacing(p, before, after, 2)
    _bottom_rule(p, pal.hair, W_RULE, 0)
    return p


def toolbox_line(col, item, pal):
    if isinstance(item, dict) and item.get("heading"):
        return col.text(item["heading"], BODY, line=15, bold=True, before=4)
    if isinstance(item, dict) and item.get("num"):
        # SHULL-CHG-0017: a fraction is stacked, never a/b inline. lhs and the fraction
        # side by side; the equals sign gets its own cell so it sits on the bar.
        lhs = (item.get("lhs", "") + "  =") if item.get("lhs") else ""
        lw = round(text_width_in(lhs, BODY) + 0.12, 2) if lhs else 0.05
        t = col.cell.add_table(rows=1, cols=2)
        fix_widths(t, [lw, col.w - lw])
        a, b = t.rows[0].cells
        mar(a, 2, 2); mar(b, 2, 2)
        a.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        write(a.paragraphs[0], lhs, BODY, line=14, color=pal.ink)
        stacked_frac(b, item["num"], item["den"], pal.ink, pal.hair, size=BODY)
        col.after_table()
        return t
    if isinstance(item, dict):
        item = item.get("plain", "")
    return col.text(item, BODY, line=15)


_SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")


def cover_content(spec, ctx):
    """What the SHULL-CHG-0014 packet opening prints, gathered from the spec
    (SHULL-CHG-0030). An old flat spec carries all of it; normalize_legacy() moves it
    under `cover`. A paged spec may carry it under `cover` too. Where a paged spec does
    not, only what the spec already holds is used - nothing is written that it does not
    say - and the build says what it derived (ctx["derived"]):

      kicker      GUIDED NOTES · PHASE nn · N SECTIONS. The phase is read from the
                  course DECISIONS.md (unit_phase); a course with no phases drops it.
      unitTargets the sections' own learning targets, in order.
      keyTerms    cover.keyTerms, grouped by section, one line per section.
      howItWorks  cover.howToUse, split into its sentences, one bullet each.
      sectionList each section's code and title.
    """
    cov = spec.get("cover", {})
    secs = spec["sectionsContent"]
    derived = ctx["derived"]
    out = {}

    kicker = cov.get("kicker")
    if not kicker:
        phase = unit_phase(ctx["course"], ctx["unit"])
        n = len(secs)
        kicker = "  ·  ".join(["GUIDED NOTES"] + ([f"PHASE {phase:02d}"] if phase else [])
                              + [f"{n} SECTION{'S' if n != 1 else ''}"])
        derived.append(f"kicker \"{kicker}\" (phase from courses/{ctx['course']}/"
                       f"DECISIONS.md)" if phase else f"kicker \"{kicker}\" (no phase in "
                       f"courses/{ctx['course']}/DECISIONS.md)")
    if ctx["key"]:
        kicker += "  ·  TEACHER KEY"
    out["kicker"] = kicker

    targets = [debullet(x) for x in cov.get("unitTargets", [])]
    if not targets:
        targets = [s["learningTarget"] for s in secs if s.get("learningTarget")]
        if targets:
            derived.append(f"unit targets = the {len(targets)} section learning targets")
    out["targets"] = targets

    terms = []
    for g in cov.get("keyTerms", []):
        if isinstance(g, dict):
            lead = f"**{sec_label(g['code'])}**  " if g.get("code") else ""
            terms.append(lead + ", ".join(g.get("terms", [])))
        else:
            terms.append(debullet(g))
    out["terms"] = terms

    how = cov.get("howItWorks") or cov.get("howToUse") or []
    if isinstance(how, str):
        how = [x.strip() for x in _SENTENCE.split(how) if x.strip()]
        if not cov.get("howItWorks"):
            derived.append(f"how these notes work = cover.howToUse, one bullet per "
                           f"sentence ({len(how)})")
    out["how"] = [debullet(x) for x in how]

    diff = {sec_num(x["code"]): x.get("difficulty")
            for x in cov.get("sections", []) if x.get("difficulty")}
    listed = cov.get("sectionList")
    if listed:
        out["checklist"] = [(pad_codes(debullet(x)), None) for x in listed]
    else:
        out["checklist"] = [(f"{sec_label(s['code'])}   {s['title']}",
                             diff.get(sec_num(s["code"]))) for s in secs]
    out["has_diff"] = bool(diff) and not listed
    out["difficultyNote"] = cov.get("difficultyNote") if out["has_diff"] else None
    return out


def _cover(doc, spec, ctx, k):
    """The cover at spacing scale `k` (1 = as designed). Returns its predicted height.

    SHULL-CHG-0030: the SHULL-CHG-0014 packet opening, as the 0f3b078 builder drew it -
    course-colour school line, unit title, kicker, closed by a heavy course-accent rule;
    Name/Date/Period; Unit Learning Targets | Key Terms; How these notes work, with the
    accent rule down its left; Sections in this unit. On top of it, 0025's cover items
    the user kept (0030 choice b): the image at the right of the masthead, the
    difficulty rating beside each section in the checklist, and the equation toolbox
    at the foot. Outlines and rules only; nothing is filled."""
    pal, cov, cc = ctx["pal"], spec.get("cover", {}), ctx["cover"]
    img = cov.get("image")
    img_path = os.path.join(ctx["base_dir"], img["path"]) if img else None
    if img and not os.path.exists(img_path):
        print(f"build_notes_docx: cover image \"{img['path']}\" not found at {img_path} "
              f"— building without it.", file=sys.stderr)
        img_path = None
    img_w = min(float(img.get("widthIn", 2.0)), 2.2) if img_path else 0

    # Masthead. The text sits on the accent rule; the image stands beside it.
    col_w = round(img_w + 0.2, 2) if img_path else 0
    widths = [TEXT_W_IN - col_w, col_w] if img_path else [TEXT_W_IN]
    t = table(doc, widths)
    a = t.rows[0].cells[0]
    for c in t.rows[0].cells:
        mar(c, 0, 6, 0, 0)
        borders(c, pal.rule_accent, sz=W_HEAD_ACCENT, edges=("bottom",))
        c.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
    write(a.paragraphs[0], f"SHULL SCIENCE  ·  {SCHOOL.upper()}", LABEL, line=11,
          bold=True, color=pal.type_accent, track=TRACK, after=3)
    write(a.add_paragraph(), ctx["unit_title"].upper(), UNIT_TITLE_PT, line=19, bold=True,
          color=pal.ink)
    write(a.add_paragraph(), cc["kicker"], LABEL, line=11, color=pal.label, track=TRACK,
          before=2)
    if img_path:
        b = t.rows[0].cells[1]
        p = b.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p.add_run().add_picture(img_path, width=Inches(img_w))

    # Name / Date / Period, in a hairline outline.
    fields = cov.get("fields") or ("NAME  _________________________________       "
                                   "DATE  ______________       PERIOD  ______")
    t = table(doc, [TEXT_W_IN])
    c = t.rows[0].cells[0]
    borders(c, pal.hair, sz=W_RULE)
    mar(c, 5, 5, 6, 6)
    write(c.paragraphs[0], fields, 9, line=12, color=pal.label)

    # Unit Learning Targets | Key Terms. Either one alone runs full width; with neither,
    # the box is left out rather than printed empty.
    lists = [(lab, items) for lab, items in (("Unit learning targets", cc["targets"]),
                                             ("Key terms", cc["terms"])) if items]
    if lists:
        pin(doc.add_paragraph(), 6 * k)
        w = round(TEXT_W_IN / len(lists), 2)
        t = table(doc, [w] * len(lists))
        for cell, (lab, items) in zip(t.rows[0].cells, lists):
            borders(cell, pal.hair, sz=W_RULE)
            mar(cell, 5, 5, 6, 6)
            cell_label(cell, lab, pal)
            for x in items:
                write(cell.add_paragraph(), "•  " + x, 9.5, line=12.5, color=pal.ink,
                      after=2)

    # How these notes work, with 0014's accent rule down its left edge.
    if cc["how"]:
        pin(doc.add_paragraph(), 6 * k)
        t = table(doc, [TEXT_W_IN])
        c = t.rows[0].cells[0]
        borders(c, pal.rule_accent, sz=W_HEAD_ACCENT, edges=("left",))
        mar(c, 2, 2, 9, 0)
        cell_label(c, "How these notes work", pal)
        for x in cc["how"]:
            write(c.add_paragraph(), "•  " + x, 9.5, line=12.5, color=pal.ink, after=2)

    # Sections in this unit: a box to tick per section, its difficulty at the right.
    pin(doc.add_paragraph(), 8 * k)
    diff_w = 1.0 if cc["has_diff"] else 0
    widths = [TEXT_W_IN - diff_w, diff_w] if diff_w else [TEXT_W_IN]
    t = table(doc, widths, rows=1 + len(cc["checklist"]))
    h = t.rows[0].cells
    cell_label(h[0], "Sections in this unit", pal)
    if diff_w:
        write(h[1].paragraphs[0], "DIFFICULTY", LABEL, line=10.5, bold=True,
              color=pal.type_accent, track=TRACK, align=WD_ALIGN_PARAGRAPH.RIGHT,
              after=4)
    for i, (text, d) in enumerate(cc["checklist"], 1):
        cells = t.rows[i].cells
        p = cells[0].paragraphs[0]
        _spacing(p, 0, 4 * k, 13)
        checkbox(p, pal, 9)
        _run(p, "   " + text, 9.5, color=pal.ink)
        if diff_w:
            write(cells[1].paragraphs[0], f"{d} / 10" if d else "", 9.5, line=13,
                  bold=True, color=pal.ink, align=WD_ALIGN_PARAGRAPH.RIGHT)
    if cc["difficultyNote"]:
        write(doc.add_paragraph(), cc["difficultyNote"], LABEL, line=11,
              color=pal.label, before=2 * k)

    # Equation toolbox (0025), kept on the cover (0030 choice b). A hairline above it.
    box = cov.get("equationToolbox")
    if box:
        rule_para(doc, pal, before=12 * k)
        label_para(doc, box.get("label", "Equation toolbox"), pal, before=10 * k,
                   after=6 * k)
        cols = box["columns"]
        half = round(TEXT_W_IN / len(cols), 2)
        t = table(doc, [half] * len(cols))
        for c, spec_col in zip(t.rows[0].cells, cols):
            mar(c, 0, 0, 0, 10)
            col = Col(c, half - 0.14, pal)
            if spec_col.get("heading"):
                col.text(spec_col["heading"], BODY, line=15, bold=True)
            for item in spec_col.get("lines", []):
                toolbox_line(col, item, pal)
            col.finish()
        for i, n in enumerate(box.get("notes", [])):
            write(doc.add_paragraph(), n, 8.5, line=12, color=pal.ink,
                  before=8 * k if i == 0 else 0)

    body = [el for el in doc.element.body if el.tag in (qn("w:p"), qn("w:tbl"))]
    pin_all(doc.element.body)
    return sum(estimate_height(el, TEXT_W_IN) for el in body)


def cover_page(doc, spec, ctx):
    """The cover, fitted to one sheet. A cover with four sections and a column of
    stacked fractions (Physics) runs long at the designed spacing; it is rebuilt once
    with the air between its parts halved. Only spacing moves; no text is shrunk to
    fit (build-document, "Page budget")."""
    avail = BODY_H_PT - SAFETY_PT
    for k in (1.0, 0.5):
        for el in [e for e in doc.element.body if e.tag in (qn("w:p"), qn("w:tbl"))]:
            doc.element.body.remove(el)
        used = _cover(doc, spec, ctx, k)
        if used <= avail:
            break
    ctx["report"].append(("cover" + (" (tight)" if k < 1 else ""), round(used / 72, 2),
                          round(avail / 72, 2)))
    if used > avail:
        ctx["overfull"].append(f"cover: predicted {(used - avail) / 72:.2f} in too tall")


def concept_review_page(doc, spec, ctx):
    """The standing last page: what each section was for, the one mix-up to watch
    for, and a few questions to answer with the explanations covered."""
    pal, cr = ctx["pal"], spec["conceptReview"]
    start = len(doc.element.body)
    break_before(doc)
    # The same title bar as a section (SHULL-CHG-0030), carrying the unit's code, with
    # the page's subtitle in the learning-target slot, unlabelled and in label grey.
    section_bar(doc, ctx, cr.get("title", "Concept Review"), ctx["unit_code"],
                cr.get("subtitle"), target_label=None, target_color=pal.label)
    pin(doc.add_paragraph(), 8)
    for i, s in enumerate(cr.get("sections", [])):
        t = table(doc, [1.1, TEXT_W_IN - 1.1])
        a, b = t.rows[0].cells
        mar(a, 5, 0, 0, 0); mar(b)
        write(a.paragraphs[0], sec_label(s["code"]), 9, line=16, bold=True,
              color=pal.ink, before=0)
        write(b.paragraphs[0], s["heading"], 13, line=17, bold=True, color=pal.ink)
        pin(doc.add_paragraph(), 5)
        for para_ in s.get("paragraphs", []):
            lines = para_ if isinstance(para_, list) else [para_]
            for j, ln in enumerate(lines):
                write(doc.add_paragraph(), ln, BODY, line=15, color=pal.ink,
                      after=7 if j == len(lines) - 1 else 0)
        cmp_ = s.get("compare")
        if cmp_:
            t = table(doc, [TEXT_W_IN / 2, TEXT_W_IN / 2])
            for c, side in zip(t.rows[0].cells, (cmp_["left"], cmp_["right"])):
                mar(c, 0, 0, 0, 12)
                write(c.paragraphs[0], side["heading"], BODY, line=14.5, bold=True,
                      color=pal.ink)
                for ln in side.get("lines", []):
                    write(c.add_paragraph(), ln, BODY, line=14.5, color=pal.ink)
            pin(doc.add_paragraph(), 6)
        if s.get("watchOut"):
            write(doc.add_paragraph(), "**Watch out:** " + s["watchOut"], 9, line=13,
                  color=pal.ink, before=2, after=12)
        rule_para(doc, pal, after=14)
    qr = cr.get("quickRecall", [])
    if qr:
        label_para(doc, cr.get("quickRecallLabel", "Quick recall / cover the "
                                                   "explanations above"), pal, before=4)
        for i, q in enumerate(qr, 1):
            q, a = (q.get("q"), q.get("a")) if isinstance(q, dict) else (q, None)
            text = f"{i}. {q}" + (f"  **{a}**" if (ctx["key"] and a) else "")
            write(doc.add_paragraph(), text, BODY, line=15, color=pal.ink, after=3)
    els = [el for el in list(doc.element.body)[start:]
           if el.tag in (qn("w:p"), qn("w:tbl"))]
    for el in els:
        pin_all(el)
    used = sum(estimate_height(el, TEXT_W_IN) for el in els)
    ctx["report"].append(("review", round(used / 72, 2),
                          round((BODY_H_PT - SAFETY_PT) / 72, 2)))
    if used > BODY_H_PT - SAFETY_PT:
        ctx["overfull"].append(f"concept review: predicted "
                               f"{(used - BODY_H_PT + SAFETY_PT) / 72:.2f} in too tall")


# ---------------------------------------------------------------------------------
# Old flat specs -> paged schema.

_SMALL = {"a", "an", "and", "as", "at", "by", "for", "in", "of", "on", "or", "the",
          "to", "vs.", "vs"}


def title_case(s):
    words = str(s).strip().split()
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        if i and lw in _SMALL:
            out.append(lw)
        elif any(c.isdigit() for c in w) or (len(w) > 1 and w.isupper() and len(w) <= 3
                                             and lw not in {"the", "sun", "and"}):
            out.append(w if len(w) <= 3 else w.capitalize())
        else:
            out.append("-".join(p[:1].upper() + p[1:].lower() for p in w.split("-")))
    return " ".join(out)


def _legacy_row(r):
    # The cue label and notes heading are kept as the spec wrote them and printed in
    # course colour (SHULL-CHG-0030). `title` names the block in build messages.
    row = {k: v for k, v in r.items() if k != "problem"}
    row["title"] = title_case(r.get("cueLabel", ""))
    row["notes"] = list(r.get("notes", []))
    if r.get("problem"):
        p = dict(r["problem"])
        # The old GIVEN/NEED table becomes inline Given:/Find: lines. The old heading
        # label is dropped: the block title already names the example.
        prob = {k: p[k] for k in ("statement", "given", "workHeightIn", "answer",
                                  "solution") if p.get(k)}
        if p.get("need"):
            prob["find"] = p["need"]
        row["problem"] = prob
        row["kind"] = "example"
    return row


# Used only when an old spec has no howItWorks of its own.
LEGACY_HOW_TO_USE = ["Quiz yourself with the left-column questions.",
                     "A gray rule down the left of a line means must-write. Copy those "
                     "exactly.",
                     "Each section ends with a RECALL block. Close your notes before you "
                     "write it."]
LEGACY_WORK_BOX = "Show your reasoning and units in each work box."
# The old closing checklist names the old summary box. Only that term is renamed.
LEGACY_TERMS = (("Summary boxes", "RECALL blocks"), ("summary boxes", "RECALL blocks"),
                ("summary box", "RECALL block"))
# The old how-it-works names the colour of the old must-write rule ("A teal rule down
# the left of a line", "a gold rule down its left edge"). The rule is grey now
# (SHULL-CHG-0025, kept by 0030), so the colour word is corrected to match the page.
_RULE_COLOUR = re.compile(r"\b(teal|gold|lime|amber|rust|orange|green|aqua|purple|"
                          r"colou?red)(\s+(?:side\s+)?rules?)\b", re.I)


def _legacy_terms(text):
    for old, new in LEGACY_TERMS:
        text = text.replace(old, new)
    return text


def _legacy_how(text):
    return _RULE_COLOUR.sub(lambda m: ("Gray" if m.group(1)[0].isupper() else "gray")
                            + m.group(2), _legacy_terms(debullet(text)))


def pack_pages(rows, heights, heads, avail, per_page=3):
    """Choose where a section's page breaks fall.

    Every way of cutting the section's blocks into consecutive pages is tried - a
    section is a handful of blocks, so that is a few dozen cuts. A cut is allowed when
    each page fits its budget (the first page carries the section title bar, later
    ones no head) and holds at most `per_page` content blocks; a closing RECALL or REVIEW
    block does not count against that, it only has to fit. A single block too tall
    for any page is allowed a page of its own - there is nothing else to do with it.
    Of the allowed cuts: fewest sheets first, then the one whose emptiest sheet is
    fullest, so the spare room is shared instead of pooling on one sheet.
    """
    import itertools
    k = len(rows)
    best = None
    for mask in itertools.product((0, 1), repeat=max(k - 1, 0)):
        cuts = [0] + [i + 1 for i, m in enumerate(mask) if m] + [k]
        pages = [list(range(cuts[i], cuts[i + 1])) for i in range(len(cuts) - 1)]
        fills, ok = [], True
        for pi, idx in enumerate(pages):
            used = heads[0 if pi == 0 else 1] + sum(heights[i] for i in idx)
            content = sum(1 for i in idx if rows[i].get("kind") not in ("recall", "review"))
            if len(idx) > 1 and (used > avail or content > per_page):
                ok = False
                break
            fills.append(used / avail)
        if not ok:
            continue
        score = (len(pages), -min(fills))
        if best is None or score < best[0]:
            best = (score, pages)
    return [[rows[i] for i in idx] for idx in best[1]]


def normalize_legacy(spec, ctx):
    """Upgrade a flat spec (rows directly under each section) to the paged schema.

    Rows are packed onto pages by measured height, at most three blocks a page. The
    first page of a section carries its title bar and learning target; later pages
    carry no head. Each row keeps its cueLabel and notesLabel. The old summary box
    becomes a RECALL block, the old closing checklist a REVIEW block on the last
    section, and the cover carries the old front matter (SHULL-CHG-0030). Nothing is
    written that the spec did not already hold.
    """
    spec = copy.deepcopy(spec)
    avail = BODY_H_PT - SAFETY_PT - 2          # the same budget fit_page() holds a page to
    secs = spec["sectionsContent"]
    for si, sec in enumerate(secs):
        rows = [_legacy_row(r) for r in sec.get("rows", [])]
        rows.append({"kind": "recall", "title": "Section summary",
                     "cues": ["Close your notes before you write.",
                              "Use the checklist to find what still needs practice."],
                     "prompt": sec.get("summaryPrompt", ""),
                     # Two lines, as the approved reference has: an old spec carries no
                     # key answer to size the writing room to, and the third line is
                     # what pushed a RECALL block onto a sheet of its own.
                     "lines": 2,
                     "selfCheck": sec.get("selfCheck", [])})
        close = spec.get("close")
        if si == len(secs) - 1 and close:
            rows.append({"kind": "review", "title": "Pulling it together", "cues": [],
                         "bigPicture": close.get("bigPicture", ""),
                         "checklist": [_legacy_terms(x) for x in close.get("checklist", [])],
                         "fuzzyLabel": close.get("fuzzyLabel", "Still fuzzy on:")
                         .replace("STILL FUZZY ON", "Still fuzzy on")})
        # Packed against measured heights: the real section title bar on a first page,
        # each block as rendered, plus the 9 pt separator it brings. The breaks are
        # chosen, not accumulated - a greedy fill put blocks on a page until one did not
        # fit, which left single blocks on 40%-full sheets. See pack_pages().
        heights = [block_height(r, ctx) + 9 for r in rows]
        # A section's first page carries the title bar and learning target; the rest
        # carry no head (SHULL-CHG-0030).
        heads = (head_height(ctx, sec), 0.0)
        pages = pack_pages(rows, heights, heads, avail)
        sec["pages"] = [{"rows": p} for p in pages]
        sec.pop("rows", None)

    # The SHULL-CHG-0014 front matter goes on the cover as the spec wrote it
    # (SHULL-CHG-0030). Three corrections only: codes are zero-padded (SHULL-CHG-0007);
    # how-it-works names the grey must-write rule the page actually draws, not the old
    # teal/gold rule; and "summary box" becomes "RECALL block".
    has_problem = any(r.get("problem") for s in secs for p in s["pages"] for r in p["rows"])
    how = [_legacy_how(x) for x in spec.get("howItWorks", [])]
    if not how:
        how = LEGACY_HOW_TO_USE + ([LEGACY_WORK_BOX] if has_problem else [])
    cover = {
        "kicker": pad_codes(spec["kicker"]) if spec.get("kicker") else None,
        "unitTargets": [debullet(x) for x in spec.get("unitTargets", [])],
        "keyTerms": [debullet(x) for x in spec.get("keyTerms", [])],
        "howItWorks": how,
        "sectionList": [pad_codes(debullet(x)) for x in spec.get("sectionList", [])],
    }
    cover = {k: v for k, v in cover.items() if v}
    if spec.get("fields"):
        cover["fields"] = spec["fields"]
    if spec.get("titleImage"):
        cover["image"] = spec["titleImage"]
    eqs = spec.get("equations") or []
    if eqs:
        cols = [{"lines": []}, {"lines": []}]
        for i, eq in enumerate(eqs):
            col = cols[i % 2]["lines"]
            if eq.get("note"):
                col.append({"heading": eq["note"][:1].upper() + eq["note"][1:]})
            if eq.get("num") and eq.get("den"):
                col.append({"lhs": eq.get("lhs", ""), "num": eq["num"], "den": eq["den"]})
            else:
                col.append(eq.get("plain", ""))
        cover["equationToolbox"] = {"label": spec.get("equationLabel",
                                                      "Equation toolbox"),
                                    "columns": cols}
    spec["cover"] = cover
    if spec.get("studyRecap") and not spec.get("conceptReview"):
        print("build_notes_docx: this spec has an old studyRecap block; the Concept "
              "Review page replaces it and does not read it.", file=sys.stderr)
    return spec


# ---------------------------------------------------------------------------------
# Checks that refuse to build.

def all_rows(spec):
    for sec in spec["sectionsContent"]:
        for page in sec.get("pages", []):
            for row in page["rows"]:
                yield sec, row


def validate(spec, course):
    valid = known_sections(course)
    codes = [sec_num(s) for s in spec.get("sections", [])]
    codes += [sec_num(s["code"]) for s in spec["sectionsContent"]]
    cov = spec.get("cover", {})
    codes += [sec_num(s["code"]) for s in cov.get("sections", [])]
    codes += [sec_num(g["code"]) for g in cov.get("keyTerms", [])
              if isinstance(g, dict) and g.get("code")]
    # An old spec's section checklist names its codes in running text ("S1.2   The Big
    # Bang ..."); they are checked like any other code.
    codes += [f"{int(m.group(1))}.{m.group(2)}" for x in cov.get("sectionList", [])
              for m in [re.search(r"\bS0*(\d{1,2})\.(\d)\b", str(x))] if m]
    codes += [sec_num(s["code"]) for s in spec.get("conceptReview", {}).get("sections", [])]
    bad = sorted({c for c in codes if c not in valid})
    if bad:
        print(f"build_notes_docx: section(s) {', '.join(bad)} are not in "
              f"courses/{course}/DECISIONS.md.", file=sys.stderr)
        return False

    # "Anytime problems need solved in guided notes leave a box for them to do it."
    # A rule that only lives in a document is not a mechanism, so this refuses to build.
    # It does not depend on how a block is titled: a worked example is declared
    # structurally ("kind": "example"), the declaration and the box must agree in both
    # directions, and a block with nothing to capture is refused outright - so stripping
    # the box from "Neutral iron-56" fails whether or not its title says EXAMPLE.
    # The title keywords stay as a second net for rows that forgot the declaration.
    missing = []
    for sec, row in all_rows(spec):
        kind = row.get("kind", "notes")
        where = f"{sec_label(sec['code'])} · {row.get('title')}"
        if kind == "example" and not row.get("problem"):
            missing.append(f"{where}: declared a worked example, has no problem block")
        elif row.get("problem") and kind != "example":
            missing.append(f'{where}: has a problem block but is not "kind": "example"')
        elif kind == "notes" and not any(row.get(k) for k in CAPTURE):
            missing.append(f"{where}: nothing on the capture side")
        elif kind == "notes" and not row.get("noWorkBox"):
            hay = " ".join([row.get("title", ""), row.get("notesLabel", "")]).upper()
            if any(w in hay for w in PROBLEM_WORDS):
                missing.append(f"{where}: reads as a problem to solve and has no work box")
    if missing:
        print("build_notes_docx: work-box check failed:", file=sys.stderr)
        for m in missing:
            print("   " + m, file=sys.stderr)
        print('\nA problem to solve is a "kind": "example" row with a "problem" block. A row '
              'that genuinely is not one takes "noWorkBox": true.\nStudents need somewhere '
              'to work it. SHULL-CHG-0016.', file=sys.stderr)
        return False

    # Course profiles. The three courses do not want the same document, and pretending
    # they do is how a Geology packet ends up with a kinematics equation bar.
    has_box = bool(cov.get("equationToolbox"))
    has_problem = any(r.get("problem") for _, r in all_rows(spec))
    if course == "geology":
        if has_box or has_problem:
            print("build_notes_docx: Geology has no math. Remove the equation toolbox and "
                  "the problem blocks — a Geology packet labels diagrams instead. "
                  "SHULL-CHG-0017.", file=sys.stderr)
            return False
    elif has_problem and not has_box:
        print(f"build_notes_docx: {course} packet has problems to solve and no equation "
              f"toolbox. Students need the equations up front so they know what they may "
              f"reference. Add cover.equationToolbox, or \"noEquationBar\": true.",
              file=sys.stderr)
        if not spec.get("noEquationBar"):
            return False
    return True


# ---------------------------------------------------------------------------------

def verify_pages(docx_path, expected):
    """Convert with LibreOffice and count sheets. A designed page that spilled shows up
    as one sheet too many - the failure this layout exists to prevent."""
    soffice = shutil.which("soffice")
    if not soffice:
        # A check that quietly does not run is a pass nobody earned.
        print("build_notes_docx: VERIFY FAILED — --verify needs LibreOffice (soffice) on "
              "the PATH to render the pages, and it is not there.", file=sys.stderr)
        return False
    import pymupdf
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", td,
                        docx_path], check=True, capture_output=True)
        pdf = os.path.join(td, os.path.splitext(os.path.basename(docx_path))[0] + ".pdf")
        got = len(pymupdf.open(pdf))
    if got != expected:
        print(f"build_notes_docx: VERIFY FAILED — {expected} designed pages rendered on "
              f"{got} sheets. A page spilled; shorten its content or its work box.",
              file=sys.stderr)
        return False
    print(f"verify: {got} sheets for {expected} designed pages")
    return True


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    verify = "--verify" in sys.argv
    spec_path = args[0] if args else os.path.join(HERE, "specs", "geo_u01_s01.2-s01.4.json")
    base_dir = os.path.dirname(os.path.abspath(spec_path))
    spec = json.load(open(spec_path))
    course = spec["course"]
    pal = GreyPalette(course)
    key = bool(spec.get("key"))
    unit = int(spec["unit"])
    COURSE = course.upper()
    ctx = {
        "pal": pal, "key": key, "base_dir": base_dir, "report": [], "overfull": [],
        "unit_title": unit_title(course, unit),
        "unit_code": f"U{unit:02d}", "course": course, "unit": unit, "derived": [],
        "footer": f"SHULL SCIENCE / {COURSE} / UNIT {unit:02d}" + (" / TEACHER KEY" if key
                                                                    else ""),
    }

    for old in ("watermarkImage",):
        if spec.get(old):
            print(f"build_notes_docx: \"{old}\" is no longer drawn — the notes carry one "
                  f"image, on the cover (cover.image).", file=sys.stderr)
    legacy = not any("pages" in s for s in spec["sectionsContent"])
    if legacy:
        spec = normalize_legacy(spec, ctx)

    if not validate(spec, course):
        return 1
    # Difficulty is a standard cover feature, but its values are course content: the
    # build says so when one is missing and never makes one up.
    rated = {sec_num(x["code"]) for x in spec.get("cover", {}).get("sections", [])
             if x.get("difficulty")}
    unrated = [sec_label(x["code"]) for x in spec["sectionsContent"]
               if sec_num(x["code"]) not in rated]
    if unrated and not legacy:
        print(f"build_notes_docx: no difficulty rating for {', '.join(unrated)} — add "
              f"cover.sections[].difficulty (1–10).", file=sys.stderr)

    code = COURSE_CODE[course]
    u = f"U{unit:02d}"
    labels = [sec_label(s["code"]) for s in spec["sectionsContent"]]
    span = f"{labels[0]}-{labels[-1]}" if len(labels) > 1 else labels[0]
    # standards/NAMING.md range form (S01.1-S01.5). A key gets _Key, so the default for
    # a key spec can never overwrite its student copy.
    out = args[1] if len(args) > 1 else \
        os.path.join(HERE, f"SHULL_{code}_Guided_Notes_{u}_{span}{'_Key' if key else ''}.docx")

    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = FONT
    st.font.size = Pt(BODY)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    s = doc.sections[0]
    s.page_width, s.page_height = Inches(PAGE_W_IN), Inches(PAGE_H_IN)
    s.left_margin = s.right_margin = Inches(MARGIN_LR_IN)
    s.top_margin, s.bottom_margin = Inches(MARGIN_TOP_IN), Inches(MARGIN_BOTTOM_IN)
    # The header is empty, but LibreOffice still reserves its one empty line below
    # the header distance. Set equal to the top margin, that line pushed every page's
    # content 12 pt down - the whole safety margin, measured off the rendered PDF.
    s.header_distance = Inches(0.2)

    designed = 1
    ctx["cover"] = cover_content(spec, ctx)
    if ctx["derived"] and not legacy:
        print("build_notes_docx: cover content derived from this spec (SHULL-CHG-0030):",
              file=sys.stderr)
        for m in ctx["derived"]:
            print("   " + m, file=sys.stderr)
    cover_page(doc, spec, ctx)
    for sec in spec["sectionsContent"]:
        for pi, page in enumerate(sec["pages"], 1):
            page["_n"] = pi
            content_page(doc, ctx, sec, page)
            designed += 1

    if spec.get("conceptReview"):
        concept_review_page(doc, spec, ctx)
        designed += 1
    else:
        print("build_notes_docx: no conceptReview in this spec — building without the "
              "standing Concept Review page. Every packet should end with one.",
              file=sys.stderr)

    footer(s, ctx)
    nobreak_hyphens(doc.element.body)
    trim_tail(doc)
    schema_order(doc)
    doc.save(out)

    print(f"wrote {out}  —  {code} {u} {span}  —  {designed} designed pages"
          + ("  (upgraded from a flat spec)" if legacy else ""))
    for label, used, avail in ctx["report"]:
        print(f"   {label:<12} {used:5.2f} in of {avail:.2f} in")
    if ctx["overfull"]:
        print("build_notes_docx: predicted to spill onto an extra sheet:", file=sys.stderr)
        for m in ctx["overfull"]:
            print("   " + m, file=sys.stderr)
    if verify and not verify_pages(out, designed):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
