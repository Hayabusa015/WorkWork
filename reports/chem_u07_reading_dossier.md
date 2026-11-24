# Chemistry U7 Unit Reading: Source Dossier (rebuild, five sections)

Prepared by: researcher | Date: 2026-11-24 | Workflow: `workflows/unit-textbook.md`, "Commission the chapter" step 2
Status: REPORT ONLY. Nothing outside `reports/` was edited.

**Scope.** U7 is now five taught sections (`courses/chemistry/DECISIONS.md` l.54–57, decision log 2026-11-24, SHULL-CHG-0110): 7.1 Mathematical Tools · 7.2 The Mole & Molar Mass · 7.3 Mole Conversions · 7.4 Percent Composition & Empirical Formulas · 7.5 Molecular Formulas. 7.6 and 7.7 are RETIRED and must not be used again.

**Inputs carried forward.** These are `reports/chem_u07_reading_content_brief.md`, `reports/chem_u07_reading_verify.md` (Rounds 1–3) and `templates/reading/specs/chem_u07_reading.json` (the current spec, still in the seven-section numbering). I re-solved every number in this dossier. None was copied from those reports.

**Network limitation (read this first).** In this session WebFetch could not reach `www.bipm.org`, `physics.nist.gov` or `www.ciaaw.org`: the hostnames did not resolve. WebSearch did work, so every external locator below is backed by one of three things:
- **(S)**: a search-result excerpt from the named page;
- **(P)**: the earlier verify rounds;
- **(K)**: a value I know but could not retrieve this session.

Nothing marked (K) should be treated as verified until someone opens the locator. To open the primary pages directly, `www.bipm.org`, `physics.nist.gov`, `www.ciaaw.org`, `webbook.nist.gov` and `pubchem.ncbi.nlm.nih.gov` have to be allowed in the session's network settings. The Auditor should open each locator during QA.

**Status codes used below:**
- **SRC**: sourced, with a locator and an excerpt or data.
- **DER**: derived by arithmetic from sourced inputs; the working is shown.
- **ILL**: illustrative. The data is made up and must be labelled as illustrative in the teacher key.
- **SEC**: secondary sources only.
- **UNVERIFIED**: I could not find a source. Do not print it as fact.

---

## A. Findings (blocking first, then by fix time)

| # | Item | Finding | Evidence | Severity | Recommendation |
|---|---|---|---|---|---|
| D1 | Section codes and cross-references in the spec | **The spec is still in the retired seven-section numbering.** It lists `"sections"` 7.1–7.7, and 7.6 and 7.7 are now RETIRED codes. "This reading covers all seven sections" is now wrong. The 7.2 title "The Mole & Avogadro's Number" is now "The Mole & Molar Mass", and "Percent Composition" is now "Percent Composition & Empirical Formulas". Internal pointers that now point at the wrong section: "The mole conversions in Section 7.4" (now 7.3); "Section 7.3 explains why" (now inside 7.2); "Section 7.3 gives the molar mass of O₂" (now 7.2); "Section 7.7 shows what can" and "which Section 7.7 describes" (now 7.5). Example and On Your Own labels 7.3 and 7.4 must be renumbered, and every `vocab[].section` value must be re-mapped. | spec l.5–13, 32, 216, 233, 271, 437, 533, 567; DECISIONS l.54–57, 445–458 | **Blocking (build)** | The designer re-maps the spec: old 7.2 + 7.3 → 7.2, old 7.4 → 7.3, old 7.5 + 7.6 → 7.4, old 7.7 → 7.5. Do not print 7.6 or 7.7 anywhere (CLAUDE.md §3). |
| D2 | Planned On Your Own 7.5: empirical HO with molar mass 34.02 → H₂O₂ | **The reading prints the answer before the student meets the problem.** The empirical-formula prose (old 7.6, now 7.4) says "Hydrogen peroxide, H₂O₂, reduces the same way to HO." The workflow says to keep the answer to a transfer question out of its prompt. | spec l.525; `workflows/unit-textbook.md` "Build for the discipline" | **Major** | Option A: remove the H₂O₂ sentence from 7.4 and keep the HO problem. Option B (preferred): keep the sentence and use On Your Own 7.5 = empirical CH₂, molar mass 28.06 g/mol → C₂H₄ (solved in §D4). |
| D3 | Vocabulary count | **The spec has 16 bold terms, and the workflow allows at most ten.** | spec l.48–130; workflow "Prepare the unit reading" step 2 | **Major (build)** | The designer selects ≤10. Content note: *formula unit* must stay defined in the prose either way, because no earlier unit introduced it (D8). |
| D4 | Spec front and back matter versus the new tear-off format | **Observation only.** The spec's vocabulary preview, Day 1 / End-of-unit columns, per-section Reading Checks and "last two pages" do not match the workflow's tear-off leaf. The workflow wants: Name line; the verbatim due instruction; one question per numbered section on the front; term–definition reference on the back. | spec l.30–47, 624–652; workflow steps 3–5 | Minor (outside my scope) | For the Overseer and designer. No content impact. |
| D5 | Reference Sheet 1 title | **The order matches DECISIONS, but the printed title may not.** DECISIONS lists sheet 1 as **Equations & Constants** and sheet 2 as **Significant Figure Rules**, and calls these the on-page titles. The builder prints the sheet 1 headings as "Equations" (page 1) and "Constants & Conversions" (page 2). Sheet 2 prints "Significant Figure Rules", which matches. The builder also prints no sheet number on the page, so "Sheet 1" and "Sheet 2" rely on the packet order. *Inference from the builder source. I did not open the built PDF.* | DECISIONS l.175–196; `templates/reference/build_reference.py` l.74, 157–158, 186 | Minor | In the reading, refer to the sheets by the title students will see, e.g. "the Equations page of your reference packet" and "Significant Figure Rules". The Secretary should reconcile the builder heading with DECISIONS. That needs a proposal; I have not changed either. |
| D6 | Reference sheet "1 lb = 453.6 g" | **This factor is rounded, not exact.** The exact definition is 1 lb = 453.592 37 g (NBS notice, Federal Register, 1 July 1959). Significant Figure Rules says that "defined conversions" have unlimited significant figures, so a student could treat 453.6 as exact. | `build_reference.py` l.131, 168; §C row 7.1-g | Minor | Do not use lb ↔ g for the 7.1 sig-fig example. Use 1 in = 2.54 cm, which is exact (options in §D1). If the Reference sheet should label 453.6 g as rounded, the Secretary raises that as a separate proposal. |
| D7 | Molar volume pointer in earlier reports | **A stale cross-reference.** The brief (F2, scope line) puts molar volume in **11.5**. After the U11/U12 swap (SHULL-CHG-0110) it is **12.5** (Avogadro's Law & Molar Volume), and 11.5 is now Molarity. The spec mentions neither, so it is unaffected. | brief l.5, 22; DECISIONS l.73–82 | Minor | Any future note should say 12.5. The rule is unchanged: no STP, 22.4 L or liters in U7. |
| D8 | "Formula unit" in an earlier unit | **Not introduced before U7.** Evidence: (a) DECISIONS U4 and U6 section titles do not name it (l.42–52); (b) the U4 guided notes give the 4.2 key terms as "Ionic bonding, ion, crystal", with no formula unit; (c) neither the U4 nor the U6 roadmap uses the term; (d) the only earlier-unit hit is a snow-day key that hedges: "Only give credit if you've taught ionic vs. covalent". *Not checked:* U4 slide videos (.mp4) and any U6 notes or slides, because no U6 notes or slide specs exist in the repo. | `templates/notes/specs/chem_u04-u05_notes_student.json` l.30–37; `templates/unit-roadmap/specs/chem_u04.json`, `chem_u06.json`; `templates/snow_day/specs/chemistry.json` l.57 | Info | Keep the full definition at first use in 7.2. Do not write "remember from Unit 4". |
| D9 | Benzene as a solvent (correcting the record) | **Round 2 R2-1 overstated the source.** It said solvent use was "largely phased out", but the current ATSDR ToxFAQ (reviewed Nov 2024) still says "Benzene is used in industry as a solvent and to make other products…". The current spec wording, "a liquid used to make plastics such as polystyrene", is supported (§C row 7.5-f) and needs no change. | §C rows 7.5-f, 7.5-g | Info | No spec change. Do not reintroduce "phased out" anywhere. |
| D10 | Baking soda in Why It Matters | **Supported by culinary sources only.** No primary authority found. "Too little: flat; too much: bitter" matches several baking guides (excess unreacted soda gives a soapy or metallic taste). | §C row WIM-a | Minor | Acceptable as an everyday illustration. Keep the claim no stronger than it is now. |
| D11 | Molar masses that differ from published values | **This is the third time in this unit.** Glucose, benzene and methane each needed a teacher note because the student table gives a different value from published sources. The new items add more: H₂O₂ 34.02 (published 34.01), C₂H₄ 28.06 (28.05), Fe₂O₃ 159.70 (159.69). Acetylene and NaCl round the same both ways. | §B | Minor | Extend the existing key teacher note to every compound printed. **Pattern:** this correction has now come up three times in one unit, so the Secretary could propose a standing one-line key note for every Chemistry reading ("values from your periodic table; published values may differ in the last digit"). |
| D12 | Recurring correction: digit count versus place value | **The same fix was needed three times in verify Round 1** (#1, #2, #3): text said "more digits" where it meant "the place value of the last digit". It is fixed in the spec, but the rebuild may reintroduce it. | verify.md Round 1 #1–#3 | Info (pattern) | Designer: describe fineness by the place value of the last digit, never by how many digits. Applies to the new 7.1 examples. |

---

## B. Classroom atomic-mass source versus IUPAC

**Classroom source:** `templates/reference/chem_data.py`, `ELEMENTS` l.6–37 (comment l.4–5: "average atomic mass (2 decimals) … IUPAC standard atomic weights"). This is the Periodic Table sheet, Reference sheet 4 (DECISIONS l.201: "average atomic mass to 2 decimals").

| Element | Student table (chem_data.py line) | IUPAC/CIAAW standard atomic weight | Abridged / conventional | Status |
|---|---|---|---|---|
| H | 1.01 (l.7) | [1.007 84, 1.008 11] | 1.008 | SRC (S): ciaaw.org/atomic-weights.htm, excerpt "1 \| H \| hydrogen \| [1.007 84, 1.008 11]" |
| C | 12.01 (l.8) | [12.0096, 12.0116] | 12.011 | SRC (S): IUPAC table (iupac.qmul.ac.uk/AtWt/) and Britannica "Atomic weight" table; conventional values from Coplen, Meija & Holden, 2016 four-figure table (USGS / J. Chem. Educ.) |
| O | 16.00 (l.8) | [15.999 03, 15.999 77] | 15.999 | SRC (S): same as C |
| Na | 22.99 (l.11) | 22.989 769 28 | 22.990 | (K): not retrieved this session |
| Cl | 35.45 (l.11) | [35.446, 35.457] | 35.45 | (K) |
| Fe | 55.85 (l.13) | 55.845 | 55.845 | (K). Used only for the optional Fe₂O₃ problem |
| Ni | 58.69 (l.13) | 58.6934 | 58.693 | (K). Not used in arithmetic; the "nickel" in the text is the coin |

**IUPAC differences that matter for printed numbers** (re-solved, using conventional values H 1.008, C 12.011, O 15.999, Na 22.990, Cl 35.45, Fe 55.845):

| Compound | Student table | IUPAC conventional | Published (PubChem) | Differs? |
|---|---|---|---|---|
| H₂O | 2.02 + 16.00 = **18.02** | 2.016 + 15.999 = 18.015 | 18.015 (K) | 18.02 in both cases (18.015 rounds to 18.02) |
| O₂ | **32.00** | 31.998 | — | yes, 0.002 |
| NaCl | 22.99 + 35.45 = **58.44** | 58.440 | 58.44 (K) | no |
| CH₄ | 12.01 + 4.04 = **16.05** | 12.011 + 4.032 = 16.043 | 16.04 (K) | **yes**. A teacher note already exists |
| C₆H₁₂O₆ | 72.06 + 12.12 + 96.00 = **180.18** | 72.066 + 12.096 + 95.994 = 180.156 | 180.16 (S, CID 5793) | **yes**. Teacher note exists |
| CH₂O | 12.01 + 2.02 + 16.00 = **30.03** | 30.026 | 30.03 (K) | no |
| C₂H₂ | 24.02 + 2.02 = **26.04** | 24.022 + 2.016 = 26.038 | 26.04 (S, CID 6326: 26.0373) | no |
| C₆H₆ | 72.06 + 6.06 = **78.12** | 72.066 + 6.048 = 78.114 | 78.11 (S, CID 241) | **yes**. Teacher note exists |
| CH | **13.02** | 13.019 | — | no |
| H₂O₂ (new) | 2.02 + 32.00 = **34.02** | 2.016 + 31.998 = 34.014 | 34.014 / 34.015 (S, CID 784) | **yes**. Add to the teacher note if used |
| C₂H₄ (new option) | 24.02 + 4.04 = **28.06** | 24.022 + 4.032 = 28.054 | 28.05 (K) | **yes**. Add if used |
| Fe₂O₃ (new option) | 111.70 + 48.00 = **159.70** | 111.690 + 47.997 = 159.687 | 159.69 (K) | **yes**. Add if used |

**Molar mass equals the atomic-mass number (spec 7.3, now 7.2):** "The same number in g/mol is the mass of one mole of atoms." Since the 2019 SI revision, the molar mass constant is no longer exactly 1 g/mol, but it differs by less than about 1 part in 10⁹. The printed wording is fine. Teacher notes must not say "exactly by definition" (brief F13). The exact CODATA value of the molar mass constant was not retrieved (physics.nist.gov blocked). **UNVERIFIED digits; the claim itself holds.**

---

## C. Source dossier: every factual claim and number in the spec

The "Spec location" column gives the current spec section, then the new section after re-mapping (D1).

### Why It Matters (front page)

| ID | Claim as printed | Value / excerpt | Source (title, edition/date) | Locator | Status |
|---|---|---|---|---|---|
| WIM-a | "Use too little baking soda and the bread stays flat; use too much and it tastes bitter." | Excess soda not neutralized by acid leaves "a metallic, soapy aftertaste"; too little gives poor rise | Baking guides, accessed 2026-11-24: Sally's Baking Addiction, "Baking Powder vs. Baking Soda"; The Bake School, "Focus on baking soda" | sallysbakingaddiction.com/baking-powder-vs-baking-soda/; bakeschool.com/focus-on-baking-soda/ | **SEC** (D10) |
| WIM-b | Atoms and molecules "react in fixed ratios by count" | Law of definite proportions / whole-number mole ratios. Previews U10 10.1 Mole Ratios | DECISIONS U10 l.69–71. Standard chemistry; no external citation needed at this level | — | SRC (curriculum) |
| WIM-c | "In the lab a chemist measures amounts by weighing them on a balance" | Accurate as worded. Round 3 R3-4 confirmed the wording | verify.md R2-2, R3-4 | — | SRC (P) |
| WIM-d | "a plant making fertilizer … extra of one ingredient is left over and too little of it leaves some of the others unused" | Ammonia (Haber–Bosch) plants: about 15% conversion per pass; "unreacted gases are recycled", reaching about 97–98% overall. Excess is **left over** (recycled), not wasted, which is exactly the spec's wording | Chemguide, "The Haber Process" (Clark); Cussler et al., "Performance of a Small-Scale Haber Process" (Ind. Eng. Chem. Res.); International Fertilizer Association history PDF | chemguide.co.uk/physical/equilibria/haber.html ("by continual recycling of the unreacted nitrogen and hydrogen, the overall conversion is about 98%"); fertilizer.org/wp-content/uploads/2023/01/HABER.pdf | SRC (S, secondary-educational). The spec already uses "left over", so Round 3 R3-3 is resolved |
| WIM-e | "A lab mixing a solution … needs the right amounts" | True, but a solution needs the right amounts for its concentration, not for any leftover reactant. The R3-3 caveat still holds | verify.md R3-3 | — | SRC (P). Wording acceptable |

### 7.1 Mathematical Tools (stays 7.1)

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 7.1-a | Record the certain digits plus one estimated digit; ruler readings 4.6 cm (cm ruler) and 4.63 cm (mm ruler) | Figure tip drawn at 4.63 cm; labels correct | Classroom convention; figure checked in verify.md Round 1 | verify.md "Ruler 4.6 / 4.63 cm"; `make_chem_u07_figures.py` | SRC (P) / ILL (the drawn pencil) |
| 7.1-b | Sig-fig rules ("nonzero digits always count; zeros depend on where they sit") | "Nonzero digits are always significant." / leading, captive and trailing-zero rules | Reference sheet 2, Significant Figure Rules | `build_reference.py` l.162–168 | SRC (classroom) |
| 7.1-c | "Keep every digit while you work, and round once, at the end." | "In a multi-step problem, keep extra digits until the final answer, then round once." | Reference sheet 2 | `build_reference.py` l.178–179 | SRC (classroom) |
| 7.1-d | Bathroom scale 148 lb (whole pounds); kitchen scale 12.4 g (tenths) | Example readings for typical tools | — | — | **ILL**. "might say" wording keeps it illustrative; brief §5 |
| 7.1-e | Precision has two meanings: fineness (place value of the last digit) and agreement of repeated measurements | VIM 2.15 "measurement precision: closeness of agreement between indications or measured quantity values obtained by replicate or repeated measurements"; fineness corresponds to VIM 4.14 "resolution" | JCGM 200:2012, *International Vocabulary of Metrology* (VIM), 3rd ed. | §2.15 and §4.14 | (P) / (K). Not re-retrieved this session |
| 7.1-f | Gas pump: $3.299 × 12.5 gal = $41.2375; you pay $41.24 | 12.5 × 3.299 = 37.4875 + 3.75 = **41.2375** ✓. Pumps round to the cent; prices are set to 9/10 of a cent, a practice dating from the 1930s | NACS, "Why Gas Is Priced Using Fractions of a Penny" | convenience.org/topics/fuels-and-energy/why-gas-is-priced-using-fractions-of-a-penny | SRC (S) + DER. The $3.299 price and the 12.5 gal are **ILL** |
| 7.1-g | "1 inch is defined as exactly 2.54 cm" | "the inch … is exactly equivalent to 25.4 millimeters"; 1 yd = 0.9144 m; 1 lb = 0.453 592 37 kg | NBS, "Refinement of values for the yard and the pound", Federal Register, 1 July 1959 (effective 1 July 1959) | Monthly Catalog record mocat.library.unt.edu/catalog/779-17771; text copy corpora.tika.apache.org/base/docs/govdocs1/656/656283.pdf | SRC (S) |
| 7.1-h | Exactly 12 eggs in a dozen; exact numbers don't limit sig figs | "Exact numbers (counted items, defined conversions) have unlimited significant figures." | Reference sheet 2 | `build_reference.py` l.168 | SRC (classroom) |
| 7.1-i | 602,200,000,000,000,000,000,000 = 6.022 × 10²³ | "6022" + 20 zeros = 24 digits, so the exponent is 23 ✓ | — | — | DER |
| 7.1-j | One water molecule is 2.99 × 10⁻²³ g | 18.02 g/mol ÷ 6.022 140 76 × 10²³ mol⁻¹ = **2.9923 × 10⁻²³ g** → 2.99 × 10⁻²³ ✓. IUPAC: 18.015 ÷ N_A = 2.9915 × 10⁻²³, also 2.99 | §B; mole definition row 7.2-b | — | DER |
| 7.1-k | "6.022 × 10²³ has four significant figures" | "In scientific notation, every digit in the coefficient is significant." | Reference sheet 2 | `build_reference.py` l.167 | SRC (classroom) |
| 7.1-l | 3 dozen × 12 eggs/1 dozen = 36 eggs; a flipped factor gives dozen²/egg | 3 × 12 = 36 ✓; dozen × dozen/egg = dozen²/egg ✓ | — | — | DER |
| 7.1-m | Honest-digits box: 12.4382 g reported from a 0.1 g scale claims "1,000 times finer" | Last digit is in the 0.0001 place; 0.1 ÷ 0.0001 = 1,000 ✓ | — | — | DER / ILL |

### 7.2 The Mole & Avogadro's Number → new 7.2 The Mole & Molar Mass (first half)

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 7.2-a | Pair = 2, dozen = 12, ream = 500 sheets | Common counting units; ream = 500 sheets is the modern US paper-trade convention | — | — | (K). Low risk; no primary source fetched |
| 7.2-b | "Since 2019 the mole has been defined as exactly 6.022 140 76 × 10²³ particles" | "The mole, symbol mol, is the SI unit of amount of substance. One mole contains exactly 6.022 140 76 × 10²³ elementary entities." In force from 20 May 2019 | BIPM, *The International System of Units (SI Brochure)*, 9th ed. (2019) | §2.3.1, p.134 (English). Same wording: BIPM *mise en pratique* SI App. 2, bipm.org/documents/20126/41489679/SI-App2-mole.pdf; IUPAC Gold Book M03980, goldbook.iupac.org/terms/view/M03980 | SRC (S + P). p.134 is cited by secondary sources; §2.3.1 comes from Round 1 (P) and was not opened this session |
| 7.2-c | N_A as a constant: 6.022 140 76 × 10²³ mol⁻¹ (exact) | CODATA lists N_A as exact | NIST CODATA, "Avogadro constant" | physics.nist.gov/cgi-bin/cuu/Value?na | (K). Host blocked |
| 7.2-d | "The mole … the SI counting unit for particles" | SI calls it the unit of **amount of substance**; "elementary entity may be an atom, a molecule, an ion, an electron, any other particle…" (Gold Book). The "counting unit" gloss is an acceptable simplification for grade 10–12 | Gold Book M03980 | as 7.2-b | SRC (S). Simplification noted |
| 7.2-e | "Avogadro's number … 6.022 × 10²³" (the term) | IUPAC distinguishes the Avogadro *constant* (N_A, mol⁻¹) from the Avogadro *number* (dimensionless). The spec's vocabulary entry treats it as a number, and the Equations sheet gives "N_A = 6.022 × 10²³ particles/mol". Consistent at this level | `build_reference.py` l.119 | — | SRC (classroom) |
| 7.2-f | Named in honor of Amedeo Avogadro, Italian, early 1800s, "who never knew its value" | Perrin proposed the name in his 1909 review. Avogadro died 9 July 1856 in Turin. Loschmidt made the first estimate (particles per cm³ of gas) in 1865, after Avogadro's death, so "never knew its value" follows from the dates. His hypothesis dates from 1811 | Jensen, W. B. & Gee, N., *J. Chem. Educ.* (Avogadro's number note); *Encyclopaedia Britannica*, "Amedeo Avogadro"; Nature Physics editorial (2016) | homepages.uc.edu/~jensenwb/reprints/136.%20Avogadro.pdf; britannica.com/biography/Amedeo-Avogadro; nature.com/articles/nphys3754 | SRC (S). "Never knew" is DER from the dates. Print **only** "named in honor of"; leave out Perrin and Loschmidt (brief F12 stands) |
| 7.2-g | Counting 1 per second: about **19 quadrillion years** | 6.022 140 76 × 10²³ s ÷ 3.155 76 × 10⁷ s/yr (Julian year, 365.25 d) = **1.908 × 10¹⁶ yr** → 19 quadrillion ✓ | Mole definition (7.2-b) | — | DER |
| 7.2-h | "roughly **1.4 million times** the age of the universe" | 1.908 × 10¹⁶ ÷ 1.3787 × 10¹⁰ = **1.384 × 10⁶** → 1.4 million ✓. Holds for any age from 13.6 to 14.1 Gyr | Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters", *A&A* 641, A6 (2020), arXiv:1807.06209 | Table 2, age t₀ = 13.787 ± 0.020 Gyr | Paper identity SRC (S). The 13.787 value is **(K)**: the search did not return the table row. Auditor to open Table 2 |
| 7.2-i | "more than 8 billion people … more than **2 million years**" | UN: "nearly 8.2 billion by mid-2024". 6.022 × 10²³ ÷ 8.2 × 10⁹ = 7.344 × 10¹³ s ÷ 3.156 × 10⁷ = **2.33 × 10⁶ yr** ✓. The claim stays true until the population passes 9.5 billion (6.022 × 10²³ ÷ (2 × 10⁶ × 3.156 × 10⁷) = 9.54 × 10⁹) | UN DESA Population Division, *World Population Prospects 2024: Summary of Results* (released 11 July 2024) | population.un.org/WPP/Publications/Files/WPP2024_Key-Messages.pdf; desapublications.un.org/publications/world-population-prospects-2024-summary-results | SRC (S) + DER |
| 7.2-j | A mole of water "fills only about **18 mL**, a little more than a tablespoon" | 18.02 g ÷ 0.997 05 g/mL (25 °C) = **18.07 mL**. ÷ 14.787 mL/tbsp = **1.22 tbsp** ✓ | Water density: NIST Chemistry WebBook, "Thermophysical Properties of Fluid Systems" (Lemmon, McLinden & Friend), water at 25 °C, 1 atm: 0.997 05 g/cm³. Tablespoon: NIST Handbook 44 (2026), Appendix C, 1 US tbsp = 14.786 765 mL | webbook.nist.gov/chemistry/fluid/; nist.gov/document/2026-nist-handbook-44-appendix-c | Density (S, secondary tables citing the WebBook: 0.997 048 g/cm³). Tablespoon (S, secondary converter citing HB44; the HB44 row itself was not seen). Conclusion robust: even 15 mL/tbsp gives 1.2 |
| 7.2-k | Representative particles: atom (C, Fe); molecule (H₂O, O₂); formula unit (NaCl); NaCl is not made of molecules | Standard model. The Gold Book entity list covers atoms, molecules and ions | Gold Book M03980 | — | SRC (S). For "formula unit" see D8 |
| 7.2-l | Formula unit = lowest whole-number ratio of ions; NaCl = one Na⁺ + one Cl⁻ | Standard high-school definition; the snow-day key uses the same idea | `templates/snow_day/specs/chemistry.json` l.57 | — | SRC (classroom). No IUPAC Gold Book entry fetched (K) |
| 7.2-m | A mole of dollar bills shared equally among everyone on Earth gives each person about **$73 trillion** | 6.022 × 10²³ ÷ 8.2 × 10⁹ = **7.34 × 10¹³** → $73 trillion ✓. With 8.0 × 10⁹: $75 T; with 8.3 × 10⁹: $72.6 T. "About $73 trillion" is pinned to the UN 8.2 billion figure | UN WPP 2024 (7.2-i) | — | DER |

### 7.3 Molar Mass → new 7.2 (second half)

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 7.3-a | Molar mass of an element = the average atomic mass from the periodic table, read in g/mol; U1 used amu | U1 has 1.5 Average Atomic Mass | DECISIONS l.25–27; chem_data.py | — | SRC (curriculum) |
| 7.3-b | Carbon 12.01 g/mol; O₂ 32.00, not 16.00 | Student table: C 12.01, O 16.00; 2 × 16.00 = 32.00 ✓ | chem_data.py l.8 | — | SRC / DER |
| 7.3-c | Example: H₂O = 18.02 g/mol | 2 × 1.01 = 2.02; + 16.00 = **18.02** ✓ | chem_data.py | — | DER |
| 7.3-d | On Your Own: CH₄ = 16.05 g/mol | 12.01 + 4 × 1.01 = 12.01 + 4.04 = **16.05** ✓. IUPAC 16.043 → 16.04 (§B) | chem_data.py | — | DER |
| 7.3-e | "methane … the main gas in natural gas" | EIA: "the largest component of natural gas is methane"; glossary: "mostly methane"; EIA Kids: 73–95% | U.S. EIA, "Natural gas explained"; EIA Glossary | eia.gov/energyexplained/natural-gas/; eia.gov/tools/glossary/index.php?id=natural+gas | SRC (S) |
| 7.3-f | Figure 7.3: carbon 12.01 g, water 18.02 g, NaCl 58.44 g, each 6.022 × 10²³ atoms / molecules / formula units | 22.99 + 35.45 = **58.44** ✓ | chem_data.py l.11 | — | DER |
| 7.3-g | A US nickel has a mass of **5.00 g**; 200 g ÷ 5.00 g = 40 nickels | US Mint: five-cent coin "Cupro-Nickel 25% Ni, Balance Cu, 5.000 g"; 200 ÷ 5.00 = **40** ✓ | United States Mint, "Coin Specifications" and "Nickel" pages | usmint.gov/learn/coin-specifications; usmint.gov/learn/coins-and-medals/circulating-coins/nickel | SRC (S) + DER. The 200 g pile is ILL |
| 7.3-h | "a natural sample of an element has nearly the same mix of isotopes wherever it comes from" | CIAAW publishes *intervals* for elements whose normal materials vary, e.g. C [12.0096, 12.0116]: a spread of about 0.02%. Single values for most other elements | CIAAW, "Standard Atomic Weights" (Atomic Weights 2021; Gd, Lu, Zr revised 2024) | ciaaw.org/atomic-weights.htm; ciaaw.org/abridged-atomic-weights.htm | SRC (S). Optionally add "on Earth" (R3-2) |
| 7.3-i | Isotopes were taught in Unit 1 | 1.3 Atomic Structure (includes isotopes) | DECISIONS l.25–27 | — | SRC (curriculum) |
| 7.3-j | Reading Check key: water 18.02 vs carbon 12.01 | as above | — | — | DER |

### 7.4 Mole Conversions → new 7.3

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 7.4-a | N = n × 6.022 × 10²³. The reference sheet writes particles = n × N_A, with N_A = 6.022 × 10²³ particles per mole | "Particles: particles = n × N<sub>A</sub>"; "N<sub>A</sub> = 6.022 × 10<sup>23</sup> particles/mol" | Equations sheet (DECISIONS sheet 1 "Equations & Constants") | `build_reference.py` l.90, 119; DECISIONS l.185 | SRC (classroom). For the title wording see D5 |
| 7.4-b | Example: 36.0 g H₂O × (1 mol / 18.02 g) = **2.00 mol**; the calculator shows 1.99778… | 36.0 ÷ 18.02 = **1.997780…** → 3 sig figs (set by 36.0) → **2.00** ✓ | Reference sheet 2 ×/÷ rule, l.170–172 | — | DER |
| 7.4-c | **NEW: magnitude check** | Proposed sentence: "One mole of water is 18.02 g, and 36.0 g is about twice that, so an answer near 2 mol makes sense." Check: 36.0 ÷ 18.02 ≈ 36 ÷ 18 = 2 ✓ | — | — | DER |
| 7.4-d | On Your Own: 64.0 g O₂ → **2.00 mol** | 64.0 ÷ 32.00 = 2.000 → **2.00** (3 sig figs) ✓ | — | — | DER |
| 7.4-e | Wrong setup gives "grams squared per mole" | g × g/mol = g²/mol ✓ | — | — | DER |
| 7.4-f | Medicine box: at equal mass, the smaller molar mass delivers more molecules | n = m ÷ M, so at fixed m, a smaller M gives a larger n ✓. Logic only; no dosage data | — | — | DER |
| 7.4-g | Do **not** reuse 1.75 mol H₂O → 31.5 g | That is the worked example printed on the Equations sheet | `build_reference.py` l.140 | — | Info |

### 7.5 Percent Composition → new 7.4 (first half)

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 7.5-a | Method: % element = mass of element ÷ mass of compound × 100 | Same formula on the Equations sheet | `build_reference.py` l.86 | — | SRC (classroom) |
| 7.5-b | Water is **11.2% H, 88.8% O** by mass | 2.02 ÷ 18.02 = 0.112 10 → **11.2%**; 16.00 ÷ 18.02 = 0.887 90 → **88.8%**; sum 100.0 ✓. IUPAC: 2.016 ÷ 18.015 = 11.19% → 11.2 ✓ | chem_data.py; §B | — | DER |
| 7.5-c | Two of three atoms are H (two-thirds by count) | 2/3 = 66.7% ✓ | — | — | DER |
| 7.5-d | **112 g H and 888 g O per kg** of water | 0.1121 × 1000 = 112.1 → 112; 0.8879 × 1000 = 887.9 → 888; 112 + 888 = 1000 ✓ | — | — | DER |
| 7.5-e | "Splitting water is one way to make hydrogen fuel" | Water electrolysis is an established hydrogen production route | U.S. DOE Hydrogen and Fuel Cell Technologies Office, "Hydrogen Production: Electrolysis" | energy.gov/eere/fuelcells/hydrogen-production-electrolysis | **(K)**: not retrieved this session. Low risk. Auditor to open |
| 7.5-f | A pure compound has a constant percent composition (drop vs tank) | Law of definite proportions; standard | — | — | SRC (standard model). Naming the law is optional |

### 7.6 Empirical Formulas → new 7.4 (second half)

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 7.6-a | Glucose C₆H₁₂O₆ → CH₂O (÷6); H₂O₂ → HO; H₂O and CO₂ irreducible; NaCl already lowest ratio | Arithmetic on subscripts ✓ | — | — | DER. **See D2 about H₂O₂** |
| 7.6-b | "Glucose, the sugar carried in your blood" | MedlinePlus: blood glucose is "the main sugar found in your blood" and the body's main source of energy | NIH National Library of Medicine, MedlinePlus, "Blood Sugar" | medlineplus.gov/bloodsugar.html | SRC (S) |
| 7.6-c | Acetic acid, C₂H₄O₂, "the acid in vinegar" | FDA: vinegar "should contain 4 grams of acetic acid per 100 mL (20 °C)" | FDA, CPG Sec. 525.825 "Vinegar, Definitions" (March 1995) | fda.gov/regulatory-information/search-fda-guidance-documents/cpg-sec-525825-vinegar-definitions-adulteration-vinegar-eels | SRC (S) |
| 7.6-d | Formaldehyde, CH₂O, "a preservative" | ATSDR: used "in many hospitals and laboratories to preserve tissue specimens"; an embalming-fluid ingredient | ATSDR, *Public Health Statement for Formaldehyde* (and ToxFAQ, reviewed 12 May 2015) | wwwn.cdc.gov/TSP/PHS/PHS.aspx?phsid=218&toxid=39 | SRC (S). No health claim is printed or needed |
| 7.6-e | All three CH₂O compounds are 40.0% C | 12.01/30.03 = 24.02/60.06 = 72.06/180.18 = **0.3999** → 40.0% ✓ | — | — | DER |
| 7.6-f | Five-step method; step 4 multipliers (x.5 → ×2; x.33/x.67 → ×3; x.25 → ×4) | 1.5 × 2 = 3; 1.33 × 3 = 4; 1.67 × 3 = 5; 1.25 × 4 = 5 ✓ | — | — | DER |
| 7.6-g | New compounds: percent data is the first data chemists get; molar mass needs one more measurement | General statement, kept general per the brief (no instruments named) | brief §2 7.6 | — | SRC (P). Accepted as general |

### 7.7 Molecular Formulas → new 7.5

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 7.7-a | Glucose: CH₂O = **30.03**; 180.18 ÷ 30.03 = **6** | 12.01 + 2.02 + 16.00 = 30.03; 180.18 ÷ 30.03 = **6.0000** ✓ | chem_data.py | — | DER |
| 7.7-b | Acetylene **26.04** = 2 × 13.02; benzene **78.12** = 6 × 13.02; CH **13.02** | 2 × 13.02 = 26.04 ✓; 6 × 13.02 = 78.12 ✓ | chem_data.py | — | DER |
| 7.7-c | Both **92.2% C** | 12.01 ÷ 13.02 = **0.922 43** → 92.2% ✓ (24.02/26.04 and 72.06/78.12 give the same) | — | — | DER |
| 7.7-d | Acetylene "the gas burned in oxy-acetylene welding torches"; "a welding gas" | OSHA regulates acetylene under oxygen-fuel gas welding and cutting. PubChem-derived records list "welding gas" as a synonym. Oxy-acetylene is the hottest common fuel-gas flame | OSHA 29 CFR 1910.253 "Oxygen-fuel gas welding and cutting"; PubChem CID 6326 (via PubChemLite) | osha.gov/laws-regs/regulations/standardnumber/1910/1910.253; pubchemlite.lcsb.uni.lu/e/compound/6326 | SRC (S) |
| 7.7-e | Acetylene is a gas at room temperature | At 1 atm it sublimes at about −84 °C (189 K) and has no liquid phase | Air Liquide Gas Encyclopedia, "Acetylene" (sublimation −84.05 °C); NIST WebBook C74862 phase data | encyclopedia.airliquide.com/acetylene; webbook.nist.gov/cgi/cbook.cgi?ID=C74862&Mask=4 | SEC (S). NIST row not seen. Conclusion robust |
| 7.7-f | Benzene "a flammable liquid at room temperature" | Boiling point 80.1 °C (ATSDR, citing Budavari 2001; NLM 2023 gives 80.08 °C). ATSDR ToxFAQ describes benzene as highly flammable | ATSDR, *Toxicological Profile for Benzene*, Ch. 4 (Chemical and Physical Information), Table 4-2 | atsdr.cdc.gov/ToxProfiles/tp3-c4.pdf; ToxFAQ wwwn.cdc.gov/TSP/ToxFAQs/ToxFAQsDetails.aspx?faqid=38&toxid=14 | Boiling point SRC (S). "Flammable" excerpt **(K)**: wording not seen in the snippet |
| 7.7-g | Benzene "is a liquid used to make plastics such as polystyrene" | ATSDR: "Various industries use benzene to make other chemicals, such as styrene (for Styrofoam® and other plastics), cumene (for various resins), and cyclohexane (for nylon and synthetic fibers)." ToxFAQ (rev. Nov 2024): "used in industry as a solvent and to make other products such as plastics…" | ATSDR, *Public Health Statement: Benzene*; ATSDR ToxFAQ for Benzene (reviewed Nov 2024) | atsdr.cdc.gov/ToxProfiles/tp3-c1-b.pdf; wwwn.cdc.gov/TSP/ToxFAQs/ToxFAQsDetails.aspx?faqid=38&toxid=14 | SRC (S). Styrofoam® is a polystyrene foam, so "polystyrene" follows. Do **not** claim "largest use" (not sourced here). See D9 |
| 7.7-h | Water: multiplier 1. Ionic compounds have formula units, so no molecular formula | Standard model | — | — | SRC (standard model) |
| 7.7-i | "A molecule's size and structure … decide how a substance behaves" | U5 5.6 Structure & Physical Properties precedes U7 | DECISIONS l.46–48 | — | SRC (curriculum) |
| 7.7-j | Back-page Q3: about 26 → acetylene, about 78 → benzene; also accept gas vs liquid | as 7.7-b, e, f | — | — | DER |

---

## D. New worked examples and On Your Own items (data checked, solved)

All measured values in this section are **ILLUSTRATIVE** unless a source is given. Label them so in the teacher key.

### D1. 7.1 Example + On Your Own: a measured value converted with an exact factor

Every option uses 1 in = 2.54 cm, which is **exact** (§C 7.1-g). The measurement alone therefore sets the significant figures. Avoid lb ↔ g (D6).

| Option | Problem | Working | Answer | Sig-fig point |
|---|---|---|---|---|
| **A (Example, recommended)** | A sheet of notebook paper measures 27.9 cm long. How long is it in inches? | 27.9 cm × (1 in / 2.54 cm) = 10.984… in | **11.0 in** | 27.9 has 3 sig figs, and 2.54 is exact, so 3 sig figs. The trailing zero in 11.0 is significant because it has a decimal point (Reference sheet 2, l.165). Plausible: US letter paper is 11 in (K, not sourced) |
| **B (Example, alternative)** | A student's height is measured as 64.0 in. What is it in centimeters? | 64.0 in × (2.54 cm / 1 in) = 162.56 cm | **163 cm** | 3 sig figs, so you round. The calculator's 162.56 shows the "don't copy the display" point |
| **On Your Own (pairs with A or B)** | A bolt is measured as 0.75 in long. How long is it in centimeters? | 0.75 in × (2.54 cm / 1 in) = 1.905 cm | **1.9 cm** | 0.75 has 2 sig figs: the leading zero doesn't count (Reference sheet 2, l.164). A changed condition from the Example (different direction, fewer sig figs), as the IES guidance recommends |

Duplication check: none of 27.9 cm, 64.0 in or 0.75 in appears in any `*chem_u07*` spec (grep of `templates/`).

### D2. 7.4 Example: empirical formula from 40.0% C, 6.7% H, 53.3% O

Student table: C 12.01, H 1.01, O 16.00. The percentages total 40.0 + 6.7 + 53.3 = 100.0 ✓.

| Step | C | H | O |
|---|---|---|---|
| 1. Assume 100 g | 40.0 g | 6.7 g | 53.3 g |
| 2. ÷ atomic mass | 40.0 ÷ 12.01 = **3.331** mol | 6.7 ÷ 1.01 = **6.634** mol | 53.3 ÷ 16.00 = **3.331** mol |
| 3. ÷ smallest (3.331) | 1.000 | 1.992 | 1.000 |
| 4. Round | 1 | 2 | 1 |
| 5. Formula | **CH₂O** ✓ | | |

Unrounded: C 3.330 558, O 3.331 250, H 6.633 663. Dividing by 3.330 558 gives C 1.0000, H 1.9918, O 1.0002.

- **Data origin:** these percentages are what CH₂O gives with the student table: C 12.01/30.03 = 39.99%; H 2.02/30.03 = 6.727%; O 16.00/30.03 = 53.28%. Label it as "data for a compound with the formula CH₂O". It is DER, not measured.
- **H precision:** 6.7 has 2 sig figs. That is fine for step 4, since 1.99 rounds clearly to 2. Printing 6.73 instead would make the total 100.03.
- **Link to 7.5:** the result matches the CH₂O family in the same section (glucose, acetic acid, formaldehyde), and 7.5 then uses glucose 180.18 ÷ 30.03 = 6.

### D3. 7.4 On Your Own: different clean data (choose 1; both solved)

| Option | Given | Step 2 (mol in 100 g) | Step 3 (÷ smallest) | Step 4 | Answer | Data check |
|---|---|---|---|---|---|---|
| **A (straight rounding)** | 85.6% C, 14.4% H | C 85.6 ÷ 12.01 = 7.127; H 14.4 ÷ 1.01 = 14.257 | C 1.000; H 2.000 | — | **CH₂** | CH₂ = 14.03: C 12.01/14.03 = 85.60%; H 2.02/14.03 = 14.40%; sum 100.0 ✓. The CH₂ family includes ethylene C₂H₄ and cyclohexane C₆H₁₂, so this sets up 7.5 |
| **B (uses the x.5 → ×2 step)** | 69.9% Fe, 30.1% O | Fe 69.9 ÷ 55.85 = 1.2516; O 30.1 ÷ 16.00 = 1.8813 | Fe 1.000; O 1.503 | ×2 gives Fe 2, O 3.006 | **Fe₂O₃** | Fe₂O₃ = 111.70 + 48.00 = 159.70: Fe 69.94%, O 30.06% → 69.9 / 30.1, sum 100.0 ✓. This is iron(III) oxide, which links to U6 6.3 naming. It is ionic, so call the result the formula of the compound's formula unit. Do not call it "rust" (rust is hydrated and variable; not sourced) |

Recommendation: use **B** if step 4 should be practiced (the reading says rounding 1.5 up is the common mistake), or **A** if 7.5 should reuse CH₂. Neither duplicates a sibling spec (grep).

### D4. 7.5 Example and On Your Own

**Example: glucose.**
- CH₂O = 12.01 + 2(1.01) + 16.00 = **30.03 g/mol**.
- 180.18 ÷ 30.03 = **6.000**, so the multiplier is 6.
- CH₂O × 6 = **C₆H₁₂O₆** ✓.
- Teacher note: published sources give glucose 180.16, and the student table gives 180.18 (§B).

**On Your Own, as requested: empirical HO, molar mass 34.02 g/mol.**
- HO = 1.01 + 16.00 = **17.01 g/mol**.
- 34.02 ÷ 17.01 = **2.000**, so the multiplier is 2.
- The answer is **H₂O₂** ✓.
- Published value: 34.01 (PubChem CID 784: 34.014–34.015).
- **Blocked by D2** while the 7.4 prose names H₂O₂ → HO.

**On Your Own, alternative that avoids D2 (recommended): empirical CH₂, molar mass 28.06 g/mol.**
- CH₂ = 12.01 + 2.02 = **14.03 g/mol**.
- 28.06 ÷ 14.03 = **2.000**.
- The answer is **C₂H₄** (ethylene).
- Published: 28.05 (IUPAC 28.054). Add this to the teacher note.
- A context line such as "ethylene, used to make polyethylene" is **not sourced in this dossier** and would need a locator first. Printing the bare formula needs none.
- Harder variant: molar mass 84.18 → 84.18 ÷ 14.03 = 6.000 → C₆H₁₂.

### D5. 7.3 one-sentence magnitude check

"One mole of water has a mass of 18.02 g, and 36.0 g is about twice that, so the answer should be close to 2 mol." Check: 2 × 18.02 = 36.04 ≈ 36.0 ✓. This matches the workflow's Chemistry row, which asks for "a magnitude check".

---

## E. Two structural checks requested

| Check | Result | Evidence |
|---|---|---|
| Was "formula unit" introduced in an earlier unit (U4/U6)? | **No evidence that it was.** Define it in full at first use in 7.2. See D8 for what was and wasn't searched | DECISIONS l.42–52; U4 notes spec l.30–37; roadmaps chem_u04/u06; snow_day l.57 |
| "Reference Sheet 1, Equations & Constants" | **Number and DECISIONS title match** (DECISIONS l.183). **The printed headings differ**: the builder prints "Equations" and "Constants & Conversions", and no sheet number (D5) | DECISIONS l.177–196; build_reference.py l.157–158 |
| "Reference Sheet 2, Significant Figure Rules" | **Matches** DECISIONS l.196 and the printed heading (build_reference.py l.186). No number is printed | as above |

---

## F. UNVERIFIED or not opened (do not print as fact without the locator)

- Exact CODATA digits of the molar mass constant (§B note). The claim "differs by less than about 1 part in 10⁹" is (K).
- Planck 2018 Table 2 age value 13.787 Gyr: (K). The comparison holds for 13.6–14.1 Gyr.
- NIST HB44 tablespoon row and the NIST WebBook water-density row: values seen only through secondary pages that cite them.
- "Flammable" wording in the ATSDR benzene ToxFAQ: (K).
- DOE electrolysis page (7.5-e): (K).
- VIM 2.15 and 4.14 wording (7.1-e): carried from Round 1, not re-opened.
- Ream = 500 sheets (7.2-a): (K).
- Any context line for ethylene, or "rust" for Fe₂O₃: not sourced. Do not print.
- Still excluded from the brief: who coined "Avogadro's number" as a printed fact (sourced here to Perrin 1909, but deliberately not printed); "mole of marbles or sand" comparisons; fertilizer-bag N-P-K wording; Ohio standard codes.

## G. Observation versus inference

- **Observed:** the spec text, line numbers, DECISIONS entries, the builder headings, the chem_data.py values, and search-result excerpts for each (S) locator.
- **Inferred:** that the built Reference PDF prints the builder headings and no sheet numbers (D5; PDF not opened); that "never knew its value" follows from the 1856 and 1865 dates; that Styrofoam® implies polystyrene.
- **Not observed:** the primary pages on bipm.org, physics.nist.gov and ciaaw.org, which were blocked this session. Their locators come from search excerpts and earlier rounds.
