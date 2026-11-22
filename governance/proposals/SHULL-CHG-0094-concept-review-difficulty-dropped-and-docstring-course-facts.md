# SHULL-CHG-0094 — Concept Review page and difficulty ratings keep being dropped; course facts sit only in docstrings

Repeat of: the same correction twice (Chem U3 2026-11-03, Geo U3 2026-11-09), for both the
Concept Review page and difficulty ratings

> Propose only. Part A is a Path B question for Matt. Parts B and C are course records that the
> Secretary drafts only after Matt confirms. No conflict with a LOCKED rule is known.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0094 |
| **Date** | 2026-11-22 |
| **Source** | Researcher finding, weekly sweep 2026-11-22 (`reports/2026-W47/researcher.md` row 6) |
| **Current Rule** | `.claude/skills/build-document/SKILL.md` line 124: "Each section in the checklist carries a **1–10 difficulty rating**. It is a standard cover feature". Line 132: "The packet closes on a **Concept Review** page." |
| **Proposed Rule** | A: Matt decides whether the Concept Review page and difficulty ratings become optional (default off) or stay standard, with the two packets treated as one-offs. B: a Geology decision-log entry records the U3 teaching order 3.1, 3.5, 3.2, 3.3, 3.4. C: the Chemistry 3.6 melting/boiling-point mapping is added to the Chemistry open questions. |
| **Supersedes** | A, if optional: SKILL.md lines 124 and 132, in part. B and C supersede nothing. |
| **Reason** | Both features were dropped in two of the last three packets. `make_chem_u03_notes.py` (2026-11-03) says "no concept review page" and that difficulty ratings are left for Matt. `make_geo_u03_s03.1-s03.5_notes.py` lines 15-17 (2026-11-09) say "No Concept Review page (Matt hands the unit review out separately) and no difficulty ratings (Matt, same date)." The same docstrings hold course facts that are not in DECISIONS. Chem: "3.6 is a mapping for Matt to confirm" (line 16). Geo: "Section order is the deck's, by Matt's direct instruction (2026-11-09): 3.1, then the rock block as 3.5, then 3.2, 3.3, 3.4", while `courses/geology/DECISIONS.md` lists 3.5 Rock Cycle last with no sequencing note. |
| **Affected Agents** | Secretary (skill; course entries once confirmed), Builder. |
| **Affected Skills** | build-document. |
| **Affected Courses** | All three (A). Geology (B). Chemistry (C). |
| **Risk** | Low. Builders follow the skill and will keep adding a page Matt removes. |
| **Recommendation** | Ask question 1. Draft B and C as Path A course records only if Matt confirms them. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

## Open question

1. Should the Concept Review page and difficulty ratings be optional, default off, or were these two
   packets one-offs?
2. Should the Geology U3 teaching order (3.1, 3.5, 3.2, 3.3, 3.4) be recorded in
   `courses/geology/DECISIONS.md`?
