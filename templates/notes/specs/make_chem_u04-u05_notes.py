"""Generate the Chemistry Units 4-5 guided-notes student and key specs (paged schema).

    python3 templates/notes/specs/make_chem_u04-u05_notes.py

Then build:

    OUT=/home/user/WorkWork/build/chem_u04-u05_guided_notes
    mkdir -p "$OUT"
    python3 templates/notes/build_notes_docx.py templates/notes/specs/chem_u04-u05_notes_student.json \
        "$OUT/Unit 4-5 Guided Notes.docx" --verify
    python3 templates/notes/build_notes_docx.py templates/notes/specs/chem_u04-u05_notes_key.json \
        "$OUT/Unit 4-5 Guided Notes Key.docx" --verify
    (cd "$OUT" && soffice --headless --convert-to pdf *.docx)
    python3 scripts/audit_fonts.py "$OUT/Unit 4-5 Guided Notes.pdf"
    python3 scripts/audit_print_ink.py "$OUT/Unit 4-5 Guided Notes.pdf"
    (and the same two audits on the Key PDF)

Needs the builder's opt-in "inline" prompt and "notesFirst" row keys.

Source of truth: the Astra 6 rebuild of "Unit 4-5 Slides.pptx" (33 slides). Matt's rules for
this packet, which override the guided-notes skill where they conflict:
  1. Follow the slides: same order, same content, blanks taken from the slide wording.
  2. Every slide example gets a work box directly below the fill-in content it belongs to.
  3. Every block is labelled with the slide range it covers.
  4. Separate key.

Restyled 2026-11-05 to Matt's newer guided-notes look:
  - Chem U3 notes (lucid-maxwell, 2026-11-03), "too much, condense": one block per slide, the
    example last in the block, one inline ruled row per item, no extra-notes lines, no recall
    blocks, no concept review page. Several sections share a page, and each block's cue names
    its own section code, since a page's title bar carries only one.
  - Chem U2 notes (bold-edison, 2026-10-30), "middle ground": a table where the slide is a
    table, open space for drawing, lighter format.
  Every block uses "notesFirst": the block's rows come first, then its table, then its work box,
  so the box sits directly under the content its example belongs to (rule 2).

Deliberate, unchanged from the first build:
  - Sections appear in DECK order, not numeric order: S05.2 (slides 10-11) comes before S05.1
    (slides 12-16) because the deck puts "What Is VSEPR" before "Drawing Lewis Structures".
  - No equation toolbox ("noEquationBar"): the only candidate lines are blanks the student fills.
  - No difficulty ratings: DECISIONS.md has none for U4/U5 and they are never invented.
  - 4.4 Metallic is skipped this year (Matt, 2026-11-04). 5.6 is left out.
  - Block titles avoid formulas with lowercase letters (CCl4, HCl, CH3Cl): the builder prints a
    title in caps as the cue label, and "CCL4" is a different thing.

Edit this file, not the JSON it writes.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "chem_u04-u05_notes"

# --------------------------------------------------------------------------------------------
# Slide content the text extraction could not read (slides 9, 19, 32), filled from the
# rendered Astra slides by the main session. Until filled, the generator writes nothing.
# --------------------------------------------------------------------------------------------
SLIDE_09 = {   # Astra slide 9, as rendered: bond type given, the rest filled in
    "headers": ["Bond type", "Electron behavior", "Class ΔEN guide"],
    "rows": [["Nonpolar covalent", "", ""], ["Polar covalent", "", ""], ["Ionic", "", ""]],
    "_key": [["Nonpolar covalent", "Nearly equal sharing", "< 0.40"],
             ["Polar covalent", "Unequal sharing; δ+ and δ−", "0.40–1.80"],
             ["Ionic", "Opposite ions attract", "> 1.80"]],
    "widths": [0.3, 0.42, 0.28], "rowHeightIn": 0.30,
}

SLIDE_19 = {   # Astra slide 19, "Common Molecular Shapes"
    "headers": ["Groups", "Lone pairs on center", "Molecular shape", "Example"],
    "rows": [["2", "0", "", ""], ["3", "0", "", ""], ["4", "0", "", ""], ["4", "1", "", ""], ["4", "2", "", ""]],
    "_key": [["2", "0", "Linear • 180°", "CO₂"], ["3", "0", "Trigonal planar • 120°", "BF₃, CH₂O"],
             ["4", "0", "Tetrahedral • 109.5°", "CH₄, CCl₄"], ["4", "1", "Trigonal pyramidal • ≈107°", "NH₃"],
             ["4", "2", "Bent • ≈104.5°", "H₂O"]],
    "widths": [0.14, 0.24, 0.38, 0.24], "rowHeightIn": 0.30,
}

SLIDE_32 = [   # Astra slide 32, as rendered
    ("CO₂", "Dispersion only"), ("CCl₄", "Dispersion only"),
    ("HCl", "Dispersion, dipole–dipole"), ("CH₃Cl", "Dispersion, dipole–dipole"),
    ("H₂O", "Dispersion, dipole–dipole, hydrogen bonding"), ("NH₃", "Dispersion, dipole–dipole, hydrogen bonding"),
    ("HF", "Dispersion, dipole–dipole, hydrogen bonding"),
]

missing = [n for n, v in (("SLIDE_19", SLIDE_19), ("SLIDE_32", SLIDE_32)) if v is None]
if missing:
    sys.exit("make_chem_u04-u05_notes: fill " + " and ".join(missing) + " from the rendered "
             "Astra slides before generating. Nothing was written.")


# --------------------------------------------------------------------------------------------
# Building blocks. Keep each row short: label + answer should stay under about 72 characters,
# so the key's bold answer fits on its one ruled row and the key paginates like the student copy.
# --------------------------------------------------------------------------------------------
def P(label, answer):
    """One inline ruled row: the label, then the writing space. The key prints `answer` on it."""
    return {"prompt": label, "answer": answer, "inline": True}


def notes(title, cues, rows, table=None, rows_first=True):
    """One slide's block with no example. `rows_first` False keeps the table above the rows,
    for a slide whose table comes before its closing line (slides 9, 18, 19)."""
    d = {"title": title, "cues": cues, "noWorkBox": True, "extraNotes": False, "notes": rows}
    if rows_first:
        d["notesFirst"] = True
    if table:
        d["table"] = table
    return d


def example(title, cues, rows, box_label, height, solution, table=None):
    """One slide's block that works an example: its rows, then (if any) its table, then the work
    box, last, directly under them. The box label names the slide (rule 3)."""
    d = {"kind": "example", "title": title, "cues": cues, "extraNotes": False,
         "notesFirst": True, "notes": rows,
         "problem": {"workLabel": box_label, "workHeightIn": height, "solution": solution}}
    if table:
        d["table"] = table
    return d


LEWIS_IN = 1.7      # Lewis structure boxes (slides 13-16)
POLAR_IN = 2.0      # Lewis + dipole arrows (slides 23-26)
PAIR_IN = 1.7       # two small molecules with arrows (slides 21, 22)


spec = {
  "course": "chemistry",
  # The builder holds one unit per packet. 4 puts "CHEMICAL BONDING" on the cover and
  # "UNIT 04" in every footer, including the U5 pages. Section bars and cues still read
  # U05 / S05.x. A template gap, reported; not worked around here.
  "unit": 4,
  "key": False,
  "noEquationBar": True,
  "cover": {
    # Set here because sections share pages: derived, the kicker would count 7 and the
    # checklist would list the combined page titles. Phase 2 is courses/chemistry/DECISIONS.md.
    "kicker": "GUIDED NOTES  ·  PHASE 02  ·  10 SECTIONS",
    "sectionList": ["S04.1   Why Atoms Bond", "S04.2   Ionic Bonding", "S04.3   Covalent Bonding",
                    "S04.5   Electronegativity & Bond Type", "S04.6   Bond Polarity",
                    "S05.2   VSEPR Theory", "S05.1   Lewis Electron Structures",
                    "S05.3   Molecular Geometry", "S05.4   Molecular Polarity",
                    "S05.5   Intermolecular Forces"],
    "keyTerms": [
      {"code": "4.1", "terms": ["Chemical bond", "octet rule"]},
      {"code": "4.2", "terms": ["Ionic bonding", "ion", "crystal"]},
      {"code": "4.3", "terms": ["Covalent bonding", "shared pair", "network solid"]},
      {"code": "4.5", "terms": ["Electronegativity (EN)", "ΔEN", "nonpolar covalent",
                                "polar covalent", "ionic"]},
      {"code": "4.6", "terms": ["Dipole arrow", "δ+", "δ−", "polar bond"]},
      {"code": "5.2", "terms": ["VSEPR", "electron group"]},
      {"code": "5.1", "terms": ["Lewis structure", "valence electrons", "lone pair",
                                "double bond"]},
      {"code": "5.3", "terms": ["Bond angle", "octet exception", "tetrahedral",
                                "trigonal pyramidal", "bent"]},
      {"code": "5.4", "terms": ["Bond polarity", "molecular polarity", "net pull"]},
      {"code": "5.5", "terms": ["Intermolecular force (IMF)", "intramolecular",
                                "hydrogen bonding", "dipole–dipole", "London dispersion"]},
    ],
    "howToUse": ("Each block names its slides, so you can match the page to the screen. "
                 "Fill in each line while that slide is up. "
                 "When a slide works an example, copy it into the box at the end of that block, "
                 "with dipole arrows where the slide shows them."),
  },
  "sectionsContent": [
    # ======================================================== slides 1-4 · S04.1, S04.2
    {"code": "4.1", "title": "Why Atoms Bond & Ionic Bonding",
     "learningTarget": "I can define a chemical bond, state the octet rule, and describe ionic bonding.",
     "pages": [{"rows": [
       notes("Slides 1–3 · Why atoms bond", ["S04.1"], [
         P("Three ideas", "bonding, molecular structure, intermolecular forces"),
         P("The unit", "draw the electrons → find the shape → explain the properties"),
         P("Atoms bond when", "the bonded arrangement has lower energy"),
         P("Chemical bond", "an attraction that holds atoms or ions together"),
         P("Octet rule", "many atoms bond with 8 outer electrons (H needs only 2)"),
         P("The octet rule is", "a guide; some atoms are exceptions"),
       ]),
       example("Slide 4 · Ionic bonding", ["S04.2"], [
         P("Ionic bonding", "electrons transfer; opposite ions attract"),
         P("Usually between", "a metal and a nonmetal"),
         P("Properties", "hard and brittle, high melting points"),
         P("Ions form", "a repeating crystal"),
         P("Conducts", "when molten or dissolved, not as a solid"),
       ], "Slide 4 · Na and Cl: show the electron transfer and the two ions it makes", 1.6,
          ["Na loses one electron → Na+", "Cl gains that electron → Cl−",
           "The opposite ions attract."]),
     ]}]},
    # ======================================================== slides 5-7 · S04.3, S04.5
    {"code": "4.3", "title": "Covalent Bonding & Electronegativity",
     "learningTarget": "I can describe covalent bonding and classify a bond from its EN difference.",
     "pages": [{"rows": [
       notes("Slide 5 · Covalent bonding", ["S04.3"], [
         P("Covalent bonding", "atoms share pairs of electrons"),
         P("Usually between", "nonmetals"),
         P("One bond", "one shared pair of electrons"),
         P("Properties", "often low melting points; usually poor conductors"),
         P("Found as", "gases, liquids, or soft solids"),
         P("Exception", "network solids (diamond): strong bonds throughout"),
       ]),
       notes("Slide 6 · EN and bond type",
             ["S04.5", "The cutoffs are class guidelines, not sharp boundaries."], [
         P("Electronegativity", "how strongly an atom pulls on shared electrons"),
         P("ΔEN", "higher EN − lower EN"),
       ], table={"headers": ["Bond type", "ΔEN", "Sharing"],
                 "widths": [0.34, 0.26, 0.40], "rowHeightIn": 0.30,
                 "rows": [["Nonpolar covalent", "", ""], ["Polar covalent", "", ""],
                          ["Ionic", "", ""]],
                 "_key": [["Nonpolar covalent", "Under 0.40", "Nearly equal sharing"],
                          ["Polar covalent", "0.40–1.80", "Unequal sharing"],
                          ["Ionic", "Over 1.80", "Opposite ions attract"]]}),
       example("Slide 7 · Classifying bonds", ["S04.5", "Subtract the EN values. Match the difference to a bond type."], [
         P("Bigger EN difference", "more uneven electron sharing"),
       ], "Slide 7 · EN: H 2.20, C 2.55, O 3.44, Na 0.93, Cl 3.16. Find ΔEN and the bond type "
          "for C–H, C–O and Na–Cl.", 1.6,
          ["C–H: 2.55 − 2.20 = 0.35; 0.35 < 0.40 → nonpolar covalent",
           "C–O: 3.44 − 2.55 = 0.89; 0.40 ≤ 0.89 ≤ 1.80 → polar covalent",
           "Na–Cl: 3.16 − 0.93 = 2.23; 2.23 > 1.80 → ionic"]),
     ]}]},
    # ======================================================== slides 8-9 · S04.6
    {"code": "4.6", "title": "Bond Polarity",
     "learningTarget": "I can draw a dipole arrow on a polar bond and label its δ+ and δ− ends.",
     "pages": [{"rows": [
       example("Slide 8 · Bond polarity and dipole arrows", ["S04.6"], [
         P("Dipole arrow points toward", "the atom pulling harder"),
         P("Nonpolar bond", "equal or nearly equal sharing (H–H, Cl–Cl, C–H)"),
         P("Polar bond", "unequal sharing; electrons closer to the higher-EN atom"),
         P("Polar examples", "H–Cl, O–H, C–O"),
         P("δ− and δ+", "partly negative; partly positive (crossed end of the arrow)"),
       ], "Slide 8 · Draw H–H and H–Cl. Add the dipole arrow, δ+ and δ− to the polar bond.", 1.8,
          ["H–H: no arrow; equal sharing.",
           "H–Cl: arrow points toward Cl; crossed end at H. H is δ+, Cl is δ−."]),
       notes("Slide 9 · Bond types at a glance",
             ["S04.6", "Compare how the electrons are shared or transferred."], [
         P("Ionic bonds, usually", "metal + nonmetal"),
         P("Covalent bonds, usually", "nonmetal + nonmetal"),
       ], table=SLIDE_09, rows_first=False),
     ]}]},
    # ======================================================== slides 10-16 · S05.2, S05.1
    {"code": "5.2", "title": "VSEPR Theory & Lewis Structures",
     "learningTarget": "I can state the VSEPR idea and draw a Lewis structure by counting, connecting, filling, and checking.",
     "pages": [
      {"rows": [
       notes("Slides 10–11 · VSEPR theory", ["S05.2"], [
         P("VSEPR", "Valence Shell Electron Pair Repulsion"),
         P("The sequence", "Lewis structure → electron groups → 3D shape"),
         P("Electron groups", "repel and spread out around the central atom"),
         P("Lewis structures show", "bonds and lone pairs"),
         P("To predict shape", "count the groups"),
         P("4 bonds, no lone pairs", "tetrahedral"),
       ]),
       notes("Slide 12 · Drawing Lewis structures",
             ["S05.1", "Follow the steps, then check your electron count."], [
         P("1  Count", "add valence electrons; − charge: add, + charge: subtract"),
         P("2  Connect", "center usually lowest EN, never H; add single bonds"),
         P("3  Fill", "outer atoms first (H 2, usually 8); leftovers on center"),
         P("4  Check", "total and shells correct"),
         P("If not, fix", "recount, check exceptions, or make double/triple bonds"),
         P("Bond line / lone pair", "2 shared / 2 unshared electrons"),
       ]),
       example("Slide 13 · Lewis structure: BF₃", ["S05.1"], [
         P("BF₃ valence electrons", "3 + 3(7) = 24"),
         P("Boron ends with", "6 electrons: an octet exception"),
       ], "Slide 13 · Draw the BF₃ Lewis structure", LEWIS_IN,
          ["Connect: three B–F bonds use 6 electrons.",
           "Fill: each F gets 3 lone pairs, 18 electrons.",
           "Check: 6 bonding + 18 lone-pair electrons = 24."]),
      ]},
      {"rows": [
       example("Slide 14 · Lewis structure: CO₂", ["S05.1"], [
         P("CO₂ valence electrons", "4 + 2(6) = 16"),
         P("Fix", "share one lone pair from each O: O=C=O"),
       ], "Slide 14 · Draw the CO₂ Lewis structure", LEWIS_IN,
          ["Connect: O–C–O uses 4 electrons.",
           "Fill: the other 12 go on the oxygens. Carbon has only 4.",
           "Fix: share one lone pair from each O → O=C=O.",
           "Check: 8 bonding + 8 lone-pair electrons = 16. All atoms have 8."]),
       example("Slide 15 · Lewis structure: NH₃", ["S05.1"], [
         P("NH₃ valence electrons", "5 + 3(1) = 8"),
         P("Leftovers", "8 − 6 = 2 electrons: one lone pair on N"),
       ], "Slide 15 · Draw the NH₃ Lewis structure", LEWIS_IN,
          ["Connect: three N–H bonds use 6 electrons. Each H now has 2.",
           "Leftovers: 8 − 6 = 2. Both go on N as one lone pair.",
           "Check: N has 8 around it. Total used = 8."]),
       example("Slide 16 · Lewis structure: CH₂O", ["S05.1", "H gets 2; C and O get 8."], [
         P("CH₂O valence electrons", "4 + 2(1) + 6 = 12"),
         P("Fix", "share one O lone pair to make C=O"),
       ], "Slide 16 · Draw the CH₂O Lewis structure", LEWIS_IN,
          ["Connect: three single bonds use 6 electrons.",
           "Fill: 6 electrons on O. Carbon has only 6.",
           "Fix: share one O lone pair → C=O.",
           "Check: C=O 4 + two C–H 4 + two O lone pairs 4 = 12."]),
      ]},
     ]},
    # ======================================================== slides 17-19 · S05.3
    {"code": "5.3", "title": "Molecular Geometry",
     "learningTarget": "I can use electron groups and lone pairs to predict a molecule's shape and bond angle.",
     "pages": [{"rows": [
       notes("Slide 17 · VSEPR: predicting shape", ["S05.3"], [
         P("Bonding groups", "a single, double, or triple bond counts as ONE group"),
         P("Lone pairs", "take up space; usually make bond angles smaller"),
       ], table={"headers": ["Molecule", "Lone pairs on the center", "Bond angle"],
                 "widths": [0.28, 0.40, 0.32], "rowHeightIn": 0.28,
                 "rows": [["CH₄", "", ""], ["NH₃", "", ""], ["H₂O", "", ""]],
                 "_key": [["CH₄", "0", "109.5°"], ["NH₃", "1", "about 107°"],
                          ["H₂O", "2", "about 104.5°"]]}),
       notes("Slide 18 · Octet rule exceptions",
             ["S05.3", "Count all bonding and lone-pair electrons around the atom."], [
         P("Cl, Br, and I", "can also exceed 8 in some compounds"),
         P("Odd total", "NO has 11 valence electrons; one stays unpaired"),
         P("Period-2 atoms (C, N, O, F)", "cannot have more than 8"),
       ], table={"headers": ["", "Atom", "Electrons around it", "Example"],
                 "widths": [0.20, 0.12, 0.24, 0.44], "rowHeightIn": 0.28,
                 "rows": [["Fewer than 8", "H", "", ""], ["Fewer than 8", "Be", "", ""],
                          ["Fewer than 8", "B", "", ""], ["More than 8", "P", "", ""],
                          ["More than 8", "S", "", ""], ["More than 8", "Xe", "", ""]],
                 "_key": [["Fewer than 8", "H", "2", "H₂: one bond"],
                          ["Fewer than 8", "Be", "4", "BeCl₂: two bonds"],
                          ["Fewer than 8", "B", "6", "BF₃: three bonds"],
                          ["More than 8", "P", "10", "PCl₅: 5 bonds"],
                          ["More than 8", "S", "12", "SF₆: 6 bonds"],
                          ["More than 8", "Xe", "12", "XeF₄: 4 bonds + 2 lone pairs"]]},
             rows_first=False),
       notes("Slide 19 · Common molecular shapes",
             ["S05.3", "Count electron groups. Name the shape using the atoms."], [
         P("Lone pairs change the shape; the shape name", "describes the atoms"),
       ], table=SLIDE_19, rows_first=False),
     ]}]},
    # ======================================================== slides 20-26 · S05.4
    {"code": "5.4", "title": "Molecular Polarity",
     "learningTarget": "I can decide whether a molecule is polar by checking its bonds and its shape.",
     "pages": [
      {"rows": [
       example("Slides 20–21 · Bond vs. molecular polarity", ["S05.4"], [
         P("A molecule with polar bonds can", "still be nonpolar"),
         P("Bond polarity (one bond)", "compare the atoms’ EN values"),
         P("Molecular polarity (whole molecule)", "check whether the bond pulls cancel"),
         P("HCl", "one polar bond → polar molecule"),
         P("CO₂", "equal, opposite pulls → nonpolar"),
         P("To find molecular polarity, check", "the bonds AND the shape"),
       ], "Slide 21 · Draw HCl and CO₂ with their dipole arrows", PAIR_IN,
          ["H–Cl: arrow toward Cl, crossed end at H. H δ+, Cl δ−.",
           "O=C=O: two arrows from C toward each O, equal and opposite, so they cancel."]),
       example("Slide 22 · Canceling bond dipoles", ["S05.4"], [
         P("Bond pulls cancel when", "their directions balance"),
         P("Balanced pulls → nonpolar", "CO₂, BF₃, CH₄, CCl₄"),
         P("Pulls do not cancel → polar", "H₂O, NH₃, HCl, CH₃Cl"),
         P("Before deciding, check", "the 3D shape and the outer atoms"),
       ], "Slide 22 · Draw BF₃ and NH₃ with their dipole arrows", PAIR_IN,
          ["BF₃: three B–F arrows toward each F, spread evenly around B; they cancel.",
           "NH₃: three N–H arrows toward N; the pyramid leaves a net pull toward N."]),
      ]},
      {"rows": [
       example("Slide 23 · Molecular polarity: H₂O",
               ["S05.4", "Draw it, check the bonds, then check the shape."], [
         P("H₂O electrons", "6 + 2(1) = 8: two bonds, two O lone pairs"),
         P("ΔEN (O 3.44, H 2.20)", "1.24: each O–H bond is polar"),
         P("Shape", "bent; the bond pulls do not cancel"),
         P("Molecule", "POLAR"),
         P("Partial charges", "oxygen side δ−, hydrogen side δ+"),
       ], "Slide 23 · Draw H₂O with its dipole arrows, δ+ and δ−", POLAR_IN,
          ["Bent H–O–H with two lone pairs on O.",
           "Arrows from each H toward O. O δ−, H δ+. The pulls do not cancel."]),
       example("Slide 24 · Molecular polarity: NH₃",
               ["S05.4", "A lone pair changes the arrangement of the three N–H bonds."], [
         P("NH₃ electrons", "5 + 3(1) = 8: three bonds, one N lone pair"),
         P("ΔEN (N 3.04, H 2.20)", "0.84: each N–H bond is polar"),
         P("Shape", "trigonal pyramidal; the pulls do not cancel"),
         P("Molecule", "POLAR"),
         P("NH₃ is", "a 3D pyramid, not a flat triangle"),
       ], "Slide 24 · Draw NH₃ with its dipole arrows", POLAR_IN,
          ["Pyramid: N on top with one lone pair, three H below.",
           "Arrows from each H toward N. Net pull toward N."]),
      ]},
      {"rows": [
       example("Slide 25 · Molecular polarity: carbon tetrachloride",
               ["S05.4", "Four polar bonds can balance in three dimensions."], [
         P("CCl₄ electrons", "4 + 4(7) = 32: four bonds, 3 lone pairs on each Cl"),
         P("ΔEN (Cl 3.16, C 2.55)", "0.61: each C–Cl bond is polar"),
         P("Shape", "tetrahedral; four equal pulls cancel"),
         P("Molecule", "NONPOLAR"),
         P("Solid wedge / dashed wedge", "toward you / away from you"),
       ], "Slide 25 · Draw CCl₄ with wedges and its dipole arrows", POLAR_IN,
          ["Tetrahedral C with four Cl; one solid wedge, one dashed wedge.",
           "Four equal arrows from C toward each Cl. They cancel."]),
       example("Slide 26 · Tetrahedral molecules",
               ["S05.4", "Both have 4 bonds and no lone pairs on the central carbon."], [
         P("CCl₄", "four identical C–Cl pulls cancel → NONPOLAR"),
         P("CH₃Cl", "the C–Cl pull is not balanced → POLAR"),
         P("Shape alone does not decide polarity", "the outer atoms matter"),
       ], "Slide 26 · Draw CCl₄ and CH₃Cl with their dipole arrows and the net pull", POLAR_IN,
          ["CCl₄: four equal C–Cl arrows cancel. No net pull.",
           "CH₃Cl: the C–Cl arrow is not balanced. Net pull toward Cl."]),
      ]},
     ]},
    # ======================================================== slides 27-32 · S05.5
    {"code": "5.5", "title": "Intermolecular Forces",
     "learningTarget": "I can name the intermolecular forces a molecule has and explain where each comes from.",
     "pages": [
      {"rows": [
       notes("Slides 27–28 · Intermolecular forces", ["S05.5"], [
         P("The three IMFs", "hydrogen bonding, dipole–dipole, London dispersion"),
         P("Intermolecular forces (IMFs)", "attractions between separate molecules"),
         P("Inside a molecule", "covalent (intramolecular) bonds connect its atoms"),
         P("Boiling water", "separates H₂O molecules; does not break O–H bonds"),
       ]),
       notes("Slide 29 · Hydrogen bonding", ["S05.5"], [
         P("Hydrogen bonding", "a partly positive H attracts a lone pair on N, O, or F"),
         P("Look for", "H bonded directly to N, O, or F"),
         P("In the picture", "Hδ+ on one water molecule attracts Oδ− on another"),
         P("Examples", "H₂O, NH₃, HF"),
         P("Effects", "helps raise water’s boiling point; holds DNA strands together"),
         P("Strength", "often strong for similar-sized molecules; not always strongest"),
       ]),
       notes("Slide 30 · Dipole–dipole forces", ["S05.5"], [
         P("Dipole–dipole", "polar molecules attract through opposite partial charges"),
         P("Look for", "polar molecules with δ+ and δ− ends"),
         P("In the picture", "Clδ− on one HCl molecule attracts Hδ+ on another"),
         P("Examples", "HCl, CH₃Cl, SO₂; all also have dispersion"),
         P("These partial charges are", "lasting features of each polar molecule"),
       ]),
      ]},
      {"rows": [
       notes("Slide 31 · London dispersion forces", ["S05.5"], [
         P("London dispersion", "moving electrons create temporary + and − ends"),
         P("Found in", "every atom and molecule"),
         P("Main attraction for", "nonpolar molecules"),
         P("Electrons shift", "a brief dipole; the neighboring cloud shifts too"),
         P("Stronger with", "larger, easier-to-shift electron clouds"),
         P("Example", "I₂ is solid at room temperature"),
         P("The picture shows", "changing charge, not permanently charged atoms"),
       ]),
       example("Slide 32 · Identifying intermolecular forces", ["S05.5"], [
         P("Every molecule has", "dispersion; check what else it has"),
         P("Stronger attractions", "higher boiling point (size and shape matter too)"),
       ], "Slide 32 · Sketch any molecule you need, to check its polarity and its H–N, H–O or H–F bonds",
          1.4,
          ["Polar: HCl, CH₃Cl, H₂O, NH₃, HF. Nonpolar: CO₂, CCl₄.",
           "H bonded to N, O or F: H₂O, NH₃, HF."],
          table={"headers": ["Molecule", "IMFs it has"], "widths": [0.22, 0.78],
                 "rowHeightIn": 0.28,
                 "rows": [[m, ""] for m, _ in SLIDE_32],
                 "_key": [[m, imf] for m, imf in SLIDE_32]}),
      ]},
     ]},
  ],
}


def strip_answers(node):
    """Student copy: the same tree with every answer removed."""
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k in ("_key", "_answerKey", "solution"):
                continue
            if k == "answer" and "prompt" in node and not isinstance(node.get("prompt"), dict):
                continue
            out[k] = strip_answers(v)
        return out
    if isinstance(node, list):
        return [strip_answers(x) for x in node]
    return node


def fill_answers(node):
    """Key: the same tree with answers put in place."""
    if isinstance(node, dict):
        out = {k: fill_answers(v) for k, v in node.items() if k not in ("_key", "_answerKey")}
        if "_key" in node:
            out["rows"] = node["_key"]
        if "_answerKey" in node:
            out["answer"] = node["_answerKey"]
        return out
    if isinstance(node, list):
        return [fill_answers(x) for x in node]
    return node


# Recall rule (templates/notes/recall.py), checked here on the paged rows too: no cue or
# notes line may ask a question. recall.offences() reads only flat specs' rows.
sys.path.insert(0, os.path.dirname(HERE))
from recall import QUESTION_MARK, OPENER  # noqa: E402
bad = []
for sec in spec["sectionsContent"]:
    for page in sec["pages"]:
        for row in page["rows"]:
            lines = [row.get("title", "")] + list(row.get("cues", []))
            lines += [n if isinstance(n, str) else n.get("prompt", n.get("text", ""))
                      for n in row.get("notes", [])]
            for t in lines:
                if QUESTION_MARK.search(t) or OPENER.match(t.lstrip("*")):
                    bad.append((sec["code"], t))
if bad:
    sys.exit("make_chem_u04-u05_notes: questions in the recall columns: " + repr(bad))

# A block title is printed in caps as its cue label. Lowercase letters in a formula would
# come out wrong (CCl4 -> CCL4), so a title may not carry one.
import re  # noqa: E402
FORMULA_LC = re.compile(r"[A-Z][a-z][₀-₉]|[A-Z][₀-₉]*[A-Z][a-z]|\bHCl\b")
caps = [row["title"] for sec in spec["sectionsContent"] for page in sec["pages"]
        for row in page["rows"] if FORMULA_LC.search(row["title"])]
if caps:
    sys.exit("make_chem_u04-u05_notes: these titles would print a formula wrongly in caps: "
             + repr(caps))

student = strip_answers(spec)
key = fill_answers(spec)
key["key"] = True
for name, data in (("student", student), ("key", key)):
    with open(os.path.join(HERE, f"{STEM}_{name}.json"), "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
pages = sum(len(s["pages"]) for s in spec["sectionsContent"])
print("wrote", STEM + "_student.json and", STEM + "_key.json", f"({pages} content pages + cover)")
