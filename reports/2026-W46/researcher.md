# Researcher — weekly system review, 2026-W46 (2026-11-15)

Report-only. Nothing outside this file was written. Every row is a recommendation for the Secretary; none is applied.
NEW = first raised this run. REPEAT = raised before; the earlier record is named.

## 1. Findings

Blocking first, then shortest fix first.

| # | File | Problem | Your action | Time |
|---|---|---|---|---|
| 1 | `templates/notes/specs/make_geo_u03_s03.1-s03.5_notes.py` lines 23, 38, 108-122; `geo_u03_s03.1-s03.5_notes_student.json` (29 lines with underscore runs) | **BLOCKING for that packet. NEW.** Geology U3 guided notes use inline underscore blanks ("Hematite may look ____. Its streak is ____."). `SHULL-CHG-0069-notes-no-inline-blanks.md` (approved 2026-11-11, "all three courses, only underscores count") bans them. Its section 5 list of non-compliant packets omits Geology U3. The generator was last touched 2026-11-12 (line 421), after the rule. No Drive-operation log for Geology U3 notes exists in `reports/drive-operations/`, so by repo evidence it is not yet filed. Physics U3 student spec has 0 underscore runs and complies. | Decide: rebuild Geology U3 notes as prompt + lines before it prints, or leave as built. | 2 min |
| 2 | `templates/slide/decks/phys_u03_specs.py` lines 2, 123, 144, 165, 197, 229; `phys_u03_s03.7.json` line 4; `phys_u03_all.json` lines 661-747 (`U03 • S03.7`); `phys_u03_combined.py` lines 16-22; `templates/worksheet/specs/phys_u03_slide_solutions.json` lines 11, 835; `scripts/build_diagram_phys_u03.py` line 513 | **BLOCKING for any rebuild. NEW (contradicts `SHULL-CHG-0068-physics-u3-six-sections.md` section 7 F5, which reported a grep finding no `3.7`; these files arrived with the 2026-11-13 consolidation).** The only U3 deck source in the repo is the superseded seven-section outline: code `3.7` (not in `courses/physics/DECISIONS.md` lines 34-36), and old titles for 3.3-3.6. Rebuilding from it prints a retired code in the footer (CLAUDE.md section 3). The slide-solutions spec declares `3.7`, so the key builder now refuses it. | Decide: regenerate these specs on the six-section map, or mark them superseded. Say which file is your current deck. | 5 min |
| 3 | same files, `phys_u03_specs.py` line 88 | NEW. Slide text "Friction waits until 3.6." Friction is `3.5` (DECISIONS line 36), and DECISIONS lines 115-116 allow friction in FBD practice before 3.5. | Fix with row 2. | 1 min |
| 4 | `templates/slide/decks/phys_u03_specs.py` lines 8-10; `templates/worksheet/specs/phys_u03_slide_solutions.py` line 7 | NEW. Stated reason "Archivo has no Greek capital sigma or small theta, so the decks write Fnet and angle" is superseded twice: ∑ is U+2211, which Archivo carries (`SHULL-CHG-0070-physics-sum-of-forces-notation.md`), and θ stays a symbol (`SHULL-CHG-0072-physics-math-symbol-fallback-face.md`). 159 `Fnet`/Σ hits in 15 files. 0070 F1 (switch the deck) is still open. | Fix with row 2. | 1 min |
| 5 | `templates/notes/specs/phys_u01_s01.1-s01.4.json` lines 321-324; `templates/notes/build_notes_docx.py` lines 612-615 | **REPEAT x3** (`reports/2026-09-24_chg0030-notes-headers-audit.md` row 1; `SHULL-CHG-0059-physics-s1.1-answer-leak.md`). Observation: "meaning 29.7 m/s downward." now sits in a `solution` field, which the builder prints only on the key. Inference: the spec leak is fixed. The record still shows Implemented By and Verified blank, and the Drive copy is unchecked. The key line is now a fragment with no working. Re-solved: v = √(2 × 9.81 × 45.0) = 29.7 m/s, t = 3.03 s. | Have the Auditor verify and close 0059; answer its open Drive question. | 5 min |
| 6 | `templates/worksheet/specs/build_phys_u03_fbd_problem_set_1.py` line 15; `phys_u02_s02.2.build.sh` lines 6-12; `phys_u02_s02.3_practice.build.sh` line 11; `templates/worksheet/build_worksheet_docx.py` lines 69-70 | **REPEAT x4+** (`SHULL-CHG-0062-physics-student-page-tier-label-pattern.md`, approved 2026-11-08 with "Yes, make it the rule"; Implemented By blank). Three days later the U3 FBD set used another one-time ramp override (3/4/4/1). Physics sets built since the first U1 packet: 9, 10, 8, 5+5+5, 12 questions. The enforced 2/2/1/1 has not been used as written since. Per `SHULL-CHG-0071-physics-u3-fbd-set-and-key-images.md` section 4, the ramp is CONFIRMED, not LOCKED. | Give the default count and tier-label rule so 0062 can be implemented. | 5 min |
| 7 | `templates/worksheet/specs/phys_u02_s02.2.build.sh` lines 25-105; `phys_u02_s02.3_practice.build.sh` lines 26-106; `phys_u02_s02.2_quiz.build.sh` lines 27-107 | NEW pattern. The same ~80-line key-builder override is pasted into three build scripts (six documents): no tier tags on the key, hand size 27, short rows merged, cards split at a seam. Line 12 of the first: "None of these is a standing rule yet". "Matt 2026-10-16: no tier tags on the key either" contradicts `courses/physics/DECISIONS.md` lines 467-469 (key keeps tier labels) and is recorded nowhere else. | Decide: make these the key builder's defaults (standard, all courses) or Physics-only. | 5 min |
| 8 | `courses/physics/DECISIONS.md` lines 276-311 and 409-426 | NEW pattern (`SHULL-CHG-0073-physics-3.1-short-title-and-lab-exceptions.md`; 2026-09-14 S1.3 entry). Both Physics labs built so far dropped the Alconox block; the second also dropped Safety and Disposal and cut the pre/post-lab mix. Both entries say "not a precedent". Two of two is a pattern. | Decide: a Physics lab profile (course decision), or keep asking each time. A default with no Safety section risks missing a real hazard on a later lab; keep that conditional. | 5 min |
| 9 | `courses/physics/DECISIONS.md` lines 166-171; `reports/drive-operations/2026-11-04_phys-u02-unit-tests-study-guide.md` lines 22-24; `reports/drive-operations/2026-09-25_phys-u01-day1-mc-bank.md` (filename only; not opened) | NEW. DECISIONS says no Day 1/Day 2 test structure is confirmed for Physics. U2 was built and filed as Day 1 Multiple Choice + Day 2 Written, versions A-C; U1 has a Day-2 test (DECISIONS lines 354-358) and a Day-1 MC bank log. | Confirm or deny it as the Physics test shape (course decision). | 2 min |
| 10 | `courses/physics/DECISIONS.md` lines 344-351; `make_phys_u03_s03.1-s03.6_notes.py` lines 146, 191, 309, 316, 372, 394; `phys_u03_specs.py` lines 179, 183, 214, 227 vs 70, 96, 239-251; `make_phys_u02_s02.1-s02.3_notes.py` lines 134-141 | NEW pattern. Rule: answers that depend on g = 9.8 carry two significant figures. U3 notes print three (588 N, 2.46 m/s², 3.35 m/s², 2.41 m/s²). The deck spec mixes two (2.5, 3.4, 2.4 m/s²) and three (588 N, 2.45 m/s², 36.8 N). U2 notes mix them (1.0 m; 28.6 m; 6.71 m). The 2026-11-04 U2 test audit also needed sig-fig fixes. | State the rule you want: two figures, or three with g written 9.80. | 3 min |
| 11 | `brand/tokens.json` lines 442-450; `templates/reference/build_reference.py` lines 9-10, 38-41, 112-113; `make_phys_u02_s02.1-s02.3_notes.py` lines 8, 119; `phys_u03_specs.py` lines 8-10; `reports/2026-10-26_chem-u03-qa-audit.md` finding 1 | NEW pattern. **Touches LOCKED typography tokens. Held for you, not resolved.** One problem, four answers: spell it ("theta", "arctan"), swap a word ("angle", "Fnet"), draw it as SVG (Chemistry reference λ and ν), fall back to Inter (0072, scoped "Physics documents only", PROVISIONAL). Twice a builder claimed Archivo lacked a glyph it has (baseline ion charges in Chemistry U3; Σ vs ∑). Chemistry needs λ, ν and ⇌ too. | Decide: one missing-glyph rule for all three courses, or keep 0072 Physics-only. | 5 min |
| 12 | `reports/2026-10-27_geo-s02.3-dinosaur-poster-qa-audit.md` findings S1, A1, and "Carried forward"; `reports/2026-10-26_chem-u03-qa-audit.md` finding 14; `SHULL-CHG-0071-...md` section 10.5 A1; `templates/lab/SHULL_Lab_TEMPLATE_MASTER.html` line 89 (as cited by the audit; not re-opened) | NEW pattern, 5 occurrences, all three courses. Student-page text under the 8 pt `printBody` floor: worksheet chrome 6.5 and 7.5 pt, lab eyebrow 7.2 pt, activity labels 7 pt, FBD label-bank subscripts about 6 pt. Routed "to the Secretary" on 2026-10-28; no proposal exists (grep of `governance/proposals/`). | Decide: raise the shared chrome to 8 pt, or lower the floor for labels. Standard-level. | 3 min |
| 13 | `standards/NAMING.md` lines 40-43; `reports/2026-10-26_chem-u03-qa-audit.md` finding 8; `reports/2026-10-27_geo-...-qa-audit.md` S3, P7; `SHULL-CHG-0071-...md` section 5 | NEW pattern, 4 occurrences, all three courses. "No row, no topic" is bypassed with a descriptor each time: "Trends and Ions", "Dinosaur Poster", "Infographic", "Free-Body Diagrams". Each was recorded as a one-off or left open. | Decide: allow a descriptor when a section has no short title (standard), or add the short-title rows. | 3 min |
| 14 | `reports/2026-10-26_chem-u03-qa-audit.md` finding 7; `reports/2026-10-27_geo-...-qa-audit.md` N2; `phys_u03_combined.py` line 19; `make_phys_u02_s02.1-s02.3_notes.py` line 94 | NEW pattern, 3 occurrences. Builders print the section code three ways: `U03 • S03.4` (slides), `U03 / S3.4` (worksheets), `U2 / S2.1` and `U01 / S01.2` (notes). NAMING section 4 asks for one chip family. | Pick one form. Standard-level. | 2 min |
| 15 | `templates/notes/specs/make_chem_u03_notes.py` lines 14-17, 68, 109, 115 | NEW. Docstring: placing melting and boiling point under 3.6 "is a mapping for Matt to confirm". The student page prints "Slide 8 · S3.6". No record shows it confirmed. Related: 3.5 "Additional Periodic Trends" was dropped 2026-10-26, and the 2026-11-03 deck adds melting and boiling points. | Confirm 3.6 as the home for melting/boiling point. | 1 min |
| 16 | `output/chem-u02/2.5 Lab Key - Flame Tests.html` lines 213-217; `reports/drive-operations/2026-10-15_chem-u02-filing.md` lines 172, 187-188; `courses/chemistry/DECISIONS.md` lines 383-388 | NEW. A 2.5 Flame Tests lab was built and filed 2026-10-29 "as a draft" with SDS checks and lab placement open. DECISIONS still blocks any lab past U0 except U1.1 as final. The filed name carries no draft marker. No safety claim is made here; the key leaves the SDS lines for you to date. | Confirm 2.5 Flame Tests as a lab placement (or not), so open question 4 can be updated. | 2 min |
| 17 | `make_geo_u03_s03.1-s03.5_notes.py` lines 15-17; `phys_u02_s02.2.build.sh` line 30; `make_chem_u03_notes.py` line 22; 49 dated "Matt, 2026-…" comments in 25 files under `templates/` | NEW pattern (same failure as `SHULL-CHG-0069-...md` "I thought we made this rule"). Your chat instructions are recorded in generator docstrings and build-script comments, not in a decisions file. Example: Geology U3 is taught 3.1, 3.5, 3.2, 3.3, 3.4; `courses/geology/DECISIONS.md` does not say so. | Approve a one-time sweep that lists these for you to mark one-off or standing. | 2 min |
| 18 | `reports/2026-10-26_chem-u03-qa-audit.md` findings 8-9; `SHULL-CHG-0059-...md`; `reports/2026-10-27_geo-...-qa-audit.md` B1 | NEW pattern, 3 occurrences, all three courses. An answer or an undecided item reached a student page: Physics S1.1 answer beside the blank, Chemistry U3 slide 19 answers on the question slide, Geology Niger site while still PROVISIONAL. Each was caught by audit, late. | Decide: add "no answer on the page that asks for it" to the QA gate. Standard-level. | 2 min |
| 19 | `courses/physics/DECISIONS.md` lines 235-236; `courses/geology/DECISIONS.md` lines 229-231 | **REPEAT** (`SHULL-CHG-0060-stale-drive-state-prose-in-decisions.md`, approved 2026-11-08, Implemented By blank). "Physics/ holds 1 of 11 unit folders" and "Geology/ is an empty placeholder" are still there; `reports/filing-queue.md` lines 13-15 list files filed under Geology Unit 02. | Ask the Secretary to implement 0060. | 1 min |
| 20 | `courses/chemistry/DECISIONS.md` line 403; `templates/slide/decks/chem_u01_s01.4_isotopes.json` | **REPEAT** (`SHULL-CHG-0061-chem-retired-1.4-still-listed.md`, approved 2026-11-08, Implemented By blank). Short-titles row `1.4 Isotopes` still lists a retired code. | Ask the Secretary to implement 0061. | 1 min |
| 21 | `courses/README.md` line 18 | **REPEAT** (`SHULL-CHG-0068-physics-u3-six-sections.md` section 7 F7, unassigned). "Physics — 11 units, 48 sections". DECISIONS says 47. | Approve replacing the count with a pointer. | 1 min |
| 22 | `courses/chemistry/DECISIONS.md` lines 4, 176, 486-488 | NEW. "Last updated: 2026-10-28" with log entries dated 2026-11-06 and 2026-11-10. "Given to students around Week 2": the packet was finalised 2026-11-10, week 11. The optional-worksheet cap question sits only inside a log entry, not in the Open questions list. | Approve three small edits. | 2 min |
| 23 | `reports/2026-10-26_chem-u03-content-verify.md` finding 6; `reports/2026-10-26_chem-u03-qa-audit.md` findings 5-6; `change-log/CHANGELOG.md` line 229 | **REPEAT** (CHANGELOG open row, 2026-09-09: "Should Chemistry adopt 2/2/1/1 too?"). The audited Chemistry U3 practice set runs 2/2/1/1 with a `SCORE / 13` header. DECISIONS asks for 3-4 medium items and a 5-point rubric at the top (lines 136-138, 167). | Answer the 2026-09-09 question; say whether practice sets carry the 5-point rubric. | 3 min |

## 2. Open questions

Answers are proposed, never adopted.

| Course | Q | Question | Status | Repo evidence now | Proposed answer |
|---|---|---|---|---|---|
| Chemistry | 3 | Grading framing | **REPEAT** (`SHULL-CHG-0063-open-question-evidence-and-pacing-checks.md` section 4) | The U3 practice set prints `SCORE / 13`, not the 5-point rubric (finding 23). Does not settle the weights. | None. Ask. |
| Chemistry | 4 | Lab placements beyond U0 | **REPEAT**, new evidence | 2.5 Flame Tests built and filed (finding 16). | Add 2.5 Flame Tests as confirmed, if Matt says so. |
| Chemistry | log | Optional-worksheet cap | NEW as a listed question | None. | Move it into the Open questions list. |
| Chemistry | pacing | PROVISIONAL pacing | **REPEAT** (0063 section 3), evidence changed | 0063 said evidence reached Unit 1. It now reaches U3 (section 3 below). | Re-base; see section 3. |
| Physics | 1 | Course identity | **REPEAT** (0063 section 4) | Atwood, incline-and-pulley and friction-on-incline problems are built (`make_phys_u03_s03.1-s03.6_notes.py` lines 428-460). | None. Matt's statement. |
| Physics | 2 | Algebra only, or plus trig | **REPEAT** (0063 section 1), stronger evidence, different answer | U2 and U3 notes use sin, cos and inverse tan throughout (`make_phys_u02_s02.1-s02.3_notes.py` lines 119-141; `make_phys_u03_s03.1-s03.6_notes.py` lines 216-238). | Algebra plus right-triangle trig. This replaces 0063's "ratios, not trig-first". |
| Physics | 3 | Gradebook weights | **REPEAT** | None. | Ask. |
| Physics | 4 | Notes-scaffolding index | **REPEAT**, changed by 0069 | "Heavy" can no longer mean inline blanks. | Ask what heavy/medium/light means under prompt + lines. |
| Physics | 5 | Where is the unit map PDF | **REPEAT** (0063 section 2) | U3 no longer follows that PDF (DECISIONS lines 69-70). | Close as "map confirmed; source not recoverable; U3 follows the deck". |
| Physics | 6 | Pacing guide PDF | **REPEAT** (0063 section 2) | Not in the repo. | Ask for it, or drop the reference. |
| Physics | 7 | Lab frequency | Half answered 2026-11-12 | Two labs in about 53 student days (S1.3, 3.1). Build dates only. | Ask. |
| Physics | 8 | Five-tab binder | **REPEAT** | None. | Ask. |
| Physics | new | Day 1 / Day 2 test structure | NEW | Finding 9. | Confirm as built for U1 and U2. |
| Geology | 1 | 5.2 vs 5.4 | **REPEAT** (0063; CHANGELOG row 2026-09-08) | None. | Ask before U5. |
| Geology | 2 | Gizmo exception | **REPEAT** | None new for Geology. | Ask. |
| Geology | 3, 4 | Grading; late work | **REPEAT** | None. | Ask. |
| Geology | 5 | Pacing guide wanted | **REPEAT**, new evidence | Section 3 below. | Ask; the data suggest a light unit-level calendar. |
| Geology | 6 | U7-U10 content PROVISIONAL | **REPEAT** | None. | Leave open. |
| Geology | 7 | U1 section-code offset | **REPEAT** (`SHULL-CHG-0058-geology-u1-numbering-offset.md`; CHANGELOG row 2026-09-09, 9 weeks) | `templates/notes/specs/geo_u01_s01.2-s01.4.json` lines 29-31 unchanged. U2 and U3 builds use roadmap codes without conflict. | Ask. Blocks U1 only. |

## 3. Pacing

Today is 2026-11-15. Student days through Fri 2026-11-13: 43 (Q1) + 10 = 53 of 176, 30%. "Latest build" is repo evidence of builds, not of classroom pace; the last column is inference.

| Course | Plan says | Latest build evidence | Sections covered | Inference |
|---|---|---|---|---|
| Chemistry | Q1 = U0-U3; Q2 = U4-U7 (`courses/chemistry/DECISIONS.md` lines 346-355, PROVISIONAL) | U3 homework filed 2026-11-06; no U4 build | 21 of 90 codes, 23% | About two weeks behind the PROVISIONAL plan. |
| Chemistry | Q2 holds U4-U7 in 41 days | Arithmetic from the file's own rule: 25 sections × 1.5 to 2 days + 4 two-day tests = 45.5 to 58 days | — | **Q2 does not fit as written**, before any delay. With 31 days left, less so. NEW. |
| Physics | No pacing in repo (open question 6) | U2 tests filed 2026-11-04; U3 lab built 2026-11-12 | 11 of 47, 23% | At this rate the map does not finish. |
| Geology | "None yet" (DECISIONS lines 222-223) | U2 study guide filed 2026-11-10; U3 notes built | 11 of 54, 20% | At this rate the map does not finish. |

| # | File | Problem | Your action | Time |
|---|---|---|---|---|
| 24 | `courses/chemistry/DECISIONS.md` lines 342-359 | **REPEAT** (0063 section 3) with a NEW calculation: the Q2 allocation needs 45.5 days at its own lowest rate and has 41. | Give the real position in each course, and which units compress or drop. | 5 min |

## 4. Content re-solved, no error found

| Material | Checked | Result |
|---|---|---|
| `make_phys_u03_s03.1-s03.6_notes.py` | All 26 worked examples | Correct. Sig-fig count only (finding 10). |
| `phys_u03_specs.py`, `phys_u03_slide_solutions.py` | Every problem slide and its steps | Arithmetic correct. Codes and notation stale (findings 2-4). |
| `phys_u03_fbd_problem_set_1.json` | Arrow magnitudes on 12 items | Consistent with equilibrium and Newton's 2nd law. |
| `make_phys_u02_s02.1-s02.3_notes.py` | Every numeric key row | Correct. |
| `output/physics/u03/3.1 Lab Key - Newton's Laws.html` lines 237-253 | Percent error, percent difference, weights | Correct. |
| `make_chem_u03_notes.py` | IE values, proton counts, iodine MP/BP, trends | Correct. |
| `templates/reference/build_reference.py` lines 83-140 | Constants, conversions, example | Correct. |
| `courses/chemistry/DECISIONS.md` lines 202-212 | Polyatomic counts 15 + 22 = 37 | Correct. |
| `make_geo_u02_question_bank.py` | Dates, sequences and keyed answers, every item | Correct. |
| `make_geo_u03_s03.1-s03.5_notes.py` | Mohs tools, streaks, grain sizes, parent rocks | Correct. |
| `chem_u03_s03.4-s03.6_trends.json` line 217 | Francium/cesium key (2026-10-26 blocking finding) | Fixed. |

Not read this run, so not vouched for: the Physics U2 worksheet, quiz and test specs, the Chemistry U1/U2 notes and decks, the Geology U2 notes and study guide, the snow-day and practice sample specs.

## 5. Skipped

| Check | Why |
|---|---|
| All Google Drive state: the filed Physics S1.1 notes copy, U3 section folders 03.1-03.7, the Flame Tests files, whether Geology U3 notes are filed, the pacing PDFs | No Drive connector this run. Not guessed. |
| `.docx`, `.pptx` and `.pdf` contents in `output/` | No tool to open them. Specs and HTML were read instead. |
| Validators and `git log` | No shell. |
| Ohio standards codes | None are printed in the material read; none were verified or proposed. |
| `legacy/`, `brand/palette-archive/` | Excluded by policy. |
