"""Generate the Chemistry U1 guided-notes student and key specs (paged schema).

    python3 templates/notes/specs/make_chem_u01_s01.1-s01.5_notes.py

One source, so the key is the student structure with answers filled and the two cannot
drift. Edit this file, not the JSON it writes. Wording follows the U1 deck
(SHULL_CHEM_Slides_U01_S01.1-S01.5) and the page grouping Matthew approved.
"""
import copy, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "chem_u01_s01.1-s01.5_notes"

def P(prompt, answer):            # a prompt with a writing line; `answer` is the key's
    return {"prompt": prompt, "answer": answer}

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
    "howToUse": "Quiz yourself with the left-column questions. Gray side rules mark must-write notes (lime blocks in the slides). Show your reasoning and units in each work box."
  },
  "sectionsContent": [
    {
      "code": "1.1",
      "title": "Matter & Changes",
      "learningTarget": "I can sort any sample of matter as an element, compound, or mixture, and homogeneous or heterogeneous if it is a mixture.",
      "pages": [
        {"subtitle": "Classify matter as an element, compound, or mixture; then classify mixtures.",
         "rows": [
          {"title": "Vocabulary",
           "cues": ["How do pure substances and mixtures differ?",
                    "Which term means evenly mixed throughout?"],
           "notes": [P("DEFINE: matter", "Anything that has mass and takes up space."),
                     P("DEFINE: pure substance", "One kind of particle throughout; fixed composition."),
                     P("DEFINE: mixture", "Two or more substances physically combined; composition can vary."),
                     "*Solution: a homogeneous mixture, evenly mixed and the same throughout."]},
          {"title": "The matter flowchart",
           "cues": ["What two questions help classify a sample?",
                    "Where does the chart split into element vs. compound?"],
           "notesLabel": "COPY THE FLOWCHART",
           "flowchart": {"root": "MATTER", "branches": ["Pure substance", "Mixture"],
                         "leaves": ["Element", "Compound", "Homogeneous", "Heterogeneous"]},
           "notes": []},
          {"title": "Element, compound, molecule",
           "cues": ["Why is O₂ not a compound?", "What makes something a molecule?"],
           "notes": [P("DEFINE: element", "One kind of atom only; can’t be broken down chemically."),
                     P("DEFINE: compound", "Two or more elements chemically bonded in a fixed, repeating ratio."),
                     P("DEFINE: molecule", "Atoms bonded together; one element (O₂) or a compound (H₂O)."),
                     "*O₂ is a molecule with one element. A compound needs at least two different elements."]}
         ]},
        {"subtitle": "Mixtures, classification practice, and a check of your understanding.",
         "rows": [
          {"title": "Homogeneous vs. heterogeneous",
           "cues": ["Which mixture is a solution?", "What test tells the two apart?"],
           "notes": [P("DEFINE: homogeneous", "Evenly mixed and the same throughout; also called a solution."),
                     P("DEFINE: heterogeneous", "The parts stay separate; you can see distinct pieces or layers."),
                     dict(P("Copy: the quick test for telling them apart",
                       "If a scoop from the top matches a scoop from the bottom, it’s homogeneous. If not, heterogeneous."), lines=2)]},
          {"title": "Classify six samples",
           "cues": ["What’s the first question you ask about any sample?"],
           "noWorkBox": True,
           "table": {"headers": ["Sample", "Classification", "Reasoning"],
                     "widths": [0.36, 0.27, 0.37], "rowHeightIn": 0.30,
                     "rows": [["Copper wire", "", ""], ["Salt water", "", ""],
                              ["Carbon dioxide, CO₂", "", ""], ["Granite", "", ""],
                              ["Oxygen gas, O₂", "", ""], ["Stainless steel", "", ""]],
                     "_key": [["Copper wire", "Element", "One kind of atom, Cu"],
                              ["Salt water", "Mixture — homogeneous", "Solution, evenly mixed"],
                              ["Carbon dioxide, CO₂", "Compound", "C and O bonded in a fixed ratio"],
                              ["Granite", "Mixture — heterogeneous", "Grains visible to the eye"],
                              ["Oxygen gas, O₂", "Element", "Molecule of one element"],
                              ["Stainless steel", "Mixture — homogeneous", "Alloy of metals, evenly mixed"]]},
           "notes": []},
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
        {"subtitle": "Find protons, neutrons, and electrons from atomic number, mass number, and charge.",
         "rows": [
          {"title": "Subatomic particles",
           "cues": ["Which particles live in the nucleus?", "Which particle has almost no mass?"],
           "table": {"headers": ["Particle", "Charge", "Mass (amu)", "Location"],
                     "widths": [0.23, 0.18, 0.25, 0.34], "rowHeightIn": 0.38,
                     "rows": [["Proton", "", "", ""], ["Neutron", "", "", ""],
                              ["Electron", "", "", ""]],
                     "_key": [["Proton", "+1", "1", "Nucleus"], ["Neutron", "0", "1", "Nucleus"],
                              ["Electron", "−1", "about 0", "Electron cloud"]]},
           "notes": ["*Protons determine the element. Forming an ion changes electrons, not protons."]},
          {"title": "Atomic & mass numbers",
           "cues": ["How do you find neutrons from A and Z?", "When does electrons ≠ Z?"],
           "notes": [P("Fill in: protons =", "Z"),
                     P("Fill in: neutrons =", "A − Z"),
                     P("Fill in: electrons (neutral atom) =", "Z"),
                     P("Fill in: electrons (ion) =", "Z, adjusted for charge (a 2+ ion has two fewer)")]},
          {"kind": "example", "title": "Neutral iron-56",
           "cues": ["What do you read straight off the periodic table?"],
           "problem": prob("Iron-56; A = 56; Z = 26; neutral atom.", FIND_PNE, PARTICLES,
                           "Protons = 26   Neutrons = 30   Electrons = 26",
                           ["protons = Z = 26",
                            "neutrons = A − Z = 56 − 26 = 30",
                            "electrons = 26 (neutral, so the same as protons)"]),
           "notes": []}
         ]},
        {"subtitle": "Ions, section summary, and an essential particle-count reminder.",
         "rows": [
          {"kind": "example", "title": "Calcium ion, 2+",
           "cues": ["Why does an ion have a different number of electrons than protons?"],
           "problem": prob("Calcium ion; A = 40; Z = 20; charge = 2+.", FIND_PNE, PARTICLES,
                           "Protons = 20   Neutrons = 20   Electrons = 18",
                           ["protons = Z = 20",
                            "neutrons = A − Z = 40 − 20 = 20",
                            "electrons = 20 − 2 = 18 (a 2+ ion lost two electrons)"]),
           "notes": []},
          {"kind": "recall", "title": "Section summary", "cues": RECALL_CUES, "lines": 3,
           "prompt": "Explain how protons, neutrons, and electrons come from Z, A, and charge. Why does the proton count stay the same when an atom becomes an ion?",
           "answer": "Protons = Z, neutrons = A − Z, electrons = Z adjusted for charge. The proton count is the element’s identity, so an ion only gains or loses electrons.",
           "selfCheck": ["I can state protons = Z and neutrons = A − Z.",
                         "I can find electrons for a neutral atom.",
                         "I can adjust electrons for an ion’s charge."]},
          {"kind": "recap", "title": "Particle-count reminders",
           "cues": ["Use these relationships to check your work."],
           "notes": [{"text": "**Protons = Z:** the element’s identity.", "after": 0},
                     {"text": "**Neutrons = A − Z:** calculate them from mass and atomic numbers.", "after": 0},
                     {"text": "**Electrons = Z, adjusted for charge.** A 2+ ion has two fewer electrons; a 1− ion has one more.", "after": 10},
                     {"text": "**Isotopes:** same protons, different neutrons. Their mass numbers differ, but their element does not."}]}
         ]}
      ]
    },
    {
      "code": "1.5",
      "title": "Average Atomic Mass",
      "learningTarget": "I can calculate a weighted average atomic mass from isotope masses and abundances.",
      "pages": [
        {"subtitle": "Calculate a weighted average from isotope masses and abundances written as decimals.",
         "rows": [
          {"title": "Isotopes",
           "cues": ["What is the same in Cl-35 and Cl-37? What differs?",
                    "Which isotope is more common?"],
           "table": {"headers": ["Isotope", "Protons", "Neutrons", "Mass no.", "Abundance"],
                     "widths": [0.18, 0.17, 0.19, 0.21, 0.25], "rowHeightIn": 0.36,
                     "rows": [["Cl-35", "", "", "", ""], ["Cl-37", "", "", "", ""]],
                     "_key": [["Cl-35", "17", "18", "35", "75.76%"],
                              ["Cl-37", "17", "20", "37", "24.24%"]]},
           "notes": [P("Copy: why 35.45 is closer to 35",
                       "Cl-35 is about 76% of chlorine atoms, so it pulls the weighted average toward 35."),
                     "*Same protons, different neutrons: mass number changes; the element does not."]},
          {"title": "The calculation",
           "cues": ["Why a weighted average, not a plain average?",
                    "What must happen to a percent first?"],
           "notes": [P("DEFINE: mass (in this formula)",
                       "That isotope’s mass in amu; usually given, close to its mass number."),
                     P("DEFINE: abundance",
                       "How common that isotope is, written as a decimal before you multiply."),
                     P("Copy: what to do after weighting each isotope",
                       "Add every isotope’s mass × abundance. The sum is the average atomic mass.")]},
          {"kind": "example", "title": "Chlorine example",
           "cues": ["What’s the first step before you touch the calculator?"],
           "problem": prob(["Cl-35: 34.969 amu, 75.76%.", "Cl-37: 36.966 amu, 24.24%."], FIND_AAM,
                           "Average atomic mass of chlorine = __________ amu.",
                           "Average atomic mass of chlorine = 35.45 amu.",
                           ["75.76% → 0.7576      24.24% → 0.2424",
                            "34.969 × 0.7576 = 26.493",
                            "36.966 × 0.2424 = 8.961",
                            "26.493 + 8.961 = 35.45 amu"]),
           "notes": []}
         ]},
        {"subtitle": "Independent practice, section summary, and readiness for the Unit 1 test.",
         "rows": [
          {"kind": "example", "title": "Your turn: copper",
           "cues": ["Predict: closer to 63 or 65?",
                    "Which isotope’s abundance does the pulling, and why?"],
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
          {"kind": "review", "title": "Pulling it together",
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
