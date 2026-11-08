# SHULL-CHG-0058 — Built Geology U1 section codes are offset from the Geology roadmap map

> **BLOCKING.** CLAUDE.md section 3 case: a built artifact carries a `U#/S#.#` code that does not match
> the course `DECISIONS.md`. **Not a conflict with a LOCKED rule** (none known). It is a conflict
> between built material and the decisions file, which wins by precedence.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0058 |
| **Date** | 2026-11-08 |
| **Source** | Auditor/Researcher finding, weekly sweep 2026-11-08 |
| **Current Rule** | See section 1. |
| **Proposed Rule** | See section 2. Nothing is adopted until Matt answers. |
| **Supersedes** | Nothing yet. If Matt chooses to renumber, the answer supersedes the section codes in `templates/notes/specs/geo_u01_s01.2-s01.4.json`. If Matt says the roadmap is wrong, it supersedes `courses/geology/DECISIONS.md` lines 19-21 (that would be a LOCKED/confirmed-status check for the Secretary). |
| **Reason** | See section 1. The built U1 material uses a shorter code list than the roadmap map, so a section code means different content depending on which source is read. Logged in `reports/drive-operations/2026-09-16f_geo-u1-file-relocation.md` lines 36-40 and `change-log/CHANGELOG.md` line 152, but never put in Geology open questions, so no one is asked to resolve it. |
| **Affected Agents** | Designer, Librarian (footers, filenames, folder codes); Auditor. |
| **Affected Skills** | Notes and worksheet build skills that read the spec files (not checked this run). |
| **Affected Courses** | Geology. |
| **Risk** | High if left. Packets can print with the wrong footer. Low for the record itself (it adds an open question only). |
| **Recommendation** | Approve adding Geology open question 7. Do not build further Geology U1 material until Matt answers. |
| **Decision** | PENDING. Questions for Matt, unadopted: (1) Renumber the built U1 material to the roadmap codes, or is the roadmap map wrong? (2) Is the Red Shift Gizmo a named exception to the no-Gizmo-in-new-material rule (open Q2), or should it be replaced? (3) Does Geology use phases at all? |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

Drive verification is deferred: no Drive access this run. The filed worksheet's footer and Drive folder
were read from repo reports, not from Drive. Re-verify on Drive before any rename or move.

---

## 1. Current state — evidence

| Source | What it says |
|---|---|
| `courses/geology/DECISIONS.md` lines 19-21 | Map: 1.1 The Big Bang; 1.2 Formation of the Universe & Early Stars; 1.3 Scale of the Universe; 1.4 Formation of a Solar System; 1.5 Our Star. |
| `templates/notes/specs/geo_u01_s01.2-s01.4.json` lines 28-31 | S1.2 Big Bang Theory; S1.3 Nebular Theory; S1.4 The Sun. |
| Filed `GEO_U1_S1.2_RedShift_Gizmo_Worksheet.docx` | Footer `GEO-U1 / S1.2`; Drive folder `02..01.2`. Same offset. |
| Spec lines 64 and 229 | Print Gizmo activity text. `courses/geology/DECISIONS.md` lines 141-149, open question 2: no Gizmo in new material. |
| Spec line 9 | Kicker prints "PHASE 01". Geology decisions define no phases. Raised in the 2026-09-24 audit, row 5, still unresolved. **Repeat.** |

## 2. Proposed Rule (for Matt's decision, not adopted)

Add to `courses/geology/DECISIONS.md` open questions, as question 7: "Built U1 section codes
(S1.2 Big Bang Theory, S1.3 Nebular Theory, S1.4 The Sun) do not match the roadmap map (1.1-1.5).
Which is correct?" Sub-items: Red Shift Gizmo exception or replacement; whether phases exist.

Until answered: no further Geology U1 builds (CLAUDE.md section 3).

## 3. What this does not do

- It does not renumber any file, spec, or Drive folder.
- It does not touch the Gizmo text or the PHASE kicker.
- It does not decide which source is right.
