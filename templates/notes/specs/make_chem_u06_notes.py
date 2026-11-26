"""Generate the Chemistry U6 Chemical Nomenclature guided-notes student and key specs.

    python3 templates/notes/specs/make_chem_u06_notes.py

Then build (Option A, the production path):

    python3 templates/notes/build_notes_docx.py templates/notes/specs/chem_u06_notes_student.json \
        "OUT/Unit 6 Guided Notes.docx" --verify
    python3 templates/notes/build_notes_docx.py templates/notes/specs/chem_u06_notes_key.json \
        "OUT/Unit 6 Guided Notes Key.docx" --verify

Source: Matt's deck "SHULL_Chemistry_Chemical_Nomenclature.pptx" (37 slides, uploaded 2026-11-20;
Drive copy 15bOPjF9SqSH95Ro3EcmJiN5yyQfuUB6I). Three deck sections: molecular (slides 4-12), ionic
(13-29), acids (30-37). Section codes from courses/chemistry/DECISIONS.md (SHULL-CHG-0099).

Matt's rules for this packet (2026-11-20/21):
  1. No fill-in-the-blank. A short prompt names what goes there; the student writes it
     (brand/SHULL_DESIGN_SYSTEM.md §11, SHULL-CHG-0069).
  2. Room to write: "the space to write is to small, i need you to increase it a bit, its ok to
     add more pages". Multi-line prompts get ruled lines below them, not one inline row.
  3. The deck's IN YOUR NOTES lines are prompts the student completes, not printed sentences.
  4. Follow the slides, in order; every block names its slides.

The deck teaches polyatomic ions (6.2) inside its ionic section: slide 14 and slides 27-29 sit
among the 6.3 slides. Blocks keep deck order (one slide is never split), so the 6.2 section's
pages carry both codes and each block's cue names its own code, as the U4-U5 packet does.

Edit this file, not the JSON it writes.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "chem_u06_notes"


def P(label, answer, lines=None):
    """A prompt. No `lines`: one inline ruled row. With `lines`: the label, then that many ruled
    lines under it. The key prints `answer` in place of the writing space."""
    d = {"prompt": label, "answer": answer}
    if lines:
        d["lines"] = lines
    else:
        d["inline"] = True
    return d


def T(headers, rows, key_rows, widths, height=0.36):
    """A fill-in table; the student copy has `rows`, the key `key_rows`."""
    return {"headers": headers, "rows": rows, "_key": key_rows, "widths": widths, "rowHeightIn": height}


def notes(title, cues, rows, table=None, table_first=False):
    d = {"title": title, "cues": cues, "noWorkBox": True, "extraNotes": False, "notes": rows}
    if not table_first:
        d["notesFirst"] = True
    if table:
        d["table"] = table
    return d


def example(title, cues, rows, box_label, height, solution, table=None):
    d = {"kind": "example", "title": title, "cues": cues, "extraNotes": False, "notesFirst": True,
         "notes": rows, "problem": {"workLabel": box_label, "workHeightIn": height, "solution": solution}}
    if table:
        d["table"] = table
    return d


spec = {
  "course": "chemistry",
  "unit": 6,
  "key": False,
  "noEquationBar": True,
  "cover": {
    "kicker": "GUIDED NOTES  ·  PHASE 02  ·  4 SECTIONS",
    "sectionList": ["S06.1   Covalent Names & Formulas", "S06.2   Polyatomic Ions",
                    "S06.3   Ionic Names & Formulas with Transition Metals",
                    "S06.4   Naming Acids & Formulas"],
    "keyTerms": [
      {"code": "6.1", "terms": ["Molecular compound", "prefix", "subscript"]},
      {"code": "6.2", "terms": ["Polyatomic ion", "ammonium", "parentheses"]},
      {"code": "6.3", "terms": ["Cation", "anion", "net charge", "criss-cross", "Roman numeral"]},
      {"code": "6.4", "terms": ["Binary acid", "oxyacid", "(aq)", "-ic / -ous"]},
    ],
    "howToUse": ("Each block names its slides. When a slide is up, write what its prompts ask for "
                 "in your own words on the lines. Copy each worked example into its box."),
  },
  "sectionsContent": [
    # ======================================================== slides 2-12 · 6.1
    {"code": "6.1", "title": "Covalent Names & Formulas",
     "learningTarget": "I can classify a compound as ionic or covalent and name and write formulas for molecular compounds.",
     "pages": [
       {"rows": [
         notes("Slides 2–3 · Names and formulas", ["S06"], [
           P("Always do this first", "Identify the compound type before choosing a naming rule.", 2),
           P("Order of checks", "Check for an acid first. Then look for ions or two nonmetals.", 2),
         ], table=T(["", "Molecular · CO₂", "Ionic · CaCl₂", "Acid · HCl(aq)"],
                    [["How to spot it", "", "", ""], ["Naming rule", "", "", ""]],
                    [["How to spot it", "Two nonmetals", "Cation + anion", "H compound in water (aq)"],
                     ["Naming rule", "Prefixes count atoms", "Balance + and − charge", "Name from the anion"]],
                    [0.22, 0.26, 0.26, 0.26], 0.40)),
         notes("Slides 5–6 · Naming molecular compounds", ["S06.1"], [
           P("Rule 1 · first element", "Keep its name. Prefix only for 2+ atoms (no mono-).", 2),
           P("Rule 2 · second element", "Use a prefix; change the ending to -ide.", 1),
           P("Rule 3 · formula", "Keep the actual atom counts.", 1),
           P("Meaning of a subscript", "Atoms of the element just before it.", 1),
         ]),
         notes("Slide 7 · Molecular prefixes", ["S06.1"], [
           P("Slide examples", "CO = carbon monoxide · CO₂ = carbon dioxide", 1),
           P("Prefixes and subscripts", "Prefixes become subscripts in the formula.", 1),
         ], table=T(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                    [["", "", "", "", "", "", "", "", "", ""]],
                    [["mono-", "di-", "tri-", "tetra-", "penta-", "hexa-", "hepta-", "octa-", "nona-", "deca-"]],
                    [0.1] * 10, 0.46), table_first=True),
       ]},
       {"rows": [
         example("Slides 8–9 · How do you name N₂O₄?", ["S06.1"], [
           P("Prefix rule", "Skip mono- on the first element; prefix the second.", 2),
           P("No subscript means", "One atom. Use mono- only on the second element.", 1),
         ], "Slides 8–9 · Name N₂O₄: the prefix for each element. Then name CO and PCl₃.", 1.5,
            ["N₂ → di- + nitrogen = dinitrogen", "O₄ → tetra- + oxide = tetroxide → dinitrogen tetroxide",
             "CO = carbon monoxide · PCl₃ = phosphorus trichloride"]),
         example("Slides 10–11 · Writing molecular formulas", ["S06.1"], [
           P("From name to formula", "Prefixes count actual atoms; keep those counts.", 1),
           P("Steps", "Write the symbols in order; each prefix gives a subscript.", 2),
         ], "Slides 10–11 · Write the formulas: dinitrogen pentoxide, sulfur hexafluoride", 1.4,
            ["di- = 2, penta- = 5 → N₂O₅", "sulfur = 1, hexa- = 6 → SF₆"]),
         notes("Slide 12 · Why N₂O₄ stays N₂O₄", ["S06.1"], [
           P("Conclusion", "N₂O₄ and NO₂ are different molecules: never reduce a molecular formula.", 2),
         ], table=T(["Formula", "Name", "Atoms in one molecule"],
                    [["N₂O₄", "", ""], ["NO₂", "", ""]],
                    [["N₂O₄", "dinitrogen tetroxide", "2 N, 4 O"], ["NO₂", "nitrogen dioxide", "1 N, 2 O"]],
                    [0.2, 0.42, 0.38], 0.42), table_first=True),
       ]},
     ]},
    # ======================================================== slides 14-29 · 6.2 and 6.3
    {"code": "6.2", "title": "Polyatomic Ions · Ionic Names & Formulas",
     "learningTarget": "I can explain what a polyatomic ion is, balance ion charges to write ionic formulas, and name ionic compounds, including transition metals.",
     "pages": [
       {"rows": [
         notes("Slide 14 · How can a group of atoms be an ion?", ["S06.2"], [
           P("Definition", "A group of bonded atoms with an overall charge.", 1),
           P("Formation of NH₄⁺ from NH₃ + H⁺", "H⁺ is attracted to N's lone pair; N shares it: new N–H bond.", 2),
           P("Reason for the +1 charge", "11 protons, 10 electrons.", 1),
           P("Bonds and charge", "Atoms share electrons (covalent); charge belongs to the whole group.", 2),
         ]),
         notes("Slides 15–16 · Naming ionic compounds", ["S06.3"], [
           P("Step 1 · cation", "Cation first (usually a metal). Variable charge → Roman numeral.", 2),
           P("Step 2 · anion", "One-element anion → -ide. Polyatomic ion keeps its name.", 2),
           P("Step 3 · writing a formula", "Criss-cross, reduce, check for zero net charge.", 1),
           P("Ion written first", "The positive ion, usually a metal.", 1),
         ], table=T(["Group 1", "Group 2", "Aluminum", "Group 17", "Group 16", "Group 15"],
                    [["", "", "", "", "", ""]], [["+1", "+2", "+3", "−1", "−2", "−3"]],
                    [1 / 6] * 6, 0.42)),
       ]},
       {"rows": [
         example("Slides 17–19 · The criss-cross method", ["S06.3"], [
           P("Charge rule", "Total positive charge + total negative charge = 0.", 1),
           P("After crossing", "Reduce if needed; check the charges add to zero.", 1),
         ], "Slides 17–19 · MgCl₂ and Al₂O₃: write the ions, cross the numbers, check the charge", 1.6,
            ["Mg²⁺ + 2 Cl⁻: (+2) + 2(−1) = 0 → MgCl₂", "Al³⁺, O²⁻ → Al₂O₃: 2(+3) + 3(−2) = 0"]),
         example("Slides 20–21 · The simplest ionic ratio", ["S06.3"], [
           P("Reducing rule", "Reduce the ratio of ions; omit subscripts of 1.", 1),
           P("Equal and opposite charges give", "A 1 : 1 ratio.", 1),
         ], "Slides 20–21 · Reduce Ca₂O₂. Write strontium sulfide.", 1.4,
            ["Ca₂O₂: 2 : 2 ÷ 2 → CaO", "Sr²⁺, S²⁻: cross 2 : 2 → reduce 1 : 1 → SrS"]),
         notes("Slides 22–23 · Naming ions with fixed charges", ["S06.3"], [
           P("Break down NaCl", "Na⁺ = sodium (cation name); Cl⁻ = chloride (root + -ide).", 2),
           P("Naming rule", "Cation, then anion. No counting prefixes.", 1),
           P("One-element anions", "Take the -ide ending.", 1),
         ], table=T(["Formula", "Name"], [["MgBr₂", ""], ["Al₂S₃", ""]],
                    [["MgBr₂", "magnesium bromide"], ["Al₂S₃", "aluminum sulfide"]], [0.3, 0.7], 0.40)),
       ]},
       {"rows": [
         example("Slides 24–26 · Metals with variable charges", ["S06.3"], [
           P("Iron’s two ions · fixed-charge metals", "Fe²⁺ = iron(II), Fe³⁺ = iron(III) · Ag⁺, Zn²⁺, Cd²⁺ (no numeral)", 2),
           P("The Roman numeral gives", "The charge on one metal ion.", 1),
           P("Finding the metal charge", "Anion total charge ÷ number of metal ions", 1),
         ], "Slides 25–26 · Name FeCl₂ and FeCl₃. Write copper(II) oxide.", 1.4,
            ["2 Cl⁻ = −2 → Fe²⁺ → iron(II) chloride", "3 Cl⁻ = −3 → Fe³⁺ → iron(III) chloride",
             "Cu²⁺ + O²⁻ → cross 2 : 2 → reduce → CuO"]),
         notes("Slide 27 · Recognizing common polyatomic ions", ["S06.2"], [
           P("Keep the group intact", "Keep the ion name and its inside subscripts.", 1),
           P("Ammonium", "NH₄⁺ is a cation even though it has no metal.", 1),
         ], table=T(["NO₃⁻", "NH₄⁺", "OH⁻", "SO₄²⁻"], [["", "", "", ""]],
                    [["nitrate", "ammonium", "hydroxide", "sulfate"]], [0.25] * 4, 0.32), table_first=True),
         example("Slides 28–29 · Parentheses count whole ions", ["S06.2"], [
           P("Meaning of Ca(NO₃)₂", "1 Ca²⁺ + 2 NO₃⁻ → 1 Ca, 2 N, 6 O atoms.", 1),
           P("Parentheses rule", "Use ( ) around a polyatomic ion when you need more than one.", 2),
           P("Inside vs. outside subscripts", "Outside counts whole ions; inside never changes.", 1),
         ], "Slides 28–29 · Write calcium nitrate and ammonium sulfate. Check the charge.", 1.4,
            ["Ca²⁺ + 2 NO₃⁻ → Ca(NO₃)₂: (+2) + 2(−1) = 0", "2 NH₄⁺ + SO₄²⁻ → (NH₄)₂SO₄: 2(+1) + (−2) = 0"]),
       ]},
     ]},
    # ======================================================== slides 31-37 · 6.4
    {"code": "6.4", "title": "Naming Acids & Formulas",
     "learningTarget": "I can recognize an acid, name binary acids and oxyacids, and write an acid’s formula from its name.",
     "pages": [
       {"rows": [
         notes("Slides 31–32 · Naming acids", ["S06.4"], [
           P("Binary acid pattern", "hydro- + nonmetal root + -ic acid", 1),
           P("Oxyacid patterns", "-ate → -ic acid; -ite → -ous acid; no hydro-.", 2),
           P("HCl(g) vs. HCl(aq)", "Hydrogen chloride (gas) vs. hydrochloric acid (in water).", 2),
           P("(aq) means", "Dissolved in water.", 1),
         ]),
         notes("Slide 33 · Naming binary acids and oxyacids", ["S06.4"], [
           P("Summary rule", "Binary: hydro-. Oxyacid: -ate → -ic, -ite → -ous. Keep per-/hypo-.", 2),
         ], table=T(["No oxygen · binary acid", "Contains oxygen · oxyacid"], [["", ""]],
                    [["hydro- + root + -ic acid. HCl(aq) → hydrochloric acid. Roots: chlor-, brom-, sulfur-",
                      "-ate → -ic: nitrate → nitric, sulfate → sulfuric. -ite → -ous: nitrite → nitrous, sulfite → sulfurous."]],
                    [0.5, 0.5], 1.5), table_first=True),
       ]},
       {"rows": [
         example("Slides 34–36 · Acid formulas", ["S06.4"], [
           P("H⁺ needed for NO₃⁻, SO₄²⁻, PO₄³⁻", "1 → HNO₃ · 2 → H₂SO₄ · 3 → H₃PO₄", 1),
           P("Hydrogen rule", "Each H⁺ balances one negative charge.", 2),
           P("Working backward from a name", "-ous → -ite; -ic → -ate.", 2),
         ], "Slides 34–36 · Name HBr(aq) and HNO₂(aq). Write hydrosulfuric acid and sulfuric acid.", 1.6,
            ["HBr(aq) = hydrobromic acid · HNO₂(aq) = nitrous acid",
             "hydrosulfuric acid = H₂S(aq) · sulfuric acid = H₂SO₄(aq)"]),
         notes("Slide 37 · Choosing the naming rules", ["S06"], [
           P("Clue 1 · acid in water", "Check whether the anion contains oxygen.", 2),
           P("Clue 2 · ionic compound", "Name the cation first; use charges for the formula.", 2),
           P("Clue 3 · two nonmetals", "Use prefixes to count atoms.", 1),
           P("The big three", "Prefixes count atoms. Charges balance. Acid names follow the anion.", 2),
         ]),
       ]},
     ]},
  ],
}


def strip_answers(node):
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k in ("_key", "solution"):
                continue
            if k == "answer" and "prompt" in node:
                continue
            out[k] = strip_answers(v)
        return out
    if isinstance(node, list):
        return [strip_answers(x) for x in node]
    return node


def fill_answers(node):
    if isinstance(node, dict):
        out = {k: fill_answers(v) for k, v in node.items() if k != "_key"}
        if "_key" in node:
            out["rows"] = node["_key"]
        return out
    if isinstance(node, list):
        return [fill_answers(x) for x in node]
    return node


SUPMAP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻", "0123456789+−")


def sup(node):
    """Every typed superscript run (Fe²⁺, NO₃⁻) becomes ^{...} markup, set as a superscript run by
    the builders; Archivo has no U+207A/U+207B glyphs."""
    import re
    if isinstance(node, str):
        return re.sub(r"[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+", lambda m: "^{" + m.group(0).translate(SUPMAP) + "}", node)
    if isinstance(node, dict):
        return {k: sup(v) for k, v in node.items()}
    if isinstance(node, list):
        return [sup(x) for x in node]
    return node


spec = sup(spec)
student = strip_answers(spec)
key = fill_answers(spec)
key["key"] = True
for name, data in (("student", student), ("key", key)):
    with open(os.path.join(HERE, f"{STEM}_{name}.json"), "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
print("wrote", STEM + "_student.json and _key.json")
