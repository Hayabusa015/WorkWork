# SHULL-CHG-0048 — scripts/README.md omits 21 of the 33 scripts in scripts/

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0048 |
| **Date** | 2026-10-22 (first raised in the 2026-10-18 weekly sweep) |
| **Source** | Janitor (2026-10-18 weekly sweep). Re-counted against the repository on 2026-10-22. |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | See section 2. |
| **Supersedes** | `scripts/README.md`, the two tables (lines 3-15), which are presented as the list of scripts. |
| **Reason** | Claim VERIFIED, with a corrected count. The desk summary said 20; the directory now holds 33 scripts besides the README, and the README names 12 of them, so 21 are undocumented. The count may have moved because scripts were added after the sweep. The "REPEAT" tag was not verified here. |
| **Affected Agents** | Janitor, Auditor (both read this README to know what enforcement exists). |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low |
| **Recommendation** | Approve. |
| **Decision** | Pending. |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | No |

---

## 1. Current Rule — verbatim

`scripts/README.md` line 1 and lines 3-4:

> # scripts — enforcement
>
> | Script | Fails the build when |

The README names these 12: `validate_layers.py`, `validate_codes.py`, `validate_tokens.py`,
`find_session_files.py`, `publish_standards.py`, `build_app_css.py`, `build_template_previews.py`,
`build_diagram_molecule.py`, `build_handwriting_font.py`, `build_handwriting_sheet.py`, `key_ink.py`,
`science_tools.py`.

## 2. Proposed Rule

Add a row or paragraph for each of the 21 scripts not named, one line each, saying what it does and
whether it validates, generates, audits or is a helper. The Secretary reads each script's header
before writing its line and does not guess from the filename.

Undocumented now (found by listing `scripts/`):

| Group | Scripts |
|---|---|
| Validators | `validate_agents.py`, `validate_references.py`, `validate_schemas.py`, `validate_profiles.py`, `validate_notes.py` |
| Auditors | `audit_worksheet.py`, `audit_slide_geometry.py`, `audit_print_ink.py`, `audit_fonts.py` |
| Generators | `build_lab_css.py`, `build_slide_tokens.py`, `build_diagram_nuclear_notation.py` |
| Tools and helpers | `_shullos.py`, `measure_tokens.py`, `image_prompts.py`, `desk_export.py`, `key_solution.py`, `repack_pptx.py` |
| Shell hooks and setup | `hook-validate.sh`, `hook-drive-guard.sh`, `setup-environment.sh` |

To keep one place for the list: the README should not restate what a script's own header already says
at length. One line each, pointing at the script.

## 3. Interaction

SHULL-CHG-0047 touches the status line at the end of this file. Approve together or sequence.
