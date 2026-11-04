# Drive operation log — PHYS U02 unit tests (Day 1 MC, Day 2 written, versions A-C), study guide, keys

**Logged:** 2026-11-04, BEFORE execution · **Task:** Matt asked for the Physics Unit 2 study guide and tests, then
"run the auditor and file everything to Drive", filing once the audit passes. Auditor verdict: PASS WITH FIXES
(sig-fig and notation fixes in the keys, applied and rebuilt; report at the session scratchpad `audit_u2.md`).

## Destination

`Physics / Unit 02 - Motion in Two Dimensions / Quiz` — `1cRsw2mysBKPAUjqDmEJE_fGGS4Zg9LBW`
(parent `1rB4t-tF-PygDHIFFQBleIpHV4GHJYBve`, verified 2026-11-04). Unit tests and their keys are unit-level (SHULL-CHG-0030).
The study guide has no folder of its own in `standards/DRIVE_ARCHITECTURE.md`; it is test preparation, so it goes in
`Quiz` beside the tests. Matt can have it moved to Guided Notes by one `update_file` if he prefers.
The Quiz folder holds 22 files at this time, none with these names (no collision, nothing overwritten).

## Operations (all creates; no rename, trash, overwrite or delete)

| # | Operation | Tool | Detail |
|---|---|---|---|
| 1 | upload 28 files into Upload Inbox `1ZDu0cSY2GKMspyboYQUH4t460p1_FYFy` | Drive API, `drive.file` token (scope unchanged) | each file already carries its final name; md5 checked against the local file |
| 2 | move each to Quiz `1cRsw2mysBKPAUjqDmEJE_fGGS4Zg9LBW` | connector `update_file` (`parentId`) | prior parent of every file: Upload Inbox; rollback: move back |

Files (a .docx and a .pdf each, names per `standards/NAMING.md`, unit-level, no short title exists for Unit 2):
`Unit 2 Test A/B/C - Day 1 Multiple Choice`, `Unit 2 Test A/B/C Key - Day 1 Multiple Choice`,
`Unit 2 Test A/B/C - Day 2 Written`, `Unit 2 Test A/B/C Key - Day 2 Written`, `Unit 2 Study Guide`, `Unit 2 Study Guide Key`.
The two bundle zips made for review are not filed.
