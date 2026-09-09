#!/usr/bin/env python3
"""Build a guided/Cornell notes packet as .docx from the same JSON spec. Option A.

Identical structure and content to build_notes.py - the difference is the output.
A .docx can be edited in Word and typed into by a student; it cannot hold the
layout as exactly as the PDF, because Word reflows.

    python3 templates/notes/build_notes_docx.py specs/<spec>.json out.docx

Colour comes from brand/tokens.json. No hex is typed in this file.
"""
import json, os, re, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
COURSE_CODE = {"chemistry": "CHEM", "physics": "PHYS", "geology": "GEO"}

T = json.load(open(os.path.join(REPO, "brand", "tokens.json")))
G = T["ground"]
FONT = T["typography"]["stack"].split(",")[0].strip().strip('"')
FLOOR = T["typography"]["floors"]["printBody"]["pt"]


BULLETS = "•·▸►‣-–— "


def debullet(x):
    """The source packets wrote their own bullets into the text; we supply one."""
    return str(x).lstrip(BULLETS).strip()


def hexof(h):
    return h.lstrip("#").upper()


def known_sections(course):
    text = open(os.path.join(REPO, "courses", course, "DECISIONS.md")).read()
    end = text.find("## Course sequencing rules")
    return set(re.findall(r"(?<![\d.])\d{1,2}\.\d(?![\d])", text[:end] if end > 0 else text))


def shade(cell, hexval):
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear"); el.set(qn("w:fill"), hexof(hexval))
    cell._tc.get_or_add_tcPr().append(el)


def borders(cell, hexval, sz=6, edges=("top", "left", "bottom", "right")):
    tcPr = cell._tc.get_or_add_tcPr()
    b = OxmlElement("w:tcBorders")
    for e in edges:
        x = OxmlElement(f"w:{e}")
        x.set(qn("w:val"), "single"); x.set(qn("w:sz"), str(sz))
        x.set(qn("w:color"), hexof(hexval))
        b.append(x)
    tcPr.append(b)


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
        el = OxmlElement("w:spacing"); el.set(qn("w:val"), "26")
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
    sets. The Cornell 1.88/5.62 split is the whole point of this layout, so it is
    pinned: autofit off, a fixed layout, and the width written on every cell."""
    table.autofit = False
    tblPr = table._tbl.tblPr
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    for row in table.rows:
        for cell, w in zip(row.cells, widths):
            cell.width = Inches(w)
    for col, w in zip(table.columns, widths):
        col.width = Inches(w)


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
# .docx, so nothing in this pipeline could see what shipped. A ruled table renders
# identically in Word, LibreOffice, Google Docs and print, and can be checked.
def tight_cells(t, top=0, bottom=0, left=40, right=40):
    for row in t.rows:
        for c in row.cells:
            mar = OxmlElement("w:tcMar")
            for edge, v in (("top", top), ("bottom", bottom), ("left", left), ("right", right)):
                e = OxmlElement(f"w:{edge}")
                e.set(qn("w:w"), str(v)); e.set(qn("w:type"), "dxa")
                mar.append(e)
            c._tc.get_or_add_tcPr().append(mar)


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


def equation_bar(doc, equations, accent, ink, hair, label):
    """The equations students may reference, at the top of the page.

    His rule: on any Physics or Chemistry sheet with math, the equations go at the top
    so students know what they are allowed to reach for. Two across, outlined not
    filled, fractions stacked.
    """
    # No box around the equations. Label, then the equations. The only rules on this
    # block are the fraction bars themselves, which are the point.
    c = one_cell(doc)
    para(c, label, 7.5, bold=True, color=accent, caps_track=True, first=True)
    cols = 2
    rows = (len(equations) + cols - 1) // cols
    t = c.add_table(rows=rows, cols=cols)
    fix_widths(t, [3.62, 3.62])
    tight_cells(t, top=30, bottom=40, left=0, right=60)
    for i, eq in enumerate(equations):
        cell = t.rows[i // cols].cells[i % cols]
        if eq.get("note"):
            p = para(cell, eq["note"], 7.5, bold=True, color=accent, caps_track=True, first=True)
            p.paragraph_format.space_after = Pt(1)
        if eq.get("num") and eq.get("den"):
            # lhs and the fraction side by side. A nested table always starts its own
            # line, so the equals sign needs its own cell to sit beside the bar.
            inner = cell.add_table(rows=1, cols=2)
            fix_widths(inner, [0.80, 2.60])
            tight_cells(inner, left=0, right=0)
            lc, fc = inner.rows[0].cells
            # Middle-aligned so the equals sign lands on the fraction bar, not above it.
            lc.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            para(lc, (eq.get("lhs", "") + "  =") if eq.get("lhs") else "", 10.5,
                 bold=True, first=True).alignment = WD_ALIGN_PARAGRAPH.RIGHT
            stacked_frac(fc, eq["num"], eq["den"], ink, hair)
            unpad_cell(cell)
        else:
            para(cell, eq.get("plain", ""), 10.5, bold=True, first=not eq.get("note"))
    return c


def diagram_block(cell, dgm, accent, ink, hair):
    """A figure students label. Geology's equivalent of a work box.

    His example: the layers of the Earth, or a plate boundary with the trench and the
    mid-ocean ridge to identify. The figure gets real room and the label lines are
    numbered beside it, so a student writes on the sheet rather than in a margin.
    """
    # The heading and caption live INSIDE the non-splitting row. Kept outside it, they
    # stranded on the previous page while the figure moved to the next - which is worse
    # than no heading at all, because the student sees a box with no instruction.
    # ONE row. cantSplit holds a row together but does nothing across two rows, so the
    # heading stranded on the previous page while the figure moved to the next - a box
    # with no instruction above it, which is worse than no heading at all.
    c = cell
    t = c.add_table(rows=1, cols=2)
    fix_widths(t, [NOTES_INNER_IN * 0.61, NOTES_INNER_IN * 0.39])
    fig, labels = t.rows[0].cells
    para(fig, dgm.get("label", "LABEL THIS DIAGRAM"), 7.5, bold=True, color=accent,
         caps_track=True, first=True)
    if dgm.get("caption"):
        para(fig, dgm["caption"], 9)
    borders(fig, hair, sz=4)
    trPr = t.rows[0]._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:cantSplit"))
    hh = OxmlElement("w:trHeight")
    hh.set(qn("w:val"), str(int(float(dgm.get("heightIn", 3.0)) * 1440)))
    hh.set(qn("w:hRule"), "atLeast")
    trPr.append(hh)
    img = dgm.get("image")
    if img and os.path.exists(os.path.join(HERE, img)):
        r = fig.add_paragraph().add_run()
        r.add_picture(os.path.join(HERE, img), width=Inches(NOTES_INNER_IN * 0.61 - 0.20))
        fig.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        # NOT first=True. The heading already claimed paragraph 0, and passing it twice
        # appends a run to the same paragraph instead of making a new one - the heading
        # and the figure note ran together as one line.
        p = para(fig, dgm.get("figureNote", "[ FIGURE ]"), 9,
                 color=hair, caps_track=True)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(10)
    para(labels, "LABEL", 7.5, bold=True, color=accent, caps_track=True, first=True)
    for i in range(int(dgm.get("labelSlots", 6))):
        p = para(labels, f"{i + 1}", 9.5, bold=True, color=ink)
        rule_lines(labels, 1, hair)
    return c


def work_box(cell, label, hexval, accent, height_in=WORK_BOX_MIN_IN, width=NOTES_INNER_IN):
    t = cell.add_table(rows=1, cols=1)
    fix_widths(t, [width])
    tr = t.rows[0]
    trPr = tr._tr.get_or_add_trPr()
    cant = OxmlElement("w:cantSplit"); trPr.append(cant)
    h = OxmlElement("w:trHeight")
    h.set(qn("w:val"), str(int(height_in * 1440)))
    h.set(qn("w:hRule"), "atLeast")
    trPr.append(h)
    inner = tr.cells[0]
    borders(inner, hexval, sz=6)
    # The label is read; the border is not. hairline on white measures 1.6:1.
    para(inner, label, 7.5, bold=True, color=accent, caps_track=True, first=True)
    return inner


def given_need(cell, given, need, hexval, accent):
    t = cell.add_table(rows=2, cols=2)
    fix_widths(t, [GIVEN_LABEL_IN, NOTES_INNER_IN - GIVEN_LABEL_IN])
    for ri, (lab, val) in enumerate((("GIVEN", given), ("NEED", need))):
        a, b = t.rows[ri].cells
        borders(a, hexval, sz=4); borders(b, hexval, sz=4)
        para(a, lab, 7.5, bold=True, color=accent, caps_track=True, first=True)
        para(b, val, 9.5, first=True)


def one_cell(doc, width=7.5):
    t = doc.add_table(rows=1, cols=1); t.alignment = WD_TABLE_ALIGNMENT.LEFT
    fix_widths(t, [width])
    return t.rows[0].cells[0]


def main():
    spec = json.load(open(sys.argv[1] if len(sys.argv) > 1
                          else os.path.join(HERE, "specs", "geo_u01_s01.2-s01.4.json")))
    course = spec["course"]
    accent = T["courses"][course]["primaryDeep"]["hex"]        # text-safe on white
    display = T["courses"][course]["primary"]["hex"]           # fills and rules only
    ink, hair, surface = G["asphalt"]["hex"], G["ruleHairline"]["hex"], G["parchment"]["hex"]
    label, footer, white = G["label"]["hex"], G["footer"]["hex"], G["white"]["hex"]

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
    st = doc.styles["Normal"]; st.font.name = FONT; st.font.size = Pt(10)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    s = doc.sections[0]
    s.page_width, s.page_height = Inches(8.5), Inches(11)
    s.left_margin = s.right_margin = Inches(0.5)
    s.top_margin = s.bottom_margin = Inches(0.44)

    # Brand bar. Outlined, not filled: SHULL_DESIGN_SYSTEM section 8 - "no full-page
    # colour banners, no shaded section backgrounds, no solid-fill headers." The first
    # build of this template ignored that and measured 3.2x the ink of Matthew's own
    # packet, which had no cell fills anywhere. A heavy accent rule carries the same
    # hierarchy for a rule's worth of toner.
    c = one_cell(doc); borders(c, display, sz=18, edges=("bottom",))
    para(c, "SHULL SCIENCE  ·  JAMES A. GARFIELD LOCAL SCHOOLS", 7.5,
         bold=True, color=accent, caps_track=True, first=True)
    para(c, spec["unitTitle"].upper(), 15, bold=True, color=ink)
    para(c, spec["kicker"], 7.5, color=label, caps_track=True)

    c = one_cell(doc); borders(c, hair)
    para(c, spec["fields"], 9, color=label, first=True)

    if eqs:
        doc.add_paragraph().paragraph_format.space_after = Pt(4)
        equation_bar(doc, eqs, accent, ink, hair,
                     spec.get("equationLabel", "EQUATIONS YOU MAY USE"))

    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [3.75, 3.75])
    for i, (lab, items) in enumerate([("UNIT LEARNING TARGETS", spec["unitTargets"]),
                                      ("KEY TERMS", spec["keyTerms"])]):
        cell = t.rows[0].cells[i]; borders(cell, hair)
        para(cell, lab, 7.5, bold=True, color=accent, caps_track=True, first=True)
        for x in items:
            para(cell, "•  " + debullet(x), 9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    c = one_cell(doc); borders(c, display, sz=18, edges=("left",))
    para(c, "HOW THESE NOTES WORK", 7.5, bold=True, color=accent, caps_track=True, first=True)
    for x in spec["howItWorks"]:
        para(c, "•  " + debullet(x), 9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    c = one_cell(doc); borders(c, white)
    para(c, "SECTIONS IN THIS UNIT", 7.5, bold=True, color=accent, caps_track=True, first=True)
    for x in spec["sectionList"]:
        para(c, "☐  " + debullet(x), 9.5)

    for sec in spec["sectionsContent"]:
        doc.add_paragraph().paragraph_format.space_after = Pt(6)
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
                diagram_block(notes, row["diagram"], accent, ink, hair)

            prob = row.get("problem")
            if prob:
                para(notes, prob.get("label", "EXAMPLE"), 7.5, bold=True,
                     color=accent, caps_track=True)
                if prob.get("statement"):
                    para(notes, prob["statement"], 9.5)
                if prob.get("given") or prob.get("need"):
                    given_need(notes, prob.get("given", ""), prob.get("need", ""), hair, accent)
                work_box(notes, prob.get("workLabel", "WORK — SHOW EVERY STEP"), hair, accent,
                         float(prob.get("workHeightIn", WORK_BOX_MIN_IN)))
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

        doc.add_paragraph().paragraph_format.space_after = Pt(2)
        c = one_cell(doc); borders(c, accent)
        para(c, "SECTION SUMMARY — close your notes before you write this", 7.5,
             bold=True, color=accent, caps_track=True, first=True)
        para(c, sec["summaryPrompt"], 9.5)
        rule_lines(c, 4, hair)
        para(c, "SELF-CHECK", 7.5, bold=True, color=accent, caps_track=True)
        for x in sec.get("selfCheck", []):
            para(c, "☐  " + x, 9)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    c = one_cell(doc); borders(c, ink, sz=12, edges=("top",))
    borders(c, display, sz=18, edges=("bottom",))
    para(c, spec["close"]["banner"], 9, bold=True, color=ink, caps_track=True, first=True)
    c = one_cell(doc); borders(c, hair)
    para(c, "SECTION CHECKLIST", 7.5, bold=True, color=accent, caps_track=True, first=True)
    for x in spec["close"]["checklist"]:
        para(c, "☐  " + x, 9)
    para(c, "UNIT BIG PICTURE", 7.5, bold=True, color=accent, caps_track=True)
    para(c, spec["close"]["bigPicture"], 9.5)
    rule_lines(c, 3, hair)
    para(c, spec["close"]["fuzzyLabel"], 8.5, bold=True, color=accent, caps_track=True)
    rule_lines(c, 3, hair)

    f = s.footer.paragraphs[0]
    f.text = f"SHULL SCIENCE          {unit} · {span}"
    for r in f.runs:
        r.font.name = FONT; r.font.size = Pt(7)
        r.font.color.rgb = RGBColor.from_string(hexof(footer))

    doc.save(out)
    print(f"wrote {out}  —  {code} {unit} {span}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
