# SHULL-CHG-0051 — SHULL-CHG-0010 header Status contradicts its own resolution

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0051 |
| **Date** | 2026-10-22 (first raised in the 2026-10-18 weekly sweep) |
| **Source** | Janitor (2026-10-18 weekly sweep). Re-checked against the repository on 2026-10-22. The "REPEAT" tag was not verified here. |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | See section 2. |
| **Supersedes** | `governance/proposals/SHULL-CHG-0010-lab-template.md` line 15, the header Status value. |
| **Reason** | Claim VERIFIED as still true. The header table says PARTIALLY IMPLEMENTED; the closing table at line 136 says IMPLEMENTED. The record's own RESOLUTION (lines 99-125) says Finding 1 is closed and Finding 2 is resolved, so nothing remains open. The Secretary's Desk export reads the first Status it finds, so the desk shows 0010 as partially implemented. |
| **Affected Agents** | Secretary (applies it); Janitor. |
| **Affected Skills** | None. |
| **Affected Courses** | None. |
| **Risk** | Low |
| **Recommendation** | Approve. This edits an implemented record's status field, which is history, so it needs approval rather than a quiet fix. |
| **Decision** | Pending. |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | No |

---

## 1. Current Rule — verbatim

`governance/proposals/SHULL-CHG-0010-lab-template.md` line 15:

> | **Status** | **PARTIALLY IMPLEMENTED** |

`governance/proposals/SHULL-CHG-0010-lab-template.md` line 136:

> | **Status** | **IMPLEMENTED** |

Note that `PARTIALLY IMPLEMENTED` is not one of the five statuses in `governance/CHANGE_CONTROL.md`
section 3 or in `schemas/change-proposal.schema.json` (line 28).

## 2. Proposed Rule

Change line 15 to `| **Status** | **IMPLEMENTED** |`. Nothing else in the file changes. The duplicate
Status and Verified rows at lines 134-137 stay as history.

If the user reads the Resolution as leaving something open, the alternative is to change line 136 to
match line 15 instead. The Secretary's reading is that nothing is open.
