# Chemistry U7 Unit Reading: verify-content on the BUILT packet and key

Prepared by: researcher (verify-content, audit mode) | Date: 2026-11-24 | Status: REPORT ONLY. No file was edited except this report.

**Checked:**
- `build/chem_u07_reading/Unit 7 Reading - The Mole.pdf`: all 8 pages, read as rendered images
- `build/chem_u07_reading/Unit 7 Reading Key - The Mole.pdf`: both pages
- `templates/reading/specs/chem_u07_reading.json`
- `templates/reading/specs/make_chem_u07_figures.py`: SMILES and figure values
- Figure PNGs 7.1, 7.5 and 7.7, viewed directly. Figures 7.2, 7.3, 7.4 and 7.6 were checked as they appear in the PDF.

**Checked against:**
- `templates/reference/chem_data.py` (student periodic table)
- `templates/reference/build_reference.py` lines 90, 119 and 162–168 (Reference Sheet 2 rules)
- `courses/chemistry/DECISIONS.md` lines 46–56, 74, 184 and 195
- `reports/chem_u07_reading_content_brief.md`

I re-solved every number myself. I did not open the `.docx` files separately. The PDF is the checked rendering.

**Result:** 0 Critical, 2 Major, 9 Minor.

## Findings (blocking first, then by fix time)

| # | Item | Finding | Evidence (page, exact quote) | Severity | Recommendation |
|---|---|---|---|---|---|
| 1 | 7.1 scale example vs "more digits" | **The claim is false as printed.** "150 lb" and "12.4 g" both have three digits, so the kitchen scale does not give "more digits". **It also clashes with Reference Sheet 2.** The sheet says trailing zeros with no decimal point are not significant ("1500 → 2", "150. → 3"). By the students' own rules, "150 lb" has 2 sig figs, which would mean a scale that reads to the nearest 10 lb. That contradicts "It reads in whole pounds". **Cause:** fineness shows in the *place value of the last digit*, not in how many digits there are. The brief's version (same bag of sugar, 5 lb vs 2271 g) did not have this problem. | p.1: "A bathroom scale might say you weigh 150 lb. It reads in whole pounds … The kitchen scale gives you more digits because it measures more finely." build_reference.py l.165–166 | **Major** | Use a weight that does not end in zero, for example "148 lb … can't tell 148 lb from 148.4 lb". Replace the claim with "The kitchen scale's last digit is in the tenths place, so it measures more finely." |
| 2 | Definition of **precision** (text, vocab, key) | **Two problems.** (a) "Shows in how many digits" has the same digit-count error as #1. (b) The two meanings are in the wrong order of standing. The main definition, fineness, is what metrology calls *resolution*. The standard definition is the one in the parenthetical: closeness of agreement among repeated measurements (BIPM VIM 2.15). That is also what high-school accuracy-vs-precision ("dartboard") items test. "Scientists also use the word for…" makes the standard meaning sound secondary. **Not conflated with accuracy:** accuracy appears nowhere, which is correct. The key says Matt asked for both meanings, so keep both and fix the wording only. | p.1: "**Precision** describes how finely a measurement is made, and it shows in how many digits a tool lets you record. (Scientists also use the word for how closely repeated measurements agree with each other.)" Spec l.47–48; key p.2 vocab | **Major** | Text: "**Precision** describes how finely a tool measures, which shows in the place value of the last digit you can record. It also describes how closely repeated measurements agree with each other." Vocab and key: change "how many digits the tool lets you record" to "the smallest place value the tool lets you record". Keep "Also accept". Matt to confirm. |
| 3 | 7.1 "number of digits" sentence | **Same digit-count wording as #1 and #2.** **Risk of a mix-up with sig figs.** By the Reference Sheet 2 ×/÷ rule, 12.5 × 3.299 gives $41.2 (3 sig figs). The cent rounding is a money convention, which brief F11 warned about. **Arithmetic checks out:** 12.5 × 3.299 = 41.2375, and rounding to the cent gives $41.24. | p.1: "The number of digits in a value tells you how finely it was measured or set." | Minor | "The place value of the last digit tells you how finely it was measured or set. Money is rounded to the cent by rule, not by significant figures." |
| 4 | Q3 exemplar is incomplete | **A second correct answer comes straight from the reading.** 7.7 says acetylene is a gas and benzene is a liquid at room temperature, so looking at its physical state would also settle the question. The key accepts only molar mass, so a sharp student could be marked wrong. | p.6: "Acetylene, C₂H₂, is the gas … Benzene, C₆H₆, is a flammable liquid at room temperature." p.7 Q3: "What one measurement would settle it". Key p.2 | Minor | Option 1: add to the key "Also accept physical state (gas vs liquid), then steer to molar mass as the chemistry answer". Option 2: reword the stem to "Using only lab-report data (percent composition, molar mass)…". |
| 5 | Particle equation has no unit | **The equation breaks the page's own units rule.** 7.4 says "put a unit on every number" and "Let the units check your setup". In N = n × 6.022 × 10²³, mol × a bare number leaves mol, not particles. Reference Sheet 1 writes N_A = 6.022 × 10²³ **particles/mol**. **The bridge itself is accurate and the notation is used consistently.** N = n × 6.022 × 10²³ appears once, "multiply/divide by Avogadro's number" is used everywhere else, and the reference sheet does write "particles = n × N_A" (l.90). | p.4: "N = n × 6.022 × 10²³" … "N_A is just a symbol for Avogadro's number, 6.022 × 10²³." | Minor | Keep Matt's form. Add the unit to the bridge sentence: "N_A is just a symbol for Avogadro's number, 6.022 × 10²³ particles per mole." Optionally name "Reference Sheet 1, Equations & Constants", matching the 7.1 reference to Sheet 2. |
| 6 | Vocab "empirical formula mass" | **A student could leave out the subscripts.** Read literally, the definition lets a student add C + H + O once for CH₂O and get 29.02 instead of 30.03. | Spec l.123; p.6; key p.2: "the sum of the atomic masses in the empirical formula" | Minor | "the sum of the atomic masses of all the atoms in the empirical formula (count each subscript)". |
| 7 | 7.6 step 4 rounding cue | **Common cases are missing.** x.67 (×3) and x.25 (×4) are left out. x.67 is a common textbook case, for example C₃H₈ gives H 2.67. | p.5: "If a value lands near x.5 or x.33, multiply all of the values by 2 or 3" | Minor | "near x.5, x.33 or x.67, or x.25, multiply all of the values by 2, 3 or 4". |
| 8 | Figure 7.5 water drawing | **The angle drawn is about 120°.** H at (370,70), O at (525,160) and H at (680,70) in the PNG measure 119.7°, because that is RDKit's 2D default. U5 (5.2–5.3 VSEPR, taught before U7) teaches 104.5°. The caption makes no claim about the angle. **Chemistry is otherwise correct:** SMILES `[H]O[H]` gives 2 H, and the drawing is bent. | fig7_5_water_percent.png; `make_chem_u07_figures.py` l.320 | Minor | Leave as is, or set 2D coordinates nearer 104.5°. Do not add an angle label. |
| 9 | Example 7.2 calculator display | **Inconsistent with 7.1.** 7.1 says the calculator shows as many digits as its screen holds, but here it "shows" a 5-digit number. 36.0 ÷ 18.02 = 1.997780… **The answer is right:** 2.00 mol (3 sig figs, set by 36.0). | p.4: "The calculator shows 1.9978." | Minor | "The calculator shows 1.99778…" |
| 10 | 7.2 world population | **The figure is going stale.** UN WPP 2024 gives "nearly 8.2 billion in mid-2024". By late 2026 the figure is about 8.3 billion. The conclusion still holds: 6.022 × 10²³ ÷ 8.3 × 10⁹ s = 2.3 million years, which is "more than 2 million". | p.3: "the roughly 8.2 billion people on Earth" | Minor | "the more than 8 billion people on Earth" (stays true). |
| 11 | Stale render in `build/chem_u07_reading/png/` | **A leftover render from an older build.** `s-1…s-9.png` show a 9-page student copy, with the vocab page numbered "09". The current PDF has 8 pages. This is not a content error, but someone could QA the wrong pages. | png/s-9.png footer "09" | Minor (housekeeping) | Regenerate or remove the PNGs before the visual audit, so QA looks at the 8-page build. |

## Specific confirmations requested (all PASS unless noted)

| Check | Result | Working / evidence |
|---|---|---|
| SMILES H₂O | PASS | `[H]O[H]`: O with 2 explicit H. Drawn bent, about 120° (see #8) |
| SMILES C₂H₂ | PASS | `[H]C#C[H]`: drawn H–C≡C–H, 2 H, each C has 4 bonds |
| SMILES C₆H₆ | PASS | `[H]c1c([H])c([H])c([H])c([H])c1[H]` gives 6 C and 6 H. Drawn as a valid Kekulé ring: 3 alternating C=C, every C has 4 bonds, 6 H shown. Bond orders are U5 prior knowledge (U5 comes before U7 in DECISIONS l.46–48) |
| Glucose / CH₂O figure | PASS | Fig 7.6 shows formulas only, no structure drawing. C₆H₁₂O₆ ÷ 6 = CH₂O. Acetic acid C₂H₄O₂ ÷ 2 = CH₂O. Formaldehyde = CH₂O |
| 150 lb / 12.4 g | **FAIL** (#1) | Digit counts are equal; "150" has 2 sig figs under Reference Sheet 2 |
| $3.299 × 12.5 | PASS (framing Minor #3) | 39.588 + 1.6495 = 41.2375, which rounds to $41.24 |
| Ruler 4.6 / 4.63 cm | PASS | The figure tip is drawn at 4.63 cm. The cm-only ruler reads 4.6 (2 sig figs). The mm ruler reads 4.63 (3 sig figs). Labels "4 is certain, 6 is estimated" and "4.6 is certain, 3 is estimated" are correct. "A little more than halfway to 5" matches the figure |
| 4.6382 cm Reading Check | PASS | 4 decimal places is ten-thousandths, as the text says. The key answer is correct and matches the student question word for word |
| Precision definition | **Major** (#2) | Not conflated with accuracy. Wording and ordering are the problem |
| N = n × 6.022 × 10²³ and N_A bridge | PASS (Minor #5) | Consistent. The bridge matches build_reference.py l.90 |
| No molar volume / 22.4 / STP / liters | PASS | Grep of the spec finds none. None in the PDF |
| No UNVERIFIED item printed | PASS | None printed: no "who named it", no marble/sand comparison, no fertilizer, no standard codes. The scale resolutions are framed as "might" (illustrative) |
| No untaught calculation | PASS | Q2 uses 58.44 g, printed in Fig 7.3. Q3 uses 26/78, printed in 7.7. The Reading Checks are conceptual |
| Key matches student | PASS | All 7 RC stems, the Q1–3 stems and all 16 vocab terms and sections are identical. The vocab definitions come from the same spec |
| Unit title / codes | PASS | "The Mole & Chemical Quantities" and 7.1–7.7 titles match DECISIONS l.54–56 |

## Numbers re-solved (all PASS, student table H 1.01 · C 12.01 · O 16.00 · Na 22.99 · Cl 35.45)

| Item | Printed | Re-solved |
|---|---|---|
| 602,200,000,000,000,000,000,000 | = 6.022 × 10²³ | 8 groups of 3 = 24 digits, which matches 10²³ |
| One water molecule | 2.99 × 10⁻²³ g | 18.02 ÷ 6.022 × 10²³ = 2.992 × 10⁻²³ |
| Counting time | 19 quadrillion yr; 1.4 million × universe age | 6.022e23 ÷ 3.156e7 = 1.908e16 yr; ÷ 1.38e10 = 1.38e6 |
| 8.2 billion counting | > 2 million yr | 7.34e13 s ÷ 3.156e7 = 2.33e6 yr |
| 1 mol water volume | about 18 mL, a little more than 1 tbsp | 18.02 ÷ 0.997 = 18.07 mL; ÷ 14.79 = 1.22 tbsp |
| SI 2019 value | 6.022 140 76 × 10²³ exactly | BIPM SI Brochure 9th ed. |
| Nickel | 5.00 g; 200 g gives 40 | US Mint 5.000 g; 200 ÷ 5.00 = 40 |
| O₂ | 32.00 | 2 × 16.00 |
| H₂O | 18.02 | 2.02 + 16.00 |
| NaCl | 58.44 | 22.99 + 35.45 |
| 36.0 g H₂O | 2.00 mol | 1.99778 gives 2.00 (3 sig figs) |
| g × g/mol | "grams squared per mole" | g²/mol |
| 3 dozen × (1 dozen/12 eggs) | "dozen squared per egg" | dozen²/egg |
| Water % H / % O | 11.2 / 88.8 | 2.02/18.02 = 0.1121; 16.00/18.02 = 0.8879 |
| 2 of 3 atoms | 67% | 66.7 |
| H per kg water | about 112 g | 0.112 × 1000 |
| CH₂O % C (all three compounds) | 40.0% | 12.01/30.03 = 24.02/60.06 = 72.06/180.18 = 0.3999 |
| CH₂O / glucose | 30.03; 180.18 ÷ 30.03 = 6 | 12.01 + 2.02 + 16.00; 6.000 |
| CH | 13.02 | 12.01 + 1.01 |
| C₂H₂ / C₆H₆ | 26.04 = 2×; 78.12 = 6× | 24.02 + 2.02; 72.06 + 6.06 |
| % C (both) | 92.2% | 12.01/13.02 = 0.9224 |
| Key note IUPAC | glucose 180.16, benzene 78.11 | 72.066 + 12.096 + 95.994 = 180.156; 72.066 + 6.048 = 78.114 |
| 1 in | exactly 2.54 cm | International yard and pound agreement, 1959 |

## Observation vs inference

- **Observed:** the key says precision was bolded "at your request". I have no record of that request in the repo. It conflicts with brief §2, which said precision should be informal and not bold, because it is not in DECISIONS. Treated as Matt's instruction (precedence 1). Flagged only so Matt can confirm.
- **Inferred:** the stale 9-page PNG set comes from an earlier build. It is not referenced by the spec.

---

## Round 2: rebuilt packet (2026-11-24)

**Checked:**
- The rebuilt student PDF: all 8 pages, read as rendered images
- The rebuilt key PDF: both pages
- The current `templates/reading/specs/chem_u07_reading.json`

**Checked against:**
- `chem_data.py` and Reference Sheet 2 rules (`build_reference.py` l.162–168)
- DECISIONS U1 (isotopes folded into 1.3, l.25–27) and U5 (l.46–48)

I re-solved every new number. I did not open the `.docx` separately.

**Result:** 0 Critical, 1 Major, 4 Minor. 10 of the 11 Round 1 findings are fixed. Round 1 #8, the figure angle, is optional and unchanged.

### Round 2 findings

| # | Item | Finding | Evidence (page, exact quote) | Severity | Recommendation |
|---|---|---|---|---|---|
| R2-1 | 7.7 Connection: benzene as a solvent | **Outdated, and it touches safety.** Benzene is a known human carcinogen: IARC Group 1, with an OSHA benzene standard (29 CFR 1910.1028) setting a PEL of 1 ppm. Its use as a general solvent has been largely phased out. Most benzene today is a feedstock for other chemicals, for example benzene → ethylbenzene → styrene → polystyrene. Saying in the present tense that it "is used as a liquid solvent" describes a past use as current. It could also suggest benzene is an ordinary lab or shop solvent. The brief said to add no health claims, and that still holds: the fix is to change the use, not to add a warning. | p.6: "Acetylene is a welding gas, and benzene is used as a liquid solvent." | **Major** | "Acetylene is a welding gas, and benzene is a liquid used to make plastics such as polystyrene." Keep the rest of the box. Its chemistry is correct: same 1 : 1 C:H ratio, acetylene is a gas (sublimes at −84 °C) and benzene is a liquid (boils at 80.1 °C), and "size and structure" decide this, which is U5 5.6 prior knowledge. |
| R2-2 | Why It Matters: two overstated phrases | (a) "they react by count, one particle at a time" is not quite right: particles react in fixed whole-number ratios by count, not "one at a time". (b) "a chemist can only weigh things on a balance" overstates it, since chemists also measure volumes. The baking-soda example is fine: too little gives poor rise, and too much gives a soapy, bitter taste. | p.1: "they react by count, one particle at a time … a chemist can only weigh things on a balance" | Minor | (a) "they react in fixed ratios by count". (b) "and in the lab a chemist measures amounts by weighing them on a balance". |
| R2-3 | 7.3 Connection: isotopes and average atomic mass | **Only half of the reason is given.** An average atomic mass works because (1) a sample holds an enormous number of atoms, **and** (2) natural samples of an element contain nearly the same mix of isotopes. The printed reason gives only (1). The U1 isotope reference is valid: isotopes are taught inside 1.3 (DECISIONS l.25–27). | p.4: "chemists use the average atomic mass, which works because even a tiny sample holds an enormous number of atoms." | Minor | "…which works because a natural sample of an element has nearly the same mix of isotopes, and even a tiny sample holds an enormous number of atoms." |
| R2-4 | On Your Own 7.3: CH₄ value from published sources | **Students who look it up will see a different number.** Published sources using IUPAC values give 16.04 g/mol (12.011 + 4 × 1.008 = 16.043). This is the same issue as glucose and benzene, which the key already explains in a teacher note, but CH₄ is not mentioned. The printed 16.05 is correct for the student table. | Key p.1 OYO 7.3: "16.05 g/mol". Teacher notes cover glucose and benzene only | Minor | Add "methane 16.05 (student table) vs 16.04 (IUPAC)" to the existing glucose/benzene teacher note. Do not add it to the student page. |
| R2-5 | Fig 7.5 water angle (Round 1 #8) | Unchanged. It is still drawn at about 120°. | p.5 | Minor (optional) | Same as Round 1 #8. |

### Round 2 confirmations (all PASS unless noted)

| Check | Result | Working / evidence |
|---|---|---|
| 7.1 Connection: "12.4382 g … 1,000 times finer" | PASS | The last digit of 12.4382 is in the 0.0001 g place, and the scale reads to 0.1 g. 0.1 ÷ 0.0001 = 1,000 ✓. Rounding to 12.4 g is correct |
| 7.2 Connection: about $73 trillion per person | PASS | 6.022 × 10²³ ÷ 8.2 × 10⁹ = 7.34 × 10¹³. With 8.3 × 10⁹ it is 7.26 × 10¹³. Both round to about $73 trillion. This fits the text's "more than 8 billion" (8.0 × 10⁹ would give $75 trillion, so "about" is fair) |
| 7.3 Connection: nickels | PASS (R2-3) | 200 ÷ 5.00 = 40. "Every nickel has the same mass" is fine at this level (US Mint 5.000 g) |
| 7.4 Connection: medicine | PASS | n = m ÷ M, so at equal mass, a smaller M gives a larger n, and more molecules ✓. "Do not hold equal numbers" is true unless the molar masses are equal; fine at this level |
| 7.5 Connection: 112 g H / 888 g O per kg | PASS | 0.112 × 1000 = 112. 0.888 × 1000 = 888. 112 + 888 = 1000 ✓ |
| 7.6 Connection: percent data first | PASS | Consistent with brief §2 7.6 (kept general, no instruments named) |
| 7.7 Connection: same ratio, different state | **Major** (R2-1) for "solvent"; the rest PASS | See R2-1 |
| On Your Own 7.3: CH₄ | PASS | 1 × 12.01 + 4 × 1.01 = 12.01 + 4.04 = **16.05 g/mol**. Addition rule: both terms have 2 decimal places, so 16.05 ✓. "Methane, the main gas in natural gas" is correct (methane is the major component) |
| On Your Own 7.4: 64.0 g O₂ | PASS | 64.0 ÷ 32.00 = 2.000. 3 sig figs (set by 64.0) gives **2.00 mol** ✓. The key note is correct. Uses the O₂ molar mass printed in 7.3 (32.00). No untaught step |
| On Your Own: no duplication with sibling specs | PASS | Neither CH₄ nor 64.0 g appears in any other `*chem_u07*` spec |
| On Your Own: key matches student | PASS | Stems are identical. Key steps match the Example 7.3 / 7.4 layout. Examples are renumbered 7.3 and 7.4 consistently in the text, the stems and the key |
| Definition lines vs `spec.vocab` | PASS | All 16 lines on student pp.1–6 match the `vocab[].def` strings word for word (only the first letter is capitalised), including precision ("…shown by the place value of the last digit it can record; also, how closely repeated measurements agree with each other") and empirical formula mass ("…(count each subscript)"). Key p.2 vocab matches too |
| Round 1 #1 scale (148 lb / 12.4 g, place value) | FIXED | p.1 |
| Round 1 #2 precision wording | FIXED | p.1–2, both meanings, place value; key note updated |
| Round 1 #3 gas pump framing | FIXED | p.2 "money is rounded to the cent by rule" |
| Round 1 #4 Q3 accept | FIXED | Key p.2 "Also accept: state (gas vs liquid)" |
| Round 1 #5 N_A unit / sheet name | FIXED | p.4 "Reference Sheet 1 … 6.022 × 10²³ particles per mole" |
| Round 1 #6 empirical formula mass | FIXED | Text, definition line and key |
| Round 1 #7 x.67 / x.25 | FIXED | p.6 step 4 |
| Round 1 #9 calculator 1.99778… | FIXED | p.4 |
| Round 1 #10 population | FIXED | p.3 "more than 8 billion people" |
| Round 1 #11 stale PNGs | FIXED | `build/chem_u07_reading/png/` is now empty |
| No molar volume / STP / UNVERIFIED / standard codes | PASS | None found in the rebuilt spec or PDF |
| Every other unchanged fact and number | PASS | Re-checked against the Round 1 tables. Values unchanged |

---

## Round 3: rebuilt packet (2026-11-24)

**Checked:**
- The current spec (`why.text`, the 7.3 and 7.7 connections, `key.teacherNotes`)
- Student PDF p.1, as a rendered image
- The regenerated `build/chem_u07_reading/fig/fig7_5_water_percent.png`, viewed directly

This is a short round covering only the six claims listed below.

**Result:** 0 Critical, 0 Major, 1 Minor. Everything else passes.

| # | Claim | Result | Working / evidence | Severity | Recommendation |
|---|---|---|---|---|---|
| R3-1 | 7.7: "benzene is a liquid used to make plastics such as polystyrene" | PASS | Accurate and current. Benzene + ethylene → ethylbenzene → styrene → polystyrene, and making styrene is one of benzene's largest uses. There is no health claim, as the brief requires. Fixes R2-1 | — | None |
| R3-2 | 7.3: "a natural sample of an element has nearly the same mix of isotopes wherever it comes from" | PASS | True at high-school level. The IUPAC standard atomic weights depend on this. "Nearly" covers the small natural variation, for which IUPAC gives ranges for elements such as H, Li, B, C, N, O, S and Cl. Fixes R2-3. Optionally add "on Earth" for strictness; not needed | — | None (optional "on Earth") |
| R3-3 | Why It Matters close: "extra of one ingredient is wasted and too little of it leaves some of the others unused" | PASS on the idea; wording Minor | The idea is right: it previews limiting and excess reactants. Two wording points. (a) "Wasted" is too strong for the fertilizer example. In ammonia synthesis (Haber–Bosch), the unreacted N₂ and H₂ are recycled, so the excess is left over, not necessarily wasted. (b) "Mixing a solution" is not a reaction. There, the right amount matters for concentration, not for leftover ingredients. The sentence still reads acceptably as a general statement. | Minor | "…because extra of one ingredient is left over and too little of it leaves some of the others unused." |
| R3-4 | Why It Matters: "react in fixed ratios by count" and "in the lab a chemist measures amounts by weighing them on a balance" | PASS | Both are accurate and match R2-2's recommendation word for word. Rendered on p.1 | — | None |
| R3-5 | Key note: methane 16.05 (student table) vs 16.04 (IUPAC) | PASS | IUPAC values: 12.011 + 4 × 1.008 = 16.043, which rounds to 16.04. Student table: 12.01 + 4.04 = 16.05. Added to the existing glucose/benzene note, key only. Fixes R2-4 | — | None |
| R3-6 | Fig 7.5: H–O–H angle on the regenerated PNG | PASS | By eye on the 1050 px PNG, I read the bond lines as roughly (398,72)→(505,153) and (545,153)→(652,72). Each is about 52.9° from vertical (atan 107/81), so about 106° in total. From the atom label centres, H (380,60), O (523,170), H (668,60), I get about 105°. This was done by eye, with no image analysis run, so treat it as ±3°. That is consistent with the designer's 104.8° and with the true value of 104.5°. Earlier it was about 120°, so this fixes Round 1 #8 / R2-5. The labels H, H, O and 2 H are correct | — | None |

**Open after Round 3:** R3-3 wording only (Minor). Every earlier finding is closed.
