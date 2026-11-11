#!/usr/bin/env python3
"""Build a multiple-choice question bank, and its separate key, from one spec.

    python3 templates/assessment/build_question_bank_docx.py <spec.json> [out.docx]
    python3 templates/assessment/build_question_bank_docx.py <spec.json> [out.docx] --key

One spec, two drawings. The bank prints every item with no answer marked, grouped by
section, two items to a row, each item held whole across a page break. The key prints the
answer letter, the learning target the item serves, why the answer is right and why each
wrong choice is wrong (build-assessment: "for a full teacher key, why each distractor is
wrong"), after a one-grid answer list for grading. The answer letter lives in the spec once; both files read it, so they cannot drift.

Spec: course, unit, sections (codes that must exist in the course DECISIONS.md), docType,
descriptor, title, directions, and `groups`, one per section:
    {"code": "2.1", "title": "...", "target": "...", "items": [
        {"stem": "...", "options": ["...", "...", "...", "..."], "answer": "B",
         "why": "...", "wrong": {"A": "...", "C": "...", "D": "..."}, "source": "..."}]}
Text may carry <b>, <i> and &nbsp; (rich() in _shull_docx).

The builder refuses an item without exactly four options, an answer letter outside A-D,
two identical options, a missing `why`, or a `wrong` note missing for any distractor. It
refuses "all of the above" and "none of the above" (build-assessment).
"""
import json, os, re, sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Inches

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _shull_name import document_name, short_title   # noqa: E402
from _shull_docx import (          # noqa: E402
    COURSE_CODE, Palette, known_sections, unit_title, borders, para, run, rich,
    fix_widths, no_split, page_setup, running_footer, cell_margins, gap, trim_tail,
)

TEXT_W_IN = 7.50
GUTTER_IN = 0.30
LETTERS = "ABCD"
BANNED = re.compile(r"\b(all|none) of the above\b", re.I)


def refuse(msg):
    print(f"build_question_bank_docx: REFUSED - {msg}", file=sys.stderr)
    return 2


def check(spec, course):
    bad = [s for s in spec["sections"] if s not in known_sections(course)]
    if bad:
        return f"section(s) {', '.join(bad)} are not in courses/{course}/DECISIONS.md."
    codes = [g["code"] for g in spec["groups"]]
    if codes != list(spec["sections"]):
        return f"groups {codes} but sections {spec['sections']}: one fact, two lists."
    for g in spec["groups"]:
        for n, it in enumerate(g["items"], 1):
            where = f"{g['code']} item {n}"
            opts = it.get("options", [])
            if len(opts) != 4:
                return f"{where}: {len(opts)} options; a bank item has exactly four."
            if len(set(o.strip().lower() for o in opts)) != 4:
                return f"{where}: two options are the same."
            if it.get("answer") not in LETTERS:
                return f"{where}: answer {it.get('answer')!r} is not A-D."
            if any(BANNED.search(o) for o in opts):
                return f"{where}: 'all/none of the above' is not allowed (build-assessment)."
            if not it.get("why"):
                return f"{where}: no `why`. A key that cannot say why is not a key."
            want = set(LETTERS) - {it["answer"]}
            if set(it.get("wrong", {})) != want:
                return f"{where}: `wrong` must explain exactly {sorted(want)}."
    return None


def header(doc, spec, pal, title, right_label):
    unit = f"U{int(spec['unit']):02d}"
    span = f"S{spec['sections'][0]}-S{spec['sections'][-1]}"
    t = doc.add_table(rows=1, cols=2)
    fix_widths(t, [5.55, 1.95])
    h, hr = t.rows[0].cells
    for cc in (h, hr):
        borders(cc, pal.hair, sz=4, edges=("top", "bottom"))
    borders(h, pal.display, sz=30, edges=("left",))
    cell_margins(h, top=80, bottom=80, left=160, right=80)
    cell_margins(hr, top=80, bottom=80, left=80, right=60)
    para(h, f"UNIT {int(spec['unit'])} — {unit_title(spec['course'], spec['unit']).upper()}",
         7.5, bold=True, color=pal.accent, caps_track=True, first=True)
    para(h, title, 15, bold=True, color=pal.ink)
    p = para(hr, f"{unit} / {span}", 11, bold=True, color=pal.accent, caps_track=True,
             first=True)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p = para(hr, right_label, 6.5, color=pal.label, caps_track=True)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    return unit, span


def group_heading(doc, g, pal, count):
    t = doc.add_table(rows=1, cols=1)
    fix_widths(t, [TEXT_W_IN])
    c = t.rows[0].cells[0]
    borders(c, pal.display, sz=18, edges=("bottom",))
    cell_margins(c, top=0, bottom=40, left=0, right=0)
    p = para(c, f"{g['code']}  ·  {g['title']}", 12, bold=True, color=pal.ink, first=True)
    run(p, f"   {count} items", 8, color=pal.label)
    return c


def item_cell(cell, n, it, pal):
    cell_margins(cell, top=40, bottom=80, left=0, right=0)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Inches(0.30)
    p.paragraph_format.first_line_indent = Inches(-0.30)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(0.30))
    run(p, f"{n}.\t", 10, bold=True, color=pal.ink)
    rich(p, it["stem"], 10, color=pal.ink)
    for L, opt in zip(LETTERS, it["options"]):
        q = cell.add_paragraph()
        q.paragraph_format.space_after = Pt(1.5)
        q.paragraph_format.left_indent = Inches(0.58)
        q.paragraph_format.first_line_indent = Inches(-0.28)
        q.paragraph_format.tab_stops.add_tab_stop(Inches(0.58))
        run(q, f"{L}\t", 9.5, bold=True, color=pal.accent)
        rich(q, opt, 9.5, color=pal.ink)


def bank(doc, spec, pal):
    col = (TEXT_W_IN - GUTTER_IN) / 2
    n = 0
    for gi, g in enumerate(spec["groups"]):
        gap(doc, 10 if gi else 6)
        group_heading(doc, g, pal, len(g["items"]))
        gap(doc, 4)
        items = g["items"]
        for k in range(0, len(items), 2):
            t = doc.add_table(rows=1, cols=3)
            fix_widths(t, [col, GUTTER_IN, col])
            no_split(t.rows[0])
            for j, ci in ((0, 0), (1, 2)):
                if k + j < len(items):
                    n += 1
                    item_cell(t.rows[0].cells[ci], n, items[k + j], pal)


def glance(doc, spec, pal, across=10):
    """Every answer letter on one grid, numbered as the bank numbers them: for grading."""
    flat = [(g["code"], it["answer"]) for g in spec["groups"] for it in g["items"]]
    gap(doc, 6)
    t = doc.add_table(rows=1, cols=1); fix_widths(t, [TEXT_W_IN])
    para(t.rows[0].cells[0], "ANSWERS AT A GLANCE", 7.5, bold=True, color=pal.accent,
         caps_track=True, first=True)
    w = TEXT_W_IN / across
    for r in range(0, len(flat), across):
        t = doc.add_table(rows=1, cols=across)
        fix_widths(t, [w] * across)
        for k, cell in enumerate(t.rows[0].cells):
            i = r + k
            if i >= len(flat):
                break
            borders(cell, pal.hair, sz=4, edges=("bottom",))
            cell_margins(cell, top=30, bottom=30, left=40, right=40)
            p = para(cell, f"{i + 1}.", 8.5, color=pal.label, first=True)
            run(p, f"  {flat[i][1]}", 10, bold=True, color=pal.accent)


def key(doc, spec, pal):
    glance(doc, spec, pal)
    n = 0
    ws = [0.36, 0.40, TEXT_W_IN - 0.76]
    for gi, g in enumerate(spec["groups"]):
        gap(doc, 10 if gi else 6)
        c = group_heading(doc, g, pal, len(g["items"]))
        para(c, "TARGET  " + g["target"], 8, color=pal.label)
        gap(doc, 2)
        for it in g["items"]:
            n += 1
            t = doc.add_table(rows=1, cols=3)
            fix_widths(t, ws)
            no_split(t.rows[0])
            a, b, d = t.rows[0].cells
            for x in (a, b, d):
                borders(x, pal.hair, sz=4, edges=("bottom",))
                cell_margins(x, top=40, bottom=40, left=40, right=40)
            para(a, f"{n}.", 9.5, bold=True, color=pal.ink, first=True)
            para(b, it["answer"], 11, bold=True, color=pal.accent, first=True)
            p = d.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            rich(p, it["stem"], 8.5, color=pal.label)
            p = d.add_paragraph(); p.paragraph_format.space_after = Pt(2)
            ans = it["options"][LETTERS.index(it["answer"])]
            run(p, f"{it['answer']}  ", 9, bold=True, color=pal.accent)
            rich(p, f"<b>{ans}</b>", 9, color=pal.ink)
            run(p, "  ", 9)
            rich(p, it["why"], 9, color=pal.ink)
            for L in LETTERS:
                if L == it["answer"]:
                    continue
                p = d.add_paragraph(); p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.left_indent = Inches(0.18)
                run(p, f"{L}  ", 8.5, bold=True, color=pal.label)
                rich(p, it["wrong"][L], 8.5, color=pal.ink)
            if it.get("source"):
                p = d.add_paragraph(); p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.left_indent = Inches(0.18)
                run(p, "Notes: " + it["source"], 7.5, italic=True, color=pal.label)


def main():
    args = [a for a in sys.argv[1:] if a != "--key"]
    is_key = "--key" in sys.argv[1:]
    if not args:
        return refuse("usage: build_question_bank_docx.py <spec.json> [out.docx] [--key]")
    spec = json.load(open(args[0]))
    course = spec["course"]
    if course not in COURSE_CODE:
        return refuse(f"unknown course {course!r}.")
    err = check(spec, course)
    if err:
        return refuse(err)
    pal = Palette(course)
    out = args[1] if len(args) > 1 else document_name(
        spec["docType"], spec["sections"], spec["unit"], key=is_key,
        unit_title=short_title(course, f"U{spec['unit']}"), descriptor=spec.get("descriptor"))

    doc = Document()
    s = page_setup(doc)
    total = sum(len(g["items"]) for g in spec["groups"])
    label = f"{total} ITEMS  ·  " + ("ANSWER KEY" if is_key else "MULTIPLE CHOICE")
    unit, span = header(doc, spec, pal, spec["title"] + (" · Teacher Key" if is_key else ""),
                        label)
    if not is_key and spec.get("directions"):
        gap(doc, 6)
        t = doc.add_table(rows=1, cols=1); fix_widths(t, [TEXT_W_IN])
        c = t.rows[0].cells[0]; borders(c, pal.ink, sz=8, edges=("top",))
        para(c, "DIRECTIONS", 7.5, bold=True, color=pal.accent, caps_track=True, first=True)
        para(c, spec["directions"], 9.5, color=pal.ink)
    (key if is_key else bank)(doc, spec, pal)
    running_footer(s, f"SHULL SCIENCE          {unit} · {span}" + (" · KEY" if is_key else ""),
                   pal, with_page_numbers=True)
    trim_tail(doc)
    doc.save(out)
    print(f"wrote {out}  —  {COURSE_CODE[course]} {unit} {span}"
          f"{' KEY' if is_key else ''}, {total} item(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
