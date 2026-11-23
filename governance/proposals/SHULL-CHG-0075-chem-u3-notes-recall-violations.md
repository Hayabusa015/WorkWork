# SHULL-CHG-0075 — Chemistry U3 guided notes break the recall-only rule

> **Blocking.** No rule change is proposed. Either the notes are fixed (a classroom deliverable, so
> it routes through the Overseer) or Matt records a named exception. Not resolved here.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0075 |
| **Date** | 2026-11-22 |
| **Source** | Janitor finding, weekly sweep 2026-11-22 (`reports/2026-W47/janitor.md` row 2) |
| **Current Rule** | `governance/proposals/SHULL-CHG-0023-notes-are-recall.md`, Proposed Rule: "A guided-notes packet is strictly recall." `scripts/README.md`: `validate_notes.py` fails when "A guided-notes spec asks a question instead of stating recall content (SHULL-CHG-0023)". |
| **Proposed Rule** | No change. Bring `chem_u03_s03.3-s03.6_notes_student.json` and `_notes_key.json` into compliance, or record an exception on the record if Matt wants the "Why" prompts kept. |
| **Supersedes** | Nothing. |
| **Reason** | `validate_notes` reports 10 problems: "Why" prompt lines in sections 3.3 and 3.4. The specs were built 2026-11-03 on a branch and never checked against main's validator. CI is red because of them (see SHULL-CHG-0076). |
| **Affected Agents** | Overseer (entry point), Builder (fix), Auditor (re-audit). |
| **Affected Skills** | build-document (guided notes). |
| **Affected Courses** | Chemistry. |
| **Risk** | Medium. Student-facing notes contradict a standing rule. If they are already filed to Drive, those copies are also affected (Drive not checked this run). |
| **Recommendation** | Fix through the Overseer. Matt may prefer an exception. |
| **Decision** | Approved by the user in chat, 2026-11-23: "yes approve 0076 and 0075, fix them". |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

Files: `templates/notes/specs/chem_u03_s03.3-s03.6_notes_student.json`,
`templates/notes/specs/chem_u03_s03.3-s03.6_notes_key.json`.

## Open question

1. Were these notes printed or filed to Drive already? If so, does the fix include a reissue?
