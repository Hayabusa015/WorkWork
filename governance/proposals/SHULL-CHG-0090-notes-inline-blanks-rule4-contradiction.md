# SHULL-CHG-0090 — "Rule 4" still tells builders to blank words inline, contradicting SHULL-CHG-0069

Repeat of: SHULL-CHG-0069 (and the SHULL-CHG-0023-notes-are-recall pattern: a stated preference
that keeps returning because the rule is documentation, not mechanism)

> No conflict with a LOCKED rule is known. SHULL-CHG-0069 (APPROVED 2026-11-11) is the rule. This
> record removes the leftover text that contradicts it. Part B is Matt's call.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0090 |
| **Date** | 2026-11-22 |
| **Source** | Researcher finding, weekly sweep 2026-11-22 (`reports/2026-W47/researcher.md` row 2) |
| **Current Rule** | `templates/notes/README.md` line 55 (rule 4, from SHULL-CHG-0054): "**A fill-in is the slide's own sentence with its key words blanked.** ... the student copy shows the blanks, sized to the word". `.claude/skills/build-document/SKILL.md` lines 111-112: "make each fill-in the slide's own sentence with the key words blanked." Against these, `templates/notes/README.md` line 91 says "**No inline underscore blanks** (`brand/SHULL_DESIGN_SYSTEM.md` §11, SHULL-CHG-0069)". |
| **Proposed Rule** | A: Rewrite README rule 4 and skill lines 111-112 in the cue-plus-ruled-lines form, pointing at `brand/SHULL_DESIGN_SYSTEM.md` §11 rather than restating it. B: Matt decides whether Geology U3 notes stay as built (no-retrofit) or are rebuilt through the Overseer. C: Build the SHULL-CHG-0069 §8 underscore refusal in `templates/notes/recall.py`. |
| **Supersedes** | `templates/notes/README.md` rule 4 (line 55-60). `.claude/skills/build-document/SKILL.md` lines 111-112, in part. |
| **Reason** | SHULL-CHG-0069 updated design system §11, the QA gate, README line 91 and skill line 135, but missed rule 4 in both files, so each file now contradicts itself. The Geology U3 generator follows rule 4: `templates/notes/specs/geo_u03_s03.1-s03.5_notes_student.json` has 29 underscore runs (grep, 2026-11-22), and its layout comment dates edits to 2026-11-12, after the rule. `recall.py` has no underscore check (grep, 0 hits), so the 0069 §8 refusal is unbuilt. Physics U3 notes comply. |
| **Affected Agents** | Secretary (A), Builder (C; B if rebuilt), Overseer (B entry point), Auditor. |
| **Affected Skills** | build-document. |
| **Affected Courses** | All three (A, C). Geology (B). |
| **Risk** | Medium. Builders read the skill and the README and will keep producing inline blanks until both are fixed. |
| **Recommendation** | Adopt A and C. For B, ask Matt. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. Was Geology U3 built before the SHULL-CHG-0069 rule took effect (no-retrofit), or should it be
   rebuilt to comply? Its layout comment cites 2026-11-12; 0069 was approved 2026-11-11.
