# Physics U4 Unit Reading: Independent Accuracy and Print Review

Auditor | 2026-11-26 | Route: `workflows/unit-textbook.md` "Independent accuracy and print review", `standards/QA_GATE.md`
Status: REPORT ONLY. Nothing outside `reports/` was edited.

## Verdict: FAIL (INCOMPLETE)

One blocking finding (B-1) and one major finding (M-1). Everything else passes. The arithmetic,
the key, the leaf, the fonts, the ink, the binding and the notation all pass. Return the findings
to the textbook-page-designer. I recheck the corrected export.

## Version and coverage

| Item | Value |
|---|---|
| Commit | `bac0846` "Physics U4 reading: build Work & Energy unit reading (pre-audit)", branch `claude/ecstatic-pascal-9cro1w` |
| Student PDF | `build/phys_u04_reading/Unit 4 Reading - Work & Energy.pdf`, 8 pp, Letter, sha256 `61456978c6c71be1209b17140320cd5baf53e5e672ba62a8d4912f4859edd920` (matches the commission) |
| Key PDF | `build/phys_u04_reading/Unit 4 Reading Key - Work & Energy.pdf`, 2 pp, sha256 `ea76157daf8b60f6a0878e874d7ac1508729f7f07f2f39e140dd82a5788f9450` (matches) |
| .docx | Both converted with soffice: 8 pp and 2 pp. The student text is byte-identical to the shipped PDF's pdftotext output |
| Spec / figures | `templates/reading/specs/phys_u04_reading.json`; `templates/reading/specs/make_phys_u04_figures.py` (I read all 7 figure functions) |
| Pages inspected | Student pp. 1–8 and key pp. 1–2, all rendered in grayscale at 100 dpi, with 220–250 dpi crops of θ glyphs, the FBD, the angled pull and the key θ |
| Proof method | **Screen proof only**, plus a simulated light-photocopy tone curve on p5. No physical photocopy was made |
| Primary sources | Not reachable. curl to openstax.org, energy.gov, nrel.gov, bipm.org and afdc.energy.gov returned "CONNECT tunnel failed, response 403" from the agent proxy. Claims were traced to dossier locators, and every physics claim was checked independently |

## Independent re-solve (from printed givens, before comparing)

| Item | My result | Printed (reading / key) | Match |
|---|---|---|---|
| Ex 4.1 push / friction / FN, Fg / net | +480. J / −360. J / 0 J / +120. J; check ∑F = 30.0 N × 4.00 m = 120. J | same | ✓ |
| Fig 4.2 area | (120. N)(4.00 m) = 480. J | same | ✓ |
| Angled pull | 50.0 cos 30.0° = 43.3 N; 50.0 sin 30.0° = 25.0 N; W = 216.5 → 217 J | same | ✓ |
| OYO 4.1 (72.0 kg, 2.50 m, 4.00 s) | W = 1764 J → 1.8 × 10³ J; P = 441 → 4.4 × 10² W; from the rounded W: 450 → 4.5 × 10² W | 1.8 × 10³ J; 4.4 × 10² W; key accepts 4.5 × 10² W | ✓ |
| Horsepower | 441/745.7 = 0.59 hp; "≈ 746 W" only on the student page | same | ✓ |
| Ex 4.2 | KE_i = 2.40 × 10⁵ J; F = 2.40 × 10⁵/48.0 = 5.00 × 10³ N, opposite the motion (a = 4.17 m/s²) | same, with direction | ✓ |
| OYO 4.2 | ½(0.145)(40.0)² = 116 J | 116 J | ✓ |
| Braking connection | 48.0 × 4 = 192 m (braking only, same force); key: 78 m → 252 m with 1.5 s reaction | same | ✓ |
| Ex 4.3 | ½(400.)(0.150)² = 4.50 J; kx = 60.0 N; triangle 4.50 J | same | ✓ |
| OYO 4.3 | (2.00)(9.8)(1.20) = 23.52 → 24 J; 39.2 − 15.68 = 23.52; no change from the table | same | ✓ |
| Ex 4.4 | √(2 × 9.8 × 3.20) = 7.92 → 7.9 m/s, direction stated | same | ✓ |
| OYO 4.4 | 1881.6 − 1470 = 411.6 → 4.1 × 10² J (key accepts 4 × 10² J) | same | ✓ |
| Fig 4.4 | KE(20.0) = 2.40 × 10⁵ J, KE(40.0) = 9.60 × 10⁵ J, ×4 | same | ✓ |
| Sig figs / units | Every answer that uses g has 2 sf. Trailing-decimal givens are used (120., 1200., 400.). Unit cancellation is shown in Ex 4.1–4.4 | — | ✓ |

## Findings

| # | Page / item | Claim or calculation | Independent evidence or result | Severity | Disposition |
|---|---|---|---|---|---|
| B-1 | p2, POWER, first sentences | "Two students climb the same stairs, one walking and one running. They do the same work against gravity, but the runner does it in less time." | Work against gravity is mgh, so it depends on each student's mass. Two different students do the same work only if they weigh the same. As printed, the claim is false, and it implies that work does not depend on mass. The workflow requires stating an idealization when it changes the interpretation. | **Blocking** (incorrect science on a student page) | Designer: e.g. "Two students **of the same mass** climb…" or "You climb the same stairs twice, once walking and once running." Recheck p2 reflow. |
| M-1 | p5, Example 4.3 follow-up | "Compressing the spring 0.150 m instead of stretching it stores the same energy…" | The example's givens say the spring is **compressed** 0.150 m. The sentence assumes a stretch, so it contradicts the worked example it follows. The physics (x² gives the same energy) is right. | Major (an internal contradiction in a worked example) | Designer: "Stretching the spring 0.150 m instead of compressing it stores the same energy…" |
| m-1 | p6, ¶ "So mechanical energy is conserved only when friction is negligible" | Condition for conserving ME | p5 gives the correct condition: "no friction and no other outside pushes" (dossier 4.4-b). The p6 sentence narrows it to friction alone. | Minor | Designer: "…only when friction and other outside pushes are negligible…" |
| m-2 | p6, WHEN FRICTION ACTS | "…she reaches the bottom more slowly" | The intended meaning is a lower speed. "More slowly" also reads as "takes longer". | Minor | Designer: "…at a lower speed." |
| m-3 | p4, Connection: Braking distance | "the brakes and tires do negative work on the car" | The external force that does negative work on the car is road friction on the tires. The brakes are internal to the car. | Minor | Designer: "friction from the road on the tires does negative work on the car". Optional. |
| m-4 | p1→p2, Figure 4.1 | First reference ("two pictures (Figure 4.1)") is the last paragraph of p1. The figure is at the top of p2 (a page turn). | QA_GATE §10 adjacency. It is the next page, not a page flipped past, and Example 4.1 sits beside it on p2. | Minor | Designer: move the reference sentence to p2, or accept. Not blocking. |
| m-5 | p1, 4.1 first paragraph | The inline definition note ("Work — …") sits between "For a constant force," and "W = Fd cos θ" | This splits one sentence across the note and makes the reading order awkward. The same note pattern repeats for all ten terms, restating the bold sentence just above. | Minor | Designer: end the sentence before the note, or place the note after the equation. |
| m-6 | p5, Connection: Pumped storage | "The National Renewable Energy Laboratory calls it the most common type of grid-level energy storage." | Dossier 4.3-j (S) excerpt supports the claim. I believe DOE renamed NREL "National Laboratory of the Rockies" in Dec 2025. **Unverified:** the proxy blocked nrel.gov. | Minor (open) | Researcher: confirm the current name, or attribute the claim to DOE (dossier 4.3-j also has DOE's "most dominant form of energy storage"). |
| m-7 | Sources, all pages | Dossier items 4.1-b (W = Fd cos θ wording), 4.1-e BIPM, 4.1-k NIST hp (K/SEC) | Primary hosts are still blocked (403). Every printed claim is standard physics that I verified independently. None is printed from an UNVERIFIED row. | Minor (open; a missing primary locator stays open per the workflow) | Researcher: open the primary pages when the allow-list permits. This does not block release on its own. |
| m-8 | Print, all pages (grayscale) | Box outlines (On Your Own boxes, In This Unit, Key Refreshers), table hairlines and the leaf's write-in rules use `ruleHairline` #C8CDC2 (gray 202), 0.25–0.75 pt | On the screen proof all are visible. Under a simulated light-copy curve (p5), the On Your Own outline and the thumb-tab outline **drop out**, while the Quantum Gold rules (gray 187, 1.0–3.0 pt) survive faintly. Writing space is unaffected because the boxes are open space. | Minor (system-wide token, not this build) | Overseer: if physical copies confirm it, propose a darker hairline under `brand/`. Not a designer fix for this edition. |
| n-1 | Glyphs | θ on student pages | θ is set as small raster pictures (283–310 ppi) that sit on the baseline and match the x-height (crops checked p1, p2). No Δ, no η, no U+03A3 Σ on student pages. ∑ is U+2211 (Archivo). The key's θ is in ShullHand, and its single Δ is Archivo (it has the glyph), in teacher notes only. | Pass. Info: the picture θ is not extractable text, and `audit_fonts.py --physics` is still pending (SHULL-CHG-0072) | None required. |
| n-2 | p1–p5, prose | Work symbol W | It is set Bold-Italic in running text, so it can look like a bolded vocabulary term. | Nice-to-have | Designer: set it italic, not bold-italic. |
| n-3 | p2, FBD | Arrow scaling | Push : friction = 0.576 in : 0.432 in = 120 : 90 ✓. FN = Fg ✓. The vertical pair is not scaled against the horizontal pair because no mass is given; the caption says only "120. N and 90.0 N arrows are scaled to each other". One arrow per force, no motion arrow, and d is a bracket on a separate scene sketch. | Pass | — |
| n-4 | p2 / p3, notation | Friction symbol f | U3 notes write fk. | Nice-to-have | Designer, optional. |
| n-5 | p4, Figure 4.5 | Path 1 dashed arrow | It runs up through the shelf line to a book sitting on the shelf. This is schematic, and the caption reads correctly. | Nice-to-have | Optional. |
| n-6 | p3, Ex 4.2 | Solve step | Goes from "F(48.0 m)(cos 180°) = −2.40 × 10⁵ J" straight to "5.00 × 10³ N" with no division row. The units row covers the step. | Nice-to-have | Optional "F = 2.40 × 10⁵ J ÷ 48.0 m" row. |
| n-7 | p3, Connection: wall | The horsepower sentence is appended to the wall connection | A non sequitur in a short box. Matt allowed one sentence only, and it is correct. | Nice-to-have | Optional. |
| n-8 | Key p2, OYO 4.4 | ME_f = ½(60.0)(7.0)² | This assumes PE_f = 0 at the bottom without saying so. | Nice-to-have | Key: "(reference level at the bottom)". |

## Physics subtleties (requested checks)

| Check | Result |
|---|---|
| Braking, not stopping, distance, with the same-force condition | ✓ cover, p4 Connection, tear-off 4.2 and key. The key explains why stopping distance does not quadruple. NHTSA is not quoted |
| PE system (object–Earth) | ✓ definition, p4 prose ("the book has PE" as shorthand), Ex 4.4 "skateboarder + Earth", pumped storage "water–Earth system". Ex 4.3 "System: the spring" is correct for PE_s |
| F = kx as a magnitude with direction in words | ✓ p4. The key notes F = −kx. The Hooke's-law limit is worded accurately |
| "Transformed into thermal energy" | ✓ OYO 4.4, p6 prose, regenerative braking, pumped storage. No "lost", "used up", "wasted", "efficiency" or "%" on student pages (grep) |
| Angled pull asks only for the pull's work | ✓ the friction exclusion is explained (3.5) |
| One cos θ case; hp ≈ 746 W only; no η | ✓ |
| W_net, KE_f − KE_i, PE_g, PE_s, ME; no Δ | ✓ student pages carry no Δ |
| ∑F not Fnet/Σ | ✓ U+2211 three times |
| g = 9.8, 2 sf; units cancelling; vector directions | ✓ braking force "opposite the car's motion"; Ex 4.4 velocity direction stated |
| Figures as evidence | Fig 4.2/4.4/4.6 axes are labelled with units, and the hatched areas are correct. In Fig 4.7 the bars are schematic and unnumbered. The friction chart uses 72:28, which differs from OYO 4.4's 78:22, so it does not give the answer away. The bars differ by hatch, open and dotted fills, so they read apart in grayscale |

## Leaf, cover and Key Refreshers

| Check | Result |
|---|---|
| Cover list = headings = question labels = key | 4.1–4.4 match one-to-one: In This Unit, the section headings (pp. 1, 3, 4, 5), the tear-off labels (p7), the key (p1) ✓ |
| Cover layout (0119/0120) | Large "4" numeral with a vertical course rule and the display title; unboxed Why It Matters (5 lines) beside an outlined In This Unit box; a full-width outlined Key Refreshers box with hairline column dividers; a How to Use row of 3 steps that describe the leaf as printed; then 4.1. No fills ✓ |
| Key Refreshers (0117 as amended by 0120) | 4 items, each opening "Unit N (N.n):", before the first section. The codes 1.1, 3.1, 3.2 and 3.4 exist in DECISIONS. I traced each to the built notes: U1 spec l.63 (scalar, in 1.1); U3 spec l.107 (Fg = mg, in 3.1), l.277 (components, in 3.2), l.398 (∑F = ma, in 3.4). No bold terms, no examples, and no tear-off question uses them ✓ |
| Name line; due line verbatim | ✓ "Due ASAP. No late work will be accepted. We will start the unit with this." |
| 4 single-part questions answerable from the reading | ✓ 4.1 perpendicular (p1), 4.2 ×4 braking (cover, p4), 4.3 path independence (p4), 4.4 thermal energy (p6) |
| Vocabulary | 10 terms, no definitions printed, 2 ruled lines each. Each term traces to its bold definition: work, joule (p1); power (p2); kinetic energy, work-energy theorem (p3); gravitational potential energy, spring constant, elastic potential energy (p4); mechanical energy (p5); law of conservation of energy (p6). The key definitions match the reading word for word ✓ |
| Parity | The reading ends on p6 (even), so there is no blank back. The leaf is p7 (front, odd) and p8 (reverse, even). Binding audit: odd pages bind left, even pages bind right, consistent with long-edge duplex ✓ |
| Simulated removal | Removing physical sheet p7/p8 leaves pp. 1–6 intact. The p6 reading text and the OYO 4.4 box stay in the packet. The leaf carries no reading content ✓ |
| OYO work space (SHULL-CHG-0122) | Open boxes on all four On Your Own items. Scoped to this reading ✓ |

## Mechanical audits

| Audit | Result |
|---|---|
| `pdffonts` / `audit_fonts.py` | Student: Archivo and Archivo Narrow only ✓. Key `--key`: Archivo plus the key handwriting faces (ShullHand, PatrickHand) ✓. `--physics` is pending (SHULL-CHG-0072) |
| `audit_print_ink.py` | Student PASS, worst 6.58% toner (p1), average 4.44%, no fill, widest solid band 0.00 in. Key PASS, worst 5.80% ✓ |
| `audit_binding.py` | Student, 8 pp: hole zone clear, guides on the binding side ✓. Key, 2 pp ✓ |
| Clipped text | None found on any rendered page ✓ |
| Coloured type | One deep token only: primaryDeep #896107 (5.56:1). Labels are #55604F, footers #61675B. No display colour is used as type ✓ |
| Codes / naming | "U04 / S4.1–S4.4"; the filenames follow SHULL-CHG-0121; `validate_codes.py` OK ✓ |
| Separate key | ✓ |
| Drive destination | Not filed (pre-audit). It is checked at the approval-to-file gate |

## Quantum Gold rules and the mixed pairing

The gold rules (gray 187, contrast 1.78) print pale but survive on the screen proof and on the
simulated light copy. None of them carries information on its own; every box also has its heading
label. The more fragile element on a light photocopy is the `ruleHairline` gray (202) used for box
outlines and the leaf's write-in rules (m-8).

**Mixed pairing:** Deep Purple rules (gray 124) with primaryDeep type are permitted by
`brand/SHULL_DESIGN_SYSTEM.md` (SHULL-CHG-0108/0109), and they would photocopy darker. Physics
"Course brand exceptions" reads **None**, though, so using them needs a recorded course decision from
Matt. **Not advisable as a fix for this edition.** The default pairing is compliant and legible.
The mixed pairing would not fix the hairline issue, which is where the real copier risk is. If
physical copies come out too pale, it is a reasonable course-level proposal for Matt.
