# Chemistry U7 "The Mole & Chemical Quantities": Unit Reading Packet Content Brief

Prepared by: researcher (verify-content, brief mode) | Date: 2026-11-24 | Status: RECOMMENDATIONS ONLY. Nothing in `brand/`, `standards/`, `governance/`, `courses/` or `templates/` was edited, and nothing was built.

**Scope check.** The section codes are confirmed in `courses/chemistry/DECISIONS.md` lines 54–56: 7.1 Mathematical Tools · 7.2 The Mole & Avogadro's Number · 7.3 Molar Mass · 7.4 Mole Conversions · 7.5 Percent Composition · 7.6 Empirical Formulas · 7.7 Molecular Formulas. Molar volume belongs to 11.5 (DECISIONS line 74), so it is left out of this packet.

**Sources used.**
- **Atomic masses:** the student periodic table, `templates/reference/chem_data.py` lines 4–11 (2 decimals per DECISIONS line 200). Values: H **1.01**, C **12.01**, N 14.01, O **16.00**, Na **22.99**, Mg 24.31, Al 26.98, Cl **35.45**, Ca 40.08.
- **Sig-fig rules:** `templates/reference/build_reference.py` lines 160–179.
- **Constants and dimensional-analysis template:** `build_reference.py` lines 119–140.
- **Mole definition:** BIPM SI Brochure, 9th ed. (2019), §2.3.1, effective 20 May 2019. "One mole contains exactly 6.022 140 76 × 10²³ elementary entities." Quoted via IUPAC Gold Book M03980, https://goldbook.iupac.org/terms/view/M03980, and BIPM https://www.bipm.org/en/si-base-units/mole.

I re-solved every number below myself. None was copied from a key.

---

## 0. Findings (blocking first, then by fix time)

| # | Item | Finding | Evidence | Severity | Recommendation |
|---|---|---|---|---|---|
| F1 | Doc type for the packet | `standards/NAMING.md` has no "Reading" type. The list is Slides · Guided_Notes · Practice_Set · Quiz · Test · Lab · Study_Guide · Reference · Key · Rubric · Activity · Organizer · Roadmap. | NAMING.md line 53–54; repo-wide grep found no "Reading" doc type | **Blocking for filing** (not for content) | Secretary proposes a type (for example `Reading`) or Matt picks an existing one before the file is named and filed. Do not invent a filename. |
| F2 | Molar volume in sibling specs | The 7.4 worksheet spec and the U7 unit-test spec both teach and test 22.4 L/mol. Locations: worksheet "gas at STP" equation and the 11.2 L O₂ challenge; unit test Day 2 equation box, problem A5 (N₂ 5.60 L) and B5 (O₂ 8.96 L), and the d1-2 rationale ("two constants introduced the same week"). DECISIONS puts molar volume in **11.5**. Matt has confirmed it is OUT for this packet. | `templates/worksheet/specs/chem_u07_s07.4.json` lines 27–32, 129–137; `templates/assessment/specs/chem_u07_unit_test.json` lines 49, 336–341, 404–423, 486–503; DECISIONS line 74 | High (for those specs; none for this packet) | The reading must not mention STP or 22.4 L. Report the two specs as stale per CLAUDE.md §2 precedence. Matt decides whether to remove the STP items or move them to U11. If they stay, the reading and the worksheet will disagree about U7 scope. |
| F3 | NaCl called "molecules" | Unit test Day 2 B4 asks "How many **molecules** are in 15.0 g of NaCl?" NaCl is ionic, so the particle is a **formula unit**. The reading (7.3) will teach exactly this difference. The arithmetic is right: 15.0 ÷ 58.44 = 0.2567 mol, × 6.022 × 10²³ = 1.55 × 10²³. | unit_test.json lines 472–483 | Medium | Change "molecules" to "formula units" in B4 and its answer, or switch B4 to a molecular compound. |
| F4 | Hydrogen = 1.008 in the test spec | NH₃ work step uses 3(1.008), giving 17.03 g/mol. The student table gives H = 1.01, so students get 17.04 g/mol. The final answer is the same either way (1.75 × 17.04 = 29.82, which rounds to 29.8 g). Distractor d1-2 "1.008 is the atomic mass of hydrogen" will not match what students see on their table (1.01). | unit_test.json lines 43, 465–466; chem_data.py line 7 | Low | Use 1.01 so the key matches the student periodic table. In this packet, hydrogen is always **1.01**. |
| F5 | Worksheet self-check rounding | 7.4 challenge: 18.0 g ÷ 18.02 g/mol = 0.99889, which rounds to **0.999 mol** at 3 sig figs. The spec's self-check prints "1.00 mol". The molecule count of 6.02 × 10²³ is correct. | worksheet spec line 124 | Low | Change the self-check to "0.999 mol · 6.02 × 10²³ molecules", or change the given to 18.02 g. |
| F6 | Particle notation | Matt's instruction for this packet is N = n × 6.022 × 10²³. That matches the worksheet and test equation boxes. The reference sheet and DECISIONS line 184 write "particles = n × N_A", so students will see both forms. | worksheet line 19; unit_test line 328; build_reference.py line 90; DECISIONS line 184 | Low | Add one bridging sentence in 7.4: "Your reference sheet writes this as particles = n × N_A. N_A is just a symbol for 6.022 × 10²³." Do not change DECISIONS. This is a per-packet instruction (precedence 1). |
| F7 | Molar mass symbol | The reference sheet uses n = m/M. Capital M is also molarity in 12.5. The worksheet and test use words: "mass (g) ÷ molar mass (g/mol)". | build_reference.py line 89; worksheet lines 12–15 | Low | Use words in the reading, matching the worksheet. Do not introduce "M" here. |
| F8 | Glucose molar mass | With the student table, C₆H₁₂O₆ = **180.18 g/mol**. Published sources using IUPAC values (C 12.011, H 1.008, O 15.999) give **180.16**. A student who looks it up will see a 0.02 difference. | Re-solved below | Low | Print 180.18 to match the student table. Add a teacher note explaining the difference. |
| F9 | Unit-test coverage | The unit-test spec lists sections 7.1–7.4 only. This packet covers 7.1–7.7. | unit_test.json lines 4–9 | Low (observation) | No change to the reading. Raising it so Matt knows 7.5–7.7 have no test items yet. |
| F10 | Standard codes | The unit test marks Ohio codes PROVISIONAL. | unit_test.json line 10 | Low | Print **no** standard code on the reading. |
| F11 | Gas-pump example | $3.299/gal shows a price set to a tenth of a cent, with the bill rounded to the cent. That is a decimal-place and money rule, not a sig-fig counting rule. Using it carelessly invites the misconception "sig figs = decimal places". | Reference sheet separates ×/÷ (sig figs) from +/− (decimal places) | Low | Frame it as "the number of digits tells you how finely something was measured or set". Keep the ruler as the example that carries the actual rule. |
| F12 | Avogadro history | It is safe to say the number is *named in honor of* Amedeo Avogadro (Italian, early 1800s) and that he never knew its value. Who coined the name, and when, is UNVERIFIED here. Avogadro's gas-volume hypothesis is 11.5 content. | — | Low | Use only the "named in honor of" sentence. Leave out the volume hypothesis and who named the number. |
| F13 | "Molar mass equals atomic mass" | Since the 2019 SI change, "molar mass in g/mol equals the atomic mass in amu" is true to about 1 part in 10⁹ instead of exactly. | BIPM SI Brochure 9th ed. | Info | "Same number" is fine for students. Teacher notes should not say "exactly by definition". |

---

## 1. Verified numbers used in the packet (one table, so each value appears once)

| Quantity | Value to print | Re-solved working |
|---|---|---|
| Avogadro's number | 6.022 × 10²³ | Exact SI value 6.02214076 × 10²³ (BIPM 2019), rounded to 4 sig figs |
| Written out | 602,200,000,000,000,000,000,000 | "6022" followed by 20 zeros = 24 digits, which matches 10²³ |
| Molar mass C | 12.01 g/mol | Student table |
| Molar mass H₂O | 18.02 g/mol | 2(1.01) + 16.00 = 2.02 + 16.00 |
| Molar mass NaCl | 58.44 g/mol | 22.99 + 35.45 |
| Molar mass O₂ (misconception example) | 32.00 g/mol | 2(16.00) |
| Mass of one water molecule | 2.99 × 10⁻²³ g | 18.02 ÷ 6.022 × 10²³ = 2.992 × 10⁻²³ |
| Volume of 1 mol of water | about 18 mL (a little over 1 tablespoon) | 18.02 g ÷ 0.997 g/mL (25 °C) = 18.07 mL. US tablespoon = 14.8 mL, so about 1.2 tbsp |
| Water: % H | **11.2 %** | 2.02 ÷ 18.02 = 0.1121. With IUPAC values, 2.016 ÷ 18.015 = 0.1119. Both give 11.2 % ✓ |
| Water: % O | **88.8 %** | 16.00 ÷ 18.02 = 0.8879. Check: 11.2 + 88.8 = 100.0 |
| Glucose C₆H₁₂O₆ | 180.18 g/mol | 6(12.01) + 12(1.01) + 6(16.00) = 72.06 + 12.12 + 96.00 |
| CH₂O (empirical) | 30.03 g/mol | 12.01 + 2.02 + 16.00. 180.18 ÷ 30.03 = 6.000 |
| Glucose % C / H / O | 40.0 / 6.73 / 53.3 % | 72.06/180.18 = 0.3999; 12.12/180.18 = 0.0673; 96.00/180.18 = 0.5328 |
| Acetylene C₂H₂ | 26.04 g/mol | 2(12.01) + 2(1.01) = 24.02 + 2.02 |
| Benzene C₆H₆ | 78.12 g/mol | 6(12.01) + 6(1.01) = 72.06 + 6.06 (IUPAC value is 78.11, see F8 logic) |
| CH (empirical) | 13.02 g/mol | 12.01 + 1.01. 26.04 ÷ 13.02 = 2; 78.12 ÷ 13.02 = 6 |
| Acetylene and benzene % C | 92.2 % (both) | 24.02/26.04 = 72.06/78.12 = 0.9224. Identical because the ratio is the same |
| H₂O₂ → HO (optional 7.6 example) | 34.02 → 17.01 g/mol | 2(1.01) + 2(16.00); 34.02 ÷ 17.01 = 2 |
| 7.4 worked example | 36.0 g H₂O = **2.00 mol** | 36.0 ÷ 18.02 = 1.9978, which rounds to 2.00 at 3 sig figs |

**Avogadro scale comparisons (arithmetic shown; print only these):**

| Comparison | Statement | Working | Assumptions and sources |
|---|---|---|---|
| A. Counting alone | Counting one particle per second, nonstop, a mole would take about **19 quadrillion years**, roughly **1.4 million times** the age of the universe. | 6.022 × 10²³ s ÷ 3.156 × 10⁷ s/yr = 1.91 × 10¹⁶ yr; ÷ 1.38 × 10¹⁰ yr = 1.38 × 10⁶ | 1 yr = 365.25 d = 3.156 × 10⁷ s. Age of the universe is 13.8 billion years (Planck 2018) |
| B. Everyone counting | If all ~8.2 billion people on Earth each counted one per second, it would still take **more than 2 million years** (about 2.3 million). | 6.022 × 10²³ ÷ 8.2 × 10⁹ = 7.34 × 10¹³ s; ÷ 3.156 × 10⁷ = 2.33 × 10⁶ yr | UN World Population Prospects 2024: "nearly 8.2 billion in mid-2024". Using 8.0 billion gives 2.4 million yr, so "more than 2 million" holds either way |
| C. Money | A mole of dollars shared equally among everyone on Earth is about **$73 trillion per person**. | 6.022 × 10²³ ÷ 8.2 × 10⁹ = 7.34 × 10¹³ | Same population figure |
| D. The twist (pair with A–C) | Yet a mole of water molecules is only about **18 mL**, a little more than a tablespoon. | See table above | Shows that molecules are extremely small |

Do **not** use the "a mole of marbles/sand would cover the Earth to X km" type of claim. These comparisons depend on marble or grain size, and I could not verify any version of them.

---

## 2. Per-section brief

### 7.1 Mathematical Tools (~1 full page, ~450–550 words)

**Open with:** "How many digits do I write down?"

**Facts to use (all verified):**
- **Every measurement has a last, estimated digit.** Record all the digits you are sure of, plus one estimated digit.
  - Ruler with **cm marks only**: an object ending between 4 and 5 is recorded as **4.3 cm**. The 4 is certain and the 3 is estimated.
  - Writing 4.32 cm claims hundredths the ruler cannot show.
  - Writing "4 cm" throws away information you actually have.
- **Kitchen vs bathroom scale (illustrative readings).** The same bag of sugar might read "5 lb" on a bathroom scale and "2271 g" on a kitchen scale. More digits means the tool measures more finely. Present both as possible readings, not real data. Check: 5 lb × 453.6 g/lb (reference-sheet factor) = 2268 g, so 2271 g is a believable reading.
- **Gas pump $3.299.** The price is set to a tenth of a cent, but you can only pay to the cent: 12.5 gal × $3.299 = $41.2375, so you pay $41.24. Fractional-cent pricing is a long-standing US practice (NACS: https://www.convenience.org/topics/fuels-and-energy/why-gas-is-priced-using-fractions-of-a-penny). See F11 for framing.
- **Splitting a bill on a calculator.** $47.00 ÷ 3 shows 15.666666…, but nobody pays $15.666666. You pay $15.67, and 3 × 15.67 = $47.01, a penny over. The calculator does not know which digits mean anything. **You decide.** That is the "why" of significant figures. The number of digits displayed varies by device, so say "a long string of 6s".
- **Exact numbers** (counted items, defined conversions such as 12 eggs = 1 dozen, 1 in = 2.54 cm) are not limited by sig figs. This matches the reference sheet.
- **Rules:** point students to **Reference Sheet 2, Significant Figure Rules**. Do not reprint the rule table, so the fact lives in one place. At most, preview "nonzero digits always count; zeros depend on where they are".
- **Do not** say sig figs are graded (Matt). Do not mention when enforcement begins.
- **Scientific notation:** a number from 1 to less than 10, times a power of ten. Big example: 6.022 × 10²³ instead of the 24-digit number. Small example: one water molecule has a mass of 2.99 × 10⁻²³ g. Every digit in the number before the "× 10" counts as significant (reference sheet).
- **Conversion factors and dimensional analysis:** use only exact numbers, which keeps sig figs out of it and previews the mole.
  - 3 dozen × (12 eggs / 1 dozen) = 36 eggs.
  - Write the factor so the unit you have is on the bottom and cancels. This mirrors the reference-sheet steps.
  - Teacher choice whether to show this as a worked example (Matt approved worked examples for 7.3 and 7.4 only). It is a one-line illustration with no numeric difficulty.

**Key terms:**
- **significant figures**: the digits in a measurement that are known for certain, plus one estimated digit.
- **measured number**: a number obtained with a tool, which always has some uncertainty.
- **exact number**: a number known with no uncertainty because it was counted or defined (12 eggs in a dozen).
- **scientific notation**: a way to write a number as a value from 1 to less than 10 times a power of ten.
- **conversion factor**: a fraction whose top and bottom are equal amounts in different units, so multiplying by it changes the unit but not the amount.
- **dimensional analysis**: solving a problem by multiplying by conversion factors so that units cancel, leaving the unit you want.

Avoid the accuracy/precision vocabulary pair. It is not in DECISIONS and is easy to define loosely. If "precision" appears, use it informally ("how finely a tool measures"), not in bold.

**Figure:**
- Two stacked ruler close-ups measuring the same pencil tip.
  - Top: cm marks only, tip about one-third past 4. Label "4.3 cm: 4 is certain, 3 is estimated".
  - Bottom: cm + mm marks, tip just past 4.3. Label "4.32 cm: 4.3 is certain, 2 is estimated".
- Caption: "A better tool earns you one more digit. Every measurement ends with one estimated digit."

**Misconceptions to address:**
- More digits always means a better answer.
- The calculator's display is the answer.
- Sig figs are the same as decimal places.
- Zeros never count, or zeros always count.
- Round at every step. The reference sheet says round once, at the end.
- Exact numbers limit the answer.

**Real-world connection:** the bill split ($15.67, a penny over) or the gas pump. Use one in the opener and the other in passing.

**Reading Check (draft):** "A ruler has only centimeter marks. Why is writing 4.32 cm claiming more than you know?" *Exemplar:* "You can estimate only one digit past the smallest mark, which is tenths. The 2 in the hundredths place is a guess the ruler can't support."

### 7.2 The Mole & Avogadro's Number (~300–400 words)

**Facts:**
- The mole is a counting unit, like a pair (2), a dozen (12) or a ream of paper (500 sheets).
- 1 mole = **6.022 × 10²³** particles of whatever you are counting.
- Since 2019, scientists have defined the mole as exactly 6.02214076 × 10²³ particles (BIPM). The text rounds to 6.022 × 10²³. This sentence is optional, but it heads off "the number might change".
- It is named in honor of Amedeo Avogadro (F12).
- Why such a big number: atoms are tiny. Use comparison A or B, then the twist D.
- The **representative particle** depends on the substance:
  - an **atom** for most elements (C, Fe);
  - a **molecule** for molecular substances (H₂O, O₂);
  - a **formula unit** for ionic compounds (NaCl).
- The same number of particles does **not** mean the same mass (set-up for 7.3). This matches the unit test d1-1, d1-2 and d1-8 learning targets.

**Key terms:**
- **mole (mol)**: the SI counting unit for particles; one mole is 6.022 × 10²³ particles.
- **Avogadro's number**: 6.022 × 10²³, the number of particles in one mole.
- **representative particle**: the smallest unit a substance is counted in: atom, molecule, or formula unit.
- **formula unit**: the lowest whole-number ratio of ions in an ionic compound, such as one Na⁺ and one Cl⁻ in NaCl.

**Figure:**
- A counting-units ladder: "pair = 2" (2 shoes) → "dozen = 12" (eggs) → "ream = 500" (paper) → "mole = 6.022 × 10²³" (an atom/molecule icon with "…").
- Caption: "A mole is a counting word, like 'dozen', just far bigger, because atoms are far smaller."

**Misconceptions to address:**
- A mole is a mass, or "1 mole = 1 gram". This is test d1-1 choice A.
- A mole of anything has the same mass.
- Moles are only for gases. This is test d1-1 choice D and d1-8 choice A.
- A huge number of particles means a huge pile. Twist D answers this.

**Real-world connection:** counting by groups at the store (eggs by the dozen, paper by the ream). Chemists need a "dozen" big enough for atoms.

**Reading Check:** "Give two ways a mole is like a dozen and one way it is different." *Exemplar:* "Both are counting words, and both mean a fixed number no matter what is counted. A mole is 6.022 × 10²³ instead of 12."

### 7.3 Molar Mass (~300–400 words + worked example)

**Facts:**
- **Molar mass** is the mass in grams of one mole of a substance, in g/mol.
- For an element, it is the average atomic mass on the periodic table (the decimal number, not the atomic number), read in g/mol instead of amu. Link back to U1 S1.5, which used "amu".
- For a compound, add the molar mass of **every** atom in the formula. Subscripts multiply, and a subscript outside parentheses multiplies everything inside. Ca(NO₃)₂ has 1 Ca, 2 N and 6 O, but that belongs to the worksheet, so the reading should not repeat it.
- **Counting by weighing:** a US nickel has a mass of 5.00 g (US Mint specifications, https://www.usmint.gov/learn/coin-specifications), so a pile of nickels weighing 200 g holds 40 nickels. Chemists do the same with molar mass.

**Worked example (Matt approved): molar mass of H₂O.**
- H: 2 × 1.01 g/mol = 2.02 g/mol
- O: 1 × 16.00 g/mol = 16.00 g/mol
- Total: 2.02 + 16.00 = **18.02 g/mol**

Present it in the same "show the sum" layout the worksheet asks for. Do not use NaCl, CO₂ or Ca(NO₃)₂ as the worked example, because those are worksheet items.

**Key terms:**
- **molar mass**: the mass of one mole of a substance, in grams per mole (g/mol).
- **average atomic mass** is already a U1 term. Re-gloss it in passing, not in bold.

**Figure: "One mole of each".** Three samples side by side, all values from the student table:

| Sample | Label | Particle line |
|---|---|---|
| Carbon (graphite) | 12.01 g | 6.022 × 10²³ atoms |
| Water | 18.02 g (about 18 mL) | 6.022 × 10²³ molecules |
| Sodium chloride (table salt) | 58.44 g | 6.022 × 10²³ formula units |

Caption: "Same number of particles, different masses, because the particles themselves have different masses."

The label words **atoms / molecules / formula units** must be exactly as given. Do not write "molecules" for NaCl (see F3).

**Misconceptions to address:**
- Adding atomic numbers instead of masses. This is test d1-3 choice A.
- Ignoring subscripts.
- Multiplying the masses together. This is test d1-3 choice B.
- Mixing up the molar mass (g/mol) with the mass of the sample (g).
- Diatomic elements: oxygen gas is O₂, 32.00 g/mol, not 16.00.
- Thinking a mole of salt and a mole of water weigh the same.

**Real-world connection:** counting nickels by weighing (above).

**Reading Check:** "A mole of water and a mole of carbon have the same number of particles. Why does the water have more mass?" *Exemplar:* "Each water molecule has more mass than a carbon atom (18.02 vs 12.01), and there are the same number of them."

### 7.4 Mole Conversions (~300–400 words + worked example)

**Facts (matching the worksheet's key ideas):**
- Grams and particles never convert directly. Every path goes through **moles**.
- Grams → moles: divide by molar mass.
- Moles → grams: multiply by molar mass.
- Moles → particles: **N = n × 6.022 × 10²³** (Matt's notation).
- Particles → moles: divide by 6.022 × 10²³.
- Carry units through every step. If they don't cancel to the unit you want, the setup is wrong. This is test d1-7.
- Add the bridge sentence from F6.
- **No STP or liters** (F2).

**Worked example (Matt approved): grams → moles.**
- Problem: "How many moles are in 36.0 g of water?"
- Setup: 36.0 g H₂O × (1 mol H₂O / 18.02 g H₂O) = **2.00 mol H₂O**
- Arithmetic: 1.9978 rounds to 2.00, because 36.0 has 3 sig figs (link back to 7.1).
- Not used in the worksheet or test, so there is no duplication. Fallback if Matt wants a less tidy result: 10.0 g H₂O = 0.555 mol (10.0 ÷ 18.02 = 0.55494).

**Key terms:** reuse **conversion factor** from 7.1 with no new bold. **Mole conversion** is not a separate bold term.

**Figure: conversion map.**
- Three boxes: GRAMS ⇄ MOLES ⇄ PARTICLES.
- Arrows between GRAMS and MOLES: "÷ molar mass (g/mol)" pointing toward moles, "× molar mass (g/mol)" pointing toward grams.
- Arrows between MOLES and PARTICLES: "× 6.022 × 10²³" pointing toward particles, "÷ 6.022 × 10²³" pointing toward moles.
- Caption: "Grams and particles never touch. Every path runs through moles."
- Caveat: the worksheet has a blank version of this map for students to complete. Matt should decide whether showing the filled map on day one spoils the worksheet item. Option: show the map with only the box labels and arrows, no factors, and let the text supply the factors. **Teacher decision.**

**Misconceptions to address:**
- Going grams → particles in one step. This is test d1-5.
- Multiplying by molar mass when going from grams to moles. Units give g²/mol, which is test d1-6 choice A.
- Using 6.022 × 10²³ to convert grams. This is test d1-6 choice B.
- Rounding in the middle of a problem.

**Real-world connection:** a pharmacist or lab tech measures medicine by mass, but the chemistry (how many molecules reach the body) depends on count. A scale cannot count molecules, but molar mass turns a mass into a count. Keep this general; no dosage figures are needed or verified.

**Reading Check:** "What quantity is always in the middle of a mole conversion, and why?" *Exemplar:* "Moles. Molar mass connects grams to moles, and Avogadro's number connects moles to particles. Nothing connects grams to particles directly."

### 7.5 Percent Composition (~300–400 words, method in words only)

**Facts:**
- **Percent composition** is the percent by **mass** of each element in a compound.
- Method in words: find the mass of each element in one mole (atomic mass × subscript), divide by the molar mass of the compound, multiply by 100. This matches reference-sheet "% element = mass of element ÷ mass of compound × 100".
- The percentages add up to 100 %.
- A pure compound always has the same percent composition, whether the sample is a drop or a lake. This is the idea behind the law of definite proportions; naming the law is optional and not required by DECISIONS.
- Water is **11.2 % H and 88.8 % O** by mass. These results may be **stated** as facts. Do not show the arithmetic, since 7.5 has no numeric worked problems.
- The twist: two-thirds of the atoms in water are hydrogen (2 of 3), but hydrogen is only 11.2 % of the mass, because each H atom (1.01) is far lighter than an O atom (16.00).

**Key terms:** **percent composition**: the percent by mass of each element in a compound.

**Figure:**
- A side-by-side comparison for water.
  - Left: three-atom molecule, labelled "by number of atoms: 2 of 3 are H (67 %)".
  - Right: a 100-unit mass bar split 11.2 (H) | 88.8 (O), labelled "by mass".
- Caption: "Water is mostly hydrogen by atom count, but mostly oxygen by mass."
- Arithmetic: 2/3 = 66.7 %, shown as "67 %".

**Misconceptions to address:**
- Percent by atom count is the same as percent by mass.
- Percent composition changes with sample size.
- Using the atomic number instead of mass.
- Forgetting the subscript, which would give 1.01/18.02 for H.

**Real-world connection:**
- Primary: if you split water to make hydrogen fuel, only about 112 g of every 1 kg of water is hydrogen (11.2 % of 1000 g = 112 g).
- Optional (rural Ohio fit): fertilizer bag numbers like 10-10-10 are percents by mass. Caveat: by US labeling convention the second and third numbers are reported as P₂O₅ and K₂O, not as elemental P and K. If used, say "percent by mass of nutrients" and do not claim "10 % phosphorus". Teacher should confirm the wording before printing.

**Reading Check:** "Two-thirds of the atoms in water are hydrogen. Why is water only 11.2 % hydrogen by mass?" *Exemplar:* "Hydrogen atoms are much lighter than oxygen atoms, so the one oxygen atom holds most of the mass."

### 7.6 Empirical Formulas (~300–400 words, method in words only)

**Facts:**
- An **empirical formula** is the simplest whole-number ratio of atoms in a compound.
- Glucose C₆H₁₂O₆ → **CH₂O**: divide every subscript by 6.
- Hydrogen peroxide H₂O₂ → HO (optional).
- Ionic formulas like NaCl are already in lowest ratio.
- Method in words, from percent data:
  1. Assume a 100 g sample, so each percent becomes grams.
  2. Change each mass to moles by dividing by atomic mass.
  3. Divide every mole value by the smallest one.
  4. Round to whole numbers. If a value lands near x.5 or x.33, multiply all values by 2 or 3 instead of rounding.
  5. Those whole numbers are the subscripts.
- The key point: subscripts are a **mole** ratio, never a mass ratio.
- One empirical formula can belong to several different compounds. CH₂O is the empirical formula of glucose (blood sugar) and of acetic acid C₂H₄O₂ (in vinegar). It is also the actual molecular formula of formaldehyde (a preservative). All three have the same percent composition (40.0 % C), which is why percent data alone cannot identify a compound. That sets up 7.7.

**Key terms:** **empirical formula**: the simplest whole-number ratio of the atoms in a compound.

**Figure:**
- A "reduce the ratio" visual: C₆H₁₂O₆ with each subscript divided by 6, giving CH₂O.
- Underneath, three small boxes (glucose C₆H₁₂O₆, acetic acid C₂H₄O₂, formaldehyde CH₂O), each with an arrow to "CH₂O".
- Caption: "Three different substances, one simplest ratio."

**Misconceptions to address:**
- Using mass ratios or percents directly as subscripts.
- Rounding 1.5 up to 2 instead of multiplying through.
- Thinking an empirical formula identifies one compound.
- Thinking the empirical formula is always different from the real formula (H₂O, CO₂).

**Real-world connection:** when chemists make or discover a new compound, a lab instrument reports the percent of each element. The empirical formula is the first thing they can work out from that data. Keep it general: combustion analysis exists, but do not name instruments or procedures.

**Reading Check:** "What does an empirical formula tell you, and what does it not tell you?" *Exemplar:* "It tells the simplest ratio of atoms. It does not tell how many atoms are actually in one molecule, so it can't identify the compound by itself."

### 7.7 Molecular Formulas (~300–400 words, method in words only)

**Facts:**
- The **molecular formula** gives the actual number of each atom in one molecule. It is always a whole-number multiple of the empirical formula.
- Method in words:
  1. Find the empirical formula mass.
  2. Divide the compound's molar mass (measured separately) by it. The result is a whole number.
  3. Multiply every subscript in the empirical formula by that number.
- **Acetylene C₂H₂ (26.04 g/mol) and benzene C₆H₆ (78.12 g/mol) both have empirical formula CH (13.02 g/mol).** 26.04 is 2 × 13.02 and 78.12 is 6 × 13.02. Both are 92.2 % carbon by mass.
  - Acetylene is the gas burned in oxy-acetylene welding torches.
  - Benzene is a flammable liquid at room temperature.
  - Do not add health claims; they are not needed.
- Glucose: 180.18 ÷ 30.03 = 6, so C₆H₁₂O₆. This may be **stated**, not worked.
- Water: the multiplier is 1, so the molecular formula is the same as the empirical formula.
- Ionic compounds have formula units, not molecules, so they have no molecular formula.

**Key terms:**
- **molecular formula**: the actual number of each kind of atom in one molecule of a compound.
- **empirical formula mass**: the sum of the atomic masses in the empirical formula.

**Figure:**
- Two molecules side by side with labels:
  - "Acetylene, C₂H₂: 26.04 g/mol = 2 × CH"
  - "Benzene, C₆H₆: 78.12 g/mol = 6 × CH"
- A shared "Empirical formula: CH, 13.02 g/mol" banner.
- Caption: "Same ratio, same percent carbon, different molecules. Molar mass tells them apart."
- Drawing note: benzene is a 6-carbon ring and acetylene is linear H–C≡C–H. Structure is U5 content; a simple ball-and-stick is fine but must not label bond types or geometry.

**Misconceptions to address:**
- The molecular formula is always different from the empirical formula.
- The multiplier can be a fraction. If it isn't a whole number, check the work.
- Percent composition can tell acetylene from benzene. It can't.

**Real-world connection:** a welding-shop gas and a liquid solvent share one simplest formula. Only molar mass separates them.

**Reading Check:** "Water's empirical and molecular formulas are both H₂O. How can that be?" *Exemplar:* "The ratio 2 H : 1 O can't be reduced any further, so the multiplier is 1."

---

## 3. Back page: 3 tiered questions (no calculations beyond what the text states)

| Tier | Question | Exemplar answer |
|---|---|---|
| 1 Literal | What is a mole, and how many particles are in one mole? | A mole is a counting unit, like a dozen. One mole is 6.022 × 10²³ particles (atoms, molecules, or formula units). |
| 2 Inferential | You have one mole of water and one mole of sodium chloride. Do the samples have the same number of particles? The same mass? Explain using the reading. | Same number: each has 6.022 × 10²³ particles (molecules of water, formula units of NaCl). Different mass: 18.02 g vs 58.44 g, because each NaCl formula unit has more mass than a water molecule. |
| 3 Application | A lab report says an unknown compound has the empirical formula CH. Your lab has acetylene (C₂H₂) and benzene (C₆H₆). Can you tell which one it is from the empirical formula alone? What one measurement would settle it, and how? | No. Both reduce to CH and both are 92.2 % carbon. Measure the molar mass: about 26 g/mol is 2 × CH (acetylene) and about 78 g/mol is 6 × CH (benzene). |

All three answers come straight from facts stated in 7.2, 7.3 and 7.7. Nothing needs an untaught calculation.

## 4. Vocabulary list (back page)

The definitions are the ones given in §2, so they are not repeated here.

| Term | First section | Reconciled with |
|---|---|---|
| significant figures | 7.1 | Reference Sheet 2 title; worksheet "significant figures" |
| measured number / exact number | 7.1 | Reference sheet "Exact numbers" rule |
| scientific notation | 7.1 | Worksheet priorKnowledge |
| conversion factor | 7.1 | Unit test d1-6 "conversion factor" |
| dimensional analysis | 7.1 | Reference sheet "Dimensional Analysis" |
| mole (mol) | 7.2 | Worksheet and test: "a counting number, the way a dozen is" |
| Avogadro's number | 7.2 | Test and reference sheet use "Avogadro's number" (not "Avogadro constant") |
| representative particle | 7.2 | New. Worksheet and test use "particles" |
| formula unit | 7.2 | Worksheet (Ca(NO₃)₂ "formula unit"). See F3 |
| molar mass | 7.3 | Worksheet "molar mass (g/mol)" |
| percent composition | 7.5 | Reference sheet "Percent composition" |
| empirical formula | 7.6 | — (not in sibling specs) |
| molecular formula | 7.7 | — |
| empirical formula mass | 7.7 | — |

Terms deliberately **excluded**: molar volume and STP (11.5), N_A as a bold term (explained once in passing, see F6), molarity and "M" (12.5), accuracy/precision (not in DECISIONS).

---

## 5. UNVERIFIED (do not print as fact)

- Who coined the name "Avogadro's number", and when (F12).
- Any "a mole of marbles/sand/…" coverage or volume comparison.
- Typical display resolution of specific bathroom and kitchen scale models. Readings in 7.1 are illustrative only.
- Fertilizer-label wording beyond "percent by mass, P₂O₅/K₂O convention". Teacher to confirm against an actual bag if used.
- Ohio standard codes for U7 (F10).
