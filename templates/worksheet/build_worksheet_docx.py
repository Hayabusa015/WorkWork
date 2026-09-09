#!/usr/bin/env python3
"""Build a SHULL worksheet / practice set as .docx from a JSON spec.

    python3 templates/worksheet/build_worksheet_docx.py specs/<spec>.json out.docx

One builder, three course profiles. The three courses do not want the same sheet, and
pretending they do is how a Geology worksheet ends up with a work box.

  Chemistry  Conceptual and math. Every math question gets an open box to solve in,
             carrying a SHOW WORK HERE watermark. Equations sit at the top of the page.
             Diagrams and charts to complete are first-class.
  Physics    NO work areas at all. Students work in their Hayden-McNeil carbonless lab
             notebooks, so work boxes and answer rules are refused outright. The page
             carries the equations and a prior-knowledge recall block instead, and the
             questions ramp: warm-up, practice, challenge, then one multi-topic problem
             that reaches back into earlier units.
  Geology    No math. Visual and expressive: diagrams to label, panels to draw in,
             cards to cut, slots to glue them into. A Geology sheet with an equation
             bar or a work box is refused.

The profile is enforced here, at build time. A rule that only lives in a document is
not a mechanism.

A packet holds one or more sections, each starting a new page - the shape of his own
PHYS U01 practice sets, which run one section per page across the whole unit.

Colour comes from brand/tokens.json. No hex is typed in this file.
"""
import json, os, sys
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _shull_docx import (          # noqa: E402
    COURSE_CODE, Palette, debullet, known_sections, unit_title,
    borders, para, run, check_item, rule_lines, fix_widths, one_cell, no_split,
    equation_bar, work_box, given_need, diagram_block, page_setup, running_footer,
    text_width_in, cell_margins, gap,
)

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))

TEXT_W_IN = 7.50
NUM_W_IN = 0.30                                  # the question number's own column
BODY_W_IN = TEXT_W_IN - NUM_W_IN

# The ramp, per course. His own PHYS U01 practice sets run 2 warm-up, 2 practice,
# 1 challenge, 1 multi-topic per section - six questions, easy to start and finishing on
# a problem that reaches into another unit. The inherited studio spec said eight
# (2/3/2/1); it is marked INHERITED in docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md, meaning
# nobody confirmed it, and his shipped packet is the better evidence. SHULL-CHG-0019
# records the conflict.
TIERS = ("warm-up", "practice", "challenge", "multi-topic")
TIER_PT = 7                     # the tag is metadata, set below the body size
TIER_TRACK_PT = 1.3             # w:spacing val 26, in points per character
TIER_GAP_IN = 0.10              # the gap between the tag and the prompt it labels
# Exact counts are enforced only where there is evidence for them. Physics has a
# shipped packet to read; Chemistry does not, so it gets the ORDER of the ramp enforced
# and picks its own counts. Inventing a Chemistry count and calling it locked is how
# the 8-question figure got into the system in the first place.
RAMP = {
    "physics":   {"warm-up": 2, "practice": 2, "challenge": 1, "multi-topic": 1},
    "chemistry": None,
    "geology":   None,          # a Geology sheet is an activity, not a question ladder
}


def tier_col_in():
    """Width of the tier column, measured from the longest tier name.

    The tags used to run inline with the prompt, which left every question starting at
    a different place and every wrapped line running back under the tag. Giving the tag
    its own column fixes both - but only if the column is wide enough for the longest
    name, or "MULTI-TOPIC" wraps to two lines and looks worse than what it replaced.
    So it is measured off the shipped Archivo files rather than picked, and it follows
    the tier names if they are ever renamed.
    """
    widest = max(text_width_in(t.upper(), TIER_PT, bold=True)
                 + TIER_TRACK_PT * len(t) / 72.0 for t in TIERS)
    # The tag is set right, so it needs no slack on its left - only the gap to the
    # prompt on its right. The cell's own margins are zeroed to match, because every
    # hundredth of an inch here comes straight off the prompt column, and on a
    # one-page-per-section sheet that is the difference between four pages and five.
    return round(widest + TIER_GAP_IN, 2)
WORK_MIN_IN = 1.6
WATERMARK = "SHOW WORK HERE"


# --------------------------------------------------------------------------- blocks

def page_break(doc):
    """Start a new page without spending a line to do it.

    A normal paragraph carrying a page break is full body height, so when a section
    ends flush with the bottom of its page that paragraph does not fit - it moves to
    the next page, and only then breaks, leaving a blank page carrying nothing but the
    footer. Pinning the line to 1pt exact makes the break paragraph effectively
    dimensionless, so it always fits where it is written.
    """
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(0); pf.space_after = Pt(0)
    pPr = p._p.get_or_add_pPr()
    sp = OxmlElement("w:spacing")
    sp.set(qn("w:before"), "0"); sp.set(qn("w:after"), "0")
    sp.set(qn("w:line"), "20"); sp.set(qn("w:lineRule"), "exact")
    pPr.append(sp)
    r = p.add_run()
    r.font.size = Pt(1)
    r.add_break(WD_BREAK.PAGE)
    return p


def label(cell, text, pal, size=7.5, first=False):
    return para(cell, text, size, bold=True, color=pal.accent, caps_track=True, first=first)


def arrow(doc, pal):
    """The reading-order arrow between rows of cards. It is on his sheet and it does
    real work - without it the six cards read as a grid, not a sequence."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    run(p, "↓", 11, bold=True, color=pal.display)
    return p


def grid(doc, n, across, height_in, pal, gutter=0.18, arrows=True):
    """A grid of equal cells, `across` per row, each row held together across a break.

    One table per ROW, not one table for the whole grid: cantSplit holds a row and does
    nothing across two, and a card sliced in half by a page break cannot be cut out.
    Columns are separated by a narrow spacer column rather than by cell margins, so the
    dashed cut lines of two neighbouring cards never touch.
    """
    cols = across * 2 - 1
    cell_w = round((TEXT_W_IN - gutter * (across - 1)) / across, 3)
    widths = []
    for i in range(across):
        widths.append(cell_w)
        if i < across - 1:
            widths.append(gutter)
    rows = (n + across - 1) // across
    out = []
    for r in range(rows):
        t = doc.add_table(rows=1, cols=cols)
        fix_widths(t, widths)
        no_split(t.rows[0], height_in)
        for i in range(across):
            if r * across + i < n:
                out.append(t.rows[0].cells[i * 2])
        if r < rows - 1 and arrows:
            arrow(doc, pal)
        else:
            gap(doc, 4)   # cards need air between rows even without an arrow
    return out


def cards_block(doc, block, pal):
    """Cards to cut out. Dashed border, title, description, and a box to draw in.

    Straight off his Nebular Theory sheet, which is the one he named as the look he
    wants: "cut it out, and color or sketch a small illustration for it."
    """
    items = block["cards"]
    across = int(block.get("across", 2))
    h = float(block.get("cardHeightIn", 1.65))
    draw_h = float(block.get("drawHeightIn", 0.95))
    cells = grid(doc, len(items), across, h, pal, arrows=block.get("arrows", True))
    for cell, card in zip(cells, items):
        borders(cell, pal.label, sz=6, val="dashed")
        label(cell, block.get("cutLabel", "✂  CUT ALONG THE DASHED LINE"), pal,
              size=6.5, first=True)
        para(cell, card["title"], 11, bold=True, color=pal.accent)
        para(cell, card["text"], 9)
        label(cell, block.get("drawLabel", "COLOR OR SKETCH THIS STAGE:"), pal, size=6.5)
        t = cell.add_table(rows=1, cols=1)
        fix_widths(t, [round(TEXT_W_IN / across - 0.5, 2)])
        no_split(t.rows[0], draw_h)
        borders(t.rows[0].cells[0], pal.ink, sz=4)
    return cells


def slots_block(doc, block, pal):
    """Numbered slots the cut cards get glued into, sized to match the cards."""
    n = int(block.get("slots", 6))
    across = int(block.get("across", 2))
    h = float(block.get("slotHeightIn", 1.65))
    inner_h = float(block.get("innerHeightIn", 0.80))
    cells = grid(doc, n, across, h, pal, arrows=block.get("arrows", True))
    for i, cell in enumerate(cells, 1):
        borders(cell, pal.ink, sz=8)
        label(cell, f"{block.get('slotLabel', 'GLUE HERE — SLOT')} {i}", pal,
              size=6.5, first=True)
        t = cell.add_table(rows=1, cols=1)
        fix_widths(t, [round(TEXT_W_IN / across - 0.5, 2)])
        no_split(t.rows[0], inner_h)
        borders(t.rows[0].cells[0], pal.label, sz=4, val="dashed")
    return cells


def draw_block(cell, block, pal, width):
    """Blank panels to draw in, captioned underneath. The lighter cousin of `cards` -
    used when there is nothing to cut, only something to show."""
    n = int(block.get("panels", 4))
    across = int(block.get("across", 4))
    col_w = round(width / across, 3)
    panel_h = float(block.get("panelHeightIn", 1.7))
    label(cell, block.get("label", "DRAW IT"), pal)
    if block.get("instruction"):
        para(cell, block["instruction"], 9.5)
    captions = block.get("captions") or []
    rows = (n + across - 1) // across
    t = cell.add_table(rows=rows * 2, cols=across)
    fix_widths(t, [col_w] * across)
    for i in range(n):
        r, c = divmod(i, across)
        panel = t.rows[r * 2].cells[c]
        borders(panel, pal.ink, sz=4)
        no_split(t.rows[r * 2], panel_h)
        # Just the number. No box, no square, no circle. SHULL-CHG-0015.
        para(panel, str(i + 1), 9, bold=True, color=pal.ink, first=True)
        under = t.rows[r * 2 + 1].cells[c]
        borders(under, pal.hair, sz=4, edges=("bottom",))
        cap = captions[i] if i < len(captions) else block.get("captionPrompt", "")
        para(under, cap, 8, color=pal.label, first=True)
    return t


def reflection_block(doc, block, pal):
    """The written close on his Geology sheet: italic prompts, a full-width rule under
    each. Ruled lines are for prose - this is the one place a Geology sheet writes."""
    c = one_cell(doc)
    label(c, block.get("label", "REFLECTION"), pal, first=True)
    for i, q in enumerate(block["prompts"], 1):
        p = c.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        run(p, f"{i}. ", 9.5, bold=True, color=pal.ink)
        run(p, q, 9.5, italic=True, color=pal.ink)
        rule_lines(c, int(block.get("linesEach", 2)), pal.ink)
    return c


# ------------------------------------------------------------------------ questions

def question_block(doc, q, i, pal, course, base_dir):
    tier_w = tier_col_in()
    t = doc.add_table(rows=1, cols=3)
    fix_widths(t, [NUM_W_IN, tier_w, BODY_W_IN - tier_w])
    # A question stays whole. Split across a page break, the parts and the work box
    # land on the next sheet with no number above them - the student sees an unlabelled
    # box and four lettered parts belonging to nothing.
    no_split(t.rows[0])
    numcell, tiercell, body = t.rows[0].cells
    # Just the number. No box, no square, no circle, in any format. SHULL-CHG-0015 -
    # his existing Physics sheet sets these in solid navy squares, which is both the
    # withdrawn number-box and a fill on a printed page.
    para(numcell, str(i), 11, bold=True, color=pal.accent, first=True)

    # The tier tag has its own column, set right so every tag ends on one edge and
    # every prompt begins on one edge. It carries no box at all: a run border cannot be
    # padded, so a boxed tag at 7pt is always clamped to the cap height and looks
    # stamped on, and a box drawn on the cell is a tall empty rectangle beside one word.
    # Four tiers in four different border weights read as a rendering fault rather than
    # a scale. The word is the tag.
    if q.get("tier"):
        # No margin on the left, where a right-set tag does not need one; the gap to
        # the prompt is on the right, where it is visible.
        cell_margins(tiercell, left=0, right=TIER_GAP_IN * 1440)
        p = para(tiercell, q["tier"].upper(), TIER_PT, bold=True, color=pal.accent,
                 caps_track=True, first=True)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    para(body, q["prompt"], 10, color=pal.ink, first=True)
    for part in q.get("parts", []):
        # Multi-part items keep full body size on every part.
        para(body, "   " + debullet(part), 10, color=pal.ink)

    body_inner = round(BODY_W_IN - tier_w - 0.16, 2)
    if q.get("diagram"):
        diagram_block(body, q["diagram"], pal, body_inner, base_dir)
    if q.get("draw"):
        draw_block(body, q["draw"], pal, body_inner - 0.2)
    if q.get("given") or q.get("need"):
        given_need(body, q.get("given", ""), q.get("need", ""), pal, body_inner)

    if q.get("math"):
        work_box(body, q.get("workLabel", ""), pal,
                 float(q.get("workHeightIn", WORK_MIN_IN)), body_inner,
                 watermark=q.get("watermark", WATERMARK))
    elif q.get("answerLines"):
        answer = int(q["answerLines"])
        rule_lines(body, answer, pal.hair)

    if q.get("selfCheck"):
        # Bracketed self-check answers for NUMERIC results only - never for an
        # explanation, a vocabulary term, or a graph reading, where the bracket hands
        # over the whole answer.
        pp = para(body, q["selfCheck"], 8, color=pal.label)
        pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    gap(doc, 3)
    return t


# ------------------------------------------------------------------------- profiles

def refuse(msg, *more):
    print("build_worksheet_docx: " + msg, file=sys.stderr)
    for m in more:
        print("   " + m, file=sys.stderr)
    return 1


def check_profile(spec, course, sec):
    """The course profile, enforced. Returns an error string or None."""
    qs = sec.get("questions", [])
    eqs = sec.get("equations", spec.get("equations")) or []
    blocks = sec.get("blocks", [])
    math_qs = [q for q in qs if q.get("math")]
    work_qs = [q for q in qs if q.get("math") or q.get("answerLines")]
    visual = ([q for q in qs if q.get("diagram") or q.get("draw")]
              + [b for b in blocks if b["kind"] in ("cards", "slots", "draw", "diagram")])
    where = f"section {sec['code']}"

    if course == "geology":
        if eqs:
            return (f"{where}: Geology has no math, so it has no equation bar. "
                    'Remove "equations". SHULL-CHG-0017.')
        if math_qs:
            return (f"{where}: Geology has no math. Remove \"math\" from "
                    f"{len(math_qs)} question(s). SHULL-CHG-0017.")
        if not visual:
            return (f"{where}: nothing to label, draw, cut or order. Geology is the "
                    "visual, expressive class - every sheet needs at least one "
                    "diagram, draw, cards or slots block. SHULL-CHG-0019.")

    if course == "physics":
        if work_qs:
            return (f"{where}: Physics carries no work areas at all - no ruled lines, "
                    "no work boxes. Students work in their Hayden-McNeil carbonless "
                    'lab notebooks. Remove "math" and "answerLines" from '
                    f"{len(work_qs)} question(s). SHULL-CHG-0019.")
        if not (sec.get("priorKnowledge") or spec.get("priorKnowledge")):
            return (f"{where}: no prior-knowledge recall block. Students arrive at a "
                    "friction problem having last seen free-body diagrams two weeks "
                    'ago. Add "priorKnowledge".')
        if not eqs:
            return (f"{where}: no equations. They go at the top of the page so "
                    "students know what they may reach for.")

    if course == "chemistry":
        if math_qs and not eqs and not spec.get("noEquationBar"):
            return (f"{where}: math questions and no equation bar. Add \"equations\", "
                    'or "noEquationBar": true if the math genuinely needs none.')

    ramp = RAMP[course]
    if ramp and qs:
        shape = {}
        for q in qs:
            shape[q.get("tier")] = shape.get(q.get("tier"), 0) + 1
        if shape != ramp:
            want = ", ".join(f"{k} {ramp[k]}" for k in TIERS)
            got = ", ".join(f"{k} {shape.get(k, 0)}" for k in TIERS)
            return (f"{where}: the ramp is {want}. This section has {got}. The ramp is "
                    "what makes a sheet start easy and finish on a full problem.")
    if qs and course != "geology":
        # The order is the ramp, whatever the counts are: difficulty never goes
        # backwards, and the multi-topic problem is last because it is the one that
        # reaches back into earlier units.
        seen = [TIERS.index(q.get("tier")) for q in qs if q.get("tier") in TIERS]
        if len(seen) != len(qs):
            loose = [q.get("tier") for q in qs if q.get("tier") not in TIERS]
            return f"{where}: unknown tier(s) {loose}. Tiers are {list(TIERS)}."
        if seen != sorted(seen):
            return (f"{where}: the questions do not ramp - "
                    f"{[q['tier'] for q in qs]}. Easy to start, harder as it goes.")
        if qs[-1].get("tier") != "multi-topic":
            return (f"{where}: the last question is {qs[-1].get('tier')!r}. It should be "
                    "the multi-topic problem that reaches back into earlier units.")
    return None


# ------------------------------------------------------------------------------ main

def main():
    if len(sys.argv) < 2:
        return refuse("usage: build_worksheet_docx.py <spec.json> [out.docx]")
    spec = json.load(open(sys.argv[1]))
    course = spec["course"]
    if course not in COURSE_CODE:
        return refuse(f"unknown course {course!r}.")
    pal = Palette(course)
    sections = spec["sectionsContent"]

    valid = known_sections(course)
    bad = [s for s in spec["sections"] if s not in valid]
    if bad:
        return refuse(f"section(s) {', '.join(bad)} are not in "
                      f"courses/{course}/DECISIONS.md.",
                      "Nothing is built against a code not in the decisions file.")
    declared = [s["code"] for s in sections]
    if declared != list(spec["sections"]):
        return refuse(f"sections {spec['sections']} but content for {declared}. "
                      "The two lists are the same fact and must agree.")

    for sec in sections:
        err = check_profile(spec, course, sec)
        if err:
            return refuse(err)

    code = COURSE_CODE[course]
    unit = f"U{int(spec['unit']):02d}"
    utitle = unit_title(course, spec["unit"])       # a course fact, read not typed
    span = (f"S{spec['sections'][0]}-S{spec['sections'][-1]}"
            if len(spec["sections"]) > 1 else f"S{spec['sections'][0]}")
    kind = spec.get("docType", "Practice_Set")
    out = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.join(HERE, f"SHULL_{code}_{kind}_{unit}_{span}.docx")

    doc = Document()
    s = page_setup(doc)

    for si, sec in enumerate(sections):
        if si:
            page_break(doc)

        # ---- Header. Outlined, not filled: design system section 8. His existing
        # Physics sheet runs a solid navy banner across the top of every page, which is
        # the single largest ink cost on it.
        c = one_cell(doc)
        borders(c, pal.display, sz=18, edges=("bottom",))
        para(c, f"SHULL SCIENCE  ·  {course.upper()}  ·  MR. SHULL  ·  "
                f"UNIT {int(spec['unit'])} — {utitle.upper()}", 7.5, bold=True,
             color=pal.accent, caps_track=True, first=True)
        para(c, sec["title"], 15, bold=True, color=pal.ink)
        para(c, f"{kind.replace('_', ' ').upper()}  ·  {unit} / S{sec['code']}"
                + (f"  ·  ~{spec['timeTargetMin']} MIN" if spec.get("timeTargetMin") else ""),
             7.5, color=pal.label, caps_track=True)

        # ---- Name / Date / Period / Score. The score total is summed from the
        # questions, never typed: a header reading "/ 20" over questions adding to 18
        # is one fact stored in two places.
        total = (sum(int(q.get("points", 1)) for q in sec.get("questions", []))
                 + sum(int(b.get("points", 0)) for b in sec.get("blocks", [])))
        t = doc.add_table(rows=1, cols=2)
        fix_widths(t, [5.95, 1.55])
        a, b = t.rows[0].cells
        borders(a, pal.hair); borders(b, pal.ink, sz=8)
        para(a, "NAME ______________________________   DATE _____________   "
                "PERIOD _____", 9, color=pal.label, first=True)
        pp = para(b, "SCORE", 7, bold=True, color=pal.accent, caps_track=True, first=True)
        pp = para(b, f"_______  /  {total}", 10, bold=True, color=pal.ink)
        pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT

        # ---- What this is about, before anything is asked of them.
        gap(doc, 2)
        c = one_cell(doc)
        borders(c, pal.display, sz=18, edges=("left",))
        label(c, sec.get("conceptLabel", "THE CONCEPT — READ THIS FIRST"), pal, first=True)
        para(c, sec["concept"]["summary"], 9.5)
        for x in sec["concept"].get("keyIdeas", []):
            para(c, "•  " + debullet(x), 9.5)

        pk = sec.get("priorKnowledge", spec.get("priorKnowledge"))
        if pk:
            gap(doc, 2)
            c = one_cell(doc); borders(c, pal.hair)
            label(c, pk.get("label", "BEFORE YOU START — YOU ALREADY KNOW THIS"),
                  pal, first=True)
            for x in pk["items"]:
                para(c, "•  " + debullet(x), 9.5)

        eqs = sec.get("equations", spec.get("equations")) or []
        if eqs:
            gap(doc, 2)
            equation_bar(doc, eqs, pal,
                         spec.get("equationLabel", "EQUATIONS YOU MAY USE"))

        if sec.get("directions"):
            gap(doc, 2)
            c = one_cell(doc); borders(c, pal.ink, sz=8, edges=("top",))
            label(c, "DIRECTIONS", pal, first=True)
            para(c, sec["directions"], 9.5)

        gap(doc, 4)
        for i, q in enumerate(sec.get("questions", []), 1):
            question_block(doc, q, i, pal, course, HERE)

        for bi, block in enumerate(sec.get("blocks", [])):
            kindb = block["kind"]
            if block.get("pageBreakBefore"):
                page_break(doc)
                c = one_cell(doc); borders(c, pal.display, sz=18, edges=("bottom",))
                para(c, block.get("heading", sec["title"]), 15, bold=True,
                     color=pal.ink, first=True)
            if block.get("instruction") and kindb in ("cards", "slots"):
                c = one_cell(doc)
                para(c, block["instruction"], 9.5, color=pal.ink, first=True)
                gap(doc, 2)
            if kindb == "cards":
                cards_block(doc, block, pal)
            elif kindb == "slots":
                slots_block(doc, block, pal)
            elif kindb == "reflection":
                reflection_block(doc, block, pal)
            elif kindb == "draw":
                draw_block(one_cell(doc), block, pal, TEXT_W_IN - 0.3)
            elif kindb == "diagram":
                diagram_block(one_cell(doc), block, pal, TEXT_W_IN - 0.3, HERE)
            else:
                return refuse(f"unknown block kind {kindb!r} in section {sec['code']}.")

        if sec.get("close"):
            # Banner and checklist in ONE non-splitting row. As two tables they broke
            # apart at the page edge and a section ended on a banner with its checklist
            # stranded alone on the next page.
            t = doc.add_table(rows=1, cols=1)
            fix_widths(t, [TEXT_W_IN])
            no_split(t.rows[0])
            c = t.rows[0].cells[0]
            borders(c, pal.ink, sz=12, edges=("top",))
            borders(c, pal.display, sz=18, edges=("bottom",))
            para(c, sec["close"]["banner"], 9, bold=True, color=pal.ink,
                 caps_track=True, first=True)
            for x in sec["close"].get("checklist", []):
                check_item(c, x, pal)

    running_footer(s, f"SHULL SCIENCE          {unit} · {span}", pal,
                   with_page_numbers=True)
    doc.save(out)
    nq = sum(len(x.get("questions", [])) for x in sections)
    print(f"wrote {out}  —  {code} {unit} {span}, "
          f"{len(sections)} section(s), {nq} question(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
