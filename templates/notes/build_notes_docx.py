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
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Every primitive on this page - how a work box is drawn, how a fraction stacks, how a
# diagram block holds together across a page break - is shared with the worksheet
# builder. It lives in one file so the two cannot drift.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _shull_docx import (          # noqa: E402
    T, G, FONT, FLOOR, COURSE_CODE, Palette, hexof, debullet, known_sections,
    unit_title,
    borders, para, check_item, rule_lines, fix_widths, one_cell, no_split, gap,
    stacked_frac, equation_bar, work_box, given_need, diagram_block,
    page_setup, running_footer, trim_tail,
)

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))


# SHULL-CHG-0016. Matthew's physics packet puts a bordered box under every worked
# example - a 1x1 table, ~1in tall, hRule "atLeast" so it grows but never shrinks, and
# cantSplit so it never breaks across a page. Students work the problem inside it.
# His rule: "anytime problems need solved in guided notes leave a box for them to do it."
WORK_BOX_MIN_IN = 1.4          # his was 0.98in; a little more room for kinematics
GIVEN_LABEL_IN = 0.72

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


# SHULL-CHG-0017. A fraction is stacked - numerator over denominator with a horizontal
# bar. Never "a/b" inline in the text. Built as a two-row table rather than Office Math
# (OMML): OMML is valid and Word renders it, but LibreOffice will not import it from

def main():
    spec = json.load(open(sys.argv[1] if len(sys.argv) > 1
                          else os.path.join(HERE, "specs", "geo_u01_s01.2-s01.4.json")))
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

    for sec in spec["sectionsContent"]:
        gap(doc, 6)
        t = doc.add_table(rows=1, cols=2)
        fix_widths(t, [5.83, 1.67])
        a, b = t.rows[0].cells
        # Section head: ruled above and below, not filled.
        for cell in (a, b):
            borders(cell, ink, sz=12, edges=("top",))
            borders(cell, display, sz=18, edges=("bottom",))
        para(a, sec["title"], 12.5, bold=True, color=ink, first=True)
        p = para(b, sec["code"], 8.5, bold=True, color=accent, caps_track=True, first=True)
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

        c = one_cell(doc); borders(c, hair)
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
            borders(cue, hair); borders(notes, hair)
            # Condensed: the cue label keeps caps and colour but loses its letter
            # tracking - tracking is what made "DISTANCE VS. DISPLACEMENT" wrap - and
            # the prompts drop half a point so a question fits on two lines, not four.
            para(cue, row["cueLabel"], 7, bold=True, color=accent, first=True)
            for q in row["cues"]:
                para(cue, q, 8.5)
            para(notes, row["notesLabel"], 7.5, bold=True, color=accent, caps_track=True, first=True)
            if row.get("diagram"):
                diagram_block(notes, row["diagram"], pal, NOTES_INNER_IN, HERE)

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
                p = para(notes, body, 9.5, bold=mw)
                if mw:
                    pPr = p._p.get_or_add_pPr()
                    bd = OxmlElement("w:pBdr"); x = OxmlElement("w:left")
                    x.set(qn("w:val"), "single"); x.set(qn("w:sz"), "18")
                    x.set(qn("w:space"), "6"); x.set(qn("w:color"), hexof(display))
                    bd.append(x); pPr.append(bd)
                else:
                    rule_lines(notes, 2 if body.rstrip().endswith("?") else 1, hair)

        gap(doc, 2)
        c = one_cell(doc); borders(c, accent)
        para(c, "SECTION SUMMARY — close your notes before you write this", 7.5,
             bold=True, color=accent, caps_track=True, first=True)
        para(c, sec["summaryPrompt"], 9.5)
        rule_lines(c, 4, hair)
        para(c, "SELF-CHECK", 7.5, bold=True, color=accent, caps_track=True)
        for x in sec.get("selfCheck", []):
            check_item(c, x, pal)

    gap(doc, 6)
    c = one_cell(doc); borders(c, ink, sz=12, edges=("top",))
    borders(c, display, sz=18, edges=("bottom",))
    para(c, spec["close"]["banner"], 9, bold=True, color=ink, caps_track=True, first=True)
    c = one_cell(doc); borders(c, hair)
    para(c, "SECTION CHECKLIST", 7.5, bold=True, color=accent, caps_track=True, first=True)
    for x in spec["close"]["checklist"]:
        check_item(c, x, pal)
    para(c, "UNIT BIG PICTURE", 7.5, bold=True, color=accent, caps_track=True)
    para(c, spec["close"]["bigPicture"], 9.5)
    rule_lines(c, 3, hair)
    para(c, spec["close"]["fuzzyLabel"], 8.5, bold=True, color=accent, caps_track=True)
    rule_lines(c, 3, hair)

    running_footer(s, f"SHULL SCIENCE          {unit} · {span}", pal)

    trim_tail(doc)
    doc.save(out)
    print(f"wrote {out}  —  {code} {unit} {span}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
