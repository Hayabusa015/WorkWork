#!/usr/bin/env python3
"""Chemistry U6 naming practice sets: 6.1 molecular, 6.3 ionic, 6.4 acids.

    python3 templates/worksheet/specs/make_chem_u06_naming.py

Writes chem_u06_s06.1_molecular_naming.json, chem_u06_s06.3_ionic_naming.json and
chem_u06_s06.4_acid_naming.json beside this file. Each sheet is two pages: front name -> formula,
back formula -> name. Each side is a worked example row, five guided rows with one column per
step, then five on-your-own rows. Matt's design, 2026-11-21: "The first 5 of each section, I want
a area where they have to write the cation and the anion, emphasizing the cation first, record
the charges, than a step to show criss crossing ... Than the next 5 just give the name or formula."

Every answer is in the rows; `blankCols` blanks them on the student copy and the key prints them.
Charges are written ^{2+} so the run is set superscript (Archivo has no U+207A/B glyphs).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))


def tbl(label, headers, widths, rows, blank, height, points=None, **kw):
    b = {"kind": "table", "label": label, "headers": headers, "widths": widths, "rows": rows,
         "rowHeightIn": height, "bodySize": 9.5, "boldFirst": False}
    if blank is not None:
        b["blankCols"] = blank
    if points:
        b["points"] = points
    b.update(kw)
    return b


def side(part, title_ex, headers, widths, ex, guided, own_heads, own, first, gh=0.58):
    """One side of the sheet: worked example, five guided rows, five on-your-own rows."""
    n = len(headers)
    blocks = [
        tbl(f"{part} · WORKED EXAMPLE", headers, widths, [ex], [], 0.30),
        tbl(f"{part} · GUIDED · FILL IN EVERY STEP", headers, widths, guided, list(range(2, n)), gh,
            points=len(guided)),
        tbl(f"{part} · ON YOUR OWN", ["#"] + own_heads, [0.06, 0.40, 0.54], own, [2], 0.40,
            points=len(own), gapBefore=8),
    ]
    if not first:
        for b in blocks:   # the page heading already names the part
            b["label"] = b["label"].split(" · ", 1)[1].split(" · ", 1)[1] if b["label"].count(" · ") >= 2 else b["label"]
        blocks[0]["pageBreakBefore"] = True
        blocks[0]["heading"] = title_ex
    return blocks


def spec(code, title, concept, directions, blocks, notes):
    return {
        "course": "chemistry", "unit": 6, "sections": [code], "docType": "Practice_Set",
        "timeTargetMin": "30", "pagesPerSection": 2,
        "sectionsContent": [{
            "code": code, "title": title, "concept": {"summary": concept, "keyIdeas": []},
            "directions": directions, "questions": [], "blocks": blocks, "keyNotes": notes}],
    }


# ---------------------------------------------------------------- 6.1 molecular
MA = ["#", "Name", "1 · 1st element (symbol)", "Prefix → #", "2 · 2nd element (symbol)", "Prefix → #", "3 · Formula"]
MAW = [0.05, 0.25, 0.13, 0.13, 0.13, 0.13, 0.18]
MB = ["#", "Formula", "1 · 1st element (name)", "# → prefix", "2 · 2nd element (root + -ide)", "# → prefix", "3 · Name"]
MBW = [0.05, 0.12, 0.15, 0.12, 0.17, 0.12, 0.27]
molecular = spec(
    "6.1", "Molecular Naming",
    "Two nonmetals · prefixes count the atoms · no mono- on the first element · second element ends in -ide · never reduce",
    "Front: split each name into its two elements and turn each prefix into a number; the numbers are the "
    "subscripts. Back: count the atoms and turn each count into a prefix. Fill in every column on the guided rows.",
    side("PART A · NAME → FORMULA", None, MA, MAW,
         ["EX", "carbon dioxide", "C", "none → 1", "O", "di- → 2", "CO₂"],
         [["1", "carbon monoxide", "C", "none → 1", "O", "mono- → 1", "CO"],
          ["2", "sulfur trioxide", "S", "none → 1", "O", "tri- → 3", "SO₃"],
          ["3", "dinitrogen trioxide", "N", "di- → 2", "O", "tri- → 3", "N₂O₃"],
          ["4", "phosphorus pentachloride", "P", "none → 1", "Cl", "penta- → 5", "PCl₅"],
          ["5", "carbon tetrachloride", "C", "none → 1", "Cl", "tetra- → 4", "CCl₄"]],
         ["Name", "Formula"],
         [["6", "nitrogen triiodide", "NI₃"], ["7", "diphosphorus pentoxide", "P₂O₅"],
          ["8", "dinitrogen monoxide", "N₂O"], ["9", "silicon dioxide", "SiO₂"],
          ["10", "tetraphosphorus decoxide", "P₄O₁₀"]], True)
    + side("PART B · FORMULA → NAME", "Part B · Formula → Name", MB, MBW,
           ["EX", "CBr₄", "carbon", "1 → none", "bromide", "4 → tetra-", "carbon tetrabromide"],
           [["1", "SO₂", "sulfur", "1 → none", "oxide", "2 → di-", "sulfur dioxide"],
            ["2", "PBr₃", "phosphorus", "1 → none", "bromide", "3 → tri-", "phosphorus tribromide"],
            ["3", "Cl₂O₇", "chlorine", "2 → di-", "oxide", "7 → hepta-", "dichlorine heptoxide"],
            ["4", "SiF₄", "silicon", "1 → none", "fluoride", "4 → tetra-", "silicon tetrafluoride"],
            ["5", "S₂Cl₂", "sulfur", "2 → di-", "chloride", "2 → di-", "disulfur dichloride"]],
           ["Formula", "Name"],
           [["6", "NO", "nitrogen monoxide"], ["7", "CS₂", "carbon disulfide"],
            ["8", "P₄S₃", "tetraphosphorus trisulfide"], ["9", "XeF₆", "xenon hexafluoride"],
            ["10", "BCl₃", "boron trichloride"]], False, gh=0.74),
    ["Prefix drops its final a or o before oxide: heptoxide, decoxide, monoxide.",
     "Molecular formulas are never reduced: N₂O₄ is not NO₂ (deck slide 12)."])

# ---------------------------------------------------------------- 6.3 ionic
IA = ["#", "Name", "1 · Cation (write first)", "Charge", "2 · Anion", "Charge", "3 · Criss-cross ( ) if 2 or more polyatomic ions", "4 · Charges cancel? show the math", "5 · Formula"]
IAW = [0.05, 0.19, 0.10, 0.07, 0.09, 0.07, 0.15, 0.15, 0.13]
IB = ["#", "Formula", "1 · Cation (write first)", "2 · Anion", "Anion charge", "3 · Un-cross: cation charge", "4 · Charges cancel? show the math", "5 · Name"]
IBW = [0.05, 0.12, 0.10, 0.09, 0.09, 0.12, 0.17, 0.26]
ionic = spec(
    "6.3", "Ionic Naming",
    "Cation first · charges add to zero · Roman numeral = charge on one metal ion · polyatomic ions stay whole; use ( ) for 2 or more",
    "Front: write the cation first, record both charges, criss-cross the charge numbers, prove the charges "
    "cancel, then write the formula (reduce if needed). Back: un-cross to find the cation's charge, prove the "
    "charges cancel, then name it. Use your reference packet for polyatomic ions.",
    side("PART A · NAME → FORMULA", None, IA, IAW,
         ["EX", "barium chloride", "Ba", "2+", "Cl", "1−", "Ba₁Cl₂", "(+2) + 2(−1) = 0", "BaCl₂"],
         [["1", "sodium chloride", "Na", "1+", "Cl", "1−", "Na₁Cl₁", "(+1) + (−1) = 0", "NaCl"],
          ["2", "calcium oxide", "Ca", "2+", "O", "2−", "Ca₂O₂ → reduce", "(+2) + (−2) = 0", "CaO"],
          ["3", "aluminum sulfide", "Al", "3+", "S", "2−", "Al₂S₃", "2(+3) + 3(−2) = 0", "Al₂S₃"],
          ["4", "iron(III) oxide", "Fe", "3+", "O", "2−", "Fe₂O₃", "2(+3) + 3(−2) = 0", "Fe₂O₃"],
          ["5", "magnesium nitrate", "Mg", "2+", "NO₃", "1−", "Mg₁(NO₃)₂", "(+2) + 2(−1) = 0", "Mg(NO₃)₂"]],
         ["Name", "Formula"],
         [["6", "potassium oxide", "K₂O"], ["7", "copper(II) chloride", "CuCl₂"],
          ["8", "ammonium phosphate", "(NH₄)₃PO₄"], ["9", "lead(IV) oxide", "PbO₂"],
          ["10", "aluminum hydroxide", "Al(OH)₃"]], True)
    + side("PART B · FORMULA → NAME", "Part B · Formula → Name", IB, IBW,
           ["EX", "CoCl₂", "Co", "Cl", "1−", "2+", "(+2) + 2(−1) = 0", "cobalt(II) chloride"],
           [["1", "KBr", "K", "Br", "1−", "1+", "(+1) + (−1) = 0", "potassium bromide"],
            ["2", "Li₂S", "Li", "S", "2−", "1+", "2(+1) + (−2) = 0", "lithium sulfide"],
            ["3", "FeCl₂", "Fe", "Cl", "1−", "2+", "(+2) + 2(−1) = 0", "iron(II) chloride"],
            ["4", "Cr₂O₃", "Cr", "O", "2−", "3+", "2(+3) + 3(−2) = 0", "chromium(III) oxide"],
            ["5", "Ca(OH)₂", "Ca", "OH", "1−", "2+", "(+2) + 2(−1) = 0", "calcium hydroxide"]],
           ["Formula", "Name"],
           [["6", "AlCl₃", "aluminum chloride"], ["7", "CuSO₄", "copper(II) sulfate"],
            ["8", "NH₄NO₃", "ammonium nitrate"], ["9", "SnF₄", "tin(IV) fluoride"],
            ["10", "BaCO₃", "barium carbonate"]], False, gh=0.74),
    ["A2 calcium oxide is the guided reduction (Ca₂O₂ → CaO); A9 lead(IV) oxide repeats it on their own (Pb₂O₄ → PbO₂).",
     "A8 and B8: the ammonium cation is polyatomic and has no metal.",
     "B4 and B9 need the un-cross: 3 O^{2−} is −6 across 2 Cr, so each Cr is +3; 4 F^{−} makes Sn +4."])

# ---------------------------------------------------------------- 6.4 acids
AA = ["#", "Acid name", "1 · Ending: acid → anion", "2 · Anion name", "3 · Anion formula + charge", "4 · Criss-cross with H^{+}", "5 · Charges cancel?", "6 · Formula"]
AAW = [0.05, 0.15, 0.13, 0.11, 0.12, 0.13, 0.17, 0.14]
AB = ["#", "Formula", "1 · H^{+} count", "2 · Anion formula + charge", "3 · Charges cancel?", "4 · Anion name", "5 · Ending: anion → acid", "6 · Acid name"]
ABW = [0.05, 0.13, 0.07, 0.12, 0.17, 0.14, 0.14, 0.18]
acids = spec(
    "6.4", "Acid Naming",
    "-ide → hydro-…-ic · -ate → -ic · -ite → -ous · one H^{+} per negative charge · keep per- and hypo-",
    "Front: translate the acid ending back to the anion ending, name the anion, write its formula and charge, "
    "criss-cross with H^{+}, prove the charges cancel, then write the formula with (aq). Back: count the H^{+} to "
    "find the anion's charge, name the anion, translate its ending, then name the acid.",
    side("PART A · ACID NAME → FORMULA", None, AA, AAW,
         ["EX", "sulfuric acid", "-ic → -ate", "sulfate", "SO₄^{2−}", "H₂(SO₄)₁", "2(+1) + (−2) = 0", "H₂SO₄(aq)"],
         [["1", "hydrochloric acid", "hydro-…-ic → -ide", "chloride", "Cl^{−}", "H₁Cl₁", "(+1) + (−1) = 0", "HCl(aq)"],
          ["2", "nitric acid", "-ic → -ate", "nitrate", "NO₃^{−}", "H₁(NO₃)₁", "(+1) + (−1) = 0", "HNO₃(aq)"],
          ["3", "hydrofluoric acid", "hydro-…-ic → -ide", "fluoride", "F^{−}", "H₁F₁", "(+1) + (−1) = 0", "HF(aq)"],
          ["4", "phosphoric acid", "-ic → -ate", "phosphate", "PO₄^{3−}", "H₃(PO₄)₁", "3(+1) + (−3) = 0", "H₃PO₄(aq)"],
          ["5", "sulfurous acid", "-ous → -ite", "sulfite", "SO₃^{2−}", "H₂(SO₃)₁", "2(+1) + (−2) = 0", "H₂SO₃(aq)"]],
         ["Acid name", "Formula"],
         [["6", "nitrous acid", "HNO₂(aq)"], ["7", "hydrobromic acid", "HBr(aq)"],
          ["8", "chromic acid", "H₂CrO₄(aq)"], ["9", "hydrocyanic acid", "HCN(aq)"],
          ["10", "chlorous acid", "HClO₂(aq)"]], True, gh=0.52)
    + side("PART B · FORMULA → ACID NAME", "Part B · Formula → Acid Name", AB, ABW,
           ["EX", "H₂CO₃(aq)", "2", "CO₃^{2−}", "2(+1) + (−2) = 0", "carbonate", "-ate → -ic", "carbonic acid"],
           [["1", "HI(aq)", "1", "I^{−}", "(+1) + (−1) = 0", "iodide", "-ide → hydro-…-ic", "hydroiodic acid"],
            ["2", "HClO₃(aq)", "1", "ClO₃^{−}", "(+1) + (−1) = 0", "chlorate", "-ate → -ic", "chloric acid"],
            ["3", "H₂S(aq)", "2", "S^{2−}", "2(+1) + (−2) = 0", "sulfide", "-ide → hydro-…-ic", "hydrosulfuric acid"],
            ["4", "HClO(aq)", "1", "ClO^{−}", "(+1) + (−1) = 0", "hypochlorite", "-ite → -ous", "hypochlorous acid"],
            ["5", "HMnO₄(aq)", "1", "MnO₄^{−}", "(+1) + (−1) = 0", "permanganate", "-ate → -ic", "permanganic acid"]],
           ["Formula", "Acid name"],
           [["6", "HClO₄(aq)", "perchloric acid"], ["7", "HC₂H₃O₂(aq)", "acetic acid"],
            ["8", "H₂Se(aq)", "hydroselenic acid"], ["9", "H₃PO₃(aq)", "phosphorous acid"],
            ["10", "H₂Cr₂O₇(aq)", "dichromic acid"]], False, gh=0.70),
    ["Phosphite and dichromate are reference-only (unstarred) in the packet; chromate and permanganate are starred.",
     "B8 H₂Se: selenide is not in the packet; students reason from S^{2−} (same group, 2−).",
     "A9 / HCN: cyanide has no oxygen, so the acid takes hydro-."])

for name, s in (("chem_u06_s06.1_molecular_naming", molecular), ("chem_u06_s06.3_ionic_naming", ionic),
                ("chem_u06_s06.4_acid_naming", acids)):
    with open(os.path.join(HERE, name + ".json"), "w") as f:
        json.dump(s, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("wrote", name + ".json")
