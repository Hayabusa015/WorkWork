# SHULL-CHG-0099 — Chemistry U6 Chemical Nomenclature: four sections

> **No conflict with a LOCKED rule.** This replaces the U6 line of the Chemistry curriculum map. It
> renumbers 6.1–6.4 to new content and retires 6.5 and 6.6. No U6 material exists in this repository
> (grep for `U06`, `S6.`, `_s06`, 2026-11-23: no Chemistry hits), so no spec or chip is renumbered here.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0099 |
| **Date** | 2026-11-23 |
| **Source** | User. Matt, in conversation, 2026-11-19, verbatim: "Section rework: 6.1: Covalent Names and Formulas 6.2: Polyatomic Ions 6.3: Ioinic Names and Formulas with transition metals. 6.4 Naming acids and formulas." Repeated 2026-11-20: "update the chemistry guidelines with the new unit 6 sections". |
| **Current Rule** | `courses/chemistry/DECISIONS.md`, Curriculum map, Phase 2: "**U6 Chemical Nomenclature** (6 sections) 6.1 Ions & Ionic Compounds · 6.2 Ionic Names & Formulas · 6.3 Transition Metals · 6.4 Polyatomic Ions · 6.5 Covalent Names & Formulas · 6.6 Acids" |
| **Proposed Rule** | "**U6 Chemical Nomenclature** (6 section codes, 4 taught) 6.1 Covalent Names & Formulas · 6.2 Polyatomic Ions · 6.3 Ionic Names & Formulas with Transition Metals · 6.4 Naming Acids & Formulas · 6.5 — RETIRED, never reused · 6.6 — RETIRED, never reused". Plus a dated decision-log entry. |
| **Supersedes** | `courses/chemistry/DECISIONS.md`, Curriculum map, U6 line. |
| **Reason** | Matt reworked the unit while building the Unit 6 roadmap page and guided notes. Old 6.1 Ions & Ionic Compounds and 6.2 Ionic Names & Formulas fold into the new 6.3; old 6.3 Transition Metals is the new 6.3; old 6.4 Polyatomic is the new 6.2; old 6.5 Covalent is the new 6.1; old 6.6 Acids is the new 6.4. Unlike U1 and U3, the codes 6.1–6.4 change meaning rather than retire, because Matt numbered the new sections 6.1–6.4. |
| **Affected Agents** | Overseer (code check), Designer, Librarian (Drive folders). |
| **Affected Skills** | None state U6 sections. The legacy installed `shull-chemistry-guidelines` skill was edited in the 2026-11-19 cloud session; it is not authoritative (CLAUDE.md §2). |
| **Affected Courses** | Chemistry only (Path A content, recorded as a record because the decisions file is only changed against an approval). |
| **Risk** | Low in the repository. Medium on Drive: if `Section 06.x` folders already exist under the old titles, the Librarian must rename them before anything is filed. Not checked; this session has no Drive access. |
| **Recommendation** | Approve. |
| **Decision** | Approved by the user in chat, 2026-11-23: "Yes, update it (Recommended)", answering "WorkWork's chemistry decisions file still lists the old 6 Unit 6 sections. OK to update it to your 4 sections (6.1 Covalent, 6.2 Polyatomic, 6.3 Ionic w/ Transition Metals, 6.4 Acids)?" Recorded by the main session (§4.1). |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `9acfddc` (curriculum map U6 line + decision-log entry). Applied by the main session in the 2026-11-23 cloud session; the Secretary agent was not available there as a sub-agent. Review before merging to main. |
| **Verified** | Yes. `scripts/validate_codes.py` before and after: Chemistry 90 → 88 valid section codes (6.5, 6.6 retired), no new warnings. `templates/unit-roadmap/build_unit_roadmap.py` reads exactly 6.1–6.4 from the file. Drive folders not checked (no Drive access). |

## Open question (not part of this record)

A U6 short title for filenames. None is added: CHG-0041 adds a row only when Matt approves one.
Until then U6 unit-level files carry no topic (`Unit 6 Roadmap.pdf`). Suggested: `Nomenclature`.
