# Chemistry U3 content verification — 2026-10-26

**Scope:** short U3 per SHULL-CHG-0054 (3.1, 3.2, 3.3, 3.4, 3.6, 3.7; 3.5 retired).
**Mode:** report only. Nothing was edited. Every finding here is a recommendation for the `secretary`.
None of the findings conflicts with a LOCKED entry.

**Sources read**
- `templates/slide/decks/chem_u03_s03.4-s03.7_trends_ions.json` + rendered PDF (slides 8, 16–19 inspected visually)
- `scripts/build_diagram_trends.py`
- `templates/worksheet/specs/chem_u03_s03.4-s03.7_trends_ions.json`
- `templates/activity/specs/chem_u03_operation_periodic_table.json` + `templates/activity/build_operation_periodic_table.py`
- `templates/activity/specs/chem_u03_quiz.json`
- `courses/chemistry/DECISIONS.md` (U3 curriculum map, Assessment shape, Practice progression, 2026-10-26 log entry)

**Method.** I re-solved every ranking and every arithmetic claim. I checked each card value against standard
reference values (CRC melting points and IEs, Pauling/Allred EN, and the Clementi 1967 calculated radii).
Where I could not confirm a source online, the verdict says **UNVERIFIED** rather than guessing.

---

## Findings (blocking first, then by fix time)

| # | Item | Location | Claim | Verdict | Correct value / source | Severity | Recommendation |
|---|---|---|---|---|---|---|---|
| 1 | Lowest IE in group 1 | Practice set, 3.6 multi-topic (4 pt) solution + finalAnswer | "the lowest is at the bottom: francium (or cesium, the lowest that is actually measured well)"; finalAnswer "francium (accept cesium)" | **WRONG** | Cesium has the lowest first IE (375.7 kJ/mol, 3.894 eV). Francium's IE has been measured precisely: 4.0727 eV, about 393 kJ/mol, which is *higher* than Cs (a relativistic effect). NIST Handbook of Basic Atomic Spectroscopic Data; Andreev et al., PRL 59, 1274 (1987). It also contradicts deck slide 8 ("Black is cesium (loosest)"). | **Blocking** (wrong key) | Make cesium the key answer. Keep "accept francium" as a full-credit *trend prediction*, since the prompt asks what you "expect". Change the note to: "Real data: Fr (393) is slightly above Cs (376), so Cs is actually lowest." Delete "measured well". |
| 2 | Group 14 EN values / "Real data" | OPT card Xi (Pb 2.33), card Theta (Sn 1.96); key "WHERE THE DATA BREAKS THE TREND" | Group 14 EN "goes 2.55, 1.90, (2.01), 1.96, 2.33. Real data." | **MISLEADING** (numbers are real but depend on oxidation state) | 2.33 is the Allred (1961) Pauling-scale value for **Pb(IV)** and 1.96 is for **Sn(IV)**. The Pb(II)/Sn(II) values are listed around 1.87/1.80. Many school tables print Pb 1.8–2.3 and Sn 1.8–2.0. The Pb card says "2+ (4+ is rare)" but carries the 4+ EN, so the card is inconsistent with itself. A student comparing the card to the reference-packet table may see a different number. | Medium | Keep the values, since they make good discussion. Add to the key: "2.33 and 1.96 are the values for the 4+ state; tables differ for Pb and Sn." Optionally cross-check the reference-packet periodic table so the teacher knows what students will see. |
| 3 | Noble gas EN "Not measured" | OPT cards Beta (Ar), Eta (Kr), Mu (Ne), Nu (Xe), Chi (He); spec `sources` line | EN "Not measured" | **INACCURATE for Kr and Xe**; acceptable for He, Ne, Ar | Pauling-scale values exist for Xe (≈2.6, from xenon compounds) and, per the Allred 1961 tabulation, Kr (3.00; this Kr figure is **UNVERIFIED** in this session). He, Ne and Ar have no value. The practice set's wording ("usually left off … because they rarely bond") is correct. | Medium (quick fix) | Change all five cards to "No value (rarely bonds)" or "Not listed". That keeps the clue and stays true for every noble gas. |
| 4 | Carbon "Does not melt" | OPT card Epsilon (C), melting point field | "Does not melt; turns to gas at 3642 °C" | **MISLEADING (absolute claim)**; source **UNVERIFIED** | At 1 atm graphite sublimes and does not melt, but carbon does melt above about 100 atm (triple point near 4,500 °C). 3642 °C (3915 K) matches the Wikipedia infobox. I could not confirm it as the CRC entry, yet the `sources` line says melting points are CRC values. | Low–Medium (quick fix) | Reword to "Does not melt at normal pressure; turns to gas at about 3640 °C". This matches the He card's wording. Either cite the value's real source or verify it against the CRC edition in use. |
| 5 | Placement is underdetermined (inference) | OPT student handout "FOUR ROUNDS" + scoring (1 pt per exact cell) | Round 3: line up rows "so atoms shrink from left to right along each row … One row has a gap." | **INFERENCE: puzzle may have more than one valid answer** | I re-ran the rule on the card radii. Shifting group 18 down one row (He with F, …, Xe with Cs), or putting the gap at the bottom of group 14 (Sn in row 4, Pb in row 5), still gives radii that shrink across every row, and IE still rises across every row. The stated rule therefore does not force the answer grid. A team can solve it by matching nearest radii (F 42/Ne 38, Cl 79/Ar 71, Br 94/Kr 88, I 115/Xe 108), but nothing in the instructions tells them to. Mendeleev ordered by atomic mass, and the cards carry no mass. | Medium | Pick one: (a) add atomic mass (or atomic number) to each card, which fits the Mendeleev story; (b) add a hint such as "neighbors in a row have similar sizes" or "the noble gas row starts one row higher"; (c) tell the teacher to accept a consistent shifted alignment. Note: this is my reasoning about the puzzle, not an observed student outcome. |
| 6 | Practice progression | Practice set, all three sections | 2 warm-up, 2 practice, 1 challenge, 1 multi-topic per section | **DOES NOT MATCH DECISIONS.md** | DECISIONS.md "Practice progression" asks for 2–4 easy, **3–4 medium**, 1–2 difficult, 1 connection. Each section has only 2 medium items. | Medium | Add 1–2 medium items per section, or have Matt confirm that a one-page-per-section practice set is an allowed exception. Do not treat this as settled without his answer. |
| 7 | Quiz version parity, item "size" | Quiz A Q6 vs B Q6 / C Q5 | A: Ca vs Ca2+ (cation). B: Cl vs Cl−. C: Br vs Br− (anions) | **NOT FULLY PARALLEL** | DECISIONS.md: versions have the "same skills and rigor with numbers/order changed". The cation case (outer level emptied) and the anion case (added repulsion) are different reasoning. | Low–Medium | Use the same ion type in all three versions, either all anions or all cations (e.g. A: Mg/Mg2+ or K/K+ to match). Or accept the mix knowingly. |
| 8 | Answers on the question slide | Deck slide 19 "Check Yourself" (rendered PDF p. 19) | Must-write bar reads "Answers: K < Ca < Br. Li+, O2−, Al3+." on the same slide as the questions | **PEDAGOGY**: the answers are visible during the 2-minute check | Values are correct: K 0.82 < Ca 1.00 < Br 2.96; Li+, O2−, Al3+. | Low | Move the answers to a following slide, or make the must-write a prompt. Also observed: the dark "PREDICT THE ION" card runs past the right margin of the slide (layout; for the designer, not a content issue). |
| 9 | "Tightest" corner | Deck slide 8, annotation a3 | "Green is fluorine (tightest)." | **IMPRECISE** | F has the highest EN. The highest IE belongs to He (2372), then Ne (2081), both above F (1681). The slide covers "three trends" including IE. | Low | "Green is fluorine (strongest pull on shared electrons; noble gases aside)". Or just say "highest electronegativity". |
| 10 | Section range spans the retired code | OPT header/footer code, built as `U03 / S3.1–S3.7` | Range S3.1–S3.7 | **AMBIGUOUS** | The range reads as if it includes 3.5, which DECISIONS.md says is retired and never reused. | Low | Use "S3.1–S3.4, S3.6–S3.7", or have the standards side rule that a range never implies retired codes. A naming question for the secretary, not a content error. |
| 11 | Quiz `sectionLabel` | Quiz A/B/C family item | "3.1–S3.2" | **FORMAT INCONSISTENCY** (rendered output not inspected) | The first code lacks the "S" that the second code has. | Low | Make it "S3.1–S3.2", or confirm the renderer adds the prefix. |
| 12 | Carbon appearance | OPT card Epsilon | "Black, brittle solid" | **QUESTIONABLE** | Graphite is soft and slippery, not usually called brittle. "Brittle" is the textbook nonmetal descriptor. | Low | "Black, soft, flaky solid", or "Black solid". |

---

## Verified correct (no action)

| Area | What was checked | Result |
|---|---|---|
| OPT, melting points (22 numeric cards + Ge) | Na 98, Ar −189, Br −7, Be 1287, Mg 650, Kr −157, Sn 232, Ba 727, Rb 39, Sr 777, Ne −249, Xe −112, Pb 327, F −220, Li 181, K 64, Cl −102, Si 1414, Cs 28, I 114, Ca 842, Ge 938 | All match CRC values, rounded. He "does not freeze at normal pressure" is correct (He needs about 25 atm to solidify). |
| OPT, first IE (23 + Ge) | Every value checked against the standard tables, e.g. Be 899.5→900, Pb 715.6, Sn 708.6, Ge 762.2 | All correct. **Pb 716 > Sn 709 is real** (lanthanide/relativistic effect), so the key's claim is accurate. |
| OPT, Pauling EN (non-noble) | Na .93, Br 2.96, Be 1.57, C 2.55, Mg 1.31, Ba .89, Rb .82, Sr .95, F 3.98, Li .98, K .82, Cl 3.16, Si 1.90, Cs .79, I 2.66, Ca 1.00, Ge 2.01 | All correct. For Sn and Pb, see #2. |
| OPT, radii vs Clementi 1967 | Li 167, Be 112, C 67, Ne 38, F 42, Na 190, Mg 145, Si 111, Cl 79, Ar 71, K 243, Ca 194, Ge 125, Br 94, Kr 88, Rb 265, Sr 219, Sn 145, I 115, Xe 108, Cs 298, Ba 253, Pb 154, He 31 | All 24 match the Clementi calculated set. The `sources` claim holds. |
| OPT, ions and appearances | 1+, 2+, 1−, Sn "2+ or 4+", Pb "2+ (4+ rare)", C/Si "shares electrons", noble gases "almost never reacts" | Correct at HS level. Appearances are fine apart from #12. |
| OPT, key arithmetic | (787+709)/2 = 748; 762−748 = 14. Ranges contain the actuals (mp 800–1080 ∋ 938; r 115–135 ∋ 125; IE 700–825 ∋ 762; EN 1.8–2.2 ∋ 2.01). Neighbor averages fall in range (mp 823, r 128, EN 1.93). Score 23+1+4 = 28 matches "/ 28". 23 cards + 1 gap card = 24 slots. | All correct. |
| OPT, key trend-break notes | Group 2 mp sequence (1287, 650, 842, 777, 727); Sn/Pb separated from group 2 by higher EN and lower mp; radius orders group 14 correctly (67<111<125<145<154) | Correct. |
| OPT, history | Mendeleev predicted eka-silicon 1871; Winkler discovered germanium 1886 and named it; gap below silicon | Correct. |
| OPT, row check | Radii shrink across every row of the answer grid (P2: 167>112>67>42>38 … P6: 298>253>154) | The answer grid does satisfy the rule (but see #5). |
| Quiz A | Ca → alkaline earth metal; Mg<Na<K; N(3.0)>P(2.2); Cl 1251 vs Na 496, 17 vs 11 p; Sr2+, Br−, Al3+; Ca 197 pm / Ca2+ 100 pm | All correct. |
| Quiz B | Cl<S<Se; Cl → halogen, nonmetal; Cl(3.2)>I(2.7); K+, S2−, N3−; F 1681 vs Li 520, 9 vs 3 p; Cl 99 / Cl− 181 pm | All correct. |
| Quiz C | Rb → alkali metal; O(3.4)>S(2.6); Be<Li<Na; S 1000 vs Mg 738, 16 vs 12 p; Br 114 / Br− 196 pm, 35 p; Rb+, Se2−, P3− | All correct. |
| Quiz shape | 6 items, 3 versions, 15 points each, same blueprint shuffled; no 3.5 content | Fits DECISIONS.md Quizzes shape and the U3 exception. |
| Practice set 3.4 | F 4.0; Na<Mg<P<Cl (0.93, 1.31, 2.19, 3.16); Cs<K<Li (376, 419, 520); Se 2.55 < 2.6 | Correct. |
| Practice set 3.6 | Na 11→Ar 18; Li 2, Na 3, K 4 levels; Mg 160 / S 103 pm (labeled "values vary"); Cs 376 / Li 520; K 419 / Na 496 | Correct, except the francium claim (#1). |
| Practice set 3.7 | Group charges; Al3+, O2−, N3−, Sr2+; Mg 160→Mg2+ 72, F 64→F− 133; Mg2+ (72) < Na+ (102) < F− (133); Na IE 496, EN 0.93 | Correct. F 64 pm is one of several published covalent values, and the answer is labeled as a reference value. |
| Deck | EN Li 1.0, C 2.6, F 4.0; group 17 F 4.0, Cl 3.2, Br 3.0, I 2.7; Na/Cl 6 more protons; Mg 3 vs Ba 6 levels, Mg higher IE; Ca2+/S2− sizes; K<Ca<Br; "Group 14 … That is Unit 4" (U4 Chemical Bonding, per DECISIONS.md) | Correct. |
| Deck figures | Trend grid: F at period 2, group 17 (Lab Lime Deep #4D730E, green ✓); Cs at period 6, group 1. Ion circles: same scale factor for all four; rendered ratios Na+/Na ≈ 0.55 (102/186 = 0.548), Cl−/Cl ≈ 1.9 (181/99 = 1.83) | Correct and to scale. Na is metallic and Cl covalent, as the script header states. |
| Cross-document radii | Na 186 (deck) vs 190 (card); Mg 160 (practice) vs 145 (card); Ca 197 (quiz) vs 194 (card) | The differences are deliberate source differences, and each document labels its source. No action. |
| Curricular fit | Sections used are 3.1–3.4, 3.6, 3.7, all present in DECISIONS.md; quiz replaces the test per the U3 exception; 45-min activity fits a 50-min period minus 5-min cleanup | Fits, apart from #6 and #10. |

## Recurring pattern worth naming

- **Edge-case claims written as absolutes.** Three times: "Does not melt" (C), "Not measured" (Kr/Xe), and
  "francium lowest". Each time a rule-of-thumb was stated as fact at the edge of the table, where real data
  breaks the trend. The materials already handle exceptions well elsewhere (Pb vs Sn IE, group 2 mp).
  Recommended habit: check any "always/never/lowest/not measured" claim about an element at the edge of a
  trend against data before it ships.

## Sources consulted

- NIST Handbook of Basic Atomic Spectroscopic Data, francium table (Fr IE 4.072741 eV): https://physics.nist.gov/PhysRefData/Handbook/Tables/franciumtable1.htm
- Andreev et al., Phys. Rev. Lett. 59, 1274 (1987), Fr ionization potential: https://link.aps.org/doi/10.1103/PhysRevLett.59.1274
- Lenntech, elements by ionization energy (Fr 4.0727 eV, Cs 3.8939 eV): https://www.lenntech.com/periodic-chart-elements/ionization-energy.htm
- Wikipedia, Carbon (sublimation 3915 K / 3642 °C): https://en.wikipedia.org/wiki/Carbon
- KnowledgeDoor, Allred electronegativity (Pb(IV) 2.33, Sn(IV) 1.96, Allred 1961): https://knowledgedoor.com/2/elements_handbook/allred_electronegativity.html
- KnowledgeDoor, Pauling electronegativity (Pb(II) 1.87, Sn(II) 1.80): https://knowledgedoor.com/2/elements_handbook/pauling_electronegativity.html
- Chemistry-online EN table (Xe 2.6): https://www.chemistry-online.com/generalities/electronegativity-table/
- Melting points, IEs, other Pauling values and Clementi radii were checked against standard reference values
  from memory (CRC Handbook / Clementi, Raimondi & Reinhardt, J. Chem. Phys. 47, 1300 (1967)). The direct
  fetches to Wikipedia and NIST failed in this session (DNS), so the Kr 3.00 EN and the CRC carbon entry are
  marked UNVERIFIED above.
