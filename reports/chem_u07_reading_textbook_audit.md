# Chemistry U7 Unit Reading: Independent Accuracy and Print Review

**Workflow:** `workflows/unit-textbook.md`, "Independent accuracy and print review" · `.claude/skills/verify-content/SKILL.md` · `standards/QA_GATE.md`
**Auditor:** independent, report-only. Nothing was modified except this file.
**Date:** 2026-11-24

## Verdict: **FAIL (INCOMPLETE)**

There is one **blocking** finding. Figure 7.1 draws the pencil starting at 0.4 cm, not at the 0 mark, but the prose says you "measure a pencil" and "record 4.6 cm" (A-1). Every printed calculation, Example, On Your Own and key answer re-solves correctly. The tear-off leaf passes every parity and format check. Seven primary-source locators remain **open** because every external host was refused by the session proxy (§4).

## 1. Artifact version and coverage

| Item | Value |
|---|---|
| Branch / commit | `claude/ecstatic-pascal-9cro1w` @ `adca763` "U7 reading: rebuild to five sections and unit-textbook tear-off (pre-audit)". Builder, spec and figure script are committed there. `build/` is untracked; the outputs are timestamped 21:25, one minute before the commit |
| Student PDF | `build/chem_u07_reading/Unit 7 Reading - The Mole.pdf`. 8 pages, Letter, LibreOffice 24.2. sha256 `7c481e32…5e20e65` |
| Student DOCX | sha256 `5f56d8aa…a3835`. Re-exported here with soffice: 8 pages, text identical to the shipped PDF |
| Key PDF | `build/chem_u07_reading/Unit 7 Reading Key - The Mole.pdf`. 2 pages. sha256 `1ee63b05…6b138` |
| Key DOCX | sha256 `71959655…7fcd`. Re-exported here: 2 pages, text identical to the shipped PDF |
| Sources read | `templates/reading/specs/chem_u07_reading.json`, `templates/reading/build_reading_docx.py`, `templates/reading/specs/make_chem_u07_figures.py`, `reports/chem_u07_reading_dossier.md`, `courses/chemistry/DECISIONS.md` (U7 l.54–57, SHULL-CHG-0110, SHULL-CHG-0114), `templates/reference/chem_data.py`, `templates/reference/build_reference.py` |
| Pages inspected | Student pp 1–8 and key pp 1–2, all rendered and viewed. Zooms: Fig 7.1 (400 dpi), Figs 7.5 and 7.7 (300 dpi), and the Example 7.1 box (200 dpi) |
| Proof method | **Screen proof only.** PyMuPDF raster in DeviceGray at 110 dpi at print size (Letter, 100%), plus zooms. **No physical photocopy or test print was made.** Toner, edge loss and hairline survival on Matt's copier are unverified |

## 2. Checklist

| Check | Result |
|---|---|
| Deliverable exists, opened | PASS. Both PDFs and both DOCX files were opened and hashed |
| Codes / scope | PASS. Chip `U07 / S7.1–S7.5`. Cover list, headings, question labels and key all read 7.1 Mathematical Tools · 7.2 The Mole & Molar Mass · 7.3 Mole Conversions · 7.4 Percent Composition & Empirical Formulas · 7.5 Molecular Formulas, matching DECISIONS l.54–57. No 7.6 or 7.7 anywhere. `validate_codes.py` OK |
| Naming | PASS. `Unit 7 Reading - The Mole` and `Unit 7 Reading Key - The Mole` (NAMING.md l.54–63, SHULL-CHG-0114). The key is a separate file |
| Fonts (`pdffonts`, `audit_fonts.py`, `--key`) | PASS. Student: ArchivoRoman Regular and Bold, ArchivoNarrow (Type 3 from the variable font; the same as in earlier rounds). Key adds ShullHand, Patrick Hand and Archivo SemiBold Italic. No DejaVu or Liberation |
| Ink (`audit_print_ink.py`) | PASS. Student: worst page 8.35% (p1), average 5.74%. Key: worst 5.52%. Widest solid band 0.00 in, and "no fill" on every page |
| Fills | PASS. Example, On Your Own, Connection and Figure 7.7 boxes are outlines and rules only. Charts use hatching |
| Coloured type | PASS. Coloured text is only `primaryDeep` #B84100. Display orange #FF6B1A appears only as rules. The key uses keyInk pen #4A2466 and pencil #5A6068 |
| Grayscale | PASS on screen. Each box type differs by shape. In Fig 7.5 and Fig 7.3, oxygen, water and graphite are hatched rather than tinted. See A-7 for the light molecule bond lines |
| Clipped text | PASS. No clip at any box, column or page edge. The only spans over a margin are trailing-space glyph boxes, all under 2 pt |
| Binding margin / hole guides | PASS. Text starts at 43.3 pt (0.60 in) on odd pages. On even pages it ends at ≤ 570.2 pt; the 1.4 pt overrun is a trailing space. Hole guides are outline only and mirrored |
| Thumb tab | PASS. Outline only. The outer stroke is **0.22 in** from the paper edge on all 8 pages. The inner edge is at 0.42 in, inside the 0.50 in outside margin. It sits on the right of odd pages and the left of even pages, never on the binding side |
| Standing decisions | PASS: textbook voice · Option B two-column layout with display-title opener · Archivo only · no fills · Why It Matters (p1) · exactly one Connection per section (7.1 Honest digits, 7.2 Counting coins by weighing, 7.3 Medicine by mass, 7.4 A new compound's first formula, 7.5 Same ratio, different jobs) · `N = n × 6.022 × 10²³` printed (p4) · no molar volume (grep finds no 22.4, STP, liter, litre or "molar volume") · thumb tab at 0.22 in. See A-12 on the Example treatment |
| Every number re-solved | PASS (§3) |
| Figures as evidence | **FAIL** (A-1). Minor notes in A-6, A-7 and A-8 |
| Tear-off leaf | PASS (§5) |
| Sources opened | **OPEN** (§4). Every external host was refused (proxy 403) |
| Drive | NOT FILED. This is a pre-release audit; the filing gate follows QA |

## 3. Independent solutions (solved from the printed givens and `chem_data.py` H 1.01, C 12.01, O 16.00, Fe 55.85, Na 22.99, Cl 35.45 before reading the key)

| Item | My working | My answer | Printed / key | Result |
|---|---|---|---|---|
| Ex 7.1: 27.9 cm → in | 27.9 ÷ 2.54 = 10.984…; 3 s.f., 2.54 exact | 11.0 in | 11.0 in, with "keep the zero" | ✓ |
| OYO 7.1: 0.75 in → cm | 0.75 × 2.54 = 1.905; 2 s.f. | 1.9 cm | Key 1.9 cm | ✓ |
| Ex 7.2: H₂O | 2(1.01) + 16.00 | 18.02 g/mol | 18.02 | ✓ |
| OYO 7.2: CH₄ | 12.01 + 4(1.01) | 16.05 g/mol | Key 16.05; teacher note gives published 16.04 | ✓ |
| Ex 7.3: 36.0 g H₂O | 36.0 ÷ 18.02 = 1.99778; 3 s.f. | 2.00 mol | 2.00 mol; magnitude check printed | ✓ |
| OYO 7.3: 64.0 g O₂ | 64.0 ÷ 32.00 = 2.000; 3 s.f. | 2.00 mol | Key 2.00 mol O₂ | ✓ |
| Ex 7.4: 40.0 / 6.7 / 53.3 % | 3.3306, 6.6337, 3.3313 mol; ÷ 3.3306 gives 1.000, 1.9918, 1.0002 | CH₂O | Table 3.331 / 6.634 / 3.331, then 1.000 / 1.992 / 1.000, giving CH₂O | ✓. The percentages sum to 100.0 |
| OYO 7.4: 69.9 % Fe / 30.1 % O | 1.25157 and 1.88125 mol; ratio 1.5031; × 2 gives 2 : 3.006 | Fe₂O₃ | Key Fe₂O₃. Check: Fe₂O₃ gives 69.94 / 30.06 % | ✓. See A-10 (1.503 vs 1.502) |
| Ex 7.5: glucose | CH₂O = 30.03; 180.18 ÷ 30.03 = 6.000 | C₆H₁₂O₆ | C₆H₁₂O₆ | ✓ |
| OYO 7.5: CH₂, 28.06 | CH₂ = 14.03; 28.06 ÷ 14.03 = 2.000 | C₂H₄ | Key C₂H₄; published 28.05 in the teacher note | ✓ |
| CH / C₂H₂ / C₆H₆ / % C | 13.02; 26.04 = 2 × 13.02; 78.12 = 6 × 13.02; 12.01 ÷ 13.02 = 92.24 % | — | 13.02, 26.04, 78.12, 92.2 % | ✓ |
| Water % H / % O | 2.02 ÷ 18.02 = 11.21 %; 88.79 % | 11.2 / 88.8 | 11.2 / 88.8; 112 g and 888 g per kg | ✓. Fig 7.5 bar is to scale (95 / 849 px = 11.2 %) |
| CH₂O family | 12.01 ÷ 30.03 = 39.99 % | 40.0 % C | 40.0 % | ✓ |
| NaCl (Fig 7.3) | 22.99 + 35.45 | 58.44 g | 58.44 g | ✓ |
| 6.022 × 10²³ written out | "602,200,000,000,000,000,000,000" has 24 digits, so the exponent is 23 | ✓ | ✓ | ✓ |
| Mass of one H₂O | 18.02 ÷ 6.02214076 × 10²³ = 2.9923 × 10⁻²³ | 2.99 × 10⁻²³ g | ✓ | ✓ |
| Counting time | 6.02214076 × 10²³ ÷ 3.15576 × 10⁷ s/yr = 1.908 × 10¹⁶ yr | about 19 quadrillion | ✓ | ✓ |
| × age of universe | 1.908 × 10¹⁶ ÷ 1.3787 × 10¹⁰ = 1.384 × 10⁶ (1.383 × 10⁶ at 13.8 Gyr) | about 1.4 million | ✓ | ✓ arithmetic. Source open (§4) |
| 8 billion counters | ÷ 8.2 × 10⁹ = 2.33 × 10⁶ yr (2.39 × 10⁶ at 8.0 × 10⁹) | > 2 million yr | ✓ | ✓ |
| 1 mol water volume | 18.02 ÷ 0.99705 = 18.07 mL; ÷ 14.7868 mL = 1.22 tbsp | about 18 mL, a little more than 1 tbsp | ✓ | ✓ arithmetic. Sources open (§4) |
| Gas pump | 3.299 × 12.5 = 41.2375, then $41.24 | ✓ | ✓ | ✓. See A-4 |
| Honest digits | 0.1 ÷ 0.0001 | 1,000× | ✓ | ✓ |
| 3 dozen | 3 × 12 = 36; the flipped factor gives dozen²/egg | ✓ | ✓ | ✓ |
| 200 g of nickels | 200 ÷ 5.00 | 40 | ✓ | ✓ |
| Fig 7.1 tip | Tip at 4 cm + 112/177 cm = 4.63 cm | 4.6 / 4.63 | Labels 4.6 cm / 4.63 cm | ✓ tip position. **But the pencil body starts at 0.40 cm (A-1)** |
| Key teacher-note published values | glucose 180.16 · benzene 78.11 · CH₄ 16.04 · C₂H₄ 28.05 · Fe₂O₃ 159.69 (from IUPAC conventional H 1.008, C 12.011, O 15.999, Fe 55.845) | ✓ | ✓ | ✓ |

## 4. Source tracing and locator attempts

Every material claim on pp 1–6 was traced to a dossier row. The following remain **open**:

| Claim (page) | Dossier | Locator attempted 2026-11-24 | Result | Independent evidence I could get | Disposition |
|---|---|---|---|---|---|
| "roughly 1.4 million times the age of the universe" (p3) | 7.2-h (K) | arxiv.org/abs/1807.06209 (Planck 2018 VI, Table 2) | **Refused**: `CONNECT tunnel failed, response 403` | None retrievable. The comparison holds for any age from 13.6 to 14.1 Gyr | OPEN. Low risk |
| "about 18 mL" (water density, p3; Fig 7.3 "about 18 mL") | 7.2-j (S, secondary) | webbook.nist.gov/chemistry/fluid/ | Refused (403) | The claim holds for any density from 0.96 to 1.03 g/mL | OPEN. Low risk |
| "a little more than a tablespoon" (p3) | 7.2-j (S, secondary) | nist.gov/document/2026-nist-handbook-44-appendix-c | Refused (403) | Pint 0.24.4 unit definitions (local, secondary): 1 tbsp = ½ US fl oz = 14.7868 mL, so 1.22 tbsp | OPEN for the primary; corroborated secondarily |
| Two meanings of "precision" (p1) | 7.1-e (P/K) | jcgm.bipm.org/vim/en/2.15.html | Refused (403) | My own knowledge of VIM 3: §2.15 *measurement precision* is the agreement of replicate measurements; "how finely a tool reads" is §4.14 *resolution*. See A-3 | OPEN, with a wording note |
| Mole defined as exactly 6.022 140 76 × 10²³ since 2019 (p2) | 7.2-b (S + P) | bipm.org | Refused (403) | Pint `constants_en.txt` (CODATA 2018): `avogadro_number = 6.02214076e23  # since May 2019` | OPEN for the primary; corroborated secondarily |
| N_A exact (implied, p4) | 7.2-c (K) | physics.nist.gov/cgi-bin/cuu/Value?na | Refused (403) | As above | OPEN for the primary; corroborated |
| Student atomic masses vs IUPAC | §B (S/K) | ciaaw.org/atomic-weights.htm | Refused (403) | The printed values come from the classroom table `chem_data.py`, which is the authority students use | OPEN. No printed claim depends on it |
| Also refused (403): energy.gov, pubchem, usmint.gov, wikipedia.org | — | — | The proxy allows no external host this session | — | Recorded. These claims rest on the dossier's (S) excerpts |

Claims the dossier flagged (K) that are **not printed**, so no source is needed: benzene "flammable", DOE electrolysis, ream = 500, "rust" (student copy), Perrin and Loschmidt.

## 5. Tear-off leaf (exported student PDF)

| Check | Result |
|---|---|
| Cover list = headings = question labels = key | PASS, one-to-one: 7.1–7.5, titles verbatim from DECISIONS |
| Name line | PASS. "NAME" with a rule at the top of p7 |
| Due line | PASS, verbatim: "Due ASAP. No late work will be accepted. We will start the unit with this." |
| Questions | PASS. Exactly 5, one per section, each a single direct question answerable from its own section in a sentence or two. Each matches its key stem word for word |
| Vocabulary | PASS. 10 printed term–definition pairs = 10 bold terms in the body (significant figures p1, conversion factor p2, mole p2, Avogadro's number p2, representative particle p3, molar mass p3, percent composition p4, empirical formula p5, molecular formula p6, empirical formula mass p6). Each is defined in its own sentence and in a set-off line whose words match p8 and the key exactly. No other body text is bold except Example titles and step numbers |
| Final reading page | p6 (even). No blank back is needed and none is inserted |
| Last two physical pages | p7 (front: questions), p8 (back: vocabulary). Printed folios 7 and 8 |
| Long-edge orientation | PASS. Both are portrait and upright. Hole guides (p7 left, p8 right) and thumb tab (p7 right, p8 left) sit on the same physical edges back to back |
| Writable space | PASS. Four full-width ruled lines per question, with about 1 in spare at the foot of p7 |
| **Leaf-removal simulation** | PASS. Removing sheet 4 (p7/p8) leaves pp 1–6: the cover, all five sections, all seven figures, every Example and On Your Own, and all ten bold definitions in the prose. Nothing on p7 or p8 is reading content; p8 duplicates the in-text definitions |

## 6. Findings

| # | Page / item | Claim or calculation | Independent evidence or result | Severity | Disposition |
|---|---|---|---|---|---|
| A-1 | p1, Figure 7.1 and the "Estimated digit" paragraph | Prose: "Suppose you measure a pencil with a ruler… you record 4.6 cm", then "the same tip reads 4.63 cm" | In both panels, the pencil's back end is drawn at **0.40 cm, not at the 0 mark** (`make_chem_u07_figures.py` `body_l = x0 + 0.4 * cm`). Measured on the render: 0 tick at x 237, back end at x 308, 177 px/cm. The drawn pencil is 4.23 cm long, so the figure models reading a length without zeroing the ruler. That is the very measurement error 7.1 should prevent. The caption ("the same pencil tip") does not repair it, because the prose calls the result the pencil's measurement | **Blocking** | Return to designer. Start the pencil body at the 0 mark (`body_l = x0`); the tip stays at 4.63 cm. Alternatively, reword the prose and caption to a tip *position*, though zeroing is the better model. Re-render Fig 7.1 and recheck p1 |
| A-2 | §4 locators | Planck age, water density, HB44 tablespoon, VIM 2.15 / 4.14, BIPM SI §2.3.1, CODATA N_A, CIAAW | Every host was refused (proxy 403). The printed claims re-derive correctly and are robust to any plausible source value. N_A and the tablespoon are corroborated by a local secondary source (Pint) | Minor (open) | OPEN. Allow those hosts and recheck, or accept on the record. Not closed by this audit |
| A-3 | p1, "Precision" paragraph | "Precision describes how finely a tool measures… The same word also describes how closely repeated measurements agree." | The metrological definition (VIM 2.15, from my knowledge; locator unreachable) is the second meaning, agreement among repeated measurements. "How finely a tool reads" is VIM 4.14 *resolution*. Both uses occur in school texts, and the paragraph names both. It is not wrong, but it leads with the non-standard sense. *Precision* is not a bold or vocab term | Minor | Designer and Matt to decide. Either lead with the agreement meaning, or keep the order and name the first sense as the everyday one |
| A-4 | p1–2, gas pump | $3.299 × 12.5 gal = $41.2375, "you pay $41.24" | The arithmetic is correct. But it comes right after "an answer calculated from measurements can't be more certain than the measurements", and 12.5 gal has 3 s.f. while $41.24 has 4. "Rounded to the cent by rule" explains it, but a student may read it as a sig-fig counterexample | Minor | Optional. Add a clause such as "a pump measures to the thousandth of a gallon", or keep it as is |
| A-5 | p1, Why It Matters | "use too much and it tastes bitter" | Dossier WIM-a (SEC) excerpt: excess soda leaves "a metallic, soapy aftertaste". "Bitter" is not in the cited excerpt | Minor | Use "soapy" or "metallic", or add a locator for "bitter" |
| A-6 | p5, Figure 7.5 water structure | H–O–H drawn at about 120° (measured: arms at 29.9° above horizontal) | Water is bent at about 104.5°, as U5 VSEPR teaches. No angle is printed. The figure's claim is atom count versus mass, which the to-scale bars carry correctly. The bent shape is qualitatively right, so I judge it **not misleading** for this figure. The key's teacher note discloses it accurately | Minor | Accept with the teacher note. Optional: a builder option for a ~104.5° layout in a later revision |
| A-7 | p5–6, molecule line weight | Fig 7.5 bonds and Fig 7.7 acetylene triple bond | The water bonds are thin mid-gray lines about 1.3 in long. The two outer lines of the acetylene triple bond float about 9.6 pt from the centre line and do not reach the C labels. Both are legible on the screen proof but may thin on a photocopy | Minor | Confirm on a test photocopy. If faint, darken or thicken the bonds in the shared builder output |
| A-8 | p3–6, unitless atomic masses in prose | "each hydrogen atom (1.01) … oxygen atom (16.00)" (p4; also key 7.4) | Numbers carry no unit (amu) | Minor | Add "amu", or rephrase |
| A-9 | p5, "Ionic formulas such as NaCl are already written as the lowest ratio" | General statement | True for NaCl and most binary salts. Formulas such as Na₂O₂ and Hg₂Cl₂ are lowest *ion* ratios but not lowest *atom* ratios, and the empirical formula is an atom ratio | Minor | Optional. "Most ionic formulas, such as NaCl, …" |
| A-10 | Key p2, OYO 7.4 | "÷ 1.252: Fe 1.000, O 1.503" | From the key's own rounded intermediates, 1.881 ÷ 1.252 = 1.502. The value 1.503 comes from unrounded moles (1.88125 ÷ 1.25157 = 1.5031). The answer Fe₂O₃ is unaffected | Minor | Print 1.502, or note "from unrounded values" |
| A-11 | p4, Connection "Medicine by mass" | "the body responds to how many molecules arrive" | The dossier (7.4-f) covers only the logic that, at equal mass, the smaller molar mass gives more molecules. The physiological premise has no locator. It is a standard simplification and is not wrong at this level | Minor | Add a locator, or soften to "what reaches the body is a number of molecules" |
| A-12 | p2–6, Example treatment | Option B: "rule-only Example banners" | Examples render as a 3 pt display-orange top rule **plus** a 0.75 pt hairline box on all sides, so they are boxed like On Your Own. There is no fill, and the two still differ by the top rule | Minor | Designer to confirm this is the approved Option B treatment |
| A-13 | Key p1, teacher note | "rust is hydrated and variable" | The dossier says "rust… not sourced". The note is teacher-facing and correct chemistry (Fe₂O₃·nH₂O) | Minor | Accept, or add a locator |
| A-14 | p4, "N_A is just a symbol for Avogadro's number, 6.022 × 10²³ particles per mole" | The vocab defines Avogadro's number as dimensionless, then gives it units here | This matches the reference sheet label (`build_reference.py` l.119). IUPAC separates the number from the constant | Info | No action; consistent with the classroom sheet |
| A-15 | p6, layout | Final reading page | The right column is about half empty below the 7.5 Connection | Info | No action required |

## 7. What passed without finding

All Example, On Your Own and key arithmetic, sig figs and units (§3). Every section cross-reference (Section 7.2 / 7.3 / 7.5, Example 7.2, Figures 7.1–7.7, each referenced and placed beside or facing its text). The reference-sheet wording ("Significant Figure Rules", "Equations" page, `particles = n × N_A`) matches `build_reference.py` l.90, 158 and 186. "Formula unit" is defined in full at first use. The dossier's D2 is resolved: OYO 7.5 uses CH₂ → C₂H₄, so H₂O₂ in the 7.4 prose gives nothing away. Fe₂O₃ is not called rust on the student copy. There is no teacher, PROVISIONAL or standards-code text on student pages. Voice reads as direct textbook prose with no brochure language.

## 8. Release condition

Fix A-1, then re-run the Auditor on p1 (figure and pagination). A one-figure change that keeps the text unchanged can reuse this content evidence for pp 2–8 after their identity is confirmed by hash or text diff. A-2 stays open until the locators are opened or Matt accepts them on the record. Minor items are the designer's call, routed through the Overseer.
