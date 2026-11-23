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
| **Status** | **IMPLEMENTED** |
| **Implemented By** | Commit 6829f2f (2026-11-23): five "Why" prompts in `templates/notes/specs/make_chem_u03_notes.py` became "Reason for the IE trend", "Reason for the electronegativity trend", "Reason for the radius trend", "Reason the ion is smaller", "Cause of a higher MP or BP". `chem_u03_s03.3-s03.6_notes_student.json` and `_notes_key.json` regenerated; only the five prompt lines changed in each, answers unchanged. Routed through the Overseer; built by the Designer. |
| **Verified** | Yes, 2026-11-23, by an independent Auditor: PASS. `validate_notes` OK; `recall.offences()` clean; student and key in step; generator output byte-identical to the JSON; local DOCX builds verify "3 sheets for 3 designed pages" each; fonts embedded; all five cues read correctly. One should-fix is carried as an open item below. |

Files: `templates/notes/specs/chem_u03_s03.3-s03.6_notes_student.json`,
`templates/notes/specs/chem_u03_s03.3-s03.6_notes_key.json`.

## Open question

1. Were these notes printed or filed to Drive already? If so, does the fix include a reissue?

   **Answer (2026-11-23):** Not filed. The Librarian's read-only Drive search found no Chemistry U3
   guided notes (student or key) on Drive, including trash, and no filing-queue or drive-operations
   entry. No Drive reissue is needed. Whether a 2026-11-03 build was printed is unknown; ask Matt.

## Open item

- **Auditor should-fix, before printing or filing.** On the student page the cue "Reason for the
  electronegativity trend" uses about 45% of its single ruled line, leaving too little writing room.
  Fix: give that row 2 lines, or shorten the cue. "Reason for the radius trend" is tight too. A fix
  is a classroom deliverable and routes through the Overseer.
