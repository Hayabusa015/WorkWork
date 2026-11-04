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

## Result

**Executed 2026-11-04 and verified.** 28 files uploaded to Upload Inbox with the `drive.file` token (scope unchanged), each Drive md5 matching the local file, then moved to Quiz with connector `update_file` (`parentId`). IDs are unchanged by the move. Verified afterwards by a `parentId` search: Quiz lists all 28 (plus the existing 2.2 quiz files, untouched), and none of the 28 remains in Upload Inbox. Nothing overwritten, renamed, trashed or deleted.

| File | ID | Bytes |
|---|---|---|
| `Unit 2 Study Guide Key.docx` | `1L6KCyIt6VaFQzssBl1Py9dV5qlFcaYzo` | 1,564,957 |
| `Unit 2 Study Guide Key.pdf` | `1uV0jqE1r_AITZM4q0fZ52X0zp-z1ihKE` | 651,007 |
| `Unit 2 Study Guide.docx` | `1NoUB3S8fWFDt5QRCFZik_R1-5T1hCHR9` | 40,882 |
| `Unit 2 Study Guide.pdf` | `1Tx09BnPmzr0CUzoCfBqpLrY14sn4LBLq` | 61,326 |
| `Unit 2 Test A - Day 1 Multiple Choice.docx` | `1tZYz9aY9UsswOTMczCrQGCz89fMuEUhO` | 42,692 |
| `Unit 2 Test A - Day 1 Multiple Choice.pdf` | `1KSMpbsseh_CTDlkt0qQ3S7PgaMsqBa_y` | 115,536 |
| `Unit 2 Test A - Day 2 Written.docx` | `1y5SQB3PCUJL4cwvuOgf1mE4xxMsOZO_Z` | 40,140 |
| `Unit 2 Test A - Day 2 Written.pdf` | `1JalQDwVSo0-mR0K9n6HNxlXJE0CM0loH` | 44,713 |
| `Unit 2 Test A Key - Day 1 Multiple Choice.docx` | `1k8jILuXN4pM-040D1EltQVUr5YfpKe_g` | 41,852 |
| `Unit 2 Test A Key - Day 1 Multiple Choice.pdf` | `1DtiGyaOPddx1E84QOHEmoZ3z8uE77TQe` | 89,949 |
| `Unit 2 Test A Key - Day 2 Written.docx` | `1--lgtSVuWgLl0w4FRN4X8T_ZQGw1VvAn` | 1,656,516 |
| `Unit 2 Test A Key - Day 2 Written.pdf` | `1zm-tqCYalNnCbpQktJqR-JfQShwhD0qC` | 688,518 |
| `Unit 2 Test B - Day 1 Multiple Choice.docx` | `1e_CyX2BKmr7498ykjQpYZ-K3eXfOOIkT` | 42,669 |
| `Unit 2 Test B - Day 1 Multiple Choice.pdf` | `1j1xbH_qhyLwOX7CPnFB37vkDuUxHlGsJ` | 115,025 |
| `Unit 2 Test B - Day 2 Written.docx` | `1eWRSFOrtW805o9gP9DnrIvCDAEiSYPHw` | 40,105 |
| `Unit 2 Test B - Day 2 Written.pdf` | `100_0U-w8lSA7oCi-ZHIR-r5wTmN5Y7DP` | 44,912 |
| `Unit 2 Test B Key - Day 1 Multiple Choice.docx` | `1gVxAQFKjp1IFJLWNxc3TmKhEOzHHeMil` | 41,868 |
| `Unit 2 Test B Key - Day 1 Multiple Choice.pdf` | `1UG_xTtHqfcj0PkTZJaN-sAZZpDF37E1u` | 89,912 |
| `Unit 2 Test B Key - Day 2 Written.docx` | `1FxRvGNR4rqszVqgwxlMnBcIYF5ZnmGhJ` | 1,690,561 |
| `Unit 2 Test B Key - Day 2 Written.pdf` | `19MGHe8BSv3phK-f_pNNXoPPk_rfe6vmG` | 700,139 |
| `Unit 2 Test C - Day 1 Multiple Choice.docx` | `1-D7bg6x5bb60f0lG08d2Mc8BJspDG4g6` | 42,778 |
| `Unit 2 Test C - Day 1 Multiple Choice.pdf` | `1K3Psea-8ASpSeyZUGtI95FZLbVdFexMO` | 115,569 |
| `Unit 2 Test C - Day 2 Written.docx` | `16ftxX_FvparJ55YeYuwcedL86ZaZLGgB` | 40,114 |
| `Unit 2 Test C - Day 2 Written.pdf` | `1Xd0XWcT80twRq0Q0MEsrR4RUS6RTJZtv` | 44,615 |
| `Unit 2 Test C Key - Day 1 Multiple Choice.docx` | `1iOp1yrIZWrtBk0gtEVZl8zlTCN0NCtWU` | 41,847 |
| `Unit 2 Test C Key - Day 1 Multiple Choice.pdf` | `1NKTwGtBpjcDFLO-02i-LrZkuOEJ-t-O0` | 90,072 |
| `Unit 2 Test C Key - Day 2 Written.docx` | `1oU77wZpFrnEhBmV-_zoj_c3JaMCABy-r` | 1,685,554 |
| `Unit 2 Test C Key - Day 2 Written.pdf` | `15wgHXuLmscxsA4GLoZsHy3VOY3v9w-us` | 698,324 |
