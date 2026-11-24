# QA Audit: Chemistry U7 Unit Reading pilot ("The Mole") and Key

**Date:** 2026-11-24 · **Auditor:** independent, report-only. Nothing was modified except this report.
**Gate:** `standards/QA_GATE.md` (full), `.claude/skills/audit-deliverable`, `standards/ANSWER_KEYS.md`, `standards/ANTI_AI_SLOP_STANDARD.md` §6–7, `standards/VOICE.md`, `standards/NAMING.md`, `brand/SHULL_DESIGN_SYSTEM.md` §8–11, `brand/tokens.json`, `courses/chemistry/DECISIONS.md`, SHULL-CHG-0042.
**Files audited:** `/home/user/WorkWork/build/chem_u07_reading/`: `Unit 7 Reading - The Mole.pdf` + `.docx` (8 pp), `Unit 7 Reading Key - The Mole.pdf` + `.docx` (2 pp), `fig/` (7 PNGs). Spec: `templates/reading/specs/chem_u07_reading.json`. Builder: `templates/reading/build_reading_docx.py`. Figures: `templates/reading/specs/make_chem_u07_figures.py`.

## Verdict: **INCOMPLETE**

There are no Blocking findings. The science is correct, every number re-solves, and the key matches the student copy word for word. But **four checks fail at Major**:

1. Figure 7.1 is on the back of the page that explains it.
2. The molecule drawings were not made by the molecule script (SHULL-CHG-0042).
3. Figure 7.2 crosses into the binding margin.
4. One bold term, **precision**, is not defined in its own sentence, which breaks the promise printed on page 1.

Under the gate, any failed check makes the deliverable INCOMPLETE.

## Checklist

| Check | Result |
|---|---|
| Deliverables exist, correct types | PASS. All 4 files opened. The PDFs have 8 and 2 pages, US Letter |
| Rendered and viewed, every page | DONE. Student pp 1–8 and key pp 1–2 were rasterised and viewed. Figures 7.5 and 7.7, the header, Example 7.2 and the key handwriting were also viewed at 200–300 dpi |
| Fonts (`pdffonts`, `audit_fonts.py`; `--key` on the key) | PASS. Student copy uses Archivo / Archivo Narrow only. Key uses Archivo, ShullHand and Patrick Hand (the token's named fallback) |
| Ink (`audit_print_ink.py`) | PASS. Student: worst page 7.02% toner, average 5.04%. Key: worst 4.72%. Widest solid band is 0.00 in on both |
| Clipped text | PASS. No clipping at any box, column, figure or page edge on all 10 pages |
| Coloured type on white | PASS. Every coloured glyph is `primaryDeep` #B84100 (title accent, section numbers, labels, figure values, water O). `primary` #FF6B1A is used only for rules and box edges. Key ink is `keyInk.pen` |
| Grayscale | PASS. Figure 7.5 separates H and O by hatch vs. open as well as by label. Figure 7.4 MOLES box is emphasis only and is also labelled. No category relies on hue alone |
| Print discipline (fills, tables) | PASS. No fills. Hairline table rules. Fraction stacked in 7.1 and Example 7.2. Numbered steps carry no marker |
| Header (SHULL-CHG-0101) | PASS. Outlined chip, kicker in primaryDeep, condensed title with one accent word, meta block, double rule in display colour. Sizes match `print.header` |
| Binding margin / hole guides (SHULL-CHG-0103) | **FAIL**. Hole guides are correct and mirrored on even pages. But Figure 7.2 enters the inside margin on p2 (#3) |
| Page budget / even count | PASS. 8 pages (spec target 8, max 10, even). Key is 2 pages |
| Line length | PASS for body: builder measures about 56 characters a line, 3.55 in columns at 10.5 pt. Full-width directions and key prose exceed it (#8) |
| Figure adjacency (QA §10) | **FAIL**. Figure 7.1 (#1). Figures 7.2–7.7 sit with their text. Figure 7.5 crosses p4→p5, but those pages face each other in a binder |
| Molecular structures (SHULL-CHG-0042) | **FAIL** (#2) |
| Term flow | **FAIL** on 1 of 16 (#4). Bold terms in the body = 16, preview = 16, vocab page = 16, key = 16, and all four lists are identical. Section tags match where each term is first bolded. 15 of 16 are defined in the bolded sentence |
| Key matches student copy | PASS. All 7 Reading Check stems and all 3 question stems match the student copy word for word (string-compared). The 16 vocab definitions agree with the in-text definitions |
| Answer-key standard | PASS with a nice-to-have (#11). Separate `Key` file. Pen ink for written answers. Unit slashes (g/mol) are allowed by §5. Decimal points are clear. No ambiguous 2/a or 1/l in numbers |
| Every number re-solved | PASS. See table below |
| Matt's approved decisions | PASS. Notation is N = n × 6.022 × 10²³. Grep found no molar volume, 22.4, STP or litres. Worked examples (boxed) appear only in 7.3 (Ex 7.1) and 7.4 (Ex 7.2). 7.1 is built around sig figs with calculator, scale, gas pump and ruler examples |
| Textbook requirement | PASS. Full expository paragraphs, bold terms in context, 7 numbered and captioned figures, a Reading Check closing every section, 3 questions on p7 and vocab on p8 |
| No teacher / PROVISIONAL content on student pages | PASS. Grep found no "PROVISIONAL", "teacher", "Matt", "TBD" or "UNVERIFIED" |
| No standards codes printed | PASS. Grep found no Ohio or NGSS codes |
| Section codes vs. DECISIONS | PASS. 7.1–7.7 and their titles match `courses/chemistry/DECISIONS.md` l.54–56. Unit title matches. `validate_codes.py` OK |
| Codes agree (document / filename / folder) | PASS for document and footer: chip `U07 / S7.1-S7.7`, footer `UNIT 07`. Filename and folder are PENDING (see Unresolved) |
| Voice / anti-slop | PASS with minor findings (#4, #7, #12). Reads as a plain textbook, not a brochure. No §6 audit-list habits |
| Separate answer key | PASS |
| Rebuildable from spec | PASS. A clean rebuild into scratch (`build_reading_docx.py spec OUT`) gave PDFs identical in text and raster on every page. All `.docx` XML parts are byte-identical (only zip timestamps differ), and all 7 figure PNGs are byte-identical. The builder reported "8 pages", "2 pages" and "about 56 characters a line" |
| Drive destination | NOT FILED, as expected (known-pending). An independent Drive search for `title contains 'Unit 7 Reading'` returned nothing, so nothing was filed early |

## Prior verify-content findings (reports/chem_u07_reading_verify.md): each confirmed in the rendered PDF

| # | Finding | Status | Evidence in render |
|---|---|---|---|
| 1 | 150 lb / "more digits" false | APPLIED | p1: "say you weigh 148 lb … can't tell 148 lb from 148.4 lb … Its last digit is in the tenths place" |
| 2 | Precision definition (digit count; order of meanings) | APPLIED (but see #4) | p1: "describes how finely a tool measures, which shows in the place value of the last digit you can record. It also describes how closely repeated measurements agree". Vocab and key say "shown by the place value of the last digit … also, how closely repeated measurements agree". The key still says "Accept either meaning" |
| 3 | "number of digits" sentence; money rule | APPLIED | p1: "money is rounded to the cent by rule. The place value of the last digit tells you how finely a value was measured or set." |
| 4 | Q3 second correct answer | APPLIED | Key p2: "Also accept: state (gas vs liquid), as stated in 7.7." |
| 5 | Unit on N_A | APPLIED | p4: "6.022 × 10²³ particles per mole". Also names "Reference Sheet 1, Equations & Constants" |
| 6 | Empirical formula mass: count subscripts | APPLIED | p6: "the sum of the atomic masses of all the atoms in the empirical formula, counting each subscript". Key: "(count each subscript)" |
| 7 | Step 4 rounding cues | APPLIED | p5: "Near x.5, multiply all of the values by 2. Near x.33 or x.67, multiply by 3. Near x.25, multiply by 4." |
| 8 | Water drawn at about 120° | APPLIED | Measured about 105° on the 300 dpi render of Fig 7.5. Fixed 2D coordinates are in the figure script |
| 9 | "calculator shows 1.9978" | APPLIED | p4 Example 7.2: "The calculator shows 1.99778…" |
| 10 | 8.2 billion going stale | APPLIED | p3: "more than 8 billion people" (the grammar issue is #7) |
| 11 | Stale 9-page `png/` render | APPLIED | `build/chem_u07_reading/` contains only the 4 deliverables and `fig/`. `png/` is gone |

## Numbers re-solved (independently; student table H 1.01, C 12.01, O 16.00, Na 22.99, Cl 35.45)

| Printed | Re-solved | Result |
|---|---|---|
| 12.5 gal × $3.299 = $41.2375 → $41.24 | 41.2375 | PASS |
| 602,200,000,000,000,000,000,000 = 6.022 × 10²³ | 24 digits | PASS |
| One water molecule 2.99 × 10⁻²³ g | 18.02 / 6.022e23 = 2.992e-23 | PASS |
| 19 quadrillion yr; 1.4 million × age of the universe | 6.022e23 / 3.156e7 = 1.91e16; / 1.38e10 = 1.38e6 | PASS |
| More than 8 billion people → more than 2 million yr | 6.022e23 / 8e9 / 3.156e7 = 2.39e6 | PASS |
| 1 mol water ≈ 18 mL, a little over 1 tbsp | 18.07 mL; 1.22 tbsp | PASS |
| Nickel 5.00 g; 200 g → 40 | 40 | PASS |
| O₂ 32.00; H₂O 18.02; NaCl 58.44 | 32.00; 2.02 + 16.00; 22.99 + 35.45 | PASS |
| Ex 7.2: 36.0 g → 2.00 mol; calculator 1.99778… | 36.0 / 18.02 = 1.997780 | PASS |
| Ruler 4.6 (2 sf) / 4.63 (3 sf); 4.6382 = ten-thousandths | as printed | PASS |
| Water 11.2% H / 88.8% O; 2 of 3 = 67% | 0.1121 / 0.8879; 66.7 | PASS |
| 112 g H per 1 kg water | 0.112 × 1000 | PASS |
| CH₂O 30.03; 180.18 / 30.03 = 6; 40.0% C | 30.03; 6.000; 0.3999 | PASS |
| CH 13.02; C₂H₂ 26.04 = 2×; C₆H₆ 78.12 = 6×; 92.2% C | 13.02; 26.04; 78.12; 0.9224 | PASS |
| 6.022 × 10²³ has 4 sig figs | per Reference Sheet 2 | PASS |
| Benzene drawing | Kekulé ring with alternating double bonds (top, lower-left, lower-right), 6 C and 6 H, every C has 4 bonds | PASS |

## Findings (Blocking first, then shortest fix first)

| # | Check | Problem | Fix | Severity |
|---|---|---|---|---|
| — | — | No Blocking findings. | — | — |
| 1 | Adjacency (QA_GATE §10) | **Figure 7.1 is separated from its text by a page flip.** The text that explains it ("(Figure 7.1, top)", "(Figure 7.1, bottom)") is in the p1 right column. The figure is at the top of the p2 left column, which in duplex is the *back* of the same sheet. A student reading the ruler explanation cannot see the rulers. | Designer: reflow so Figure 7.1 lands on p1 next to "The estimated digit". For example, tighten the p1 front matter or the vocab preview, or move the "Precision"/gas-pump paragraphs after the figure. Re-render and confirm. | **Major** |
| 2 | Molecules (SHULL-CHG-0042; audit-deliverable §4) | **Fig 7.5 (H₂O) and Fig 7.7 (C₂H₂, C₆H₆) were not produced by `scripts/build_diagram_molecule.py`.** `make_chem_u07_figures.py` has its own `molecule()` routine (RDKit, explicit H kept, and fixed 2D coordinates for water). Its docstring says the script strips explicit H. CHG-0042 §2.1: "If RDKit cannot draw it well … stop and ask Matt — do not improvise." The docstring points to "the build report", but no build report exists in `reports/`. The structures themselves are correct (verify-content checked the SMILES, and this audit checked the drawings). The labels and molar masses are typed, not derived from the SMILES, which is the safeguard CHG-0042 exists to provide. | Overseer: either (a) route a change so `build_diagram_molecule.py` gains an explicit-H / fixed-coordinate option, and rebuild 7.5 and 7.7 through it, or (b) get and record Matt's explicit sign-off on this exception. Also file the missing build report or remove the reference to it. | **Major** |
| 3 | Binding margin (SHULL-CHG-0103; DS §8) | **Figure 7.2 enters the 0.60 in inside margin on p2 (an even page, so the inside margin is on the right).** The image's right edge is at x = 574.25 pt. The limit is 612 − 43.2 = 568.8 pt, so it intrudes 5.45 pt (0.08 in). The drawn "mole" box reaches about 572 pt. It does not touch the hole guide (which starts at 575.3 pt), but the rule is "Nothing else enters the inside margin". All other pages and figures stay inside. | Designer: the image is offset to the right in the ladder layout. Draw it within the column, or remove the indent, so the right edge is ≤ 568.8 pt. Re-measure. | **Major** |
| 4 | Term flow / Matt's "definitions bolded" | **Precision is bolded in a sentence that does not define it.** "**Precision** has two meanings, and you will see both." The definitions follow in the next two sentences. Page 1 tells students: "Each term in **bold** is defined in the sentence where it first appears." The other 15 terms meet that promise. "you will see both" is also filler. | Designer (spec text): "**Precision** describes how finely a tool measures, which shows in the place value of the last digit you can record, and also how closely repeated measurements agree with each other." Or keep two sentences, with the first one carrying the bold term and the first meaning. | **Major** |
| 5 | Numbering consistency | Figures 7.n and Reading Checks 7.n match their section numbers, but **Example 7.1 is in Section 7.3 and Example 7.2 is in Section 7.4**. A student told to "look at Example 7.1" may turn to Section 7.1. | Number the examples "Example 7.3" and "Example 7.4", or "Example 1" and "Example 2". | Minor |
| 6 | Chip consistency (NAMING §4, "one chip family") | The reading chip shows `U07 / S7.1-S7.7` with a hyphen-minus. `build_quiz.py` and `build_operation_periodic_table.py` use an en dash (`S7.1–S7.7`). | Use the en dash in `build_reading_docx.py` l.667 and l.718, so the chip matches the other unit-level documents. | Minor |
| 7 | Voice | p3: "If all of the more than 8 billion people on Earth counted…" reads awkwardly aloud. | "If every one of the more than 8 billion people on Earth counted…" or "If all 8 billion-plus people…". | Minor |
| 8 | Line length (QA_GATE §10) | Full-width prose runs past about 80 characters a line: the p7 directions (about 120 characters a line), the p8 directions (one line, about 115), and on the key the Teacher Notes and question stems (about 120–130). Body columns comply. | Set the directions to the column measure, or break them into two short lines. On the key, narrow the teacher-notes box. | Minor |
| 9 | Vague prompt (ANTI_AI_SLOP §7) | Q2 ends "Explain using the reading." §7 asks for prompts that name the evidence to use. | "Use Figure 7.3 in your explanation." | Minor |
| 10 | Traceability | The figure script refers to "the build report", but none exists in `reports/` (see #2). | File a build report, or remove the reference. | Minor |
| 11 | Key legibility (ANSWER_KEYS §7) | In ShullHand, "Cl" in "NaCl" (key p2 Q2, and vocab "formula unit") reads as "NaCI". The lowercase l is a plain vertical stroke, the same 1/l/I ambiguity §7 names. Context makes it clear to a chemistry teacher. | Set element symbols in the token's fallback (or the brand face), as is already done for digits. | Nice-to-have |
| 12 | Polish | Example 7.2 box has about one blank line between the equation and the explanation (p4). The key heading says "Questions (back page)", but the questions are on p7, which is not the back page. | Tighten the space after the equation. Change the heading to "Questions (page 7)". | Nice-to-have |

## Unresolved / pending: recorded, not failed

| Item | State |
|---|---|
| "Reading" document type is not in `standards/NAMING.md` §2 types | PENDING (known). No proposal exists in `governance/proposals/` yet (grep found no "Reading" type proposal). Working filenames are flagged in the spec's `workingFilename.$comment` |
| U7 short title "The Mole" is not in the DECISIONS "Short titles" table | PENDING (known). Under NAMING §2, "No row, no topic". The filename cannot be final until a row exists |
| Drive filing | NOT FILED (known; waits for Matt). Independent Drive search confirms no "Unit 7 Reading" object exists. Folder agreement (QA §6) can only be checked after filing |
| Precision bolded and in the vocab list | NEEDS MATT CONFIRMATION. The content brief §2/§4 said not to bold it (it is not in DECISIONS). The key's teacher note now states it as fact without the earlier "at your request". The repo has no record of the request |
| Sibling specs teach molar volume (22.4 L, STP) in U7 | OPEN, outside this deliverable (brief F2). `templates/worksheet/specs/chem_u07_s07.4.json` and `templates/assessment/specs/chem_u07_unit_test.json` disagree with this reading's scope and with DECISIONS l.74 (11.5). Matt to decide |
| 7.1 egg/dozen conversion is displayed as a set-up equation | CONFIRM WITH MATT that a one-line illustration does not count as a "worked example" (approved: worked examples in 7.3 and 7.4 only). It is not boxed or labelled as an Example |
| `keyHandwriting`, `keyInk.*`, `print.binding`, `print.holeGuides` tokens | PROVISIONAL in `brand/tokens.json`. This deliverable uses them as specified |

## Rebuild record

`python3 templates/reading/build_reading_docx.py templates/reading/specs/chem_u07_reading.json <scratch>` gave the following:
- Column 3.55 in, about 56 characters a line.
- 8-page student copy and 2-page key.
- PDFs identical in text and in raster on every page.
- `.docx` parts byte-identical.
- All 7 figures byte-identical.

The deliverable is fully reproducible from the spec.

---

# Round 2: Re-audit after the Designer's rebuild

**Date:** 2026-11-24 · **Auditor:** independent, report-only. Nothing was modified except this appended section.
**Files:** the same four files in `/home/user/WorkWork/build/chem_u07_reading/` (rebuilt 02:14), plus `fig/` (7 PNGs, regenerated).
**Coordinator instructions for this round:**
- Record #2 as Unresolved, pending Matt's decision. Do not fail the gate on it.
- Record precision bolding as decided. Matt approved a sample in chat that bolded and defined precision, before he said "Create the packet."

## Verdict: **PASS** (with #2 recorded as Unresolved, pending Matt)

- Every Round 1 finding except #2 is resolved, confirmed in the rendered PDFs.
- The fixes broke nothing. Page count, fonts, ink, colour, term flow, key match and rebuildability all still pass.
- Two new Minor/nice-to-have items appear below (R2-1, R2-2). Neither is a failed gate check.

What is still open: #2 waits on Matt. Naming and Drive filing are still pending, as known.

## Checklist (Round 2)

| Check | Result |
|---|---|
| Rendered and viewed, every page | DONE. Student pp 1–8 and key pp 1–2 at 100 dpi. Key handwriting ("NaCl") at 250 dpi |
| Page count / budget | PASS. Student 8 (even, spec target 8). Key 2 |
| Fonts (`pdffonts`, `audit_fonts.py`, `--key`) | PASS. Student copy is Archivo only. Key is Archivo plus ShullHand and Patrick Hand (the token's named fallback) |
| Ink (`audit_print_ink.py`) | PASS. Student worst page 7.15% toner (p2). Key worst 5.28%. Widest solid band 0.00 in |
| Colour inventory | PASS. Type is only #14161B, #B84100 (`primaryDeep`), #55604F, #61675B, #4A2466 (`keyInk.pen`, key only). No display colour is used as type |
| Clipped text | PASS. None on any of the 10 pages |
| Figure adjacency | PASS. Fig 7.1 is now on p1, directly under the ruler paragraphs. Figs 7.2–7.7 stay with their text. Fig 7.5 crosses p4→p5, which face each other in a binder |
| Binding margin | PASS. Fig 7.2 right edge is now 559.8 pt (limit 568.8). Residuals on even pages are ≤ 1.5 pt: a trailing-space glyph box on p2, and box rules at 569.2–569.4 pt. Both were present in Round 1, are within rendering tolerance, and stay well clear of the hole guides at 575.3 pt |
| p1 reflow and paragraph order | PASS. The new p1 order is: opener, scales, precision, "The estimated digit", the cm and mm ruler paragraphs, sig-fig definition, Figure 7.1. p2 continues with rounding, then the gas pump ("The place value of the last digit matters outside the lab, too"), then measured and exact numbers, scientific notation, and conversion factors. The logic reads in order and every cross-reference still points the right way |
| Line length | PASS. Body columns are about 56 characters a line (builder-measured). p7 and p8 directions are narrowed (longest line 74 characters). The key is now two-column (longest line 64) |
| Term flow | PASS. 16 bold body terms. All 16 are defined in the sentence that bolds them, including **precision**: "**Precision** describes how finely a tool measures, …, and it also describes how closely repeated measurements agree with each other." Preview, vocab page and key each list the same 16 terms |
| Key matches student copy | PASS. All 7 Reading Check stems and all 3 question stems (including the revised Q2) appear word for word in both files (string-compared) |
| Numbers | PASS. Every Round 1 value is unchanged and still present in the text. Figure labels are now computed from the RDKit molecule or formula plus `chem_data.py`, and the build stops on any mismatch with the brief. The rendered figure values (12.01, 18.02, 58.44, 26.04, 78.12, 13.02, 11.2/88.8) match the brief |
| No teacher / PROVISIONAL / standards-code content on student pages; no 22.4, STP or litres | PASS (grep) |
| Rebuildable from the spec | PASS. A clean rebuild into scratch gave identical text and raster on every page of both PDFs. Every `.docx` XML part and all 7 figure PNGs are byte-identical. The builder reported "8 pages", "2 pages" and "about 56 characters a line" |
| Drive | NOT FILED (known-pending) |

## Round 1 findings: status

| # | Finding | Status | Evidence (Round 2 render) |
|---|---|---|---|
| 1 | Fig 7.1 on the back of its text | **RESOLVED** | p1 right column: the ruler paragraphs, then Figure 7.1 and its caption, on the same side of the sheet |
| 2 | Molecules not made by `build_diagram_molecule.py` (CHG-0042) | **UNRESOLVED: pending Matt's decision** (not failed, per coordinator) | Partial fix confirmed: formulas, molar masses and percentages on Figs 7.3, 7.5 and 7.7 are now computed (`counts_of`, `molar_mass`, `hill`) and checked against the brief, and the build stops on a mismatch. The drawing itself still uses the local `molecule()` routine with explicit H kept. The figure script's docstring now records the exception as waiting on Matt |
| 3 | Fig 7.2 in the binding margin | **RESOLVED** | p2 image right edge is 559.8 pt (was 574.25) |
| 4 | Precision not defined in its own sentence | **RESOLVED** | p1: "**Precision** describes how finely a tool measures, which shows in the place value of the last digit you can record, and it also describes how closely repeated measurements agree with each other." The filler "you will see both" is gone |
| 5 | Example numbering | **RESOLVED** | p3 "EXAMPLE 7.3" (in 7.3), p4 "EXAMPLE 7.4" (in 7.4). No "Example 7.1" or "7.2" remains |
| 6 | Chip hyphen | **RESOLVED** | Chip on student and key reads `U07 / S7.1–S7.7` (en dash, U+2013). Builder l.676 and l.727 |
| 7 | "all of the more than 8 billion" | **RESOLVED** | p3: "If every person on Earth, more than 8 billion people, counted at the same time…" |
| 8 | Over-long directions and key prose | **RESOLVED** | p7 and p8 directions wrap at ≤ 74 characters. The key is two-column, with teacher notes in the left column (≤ 64 characters). See R2-2 for the question stems |
| 9 | Q2 "Explain using the reading" | **RESOLVED** | p7 Q2 and key: "Use Figure 7.3 and Section 7.3 to explain." |
| 10 | Docstring cites a missing build report | **RESOLVED** | The docstring now says "Whether to extend that script or keep this exception is waiting on Matt (audit finding #2)." There is no dangling reference |
| 11 | "NaCl" reads as "NaCI" in ShullHand | **RESOLVED** | "Cl" is now set in Patrick Hand (all 4 occurrences checked). Its l has a curved tail and reads clearly as "NaCl" at 250 dpi |
| 12 | Example 7.2 gap; "Questions (back page)" | **RESOLVED** | The Example 7.4 box is tight. Key heading reads "Questions (page 7) — exemplar answers" |

## New findings (Round 2)

| # | Check | Problem | Fix | Severity |
|---|---|---|---|---|
| R2-1 | Adjacency (QA §10), introduced by the reflow | On p2, "write the factor with dozen on the bottom so it cancels:" ends the left column, and the displayed equation (3 dozen × 12 eggs / 1 dozen = 36 eggs) starts the right column. The colon's lead-in and its equation are split by a column break. Same page, so no flip is needed. | Keep the lead-in sentence with the equation (keep-with-next on the paragraph), or move one line. | Minor |
| R2-2 | Line length | The p7 question stems are still set full width (longest line about 105 characters). They are short, one to three lines, and are not running prose, so the body rule is met in spirit. | Optionally indent or narrow the stems to the column measure. | Nice-to-have |

## Unresolved / decided (Round 2)

| Item | State |
|---|---|
| #2 Molecule-script exception (SHULL-CHG-0042) | **UNRESOLVED: pending Matt's decision.** The options are: (a) extend `scripts/build_diagram_molecule.py` with an explicit-H / fixed-coordinate option and rebuild Figs 7.5 and 7.7 through it, or (b) record Matt's approval of the local routine as an exception. Structures are verified correct, and labels are now computed and checked |
| Precision bolded and in the vocab list | **DECIDED.** Matt approved, in chat, a sample that bolded and defined precision, before he said "Create the packet." Precedence 1 (Matt's direct instruction) overrides content brief §2. The repo holds no copy of that chat. It is recorded here on the coordinator's report |
| "Reading" type in NAMING.md; U7 short title in DECISIONS | PENDING (known). No proposal is filed yet. Filenames are working names |
| Drive filing | PENDING (known; waits for Matt). Folder-path code agreement can be checked only after filing |
| Sibling specs teach 22.4 L / STP in U7 | OPEN, outside this deliverable (brief F2). Matt to decide |
| 7.1 dozen-to-eggs displayed setup vs "worked examples only in 7.3/7.4" | CONFIRM WITH MATT. It is not boxed or labelled as an Example |
| `keyHandwriting`, `keyInk.*`, `print.binding`, `print.holeGuides` | PROVISIONAL tokens, used as specified |

---

# Round 3: "Option B" textbook redesign

**Date:** 2026-11-24 · **Auditor:** independent, report-only. Nothing was modified except this appended section.
**Files:** the same four files in `/home/user/WorkWork/build/chem_u07_reading/` (rebuilt 10:45–10:46), plus `fig/`.
**Approved by Matt (not re-litigated here):**
- Why It Matters opener.
- Seven Connection boxes.
- Option B layout: two columns, display-title opener, first-line indents, set-off definition lines, caps headings, rule-only Example banners, On Your Own boxes, running header, outside thumb tab, centred page numbers.
- Stay within SHULL rules: Archivo only, no fills.

**Scope note:** verify-content is running in parallel, so the science was spot-checked only.

## Verdict: **INCOMPLETE**

- No Blocking findings.
- Two Major checks fail:
  - Opener text runs into the column rule on p1 (R3-1).
  - The vocabulary preview's K / S / N columns have no legend (R3-2).
- One Major printability risk, which you asked me to judge: the thumb tab sits 0.14 in from the paper edge on **every** page, odd and even alike (R3-3).
- Everything else passes: ink, fonts, binding margin, hole guides, term flow (16 / 16 / 16 / 16 / 16), key match including On Your Own, answer-key standard, line length, and rebuildability.

## Checklist (Round 3)

| Check | Result |
|---|---|
| Rendered and viewed, every page | DONE. Student pp 1–8 and key pp 1–2 at 100 dpi. Zooms at 200 dpi of the p1 opener and vocab preview, and of the key's On Your Own solutions |
| Page count | PASS. Student 8 (even). Key 2 |
| Fonts (`pdffonts`, `audit_fonts.py`, `--key`) | PASS. Student copy is Archivo / Archivo Narrow only. Key adds ShullHand and its token fallback, Patrick Hand |
| Ink (`audit_print_ink.py`) | PASS. Worst page 8.22% toner (p2), under the 9% ceiling. Average 5.69%. Key worst 4.87%. Widest solid band 0.00 in on both. Highest pages yet (p1 8.09%, p2 8.22%), but within budget |
| Fills / print discipline | PASS. No fills anywhere. Example banners are a rule only. On Your Own boxes are hairline outlines. Connection boxes are a course rule above and a hairline below. Reading Checks are outlined. Thumb tab is outline only |
| Coloured type on white | PASS. Coloured type is only `primaryDeep` #B84100: caps headings, definition lines, labels, display-title accent, tab text. `primaryDeep` measures 5.53 on white against a 5.5 target, so the 9 pt definition lines clear the type rule. The display orange is used only for rules. The key uses `keyInk.pen` #4A2466 for prose, `keyInk.pencil` #5A6068 for On Your Own math and `keyInk.box` #9F1D2C for answer boxes, as `ANSWER_KEYS` §2 requires |
| Grayscale | PASS. Each box type differs by shape as well as colour: Reading Check is a full outline with a heavy left edge, Connection has a top rule plus a hairline, Example is a banner rule, On Your Own is a hairline box. Definition lines differ from body by indent, em dash and bold term |
| Clipped text | **FAIL** (R3-1). No hard clip at any page or box edge. But the p1 opener's left-column text runs up to the vertical column rule |
| Binding margin / hole guides | PASS. Hole guides sit at 18.0 pt (odd) and 575.3 pt (even), at y 80.7, 386.6 and 692.7, outline only, mirrored on every page. Nothing enters the 0.60 in inside margin beyond the ≤ 1.5 pt residual of box rules and a trailing-space glyph box, unchanged since Round 1 and well clear of the holes |
| Thumb tab: outside edge, clear of the binding margin | PASS on placement. Right edge on odd pages (581.7–601.8 pt) and left edge on even pages (10.1–30.2 pt), at the same height (y 173–210 pt) on all 10 pages. Never on the binding side. Its inner edge stays inside the 0.50 in outside margin (builder `TAB_EDGE_IN` 0.14 + `TAB_W_IN` 0.28) |
| Thumb tab: printability | **RISK, Major** (R3-3) |
| Page numbers | PASS. Centred, from an auto `PAGE` field in every footer part (`footer1`–`footer5.xml`), which satisfies DS §11's "auto-generated page count" |
| Header / footer duplication | PASS on pp 2–8, with a Minor on p1 (R3-6). The running header carries course and doc type on the inside and unit plus title on the outside. The footer carries only the page number and no longer repeats the path. On p1, the unit title is printed three times |
| Figures and boxes beside their text | PASS. Figs 7.1 (p1), 7.3 and 7.4 (p4), 7.5 and 7.6 (p5) and 7.7 (p6) sit with their text. Fig 7.2 is referenced at the foot of p2 and placed at the top of p3. Those pages face each other in a binder, so no flip is needed. Accepted, as Fig 7.5 was in Round 1 |
| Example 7.3 → On Your Own 7.3 (the designer's reported p3→p4 flip) | **Not present in this build.** Example 7.3 and On Your Own 7.3 are both on p3 (right column, one above the other). Example 7.4 and On Your Own 7.4 are both on p4. On Your Own 7.4's pointer back to "Section 7.3 gives the molar mass of O₂" is a back-reference to the previous page (32.00 g/mol, p3), which is acceptable. The designer's note likely describes an earlier layout. Nothing to fix |
| Line length | PASS. Body columns about 56 characters a line (builder-measured). Why It Matters about 58. Connection text ≤ 65. Directions on pp 7–8 ≤ 76. Question stems now wrap at the column measure (Round 2's R2-2 is resolved). Key lines ≤ 64 |
| Term flow | PASS. 16 bold terms in the body = 16 set-off definition lines = 16 preview terms = 16 vocab-page terms = 16 key definitions. String check: every definition line reads "Term — [definition]", identical to the spec vocab definition, and appears word for word in the key. Every bold term is defined in its own sentence, precision included (p1) |
| Key matches student copy | PASS. All 7 Reading Check stems, both On Your Own stems and all 3 question stems appear word for word in both files |
| On Your Own solutions (spot check) | PASS. CH₄: 12.01 + 4(1.01) = 16.05 g/mol. 64.0 g ÷ 32.00 g/mol = 2.00 mol (3 sig figs). The builder re-solves both at build time ("molarMass re-solved = 16.05", "gramsToMoles re-solved = 2.0") |
| Answer-key standard | PASS (Minor polish in R3-8). On Your Own math is in pencil ink with answers boxed in box ink, each step on its own line, and the 7.4 division stacked. g/mol inline is allowed by §5. Digits and decimal points are legible. "Cl" is set in the fallback face |
| New prose: voice / anti-slop | PASS with Minor findings (R3-4, R3-5). The opener and the seven Connections read as plain, concrete textbook prose with no brochure language. Spot-checked facts: "1,000 times finer" (0.0001 vs 0.1 g) ✓. "$73 trillion" ✓ (6.022e23 ÷ 8.2e9). "888 g oxygen" ✓. Nickels, isotopes, medicine ✓ |
| No teacher / PROVISIONAL / standards-code content; no 22.4, STP or litres | PASS (grep) |
| Codes | PASS. Chip `U07 / S7.1–S7.7`. `validate_codes.py` OK. Sections match DECISIONS l.54–56 |
| Rebuildable from the spec | PASS. A clean rebuild into scratch gave identical text and raster on every page of both PDFs. Every `.docx` XML part and all 7 figure PNGs are byte-identical |
| Drive | NOT FILED (known-pending) |

## Findings (Round 3)

| # | Check | Problem | Fix | Severity |
|---|---|---|---|---|
| R3-1 | Clipped text / collision (QA §3) | **On p1, the opener's left-column text runs into the vertical orange column rule.** "Each term in **bold** is defined in" ends about 1 pt from the rule (rule at x = 298.8 pt; the line box is 300.5 pt with its trailing space). "reread the" ends about 3 pt from it. At reading size, "in" looks like it touches the rule. The left cell has no gutter padding. | Designer: add right padding to the opener's left cell (or move the rule into the gutter) so text clears the rule by at least the column gap. Re-render and check the p1 zoom. | **Major** |
| R3-2 | Directions / usability | **The vocabulary preview headers are abbreviated to "K S N" with no legend.** The directions say only "Before you read, mark one box for each term." Rounds 1–2 printed "KNOW IT · SEEN IT · NEW". A student cannot tell what K, S and N mean. | Add the legend to the directions, e.g. "Before you read, mark one box for each term: K = I know it, S = I've seen it, N = it's new." Or restore the full headers if they fit. | **Major** |
| R3-3 | Printability (thumb tab) | **The tab's outer stroke is 0.14 in from the paper edge on every page, odd and even** (0.141 in odd, 0.140 in even). The "UNIT" text is 0.159–0.164 in from the edge. Many laser printers and copiers cannot print the outer 0.167 in (4.2 mm) or more. On the classroom copier, the outer stroke would likely drop and the "UNIT" letters could be shaved. That would be clipped text that the PDF render cannot show. The tab sits inside the outside margin and never touches the binding side, so placement is otherwise correct. | Designer: move the tab inward. `TAB_EDGE_IN` 0.22 puts the stroke at 0.22 in and the inner edge exactly at the 0.50 in margin (0.22 + 0.28). Or narrow the tab. Then confirm on a test print on Matt's copier, together with the PROVISIONAL hole-guide test punch. | **Major** (risk) |
| R3-4 | Science wording (for verify-content) | Connection 7.7: "benzene is used as a liquid solvent." Today benzene is mainly a feedstock for plastics and other chemicals. In the US, solvent use has largely been phased out because of toxicity, so the present-tense claim is dated. The content brief's own framing ("a liquid solvent") carried this in. | "benzene is a liquid used to make plastics and other chemicals." Leave final wording to verify-content. | Minor |
| R3-5 | Voice: repetition (ANTI_AI_SLOP §6) | The pharmacist point appears twice: Why It Matters ("Pharmacists use this idea when they measure a medicine by mass, because what matters in the body is how many molecules arrive") and Connection 7.4 ("A pharmacist measures a medicine on a balance, but the body responds to how many molecules arrive"). | Cut the last sentence of Why It Matters, or give the 7.4 Connection a different example. | Minor |
| R3-6 | Header duplication | On p1, the unit title is printed three times (SHULL-CHG-0101 header title, header meta line "Unit 7 · The Mole & Chemical Quantities", and the display title) and "Unit 7" four times (chip, meta line, "UNIT 7" eyebrow, thumb tab). The display title is Matt-approved and the header is LOCKED, so the overlap is structural. The "UNIT 7" eyebrow above the display title adds nothing the tab and chip don't already say. | Drop the "UNIT 7" eyebrow. Ask Matt whether the display-title opener should replace the header's title line on readings (that would be a CHG-0101 question). | Minor |
| R3-7 | Adjacency across a flip | Two text splits cross a sheet flip. (a) The precision sentence ends at the foot of p1, and its set-off definition line starts p2 (back of the same sheet). (b) The 7.6 five-step list splits: steps 1–3 on p5, steps 4–5 on p6 (back of the sheet). The definition is still complete in the p1 sentence, and the list is continuous text, so neither is a figure split. | Keep each definition line with its sentence, and keep the 7.6 list together (keep-with-next / keep-lines). | Minor |
| R3-8 | Key polish | On Your Own 7.4 in the key: the equation ends with "=" and the boxed "2.00 mol O₂" sits about two lines lower, with empty space between. On Your Own 7.3 also breaks after "=". | Put the boxed result on the same line as the "=", or directly below it with no gap. | Nice-to-have |
| R3-9 | Token use | The running-header unit title is set in `ground.label` (#55604F, bold 7 pt). The token that names this role is `ground.footer` ("Running header and footer text only"), which the course/doc-type half of the same header already uses. | Use `ground.footer` for both halves of the running header. | Nice-to-have |

## Prior-round status

| Item | Status |
|---|---|
| Round 1 #1, #3–#12 | Still resolved in the redesign: Fig 7.1 on p1; Fig 7.2 clear of the binding margin; precision defined in its own sentence; Examples 7.3 and 7.4; en-dash chip; the 8-billion wording; line length; Q2 prompt; docstring; "Cl" in the fallback face. The "Questions (page 7)" heading and Example spacing are fine |
| R2-1 (dozen lead-in split from its equation) | **Resolved.** p2: "To find the number of eggs in 3 dozen, write the factor with dozen on the bottom so it cancels:" sits directly above the equation in the right column |
| R2-2 (full-width question stems) | **Resolved.** The p7 stems wrap at the column measure |
| #2 Molecule-script exception (SHULL-CHG-0042) | **UNRESOLVED: pending Matt's decision.** Unchanged: figure labels are computed, and the drawings come from the local RDKit routine. Not failed, per coordinator |
| Precision bolding | **DECIDED** (Matt approved the chat sample before "Create the packet") |
| "Reading" type in NAMING; U7 short title in DECISIONS; Drive filing | PENDING (known). No proposal is filed yet. Not filed to Drive |
| Sibling specs teach 22.4 L / STP; 7.1 dozen setup vs "worked examples only in 7.3/7.4" | OPEN / confirm with Matt (unchanged). The On Your Own items are in 7.3 and 7.4 only, matching that decision |
| PROVISIONAL tokens (`keyHandwriting`, `keyInk.*`, `print.binding`, `print.holeGuides`) | Used as specified. The R3-3 test print should be done alongside the hole-guide test punch |
