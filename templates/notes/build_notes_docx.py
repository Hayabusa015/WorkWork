#!/usr/bin/env python3
"""Build a guided/Cornell notes packet as .docx from the same JSON spec. Option A.

Identical structure and content to build_notes.py - the difference is the output.
A .docx can be edited in Word and typed into by a student; it cannot hold the
layout as exactly as the PDF, because Word reflows.

    python3 templates/notes/build_notes_docx.py specs/<spec>.json out.docx

Colour comes from brand/tokens.json. No hex is typed in this file.
"""
import json, os, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Every primitive on this page - how a work box is drawn, how a fraction stacks, how a
# diagram block holds together across a page break - is shared with the worksheet
# builder. It lives in one file so the two cannot drift.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _shull_docx import (          # noqa: E402
    T, G, FONT, FLOOR, COURSE_CODE, Palette, hexof, debullet, known_sections,
    unit_title,
    borders, para, check_item, rule_lines, fix_widths, tight_cells, one_cell,
    no_split, gap, stacked_frac, equation_bar, work_box, given_need, diagram_block,
    fillin_table, unpad_cell, cell_margins, page_setup, running_footer, trim_tail,
    add_watermark, study_recap_page,
)


# SHULL-CHG-0019. Matthew's own words: "if there's a matter flow chart, I kind of just
# want them to fill in their own matter flow chart on the paper." Guided notes capture
# what's on the board during lecture - they are not a reasoning worksheet - so the
# S1.1 Matter Flowchart row is a small tree of boxes the student labels as it's drawn,
# not a set of open questions. This is specific to one row in one course's one section,
# so it lives here rather than in _shull_docx.py: a shared primitive is for a shape
# more than one builder needs, and nothing else in the system draws a branching tree.
# Archivo carries "↓" (down arrow) but none of the diagonal arrow glyphs, so the
# connectors are straight-down arrows only - the branching itself is shown by which
# columns of the grid each box spans, the same way Matthew draws it on the board.
def matter_flowchart(cell, pal, inner_w, filled=False):
    """S1.1's Matter Flowchart: MATTER splits into Pure substance / Mixture, and each
    of those splits again into Element/Compound and Homogeneous/Heterogeneous.

    `filled=False` (student copy): only MATTER is printed; every other box is blank
    for the student to label as the chart goes up on the board. `filled=True` (key):
    every box carries its answer. Same four-column grid either way, so the two
    documents stay pixel-for-pixel comparable - the key is the student page, answered.
    """
    box_h = 0.34
    t = cell.add_table(rows=5, cols=4)
    fix_widths(t, [inner_w / 4] * 4)
    tight_cells(t, top=16, bottom=16, left=30, right=30)

    def box(c, text):
        borders(c, pal.hair, sz=6)
        c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = para(c, text, 9.5, bold=True, color=pal.ink, first=True)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    def arrow(c):
        c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = para(c, "↓", 11, bold=True, color=pal.hair, first=True)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Level 1 - MATTER, the one thing everyone starts from. Centred over the row by
    # merging only the middle two columns; the outer two stay unbordered spacers.
    top = t.rows[0].cells[1].merge(t.rows[0].cells[2])
    box(top, "MATTER")
    no_split(t.rows[0], box_h)

    # One connector, then the fork into two.
    left_arrow = t.rows[1].cells[0].merge(t.rows[1].cells[1])
    right_arrow = t.rows[1].cells[2].merge(t.rows[1].cells[3])
    arrow(left_arrow)
    arrow(right_arrow)

    # Level 2 - Pure substance / Mixture.
    pure = t.rows[2].cells[0].merge(t.rows[2].cells[1])
    mix = t.rows[2].cells[2].merge(t.rows[2].cells[3])
    box(pure, "Pure substance" if filled else "")
    box(mix, "Mixture" if filled else "")
    no_split(t.rows[2], box_h)

    # Connector into the four leaves - one arrow per leaf, directly above it.
    for c in t.rows[3].cells:
        arrow(c)

    # Level 3 - the four leaves, in the deck's own order.
    leaves = ["Element", "Compound", "Homogeneous", "Heterogeneous"]
    for c, name in zip(t.rows[4].cells, leaves):
        box(c, name if filled else "")
    no_split(t.rows[4], box_h)
    return t

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))


# SHULL-CHG-0016. Matthew's physics packet puts a bordered box under every worked
# example - a 1x1 table, ~1in tall, hRule "atLeast" so it grows but never shrinks, and
# cantSplit so it never breaks across a page. Students work the problem inside it.
# His rule: "anytime problems need solved in guided notes leave a box for them to do it."
WORK_BOX_MIN_IN = 1.4          # his was 0.98in; a little more room for kinematics
GIVEN_LABEL_IN = 0.72

# A watermark is a whisper you notice only if you look for it. Its ink level is the
# design system's (print.watermarkOpacityPct, applied in add_watermark); its size and
# position are this template's, because they depend on where THIS page puts content.
WATERMARK_W_IN = 3.0
WATERMARK_VERT_FRAC = 0.80

# The Cornell split, decided once. His own packets ran a 1.88in (Geology) / 2.00in
# (Physics) cue column; he asked for it narrower and condensed - the cue is a prompt,
# not a second body column, and every inch it gives back goes to the notes side where
# the students actually write. Everything on the notes side is measured off NOTES_INNER
# so nothing has to be re-derived when this moves again.
TEXT_W_IN = 7.50
CUE_W_IN = 1.28
NOTES_W_IN = TEXT_W_IN - CUE_W_IN          # 6.22
CELL_MAR_IN = 0.56                          # default tcMar, both sides, both nestings
NOTES_INNER_IN = round(NOTES_W_IN - CELL_MAR_IN, 2)   # 5.66


# The weight ladder. Every border in the body used to be the same hairline at the same
# weight, so a section boundary, a row divider and the inside edge of a fill-in table
# all claimed the page equally and the sheet read as one undifferentiated grid. Four
# steps is enough - in print a half-point reads clearly - and naming them here is what
# stops the next edit from picking a number that happens to look fine in isolation.
# Eighths of a point, which is what w:sz counts.
W_SECTION = 18      # the accent rule under a section head. Nothing else is this heavy.
W_HEAD_TOP = 12     # the ink rule above it
W_RAIL = 12         # the cue-column rail
W_ROW = 8           # one notes row from the next
W_BOX = 6           # an element's own outline - work box, learning target, summary
W_INNER = 4         # inside an element - table cells, given/need, writing lines

# "Siding": a vertical accent rule down the left edge of every cue cell. The Cornell
# split was drawn with the same hairline as everything else, so the page had no spine
# and the cue column did not read as a column at a glance - it read as the narrow
# cells of a table. A cell border, not a fill: SHULL_DESIGN_SYSTEM section 8, and the
# same mechanism as the masthead kicker and the must-write line, which is the one that
# renders reliably inside a nested cell in both Word and LibreOffice.
#
# It also gives the dead space at the foot of a short cue cell something to be. The
# notes side is always taller than its cue, so most cue cells end in a gap; with a rail
# running past it that gap is margin, and without one it is a hole.


# SHULL-CHG-0017. A fraction is stacked - numerator over denominator with a horizontal
# bar. Never "a/b" inline in the text. Built as a two-row table rather than Office Math
# (OMML): OMML is valid and Word renders it, but LibreOffice will not import it from

def main():
    spec_path = sys.argv[1] if len(sys.argv) > 1 \
        else os.path.join(HERE, "specs", "geo_u01_s01.2-s01.4.json")
    spec_dir = os.path.dirname(os.path.abspath(spec_path))
    spec = json.load(open(spec_path))
    course = spec["course"]
    pal = Palette(course)
    accent, display, ink, hair = pal.accent, pal.display, pal.ink, pal.hair
    label, footer, white = pal.label, pal.footer, pal.white

    valid = known_sections(course)
    bad = [s for s in spec["sections"] if s not in valid]
    if bad:
        print(f"build_notes_docx: section(s) {', '.join(bad)} are not in "
              f"courses/{course}/DECISIONS.md.", file=sys.stderr)
        return 1

    # "Anytime problems need solved in guided notes leave a box for them to do it."
    # A rule that only lives in a document is not a mechanism, so this refuses to build.
    PROBLEM_WORDS = ("EXAMPLE", "PRACTICE", "PROBLEM", "SOLVE", "CALCULATE", "YOUR TURN")
    missing = []
    for sec in spec["sectionsContent"]:
        for row in sec["rows"]:
            if row.get("problem") or row.get("noWorkBox"):
                continue
            hay = " ".join([row.get("cueLabel", ""), row.get("notesLabel", "")]).upper()
            if any(w in hay for w in PROBLEM_WORDS):
                missing.append(f"{sec['code']} · {row.get('notesLabel') or row.get('cueLabel')}")
    if missing:
        print("build_notes_docx: these rows look like problems to solve and have no work box:",
              file=sys.stderr)
        for m in missing:
            print("   " + m, file=sys.stderr)
        print('\nAdd a "problem" block, or "noWorkBox": true if it genuinely is not one.\n'
              'Students need somewhere to work it. SHULL-CHG-0016.', file=sys.stderr)
        return 1

    # Course profiles. The three courses do not want the same document, and pretending
    # they do is how a Geology packet ends up with a kinematics equation bar.
    eqs = spec.get("equations") or []
    has_problem = any(r.get("problem") for sec in spec["sectionsContent"] for r in sec["rows"])
    if course == "geology":
        if eqs or has_problem:
            print("build_notes_docx: Geology has no math. Remove the equation bar and the "
                  "problem blocks — a Geology packet labels diagrams instead. SHULL-CHG-0017.",
                  file=sys.stderr)
            return 1
    else:
        if has_problem and not eqs:
            print(f"build_notes_docx: {course} packet has problems to solve and no equation "
                  f"bar. Students need the equations at the top of the page so they know what "
                  f"they may reference. Add \"equations\", or \"noEquationBar\": true.",
                  file=sys.stderr)
            if not spec.get("noEquationBar"):
                return 1

    code = COURSE_CODE[course]
    unit = f"U{int(spec['unit']):02d}"
    span = (f"S{spec['sections'][0]}-S{spec['sections'][-1]}"
            if len(spec["sections"]) > 1 else f"S{spec['sections'][0]}")
    out = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.join(HERE, f"SHULL_{code}_Guided_Notes_{unit}_{span}.docx")

    doc = Document()
    s = page_setup(doc)

    # Optional faint background image, repeating on every page including the title
    # page and the closing recap page - the header holds it once because this
    # template never splits into a new section. Path is resolved against the SPEC
    # FILE's own directory, the same convention as titleImage. Absent field or
    # missing file: no change from prior behavior.
    wm_spec = spec.get("watermarkImage")
    if wm_spec:
        wm_path = os.path.join(spec_dir, wm_spec["path"])
        if os.path.exists(wm_path):
            # Geometry is the template's, not the spec's. At the 5.0in the Chemistry
            # spec asked for, centred, the atom sat directly behind the matter
            # flowchart, the work box and the fill-in prompts - a second drawing
            # competing with the first on the page a student is trying to write on.
            # A watermark is a ground: small enough not to reach the content column's
            # working width, low enough to sit in the quiet bottom third of a page
            # whose weight is at the top. `widthIn` is honoured only when it asks for
            # LESS than that, so a spec can make it quieter and cannot make it louder.
            want = float(wm_spec.get("widthIn", WATERMARK_W_IN))
            add_watermark(s, wm_path, min(want, WATERMARK_W_IN),
                          vert_frac=WATERMARK_VERT_FRAC)
        else:
            print(f"build_notes_docx: watermarkImage \"{wm_spec['path']}\" not found at "
                  f"{wm_path} — building without it.", file=sys.stderr)

    # Brand bar. Outlined, not filled: SHULL_DESIGN_SYSTEM section 8 - "no full-page
    # colour banners, no shaded section backgrounds, no solid-fill headers." The first
    # build of this template ignored that and measured 3.2x the ink of Matthew's own
    # packet, which had no cell fills anywhere. A heavy accent rule carries the same
    # hierarchy for a rule's worth of toner.
    c = one_cell(doc); borders(c, display, sz=18, edges=("bottom",))
    para(c, "SHULL SCIENCE  ·  JAMES A. GARFIELD LOCAL SCHOOLS", 7.5,
         bold=True, color=accent, caps_track=True, first=True)
    para(c, unit_title(course, spec["unit"]).upper(), 15, bold=True, color=ink)
    para(c, spec["kicker"], 7.5, color=label, caps_track=True)

    c = one_cell(doc); borders(c, hair)
    para(c, spec["fields"], 9, color=label, first=True)

    if eqs:
        gap(doc, 4)
        equation_bar(doc, eqs, pal,
                     spec.get("equationLabel", "EQUATIONS YOU MAY USE"))

    gap(doc, 4)
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [3.75, 3.75])
    for i, (lab, items) in enumerate([("UNIT LEARNING TARGETS", spec["unitTargets"]),
                                      ("KEY TERMS", spec["keyTerms"])]):
        cell = t.rows[0].cells[i]; borders(cell, hair)
        para(cell, lab, 7.5, bold=True, color=accent, caps_track=True, first=True)
        for x in items:
            para(cell, "•  " + debullet(x), 9.5)

    gap(doc, 4)
    c = one_cell(doc); borders(c, display, sz=18, edges=("left",))
    para(c, "HOW THESE NOTES WORK", 7.5, bold=True, color=accent, caps_track=True, first=True)
    for x in spec["howItWorks"]:
        para(c, "•  " + debullet(x), 9.5)

    gap(doc, 2)
    c = one_cell(doc); borders(c, white)
    para(c, "SECTIONS IN THIS UNIT", 7.5, bold=True, color=accent, caps_track=True, first=True)
    for x in spec["sectionList"]:
        check_item(c, debullet(x), pal, 9.5)

    # SHULL-CHG-0018. Page 1 is now a dedicated, standalone title page (front matter
    # gets its own page_break below, before section 1 starts), so there is room for an
    # optional reference image right on the cover - his ask was a Bohr-model diagram
    # already relevant to the atomic-structure section. Path is resolved against the
    # SPEC FILE's own directory, not this script's, since that is where a build's local
    # assets live. Absent field or missing file: no change from prior behavior, and a
    # missing file is a clear stderr note rather than a crash - Geology/Physics specs
    # that never set this must keep building exactly as before.
    img_spec = spec.get("titleImage")
    if img_spec:
        img_path = os.path.join(spec_dir, img_spec["path"])
        if os.path.exists(img_path):
            # The plate is framed, and the caption lives inside the frame with it.
            # Dropped straight onto the page, a raster carrying its own cream ground
            # read as a foreign object pasted on white - nothing said where the
            # picture ended and the sheet began. A hairline rule and real padding
            # make the edge a decision. Outlined, not filled; the frame is the only
            # ink it costs.
            gap(doc, 14)
            img_w = float(img_spec.get("widthIn", 3.2))
            ft = doc.add_table(rows=1, cols=1)
            ft.alignment = WD_TABLE_ALIGNMENT.CENTER
            fix_widths(ft, [round(img_w + 0.44, 2)])
            fc = ft.rows[0].cells[0]
            borders(fc, hair, sz=W_BOX)
            cell_margins(fc, top=110, bottom=90, left=110, right=110)
            p = fc.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(0)
            p.add_run().add_picture(img_path, width=Inches(img_w))
            if img_spec.get("caption"):
                cap = fc.add_paragraph()
                cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                cap.paragraph_format.space_before = Pt(6)
                cap.paragraph_format.space_after = Pt(0)
                r = cap.add_run(img_spec["caption"])
                r.font.name = FONT; r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor.from_string(hexof(label))
        else:
            print(f"build_notes_docx: titleImage \"{img_spec['path']}\" not found at "
                  f"{img_path} — building without it.", file=sys.stderr)

    for sec in spec["sectionsContent"]:
        doc.add_page_break()
        # A section head sat 6pt off the top margin with the learning target pressed
        # straight underneath, so the loudest thing on the page had nothing around it
        # and read as jammed rather than as an opening. The air is the hierarchy here:
        # nothing else on the page gets this much room above it.
        gap(doc, 20)
        t = doc.add_table(rows=1, cols=2)
        fix_widths(t, [5.83, 1.67])
        a, b = t.rows[0].cells
        # Section head: ruled above and below, not filled.
        for cell in (a, b):
            borders(cell, ink, sz=W_HEAD_TOP, edges=("top",))
            borders(cell, display, sz=W_SECTION, edges=("bottom",))
            cell_margins(cell, top=90, bottom=90, left=0, right=0)
        para(a, sec["title"], 12.5, bold=True, color=ink, first=True)
        p = para(b, sec["code"], 8.5, bold=True, color=accent, caps_track=True, first=True)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

        gap(doc, 7)
        c = one_cell(doc); borders(c, hair, sz=W_BOX)
        cell_margins(c, top=45, bottom=45, left=40, right=40)
        p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(2)
        r = p.add_run("LEARNING TARGET   "); r.font.name = FONT; r.font.size = Pt(7.5)
        r.bold = True; r.font.color.rgb = RGBColor.from_string(hexof(accent))
        r2 = p.add_run(sec["learningTarget"]); r2.font.name = FONT; r2.font.size = Pt(9.5)

        t = doc.add_table(rows=len(sec["rows"]), cols=2)
        fix_widths(t, [CUE_W_IN, NOTES_W_IN])
        for ri, row in enumerate(sec["rows"]):
            cue, notes = t.rows[ri].cells
            # No fill on the cue column. Matthew's packet separated the columns with a
            # rule alone, which is the Cornell convention and costs nothing to print.
            # The weight ladder does the rest: the boundary between one row and the
            # next is heavier than the hairline dividing cue from notes, which is in
            # turn heavier than anything drawn inside a row.
            for cell in (cue, notes):
                borders(cell, hair, sz=W_ROW, edges=("top", "bottom"))
                borders(cell, hair, sz=W_INNER, edges=("left", "right"))
            # The rail. Last, so it replaces the hairline on that edge rather than
            # arguing with it.
            borders(cue, display, sz=W_RAIL, edges=("left",))
            cell_margins(cue, top=30, bottom=30, left=130, right=50)
            # A place for the eye to land, and a way to say "third block" without
            # counting. Accent-deep, because it is type on a light ground.
            n = para(cue, str(ri + 1), 13, bold=True, color=accent, first=True)
            n.paragraph_format.space_after = Pt(0)
            # Condensed: the cue label keeps caps and colour but loses its letter
            # tracking - tracking is what made "DISTANCE VS. DISPLACEMENT" wrap - and
            # the prompts drop half a point so a question fits on two lines, not four.
            lab = para(cue, row["cueLabel"], 7, bold=True, color=accent)
            lab.paragraph_format.space_after = Pt(4)
            for q in row["cues"]:
                para(cue, q, 8.5)
                # SHULL-CHG-0020. His ask: "give recall." The cue column already told
                # a student to "cover the right side and quiz yourself with it later" -
                # but gave nowhere to actually write the answer when they did, so
                # recall stayed a mental exercise instead of a real self-check. One
                # short line per cue turns it into one.
                rule_lines(cue, 1, hair)
            para(notes, row["notesLabel"], 7.5, bold=True, color=accent, caps_track=True, first=True)
            if row.get("diagram"):
                diagram_block(notes, row["diagram"], pal, NOTES_INNER_IN, HERE)
            if row.get("table"):
                fillin_table(notes, row["table"], pal, NOTES_INNER_IN)
                unpad_cell(notes)
            if row.get("matterFlowchart"):
                matter_flowchart(notes, pal, NOTES_INNER_IN,
                                  filled=bool(row["matterFlowchart"].get("filled")))
                unpad_cell(notes)

            prob = row.get("problem")
            if prob:
                para(notes, prob.get("label", "EXAMPLE"), 7.5, bold=True,
                     color=accent, caps_track=True)
                if prob.get("statement"):
                    para(notes, prob["statement"], 9.5)
                if prob.get("given") or prob.get("need"):
                    given_need(notes, prob.get("given", ""), prob.get("need", ""),
                               pal, NOTES_INNER_IN)
                work_box(notes, prob.get("workLabel", "WORK — SHOW EVERY STEP"), pal,
                         float(prob.get("workHeightIn", WORK_BOX_MIN_IN)), NOTES_INNER_IN)
                if prob.get("answer"):
                    para(notes, prob["answer"], 9.5)

            for n in row["notes"]:
                mw = n.startswith(("*", "✎"))
                body = n.lstrip("*✎").strip()
                if mw:
                    # A paragraph-level w:pBdr left border (the original approach) is
                    # valid OOXML and present in the saved file, but LibreOffice does
                    # not paint it inside a nested table cell - confirmed by inspecting
                    # the raw XML (border there, sz 18, colour correct) against the
                    # rendered PDF (no line at all). Every OTHER accent bar in this
                    # system (the masthead kicker, work_box's label) is a TABLE CELL
                    # border, which does render reliably - so the must-write line gets
                    # the same treatment: its own 1x1 table with a left cell border,
                    # not a paragraph border.
                    mwt = notes.add_table(rows=1, cols=1)
                    fix_widths(mwt, [NOTES_INNER_IN])
                    mwc = mwt.rows[0].cells[0]
                    borders(mwc, display, sz=18, edges=("left",))
                    cell_margins(mwc, top=20, bottom=20, left=120, right=0)
                    para(mwc, body, 9.5, bold=True, first=True)
                    # NOT unpad_cell(notes) here: that helper strips every empty
                    # paragraph before the FIRST table anywhere in the cell, not just
                    # the one this call just introduced - in a notes cell that already
                    # has earlier rule_lines() blank writing lines before this
                    # must-write table, it deleted those too. Harmless here: the one
                    # extra blank paragraph python-docx leaves before a freshly added
                    # table is a few points of space, not a rendering defect.
                else:
                    para(notes, body, 9.5, bold=False)
                    rule_lines(notes, 2 if body.rstrip().endswith("?") else 1, hair)

            # SHULL-CHG-0020. His ask: "add box to add anything from the slide,
            # 'Extra'." The structured prompts above cover what he planned to put on
            # the slide - this is the catch-all for whatever he adds live that isn't
            # one of them, kept with the row it belongs to rather than pooled once at
            # the end of the section, since that's what "from the slide" scopes it to.
            # It is an affordance, not a heading. Set in the accent at the same size
            # and tracking as "FOUR TERMS YOU'LL USE ALL UNIT" it made a catch-all box
            # look like teaching content, four and five times a page. Same words, same
            # place, quieter voice: smaller, grey, barely tracked, not bold.
            x = para(notes, "EXTRA — ANYTHING ELSE FROM THE SLIDE", 7,
                     color=label, caps_track=12)
            x.paragraph_format.space_before = Pt(3)
            rule_lines(notes, 2, hair)

        gap(doc, 2)
        c = one_cell(doc, protect=True); borders(c, accent)
        para(c, "SECTION SUMMARY — close your notes before you write this", 7.5,
             bold=True, color=accent, caps_track=True, first=True)
        para(c, sec["summaryPrompt"], 9.5)
        rule_lines(c, 4, hair)
        para(c, "SELF-CHECK", 7.5, bold=True, color=accent, caps_track=True)
        for x in sec.get("selfCheck", []):
            check_item(c, x, pal)

    gap(doc, 14)
    c = one_cell(doc); borders(c, ink, sz=W_HEAD_TOP, edges=("top",))
    borders(c, display, sz=W_SECTION, edges=("bottom",))
    cell_margins(c, top=60, bottom=60, left=0, right=0)
    # keepNext: the closing banner belongs to the checklist under it. Left to fall
    # where it liked it stranded at the foot of the last section's page, a heading
    # with its content on the next sheet.
    bp = para(c, spec["close"]["banner"], 9, bold=True, color=ink, caps_track=True,
              first=True)
    bp.paragraph_format.keep_with_next = True
    c = one_cell(doc, protect=True); borders(c, hair, sz=W_BOX)
    cell_margins(c, top=45, bottom=45, left=40, right=40)
    para(c, "SECTION CHECKLIST", 7.5, bold=True, color=accent, caps_track=True, first=True)
    for x in spec["close"]["checklist"]:
        check_item(c, x, pal)
    para(c, "UNIT BIG PICTURE", 7.5, bold=True, color=accent, caps_track=True)
    para(c, spec["close"]["bigPicture"], 9.5)
    rule_lines(c, 3, hair)
    para(c, spec["close"]["fuzzyLabel"], 8.5, bold=True, color=accent, caps_track=True)
    rule_lines(c, 3, hair)

    # SHULL-CHG-0018. A standing last page, every course: topic breakdown, key
    # points, confusing points, remember. Required-with-a-loud-warning rather than a
    # hard crash - Geology's and Physics's already-shipped specs don't have this
    # content yet and inventing it is not this builder's job - so a spec missing it
    # still builds, loudly, matching the noEquationBar soft-opt-out pattern.
    recap = spec.get("studyRecap")
    if recap:
        study_recap_page(doc, recap, pal)
    else:
        print("build_notes_docx: this course's notes should end with a Study Recap "
              "page — none provided, building without one; see SHULL-CHG-0018 "
              "discussion.", file=sys.stderr)

    running_footer(s, f"SHULL SCIENCE          {unit} · {span}", pal)

    trim_tail(doc)
    doc.save(out)
    print(f"wrote {out}  —  {code} {unit} {span}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
