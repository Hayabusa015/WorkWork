# Chemistry: Ohio Learning Standards code verification (primary source)

Prepared by: researcher | Date: 2026-11-23 | Status: RECOMMENDATIONS ONLY. Nothing in `brand/`,
`standards/`, `governance/`, `courses/` or `templates/` was edited. This file replaces the earlier
secondary-source draft of the same name, which said every code was UNVERIFIED.

**Primary source used:** the PDF Matt uploaded, `SciFinalStandardsMC060719.pdf` (387 pp.). I read it
through a text extraction and checked pp. 1, 259, 270 and 284 visually. **PDF page number = printed
page number** (checked on p. 259 and p. 284). Every page cited below is that number.

Verdict key: **CONFIRMED** = matches the official text. **WRONG** = contradicted by the official
text (a correction is given). **NONE** = no Chemistry content statement covers the item.
"VIP" = Visions into Practice classroom examples. The document itself says they "are suggestions and
are not mandatory" (p. 270 and others). VIP support is weaker than support from the content
statement or its elaboration, and it is labelled VIP below.

## 0. Bottom line

| # | Finding | Verdict |
|---|---|---|
| 1 | The scheme is real: 9 Chemistry content statements, C.PM.1–C.PM.6 and C.IM.1–C.IM.3, in two strands (p. 259) | CONFIRMED |
| 2 | U6 spec codes C.PM.2, C.PM.3, C.PM.4 and C.IM.1 all exist with the titles given | CONFIRMED |
| 3 | U6 spec, 6.2 Polyatomic Ions, has main = C.PM.3. Polyatomic ions are in **C.PM.4** (p. 270, p. 271), and nowhere in C.PM.3 (pp. 266–269) | **WRONG** |
| 4 | U6 spec key for C.PM.3 ends "polyatomic ions" | **WRONG** |
| 5 | U6 spec `standards_source` "Ohio Learning Standards for Science (2018)" leaves out "Ohio's" | **WRONG** (minor) |
| 6 | Science inquiry has **no citable code** at high school | CONFIRMED (no code exists) |
| 7 | U15 Nuclear Chemistry: no Chemistry content statement. Nuclear content is in Physical Science PS.M.5 and Physics P.E.5 | NONE |

## 1. Official document name (for the source line)

| Item | Official text | Page | Verdict |
|---|---|---|---|
| Cover title | "Ohio's Learning Standards and Model Curriculum" / "Science" / "STANDARDS ADOPTED FEBRUARY 2018" / "MODEL CURRICULUM ADOPTED MAY 2019" | 1 | CONFIRMED |
| Front-matter running head | "OHIO'S LEARNING STANDARDS AND MODEL CURRICULUM \| SCIENCE \| ADOPTED 2018-2019" | 2–4 | CONFIRMED |
| Running head on the Chemistry pages | "OHIO'S LEARNING STANDARDS \| SCIENCE \| ADOPTED 2018" | 259–286 | CONFIRMED |
| Section name used inside the document | "Ohio's Learning Standards for Science" (table of contents entry) | 2, 17 | CONFIRMED |
| Spec value `"Ohio Learning Standards for Science (2018) · Chemistry"` | Leaves out the possessive "Ohio's" | — | **WRONG** (minor) |

**Recommended source line:** `Ohio's Learning Standards for Science (adopted 2018) · Chemistry`.
If the line should name the document itself:
`Ohio's Learning Standards and Model Curriculum: Science (2018/2019) · Chemistry`.
Both forms appear in the official text.

Currency: this document cannot show whether a later revision replaced it. That question stays
**UNVERIFIED**. Nothing in the upload suggests a later version.

## 2. Official Chemistry code list (verbatim)

Strands (p. 259): **"C.PM: STRUCTURE AND PROPERTIES OF MATTER"** and **"C.IM: INTERACTIONS OF
MATTER"**. Course note (p. 259): "The following information may be taught in any order; there is no
ODE-recommended sequence."

| Code | Official title | Official sub-points (verbatim) | Syllabus page | Statement + elaboration page | VIP pages | Draft verdict |
|---|---|---|---|---|---|---|
| C.PM.1 | Atomic structure | • Evolution of atomic models/theory • Electrons • Electron configurations | 259 | 261 | 262–263 | CONFIRMED |
| C.PM.2 | Periodic table (written "Periodic Table" on p. 259) | • Properties • Trends | 259 | 264 | 264–265 | CONFIRMED |
| C.PM.3 | Chemical bonding | • Ionic • Polar/covalent | 259 | 266 | 267–269 | Draft "Metallic; Polyatomic ions" as sub-points: **WRONG**. Metallic bonding is in the elaboration ("The concept of metallic bonding is also introduced", p. 266) and the VIP (p. 269), not the sub-point list. Polyatomic ions do not appear in C.PM.3 at all |
| C.PM.4 | Representing compounds | • Formula writing • Nomenclature • Models and shapes (Lewis structures, ball and stick, molecular geometries) | 259 | 270 | 271 | CONFIRMED |
| C.PM.5 | Quantifying matter | **No bullet sub-points** (pp. 259, 272) | 259 | 272 | 273 | Draft sub-point list: **WRONG**. There are no official sub-points. The elaboration covers SI units, significant figures, scientific notation, error analysis, dimensional analysis, average atomic mass, the mole, molar mass, and Avogadro's number with density conversions (p. 272). Percent composition and empirical formula appear **only in the VIP** (p. 273) |
| C.PM.6 | Intermolecular forces of attraction | • Types and strengths • Implications for properties of substances (sub-bullets: Melting and boiling point; Solubility; Vapor pressure) | 259 | 274 | 275–276 | CONFIRMED |
| C.IM.1 | Chemical reactions | • Types of reactions • Kinetics • Energy • Equilibrium • Acids/bases | 259 | 277–278 | 279–281 | CONFIRMED |
| C.IM.2 | Gas laws | • Pressure, volume and temperature • Ideal gas law | 259 | 282 | 283 | CONFIRMED |
| C.IM.3 | Stoichiometry | • **Molar calculations** • Solutions • Limiting reagents | 259 (says "Molecular calculations") | 284 ("Molar calculations") | 285 ("Molar Calculations") | Resolved: **the source contradicts itself.** The syllabus (p. 259) says "Molecular calculations". The content statement (p. 284) and the VIP heading (p. 285) say "Molar calculations". Use "Molar" (the content statement, and 2 of 3 occurrences) |

Key verbatim quotes the mapping relies on:

| Code | Quote | Page |
|---|---|---|
| C.PM.1 | "In this course, electron configuration (extended and noble gas notation) and orbital diagrams can be shown for any element in the first three periods." / "Note: Quantum numbers and equations of de Broglie, Schrödinger and Plank are beyond the scope of this course." | 261 |
| C.PM.2 | "Atomic theory is used to describe and explain trends in properties across periods or down columns including atomic radii, ionic radii, first ionization energies, electronegativities…" | 264 |
| C.PM.3 | "Differences in electronegativity values can be used to predict where a bond fits on the continuum between ionic and covalent bonds. The polarity of a bond depends on the electronegativity difference and the distance between the atoms (bond length)." | 266 |
| C.PM.4 | "This can include ionic compounds made up of elements from groups 1, 2, 17, hydrogen, oxygen and polyatomic ions (given the formula and charge of the polyatomic ion). Given the formula, a compound can be named using conventional systems that include Greek prefixes and Roman numerals where appropriate." | 270 |
| C.PM.5 | "Using the International System of Units (SI), significant digits or figures, scientific notation, error analysis and dimensional analysis are vital to scientific communication." / "The atomic mass of an element is calculated given the mass and relative abundance of each isotope…" | 272 |
| C.PM.6 | "Types of intermolecular attractions include London dispersion forces…, dipole-dipole forces… and hydrogen bonding…" | 274 |
| C.IM.1 | "The role of energy in determining the spontaneity of chemical reactions is dealt with conceptually in this course. Entropy and its influence on the spontaneity of reactions are reserved for more advanced study." | 278 |
| C.IM.2 | "…problems can be solved for an unchanging gaseous system using the ideal gas law (PV = nRT)…" | 282 |
| C.IM.3 | "When performing a reaction in the lab, the experimental yield can be compared to the theoretical yield to calculate percent yield. The concept of limiting reagents is treated conceptually." | 284 |

## 3. Science inquiry: is there a citable code?

| Item | Finding | Page | Verdict |
|---|---|---|---|
| HS inquiry strand | The high school "Nature of Science" table has a category, "Scientific Inquiry, Practice and Applications": "All students must use these scientific processes with appropriate laboratory safety techniques…". It carries **no code** | 11, repeated in the Chemistry section on 260 | CONFIRMED: no code |
| "Science Inquiry and Applications" | This heading appears only for grades 5–8 (p. 16). K–4 uses "Science Inquiry, Practices and Applications" (p. 15). Neither has a code | 15–16 | Not applicable to HS. No code |
| Chemistry course description | "Each course should include inquiry-based laboratory experience that engages students in asking valid scientific questions and gathering and analyzing information." | 259 | CONFIRMED. The roadmap footer ("inquiry practices are built in") is consistent with this |

**Do not invent an inquiry code.** If the roadmap needs to cite inquiry, cite it in words:
"Nature of Science: Scientific Inquiry, Practice and Applications (p. 260)".

## 4. Standards key: short descriptions (official wording)

| Code | Key title | Key description (≤ ~12 words, from the official text) | Basis |
|---|---|---|---|
| C.PM.1 | Atomic structure | evolution of atomic models/theory; electrons; electron configurations | sub-points, p. 259/261 |
| C.PM.2 | Periodic table | properties and trends | sub-points, p. 259/264 |
| C.PM.3 | Chemical bonding | ionic and polar/covalent bonds; metallic bonding also introduced | sub-points + elaboration, p. 266 |
| C.PM.4 | Representing compounds | formula writing; nomenclature; models and shapes (Lewis, ball-and-stick, geometries) | sub-points, p. 270 |
| C.PM.5 | Quantifying matter | SI units, significant figures, dimensional analysis, the mole, molar mass | elaboration, p. 272 (there are no sub-points) |
| C.PM.6 | Intermolecular forces of attraction | types and strengths; effects on melting/boiling point, solubility, vapor pressure | sub-points, p. 274 |
| C.IM.1 | Chemical reactions | types of reactions; kinetics; energy; equilibrium; acids/bases | sub-points, p. 277 |
| C.IM.2 | Gas laws | pressure, volume and temperature; ideal gas law | sub-points, p. 282 |
| C.IM.3 | Stoichiometry | molar calculations; solutions; limiting reagents | sub-points, p. 284 |

A unit-specific note after the description (for example "used here to predict ion charges") is
fine. It must stay visibly separate from the official wording, so it is not read as part of the
standard.

## 5. Section-by-section mapping, U0–U15 (retired 1.4, 3.5, 6.5, 6.6 skipped)

This mapping is my judgement from the official text. ODEW does not publish an alignment. "Draft"
gives the verdict on the earlier draft's mapping.

| Sec | Title | Main | Support | Justification (official text, page) | Draft |
|---|---|---|---|---|---|
| 0.1 | Laboratory Equipment | NONE | C.PM.5 (VIP) | No content statement. C.PM.5 VIP: "Carry out laboratory measurements with a variety of equipment (e.g., graduated cylinders, beakers, balances)…" (p. 273). NOS SIPA, uncoded (p. 260) | CONFIRMED (none) |
| 0.2 | Laboratory Safety | NONE | — | No content statement. NOS SIPA, uncoded: "observing appropriate safety techniques" (p. 260) | CONFIRMED |
| 0.3 | Science Lab & Basic Skills | C.PM.5 *if the section teaches measurement*; otherwise NONE | — | C.PM.5 elaboration on SI and measurement (p. 272) and VIP measurement tasks (p. 273). I have not seen the 0.3 content | CONFIRMED (conditional) |
| 0.4 | Scientific Observations | NONE | — | No Chemistry statement. NOS, uncoded: "Make observations and look for patterns" (p. 260). Classifying by properties is Physical Science PS.M.1 (p. 209), not Chemistry | Draft said C.PM.5 support: WRONG. Remove it |
| 1.1 | Matter & Changes | NONE | C.PM.6 (VIP, for the chromatography lab) | Classification of matter is Physical Science PS.M.1, "Heterogeneous vs. homogeneous; Properties of matter; States of matter and its changes" (p. 209). C.PM.6 VIP: "Construct a chromatography technique to separate the components of different dyes… applying principles of inter- and intra-molecular forces" (p. 275) | CONFIRMED (none). Support basis corrected to the C.PM.6 VIP |
| 1.2 | History of the Atomic Model | C.PM.1 | — | Sub-point "Evolution of atomic models/theory" (p. 261). Thomson, Rutherford, Bohr and Schrödinger are named (p. 261) | CONFIRMED |
| 1.3 | Atomic Structure (incl. isotopes) | C.PM.1 | C.PM.5 | C.PM.1 elaboration: protons, neutrons, electrons, isotopes were "included" in Physical Science and are revisited here (p. 261). VIP: "Determine the atomic number, mass number, number of protons, neutrons and electrons" (p. 262). C.PM.5: "Elemental samples are a mixture of several isotopes" (p. 272) | CONFIRMED (C.PM.5 support added) |
| 1.5 | Average Atomic Mass | **C.PM.5** | C.PM.1 (VIP) | C.PM.5 **elaboration**: "The atomic mass of an element is calculated given the mass and relative abundance of each isotope" (p. 272). C.PM.1 has it only as a VIP item (p. 262) | Draft main C.PM.1: **WRONG**. Main is C.PM.5 |
| 2.1 | The Bohr Model | C.PM.1 | C.PM.2 | "Bohr used data from atomic spectra to propose a planetary model" (p. 261). "Bohr's planetary model is useful to explain and predict periodic trends" (p. 261) | CONFIRMED |
| 2.2 | Energy Levels, Sublevels & Orbitals | C.PM.1 | — | "Electron energy levels consist of sublevels (s, p, d and f), each with a characteristic number and shape of orbitals" (p. 261). Quantum numbers are out of scope (p. 261) | CONFIRMED |
| 2.3 | Electron Configurations | C.PM.1 | C.PM.2 | Sub-point "Electron configurations". Scope is "any element in the first three periods" (p. 261). "The electron configuration of an atom can be determined from the position on the periodic table" (p. 264) | CONFIRMED |
| 2.4 | Electron Stability & Valence Electrons | C.PM.1 | C.PM.3 | "Valence electrons are responsible for most of the chemical properties of elements" (p. 261). "An atom's electron configuration, particularly the valence electrons, determines how an atom interacts…" (p. 266) | CONFIRMED |
| 2.5 | Atomic & Electron Spectra | C.PM.1 | — | "Data from atomic spectra (emission and absorption) gives evidence that electrons can only exist at certain discrete energy levels" (p. 261). VIP flame test (p. 263) | CONFIRMED |
| 3.1 | Organization, Families & Groups | C.PM.2 | C.PM.1 | "How the periodic table is divided into groups, families, periods, metals, nonmetals and metalloids is also included and will be revisited here" (p. 264). Valence configurations repeat within a group (p. 264) | CONFIRMED |
| 3.2 | Metals, Nonmetals & Metalloids | C.PM.2 | — | Same sentence (p. 264). VIP: "Given a metalloid, judge whether [it] is more likely to behave as a metal or nonmetal" (p. 264) | CONFIRMED |
| 3.3 | Atomic & Ionic Radius | C.PM.2 | — | Trends "including atomic radii, ionic radii" (p. 264) | CONFIRMED |
| 3.4 | Ionization Energy & Electronegativity | C.PM.2 | C.PM.3 | "first ionization energies, electronegativities" (p. 264). Additional ionization energies are reserved for advanced study (p. 264). Electronegativity is used for bonding (p. 266) | CONFIRMED |
| 3.6 | Explaining Periodic Trends | C.PM.2 | C.PM.1 | "Atomic theory is used to describe and explain trends" (p. 264). VIP: "Describe how shielding effect explains the trend in atomic size" (p. 265). Bohr model explains trends (p. 261) | CONFIRMED |
| 3.7 | Ion Formation | **C.PM.3** | C.PM.2, C.PM.1 | C.PM.3 VIP (Ionic bonds): "use the octet rule to predict the most stable ion formed" and "Using electron configurations, hypothesize how an atom becomes a cation or anion" (p. 267). Ionic radii trend (p. 264) | Draft main C.PM.2: **WRONG**. Main is C.PM.3 (VIP-based) |
| 4.1 | Why Atoms Bond | C.PM.3 | — | "Atoms of many elements are more stable when they are bonded to other atoms… energy is released" (p. 266) | CONFIRMED |
| 4.2 | Ionic Bonding | C.PM.3 | C.PM.1 | Sub-point "Ionic" (p. 266). VIP: "Represent the formation of a bond using electron configurations" (p. 267) | CONFIRMED |
| 4.3 | Covalent Bonding | C.PM.3 | C.PM.4 | Sub-point "Polar/covalent" (p. 266). VIP: "Write equations for covalent bond formation… using Lewis structures"; single/double/triple bonds (p. 268) | CONFIRMED |
| 4.4 | Metallic Bonding | C.PM.3 | — | "The concept of metallic bonding is also introduced to explain many of the properties of metals (e.g., conductivity)" (p. 266). VIP "Metallic bonds" (p. 269). This comes from the elaboration, not a sub-point | CONFIRMED |
| 4.5 | Electronegativity & Bond Type | C.PM.3 | C.PM.2 | "Differences in electronegativity values can be used to predict where a bond fits on the continuum" (p. 266) | CONFIRMED |
| 4.6 | Bond Polarity | C.PM.3 | — | "The polarity of a bond depends on the electronegativity difference and the distance between the atoms" (p. 266) | CONFIRMED |
| 5.1 | Lewis Electron Structures | C.PM.4 | C.PM.3 | "Models and shapes (Lewis structures…)". Limited to "hydrogen, carbon, nitrogen, oxygen, phosphorus, sulfur and the halogens" (p. 270) | CONFIRMED |
| 5.2 | VSEPR Theory | C.PM.4 | — | Lewis structures "can be combined with valence shell electron pair repulsion (VSEPR) theory" (p. 270) | CONFIRMED |
| 5.3 | Molecular Geometry | C.PM.4 | — | "…to predict the three-dimensional electron pair and molecular geometry" (p. 270) | CONFIRMED |
| 5.4 | Molecular Polarity | **C.PM.3** | C.PM.4, C.PM.6 | C.PM.3 VIP: "Distinguish between bond polarity and molecular polarity. Construct models illustrating how a nonpolar molecule can be formed from polar bonds" (p. 268). C.PM.6: "the shape and polarity of a molecule are particularly important…" (p. 274) | Draft main C.PM.4: **WRONG** (C.PM.4 does not mention polarity). Main is C.PM.3 |
| 5.5 | Intermolecular Forces | C.PM.6 | — | Sub-point "Types and strengths". London, dipole-dipole and hydrogen bonding are named (p. 274) | CONFIRMED |
| 5.6 | Structure & Physical Properties | C.PM.6 | C.PM.3 | "Implications for properties of substances: Melting and boiling point, Solubility, Vapor pressure" (p. 274). Ionic lattices and network covalent properties (p. 266) | CONFIRMED (support changed from C.PM.4 to C.PM.3) |
| 6.1 | Covalent Names & Formulas | C.PM.4 | C.PM.3 | "named using conventional systems that include Greek prefixes… Given the name of an ionic or covalent substance, formulas can be written" (p. 270) | CONFIRMED |
| 6.2 | Polyatomic Ions | **C.PM.4** | C.PM.3 | "ionic compounds made up of elements from groups 1, 2, 17, hydrogen, oxygen and polyatomic ions (given the formula and charge of the polyatomic ion)" (p. 270). VIP: "Given elements from the periodic table and/or polyatomic ions, predict the formula" (p. 271). C.PM.3 supports "covalently bonded group"; "a substance may contain more than one type of bond" (p. 266) | Spec main C.PM.3: **WRONG**. Swap: main C.PM.4, support C.PM.3 |
| 6.3 | Ionic Names & Formulas with Transition Metals | C.PM.4 | C.PM.3, C.PM.2 | "Using the periodic table, formulas of ionic compounds… can be predicted… Roman numerals where appropriate" (p. 270). Octet rule and stable ion (C.PM.3 VIP, p. 267). Group valence pattern (p. 264) | CONFIRMED |
| 6.4 | Naming Acids & Formulas | C.PM.4 | C.IM.1 | C.PM.4 VIP: "Write a formula from the name of an acid" and "Name an acid based on its chemical formula" (p. 271). C.IM.1: "Acids often result when hydrogen is covalently bonded to an electronegative element…" (p. 278) | CONFIRMED |
| 7.1 | Mathematical Tools | C.PM.5 | — | "SI, significant digits or figures, scientific notation, error analysis and dimensional analysis" (p. 272) | CONFIRMED |
| 7.2 | The Mole & Avogadro's Number | C.PM.5 | — | "the mole is used to translate between the atomic and macroscopic levels" (p. 272). See finding F8 on the mole definition | CONFIRMED |
| 7.3 | Molar Mass | C.PM.5 | — | "The mass of one mole of a substance is equal to its molar mass in grams" (p. 272) | CONFIRMED |
| 7.4 | Mole Conversions | C.PM.5 | — | "…convert between mass, moles, volume and number of particles of a sample" (p. 272) | CONFIRMED |
| 7.5 | Percent Composition | C.PM.5 (VIP) | C.PM.4 | VIP only: "Design a method to determine the empirical formula or percent composition of an unknown hydrate/compound" (p. 273). It is not in the elaboration | CONFIRMED (VIP-based) |
| 7.6 | Empirical Formulas | C.PM.5 (VIP) | C.PM.4 | Same VIP (p. 273) | CONFIRMED (VIP-based) |
| 7.7 | Molecular Formulas | C.PM.5 (inferred) | C.PM.4 | "Molecular formula" does not appear anywhere in the Chemistry section. This is extrapolated from the empirical-formula VIP (p. 273) | Inference only. Label it as such |
| 8.1 | Reading & Writing Chemical Equations | C.IM.1 | C.PM.4 | "…more complex reactions will be studied, classified and represented with balanced chemical equations" (p. 277) | CONFIRMED |
| 8.2 | Balancing Equations | C.IM.1 | — | Same sentence (p. 277). Conservation of matter is described as Physical Science prior knowledge (p. 277) | Draft support C.IM.3: **WRONG** (C.IM.3 covers stoichiometric calculations, p. 284). Remove it |
| 8.3 | Reaction Types | C.IM.1 | — | "oxidation/reduction, synthesis, decomposition, single replacement, double replacement… and combustion" (p. 277) | CONFIRMED |
| 8.4 | Predicting Products | C.IM.1 | — | VIP: "Using activity series and solubility rules construct an outcome for single replacement and double replacement reactions" (p. 279) | CONFIRMED |
| 9.1 | Energy & Heat | C.IM.1 | — | Sub-point "Energy". "Thermal energy is the energy of a system due to the movement of its particles" (p. 277) | CONFIRMED |
| 9.2 | Endothermic & Exothermic | C.IM.1 | C.PM.3 | "energy is transferred out of the system (exothermic) when the products have stronger bonds…" (p. 278). Bond energy (C.PM.3 VIP, p. 267) | CONFIRMED |
| 9.3 | Enthalpy | C.IM.1 | — | "Predictions of the energy requirements… given a table of bond energies. Graphic representations…" (p. 278). The word "enthalpy" does not appear | CONFIRMED (the term is Matt's, the content is Ohio's) |
| 9.4 | Calorimetry | C.IM.1 | — | "calorimetry experiments… Specific heat values can be used to calculate the thermal energy change" (pp. 277–278) | CONFIRMED |
| 9.5 | Spontaneity `EXT` | C.IM.1 (conceptual part only) | — | "spontaneity… dealt with conceptually… Entropy and its influence on the spontaneity of reactions are reserved for more advanced study" (p. 278) | CONFIRMED. Entropy and Gibbs content is beyond Ohio scope, which fits `EXT` |
| 10.1 | Mole Ratios | C.IM.3 | — | "The coefficients of the balanced equation indicate the ratios… in terms of both particles and moles" (p. 284) | CONFIRMED |
| 10.2 | Stoichiometric Calculations | C.IM.3 | — | "A stoichiometric calculation involves the conversion from the amount of one substance… to the amount of another" (p. 284) | CONFIRMED |
| 10.3 | Mass–Mass & Other Conversions | C.IM.3 | C.PM.5 | "amounts can be changed to mass, volume of a gas, volume of solutions and/or number of particles" (p. 284) | CONFIRMED |
| 10.4 | Limiting Reactants | C.IM.3 | — | Sub-point "Limiting reagents". "treated conceptually" (p. 284). VIP mentions BCA tables (p. 286) | CONFIRMED |
| 10.5 | Theoretical & Percent Yield | C.IM.3 | — | "the experimental yield can be compared to the theoretical yield to calculate percent yield" (p. 284) | Draft "not found": **WRONG**. It is in the C.IM.3 elaboration |
| 11.1 | Kinetic Molecular Theory | C.IM.2 | — | "The kinetic-molecular theory can be used to explain the properties of gases" (p. 282) | CONFIRMED (draft support C.PM.6 dropped) |
| 11.2 | Gas Pressure & Variables | C.IM.2 | — | Sub-point "Pressure, volume and temperature". VIP: "Convert between different pressure units" (p. 283). Kelvin is required (p. 282) | CONFIRMED |
| 11.3 | Boyle's, Charles's & Gay-Lussac's Laws | C.IM.2 | — | "When two of these four are kept constant, the relationship between the other two can be quantified" (p. 282). Ohio stresses solving "rather than memorizing the specific names and formulas" (p. 282) | CONFIRMED |
| 11.4 | Combined Gas Law | C.IM.2 | — | "Problems can also be solved involving the changes in temperature, pressure, volume and amount of a gas" (p. 282) | CONFIRMED |
| 11.5 | Avogadro's Law & Molar Volume | C.IM.2 | C.IM.3 | "(Avogadro's law)" (p. 282). VIP: "relate to molar volume at standard temperature and pressure" (p. 283). "volume of a gas" (p. 284) | CONFIRMED |
| 11.6 | Ideal Gas Law | C.IM.2 | — | Sub-point "Ideal gas law". PV = nRT, R = 8.31 J/(mol·K) (p. 282) | CONFIRMED |
| 12.1 | Solutions & Dissolving | C.PM.6 | C.IM.3 | "In order for an ionic substance to dissolve in water, the attractive forces between the ions must be overcome…" (p. 274). C.IM.3 VIP: "Distinguish between solute, solvent and solution" (p. 285) | CONFIRMED |
| 12.2 | Solubility | C.PM.6 | — | Sub-point "Solubility". "greater solubility when dissolving in a solvent with similar intermolecular forces" (p. 274) | CONFIRMED |
| 12.3 | Factors Affecting Solubility & Dissolving Rate | C.PM.6 | C.IM.1 | Solubility (p. 274). "the collision theory can be applied to dissolving solids… The rate at which a substance dissolves should not be confused with… solubility" (p. 277) | CONFIRMED (C.IM.1 Kinetics added for rate) |
| 12.4 | Electrolytes | **NONE** | C.PM.6, C.PM.3 (VIP) | "Electrolyte" does not appear in the Chemistry section. Nearest text: ionic substance dissolving (p. 274), and the VIP on distinguishing bond types by "conductivity" (p. 267) | Draft main C.PM.3: **WRONG**. Main is NONE |
| 12.5 | Molarity | C.IM.3 | — | "Molarity is a measure of the concentration of a solution" (p. 284). VIP: "Calculate the molarity" (p. 285) | CONFIRMED |
| 12.6 | Dilutions | C.IM.3 | — | VIP: "Create a solution and a dilution of a known concentration" (p. 285) | CONFIRMED |
| 12.7 | Solution Stoichiometry | C.IM.3 | — | "Molarity… can be used in stoichiometric calculations" (p. 284) | CONFIRMED |
| 13.1 | Collision Theory | C.IM.1 | — | "Reactions occur when reacting particles collide in an appropriate orientation and with sufficient energy" (p. 277) | CONFIRMED |
| 13.2 | Factors Affecting Reaction Rate | C.IM.1 | — | "changing the concentration…, the temperature or the pressure…, or using a catalyst, can change the reaction rate" (p. 277). Mathematical rates are out of scope | CONFIRMED |
| 13.3 | Chemical Equilibrium | C.IM.1 | — | "dynamic equilibrium… the rate of the reverse reaction is equal to the rate of the forward reaction" (p. 278) | CONFIRMED |
| 13.4 | Equilibrium Shifts | C.IM.1 | — | "the equilibrium system will respond by shifting to a new equilibrium state" (p. 278) | CONFIRMED |
| 13.5 | Le Châtelier's Principle | C.IM.1 | — | "(Le Chatelier's Principle)" named (p. 278). "Mathematical treatment of equilibrium reactions is reserved for advanced study" | CONFIRMED |
| 14.1 | Properties & Definitions | C.IM.1 | — | Hydronium and hydroxide definitions (p. 278). "Brønsted-Lowry and Lewis acids and bases is not the focus at this level" (p. 278) | CONFIRMED |
| 14.2 | Strong vs Weak Acids/Bases | C.IM.1 (inferred) | — | Strength is not named. Closest text: "easily dissociated" (p. 278). "Detailed instruction about the equilibrium of acids and bases… is not the focus" (p. 278) | Inference only |
| 14.3 | pH & pOH | C.IM.1 | — | "pH can be calculated from the concentration of the hydronium ion" (p. 278). VIP (p. 281). pOH is not named | CONFIRMED (pH). pOH is Matt's extension |
| 14.4 | Neutralization | C.IM.1 | — | "Acids can react with bases to form a salt and water" (p. 278) | CONFIRMED |
| 14.5 | Acid–Base Stoichiometry | C.IM.1 | C.IM.3 | "neutralization reactions can be studied quantitatively" (p. 278) | CONFIRMED |
| 14.6 | Titrations | C.IM.1 | C.IM.3 | "…by performing titration experiments" (p. 278). C.IM.3 VIP: "Determine the concentration of an unknown solution through titration" (p. 285) | CONFIRMED |
| 15.1 | Nuclear Stability & Radioactivity | **NONE** | C.PM.1 (prior knowledge only) | C.PM.1 says Physical Science covered "isotopes and the strong nuclear force" (p. 261). Nuclear content is Physical Science **PS.M.5 "Reactions of matter" → "Nuclear reactions"** (pp. 207, 209, 211) and Physics **P.E.5 "Nuclear energy"** (pp. 328, 344–345) | CONFIRMED (none) |
| 15.2 | Types of Radioactive Decay | **NONE** | — | No Chemistry statement. See PS.M.5 (p. 211) | CONFIRMED (none) |
| 15.3 | Nuclear Equations | **NONE** | — | No Chemistry statement. PS.M.5: "the balanced nuclear equation can be written" (p. 211) | CONFIRMED (none) |
| 15.4 | Half-Life | **NONE** | — | No Chemistry statement. PS.M.5 covers half-life (p. 211) | CONFIRMED (none) |
| 15.5 | Fission & Fusion | **NONE** | — | No Chemistry statement. PS.M.5 (p. 211), P.E.5 (p. 345) | CONFIRMED (none) |
| 15.6 | Applications, Risks & Benefits | **NONE** | — | No Chemistry statement. P.E.5: "advantages and disadvantages of generating electricity from fission and fusion" (p. 345) | CONFIRMED (none) |

Printing PS.M.5 or P.E.5 on a *Chemistry* roadmap is Matt's call. They are real codes, but from other
courses. The safe default is "—" or "Course extension (beyond the Ohio Chemistry statements)".

## 6. U6 spec verdicts: `templates/unit-roadmap/specs/chem_u06.json`

| # | Item | Spec value | Verdict | Evidence | Correction |
|---|---|---|---|---|---|
| 1 | 6.1 standards | main C.PM.4, support C.PM.3 | **CONFIRMED** | Greek prefixes, formulas from names (p. 270). Covalent bonding (p. 266) | — |
| 2 | 6.2 standards | main C.PM.3, support C.PM.4 | **WRONG** | Polyatomic ions are named only in C.PM.4 (p. 270, VIP p. 271). C.PM.3 (pp. 266–269) never mentions them | `{"main": ["C.PM.4"], "support": ["C.PM.3"]}` |
| 3 | 6.3 standards | main C.PM.4, support C.PM.3, C.PM.2 | **CONFIRMED** | "Roman numerals where appropriate"; "Using the periodic table, formulas of ionic compounds… can be predicted" (p. 270) | — |
| 4 | 6.4 standards | main C.PM.4, support C.IM.1 | **CONFIRMED** | Acid naming and formulas are C.PM.4 VIP (p. 271). Acid structure is C.IM.1 (p. 278) | — |
| 5 | Key C.PM.2 | "Periodic table" — "properties and trends; used here to predict ion charges." | **CONFIRMED** | Sub-points "Properties; Trends" (p. 264). The trailing clause is a unit note, not official text | — |
| 6 | Key C.PM.3 | "Chemical bonding" — "ionic, polar/nonpolar covalent, metallic bonding; polyatomic ions." | **WRONG** | Official sub-points are only "Ionic; Polar/covalent" (p. 266). Metallic is in the elaboration (p. 266), and nonpolar covalent in the VIP (pp. 267–268). **"polyatomic ions" is not in C.PM.3** | "ionic and polar/covalent bonds; metallic bonding also introduced." |
| 7 | Key C.PM.4 | "Representing compounds" — "formula writing, nomenclature, models and shapes." | **CONFIRMED** | Verbatim sub-points (p. 270) | Optional: add "(Lewis structures, ball and stick, molecular geometries)" |
| 8 | Key C.IM.1 | "Chemical reactions" — "acids/bases. 6.4 introduces acid names; acid–base chemistry is taught in Unit 14." | **CONFIRMED** | "Acids/bases" is a sub-point (p. 277). U14 Acids & Bases matches `courses/chemistry/DECISIONS.md` | Optional: "acids/bases (one of five sub-points)…", so readers don't take the code to be only acids/bases |
| 9 | `standards_source` | "Ohio Learning Standards for Science (2018) · Chemistry" | **WRONG** (minor) | The official form is "Ohio's Learning Standards for Science" (pp. 2, 17), adopted February 2018 (p. 1) | "Ohio's Learning Standards for Science (adopted 2018) · Chemistry" |

The same C.PM.3 key text and 6.2 mapping are almost certainly printed in
`output/chemistry/u06/Unit 6 Roadmap.html`. It matches a grep for the same string. A rebuild is
needed after the spec is fixed.

## 7. Findings and recommendations

| # | Item | Finding | Evidence | Severity | Recommendation |
|---|---|---|---|---|---|
| F1 | U6 spec 6.2 mapping | Main C.PM.3 is wrong. Polyatomic ions belong to C.PM.4 | p. 270, p. 271; C.PM.3 pp. 266–269 | **Blocking (for print)** | Change 6.2 to main C.PM.4, support C.PM.3. Rebuild the U6 Roadmap |
| F2 | U6 spec C.PM.3 key | "polyatomic ions" is wrongly attributed to C.PM.3. "metallic" and "nonpolar" are not official sub-points | p. 266–268 | **Blocking (for print)** | Key text: "ionic and polar/covalent bonds; metallic bonding also introduced." |
| F3 | U6 `standards_source` | Leaves out "Ohio's" | pp. 1, 2, 17 | Low (2 min) | "Ohio's Learning Standards for Science (adopted 2018) · Chemistry" |
| F4 | Recurring pattern | This is the third pass at Ohio codes (F3 in `reports/u2-content-briefs.md` 2026-10-04, then the draft of this report). Codes still live only in per-unit specs. There is no single authoritative list | Repo grep | High | Secretary to propose that the §2 code list and §4 key descriptions live **once** in `courses/chemistry/DECISIONS.md`, with specs pointing at them (CLAUDE.md §1). Each unit spec would then hold only the section → code mapping |
| F5 | C.IM.3 sub-point wording | The source contradicts itself: "Molecular calculations" (p. 259) against "Molar calculations" (pp. 284, 285) | pp. 259, 284, 285 | Low | Use "Molar calculations". Note the discrepancy in DECISIONS.md if the list is adopted |
| F6 | C.PM.5 | No official sub-points. Percent composition and empirical formula appear only in a non-mandatory VIP. "Molecular formula" is never named | pp. 272–273 | Low | Key uses elaboration wording. 7.5–7.7 are mapped to C.PM.5 as VIP-based or inferred, not as settled |
| F7 | Scope notes useful to builders (observation) | Ohio limits: e-configs to the first three periods (p. 261). Lewis/VSEPR to H, C, N, O, P, S and halogens (p. 270). Limiting reagents "treated conceptually" (p. 284). No math for rates or equilibrium (pp. 277–278). Entropy reserved (p. 278). B-L/Lewis acids "not the focus" (p. 278). Polyatomic ions "given the formula and charge" (p. 270) | cited pages | Info | No conflict with DECISIONS.md: Ohio sets a floor, and Matt's memorize-15 rule is a course decision. Useful for `EXT` labelling |
| F8 | Mole definition in the source (observation) | The official text defines the mole as "the number of atoms in exactly 12 grams of the isotope carbon-12" (p. 272). That is the pre-2019 SI definition. Since the SI redefinition of 20 May 2019, the mole is defined by a fixed Avogadro constant, 6.02214076 × 10²³ mol⁻¹ | p. 272; SI 2019 redefinition | Low | Do not copy the Ohio definition into student materials as the current definition. Use the fixed-N_A definition |
| F9 | C.PM.6 classroom caution (observation) | "Dissolving of a solute in water is an example of a process that is difficult to classify as a chemical or physical change and it is not appropriate to have students classify it one way or another." | p. 274 | Low | Check U1.1 and U12.1 materials for any item asking students to classify dissolving as physical or chemical |
| F10 | Unmapped sections | 0.1, 0.2, 0.4, 1.1, 12.4 and all of U15 have no Chemistry content statement | §5 | Low | Show "—" or "Course extension". Do not borrow a code |
| F11 | Inquiry | No code exists at high school. The uncoded NOS category is "Scientific Inquiry, Practice and Applications" | pp. 11, 259, 260 | Info | Keep the footer wording. Never print an inquiry code |
| F12 | Draft corrections | Earlier draft mappings now marked WRONG: 1.5 main, 3.7 main, 5.4 main, 8.2 support, 10.5 "not found", 12.4 main, 0.4 support, C.PM.3 and C.PM.5 sub-points | §2, §5 | Info | Use §5 of this report, not the earlier draft |
