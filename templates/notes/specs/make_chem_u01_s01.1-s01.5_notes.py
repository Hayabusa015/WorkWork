"""Generate the Chemistry U1 guided-notes student and key specs (paged schema).

    python3 templates/notes/specs/make_chem_u01_s01.1-s01.5_notes.py

One source, so the key is the student structure with answers filled and the two cannot
drift. Edit this file, not the JSON it writes.

Written from the deck, slide by slide (SHULL-CHG-0054): "Unit 1 - Matter and Atomic
Theory Notes.pptx", 22 slides, in Drive under Unit 01 / Presentations. Every block's
title is its slide's headline, word for word; `slides` names the slide(s); blocks follow
slide order; and a fill-in is the slide's own sentence with its key words blanked.
The must-write lines are the slide's lime blocks. Rebuilt 2026-10-23.
"""
import copy, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "chem_u01_s01.1-s01.5_notes"

def F(sentence):
    """A slide sentence with its key words in {braces}. The student copy gets a blank
    sized to the word; the key gets the finished sentence."""
    blank = lambda m: "_" * max(6, len(m.group(1)) + 3)
    return {"prompt": re.sub(r"\{([^}]*)\}", blank, sentence),
            "answer": re.sub(r"\{([^}]*)\}", r"\1", sentence),
            "lines": 0, "fill": True}

def prob(given, find, answer_blank, answer_key, solution):
    return {"given": given, "find": find, "answer": answer_blank,
            "_answerKey": answer_key, "solution": solution}

PARTICLES = "Protons = _____   Neutrons = _____   Electrons = _____"
FIND_PNE = "protons, neutrons, electrons."
FIND_AAM = "average atomic mass in amu, to two decimals."
RECALL_CUES = ["Close your notes before you write.",
               "Use the checklist to find what still needs practice."]

spec = {
  "course": "chemistry",
  "unit": 1,
  "key": False,
  "deck": "Unit 1 - Matter and Atomic Theory Notes.pptx",
  "cover": {
    "image": {"path": "../assets/chem_u01_cover_atom.png", "widthIn": 1.95},
    "sections": [
      {"code": "1.1", "difficulty": 1,
       "blurb": "Classify elements, compounds, and mixtures; distinguish homogeneous from heterogeneous mixtures."},
      {"code": "1.3", "difficulty": 2,
       "blurb": "Use atomic number, mass number, and charge to count protons, neutrons, and electrons."},
      {"code": "1.5", "difficulty": 3,
       "blurb": "Compare isotopes and calculate weighted averages from isotope masses and abundances written as decimals."}
    ],
    "difficultyNote": "Estimated for advanced high school students: 1 = introductory; 10 = highly challenging.",
    "equationToolbox": {
      "label": "Equation toolbox",
      "columns": [
        {"heading": "Particle counts",
         "lines": ["protons = Z", "neutrons = A − Z", "electrons = Z, adjusted for charge"]},
        {"heading": "Average atomic mass",
         "lines": ["(mass₁ × abundance₁) +", "(mass₂ × abundance₂) + …",
                   {"lhs": "abundance as a decimal", "num": "percent", "den": "100"}]}
      ],
      "notes": ["Z = atomic number; A = mass number.",
                "Neutral atom: charge = 0. A 2+ ion has two fewer electrons."]
    },
    "keyTerms": [
      {"code": "1.1", "terms": ["Matter", "pure substance", "mixture", "solution", "element",
                                "compound", "molecule", "homogeneous", "heterogeneous"]},
      {"code": "1.3", "terms": ["Proton", "neutron", "electron", "nucleus", "ion",
                                "atomic number (Z)", "mass number (A)"]},
      {"code": "1.5", "terms": ["Isotope", "abundance", "weighted average",
                                "average atomic mass"]}
    ],
    "howToUse": "Every block is titled with its slide's headline and names the slide it comes from. A lime block on the slide marked IN YOUR NOTES tells you which block to fill. Bold lines with a gray rule are those lime blocks: copy them word for word. Show your reasoning and units in each work box."
  },
  "sectionsContent": [
    {
      "code": "1.1",
      "title": "Matter & Changes",
      "learningTarget": "I can sort any sample of matter as an element, compound, or mixture, and homogeneous or heterogeneous if it is a mixture.",
      "pages": [
        {"rows": [
          {"title": "Four Terms You'll Use All Unit", "slides": 4,
           "cues": ["All four definitions, then examples."],
           "notes": [F("Matter: anything that has {mass} and takes up {space}."),
                     F("Pure substance: {one kind} of particle throughout. {Fixed} composition."),
                     F("Mixture: two or more substances {physically} combined. Composition {can vary}."),
                     F("Solution: a {homogeneous} mixture, evenly mixed, same throughout.")]},
          {"title": "The Matter Flowchart", "slides": 5,
           "cues": ["The full chart, every box.", "An example under each leaf."],
           "notesLabel": "COPY THE FLOWCHART",
           "flowchart": {"root": "MATTER", "branches": ["Pure substance", "Mixture"],
                         "leaves": ["Element", "Compound", "Homogeneous", "Heterogeneous"]},
           "notes": [F("Element: {Cu, O₂, He}    Compound: {H₂O, NaCl}"),
                     F("Homogeneous: {salt water, air}    Heterogeneous: {sand in water}"),
                     "*Ask two questions: can it be separated physically, and are the parts evenly mixed."]},
          {"title": "Element, Compound, Molecule", "slides": 6,
           "cues": ["Three definitions.", "The one students miss."],
           "notes": [F("Element: one kind of {atom} only. Cannot be broken down {chemically}."),
                     F("Compound: two or more {elements} bonded in a {fixed ratio}."),
                     F("Molecule: atoms {bonded together}, element or compound."),
                     "*O₂ is a molecule but not a compound. Compound needs two different elements."]}
         ]},
        {"rows": [
          {"title": "Evenly Mixed, or Not", "slides": 7,
           "cues": ["Homogeneous vs. heterogeneous.", "The scoop test."],
           "notes": [F("Homogeneous = {solution}. Same throughout. You {cannot} see the parts."),
                     F("Heterogeneous: parts stay {separate}. You {can} see them."),
                     "*If a scoop from the top matches a scoop from the bottom, it is homogeneous."]},
          {"title": "Run Six Samples Through the Chart", "slides": [8, 9],
           "cues": ["Separated physically first, then evenly mixed."],
           "noWorkBox": True,
           "table": {"headers": ["Sample", "Classification", "Why"],
                     "widths": [0.36, 0.27, 0.37], "rowHeightIn": 0.30,
                     "rows": [["Copper wire", "", ""], ["Salt water", "", ""],
                              ["Carbon dioxide", "", ""], ["Granite", "", ""],
                              ["Oxygen gas, O₂", "", ""], ["Stainless steel", "", ""]],
                     "_key": [["Copper wire", "Element", "One kind of atom, Cu"],
                              ["Salt water", "Solution", "Homogeneous mixture"],
                              ["Carbon dioxide", "Compound", "C and O bonded, CO₂"],
                              ["Granite", "Heterogeneous", "Grains you can see"],
                              ["Oxygen gas, O₂", "Element", "Molecule, one element"],
                              ["Stainless steel", "Solution", "Alloy, evenly mixed"]]},
           "notes": ["*O₂ is an element, not a compound. Steel is a solution too."]},
          {"kind": "recall", "title": "Section summary", "cues": RECALL_CUES, "lines": 3,
           "prompt": "Explain how to decide whether a new sample is an element, compound, or mixture — and whether a mixture is homogeneous or heterogeneous.",
           "answer": "If it can be separated physically, it’s a mixture: homogeneous if evenly mixed, heterogeneous if not. If not, it’s a pure substance: one kind of atom is an element; two or more bonded elements is a compound.",
           "selfCheck": ["I can define matter, pure substance, mixture, and solution.",
                         "I can classify a sample using the matter flowchart.",
                         "I can explain why O₂ is an element, not a compound."]}
         ]}
      ]
    },
    {
      "code": "1.3",
      "title": "Atomic Structure",
      "learningTarget": "I can find the protons, neutrons, and electrons in an atom or ion from its symbol, mass number, and atomic number.",
      "pages": [
        {"rows": [
          {"title": "Three Particles, Two Regions", "slides": 11,
           "cues": ["The particle table.", "The ID-number particle."],
           "table": {"headers": ["Particle", "Charge", "Mass (amu)", "Location"],
                     "widths": [0.23, 0.18, 0.25, 0.34], "rowHeightIn": 0.38,
                     "rows": [["Proton", "", "", ""], ["Neutron", "", "", ""],
                              ["Electron", "", "", ""]],
                     "_key": [["Proton", "+1", "1", "Nucleus"], ["Neutron", "0", "1", "Nucleus"],
                              ["Electron", "−1", "about 0", "Electron cloud"]]},
           "notes": ["*Protons are the ID number. Change the protons, change the element. Only electrons come and go."]},
          {"title": "Two Numbers Tell You Everything", "slides": 12,
           "cues": ["The three particle counts.", "Mass number A, atomic number Z."],
           "notes": [F("protons = {Z}   (straight off the periodic table)"),
                     F("neutrons = {A − Z}   (mass number minus atomic number)"),
                     F("electrons = {Z}   (neutral atom; adjust for an ion's charge)"),
                     "*Neutrons are never listed. You always subtract: A − Z."]}
         ]},
        {"rows": [
          {"kind": "example", "title": "Find the Protons, Neutrons, and Electrons",
           "slides": [13, 14], "notesLabel": "PART A · NEUTRAL ATOM",
           "cues": ["Write the subtraction, not just the answer."],
           "problem": prob("Iron-56; A = 56; Z = 26; neutral atom.", FIND_PNE, PARTICLES,
                           "Protons = 26   Neutrons = 30   Electrons = 26",
                           ["protons = Z = 26",
                            "neutrons = 56 − 26 = 30",
                            "electrons: neutral, so 26"]),
           "notes": []},
          {"kind": "example", "title": "Find the Protons, Neutrons, and Electrons",
           "slides": [13, 14], "notesLabel": "PART B · AN ION",
           "cues": ["A 2+ charge means two electrons left."],
           "problem": prob("Calcium-40; A = 40; Z = 20; charge 2+.", FIND_PNE, PARTICLES,
                           "Protons = 20   Neutrons = 20   Electrons = 18",
                           ["protons = Z = 20",
                            "neutrons = 40 − 20 = 20",
                            "electrons = 20 − 2 = 18 (it is still calcium: protons never change)"]),
           "notes": []},
          {"kind": "recall", "title": "Section summary", "cues": RECALL_CUES, "lines": 3,
           "prompt": "Explain how protons, neutrons, and electrons come from Z, A, and charge. Why does the proton count stay the same when an atom becomes an ion?",
           "answer": "Protons = Z, neutrons = A − Z, electrons = Z adjusted for charge. The proton count is the element’s identity, so an ion only gains or loses electrons.",
           "selfCheck": ["I can state protons = Z and neutrons = A − Z.",
                         "I can find electrons for a neutral atom.",
                         "I can adjust electrons for an ion’s charge."]}
         ]}
      ]
    },
    {
      "code": "1.5",
      "title": "Average Atomic Mass",
      "learningTarget": "I can calculate a weighted average atomic mass from isotope masses and abundances.",
      "pages": [
        {"rows": [
          {"title": "Isotopes: Same Element, Different Mass", "slides": 16,
           "cues": ["The chlorine isotope table.", "The reason 35.45 sits closer to 35."],
           "table": {"headers": ["Isotope", "Protons", "Neutrons", "Abundance"],
                     "widths": [0.22, 0.24, 0.24, 0.30], "rowHeightIn": 0.36,
                     "rows": [["Chlorine-35", "", "", ""], ["Chlorine-37", "", "", ""]],
                     "_key": [["Chlorine-35", "17", "18", "75.76%"],
                              ["Chlorine-37", "17", "20", "24.24%"]]},
           "notes": [F("Cl on the periodic table: {35.45}, closer to 35. Most Cl atoms are {Cl-35}."),
                     "*Same protons, different neutrons. Mass number changes; the element does not."]},
          {"title": "A Weighted Average, Not a Plain One", "slides": 17,
           "cues": ["The formula.", "The meaning of each part."],
           "notes": [F("average atomic mass = ({mass₁} × {abundance₁}) + ({mass₂} × {abundance₂}) + …"),
                     F("mass: the isotope's mass in {amu}. Usually given, close to its {mass number}."),
                     F("abundance: how common that isotope is, written as a {decimal}."),
                     F("the sum: add every isotope's {contribution}. Answer lands {between} the masses."),
                     "*Turn the percent into a decimal first: 75.76% becomes 0.7576."]},
          {"kind": "example", "title": "Average Atomic Mass of Chlorine", "slides": [18, 19],
           "cues": ["Percents to decimals first."],
           "problem": prob(["Cl-35: 34.969 amu, 75.76%.", "Cl-37: 36.966 amu, 24.24%."], FIND_AAM,
                           "Average atomic mass of chlorine = __________ amu.",
                           "Average atomic mass of chlorine = 35.45 amu.",
                           ["75.76% → 0.7576      24.24% → 0.2424",
                            "34.969 × 0.7576 = 26.493",
                            "36.966 × 0.2424 = 8.961",
                            "26.493 + 8.961 = 35.45 amu"]),
           "notes": []}
         ]},
        {"rows": [
          {"kind": "example", "title": "Now Do Copper", "slides": [20, 21],
           "cues": ["Predict first: closer to 63 or to 65."],
           "problem": prob(["Cu-63: 62.930 amu, 69.15%.", "Cu-65: 64.928 amu, 30.85%."], FIND_AAM,
                           "Average atomic mass of copper = __________ amu.",
                           "Average atomic mass of copper = 63.55 amu.",
                           ["69.15% → 0.6915      30.85% → 0.3085",
                            "62.930 × 0.6915 = 43.516",
                            "64.928 × 0.3085 = 20.030",
                            "43.516 + 20.030 = 63.55 amu. Closer to 63: Cu-63 is about 69% of copper."]),
           "notes": []},
          {"kind": "recall", "title": "Section summary", "cues": RECALL_CUES, "lines": 3,
           "prompt": "Why isn’t atomic mass on the periodic table a whole number? Explain using isotope, abundance, and weighted average.",
           "answer": "It’s a weighted average of the element’s isotopes, which have different masses. Each isotope counts by its abundance, so the average lands between the isotope masses.",
           "selfCheck": ["I can explain what makes two atoms isotopes.",
                         "I can convert percent abundance to a decimal.",
                         "I can calculate a weighted average from isotope data."]},
          {"kind": "review", "title": "Three Questions You Should Be Able to Answer",
           "slides": 22,
           "cues": ["Day 1: conceptual test.", "Day 2: calculations from S01.3 and S01.5."],
           "bigPicture": "Matter is built from atoms; atoms contain protons, neutrons, and electrons. Periodic-table atomic mass is a weighted average of isotopes.",
           "checklist": ["Notes complete for all three sections",
                         "Six-sample classification complete",
                         "Iron and calcium examples complete",
                         "Chlorine and copper calculations complete"],
           "fuzzyLabel": "Still fuzzy on / bring to review day:"}
         ]}
      ]
    }
  ],
  "conceptReview": {
    "title": "Unit 1 / Concept Review",
    "subtitle": "Connect the ideas, check common mix-ups, and explain the science in your own words.",
    "sections": [
      {"code": "1.1", "heading": "Classifying matter",
       "paragraphs": [["**Matter** has mass and occupies space. A **pure substance** has a fixed composition;",
                       "a **mixture** has variable composition and can be separated by physical means."]],
       "compare": {"left": {"heading": "Pure substances",
                            "lines": ["Element: one kind of atom.",
                                      "Compound: two or more elements",
                                      "chemically bonded in a fixed ratio."]},
                   "right": {"heading": "Mixtures",
                             "lines": ["Homogeneous: uniform throughout;",
                                       "also called a solution (such as salt water).",
                                       "Heterogeneous: nonuniform (such as granite)."]}},
       "watchOut": "O₂ is a molecule and an element. CO₂ is a molecule and a compound."},
      {"code": "1.3", "heading": "Reading an atom or ion",
       "paragraphs": [["**Proton:** +1 charge, about 1 amu, in the nucleus.",
                       "**Neutron:** 0 charge, about 1 amu, in the nucleus.",
                       "**Electron:** −1 charge, very small mass, outside the nucleus."],
                      ["**Z = protons.** This determines the element. **A = protons + neutrons.**",
                       "Neutrons = A − Z. Neutral atoms have equal numbers of protons and electrons.",
                       "Positive ions have lost electrons; negative ions have gained electrons."]],
       "watchOut": "Forming an ion changes electrons, not the element’s proton count."},
      {"code": "1.5", "heading": "Understanding average atomic mass",
       "paragraphs": [["**Isotopes:** atoms of the same element with the same protons but different neutrons.",
                       "**Abundance:** the fraction or percentage of atoms that are a particular isotope.",
                       "**Weighted average:** each isotope’s mass contributes according to its abundance."],
                      ["**Calculate:** Convert each percent to a decimal. Multiply each isotope’s mass by its abundance as a decimal, then add the products. Report the result in amu.",
                       "**Check:** The average falls between the isotope masses, closer to the more abundant one."]],
       "watchOut": "75.76% = 0.7576. Mass number is a count; average atomic mass is weighted."}
    ],
    "quickRecall": ["Why is O₂ an element even though it contains two atoms?",
                    "What changes when an atom becomes an ion? What changes between isotopes?",
                    "Why is chlorine’s average atomic mass closer to 35 than to 37?"]
  }
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
            if k in ("_key",):
                continue
            if k == "_answerKey":
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

def shape(n):
    if isinstance(n, dict):
        return {k: shape(v) for k, v in n.items() if k not in ("answer", "solution", "key")}
    if isinstance(n, list):
        return [shape(x) if not isinstance(x, str) else "s" for x in n]
    return type(n).__name__
s2, k2 = shape(student), shape(key)
# table rows differ in content only
print("structure identical (ignoring answers):", json.dumps(s2, sort_keys=True) == json.dumps(k2, sort_keys=True))
