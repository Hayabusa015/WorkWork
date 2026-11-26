# Physics U4 Unit Reading: Source Dossier (four sections)

Prepared by: researcher | Date: 2026-11-26 | Workflow: `workflows/unit-textbook.md`, "Commission the chapter" step 2
Status: REPORT ONLY. Nothing outside `reports/` was edited.

**Scope.** U4 Work, Energy & Power has four sections (`courses/physics/DECISIONS.md` l.38–40): 4.1 Work & Power · 4.2 Kinetic Energy & Work-Energy Theorem · 4.3 Potential Energy (Gravitational & Elastic) · 4.4 Conservation of Energy. This is the first Physics unit reading. `templates/reading/specs/` holds Chemistry specs only.

**Inputs.**
- The Overseer outline and Matt's decisions of 2026-11-26, both as relayed in the commission.
- DECISIONS l.38–40, 102–129 (build rules), 137–149 (no work areas), 250–264 (short titles), 313–329 (θ, ∑F) and 344–350 (g = 9.8).
- `templates/notes/specs/phys_u03_s03.1-s03.6_notes_student.json`.
- `templates/notes/specs/phys_u02_s02.1-s02.3_notes_key.json`.
- `templates/notes/specs/phys_u01_s01.1-s01.4.json`.
- `governance/proposals/SHULL-CHG-0095-physics-oq2-trig-evidence.md`.

I re-solved every number below from the givens. None was copied from the outline without checking.

**Network limitation (read this first).** WebFetch failed with `ENOTFOUND` for `openstax.org`, `www.bipm.org`, `www.nist.gov` and `phys.libretexts.org`. After the fourth failure I stopped trying hosts, as the tool instructs. WebSearch worked. Each external locator below is marked with one of three tags:
- **(S)**: a search-result excerpt from the named page;
- **(K)**: a value I know but could not retrieve this session;
- **(R)**: a repository file, with its line number.

Nothing marked (K) is verified until someone opens the locator. To open the primary pages directly, the session must allow `openstax.org`, `www.bipm.org`, `www.nist.gov`, `www.energy.gov`, `afdc.energy.gov`, `www.nhtsa.gov` and `www.mlb.com`. **Pattern:** primary hosts have now been blocked in three consecutive dossiers (Chem U7 on 2026-11-24, Chem U6 on 2026-11-25, Phys U4 today). See chem U6 dossier A-15. The allow-list proposal is still worth making.

**Status codes** (same as `reports/chem_u06_reading_dossier.md`):
- **SRC**: sourced, with a locator and an excerpt or data.
- **DER**: derived by arithmetic from sourced inputs; the working is shown.
- **ILL**: illustrative (an invented scenario with checked physics).
- **SEC**: secondary sources only.
- **UNVERIFIED**: I could not find a source. Do not print it as fact.

---

## A. Findings (blocking first, then by fix time)

| # | Item | Finding | Evidence | Severity | Recommendation |
|---|---|---|---|---|---|
| A-1 | 4.2 Connection and tear-off: braking distance and the NHTSA wording | **NHTSA's brochure says "stopping distance quadruples" when speed doubles. As physics, that is wrong for total stopping distance.** Stopping distance = reaction distance (∝ v) + braking distance (∝ v²). Only **braking** distance quadruples, and only if the braking force stays the same. Worked check, v = 20.0 m/s and a = 4.17 m/s²: braking distance 48.0 m → 192 m when v doubles (×4). With a 1.5 s reaction time the reaction distance is 30.0 m → 60.0 m, so the total goes 78.0 m → 252 m (×3.2, not ×4) | NHTSA "Speeding" brochure DOT HS 812 008 (PRINT-072015): "every time your speed doubles, your stopping distance quadruples" (S, mirror at ca1.uscourts.gov). A Navy citation of NHTSA gives 221 ft at 50 mph and 292 ft at 60 mph (S). Brake (UK): braking distance "proportional to the square of the initial speed" (S, SEC). DER below | **Blocking (accuracy of a printed claim and the tear-off answer)** | Print **"braking distance"**, never "stopping distance". Add the condition: "if the brakes supply the same force". Do not quote NHTSA's sentence. Cite NHTSA only for the general point that speed raises crash risk, or cite no agency and present the claim as a consequence of KE ∝ v² (DER). Tear-off wording: "...about how much farther does it skid while braking?" |
| A-2 | 4.4 On Your Own wording: "ME lost" | DECISIONS lists "energy is 'used up' rather than transferred" as a misconception to write against (l.126–128). Matt's convention is "energy transferred, not used up". "ME lost ≈ 4.1 × 10² J" and "energy lost to friction" undercut both | DECISIONS l.126–128 (R) | **Blocking (house rule on a student page)** | Ask for "how much mechanical energy was **transformed into thermal energy**". Key: "ME decreased by 4.1 × 10² J. That energy did not disappear; it became thermal energy in the board, wheels and ramp." Apply the same rule to every "lost/wasted" phrase, including the regenerative-braking connection (A-14). |
| A-3 | 4.4 Example: "3.20 m frictionless ramp" | **Ambiguous.** v = √(2gh) needs the **vertical drop**, not the ramp's length. A reader who takes 3.20 m as the length along the slope cannot get 7.9 m/s without an angle | DER §B 4.4 | **Blocking (the problem is unsolvable as worded if misread)** | "...starts from rest at the top of a frictionless ramp **3.20 m high** (vertical height)." The figure labels h as a vertical bracket. |
| A-4 | 4.1 On Your Own: rounding trap in P | W = mgh = 60.0 × 9.8 × 3.00 = **1764 J → 1.8 × 10³ J**. Using the unrounded value, P = 1764 / 4.00 = **441 W → 4.4 × 10² W** ✓. If a student divides the rounded W instead, they get 1.8 × 10³ / 4.00 = 450 → **4.5 × 10² W** | DER §B 4.1 | **Major (key accuracy)** | Key: "carry 1764 J into the next step; round only at the end". Accept 4.5 × 10² W with a note. The worked Example should model carrying an unrounded value, so the habit is taught before it is tested. |
| A-5 | FBD rule versus showing displacement (4.1 Example, angled pull) | DECISIONS: one arrow per force and "**no arrow for 'motion'**" (l.113–116). Work needs the displacement d and, for cos θ, the angle between F and d. If d is drawn as an arrow on the FBD, it reads as a motion arrow | DECISIONS l.113–116 (R) | **Major** | Draw two figures: (1) the FBD with Fpush, f, FN and Fg only, arrows scaled (120 > 90.0; FN = Fg); (2) a separate scene sketch with d shown as a labelled dimension bracket under the box, **not** on the FBD. Angled pull: mark θ between F and the horizontal (the direction of d) on the scene sketch. If the designer wants d as an arrow anywhere, that is Matt's call. |
| A-6 | Vector rule: braking force | DECISIONS: "Any vector quantity gets a direction, always" (l.104–105). "Braking force 5.00 × 10³ N" alone is incomplete | DECISIONS l.104–105 (R) | Major | "5.00 × 10³ N, opposite the car's motion". Work, KE, PE, ME and P are scalars, so no direction is needed; say so once in 4.1 ("work is a scalar, but it can be positive or negative"). |
| A-7 | Sig figs in givens: "120 N" (4.1) and "1200 kg" (4.2) | Both are ambiguous: 2 or 3 sig figs. The outline's answers (480 J, +120 J, 2.40 × 10⁵ J) assume 3. Physics already uses the trailing-decimal convention: "40. m" (U1 notes l.91), and the outline itself has "k = 400. N/m" | U1 notes l.91 (R) | Major (sig figs are enforced from U0, DECISIONS l.85) | Write **120. N** and **1200. kg** (or 1.20 × 10³ kg), and report W_net as **+120. J** (or 1.20 × 10² J). |
| A-8 | 4.1 On Your Own: "work done by the student" | Strictly, the stair's normal force does no work on the student, because its point of contact does not move. The student's own muscles convert chemical energy. mgh is the work done **against gravity**, and it equals the PE gain only at steady speed (no KE change) | OpenStax 7.7 treats the same scenario as KE + PE gained (S) | Minor (teacher note) | Student wording: "How much energy does the student transfer to gravitational potential energy?" or "how much work is done against gravity", plus "at a steady pace". Key note on the muscle subtlety. |
| A-9 | 4.1 On Your Own resembles OpenStax Example | OpenStax College Physics 7.7 (2e) uses a 60.0 kg woman, 3.00 m of stairs and 3.50 s; its PE term is the same 1764 J, and its answer is 538 W with KE included | OpenStax 7.7 Power (S) | Info | It is not a rights problem (OpenStax is CC BY, and these are numbers). For originality, consider changing a given (e.g. 55.0 kg, or 4.50 m in 6.00 s). If kept, the key should not cite the OpenStax answer, which includes KE. |
| A-10 | 4.4 On Your Own: sig figs in a subtraction | Using the house rule (answers that depend on g → 2 sf, l.345–346): 1881.6 − 1470 = 411.6 → **4.1 × 10² J** ✓. A strict subtraction rule on 2-sf values (1.9 × 10³ − 1.5 × 10³) gives **4 × 10² J** | DER §B 4.4 | Minor | Key: report 4.1 × 10² J from unrounded intermediates and accept 4 × 10² J. Do not make students arbitrate this. |
| A-11 | W (work) versus W (watt) | The italic symbol W (work) and the roman unit W (watt) share a letter, as in "P = W/t = 441 W". Weight is Fg in U3 (notes l.12), so weight is not a third collision | U3 notes l.12 (R) | Minor | Add one sentence in 4.1: "Do not confuse W for work (a quantity) with W for watt (a unit)." Set the quantity W in italic. |
| A-12 | Hooke's law sign | The outline says "F = kx (restoring)". OpenStax 16.1 writes **F = −kx**. OpenStax AP 5.3 writes the magnitude form F = kΔL. Both are sourced | §C 4.3-d | Minor | Print **F = kx** as a magnitude plus the words "the spring force points opposite the stretch or compression". This avoids a sign students cannot yet use. Key note: "advanced texts write F = −kx". |
| A-13 | "Spring constant" versus OpenStax "force constant" | OpenStax 16.1 calls k the "force constant" (S). "Spring constant" is the usual high-school term | §C 4.3-d | Info | Keep "spring constant" as the bold term. Key note on the other name. |
| A-14 | Regenerative braking wording | AFDC: the motor "converts otherwise wasted energy from braking into electricity and stores it in the battery" (S). "Wasted" clashes with A-2 | §C 4.4-g | Minor | Write: "Ordinary brakes turn the car's KE into thermal energy in the brake pads. Regenerative braking runs the motor as a generator, so part of the KE becomes electrical energy stored in the battery." No percentage. |
| A-15 | Pumped storage: numbers and efficiency | DOE calls pumped storage "the most dominant form of energy storage on the electric grid" (S). No search result gave a US-share percentage. The plant is a net consumer of electricity: it returns less than it used for pumping (S, SEC) | §C 4.3-j | Minor | Keep it qualitative; print no percentage. If a reason is needed for why it returns less, say "some energy becomes thermal energy in the pumps, turbines and pipes", not "is lost". This is consistent with Matt's no-efficiency call in 4.1. |
| A-16 | Short title "Work & Energy" not yet recorded | Matt chose it on 2026-11-26. DECISIONS' Short titles table has no U4 row (l.256–264), and filenames get no topic without a row (l.253–254). It is 13 characters, within the 20-character limit | DECISIONS l.250–264 (R) | Minor (process) | The Secretary adds row `U4 · Work & Energy` against an approved ID before filing. |
| A-17 | On Your Own work space | Matt's exception for this reading. The no-work-area rule names "practice sets, homework worksheets, and study guides" (l.139–141). A unit reading is not named, so this is a clarification as much as an exception | DECISIONS l.139–149 (R) | Info (process) | Record it in the decision log, scoped to this reading and **not a precedent**, matching the format of the 3.1 lab entry (l.276–311). |
| A-18 | Trig: W = Fd cos θ and open question 2 | Open question 2 (algebra-only or trig) is still open. SHULL-CHG-0095 is PENDING. Built U2/U3 material already uses Fx = F cos θ (U3 notes l.25) and Ax = A cos θ (U2 key l.203) | (R) | Info | No conflict with Matt's 2026-11-26 decision. Using cos θ in one case is consistent with built material. Do not cite this reading as resolving open question 2. |
| A-19 | Notation: no Δ, but U1 used Δx and Δt | U1 notes use Δx and Δt (l.92, 317). This reading writes KE_f − KE_i and PE_f − PE_i by Matt's choice. That is consistent inside the reading | (R) | Info | Use the f/i form everywhere, including PE_g in 4.3 (PE_g,f − PE_g,i). Never mix forms on one page. |

---

## B. Calculations re-solved (DER)

g = 9.8 m/s² throughout (DECISIONS l.344–350). Answers that use g are given to 2 sf.

| Item | Working | Result | Matches outline? |
|---|---|---|---|
| 4.1 Example: push | W = Fd cos 0° = (120. N)(4.00 m)(1) | **+480. J** | ✓ |
| 4.1 Example: friction | W = (90.0 N)(4.00 m)(cos 180°) = (90.0)(4.00)(−1) | **−360. J** | ✓ |
| 4.1 Example: FN, Fg | cos 90° = 0 | **0 J** each | ✓ |
| 4.1 Example: net | 480. + (−360.) + 0 + 0 | **+120. J** | ✓. Cross-check: ∑F = 120. − 90.0 = 30.0 N; (30.0 N)(4.00 m) = 120. J ✓. This is a good link to 3.4 |
| 4.1 Angled pull (proposed) | W = Fd cos θ = (50.0 N)(5.00 m)(cos 30.0°) = 250. × 0.8660 = 216.5 | **217 J** (3 sf) | New. Only the horizontal component F cos θ = 43.3 N does work; the vertical component (25.0 N) does none. **Ask only for the pull's work.** An upward pull also lowers FN and so changes friction (U3 notes l.436, "FN here is less than mg"), so leave friction out of this case or this becomes a 3.5 problem |
| 4.1 Unit check | N·m = J; J/s = W; J = kg·m²/s² | ✓ | |
| 4.1 On Your Own | W = mgh = (60.0 kg)(9.8 m/s²)(3.00 m) = 1764 J; P = 1764 J / 4.00 s = 441 W | **1.8 × 10³ J; 4.4 × 10² W** | ✓ (see A-4) |
| 4.1 Horsepower (optional) | 441 W ÷ 745.7 W/hp = 0.591 | ≈ 0.59 hp | Not required. Matt allowed one sentence only |
| 4.2 Example: KE_i | ½(1200. kg)(20.0 m/s)² = 600 × 400. | **2.40 × 10⁵ J** | ✓ |
| 4.2 Example: force | W_net = KE_f − KE_i = 0 − 2.40 × 10⁵ J. W_net = F d cos 180° → F = 2.40 × 10⁵ J / 48.0 m | **5.00 × 10³ N, opposite the motion** | ✓. Plausibility: a = 5000/1200 = 4.17 m/s² (0.43 g), a firm but ordinary stop; v²/(2d) = 400/96.0 = 4.17 ✓. 20.0 m/s ≈ 44.7 mph |
| 4.2 Braking distance ∝ v² | Constant F: F d = ½mv² → d = mv²/(2F). 2v → 4d. 48.0 m → 192 m | ×4 for braking distance only (A-1) | DER |
| 4.2 On Your Own | KE = ½(0.145 kg)(40.0 m/s)² = 0.0725 × 1600 = 116 J; W_net = 116 J − 0 | **116 J** | ✓. 40.0 m/s ≈ 89.5 mph, a plausible pitch. Wording: "net work on the ball" (gravity and air are ignored) |
| 4.2 Doubling v | KE ∝ v²: (2v)² = 4v² | ×4 | DER |
| 4.3 Example | PE_s = ½(400. N/m)(0.150 m)² = 200. × 0.0225 | **4.50 J** | ✓. Triangle check: F = kx = 60.0 N; area = ½(0.150 m)(60.0 N) = 4.50 J ✓. This is the F-x graph-area skill in DECISIONS l.119–120 |
| 4.3 On Your Own | PE_g,f − PE_g,i = mg(h_f − h_i) = (2.00)(9.8)(2.00 − 0.80) = 19.6 × 1.20 = 23.52 J. Reference check: 39.2 J − 15.68 J = 23.52 J | **24 J** | ✓. The reference level cancels |
| 4.3 Path independence via 3.3 | Ramp of length L at θ: work against gravity = (mg sin θ)(L), and L sin θ = h, so the work is mgh | Same as lifting straight up | DER. Supports the 4.3 tear-off (frictionless case) |
| 4.4 Example | mgh = ½mv² → v = √(2gh) = √(2 × 9.8 × 3.20) = √62.72 = 7.920 | **7.9 m/s**; m cancels | ✓ (h is the vertical height, A-3) |
| 4.4 On Your Own | ME_i = (60.0)(9.8)(3.20) = 1881.6 J. KE_f = ½(60.0)(7.0)² = 30.0 × 49 = 1470 J. Difference = 411.6 J | **4.1 × 10² J** transformed to thermal energy | ✓ arithmetic (1882 vs 1470 confirmed). Wording per A-2, sig figs per A-10. Fraction: 411.6/1881.6 = 21.9% (not needed) |

---

## C. Source dossier: every factual claim in the outline

### 4.1 Work & Power

| ID | Claim | Value / excerpt | Source (title, edition/date) | Locator | Status |
|---|---|---|---|---|---|
| 4.1-a | Work = energy transferred by a force through a displacement | 1e summary: "Work is the transfer of energy by a force acting on an object as it is displaced." | OpenStax *College Physics* 7.1 section summary (1e); 2e equivalent | openstax.org/books/college-physics/pages/7-section-summary | SRC (S) |
| 4.1-b | W = Fd cos θ; θ is the angle between F and d | 7.1 defines W = Fd cos θ (K for exact wording) | OpenStax *College Physics 2e* 7.1 | openstax.org/books/college-physics-2e/pages/7-1-work-the-scientific-definition | (K). Host blocked |
| 4.1-c | Zero work for a perpendicular force (or zero displacement) | 2e summary: "The work done by a force is zero if the displacement is either zero or perpendicular to the force." | OpenStax *College Physics 2e* ch. 7 summary | openstax.org/books/college-physics-2e/pages/7-section-summary | SRC (S) |
| 4.1-d | Negative work for an opposing force | 7.5: friction work is negative "because f is in the opposite direction of the motion (θ = 180°, cos θ = −1)" | OpenStax *College Physics 2e* 7.5 Nonconservative Forces | openstax.org/books/college-physics-2e/pages/7-5-nonconservative-forces | SRC (S). Teacher note: treating friction work as −fd is the standard textbook simplification. The resulting thermal energy is shared between box and floor; do not claim it all goes into the box |
| 4.1-e | 1 J = 1 N·m | Glossary: "joule: SI unit of work and energy, equal to one newton-meter"; 7.1: 1 J = 1 N·m = 1 kg·m²/s² | OpenStax *College Physics* ch. 7 glossary; BIPM *SI Brochure* 9th ed. (2019) Table 4 (K) | openstax.org/books/college-physics/pages/7-glossary; bipm.org/en/si-brochure-9 | SRC (S) for OpenStax; BIPM (K), host blocked. NIST SP 330 (2019) Table 4 lists "the 22 SI units with special names" (S) |
| 4.1-f | P = W/t; 1 W = 1 J/s | Glossary: "power: the rate at which work is done"; 7.7: "1 watt equals 1 joule/second" | OpenStax *College Physics 2e* 7.7 Power; BIPM Table 4 (K) | openstax.org/books/college-physics-2e/pages/7-7-power | SRC (S). P = W/t is **average** power; no need to say so on the student page |
| 4.1-g | Example: 120 N push / 90.0 N friction / 4.00 m | §B | — | — | ILL + DER |
| 4.1-h | Angled pull, 50.0 N at 30.0° over 5.00 m → 217 J | §B | — | — | ILL + DER (proposed) |
| 4.1-i | On Your Own: stairs | §B; compare OpenStax 7.7 (A-9) | — | — | ILL + DER |
| 4.1-j | Pushing a wall does no work (on the wall) | d = 0 → W = 0, by 4.1-c | as 4.1-c | — | SRC (S) + DER. Teacher note: you still tire, because muscles convert chemical energy to thermal energy. This supports "transferred, not used up" |
| 4.1-k | 1 hp ≈ 746 W (745.7 W) | NIST SP 811 Appendix B: horsepower (550 ft·lbf/s) = 7.456 999 E+02 W. Electric horsepower = 746 W exactly. Metric horsepower ≈ 735.5 W | NIST SP 811 (2008), App. B.8/B.9 | nist.gov/pml/special-publication-811 (blocked); value via R NISTunits docs, unitconverters.net 745.6998715823 W, Wikipedia "Horsepower" (S, SEC) | **SEC** (S); SP 811 entry (K). "≈ 746 W" is correct for either definition to 3 sf. Name the 550 ft·lbf/s horsepower if a source line is printed. OpenStax 7.7 also uses 1 hp = 746 W (K) |

### 4.2 Kinetic Energy & Work-Energy Theorem

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 4.2-a | KE = ½mv² | 2e 7.2: net work on a system equals the change in translational KE, ½mv² | OpenStax *College Physics 2e* 7.2 | openstax.org/books/college-physics-2e/pages/7-2-kinetic-energy-and-the-work-energy-theorem | SRC (S) |
| 4.2-b | KE is a scalar and never negative | m > 0 and v² ≥ 0 | DER | — | DER |
| 4.2-c | Doubling v → 4× KE | §B | DER | — | DER |
| 4.2-d | Work-energy theorem W_net = KE_f − KE_i | As 4.2-a | OpenStax 7.2 | as 4.2-a | SRC (S). Notation per Matt's 2026-11-26 decision |
| 4.2-e | Example: car, 2.40 × 10⁵ J and 5.00 × 10³ N | §B | — | — | ILL + DER (A-6, A-7) |
| 4.2-f | 0.145 kg baseball | MLB *Official Baseball Rules* 3.01: 5 to 5¼ oz (≈ 142–149 g) | MLB *Official Baseball Rules* (2024 edition, Baseball Canada reprint) | baseball.ca/uploads/files/2024%20Rules/2024%20MLB%20Official%20Rules%20-%20EN.pdf; content.mlb.com 2019 PDF | **SEC** (S): the rule text was not shown in the excerpt. 0.145 kg sits inside the range (DER: 5 oz = 141.7 g, 5.25 oz = 148.8 g) |
| 4.2-g | Braking distance grows with v² (constant braking force) | See A-1 | NHTSA DOT HS 812 008 (2015) (S), **wording unsafe**; Brake UK (S, SEC); Oregon DOT tailgate talk "about four times as much distance to stop" (S) | ca1.uscourts.gov/sites/ca1/files/citations/S1N_Speeding-August2015_812008.pdf; brake.org.uk/.../stopping-distances; oregon.gov/odot/Programs/T2/TailgateTalks/ControllingSpeed.PDF | DER for the physics. No government source found that states the braking-only rule correctly. See A-1 |

### 4.3 Potential Energy (Gravitational & Elastic)

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 4.3-a | PE_g = mgh from a chosen reference | 7.3: the zero point "is arbitrary; what is important is the difference in gravitational potential energy" | OpenStax *College Physics* 7.3 | openstax.org/books/college-physics-2e/pages/7-3-gravitational-potential-energy | SRC (S) |
| 4.3-b | PE_g belongs to the object–Earth system | 2e 7.3: "the gravitational potential energy put into (or gained by) the object-Earth system… associated with the state of separation between two objects" | OpenStax 2e 7.3 | as 4.3-a | SRC (S). Supports Matt's "system = object + Earth". Teacher note: "the book has PE" is accepted shorthand. If the system is the book alone, gravity does external work and there is no PE term. Pick one framing and do not mix them |
| 4.3-c | Path independence | 2e 7.3 figure caption: "The change in gravitational potential energy (ΔPEg) between points A and B is independent of the path. ΔPEg = mgh for any path" | OpenStax 2e 7.3 | as 4.3-a | SRC (S) + DER (§B, via 3.3) |
| 4.3-d | Hooke's law: restoring force, k in N/m | 16.1: F = −kx; "k is a constant related to the difficulty in deforming the system"; "The units of k are newtons per meter (N/m)"; larger k means stiffer | OpenStax *College Physics* 16.1 Hooke's Law: Stress and Strain Revisited | openstax.org/books/college-physics/pages/16-1-hookes-law-stress-and-strain-revisited | SRC (S). See A-12, A-13 |
| 4.3-e | PE_s = ½kx² | 16.1: "The potential energy stored in a spring is PEel = ½kx²" | OpenStax 16.1 | as 4.3-d | SRC (S). OpenStax writes PE_el. Matt's PE_s is a notation choice and fine |
| 4.3-f | ½kx² = the area of the triangle under F vs x | F rises linearly from 0 to kx; area = ½ · x · kx | DER; DECISIONS l.119–120 "F-x area is work" | (R) | DER. Graph figure: F (N) vs x (m), line through the origin, shaded triangle, with 0.150 m and 60.0 N labelled in text |
| 4.3-g | Elastic limit | AP 5.3: for small deformations Hooke's law is obeyed; larger forces give a curved graph but still elastic behaviour; "still greater forces permanently deform the object". UP1 12.4: the elastic limit is the stress "beyond which the material… becomes permanently deformed" | OpenStax *College Physics for AP Courses* 5.3; *University Physics Vol. 1* 12.4 | openstax.org/books/college-physics-ap-courses/pages/5-3-elasticity-stress-and-strain; openstax.org/books/university-physics-volume-1/pages/12-4-elasticity-and-plasticity | SRC (S). **Nuance:** the proportional (Hooke's-law) limit comes before the elastic limit. For students, "stretched too far, a spring no longer obeys F = kx and may not return to its original length" is accurate. Do not say Hooke's law holds right up to the elastic limit |
| 4.3-h | Example: 4.50 J | §B | — | — | ILL + DER |
| 4.3-i | On Your Own: book, ≈24 J | §B | — | — | ILL + DER |
| 4.3-j | Pumped-storage hydro | DOE: during low demand, excess generation pumps water from a lower to an upper reservoir; at high demand, water flows down through turbines that turn generators. DOE: PSH is "the most dominant form of energy storage on the electric grid today". NREL: "most common type of grid-level energy storage system based on megawatts installed" | US DOE Water Power Technologies Office, "Pumped Storage Hydropower" / "How Pumped Storage Hydropower Works"; NREL "Pumped Storage Hydropower" | energy.gov/eere/water/pumped-storage-hydropower; energy.gov/eere/water/how-pumped-storage-hydropower-works; nrel.gov/water/pumped-storage-hydropower | SRC (S). No % share found, so print none (A-15) |
| 4.3-k | Tear-off: book lifted straight up vs pushed up a ramp to the same height | Same PE_g change (4.3-c) | — | — | DER. See §E |

### 4.4 Conservation of Energy

| ID | Claim | Value / excerpt | Source | Locator | Status |
|---|---|---|---|---|---|
| 4.4-a | ME = KE + PE | 1e glossary: mechanical energy is "the sum of kinetic energy and potential energy" | OpenStax *College Physics* ch. 7 glossary | openstax.org/books/college-physics/pages/7-glossary | SRC (S) |
| 4.4-b | ME is conserved when only conservative forces do work (no friction) | Summary: KE_i + PE_i = KE_f + PE_f when only conservative forces act | OpenStax ch. 7 summary (7.4) | openstax.org/books/college-physics/pages/7-section-summary | SRC (S). Student phrasing "without friction" is acceptable for a frictionless ramp; key note: "and no other outside pushes" |
| 4.4-c | With friction, ME decreases by the work friction does; the energy becomes thermal energy | 7.5: "The total mechanical energy changes by exactly the amount of work done by nonconservative forces"; friction "creates thermal energy" | OpenStax 2e 7.5 | openstax.org/books/college-physics-2e/pages/7-5-nonconservative-forces | SRC (S) |
| 4.4-d | Law of conservation of energy | 1e glossary: "total energy is constant in any process; it may change in form or be transferred from one system to another, but the total remains the same". 2e 7.6: KE_i + PE_i + W_nc + OE_i = KE_f + PE_f + OE_f | OpenStax ch. 7 glossary (1e); 2e ch. 7 summary | as 4.4-a; openstax.org/books/college-physics-2e/pages/7-section-summary | SRC (S). The 2e glossary text was garbled in the search extract; it was not checked |
| 4.4-e | Example: v ≈ 7.9 m/s, mass cancels | §B | — | — | ILL + DER (A-3) |
| 4.4-f | On Your Own: 4.1 × 10² J | §B | — | — | ILL + DER (A-2, A-10) |
| 4.4-g | Regenerative braking | AFDC (full-hybrid animation): the electric motor "converts otherwise wasted energy from braking into electricity and stores it in the battery". Start-stop hybrid page: the generator-starter generates "electricity which is stored in the battery" | US DOE AFDC / fueleconomy.gov hybrid animations | afdc.energy.gov/fueleconomy/animations/hybrids/fullhybrid/fullhybridbraking.html | SRC (S). Wording per A-14. Do not claim a recovery percentage (none sourced) |
| 4.4-h | Tear-off: where does a sliding box's KE go? | To thermal energy in box and floor (some to sound) | 4.4-c | — | SRC (S) + DER |

---

## D. The ten bold terms: suggested definitions

Every definition checks against OpenStax *College Physics* (2e) ch. 7 or §16.1, cited as a secondary source; BIPM covers the unit terms.

| Term | Section | Suggested student definition | Check | Status / note |
|---|---|---|---|---|
| work | 4.1 | the energy transferred to or from an object when a force acts on it through a displacement; W = Fd cos θ | 4.1-a (S) | SRC (S). Add "a scalar; it can be positive, negative or zero" in the prose |
| joule | 4.1 | the SI unit of work and energy; 1 J = 1 N·m | 4.1-e (S); BIPM Table 4 (K) | SRC (S) / BIPM (K) |
| power | 4.1 | the rate at which work is done, or energy is transferred; P = W/t, measured in watts (1 W = 1 J/s) | 4.1-f (S) | SRC (S) |
| kinetic energy | 4.2 | the energy an object has because it is moving; KE = ½mv² | 4.2-a (S) | SRC (S) |
| work-energy theorem | 4.2 | the net work done on an object equals its change in kinetic energy: W_net = KE_f − KE_i | 4.2-a (S) | SRC (S) |
| gravitational potential energy | 4.3 | energy stored in an object–Earth system because of the object's height above a chosen reference level; PE_g = mgh | 4.3-a, 4.3-b (S) | SRC (S). The glossary wording "due to its position in a gravitational field" was **not** found; do not quote it |
| spring constant | 4.3 | a measure of a spring's stiffness: the force needed per meter of stretch or compression, in N/m | 4.3-d (S) | SRC (S). OpenStax: "force constant" (A-13) |
| elastic potential energy | 4.3 | energy stored in a stretched or compressed spring or other elastic object; PE_s = ½kx² | 4.3-e (S) | SRC (S) |
| mechanical energy | 4.4 | the sum of an object's kinetic and potential energy; ME = KE + PE | 4.4-a (S) | SRC (S) |
| law of conservation of energy | 4.4 | energy is never created or destroyed; it changes form or is transferred, and the total stays the same | 4.4-d (S) | SRC (S). Do not shorten it to "ME is always conserved" |

Count = 10, at the workflow limit. "Hooke's law" and "elastic limit" stay as plain-text terms, unbolded.

---

## E. Tear-off questions: answerable from the reading?

| Section | Question (suggested) | Answer | Answerable? | Condition |
|---|---|---|---|---|
| 4.1 | You carry a backpack at constant speed across a level hall. How much work does your upward force do on the backpack? | Zero: the force is perpendicular to the displacement | Yes | The prose must state the perpendicular-force rule and give a carrying or holding example. Key note: speeding up and slowing down involve small horizontal forces; feeling tired is muscle chemistry, not work on the pack |
| 4.2 | A car's speed doubles. If the brakes supply the same force, about how many times farther does it travel while braking? | About 4 times | Yes | The prose must state KE ∝ v² and link KE to braking work through W_net = KE_f − KE_i, with the same-force condition. Say **braking**, not stopping (A-1) |
| 4.3 | A book is lifted straight up to a shelf, and an identical book is pushed up a frictionless ramp to the same shelf. Compare their gains in gravitational potential energy. | Equal: only the height change matters | Yes | Requires the path-independence statement. **Do not ask which takes more work** if friction is not ruled out |
| 4.4 | A box slides across the floor and stops. Where did its kinetic energy go? | Mostly thermal energy in the box and floor (some sound) | Yes | The prose must name thermal energy. A correct answer must not say "used up" or "lost" |

Single-part check: each is phrased as a single question.

---

## F. Key Refreshers: earlier-unit codes confirmed

| Refresher | Code | Evidence | Status / note |
|---|---|---|---|
| Rearrange an equation (solve in symbols) | **U0, 0.3** Algebraic Equation Manipulation | DECISIONS l.22–23 (R) | Code confirmed. **No U0 material exists in the repository**, so the method "solve in symbols first" cannot be confirmed as how 0.3 was taught. Phrase it neutrally ("rearrange for the unknown before you substitute") or ask Matt |
| Vectors vs scalars | **U1, 1.1** Distance, Displacement & Velocity | U1 notes l.20 ("Scalar, vector, magnitude, direction"), l.63–64, l.76–77 (R) | Confirmed. Components with cos θ are **U2, 2.1** (U2 key l.203: Ax = A cos θ) and U3 **3.2** ("Breaking a Force into Components", notes l.277–283; toolbox Fx = F cos θ, l.25). Cite 2.1 or 3.2 for the cos θ refresher |
| Weight Fg = mg | **U3, 3.1** Newton's Laws | U3 notes l.107 learning target, "use Fg = mg to find an object's weight" (R) | Confirmed: 3.1. Use the symbol Fg (U3 l.12) |
| ∑F = ma | **U3, 3.4** Net Force and Acceleration | U3 notes l.398 (R) | Confirmed. Typeset U+2211 |
| mg sin θ on a ramp (optional) | **U3, 3.3** Forces on an Incline | U3 notes l.34, l.387 "Fg,parallel = mg sin θ" (R) | Confirmed. Useful for the 4.3 path-independence derivation (§B) |
| g value | g = 9.8 m/s² | DECISIONS l.344–350 (R) | **U1 used 9.81** (U1 notes l.16, 262, 274, 300, 317, 330). Do not carry 9.81 into any U4 refresher; the 1.4 free-fall refresher, if used, must say 9.8 |

---

## G. UNVERIFIED or not opened (do not print as fact without the locator)

- Exact OpenStax 2e wording of the W = Fd cos θ statement and the 2e glossary entries: (K), or garbled in the extract.
- BIPM *SI Brochure* Table 4 rows for J and W: (K). Host blocked.
- NIST SP 811 entry 7.456 999 E+02 W: confirmed through secondary converters only (SEC).
- MLB Rule 3.01 wording: SEC.
- A correct government statement of "braking distance ∝ v²": **not found**. NHTSA's wording is about stopping distance and is physically loose (A-1).
- Any percentage for pumped storage's US share or round-trip efficiency, and any regenerative-braking recovery percentage: not sourced. Do not print.
- "Solve in symbols first" as the U0 method: UNVERIFIED (no U0 build exists).
- Braking at 0.43 g as "ordinary": (K), a plausibility judgement only.

## H. Observation versus inference

- **Observed:**
  - DECISIONS lines;
  - the U1, U2 and U3 spec text and line numbers;
  - search-result excerpts for each (S) locator;
  - my own arithmetic.
- **Inferred (teaching judgements):**
  - that "ME lost" will reinforce the used-up misconception (A-2);
  - that a displacement arrow on an FBD will read as a motion arrow (A-5);
  - that students will round W before computing P (A-4);
  - that "3.20 m ramp" will be read as a length (A-3).
- **Not observed:** any primary page on openstax.org, bipm.org, nist.gov, energy.gov, afdc.energy.gov, nhtsa.gov or mlb.com.

## I. Search sources used (accessed 2026-11-26)

- [OpenStax College Physics ch. 7 glossary](https://openstax.org/books/college-physics/pages/7-glossary) · [ch. 7 glossary (2e)](https://openstax.org/books/college-physics-2e/pages/7-glossary) · [ch. 7 summary (1e)](https://openstax.org/books/college-physics/pages/7-section-summary) · [ch. 7 summary (2e)](https://openstax.org/books/college-physics-2e/pages/7-section-summary)
- [OpenStax 2e 7.2](https://openstax.org/books/college-physics-2e/pages/7-2-kinetic-energy-and-the-work-energy-theorem) · [7.3](https://openstax.org/books/college-physics-2e/pages/7-3-gravitational-potential-energy) · [7.5](https://openstax.org/books/college-physics-2e/pages/7-5-nonconservative-forces) · [7.7](https://openstax.org/books/college-physics-2e/pages/7-7-power) · [7.7 (1e)](https://openstax.org/books/college-physics/pages/7-7-power)
- [OpenStax 16.1 Hooke's law](https://openstax.org/books/college-physics/pages/16-1-hookes-law-stress-and-strain-revisited) · [AP 5.3 elasticity](https://openstax.org/books/college-physics-ap-courses/pages/5-3-elasticity-stress-and-strain) · [UP1 12.4](https://openstax.org/books/university-physics-volume-1/pages/12-4-elasticity-and-plasticity)
- [BIPM SI Brochure 9](https://www.bipm.org/en/si-brochure-9) · [NIST SP 330 (2019)](https://www.nist.gov/node/445661)
- [NISTunits horsepower to watt](https://search.r-project.org/CRAN/refmans/NISTunits/html/NISThorsepowerTOwatt.html) · [unitconverters hp (550 ft·lbf/s)](https://www.unitconverters.net/power/horsepower-550-ft-lbf-s-to-watt.htm) · [NIST SP 811 1991 (legacy)](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication811e1991.pdf)
- [NHTSA Speeding brochure DOT HS 812 008 (mirror)](https://www.ca1.uscourts.gov/sites/ca1/files/citations/S1N_Speeding-August2015_812008.pdf) · [Oregon DOT tailgate talk](https://oregon.gov/odot/Programs/T2/TailgateTalks/ControllingSpeed.PDF) · [Brake UK stopping distances](https://www.brake.org.uk/get-involved/take-action/mybrake/knowledge-centre/speed/stopping-distances) · [Navy SA 26-20](https://navalsafetycommand.navy.mil/Portals/100/Documents/SA%2026-20%20Speeding%20Mishaps.pdf)
- [DOE pumped storage](https://www.energy.gov/eere/water/how-pumped-storage-hydropower-works) · [NREL pumped storage](https://www.nrel.gov/water/pumped-storage-hydropower)
- [AFDC full-hybrid braking animation](https://afdc.energy.gov/fueleconomy/animations/hybrids/fullhybrid/fullhybridbraking.html)
- [MLB Official Rules 2024 (Baseball Canada reprint)](https://www.baseball.ca/uploads/files/2024%20Rules/2024%20MLB%20Official%20Rules%20-%20EN.pdf) · [baseballrulesacademy 3.01](https://baseballrulesacademy.com/official-rule/mlb/3-01-the-ball/)
