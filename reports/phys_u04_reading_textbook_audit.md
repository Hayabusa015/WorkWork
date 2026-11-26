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

---

# Round 2: recheck of the corrected export

Auditor | 2026-11-26 | Report only. Nothing outside `reports/` was edited.

## Verdict: PASS

B-1 and M-1 are fixed, and so are m-1 to m-6, n-4 and n-6 to n-8. Nothing new is blocking or major.
m-7 (primary sources blocked) and m-8 (hairline grey on photocopies) stay open. As in Round 1,
neither blocks this edition. The reading is ready for the approval-to-file gate.

## Version and coverage

| Item | Value |
|---|---|
| Commit | `26bbe37` "Physics U4 reading: apply audit round 1 fixes (stairs wording, spring sentence, minor wording, f_k, DOE credit)". It changes only the spec and the figure script. The Round 1 build commit now shows in history as `dd164c8` (Round 1 recorded `bac0846`; same message) |
| Student PDF | same path, 8 pp, sha256 `30dd0218d2a55790ad3dd66b186f2c959330731262ff51b5d0339e24028d18c0` ✓ |
| Key PDF | same path, 2 pp, sha256 `04eb69760fd2778a5afcebf923d0d492f1013910c43d64ddde31df0a26d03848` ✓ |
| Inspected in full | Student pp. 1–6 and key pp. 1–2, rendered in grayscale at 100 dpi. I diffed every sentence of the key text against my Round 1 conversion |
| Reused evidence | Student pp. 7–8. The new 100 dpi grayscale renders are **pixel-identical** to my own Round 1 renders of sha `61456978…` (PIL difference bbox = None), and the leaf text is identical (same md5). The Round 1 leaf evidence stands |
| Proof method | Screen proof only. No physical photocopy |

## Round 1 findings: disposition

| # | Round 1 finding | What is printed now | Result |
|---|---|---|---|
| B-1 | "Two students… same work" | p2: "You climb the same stairs twice, once walking and once running. You do the same work against gravity both times, but running does it in less time." Same person, so the same mg and h | **Closed** ✓ |
| M-1 | Spring sentence reversed | p5: "Stretching the spring 0.150 m instead of compressing it stores the same energy…", which matches the example's compressed givens | **Closed** ✓ |
| m-1 | Conservation condition | p6: "…conserved only when friction and other outside pushes are negligible…", which agrees with p5 | Closed ✓ |
| m-2 | "more slowly" | p5/6: "reaches the bottom at a lower speed" | Closed ✓ |
| m-3 | Brakes do the work | p4: "friction from the road on the tires does negative work on the car… If that braking force stays the same…" The same-force condition is kept | Closed ✓ |
| m-4 | Fig 4.1 on the far side of a page turn | Fig 4.1 now heads p2, directly above "you need the two pictures in Figure 4.1" | Closed ✓ |
| m-5 | Note split the sentence | The sentence now ends before the note, and a lead-in follows it ("For a constant force, the work is" / "In symbols," / "For an object of mass m moving at speed v," / "For an object of mass m at height h," / "For a spring with spring constant k stretched or compressed a distance x,"). Every lead-in is correct | Closed ✓ |
| m-6 | NREL credit | p5: "The U.S. Department of Energy calls pumped storage 'the most dominant form of energy storage on the electric grid today.'" This matches dossier 4.3-j word for word. "National Renewable" no longer appears | Closed ✓ (the dossier's excerpt is a search-result excerpt; see m-7) |
| m-7 | Primary hosts blocked | Not rechecked; no proxy change was reported | **Open**, non-blocking |
| m-8 | Hairline grey on photocopies | Unchanged (affects all courses) | **Open**, non-blocking |
| n-2 | Bold-italic W | W is now upright everywhere (prose, displays, Example rows, P = W/t). p1 adds "Don't confuse W for work, a quantity, with W for the watt, the unit of power below." **Judged acceptable.** Every other quantity symbol in this reading (F, d, m, v, h, k, x) is already upright, so upright W is consistent. The p1 sentence addresses dossier A-11, and the student pages never put W (work) next to W (watt) in one expression. The pdffonts output confirms no italic face is left on the student PDF | Closed (alternative fix accepted) |
| n-3 | FBD scaling | Unchanged; Pass | — |
| n-4 | f vs fk | The Fig 4.1 label is f<sub>k</sub>, the Example 4.1 row reads "Friction f<sub>k</sub>, θ = 180°", and the key note says "f_k, as in the Unit 3 notes". Consistent | Closed ✓ |
| n-5 | Fig 4.5 lift path | Unchanged; optional | Left as is |
| n-6 | Solve step | Example 4.2 has a new row "Solve for F: F = 2.40 × 10⁵ J ÷ 48.0 m", then "5.00 × 10³ N, opposite the car's motion". I re-solved it: 5000 N ✓ | Closed ✓ |
| n-7 | Horsepower non sequitur | p3: "…you do no work on it and deliver no power to it… A car engine is the opposite case: it does a lot of work quickly, and its power is often given in horsepower, where one horsepower is about 746 W." The horsepower sentence is now connected and correct, and still says ≈ 746 W only | Closed ✓ |
| n-8 | Key reference level | Key p2, OYO 4.4: "Reference level at the bottom: PE_f = 0", then "ME_f = ½(60.0 kg)(7.0 m/s)² + 0 = 1470 J" → 4.1 × 10² J ✓ | Closed ✓ |

## New findings (Round 2)

| # | Page / item | Observation | Severity | Disposition |
|---|---|---|---|---|
| R2-1 | Key p1, Teacher Notes "Notation" | "(Italic was dropped because the container render sets it bold-italic, which reads like a vocabulary term.)" This is build-tooling detail on a teacher-facing page and tells Matt nothing he can act on | Nice-to-have | Designer, optional: cut the parenthesis and keep "W for work is set upright; the reading says once not to confuse it with the watt." |
| R2-2 | p1, p2 and p4 line breaks | "cos θ" never splits: θ is an inline picture that sits on the same line as "cos" in every rendered instance (p1 ×6, p2 ×3, refresher). Some breaks still fall right after "=" ("θ =" / "0°", p1; "(cos 30.0°) =" / "43.3 N", p2; "g =" / "9.8 m/s²", p4). These carried over from Round 1 and are readable | Nice-to-have | Designer, optional: non-breaking space after "=" in those runs |

## Content recheck

| Check | Result |
|---|---|
| Givens and answers | No given changed. My Round 1 solutions all still match the reading and the key (480/−360/0/+120 J; 217 J; 1764 J, 4.4 × 10² W, 4.5 × 10² W accepted; 2.40 × 10⁵ J, 5.00 × 10³ N opposite the motion; 116 J; 192 m; 4.50 J; 24 J; 7.9 m/s; 4.1 × 10² J) ✓ |
| Key | Sentence-level diff against Round 1: only the notation note, the f_k note, the OYO 4.4 reference-level lines, and the 4.3/4.4 labels, which moved with the reflow. The answers are unchanged. The key's vocabulary definitions still match the reading word for word ✓ |
| Student words | No Δ, η, Σ (U+03A3), "lost", "used up", "wasted", "efficiency", "%", "stopping distance", Fnet or 9.81 on pp. 1–6. ∑ (U+2211) appears 3 times ✓ |
| Figure adjacency | 4.1 p2 above its reference; 4.2 p2, opposite column to its reference; 4.3 p2; 4.4 p3, same page as its reference; 4.5 and 4.6 p4; 4.7 p5. No figure is a page turn away from its first reference ✓ |
| Clipped text | None on pp. 1–6 or key pp. 1–2 ✓ |
| Leaf | The reading still ends on p6 (even), and the leaf is p7/p8. The 10 bold terms keep their pages (work, joule p1; power p2; KE, work-energy theorem p3; GPE, spring constant, EPE p4; ME p5; law of conservation p6). Cover list = headings = labels = key (4.1–4.4). Simulated removal of p7/p8 leaves all reading content, including OYO 4.4 and the regenerative-braking connection on p6 ✓ |

## Mechanical audits

| Audit | Result |
|---|---|
| Fonts | Student: Archivo Bold, Regular and Narrow only, "OK — Archivo only" ✓. Key `--key`: "OK — Archivo and the key handwriting face only" ✓ |
| Ink | Student PASS, 6.80% toner at worst, widest solid band 0.00 in. Key PASS, 6.03% ✓ |
| Binding | Student, 8 pp, and key, 2 pp: hole zone clear, guides on the binding side, outline only ✓ |
| Codes | `validate_codes.py` OK; names unchanged ✓ |

---

# Round 3: revision adding "Putting It Together" (SHULL-CHG-0123)

Auditor | 2026-11-26 | Report only. Nothing outside `reports/` was edited.

## Verdict: FAIL (INCOMPLETE)

The fix is one phrase on the teacher key. The student PDF passes in full. The closer passes every
item of the Physics DECISIONS audit check, and the science is correct. A teacher note on key p1
still calls SHULL-CHG-0123 "record in progress", but that record is CONFIRMED in
`courses/physics/DECISIONS.md`. A settled rule is shown as unsettled on the filed key (QA check 10,
unresolved status). Once that phrase is corrected, I can sign off by checking key p1 alone.

## Version and coverage

| Item | Value |
|---|---|
| Commit | `e8f0b37` "SHULL-CHG-0123 (builder) and Physics U4 revision: Putting It Together closer…", on top of `b7ef299` (DECISIONS rule and workflow pointer) |
| Student PDF | 8 pp, sha256 `2c62330f8e02bb02499775fb4882ca232bb305db26debb152772803e2742f8dd` ✓ |
| Key PDF | 2 pp, sha256 `a79dbca81ed5e9528db10977822cc2d763877b3f51fb342b22be935929b61e8b` ✓ |
| Filed baseline | `/tmp/claude-0/-home-user/3da17e47-8c6d-54ca-81fc-464404b893fa/scratchpad/reg/phys_filed_30dd.pdf`. Its sha256 is `30dd0218…`, the Round 2 PASS edition |
| Identity check (my own) | Student pp. 1–5 and 7–8: the extracted text is identical **and** the 100 dpi grayscale pixels are identical to the filed PDF and to my Round 2 renders. Only p6 differs. Key p2: pixel-identical to Round 2. Key p1 differs only in the one added Teacher Notes paragraph (sentence diff, render bbox at the foot of the notes box) |
| Inspected fresh | Student p6 (full page plus a 150 dpi crop of Fig 4.8) and key p1. All other pages reuse the Round 2 evidence after the identity check above |
| Proof method | Screen proof only |
| Not checked | The commit also changes `templates/reading/build_reading_docx.py`, and its message says "Chem U6/U7 output unchanged". I did not verify that claim. It is outside this audit |

## SHULL-CHG-0123 audit check, item by item

| Check (DECISIONS "Unit readings: Putting It Together") | Evidence | Result |
|---|---|---|
| Placement: after the last numbered section, before the leaf and any blank back | p6 order: 4.4 text → OYO 4.4 → Regenerative braking Connection → PUTTING IT TOGETHER → Fig 4.8 → next-unit sentence. The leaf starts on p7. The reading still ends on p6 (even), so there is no blank back. The heading has no section code. In This Unit (p1) is unchanged | ✓ |
| Both routes, solved independently from the printed givens: same answer, same sig figs | Givens: ∑F = 120. − 90.0 = 30.0 N, m = 15.0 kg, from rest, d = 4.00 m. **Route A:** a = 30.0/15.0 = 2.00 m/s²; v² = 0 + 2(2.00)(4.00) = 16.0 m²/s²; v = 4.00 m/s. **Route B:** W_net = 120. J (Ex 4.1); v² = 2(120.)/15.0 = 16.0 m²/s²; v = 4.00 m/s. Both are 3 sf, and every given has 3 sf (g is not used). Units cancel in both. The sign convention is stated ("+ is the way it moves"). ∑F is U+2211. The text says "Both routes give 4.00 m/s" | ✓ |
| Second tool belongs to an earlier unit | ∑F = ma is `3.4` Net Force and Acceleration (map; U3 notes spec l.398). v² = v₀² + 2aΔx is `1.2` Acceleration & Kinematic Equations (map title; U1 notes spec equation list l.376; 1.2 problem givens v₀, a, Δx at l.175). The reading's labels "Unit 3 (3.4)" and "Unit 1 (1.2)" are correct | ✓ |
| The derivation claim | "For a constant force, the work-energy theorem follows from ∑F = ma combined with v² = v₀² + 2ad": ∑F·d = ma·d = ½m(v² − v₀²) ✓. "Time taken out" is correct because that kinematic equation has no t | ✓ |
| Chain titles match the map | Fig 4.8 reads "Motion in One Dimension; Motion in Two Dimensions", "Forces and Motion", "Work, Energy & Power", "Momentum & Impulse". These match the curriculum map exactly. `unit_titles()` in the figure script reads them from DECISIONS with a regex, so none is typed. The short heads (Kinematics, Forces, Energy, Momentum) follow the rule's own wording "U1/U2 kinematics → U3 forces → U4 energy → U5 momentum" | ✓ |
| Highlighted unit is the current one, with no fill | Unit 4 has a 2.0 pt box plus a 0.6 pt outer outline. Unit 5 is dashed (next). There is no fill | ✓ |
| Grayscale at print size | 150 dpi grayscale crop: every head, title, equation and link label is legible. The current and next units differ by line weight and dash, not hue. The titles are in label grey #55604F (6.62:1) | ✓ |
| Next-unit sentence | "When a force acts over a time instead of a distance, you get momentum and impulse (Unit 5)." It names the correct next unit by number, and its title words match the map ("Momentum & Impulse"). It is one sentence | ✓ (wording note R3-2) |
| No bold term, nothing untaught, no tear-off question | The bold spans on p6 are only the 4.4 vocabulary term and box/route labels; no new term. Every equation used (∑F = ma, v² = v₀² + 2ad, W_net = KE_f − KE_i, KE = ½mv²) is taught in U1, U3 or U4. The tear-off p7/p8 is pixel-identical to Round 2, and no question draws on the closer | ✓ |

## Other requested checks

| Check | Result |
|---|---|
| Momentum/impulse exception | **Acceptable.** The ban is a spec-level build guard (`phys_u04_reading.json` "banned"), not a DECISIONS rule. The CONFIRMED SHULL-CHG-0123 rule *requires* the closer to name U5 and its map title and to show U5 in the chain. The builder scopes the `except` to the closer and to exactly one occurrence. A text scan of the student PDF finds "momentum" and "impulse" only in that sentence. Fig 4.8 carries "UNIT 5 · MOMENTUM", "Momentum & Impulse" and "F · t" as raster image text, which the guard does not scan. All three are required by, or follow from, the chain rule. Info: the builder's ban does not reach figure text, so figures need the visual check done here |
| d versus Δx note | U1 writes v² = v₀² + 2aΔx (U1 notes spec l.376; Δx throughout). The reading says "Unit 1 (1.2) then gives the final speed, with d for the displacement", which flags the substitution accurately and keeps Matt's no-Δ rule for student pages. v₀ matches U1's symbol ✓ |
| Notation and terms on student pages | No Δ, η or U+03A3 Σ; ∑ ×6. No "lost", "used up", "waste", "efficiency", "stopping distance", Fnet or 9.81 ✓ |
| Figure adjacency | Fig 4.8 sits directly below "Figure 4.8 shows how the units link together." ✓ |
| Clipped text | None on p6 or key p1 ✓ |
| Fonts | Student: "OK — Archivo only". Key `--key`: "OK — Archivo and the key handwriting face only" ✓ |
| Ink | Student PASS, 6.80% toner at worst (p6 5.33%), no fill. Key PASS, 6.52% ✓ |
| Binding | Student, 8 pp, and key, 2 pp: hole zone clear, guides on the binding side ✓ |
| Codes | `validate_codes.py` OK ✓ |
| Leaf | Unchanged and pixel-identical. Cover list = headings = labels = key (4.1–4.4). 10 terms on their Round 2 pages. The leaf is p7/p8. Removing p7/p8 leaves p6, including the closer, in the packet ✓ |

## Findings (Round 3)

| # | Page / item | Claim | Independent evidence | Severity | Disposition |
|---|---|---|---|---|---|
| R3-1 | Key p1, Teacher Notes, "Putting It Together (Matt, 2026-11-26; record in progress)" | The record's status | SHULL-CHG-0123 is CONFIRMED in `courses/physics/DECISIONS.md` ("Unit readings: Putting It Together", decision log 2026-11-26) and implemented in `b7ef299`. The key shows a settled rule as unsettled | Should-fix (fails QA check 10). **Makes the edition INCOMPLETE** | Designer: replace "record in progress" with "SHULL-CHG-0123". Recheck key p1 only |
| R3-2 | p6, last sentence | "…you get momentum and impulse (Unit 5)." | Loose. A force acting over a time gives an impulse, which changes momentum; a force does not "get" momentum. It is acceptable as a pointer, and fixing it would add U5 content | Nice-to-have | Optional, e.g. "When a force acts over a time instead of a distance, it leads to Unit 5, Momentum & Impulse." |
| R3-3 | p6, Route B | "So v = 4.00 m/s" | The speed has no direction, though Route A says "along the motion". The question asks "How fast", so speed is correct | Nice-to-have | Optional "along the motion" |
| m-7, m-8 | — | Primary sources blocked; hairline grey on photocopies | Unchanged | Open, non-blocking | As before |
