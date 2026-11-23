# SHULL-CHG-0076 — CI on main is red: four validators fail

> **Blocking (CI).** Four findings are bundled because each one turns `main` red. Each part can be
> decided on its own. Part C is **not** a brand defect: the archived Lab Lime palette is covered by
> no-retrofit, so `brand/palette-archive/` rules are not in question. No conflict with a LOCKED rule
> is known.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0076 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` rows 3-6) |
| **Current Rule** | `scripts/validate_codes.py` lines 89-99 (Short titles, SHULL-CHG-0041): a row fails if `code[:1].upper() != "U" and code not in valid[c]` — "{code} is not a section in this file". `scripts/validate_tokens.py`: fails when "A raw hex value is typed outside `tokens.json`" (`scripts/README.md`). `GENERATED` and `SVG_EXCEPTION` are the only exemptions. `scripts/validate_layers.py`: fails when "A course fact (unit title, section code, calendar date, grading percentage) appears in a skill". |
| **Proposed Rule** | A: `validate_codes` accepts `REF` as a non-section short-title key. B: the five branch-built files read colours from `brand/tokens.json` (or a generated token file), or Matt records a named exception. C: Matt chooses to exempt `output/` snapshots in `validate_tokens` or remove the stale copy. D: `validate_layers` uses word-boundary matching and ignores section titles, and Matt decides whether a deck `sectionTitle` may name the unit. |
| **Supersedes** | A: `scripts/validate_codes.py` Short-titles check, in part. C: `scripts/validate_tokens.py` exemption list, in part, if exemption is chosen. D: `scripts/validate_layers.py` matching, in part. B supersedes nothing. |
| **Reason** | All eight validators run in `.github/workflows`, so `main` has been red since the 2026-11-13 consolidation. A red baseline hides new failures. |
| **Affected Agents** | Secretary (tooling edits once approved), Builder (part B rebuild of affected files), Designer (part B token reads). |
| **Affected Skills** | apply-shull-design (part B). |
| **Affected Courses** | Chemistry (A, B, C), Physics (B, D), Geology (B, D). |
| **Risk** | Medium. A and D loosen checks; a loose regex can let real defects through. |
| **Recommendation** | A and D as proposed. B: read from tokens. C: Matt's choice (open question 2). |
| **Decision** | Approved by the user in chat, 2026-11-23: "yes approve 0076 and 0075, fix them". Open choices answered by the user the same day, choosing these options in the main session's question: part C "Remove it (Recommended)"; part D "No, use 'Unit N, all sections' (Recommended)"; part B "Named exception (Recommended)". |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | Commit ef106b4 (2026-11-23). A: `scripts/validate_codes.py` accepts `REF` as a non-section short-title key. B: `scripts/validate_tokens.py` gets a `NAMED_EXCEPTION` set for `templates/activity/web/operation_periodic_table_demo.template.html`, `templates/reference/build_reference.py` and `templates/reference/vsepr_geometry.py` (colours with no token); `templates/notes/specs/make_geo_u03_figures.py` and `templates/test/figure_vectors.py` now read colours from `brand/tokens.json` (figures rebuilt byte-identical). C: `output/chem-u02/shull-lab-tokens.css` removed. The two flame-test lab HTML snapshots in `output/chem-u02/` linked to it; their rendered PDFs are unaffected; a rebuild should come from the lab template. D: `scripts/validate_layers.py` matches whole words and blanks out section titles that contain a unit title. Beyond the record's wording, stated plainly: it counts a one-word unit title only where it is a label (a heading, a title/unit JSON field, or beside U5 / Unit 5), so the prose "Volcanoes released…" no longer trips it; tested that "## U5 Volcanoes" and "Geologic Time unit" are still flagged. Commit 6829f2f (2026-11-23), D: `phys_u02_unit.json` and `phys_u03_all.json` `sectionTitle` = "Unit 2, all sections" / "Unit 3, all sections" (and the literal in `phys_u03_combined.py`); no builder reads `sectionTitle`, so slides are unaffected. |
| **Verified** | Yes, 2026-11-23, Auditor run on the working tree: `validate_layers`, `validate_codes`, `validate_tokens`, `validate_agents`, `validate_schemas`, `validate_references`, `validate_profiles`, `validate_notes`, `validate_change_ids` all exit 0; `measure_tokens`, `build_slide_tokens`, `build_app_css` `--check` all exit 0. Open observation, not fixed: the cover headline fields still read "Unit 3\nForces and Motion" and "Unit 2\nMotion in Two Dimensions". `validate_layers` misses them only because of the literal "\n" before the title. |

## Validator results (2026-11-22, from the Janitor's run)

| Validator | Exit | Result |
|---|---|---|
| `validate_layers.py` | 1 | FAIL, 5 problems (169 files) |
| `validate_codes.py` | 1 | FAIL, 15 problems (306 files): 2 are Physics `3.7` (SHULL-CHG-0074), 13 are `REF is not a section` |
| `validate_tokens.py` | 1 | FAIL, 51 raw hex across 6 files (273 files) |
| `measure_tokens.py --check` | 0 | OK (note: Geology display pair 6 grey levels apart, needs border and label) |
| `validate_agents.py` | 0 | OK, 7 agents match the matrix |
| `validate_references.py` | 0 | OK (252 files) |
| `validate_schemas.py` | 0 | OK, 12 cases |
| `validate_profiles.py` | 0 | OK, 15 refusals, 2 allowances, 4 specs build |
| `validate_notes.py` | 1 | FAIL, 10 problems (14 files) (SHULL-CHG-0075) |
| `build_slide_tokens.py --check` / `build_app_css.py --check` | 0 | current |

The Secretary did not re-run these validators.

## Parts

| Part | Janitor row | What fails | Detail |
|---|---|---|---|
| A | 3 | `validate_codes`, 13 hits | `courses/chemistry/DECISIONS.md` Short titles has 13 `REF` rows (confirmed by grep), added by `SHULL-CHG-0068-chemistry-reference-packet.md` (59858c0, 2026-11-06). Validator gap, not a data defect. |
| B | 4 | `validate_tokens`, 36 hex | `templates/activity/web/operation_periodic_table_demo.template.html` (17), `templates/reference/build_reference.py` (8), `templates/notes/specs/make_geo_u03_figures.py` (6), `templates/reference/vsepr_geometry.py` (4), `templates/test/figure_vectors.py` (1). Branch-built files, 2026-11-04 to 11-09. |
| C | 5 | `validate_tokens`, 15 hex | `output/chem-u02/shull-lab-tokens.css` is an old, differing copy of the generated `templates/lab/shull-lab-tokens.css`, outside the `GENERATED` list. Carries archived Lab Lime; no-retrofit applies, so **not a brand defect**. The defect is the stale duplicate. |
| D | 6 | `validate_layers`, 5 hits | Two restate a unit title in deck `sectionTitle` (`phys_u03_all.json:5` "Forces and Motion", `phys_u02_unit.json:5` "Motion in Two Dimensions"). Three look like substring false positives: `geo_u02_question_bank.json:22,596` ("Volcanoes" at 596), `geo_u02_s02.1-s02.5.json:35` ("The Geologic Time Scale" contains "Geologic Time"). |

## Open question

1. Part D: may a deck's `sectionTitle` name the unit, or must it name the section?

   **Answer (2026-11-23, Matt):** No. Use "Unit N, all sections". Applied in commit 6829f2f.
2. Part C: exempt `output/` snapshots in the validator, or remove `output/chem-u02/shull-lab-tokens.css`?
   Removal is a deletion and needs Matt's explicit confirmation.

   **Answer (2026-11-23, Matt):** Remove it. Removed in commit ef106b4.
