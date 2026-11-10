# SHULL-CHG-0061 — Retired Chemistry section 1.4 is still listed as live

> No conflict with a LOCKED rule (none known), but the Chemistry decisions file contradicts itself
> (retired at lines 26 and 365-372; listed at line 352).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0061 |
| **Date** | 2026-11-08 |
| **Source** | Janitor finding, weekly sweep 2026-11-08 |
| **Current Rule** | `courses/chemistry/DECISIONS.md` line 352, Short titles table: row "1.4 \| Isotopes". Same file lines 26 and 365-372: 1.4 is retired. `standards/NAMING.md` line 57: worked example "1.4 Slides - Isotopes.pptx". `templates/slide/decks/chem_u01_s01.4_isotopes.json` still exists. |
| **Proposed Rule** | Remove or annotate the 1.4 row in the Short titles table (Matt decides which). Replace the NAMING example with a live code, for instance "1.5 Slides - Average Atomic Mass.pptx". |
| **Supersedes** | `courses/chemistry/DECISIONS.md` line 352, in part; `standards/NAMING.md` line 57, in part. |
| **Reason** | A retired code shown as live in a table and in a standards example can be built against. |
| **Affected Agents** | Secretary (edit). Designer (reads the Short titles table). |
| **Affected Skills** | None found this run. |
| **Affected Courses** | Chemistry. |
| **Risk** | Low. |
| **Recommendation** | Approve the NAMING example swap. Ask Matt on the table row. |
| **Decision** | Approved by the user via the Secretary's Desk, 2026-11-08T22:43:25.887Z. Still open — Questions for Matt, not answered by the click: (1) Remove the 1.4 row, or keep it annotated "retired"? (2) Delete the orphan deck spec `chem_u01_s01.4_isotopes.json`, or keep it as history? Answered in chat 2026-11-08 (Q1 and Q2): "Mark it 'retired' (Recommended)" — option text: "Keeps the history; the orphan deck spec stays as history too" |
| **Status** | **APPROVED** |
| **Implemented By** | |
| **Verified** | |

Drive verification is deferred: no Drive access this run. Whether a "1.4 Slides - Isotopes.pptx" exists
on Drive was not checked.
