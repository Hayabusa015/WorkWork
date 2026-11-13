"""Generate the Chemistry U3 guided-notes student and key specs (paged schema).

    python3 templates/notes/specs/make_chem_u03_notes.py

One source, so the key is the student structure with answers filled and the two cannot
drift. Edit this file, not the JSON it writes.

Follows Matt's own U3 deck, "SHULL Chemistry Unit 03 - Periodic Trends - With Melting and
Boiling" (2026-11-03), slide by slide and in its order: students record the important items on
each slide, not every word, and nothing that is not on the slides. Slides 10-15 of that deck are
click-to-enlarge reference views (periodic table, trend heat maps) and have no notes of their own.

Section codes from courses/chemistry/DECISIONS.md; 3.5 is retired (SHULL-CHG-0054) and unused.
Slide 2 (why trends change) and slides 8-9 (melting/boiling points, summary) both sit under 3.6
Explaining Periodic Trends, which keeps the deck's order; melting and boiling point has no section
of its own, and 3.6 is a mapping for Matt to confirm. Difficulty ratings are course content and
are left for Matt: none is invented here.

Strictly recall (templates/notes/recall.py): cues name what to record; the deck's example
questions become records of the example and its answer.

Condensed on Matt's instruction (2026-11-03): one block per slide, the example as the block's last
line, one inline ruled row per item, two content pages, no extra-notes lines, no recall
blocks, no concept review page.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "chem_u03_s03.3-s03.6_notes"


def P(prompt, answer, lines=None):          # one inline ruled row; `answer` is the key's
    d = {"prompt": prompt, "answer": answer, "inline": True}
    if lines:
        d["lines"] = lines
    return d


def block(title, cue, notes):
    """One slide = one block. The example is the last line of the block, not a block of its own,
    and there is no extra-notes line: Matt asked for a condensed packet (2026-11-03)."""
    return {"title": title, "cues": [cue], "noWorkBox": True, "extraNotes": False, "notes": notes}


spec = {
  "course": "chemistry",
  "unit": 3,
  "key": False,
  "cover": {
    "keyTerms": [
      {"code": "3.6", "terms": ["Period", "group", "shielding", "metallic character",
                                "melting point", "boiling point"]},
      {"code": "3.4", "terms": ["Ionization energy", "successive ionization energy",
                                "valence electron", "electronegativity"]},
      {"code": "3.3", "terms": ["Atomic radius", "picometer (pm)", "ion"]},
    ],
    "howToUse": ("Fill in each blank while its slide is up. Record the important items, not every word. "
                 "The last line of each block is the slide's example."),
  },
  "sectionsContent": [
    # Two content pages (Matt, 2026-11-03: condense). Each block's cue names its slide and
    # its own section code, since a page can carry only one code in its title bar.
    {
      "code": "3.4",
      "title": "Why Trends Change, Ionization Energy & Electronegativity",
      "learningTarget": "I can explain why trends change and describe the ionization energy and electronegativity trends.",
      "pages": [{"rows": [
        block("Why trends change", "Slide 2 · S3.6", [
          P("Period / group", "A period is a row. A group is a column."),
          P("Across a row", "More protons; outer electrons pulled inward."),
          P("Down a group", "Another energy level."),
          P("Shielding", "Inner electrons reduce the pull felt by outer electrons."),
          P("Example: Li vs. F; Li vs. Na", "Li 3 protons, F 9. Li 2 levels, Na 3."),
        ]),
        block("Ionization energy", "Slide 3 · S3.4", [
          P("Definition (units)", "Energy to remove an electron from a gas atom (kJ/mol)."),
          P("Trend", "Increases across a row → and up a column ↑."),
          P("Why", "More nuclear pull = harder. More distance and shielding = easier."),
          P("Example: Ca vs. Br, higher IE", "Br. Same period; 15 more protons."),
        ]),
        block("Successive ionization energy", "Slide 4 · S3.4", [
          P("A large jump shows", "An inner electron was removed."),
          P("Example: Al 578, 1,817, 2,745, 11,577 — valence electrons", "3 (jump at the 4th)"),
          P("Example: Mg 738, 1,451, 7,733, 10,543 — valence electrons", "2 (jump at the 3rd)"),
        ]),
        block("Electro-negativity", "Slide 5 · S3.4", [
          P("Definition (units)", "Pull on shared electrons in a bond (no units)."),
          P("Trend", "Increases across → and up ↑. F highest; noble gases excluded."),
          P("Why", "More nuclear pull attracts shared electrons; distance and shielding weaken it."),
          P("Example: rank S, O, F", "S < O < F"),
        ]),
      ]}],
    },
    {
      "code": "3.3",
      "title": "Atomic Radius, Ion Size, Melting & Boiling Points",
      "learningTarget": "I can describe the atomic radius trend, compare an ion to its atom, and summarize the periodic trends.",
      "pages": [{"rows": [
        block("Atomic radius", "Slide 6 · S3.3", [
          P("Definition (units)", "The size of an atom (pm)."),
          P("Trend", "Increases down a column ↓ and to the left across a row ←."),
          P("Why", "Down: another energy level. Across: more protons pull inward."),
          P("Example: Ca vs. Br, larger atom", "Ca. Same period; Br has more protons."),
        ]),
        block("Ion size", "Slide 7 · S3.3", [
          P("Magnesium ion vs. atom", "Ion is smaller: 12 → 10 electrons."),
          P("Why", "Outer level gone; still 12 protons."),
        ]),
        block("Melting and boiling points", "Slide 8 · S3.6", [
          P("Definitions (units)", "Melting: solid → liquid. Boiling: liquid → gas. °C."),
          P("Trend", "No single trend. Group 1: both fall. Group 17: both rise."),
          P("Why", "Stronger attractions need more energy to overcome."),
          P("Example: group 17, highest MP and BP", "Iodine, I₂ (113.7 °C, 184.4 °C)"),
        ]),
        block("Trend summary", "Slide 9 · S3.6", [
          P("Toward the top right", "Higher ionization energy and electronegativity"),
          P("Toward the bottom left", "Larger atomic radius, stronger metallic character"),
          P("Metallic character", "How easily an atom loses electrons; strong near Cs."),
        ]),
      ]}],
    },
  ],
}


def strip_answers(node):
    """Student copy: the same tree with every answer removed."""
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k in ("_key", "_answerKey", "solution"):
                continue
            if k == "answer" and ("prompt" in node and not isinstance(node.get("prompt"), dict)):
                continue
            out[k] = strip_answers(v)
        return out
    if isinstance(node, list):
        return [strip_answers(x) for x in node]
    return node


def fill_answers(node):
    """Key: the same tree with answers put in place."""
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k in ("_key", "_answerKey"):
                continue
            out[k] = fill_answers(v)
        if "_key" in node:
            out["rows"] = node["_key"]
        if "_answerKey" in node:
            out["answer"] = node["_answerKey"]
        return out
    if isinstance(node, list):
        return [fill_answers(x) for x in node]
    return node


student = strip_answers(spec)
key = fill_answers(spec)
key["key"] = True
for name, data in (("student", student), ("key", key)):
    with open(os.path.join(HERE, f"{STEM}_{name}.json"), "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
print("wrote", STEM + "_student.json and _key.json")
