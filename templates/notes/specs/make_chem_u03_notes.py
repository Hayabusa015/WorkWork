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
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "chem_u03_s03.3-s03.6_notes"


def P(prompt, answer, lines=None):          # a prompt with a writing line; `answer` is the key's
    d = {"prompt": prompt, "answer": answer}
    if lines:
        d["lines"] = lines
    return d


RECALL_CUES = ["Close your notes before you write.",
               "Use the checklist to find what still needs practice."]

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
                 "Gray side rules mark must-write notes."),
  },
  "sectionsContent": [
    # ---------------------------------------------------------------- slide 2
    {
      "code": "3.6",
      "title": "Why Periodic Trends Change",
      "learningTarget": "I can explain periodic trends using protons, energy levels, and shielding.",
      "pages": [
        {"rows": [
          {"title": "Across a row",
           "cues": ["Slide 2: period and group", "The change across a row", "Example: Li and F"],
           "notes": [P("Period and group", "A period is a row. A group is a column."),
                     P("Across a row, atoms gain more", "protons"),
                     P("Effect on the outer electrons", "They are usually pulled inward."),
                     P("Protons: Li and F", "Li: 3 protons   F: 9 protons")]},
          {"title": "Down a group",
           "cues": ["The change down a group", "Example: Li and Na"],
           "notes": [P("Down a column, atoms gain another", "energy level"),
                     P("Energy levels: Li and Na", "Li: 2 levels   Na: 3 levels"),
                     P("DEFINE: shielding", "Inner electrons reduce the pull felt by outer electrons.", lines=2)]},
          {"kind": "recall", "title": "Section summary", "cues": RECALL_CUES, "lines": 3,
           "prompt": "Explain what changes across a row and what changes down a group, and how each one affects the outer electrons.",
           "answer": "Across a row, atoms gain protons, so the outer electrons are pulled inward more. Down a group, atoms gain energy levels, and inner electrons shield the outer ones from the nucleus.",
           "selfCheck": ["I can tell a period from a group.",
                         "I can explain what changes across a row and down a group.",
                         "I can define shielding."]},
        ]},
      ],
    },
    # ---------------------------------------------------------------- slides 3-5
    {
      "code": "3.4",
      "title": "Ionization Energy & Electronegativity",
      "learningTarget": "I can describe and explain the trends in ionization energy and electronegativity.",
      "pages": [
        {"rows": [
          {"title": "Ionization energy",
           "cues": ["Slide 3: definition, units, trend, reason"],
           "notes": [P("DEFINE: ionization energy", "Energy needed to remove an electron from a gas atom.", lines=2),
                     P("Units", "kJ/mol"),
                     P("Trend", "Generally increases across a row → and up a column ↑."),
                     P("Why (both parts)", "More nuclear pull = harder to remove. More distance and shielding = easier.", lines=2)]},
          {"title": "Ca vs. Br",
           "cues": ["Slide 3 example: higher ionization energy"],
           "noWorkBox": True,
           "notes": [P("Higher ionization energy", "Br"),
                     P("Reason", "Same row (period 4). Br has 15 more protons pulling on electrons in the same main energy level.", lines=2)]},
          {"title": "Successive ionization energy",
           "cues": ["Slide 4: removing electrons one at a time", "Record both elements"],
           "notes": [P("A large jump shows", "an inner electron was removed")],
           "table": {"headers": ["Element", "1st", "2nd", "3rd", "4th", "Valence electrons"],
                     "widths": [0.22, 0.14, 0.14, 0.14, 0.14, 0.22], "rowHeightIn": 0.36,
                     "rows": [["Aluminum", "", "", "", "", ""],
                              ["Magnesium", "", "", "", "", ""]],
                     "_key": [["Aluminum", "578", "1,817", "2,745", "11,577", "3"],
                              ["Magnesium", "738", "1,451", "7,733", "10,543", "2"]]}},
        ]},
        {"rows": [
          {"title": "Electronegativity", "cueLabel": "ELECTRO-NEGATIVITY",
           "cues": ["Slide 5: definition, units, trend, reason"],
           "notes": [P("DEFINE: electronegativity", "How strongly an atom pulls on shared electrons in a bond.", lines=2),
                     P("Units", "No units"),
                     P("Trend", "Generally increases across a row → and up a column ↑. Fluorine is highest."),
                     P("Why (both parts)", "More nuclear pull attracts shared electrons. More distance and shielding weaken it.", lines=2),
                     "*Noble gases are not included in this trend."]},
          {"title": "Rank S, O, F",
           "cues": ["Slide 5 example: lowest to highest"],
           "noWorkBox": True,
           "notes": [P("Order, lowest to highest", "S < O < F"),
                     P("Reason", "O is above S. F is right of O.")]},
          {"kind": "recall", "title": "Section summary", "cues": RECALL_CUES, "lines": 3,
           "prompt": "Describe the trends in ionization energy and electronegativity, and give the reason for both.",
           "answer": "Both generally increase across a row and up a column. More nuclear pull holds electrons tighter; more distance and shielding weaken the pull.",
           "selfCheck": ["I can define ionization energy and electronegativity.",
                         "I can find the valence electrons from a jump in successive ionization energies.",
                         "I can rank elements by ionization energy or electronegativity."]},
        ]},
      ],
    },
    # ---------------------------------------------------------------- slides 6-7
    {
      "code": "3.3",
      "title": "Atomic & Ionic Radius",
      "learningTarget": "I can describe and explain the atomic radius trend and compare an ion to its atom.",
      "pages": [
        {"rows": [
          {"title": "Atomic radius",
           "cues": ["Slide 6: definition, units, trend, reason"],
           "notes": [P("DEFINE: atomic radius", "The size of an atom."),
                     P("Units", "picometers (pm)"),
                     P("Trend", "Generally increases down a column ↓ and to the left across a row ←."),
                     P("Why (both parts)", "Down: another energy level adds size. Across: more protons pull electrons inward.", lines=2)]},
          {"title": "Ca vs. Br",
           "cues": ["Slide 6 example: the larger atom"],
           "noWorkBox": True,
           "notes": [P("Larger atom", "Ca"),
                     P("Reason", "Both are in period 4. Br has more protons pulling its electrons inward.", lines=2)]},
        ]},
        {"rows": [
          {"title": "Ion size: magnesium",
           "cues": ["Slide 7: magnesium loses its two outer electrons"],
           "table": {"headers": ["Particle", "Electrons", "Larger or smaller"],
                     "widths": [0.3, 0.3, 0.4], "rowHeightIn": 0.34,
                     "rows": [["Mg", "", ""], ["Mg^{2+}", "", ""]],
                     "_key": [["Mg", "12", "Larger"], ["Mg^{2+}", "10", "Smaller"]]},
           "notes": [P("Why the ion is smaller", "The outer level is gone. The nucleus still has 12 protons.", lines=2)]},
          {"kind": "recall", "title": "Section summary", "cues": RECALL_CUES, "lines": 3,
           "prompt": "Describe the atomic radius trend, give both reasons, and explain why the magnesium ion is smaller than the magnesium atom.",
           "answer": "Radius increases down a column (another energy level) and to the left across a row (fewer protons pulling inward). The magnesium ion lost its outer level, and the same 12 protons hold fewer electrons.",
           "selfCheck": ["I can define atomic radius and give its units.",
                         "I can compare the sizes of two atoms in the same period or group.",
                         "I can explain why a positive ion is smaller than its atom."]},
        ]},
      ],
    },
    # ---------------------------------------------------------------- slides 8-9
    {
      "code": "3.6",
      "title": "Melting & Boiling Points; Trend Summary",
      "learningTarget": "I can describe the melting and boiling point patterns in groups 1 and 17 and summarize the periodic trends.",
      "pages": [
        {"rows": [
          {"title": "Melting and boiling points",
           "cues": ["Slide 8: definitions, trend, reason"],
           "notes": [P("DEFINE: melting point", "solid → liquid"),
                     P("DEFINE: boiling point", "liquid → gas"),
                     P("Units used here", "°C"),
                     P("Trend", "No single trend across the whole table. Down group 1: both fall (Li → Cs). Down group 17: both rise (F → I).", lines=2),
                     P("Why", "Stronger attractions usually need more energy to overcome. Different bonds give different patterns.", lines=2)]},
        ]},
        {"rows": [
          {"title": "Group 17 data",
           "cues": ["Slide 8 example: the halogens"],
           "table": {"headers": ["Element", "Melt (°C)", "Boil (°C)"],
                     "widths": [0.34, 0.33, 0.33], "rowHeightIn": 0.32,
                     "rows": [["Cl₂", "", ""], ["Br₂", "", ""], ["I₂", "", ""]],
                     "_key": [["Cl₂", "−101.5", "−34.0"], ["Br₂", "−7.2", "58.8"], ["I₂", "113.7", "184.4"]]},
           "notes": [P("Highest melting and boiling point", "Iodine, I₂"),
                     P("Reason", "Larger halogen molecules attract each other more strongly.")]},
          {"title": "Trend summary",
           "cues": ["Slide 9: the two corners of the table"],
           "table": {"headers": ["Direction", "Trends"],
                     "widths": [0.3, 0.7], "rowHeightIn": 0.42,
                     "rows": [["Toward the top right", ""], ["Toward the bottom left", ""]],
                     "_key": [["Toward the top right", "Higher ionization energy, higher electronegativity"],
                              ["Toward the bottom left", "Larger atomic radius, stronger metallic character"]]},
           "notes": [P("DEFINE: metallic character", "How easily an atom loses electrons; strong near Cs."),
                     "*Use the arrows to label your Gizmo sheet. There are exceptions."]},
          {"kind": "recall", "title": "Section summary", "cues": RECALL_CUES, "lines": 3,
           "prompt": "Summarize which way each trend points, and explain why melting and boiling points have no single trend.",
           "answer": "Ionization energy and electronegativity rise toward the top right; atomic radius and metallic character rise toward the bottom left. Melting and boiling points depend on the attractions in each group: they fall down group 1 and rise down group 17.",
           "selfCheck": ["I can define melting point, boiling point, and metallic character.",
                         "I can describe the melting and boiling point patterns in groups 1 and 17.",
                         "I can state which corner of the table each trend points to."]},
        ]},
      ],
    },
  ],
  "conceptReview": {
    "title": "Concept Review",
    "subtitle": "Periodic trends, from the unit slides",
    "sections": [
      {"code": "3.6", "heading": "Why trends change",
       "paragraphs": [["**Across a row:** more protons pull the outer electrons inward.",
                       "**Down a group:** another energy level; inner electrons shield the outer ones."]],
       "watchOut": "Shielding comes from inner electrons, not from protons."},
      {"code": "3.4", "heading": "Ionization energy and electronegativity",
       "paragraphs": [["**Ionization energy:** energy to remove an electron (kJ/mol). **Electronegativity:** pull on shared electrons (no units).",
                       "Both generally increase across a row and up a column. A large jump in successive ionization energies marks the first inner electron."]],
       "watchOut": "Noble gases are left out of the electronegativity trend."},
      {"code": "3.3", "heading": "Atomic and ionic radius",
       "paragraphs": [["**Atomic radius:** the size of an atom, in pm. Increases down a column and to the left across a row.",
                       "**The magnesium ion is smaller than the atom:** its outer level is gone, and the same 12 protons hold fewer electrons."]],
       "watchOut": "Radius runs opposite to ionization energy and electronegativity."},
      {"code": "3.6", "heading": "Melting and boiling points",
       "paragraphs": [["No single trend across the table. Down group 1 both fall; down group 17 both rise.",
                       "**Toward the top right:** higher IE and EN. **Toward the bottom left:** larger radius, stronger metallic character."]],
       "watchOut": "Melting and boiling points are temperatures (°C), not energies."},
    ],
    "quickRecall": ["Which has the higher ionization energy, Ca or Br, and why?",
                    "Why does aluminum's 4th ionization energy jump?",
                    "Why is the magnesium ion smaller than the magnesium atom?"],
  },
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
