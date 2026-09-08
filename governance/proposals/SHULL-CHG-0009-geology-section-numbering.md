# SHULL-CHG-0009 — Geology section numbering

| Field | Value |
|---|---|
| **Date** | 2026-09-08 |
| **Source** | User decision, plus a Drive document located during implementation |
| **Resolves** | CONFLICT-25 |
| **Current Rule** | `shull-geology-guidelines` §10 item 4 and `SHULL_Course_Maps.md` §C.3: Geology has no section numbers within units, and whether it should was an open question. This blocked `validate_codes.py`, which would otherwise fail every Geology document. |
| **Proposed Rule** | **Geology has section numbers.** The full map is 10 units, 54 sections. |
| **Supersedes** | `shull-geology-guidelines` §10 item 4 · `SHULL_Course_Maps.md` §C.3 |
| **Reason** | The user confirmed sections were added to the Geology project while Plate Tectonics was numbered U4. The `Geology_Course_Roadmap` document in Drive carries the complete list and numbers Plate Tectonics as U4, independently corroborating both this and SHULL-CHG-0004. |
| **Affected Agents** | Overseer, Designer, Librarian, Auditor |
| **Affected Skills** | `naming`, `validate_codes`, every `build-*` |
| **Affected Courses** | Geology |
| **Risk** | Low |
| **Recommendation** | Adopt |
| **Decision** | Approved by the user |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `courses/geology/DECISIONS.md` |
| **Verified** | Yes — 54 unique section codes extracted from the written file and counted programmatically; per-unit counts 6+5+5+5+5+5+5+6+6+6 sum to 54. |

## Source and its authority

`Geology_Course_Roadmap` is the **front-of-binder student roadmap** — the same document type as the
Chemistry organizer, which is the confirmed source for the Chemistry map. It is student-facing and
already in use, which makes it strong evidence rather than a working draft.

Critically, **it numbers Plate Tectonics as U4**, matching SHULL-CHG-0004. The unit numbering and the
section numbering corroborate each other from one source.

## What this unblocks

- `courses/geology/DECISIONS.md` — written, complete
- `validate_codes.py` — can now run on all three courses without special-casing Geology
- Geology Drive folder creation — ten unit folders and their section folders
- Geology batch renaming — the last blocker is cleared

## One thing it did not resolve

Sections `5.2` "Volcano Types & Composition" and `5.4` "Types of Volcanoes" read as near-duplicates.
The legacy skill listed them separately too, so this is probably a real split — composition versus
morphology — rather than an error. **It is recorded as Geology open question 1 and is not being
guessed at.** Building either section is blocked until confirmed.
