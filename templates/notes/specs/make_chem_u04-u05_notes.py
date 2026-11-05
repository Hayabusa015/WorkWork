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

Source of truth: the Astra 6 rebuild of "Unit 4-5 Slides.pptx" (33 slides). Matt's rules for
this packet, which override the guided-notes skill where they conflict:
  1. Follow the slides: same order, same content, blanks taken from the slide wording.
  2. Every slide example gets a work box directly below the fill-in content it belongs to.
  3. Every block is labelled with the slide range it covers.

Consequences, deliberate:
  - Sections appear in DECK order, not numeric order: S05.2 (slides 10-11) comes before S05.1
    (slides 12-16) because the deck puts "What Is VSEPR" before "Drawing Lewis Structures".
  - No RECALL blocks and no Concept Review page: both would add content that is not on a slide.
  - No equation toolbox ("noEquationBar"): the only candidate lines are the slide 6 cutoffs and
    the slide 12 electron rules, which are blanks the student fills in. A toolbox on the cover
    would print the answers.
  - No difficulty ratings: DECISIONS.md has none for U4/U5 and they are never invented.
  - 4.4 Metallic is skipped this year (Matt, 2026-11-04). 5.6 is left out.

Edit this file, not the JSON it writes.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STEM = "chem_u04-u05_notes"

# --------------------------------------------------------------------------------------------
# Slide content the text extraction could not read. Slides 9, 19 and 32 carry their main
# content as a picture or table that did not come out of slide_text.txt. Fill these from the
# rendered Astra slide before building. Until both are filled the generator writes nothing,
# so a guessed table can never reach a student page.
#
# SLIDE_09 is filled from the ORIGINAL deck's slide 11 ("Bond Types at a Glance"), which the
# Astra slide 9 notes name as its source. Confirm against the rendered Astra slide 9.
# --------------------------------------------------------------------------------------------
SLIDE_09 = {   # Astra slide 9, as rendered: bond type given, the rest filled in
    "headers": ["Bond type", "Electron behavior", "Class ΔEN guide"],
    "rows": [["Nonpolar covalent", "", ""], ["Polar covalent", "", ""], ["Ionic", "", ""]],
    "_key": [["Nonpolar covalent", "Nearly equal sharing", "< 0.40"],
             ["Polar covalent", "Unequal sharing; δ+ and δ−", "0.40–1.80"],
             ["Ionic", "Opposite ions attract", "> 1.80"]],
    "widths": [0.3, 0.42, 0.28], "rowHeightIn": 0.34,
}

# Slide 19, "Common Molecular Shapes". Fill with the slide's own table:
#   {"headers": [...], "rows": [[...blank cells...]], "_key": [[...]], "widths": [...],
#    "rowHeightIn": 0.32}
SLIDE_19 = {
    "headers": ["Groups", "Lone pairs on center", "Molecular shape", "Example"],
    "rows": [["2", "0", "", ""], ["3", "0", "", ""], ["4", "0", "", ""], ["4", "1", "", ""], ["4", "2", "", ""]],
    "_key": [["2", "0", "Linear • 180°", "CO₂"], ["3", "0", "Trigonal planar • 120°", "BF₃, CH₂O"],
             ["4", "0", "Tetrahedral • 109.5°", "CH₄, CCl₄"], ["4", "1", "Trigonal pyramidal • ≈107°", "NH₃"],
             ["4", "2", "Bent • ≈104.5°", "H₂O"]],
    "widths": [0.14, 0.24, 0.38, 0.24], "rowHeightIn": 0.32,
}

# Slide 32, "Identifying Intermolecular Forces". Fill with the slide's molecules, in slide
# order, and the IMFs the slide gives each, e.g. [("HCl", "Dispersion, dipole–dipole"), ...].
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


def P(prompt, answer, lines=1):
    """A prompt with a writing line; `answer` is what the key prints in the line's place."""
    d = {"prompt": prompt, "answer": answer}
    if lines != 1:
        d["lines"] = lines
    return d


def box(given, find, answer_blank, answer_key, solution, height=2.0, label=None):
    d = {"given": given, "find": find, "answer": answer_blank, "_answerKey": answer_key,
         "solution": solution, "workHeightIn": height}
    if label:
        d["workLabel"] = label
    return d


DRAW = "Draw it as shown on the slide"
DRAW_DIPOLE = "Draw it as shown on the slide, with dipole arrows"

spec = {
  "course": "chemistry",
  # The builder holds one unit per packet. 4 puts "CHEMICAL BONDING" on the cover and
  # "UNIT 04" in every footer, including the U5 pages. Section bars still read U05 / S05.x.
  # This is a template gap, reported; it is not worked around here.
  "unit": 4,
  "key": False,
  "noEquationBar": True,
  "cover": {
    "sections": [{"code": c} for c in
                 ("4.1", "4.2", "4.3", "4.5", "4.6", "5.2", "5.1", "5.3", "5.4", "5.5")],
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
    "howToUse": ("Every block names the slides it covers, so you can match this page to the "
                 "screen. Fill in each blank with the slide's wording while that slide is up. "
                 "When the slide works an example, copy it into the box under the notes, "
                 "including dipole arrows where the slide shows them."),
  },
  "sectionsContent": [
    # ---------------------------------------------------------------- 4.1, slides 1-3
    {"code": "4.1", "title": "Why Atoms Bond",
     "learningTarget": "I can define a chemical bond and state the octet rule.",
     "pages": [{"rows": [
       {"title": "Slides 1–2 · Unit overview",
        "cues": ["Three ideas for this unit"],
        "notes": [P("01 Bonding: electrons are", "transferred or shared"),
                  P("02 Molecular structure: the way", "the atoms are arranged"),
                  P("03 Intermolecular forces: the way", "separate molecules attract each other"),
                  P("The unit in one line: draw the electrons →",
                    "find the shape → explain the properties")]},
       {"title": "Slide 3 · Why atoms bond",
        "cues": ["Definition: chemical bond", "The octet rule"],
        "notes": [P("Atoms bond when the bonded arrangement has", "lower energy"),
                  P("Chemical bond:", "an attraction that holds atoms or ions together."),
                  P("The octet rule: many atoms bond with", "8 outer electrons around them"),
                  P("Hydrogen needs only", "2"),
                  P("Neon:", "8 outer electrons"),
                  P("The octet rule is a", "guide. Some atoms are exceptions.")]},
     ]}]},
    # ---------------------------------------------------------------- 4.2, slide 4
    {"code": "4.2", "title": "Ionic Bonding",
     "learningTarget": "I can describe ionic bonding as electron transfer between a metal and a nonmetal.",
     "pages": [{"rows": [
       {"title": "Slide 4 · Ionic bonding",
        "cues": ["The bonding partners", "The electron transfer", "Properties"],
        "notes": [P("Ionic bonding: electrons", "transfer. Opposite ions attract."),
                  P("The bonding partners: usually", "a metal and a nonmetal"),
                  P("Na", "loses an electron → Na+"),
                  P("Cl", "gains an electron → Cl−"),
                  P("Property:", "hard and brittle"),
                  P("Property:", "high melting points"),
                  P("Ions form a", "repeating crystal"),
                  P("Conducts when", "molten or dissolved, but not as a solid")]},
       {"kind": "example", "title": "Slide 4 · Example: Na and Cl",
        "cues": ["Electron transfer"],
        "problem": box("Sodium (Na) and chlorine (Cl).",
                       "the electron transfer and the two ions it makes.",
                       "Ions formed: ________ and ________",
                       "Ions formed: Na+ and Cl−",
                       ["Na loses one electron → Na+",
                        "Cl gains that electron → Cl−",
                        "The opposite ions attract."],
                       height=1.6, label=DRAW),
        "notes": []},
     ]}]},
    # ---------------------------------------------------------------- 4.3, slide 5
    {"code": "4.3", "title": "Covalent Bonding",
     "learningTarget": "I can describe covalent bonding as atoms sharing pairs of electrons.",
     "pages": [{"rows": [
       {"title": "Slide 5 · Covalent bonding",
        "cues": ["The bonding partners", "One bond", "Properties", "The exception"],
        "notes": [P("Covalent bonding: atoms", "share pairs of electrons"),
                  P("The bonding partners: usually", "nonmetals"),
                  P("One shared pair makes", "one bond"),
                  P("Property:", "often low melting points"),
                  P("Property:", "gases, liquids, or soft solids"),
                  P("Property:", "usually poor conductors"),
                  P("Exception:", "network solids such as diamond have strong bonds throughout.")]},
     ]}]},
    # ---------------------------------------------------------------- 4.5, slides 6-7
    {"code": "4.5", "title": "Electronegativity & Bond Type",
     "learningTarget": "I can use the EN difference to classify a bond as nonpolar covalent, polar covalent, or ionic.",
     "pages": [{"rows": [
       {"title": "Slide 6 · Electronegativity",
        "cues": ["Definition: electronegativity", "The ΔEN rule"],
        "notes": [P("Electronegativity (EN):", "how strongly an atom pulls on shared electrons."),
                  P("ΔEN =", "higher EN − lower EN")]},
       {"title": "Slide 6 · Bond type from ΔEN",
        "cues": ["The three bond types and their cutoffs"],
        "noWorkBox": True,
        "table": {"headers": ["Bond type", "ΔEN", "Sharing"],
                  "widths": [0.34, 0.26, 0.40], "rowHeightIn": 0.34,
                  "rows": [["Nonpolar covalent", "", ""], ["Polar covalent", "", ""],
                           ["Ionic", "", ""]],
                  "_key": [["Nonpolar covalent", "Under 0.40", "Nearly equal sharing"],
                           ["Polar covalent", "0.40–1.80", "Unequal sharing"],
                           ["Ionic", "Over 1.80", "Opposite ions attract"]]},
        "notes": [P("These cutoffs are class", "guidelines, not sharp boundaries.")]},
       {"kind": "example", "title": "Slide 7 · Example: classifying bonds",
        "cues": ["Subtract the EN values", "Match the difference to a bond type"],
        "problem": box(["C–H: C 2.55, H 2.20", "C–O: O 3.44, C 2.55", "Na–Cl: Cl 3.16, Na 0.93"],
                       "ΔEN and bond type for each bond.",
                       "C–H ____________   C–O ____________   Na–Cl ____________",
                       "C–H nonpolar covalent   C–O polar covalent   Na–Cl ionic",
                       ["C–H: 2.55 − 2.20 = 0.35; 0.35 < 0.40 → nonpolar covalent",
                        "C–O: 3.44 − 2.55 = 0.89; 0.40 ≤ 0.89 ≤ 1.80 → polar covalent",
                        "Na–Cl: 3.16 − 0.93 = 2.23; 2.23 > 1.80 → ionic"],
                       height=1.6, label="Show the subtraction for each bond"),
        "notes": [P("Bigger EN difference =", "more uneven electron sharing")]},
     ]}]},
    # ---------------------------------------------------------------- 4.6, slides 8-9
    {"code": "4.6", "title": "Bond Polarity",
     "learningTarget": "I can draw a dipole arrow on a polar bond and label its δ+ and δ− ends.",
     "pages": [{"rows": [
       {"title": "Slide 8 · Bond polarity and dipole arrows",
        "cues": ["Nonpolar bond", "Polar bond", "Reading δ+ and δ−"],
        "notes": [P("The dipole arrow points toward", "the atom pulling harder"),
                  P("Nonpolar bond:", "equal or nearly equal sharing"),
                  P("Nonpolar examples:", "H–H, Cl–Cl, C–H"),
                  P("Polar bond:", "unequal sharing: electrons stay closer to the higher-EN atom"),
                  P("Polar examples:", "H–Cl, O–H, C–O"),
                  P("δ− =", "partly negative"),
                  P("δ+ =", "partly positive (crossed end of the arrow)")]},
       {"kind": "example", "title": "Slide 8 · Example: H–H and H–Cl",
        "cues": ["Dipole arrow on a polar bond"],
        "problem": box("H–H (nonpolar) and H–Cl (polar), as drawn on slide 8.",
                       "each bond, with the dipole arrow and δ+ / δ− on the polar one.",
                       "", "",
                       ["H–H: no arrow; equal sharing.",
                        "H–Cl: arrow points toward Cl; crossed end at H. H is δ+, Cl is δ−."],
                       height=1.5, label=DRAW_DIPOLE),
        "notes": []},
      ]},
      {"rows": [
       {"title": "Slide 9 · Bond types at a glance",
        "cues": ["Compare how the electrons are shared or transferred"],
        "noWorkBox": True,
        "table": SLIDE_09,
        "notes": [P("Ionic: usually", "metal + nonmetal"),
                  P("Covalent: usually", "nonmetal + nonmetal")]},
     ]}]},
    # ---------------------------------------------------------------- 5.2, slides 10-11
    {"code": "5.2", "title": "VSEPR Theory",
     "learningTarget": "I can state the VSEPR idea: electron groups repel and spread out around the central atom.",
     "pages": [{"rows": [
       {"title": "Slides 10–11 · VSEPR theory",
        "cues": ["The VSEPR sequence", "The name, spelled out", "The idea"],
        "notes": [P("Lewis structure →", "electron groups → 3D shape"),
                  P("VSEPR =", "Valence Shell Electron Pair Repulsion"),
                  P("The idea: electron groups", "repel each other"),
                  P("They spread out around the central atom", "as far as possible"),
                  P("Lewis structures come first. They show", "bonds and lone pairs"),
                  P("Count the groups to", "predict shape"),
                  P("4 bonds, no lone pairs →", "tetrahedral")]},
     ]}]},
    # ---------------------------------------------------------------- 5.1, slides 12-16
    {"code": "5.1", "title": "Lewis Electron Structures",
     "learningTarget": "I can draw a Lewis structure by counting, connecting, filling, and checking electrons.",
     "pages": [
      {"rows": [
       {"title": "Slide 12 · Drawing Lewis structures",
        "cues": ["The four steps, in order"],
        "noWorkBox": True,
        "table": {"headers": ["Step", "What to do"],
                  "widths": [0.18, 0.82], "rowHeightIn": 0.52,
                  "rows": [["1  Count", ""], ["2  Connect", ""], ["3  Fill", ""],
                           ["4  Check", ""]],
                  "_key": [["1  Count", "Add valence electrons. − charge: add electrons. + charge: subtract electrons."],
                           ["2  Connect", "Center: usually lowest EN. Never put H in the center. Add single bonds."],
                           ["3  Fill", "Fill outer atoms first. H: 2; usually 8 for others. Put leftovers on the center."],
                           ["4  Check", "Total and shells correct. If not: recount electrons, check octet exceptions, and turn lone pairs into double or triple bonds if needed. Then check again."]]},
        "notes": [P("Bond line =", "2 shared electrons"),
                  P("Lone pair =", "2 unshared electrons")]},
       {"kind": "example", "title": "Slide 13 · Example: BF₃",
        "cues": ["Boron trifluoride", "Count, connect, fill and check"],
        "problem": box("BF₃, boron trifluoride.", "the Lewis structure.",
                       "Valence electrons = ________",
                       "Valence electrons = 3 + 3(7) = 24",
                       ["Count: 3 + 3(7) = 24", "Connect: three B–F bonds use 6 electrons.",
                        "Fill: each F gets 3 lone pairs, 18 electrons.",
                        "Check: 6 bonding + 18 lone-pair electrons = 24."],
                       height=2.0, label=DRAW),
        "notes": [P("B has 6 electrons:", "an octet exception")]},
      ]},
      {"rows": [
       {"kind": "example", "title": "Slide 14 · Example: CO₂",
        "cues": ["Carbon dioxide"],
        "problem": box("CO₂, carbon dioxide.", "the Lewis structure.",
                       "Valence electrons = ________",
                       "Valence electrons = 4 + 2(6) = 16",
                       ["Count: 4 + 2(6) = 16", "Connect: O–C–O uses 4 electrons.",
                        "Fill: the remaining 12 go on the oxygens. Carbon still has only 4.",
                        "Fix: share one lone pair from each O → O=C=O."],
                       height=2.0, label=DRAW),
        "notes": [P("O=C=O:", "8 bonding electrons + 8 lone-pair electrons = 16. All atoms have 8.")]},
       {"kind": "example", "title": "Slide 15 · Example: NH₃",
        "cues": ["Ammonia", "The leftover electrons"],
        "problem": box("NH₃, ammonia.", "the Lewis structure.",
                       "Valence electrons = ________",
                       "Valence electrons = 5 + 3(1) = 8",
                       ["Count: 5 + 3(1) = 8",
                        "Connect: three N–H bonds use 6 electrons. Each H now has 2.",
                        "Leftovers: 8 − 6 = 2. Both go on N as one lone pair."],
                       height=2.0, label=DRAW),
        "notes": [P("Check: N has", "8 electrons around it. Each H has 2. Total used = 8.")]},
      ]},
      {"rows": [
       {"kind": "example", "title": "Slide 16 · Example: CH₂O",
        "cues": ["Formaldehyde", "H gets 2; C and O get 8"],
        "problem": box("CH₂O, formaldehyde.", "the Lewis structure.",
                       "Valence electrons = ________",
                       "Valence electrons = 4 + 2(1) + 6 = 12",
                       ["Count: 4 + 2(1) + 6 = 12",
                        "Connect: three single bonds use 6 electrons.",
                        "Fill: put 6 electrons on O. Carbon has only 6.",
                        "Fix: share one O lone pair to make C=O."],
                       height=2.0, label=DRAW),
        "notes": [P("Electron total:", "C=O uses 4; two C–H bonds use 4; two O lone pairs use 4. Total: 12.")]},
      ]},
     ]},
    # ---------------------------------------------------------------- 5.3, slides 17-19
    {"code": "5.3", "title": "Molecular Geometry",
     "learningTarget": "I can use electron groups and lone pairs to predict a molecule's shape and bond angle.",
     "pages": [
      {"rows": [
       {"title": "Slide 17 · VSEPR: predicting shape",
        "cues": ["Bonding groups", "Lone pairs"],
        "notes": [P("Electron groups repel each other, so they", "spread out"),
                  P("A single, double, or triple bond counts as", "ONE electron group"),
                  P("Lone pairs also", "take up space"),
                  P("Lone pairs usually make bond angles", "smaller")]},
       {"title": "Slide 17 · Bond angles",
        "cues": ["Three molecules, same four electron groups"],
        "noWorkBox": True,
        "table": {"headers": ["Molecule", "Lone pairs on the center", "Bond angle"],
                  "widths": [0.28, 0.40, 0.32], "rowHeightIn": 0.34,
                  "rows": [["CH₄", "", ""], ["NH₃", "", ""], ["H₂O", "", ""]],
                  "_key": [["CH₄", "0", "109.5°"], ["NH₃", "1", "about 107°"],
                           ["H₂O", "2", "about 104.5°"]]},
        "notes": [P("VSEPR =", "Valence Shell Electron Pair Repulsion")]},
      ]},
      {"rows": [
       {"title": "Slide 18 · Octet rule exceptions",
        "cues": ["Count all bonding and lone-pair electrons around the atom",
                 "Fewer than 8", "More than 8", "Odd total"],
        "noWorkBox": True,
        "table": {"headers": ["", "Atom", "Electrons around it", "Example"],
                  "widths": [0.22, 0.16, 0.26, 0.36], "rowHeightIn": 0.30,
                  "rows": [["Fewer than 8", "H", "", ""], ["Fewer than 8", "Be", "", ""],
                           ["Fewer than 8", "B", "", ""], ["More than 8", "P", "", ""],
                           ["More than 8", "S", "", ""], ["More than 8", "Xe", "", ""]],
                  "_key": [["Fewer than 8", "H", "2", "H₂: one bond"],
                           ["Fewer than 8", "Be", "4", "BeCl₂: two bonds"],
                           ["Fewer than 8", "B", "6", "BF₃: three bonds"],
                           ["More than 8", "P", "10", "PCl₅: 5 bonds"],
                           ["More than 8", "S", "12", "SF₆: 6 bonds"],
                           ["More than 8", "Xe", "12", "XeF₄: 4 bonds + 2 lone pairs"]]},
        "notes": [P("Cl, Br, and I can also", "exceed 8 in some compounds"),
                  P("Odd total: NO has", "11 valence electrons total, so one electron stays unpaired"),
                  P("Period-2 atoms (including C, N, O, and F)", "cannot have more than 8")]},
       {"title": "Slide 19 · Common molecular shapes",
        "cues": ["Count electron groups", "Name the shape using the atoms"],
        "noWorkBox": True,
        "table": SLIDE_19,
        "notes": [P("Lone pairs change the shape. The shape name", "describes the atoms")]},
      ]},
     ]},
    # ---------------------------------------------------------------- 5.4, slides 20-26
    {"code": "5.4", "title": "Molecular Polarity",
     "learningTarget": "I can decide whether a molecule is polar by checking its bonds and its shape.",
     "pages": [
      {"rows": [
       {"title": "Slides 20–21 · Bond vs. molecular polarity",
        "cues": ["Bond polarity", "Molecular polarity"],
        "notes": [P("Polar molecules: how bond pulls and", "molecular shape work together"),
                  P("A molecule can contain polar bonds and", "still be nonpolar"),
                  P("Bond polarity, one bond: compare", "the atoms’ EN values"),
                  P("HCl: one polar bond →", "polar molecule"),
                  P("Molecular polarity, whole molecule: check that", "the bond pulls cancel"),
                  P("CO₂: equal opposite pulls →", "nonpolar"),
                  P("To find molecular polarity, check", "the bonds AND the shape")]},
       {"kind": "example", "title": "Slide 21 · Example: HCl and CO₂",
        "cues": ["One polar bond", "Two equal, opposite pulls"],
        "problem": box("HCl and CO₂, as drawn on slide 21.",
                       "each molecule with its dipole arrows, then polar or nonpolar.",
                       "HCl: ____________   CO₂: ____________",
                       "HCl: polar   CO₂: nonpolar",
                       ["H–Cl: arrow toward Cl, crossed end at H. H δ+, Cl δ−.",
                        "O=C=O: two arrows from C toward each O, equal and opposite, so they cancel."],
                       height=2.0, label=DRAW_DIPOLE),
        "notes": []},
      ]},
      {"rows": [
       {"title": "Slide 22 · Canceling bond dipoles",
        "cues": ["Balanced pulls", "Pulls that do not cancel"],
        "notes": [P("Bond pulls cancel when", "their directions balance"),
                  P("Balanced pulls → nonpolar:", "CO₂, BF₃, CH₄, CCl₄"),
                  P("Pulls do not cancel → polar:", "H₂O, NH₃, HCl, CH₃Cl"),
                  P("Before deciding, check", "the 3D shape and the outer atoms")]},
       {"kind": "example", "title": "Slide 22 · Example: BF₃ and NH₃",
        "cues": ["Balanced vs. unbalanced"],
        "problem": box("BF₃ and NH₃, as drawn on slide 22.",
                       "each molecule with its dipole arrows, then polar or nonpolar.",
                       "BF₃: ____________   NH₃: ____________",
                       "BF₃: nonpolar   NH₃: polar",
                       ["BF₃: three B–F arrows toward each F, spread evenly around B, cancel.",
                        "NH₃: three N–H arrows toward N; the pyramid leaves a net pull toward N."],
                       height=2.0, label=DRAW_DIPOLE),
        "notes": []},
      ]},
      {"rows": [
       {"kind": "example", "title": "Slide 23 · Example: H₂O",
        "cues": ["Draw it, check the bonds, then check the shape"],
        "problem": box("H₂O. EN: O 3.44, H 2.20.",
                       "Lewis structure, bond polarity, shape, and molecular polarity.",
                       "Electrons ______   ΔEN ______   Shape ____________   Molecule ________",
                       "Electrons 8   ΔEN 1.24   Shape bent   Molecule POLAR",
                       ["Lewis: 6 + 2(1) = 8. Two bonds and two O lone pairs.",
                        "Bonds: 3.44 − 2.20 = 1.24. Each O–H bond is polar.",
                        "Shape: bent. The bond pulls do not cancel."],
                       height=2.0, label=DRAW_DIPOLE),
        "notes": [P("Oxygen side:", "δ−. Hydrogen side: δ+.")]},
       {"kind": "example", "title": "Slide 24 · Example: NH₃",
        "cues": ["A lone pair changes the arrangement of the three N–H bonds"],
        "problem": box("NH₃. EN: N 3.04, H 2.20.",
                       "Lewis structure, bond polarity, shape, and molecular polarity.",
                       "Electrons ______   ΔEN ______   Shape ____________   Molecule ________",
                       "Electrons 8   ΔEN 0.84   Shape trigonal pyramidal   Molecule POLAR",
                       ["Lewis: 5 + 3(1) = 8. Three bonds and one N lone pair.",
                        "Bonds: 3.04 − 2.20 = 0.84. Each N–H bond is polar.",
                        "Shape: trigonal pyramidal. The pulls do not cancel."],
                       height=2.0, label=DRAW_DIPOLE),
        "notes": [P("NH₃ is a three-dimensional", "pyramid, not a flat triangle")]},
      ]},
      {"rows": [
       {"kind": "example", "title": "Slide 25 · Example: CCl₄",
        "cues": ["Four polar bonds can balance in three dimensions"],
        "problem": box("CCl₄. EN: Cl 3.16, C 2.55.",
                       "Lewis structure, bond polarity, shape, and molecular polarity.",
                       "Electrons ______   ΔEN ______   Shape ____________   Molecule ________",
                       "Electrons 32   ΔEN 0.61   Shape tetrahedral   Molecule NONPOLAR",
                       ["Lewis: 4 + 4(7) = 32. Four bonds; 3 lone pairs on each Cl.",
                        "Bonds: 3.16 − 2.55 = 0.61. Each C–Cl bond is polar.",
                        "Shape: tetrahedral. Four equal pulls cancel."],
                       height=2.0, label=DRAW_DIPOLE),
        "notes": [P("Solid wedge =", "toward you. Dashed wedge = away.")]},
       {"kind": "example", "title": "Slide 26 · Example: CCl₄ vs. CH₃Cl",
        "cues": ["Both have 4 bonds and no lone pairs on the central carbon"],
        "problem": box("CCl₄ and CH₃Cl, both tetrahedral.",
                       "each molecule with its dipole arrows and net pull, then polar or nonpolar.",
                       "CCl₄: ____________   CH₃Cl: ____________",
                       "CCl₄: NONPOLAR   CH₃Cl: POLAR",
                       ["CCl₄: four identical C–Cl pulls cancel.",
                        "CH₃Cl: the C–Cl pull is not balanced. Net pull toward Cl."],
                       height=2.0, label=DRAW_DIPOLE),
        "notes": [P("Shape alone does not decide polarity.", "The outer atoms matter.")]},
      ]},
     ]},
    # ---------------------------------------------------------------- 5.5, slides 27-32
    {"code": "5.5", "title": "Intermolecular Forces",
     "learningTarget": "I can name the intermolecular forces a molecule has and explain where each comes from.",
     "pages": [
      {"rows": [
       {"title": "Slides 27–28 · Intermolecular forces",
        "cues": ["The three IMFs", "Inside vs. between molecules"],
        "notes": [P("The three IMFs:", "hydrogen bonding, dipole–dipole, London dispersion"),
                  P("Intermolecular forces: attractions", "between separate molecules"),
                  P("Inside a molecule: covalent bonds connect its atoms. These are",
                    "intramolecular bonds"),
                  P("Between molecules: intermolecular forces (IMFs)",
                    "attract one molecule to another"),
                  P("Boiling water separates H₂O molecules; it does not",
                    "break their O–H bonds")]},
       {"title": "Slide 29 · Hydrogen bonding",
        "cues": ["Look for", "In the picture", "Examples"],
        "notes": [P("Hydrogen bonding: a partly positive H attracts",
                    "a lone pair on a nearby N, O, or F"),
                  P("Look for: H bonded directly to", "N, O, or F"),
                  P("In the picture: Hδ+ in one water molecule attracts", "Oδ− in another"),
                  P("Examples:", "H₂O, NH₃, HF"),
                  P("Helps raise water’s boiling point and", "hold DNA strands together"),
                  P("Strength:", "often strong for similar-sized molecules; not always strongest")]},
      ]},
      {"rows": [
       {"title": "Slide 30 · Dipole–dipole forces",
        "cues": ["Look for", "In the picture", "Examples"],
        "notes": [P("Dipole–dipole: polar molecules attract through",
                    "their opposite partial charges"),
                  P("Look for:", "polar molecules with δ+ and δ− ends"),
                  P("In the picture: Clδ− on one HCl molecule attracts", "Hδ+ on another"),
                  P("Examples:", "HCl, CH₃Cl, SO₂. All also have dispersion."),
                  P("These partial charges are", "lasting features of each polar molecule")]},
       {"title": "Slide 31 · London dispersion forces",
        "cues": ["The molecules that have them", "The electron shift", "The strength factor"],
        "notes": [P("London dispersion: moving electrons create",
                    "temporary positive and negative ends"),
                  P("Found in:", "every atom and molecule"),
                  P("Main attraction for", "nonpolar molecules"),
                  P("Electrons shift →", "a brief dipole. The neighboring cloud shifts too."),
                  P("Stronger with", "larger, easier-to-shift clouds"),
                  P("Example:", "I₂ is solid at room temperature."),
                  P("The picture shows", "changing charge, not permanent charged atoms")]},
      ]},
      {"rows": [
       {"kind": "example", "title": "Slide 32 · Practice: identifying IMFs",
        "cues": ["Every molecule has dispersion", "Check what else it has"],
        "problem": box(["Molecules from slide 32: " + ", ".join(m for m, _ in SLIDE_32) + "."],
                       "the IMFs each molecule has.",
                       "", "",
                       [f"{m}: {imf}" for m, imf in SLIDE_32],
                       height=2.4, label="Sketch each molecule and list its IMFs"),
        "notes": [P("Every molecule has", "dispersion. Check what else it has."),
                  P("Stronger attractions usually mean",
                    "a higher boiling point. Size and shape matter too.")]},
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
            lines = list(row.get("cues", []))
            lines += [n if isinstance(n, str) else n.get("prompt", n.get("text", ""))
                      for n in row.get("notes", [])]
            for t in lines:
                if QUESTION_MARK.search(t) or OPENER.match(t.lstrip("*")):
                    bad.append((sec["code"], t))
if bad:
    sys.exit("make_chem_u04-u05_notes: questions in the recall columns: " + repr(bad))

student = strip_answers(spec)
key = fill_answers(spec)
key["key"] = True
for name, data in (("student", student), ("key", key)):
    with open(os.path.join(HERE, f"{STEM}_{name}.json"), "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
print("wrote", STEM + "_student.json and", STEM + "_key.json")
