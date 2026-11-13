#!/usr/bin/env python3
"""Build the CHEM U03 Periodic Trends Gizmo sheet (S3.3 atomic radius, S3.4 ionization energy)
and its separate key.

    python3 templates/activity/build_trends_gizmo.py OUTDIR

Rewritten 2026-11-03 from Matt's own Gizmo worksheet, on his instruction to make it plain and to
the point: collect data in a table, then answer short questions the data answers, then pull the
trends together in one summary table. Each question is one idea in one sentence.

Gizmo readings (ruler radii, pull distances) vary with how carefully a student measures, so the
key gives the counts that are fixed (protons, energy levels), reference ionization energies, and
the trend that is graded - not invented Gizmo numbers.
"""
import os, sys
from docx import Document
from docx.shared import Pt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from _shull_docx import (   # noqa: E402
    Palette, known_sections, para, run, page_setup, running_footer, gap, one_cell, borders,
    cell_margins, rule_lines, fillin_table, no_split,
)
from _shull_name import document_name   # noqa: E402
sys.path.insert(0, HERE)
from _print_parts import TEXT_W, header, fields, page_break, boxed, label   # noqa: E402

COURSE, UNIT, SECTIONS = "chemistry", 3, ["3.3", "3.4"]
CODE = "U03 / S3.3–S3.4"

GROUP1 = ["H", "Li", "Na", "K", "Rb", "Cs"]
PERIOD3 = ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]
LEVELS = {"H": "1", "Li": "2", "Na": "3", "K": "4", "Rb": "5", "Cs": "6",
          "Mg": "3", "Al": "3", "Si": "3", "P": "3", "S": "3", "Cl": "3", "Ar": "3"}
PROTONS = {"Na": "11", "Mg": "12", "Al": "13", "Si": "14", "P": "15", "S": "16", "Cl": "17", "Ar": "18"}
IE = {"H": "1312", "Li": "520", "Na": "496", "K": "419", "Rb": "403", "Cs": "376",
      "Mg": "738", "Al": "578", "Si": "787", "P": "1012", "S": "1000", "Cl": "1251", "Ar": "1521"}
GIZMO = "Gizmo"     # key cell: the student's own reading


def table(doc, pal, title, headers, rows, widths):
    c = one_cell(doc)
    borders(c, pal.hair, sz=4)
    cell_margins(c, top=60, bottom=70, left=110, right=110)
    label(c, title, pal, first=True)
    fillin_table(c, {"headers": headers, "rows": rows, "widths": widths, "rowHeightIn": 0.25},
                 pal, TEXT_W - 0.3, header_caps=True)
    gap(doc, 5)


def questions(doc, pal, start, qs, key):
    """qs: (prompt, answer, lines). Ruled lines for a written answer; none when the blank is in the
    sentence. The key prints the answer instead."""
    c = one_cell(doc)
    borders(c, pal.hair, sz=4)
    cell_margins(c, top=50, bottom=60, left=110, right=110)
    for i, (prompt, answer, lines) in enumerate(qs):
        p = para(c, "", 10, first=(i == 0))
        run(p, f"{start + i}.  ", 10, bold=True, color=pal.ink)
        run(p, prompt, 10, color=pal.ink)
        if key:
            para(c, answer, 10, bold=True, color=pal.accent)
        elif lines:
            rule_lines(c, lines, pal.hair)
        else:
            para(c, "", 4)      # the blank in the sentence is the answer space
    gap(doc, 6)
    return start + len(qs)


def build(out, key):
    pal = Palette(COURSE)
    doc = Document()
    sec = page_setup(doc)
    running_footer(sec, f"SHULL SCIENCE   {CODE}   ACTIVITY{'   KEY' if key else ''}", pal, with_page_numbers=True)
    spec = {"course": COURSE, "unit": UNIT}
    header(doc, spec, pal, "Periodic Trends Gizmo" + (" — Key" if key else ""),
           "ACTIVITY  ·  ANSWER KEY" if key else "ACTIVITY  ·  ~40 MIN", CODE)
    gap(doc, 5)
    fields(doc, pal, [("NAME", 4.2), ("DATE", 1.8), ("PERIOD", 1.5)])
    gap(doc, 6)
    if key:
        boxed(doc, pal, "ABOUT THIS KEY", [
            "Radius and distance values are the student's own Gizmo readings and will vary. Grade the "
            "trend, not the number. Energy levels and protons are fixed. Ionization energies are "
            "reference values (kJ/mol); the Gizmo's should be close."])
        gap(doc, 6)

    # ---------------- Part 1: atomic radius
    boxed(doc, pal, "PART 1 · ATOMIC RADIUS", [
        "Choose Atomic radius from the menu. Atomic radius is the size of the atom: the distance from "
        "the nucleus to the outer electrons."])
    gap(doc, 5)
    g = lambda e: GIZMO if key else ""
    table(doc, pal, "DOWN GROUP 1 — use the ruler, count the rings",
          ["ELEMENT", "ENERGY LEVELS", "ATOMIC RADIUS (pm)"],
          [[e, LEVELS[e] if key else "", g(e)] for e in GROUP1], [0.3, 0.35, 0.35])
    n = questions(doc, pal, 1, [
        ("Going down group 1, the atomic radius __________ .", "increases", 0),
        ("What goes up by one each time you move down the group?",
         "the number of energy levels (one more ring of electrons)", 1),
    ], key)
    table(doc, pal, "ACROSS PERIOD 3",
          ["ELEMENT", "PROTONS", "ENERGY LEVELS", "ATOMIC RADIUS (pm)"],
          [[e, PROTONS[e] if key else "", LEVELS[e] if key else "", g(e)] for e in PERIOD3],
          [0.22, 0.24, 0.24, 0.30])
    n = questions(doc, pal, n, [
        ("Going across period 3, the atomic radius __________ .", "decreases", 0),
        ("Across the period, the number of energy levels __________ and the number of protons __________ .",
         "stays the same (3); increases (11 to 18)", 0),
        ("Why does adding protons make the atom smaller when the energy levels stay the same?",
         "More protons pull harder on the same energy levels, so the electrons are held closer to the nucleus.", 2),
    ], key)

    # ---------------- Part 2: ionization energy
    page_break(doc)
    boxed(doc, pal, "PART 2 · IONIZATION ENERGY", [
        "Choose Ionization energy. It is the energy needed to remove one electron. Drag the atom toward "
        "the + charge until the electron comes off, then record the distance and the ionization energy."])
    gap(doc, 5)
    ie = lambda e: IE[e] if key else ""
    table(doc, pal, "DOWN GROUP 1",
          ["ELEMENT", "DISTANCE PULLED", "IONIZATION ENERGY (kJ/mol)"],
          [[e, g(e), ie(e)] for e in GROUP1], [0.3, 0.3, 0.4])
    n = questions(doc, pal, n, [
        ("Going down group 1, the ionization energy __________ .", "decreases", 0),
        ("Why is the outer electron of a large atom easier to remove?",
         "It is farther from the nucleus (more energy levels), so the nucleus holds it less tightly.", 2),
    ], key)
    table(doc, pal, "ACROSS PERIOD 3",
          ["ELEMENT", "DISTANCE PULLED", "IONIZATION ENERGY (kJ/mol)"],
          [[e, g(e), ie(e)] for e in PERIOD3], [0.3, 0.3, 0.4])
    n = questions(doc, pal, n, [
        ("Going across period 3, the ionization energy __________ .",
         "increases (overall; Al and S dip slightly below the element before them)", 0),
        ("Metals lose electrons easily. Which group is the most metallic: the one with the highest or the "
         "lowest ionization energy? Name the group.", "lowest ionization energy: group 1, the alkali metals", 1),
    ], key)

    # ---------------- Conclusion
    c = one_cell(doc)
    borders(c, pal.hair, sz=4)
    cell_margins(c, top=60, bottom=70, left=110, right=110)
    label(c, "PULL IT TOGETHER — WRITE INCREASES OR DECREASES, THEN THE REASON", pal, first=True)
    rows = [
        ["Atomic radius", "decreases", "increases",
         "more protons across; more energy levels down"],
        ["Ionization energy", "increases", "decreases",
         "radius: a smaller atom holds its electrons tighter"],
        ["Metallic character", "decreases", "increases",
         "the opposite of ionization energy"],
    ]
    if not key:
        rows = [[r[0], "", "", ""] for r in rows]
    fillin_table(c, {"headers": ["TREND", "ACROSS A PERIOD →", "DOWN A GROUP ↓", "WHY"],
                     "rows": rows, "widths": [0.2, 0.17, 0.17, 0.46], "rowHeightIn": 0.38},
                 pal, TEXT_W - 0.3, header_caps=True)
    doc.save(out)
    print("wrote", out)


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else HERE
    bad = [s for s in SECTIONS if s not in known_sections(COURSE)]
    if bad:
        sys.exit(f"build_trends_gizmo: {bad} not in courses/{COURSE}/DECISIONS.md")
    for key in (False, True):
        build(os.path.join(outdir, document_name("Activity", SECTIONS, UNIT, key=key,
                                                 descriptor="Trends Gizmo")), key)


if __name__ == "__main__":
    main()
