# SHULL-CHG-0057 — A Snow Day folder under each course holds snow-day assignments

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0057 |
| **Date** | 2026-11-05 |
| **Source** | User, 2026-11-05, answering the question of where the six snow-day Docs belong. Verbatim: *"snow day folder under each course"*. |
| **Current Rule** | `standards/DRIVE_ARCHITECTURE.md` §1 and §2: files are routed Course → Unit → Section. A snow-day assignment has no unit or section, and rule 4 says to ask rather than default to a misc folder. |
| **Proposed Rule** | One `Snow Day` folder directly under each course folder, sibling of the Unit folders. Snow-day assignments and their keys are filed there. |
| **Supersedes** | Nothing. It adds one recognised course-level folder. SHULL-CHG-0035 (no system-created content folders) is unchanged: the user created these folders. |
| **Reason** | The 2026-10-28 snow-day builder (`templates/snow_day/`) produced six Docs with no unit or section. They sat in the Upload Inbox unfiled. |
| **Affected Agents** | Librarian (a new destination to route to). |
| **Affected Skills** | `shelve-drive-file` routes by the architecture standard; no edit. |
| **Affected Courses** | Chemistry, Physics, Geology. |
| **Risk** | Low. A new folder; nothing renamed. |
| **Decision** | **Approved by the user, 2026-11-05**, in the main session: "snow day folder under each course". |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | Secretary, 2026-11-05 (commit in the PR carrying this record) |
| **Verified** | 2026-11-05. Folders created and the six Docs moved by `update_file` (IDs kept); an independent `parentId` search shows each Doc in its course's folder. |

## Drive operation

Created by the Librarian with the user's approval. Prior parent of every Doc: Upload Inbox
(`1ZDu0cSY2GKMspyboYQUH4t460p1_FYFy`). Rollback: `update_file` parentId back to the Inbox.

| Course | Snow Day folder ID | Files moved (ID) |
|---|---|---|
| Geology | 15Vc5BYsGDip1C_q-lprePqEHlRbZWI0u | Snow Day Activity - Lake Effect Snow (1b5iyxbmp6aSmVn_VybUOtsjO4GeY3dV0ssYJE5zv8_8); Snow Day Activity Key - Lake Effect Snow (1KTkpd2GCsAZQL-Fv-jkIh4xh67r1NUOtcvHvorMApW0) |
| Chemistry | 1hA6aWnJ5IoKDmdvKnHelfj1mlr1ewv0c | Snow Day Activity - Why Salt Melts Road Ice (18YEFKV_r2mi1INMusiqg15VPG_EVm3Ri3jNTU4_jBwo); Snow Day Activity Key - Why Salt Melts Road Ice (1iKQBh2ewjWxmO5XFJrCKiAkXmqFrqO8U7zVp82Cf1Io) |
| Physics | 141OLqJPb-Q0ITxhIXiM0t5E03P7WSQNU | Snow Day Activity - The Physics of Sledding (1L9n5_P-bRTtCvR-DhXh9Z9KGdcUYfpclwA3nqkL4HFg); Snow Day Activity Key - The Physics of Sledding (1_mIVvlEb7O3JbD3TxQpitirxTQ5JTWg4tnDfC2ce0Xo) |

## Left open

- The six are native Google Docs (the 2026-10-28 upload converted them), not .docx. They keep their
  names, which are not section-led; no rename was asked for.
