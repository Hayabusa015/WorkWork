#!/usr/bin/env python3
"""Build a SHULL quiz in parallel versions, plus a separate key for each version.

    python3 templates/activity/build_quiz.py specs/chem_u03_quiz.json OUTDIR

The spec carries every version in full rather than a template that gets shuffled at build
time: build-assessment requires each version to be re-solved on its own, and a solution that
exists only after a shuffle cannot have been. The builder refuses versions whose point totals
or blueprints differ.
"""
import json, os, sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.shared import Inches

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from _shull_docx import (   # noqa: E402
    Palette, known_sections, borders, para, run, no_split, page_setup, running_footer,
    cell_margins, gap, one_cell, rule_lines,
)
from _shull_name import document_name   # noqa: E402
sys.path.insert(0, HERE)
from _print_parts import header, fields, label   # noqa: E402


def refuse(msg):
    print("build_quiz: " + msg, file=sys.stderr)
    sys.exit(1)


def question(doc, pal, n, q, key=False):
    c = one_cell(doc)
    no_split(doc.tables[-1].rows[0])
    borders(c, pal.hair, sz=4, edges=("bottom",))
    cell_margins(c, top=60, bottom=90, left=0, right=0)
    p = para(c, "", 10, first=True)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(7.45), WD_TAB_ALIGNMENT.RIGHT)
    # Just the number. No box, no circle. SHULL-CHG-0015.
    run(p, f"{n}.  ", 10.5, bold=True, color=pal.ink)
    run(p, q["prompt"], 10, color=pal.ink)
    run(p, "\t", 10)
    pts = f"{q['points']} pt" + ("s" if q["points"] != 1 else "")
    run(p, f"S{q.get('sectionLabel', q['section'])}  ·  {pts}", 7, bold=True, color=pal.label)
    for part in q.get("parts", []):
        para(c, part, 10, color=pal.ink)
        if not key:
            rule_lines(c, 1, pal.hair)
    if key:
        p = para(c, "", 10)
        run(p, "ANSWER  ", 7.5, bold=True, color=pal.accent)
        run(p, q["answer"], 10, bold=True, color=pal.accent)
        for ln in q["solution"].split("\n"):
            para(c, ln, 9.5, color=pal.ink)
    elif q.get("lines"):
        rule_lines(c, int(q["lines"]), pal.hair)
    gap(doc, 6)


def build(spec, pal, version, qs, key, out):
    doc = Document()
    sec = page_setup(doc)
    code = f"U{int(spec['unit']):02d} / S{spec['sections'][0]}–S{spec['sections'][-1]}"
    running_footer(sec, f"SHULL SCIENCE   {code}   QUIZ {version}" + ("   KEY" if key else ""), pal)
    title = f"Unit {int(spec['unit'])} Quiz" + (" — Answer Key" if key else "")
    kind = f"VERSION {version}" + ("  ·  ANSWER KEY" if key else f"  ·  ~{spec['timeTargetMin']} MIN")
    header(doc, spec, pal, title, kind, code)
    gap(doc, 5)
    total = sum(q["points"] for q in qs)
    fields(doc, pal, [("NAME", 3.6), ("DATE", 1.4), ("PERIOD", 1.0), (f"SCORE         / {total}", 1.5)])
    gap(doc, 8)
    if not key:
        p = para(doc, "Answer every question. For an explanation, name the trend, compare the atoms, and give "
                      "the cause. Write charges after the symbol, number first: Mg2+, O2−.", 9.5, color=pal.ink)
        gap(doc, 6)
    for n, q in enumerate(qs, 1):
        question(doc, pal, n, q, key)
    doc.save(out)


def main():
    if len(sys.argv) < 3:
        refuse("usage: build_quiz.py <spec.json> <outdir>")
    spec = json.load(open(sys.argv[1]))
    bad = [s for s in spec["sections"] if s not in known_sections(spec["course"])]
    if bad:
        refuse(f"section(s) {bad} not in courses/{spec['course']}/DECISIONS.md. Stop and ask.")
    vs = spec["versions"]
    blueprints = {v: sorted((q["item"], q["section"], q["points"]) for q in qs) for v, qs in vs.items()}
    if len({json.dumps(b) for b in blueprints.values()}) != 1:
        refuse(f"versions do not share one blueprint: {blueprints}")
    for v, qs in vs.items():
        for q in qs:
            if q["section"] not in spec["sections"]:
                refuse(f"version {v}: question on S{q['section']}, not in the spec's sections")
            if not q.get("solution") or not q.get("answer"):
                refuse(f"version {v}: a question has no answer or solution; the key would skip it")
    pal = Palette(spec["course"])
    for v, qs in vs.items():
        for key in (False, True):
            name = document_name(spec["docType"], spec["sections"], spec["unit"], version=v, key=key)
            build(spec, pal, v, qs, key, os.path.join(sys.argv[2], name))
            print("wrote", os.path.join(sys.argv[2], name))


if __name__ == "__main__":
    main()
