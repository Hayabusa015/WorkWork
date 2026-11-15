# Janitor sweep — 2026-W46 (2026-11-15)

Report-only. Tree checked: `1b584e8` (local `main` = local `origin/main`; not re-fetched). `legacy/` excluded.

## 1. Findings

| # | File | Problem | Your action | Time |
|---|---|---|---|---|
| **BLOCKING** | | | | |
| 1 | `governance/proposals/` (23 files) | **NEW** (class repeats SHULL-CHG-0052). 8 Change IDs name 23 records: 0023 ×4, 0024 ×5, 0046 ×2, 0054 ×3, 0066 ×2, 0068 ×3, 0069 ×2, 0070 ×2. 15 surplus records. All 8 collisions are new on `main` since the consolidation (`d5271f5`, the commit before it, had 57 files and 0 duplicates). `governance/CHANGE_CONTROL.md:43` says "Never reused". Detail in table 3. | Decide: renumber (which record keeps each number) or keep and disambiguate by slug | 10 min |
| 2 | `scripts/desk_export.py:72` | **NEW.** Export keys each document by `f.name[:14]`. 78 records give 63 distinct IDs, so 15 records are overwritten on the Secretary's Desk. Last filename wins: 0023 shows a PENDING record and hides 3 IMPLEMENTED; 0024 shows PENDING and hides 4; 0068 shows PENDING and hides 1 APPROVED + 1 IMPLEMENTED; 0070 shows IMPLEMENTED and hides 1 APPROVED. Table 3. | Do not click Approve/Reject on 0023, 0024, 0066, 0068, 0069, 0070 until finding 1 is settled | 1 min |
| 3 | `scripts/validate_codes.py` output | **NEW** (noted in `docs/PLAN_2026-11-13_consolidate-and-ship.md:85`). FAIL, 15 problems. 2 × Physics section 3.7 not in `courses/physics/DECISIONS.md` (`templates/slide/decks/phys_u03_s03.7.json`, `templates/worksheet/specs/phys_u03_slide_solutions.json`); DECISIONS lines 34-36 list six sections (SHULL-CHG-0068 physics). 13 × `courses/chemistry/DECISIONS.md` lines 406-418 Short titles row `REF` "is not a section in this file". | Decide: retire the 3.7 deck spec or renumber it; allow `REF` in the validator or move the rows | 10 min |
| 4 | `scripts/validate_layers.py` output | **NEW** (same plan note). FAIL, 5 problems: unit titles typed into specs. `templates/assessment/specs/geo_u02_question_bank.json:22` and `:596`; `templates/slide/decks/phys_u03_all.json:5`; `templates/slide/decks/phys_u02_unit.json:5`; `templates/notes/specs/geo_u02_s02.1-s02.5.json:35`. | Approve a build fix (Designer) | 2 min |
| 5 | `scripts/validate_notes.py` output | **NEW** (left open in merge commit `690829a`). FAIL, 10 problems: 5 "Why" lines in sections 3.3 and 3.4, in each of `templates/notes/specs/chem_u03_s03.3-s03.6_notes_key.json` and `..._notes_student.json`. | Decide: reword the five lines or exempt them | 5 min |
| 6 | `scripts/validate_tokens.py` output | **NEW** (same plan note). FAIL, 51 raw hex values in 6 files: `templates/activity/web/operation_periodic_table_demo.template.html` 17; `output/chem-u02/shull-lab-tokens.css` 15; `templates/reference/build_reference.py` 8; `templates/notes/specs/make_geo_u03_figures.py` 6; `templates/reference/vsepr_geometry.py` 4; `templates/test/figure_vectors.py:231` 1. The `output/` file is generated CSS on the archived Lab Lime palette: the palette is not flagged, only that a built file is scanned. | Decide per file: read tokens, or exclude `output/` from the scan | 10 min |
| 7 | `scripts/hook-validate.sh:13` | **NEW.** The Stop hook runs all four failing validators, so it fails for every session on this tree. | None beyond 3-6 | 0 min |
| **REPEATS** | | | | |
| 8 | `workflows/weekly-system-review.md:37-40` | **REPEAT of SHULL-CHG-0065.** "the schedule needs revisiting at the DST change" text unchanged (file last touched 2026-10-22). Record's Decision carries your answer of 2026-11-08, "Keep 4:56 PM"; wording not replaced. Part 2 (legacy retirement) unanswered. | Tell the Secretary to apply Part 1; answer Part 2 | 3 min |
| 9 | `governance/proposals/SHULL-CHG-0034-approval-recording.md:22-24` | **REPEAT of SHULL-CHG-0064.** APPROVED since 2026-09-23 (53 days). Implemented By "blank. Not implemented." No "verbatim" rule in any `.claude/agents/*.md`. | Finish or defer | 2 min |
| 10 | `governance/proposals/SHULL-CHG-0038-notes-old-headers.md:23-25` | **REPEAT of SHULL-CHG-0064.** APPROVED since 2026-09-23 (53 days). Implemented By blank; Verified "No". | Finish or defer | 2 min |
| 11 | `governance/proposals/SHULL-CHG-0039-selfcheck-in-work-box.md:22-24` | **REPEAT of SHULL-CHG-0064.** APPROVED since 2026-09-28 (48 days). Implemented By blank; code appears shipped. | Approve an Auditor check and backfill | 2 min |
| 12 | `governance/proposals/SHULL-CHG-0035-drive-unit-folders.md:24-26` | **REPEAT of SHULL-CHG-0064.** APPROVED since 2026-10-15 (31 days). Verified "Partly". Item (a) needs Drive: not checked this run. | Answer 0064 Q2 (drop the Tests-Quizizz check?) | 2 min |
| 13 | `governance/proposals/SHULL-CHG-0058..0065` (8 files) | **REPEAT (last sweep's records).** All 8 still APPROVED, Implemented By and Verified blank. Work has landed for some without backfill. Table 4. | Tell the Secretary to backfill the SHAs; answer the open questions in table 4 | 10 min |
| 14 | `docs/SHULLOS_IMPLEMENTATION_PLAN.md:1031` and `:1149-1150` | **REPEAT of SHULL-CHG-0046** (5th occurrence). Line 1031: "Status as of 2026-09-08: Phases 1-12 complete. Phases 13-14 not started." Lines 1149-1150: "Not started, deliberately. The Routine is scheduled only after..." directly under the "Actual: activated 2026-09-24" note at 1144. | Approve a wording fix | 1 min |
| 15 | `scripts/README.md` | **REPEAT of SHULL-CHG-0048.** 11 scripts undocumented: `add_click_builds.py`, `add_slide_builds.py`, `build_diagram_phys_u03.py`, `build_diagram_trends.py`, `build_diagram_u02_s02.1_bohr_figures.py`, `..._s02.2_orbitals.py`, `..._s02.3_configurations.py`, `..._s02.4_stability_valence_ions.py`, `..._s02.5_spectra.py`, `build_diagram_u03_slides.py`, `test_key_solution.py`. | Approve a README update | 1 min |
| 16 | `courses/chemistry/DECISIONS.md:4` | **REPEAT of SHULL-CHG-0060 item 3.** "Last updated: 2026-10-28"; newest log entry is 2026-11-10 (line 422). Fixed once in `b4e5110`, stale again. | Approve the date fix; decide on the validator check (0060 Q3) | 1 min |
| **NEW, non-blocking** | | | | |
| 17 | `change-log/CHANGELOG.md` | **NEW.** 19 rows carry a duplicated ID (0023: L161, L181; 0024: L144, L154, L160; 0046: L120, L127; 0054: L92, L97, L102; 0066: L55, L56; 0068: L47, L53, L78; 0069: L46, L77; 0070: L32, L45). Follows finding 1. | None beyond finding 1 | 0 min |
| 18 | `change-log/CHANGELOG.md:199`, `:144`, `:92` | **NEW.** Status mismatch, changelog PARTIAL vs record IMPLEMENTED: SHULL-CHG-0010 (header fixed by 0051, row not superseded); SHULL-CHG-0024 short-filenames; SHULL-CHG-0054 kinetic-orange (record line 18 admits the mismatch). | Approve superseding rows, or tell me which side is right | 3 min |
| 19 | `change-log/CHANGELOG.md:255` | **NEW.** "recorded retroactively in SHULL-CHG-0024". The retroactive record is SHULL-CHG-0032 (row at L173; `docs/CHANGE_ID_RENUMBERING_2026-10-15.md` maps 0024 to 0032). Missed in the 2026-10-15 renumber. | Approve a one-word fix | 1 min |
| 20 | `change-log/CHANGELOG.md:23` vs rows | **NEW.** File defines four statuses (CONFIRMED, PARTIAL, PROPOSED, SUPERSEDED). 14 rows use others: IMPLEMENTED at L84, L85, L127, L179, L180; APPROVED at L56, L62-L69. | Decide: widen the vocabulary or normalise the rows | 2 min |
| 21 | `change-log/CHANGELOG.md` | **NEW.** 7 records have no row: 0023 assessment-template (IMPLEMENTED); 0023 status-docs-stale, 0024 physics-u1-vectors, 0024 validate-tokens-app-exclusion (PENDING); 0031, 0037, 0040 (REJECTED). | Decide: do REJECTED and PENDING records get rows? | 2 min |
| 22 | `change-log/CHANGELOG.md:28-39`, `:93-102`, `:150-163` | **NEW (consolidation leftover).** Date sections out of order (11-10 above 11-12 above 11-11; 10-23 above 10-26; 09-22 and 09-20 above 09-23). Blank line missing before headings at L33, L93, L98, L121, L150. | Approve a reorder | 1 min |
| 23 | `change-log/CHANGELOG.md:224-225` | **NEW.** Two rows in "Open, not yet a change record" read "Answered 2026-09-23 — approved". | Approve removal | 1 min |
| 24 | `governance/proposals/SHULL-CHG-0023-status-docs-stale-and-undocumented-app.md:39` | **NEW on main** (file arrived in the consolidation). PENDING since 2026-09-18, 58 days. Status-line half was fixed by SHULL-CHG-0046/0047. The app-documentation question is still open. | Reject, or approve the remaining half | 2 min |
| 25 | `governance/proposals/SHULL-CHG-0024-validate-tokens-app-exclusion.md:40` | **NEW on main.** PENDING since 2026-09-18, 58 days. Appears moot: `validate_tokens.py` reports no `app/` line today. | Reject as overtaken | 1 min |
| 26 | `governance/proposals/SHULL-CHG-0024-physics-u1-vectors-section.md:18` | **NEW on main.** PENDING since 2026-09-25, 51 days. `courses/physics/DECISIONS.md:25-27` still lists U1 as 4 sections, no `1.0`. | Approve, reject or defer | 2 min |
| 27 | `governance/proposals/SHULL-CHG-0068-print-document-format-fixes.md:21` | **NEW.** PENDING since 2026-11-09, 6 days. Not yet aged; hidden on the desk by finding 2 only if export order changes (it currently wins 0068). | Decide | 5 min |
| 28 | 8 APPROVED records (table 5) | **NEW.** APPROVED, not IMPLEMENTED: 0024 overseer-routes (54 days), 0066 study-guide-unit-span, 0068 physics-u3, 0069 notes-no-inline-blanks, 0070 physics-sum-of-forces, 0071, 0072, 0073. Five say "SHA of that commit: pending, add it here" although the commits exist. | Tell the Secretary to backfill; answer 0024's two `.claude/` questions | 5 min |
| 29 | `governance/proposals/` headers | **NEW.** Three header formats: YAML front matter (15 files, within 0018-0028 and 0041), field table (61), flat text (2). Detail in table 6. | Decide whether to standardise | 3 min |
| 30 | `CLAUDE.md:7`, `README.md:34` | **NEW** (class of SHULL-CHG-0046). "all twelve skills". `.claude/skills/` holds 14; `.claude/skills/README.md` lists 14 (`humanize`, `reconcile-session-files` added 2026-10-15). `README.md:6` says these facts live in `CLAUDE.md`, then restates them at lines 33-34. | Approve a wording fix | 1 min |
| 31 | `brand/README.md:18-19`, `README.md:30` | **NEW.** "all five superseded palettes" / "the five archived palettes". `brand/palette-archive/` holds six (`chem-lab-lime.md` added 2026-10-28 by SHULL-CHG-0054). | Approve a wording fix | 1 min |
| 32 | repo root, 20 `*.whl` files | **NEW on main.** 20 Python wheels, 38 MB, tracked in the root. First committed in `1e8a084` (a WIP commit, 2026-10-04); reached `main` in `3fa32b0`. Not referenced by a README. | Approve removal from tracking | 1 min |
| 33 | `out/`, `output/`, `build/`, `deliverables/` | **NEW.** 183 tracked built files in four differently named directories (42 `.docx`, 42 `.pdf`, 8 `.pptx`, 79 `.png`). `.gitignore:10-12` says built deliverables are not tracked because Drive is canonical. Drive side not checked. | Decide: one output directory, tracked or ignored | 5 min |
| 34 | `.claude/skills/weekly-system-review/SKILL.md:24-28` | **NEW.** Procedure lists 5 validators. `scripts/hook-validate.sh:13` runs 8; 9 exist (`validate_notes`, `validate_profiles`, `validate_references`, `validate_schemas` missing from the skill). | Approve a skill update | 1 min |
| 35 | `reports/` | **NEW.** No weekly report directory between `2026-W38` and this one, though sweeps ran 2026-09-27, 10-04, 10-18 and 11-08 (per the records). The skill says findings go to `reports/YYYY-WW/`. Repeat status this week was established from records only. | Decide whether past sweeps need a note | 1 min |
| 36 | `governance/proposals/SHULL-CHG-0032-notes-template-retroactive.md:184-186` | **NEW.** IMPLEMENTED record still says "Status: being corrected... The Secretary has not verified that removal." | Approve a verification pass | 1 min |
| 37 | `governance/proposals/SHULL-CHG-0064-approved-records-still-open.md:34-37` | **NEW.** Cites `CHANGELOG.md` lines 96, 95, 73. After the consolidation those rows are at 171, 170, 142. | None; note only | 0 min |

## 2. Validators

| Validator | Result | Count |
|---|---|---|
| `validate_layers.py` | FAIL | 5 |
| `validate_codes.py` | FAIL | 15 |
| `validate_tokens.py` | FAIL | 51 |
| `measure_tokens.py --check` | PASS | 1 NOTE: geology display pair 6 grey levels apart (floor 20) |
| `validate_agents.py` | PASS | 7 agents |
| `validate_notes.py` | FAIL | 10 |
| `validate_profiles.py` | PASS | 15 refusals, 2 allowances, 4 specs |
| `validate_references.py` | PASS | 252 files |
| `validate_schemas.py` | PASS | 12 cases |

Every file named in a failure was absent from `main` at `d5271f5` (before the consolidation).

## 3. Duplicate Change IDs

"Desk shows" = the record `desk_export.py` leaves under that ID (last in filename order).

| ID | Record (slug) | Status | Date | On main before consolidation | Desk shows |
|---|---|---|---|---|---|
| 0023 | assessment-template | IMPLEMENTED | 2026-09-12 | no | hidden |
| 0023 | cognitive-load-visual-design | IMPLEMENTED | 2026-09-16 | no | hidden |
| 0023 | notes-are-recall | IMPLEMENTED | 2026-09-20 | yes | hidden |
| 0023 | status-docs-stale-and-undocumented-app | PENDING | 2026-09-18 | no | shown |
| 0024 | app-identity-colour | IMPLEMENTED | 2026-09-20 | no | hidden |
| 0024 | overseer-routes-classroom-builds | APPROVED | 2026-09-22 | no | hidden |
| 0024 | physics-u1-vectors-section | PENDING | 2026-09-25 | no | hidden |
| 0024 | short-filenames | IMPLEMENTED | 2026-10-15 | yes | hidden |
| 0024 | validate-tokens-app-exclusion | PENDING | 2026-09-18 | no | shown |
| 0046 | equivalent-directions-on-keys | IMPLEMENTED | 2026-10-21 | no | hidden |
| 0046 | phase-13-status-stale | IMPLEMENTED | 2026-10-18 | yes | shown |
| 0054 | chem-u3-short-unit | IMPLEMENTED | 2026-10-26 | no | hidden |
| 0054 | chemistry-kinetic-orange | IMPLEMENTED | 2026-10-28 | yes | hidden |
| 0054 | notes-follow-slides | IMPLEMENTED | 2026-10-23 | no | shown |
| 0066 | slide-template-four-fixes | IMPLEMENTED | 2026-11-09 | yes | hidden |
| 0066 | study-guide-unit-span | APPROVED | 2026-11-09 | no | shown |
| 0068 | chemistry-reference-packet | IMPLEMENTED | 2026-11-06 | no | hidden |
| 0068 | physics-u3-six-sections | APPROVED | 2026-11-10 | no | hidden |
| 0068 | print-document-format-fixes | PENDING | 2026-11-09 | no | shown |
| 0069 | course-wide-reference-filename | IMPLEMENTED | 2026-11-06 | no | hidden |
| 0069 | notes-no-inline-blanks | APPROVED | 2026-11-11 | no | shown |
| 0070 | physics-sum-of-forces-notation | APPROVED | 2026-11-11 | no | hidden |
| 0070 | reference-vsepr-grid-and-solubility-x | IMPLEMENTED | 2026-11-10 | no | shown |

Ambiguous cross-references outside `governance/proposals/`, `change-log/`, `reports/`, `legacy/`:

| ID | References | Files | Commits citing the ID (all branches) |
|---|---|---|---|
| 0023 | 8 | 6 | 15 |
| 0024 | 17 | 14 | 26 |
| 0046 | 3 | 3 | 8 |
| 0054 | 29 | 17 | 20 |
| 0066 | 26 | 11 | 8 |
| 0068 | 11 | 5 | 6 |
| 0069 | 22 | 11 | 4 |
| 0070 | 3 | 2 | 8 |

Example: `courses/chemistry/DECISIONS.md:442` and `courses/physics/DECISIONS.md:342` both read "Status: CONFIRMED · SHULL-CHG-0068" and mean different records. Commit `f716dcf` cites "SHULL-CHG-0068, SHULL-CHG-0070" (the Physics pair); `7204bf4` cites SHULL-CHG-0070 (the reference packet).

## 4. Last sweep's records (SHULL-CHG-0058 to 0065), all APPROVED 2026-11-08

| ID | Landed, not backfilled | Still open |
|---|---|---|
| 0058 | `84d4eb1`: Geology open question 7 added (`courses/geology/DECISIONS.md:247`) | Q1-Q3 unanswered |
| 0059 | `38de3fe`: answer moved to the key solution (`templates/notes/specs/phys_u01_s01.1-s01.4.json:322-324`) | Record still APPROVED; Drive-copy question unanswered; Drive not checked |
| 0060 | `b4e5110` (item 3, Chemistry date, stale again: finding 16); `f92c179` (item 4) | Item 1, answered "Yes, delete" 2026-11-08: Drive-status prose still at `courses/geology/DECISIONS.md:229` and `courses/physics/DECISIONS.md:235`. Items 2, 5, 6 open |
| 0061 | `f92c179`: NAMING example replaced | Answered "Mark it 'retired'" 2026-11-08: `courses/chemistry/DECISIONS.md:403` still reads "1.4 \| Isotopes", no annotation |
| 0062 | nothing | Answered "Yes, make it the rule" 2026-11-08: no dated entry in `courses/physics/DECISIONS.md`; line 443 still says the 2/2/1/1 ramp is unchanged |
| 0063 | nothing | Questions in sections 1-3 unanswered |
| 0064 | nothing | Findings 9-12 |
| 0065 | nothing | Finding 8 |

## 5. Other APPROVED, not IMPLEMENTED

| Record | Approved | Days | Implemented By field | Commit found |
|---|---|---|---|---|
| 0024 overseer-routes-classroom-builds | 2026-09-22 | 54 | two `.claude/` changes outstanding (record line 202) | n/a |
| 0066 study-guide-unit-span | 2026-11-09 | 6 | blank | none found |
| 0068 physics-u3-six-sections | 2026-11-11 | 4 | "SHA... pending, add it here" | `f716dcf` |
| 0069 notes-no-inline-blanks | 2026-11-11 | 4 | blank | `18d3d46` (docs) |
| 0070 physics-sum-of-forces-notation | 2026-11-11 | 4 | "SHA... pending"; U3 deck switch not done | `f716dcf` |
| 0071 physics-u3-fbd-set-and-key-images | 2026-11-11 | 4 | "SHA... pending"; visual QA outstanding | `f9d9f41`, `d3edc84`, `2aa8251` |
| 0072 physics-math-symbol-fallback-face | 2026-11-11 | 4 | "Partial... SHA pending"; code follow-ups pending | `d1cad19` |
| 0073 physics-3.1-short-title-and-lab-exceptions | 2026-11-12 | 3 | "SHA... pending" | `258a32f` |

## 6. Header status formats

| Pattern | Files | Effect |
|---|---|---|
| Flat `Status:           PENDING`, no `# ` title | 0023 status-docs-stale (line 39), 0024 validate-tokens-app-exclusion (line 40) | Desk title exports as the bare ID, date blank |
| Status stated twice (front matter line 4 and a trailing `Status:` line) | 0024 short-filenames (74), 0025 (48), 0026 (61), 0027 (84), 0028 (82), 0041 (93) | Two copies of one fact; they agree today |
| Status cell carries more than the enum | 0016:9, 0017:8 ("IMPLEMENTED, and enforced at build time"); 0029:23, 0030:23; 0032:22; 0033:23; 0043:18; 0044:18; 0045:18; 0054 kinetic-orange:18 | Exporter still reads IMPLEMENTED |
| `Status: CONFIRMED · SHULL-CHG-NNNN` in the body | 0033:391, 0036:91, 0040:111, 0054 chem-u3:123, 0054 kinetic-orange:96, 0068 chem-reference:176, 0070 reference-vsepr:101, 0073:144 and :217 | **Not a defect.** Quoted decision-log entries; the exporter reads the header first |
| `**Status: being corrected.**` in the body | 0032:184 | Finding 36 |

## 7. Consolidation leftovers checked

| Check | Result |
|---|---|
| Conflict markers outside `legacy/` | None |
| Duplicate JSON keys in `brand/tokens.json`, `config/drive.json`, `package.json` | None |
| Repeated `##`/`###` headings in live markdown | None that is a defect |
| Broken path references in live markdown | None (`validate_references.py` passes; manual scan found only runtime directories) |
| Out-of-order sections | `change-log/CHANGELOG.md` (finding 22) |
| Same ID created by two branches | Table 3 |
| `claude/funny-heisenberg-vu0q4r` | Still a remote branch; merge state not verified |

## 8. Skipped

| Skipped | Reason |
|---|---|
| Every Drive-vs-repo check (0035 item a; 0059 filed copy; 0060 rows 1, 2, 6; `config/drive.json` known defects; filed-document names) | No Drive connector this run |
| Live Secretary's Desk `proposals` and `decisions` collections | Not readable this run; finding 2 is from the exporter's output, not the live desk |
| The Routine's live cron value | Outside the repository |
| Validators on the pre-consolidation tree | Would need a checkout; nothing was changed |
