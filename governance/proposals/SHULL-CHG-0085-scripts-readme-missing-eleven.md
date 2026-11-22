# SHULL-CHG-0085 — scripts/README.md is missing eleven scripts

Repeat of: SHULL-CHG-0048 (`SHULL-CHG-0048-scripts-readme-undocumented.md`)

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0085 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 23) |
| **Current Rule** | `scripts/README.md` lists scripts in a two-column table ("Script \| Fails the build when" and following sections). The eleven scripts below have no row (grep, 2026-11-22). |
| **Proposed Rule** | Add one row for each script, describing what it does in the README's existing format. |
| **Supersedes** | Nothing. |
| **Reason** | The README is the index for `scripts/`. These scripts arrived through the 2026-11-13 consolidation. `branch_ledger.py` is documented (line 20). |
| **Affected Agents** | Secretary or whoever is approved to edit `scripts/README.md`. |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low. |
| **Recommendation** | Adopt. Read each script's docstring for its row; do not guess purpose from the filename. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

Undocumented: `add_click_builds.py`, `add_slide_builds.py`, `build_diagram_phys_u03.py`,
`build_diagram_trends.py`, `build_diagram_u02_s02.1_bohr_figures.py`, `build_diagram_u02_s02.2_orbitals.py`,
`build_diagram_u02_s02.3_configurations.py`, `build_diagram_u02_s02.4_stability_valence_ions.py`,
`build_diagram_u02_s02.5_spectra.py`, `build_diagram_u03_slides.py`, `test_key_solution.py`.

## Open question

1. This is the second time `scripts/README.md` has drifted (after SHULL-CHG-0048). Should a validator
   check that every `scripts/*.py` has a README row? That would be a separate tooling change.
