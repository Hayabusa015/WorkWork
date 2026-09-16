# Drive operation log — Geology + Physics retrofit to SHULL-CHG-0024

**Logged:** 2026-09-16 · **Agent:** Librarian
**Task:** Retrofit Geology (all 10 units, 54 sections) and Physics (9 units built today — 00, 02-10,
44 sections) from the SHULL-CHG-0023 grammar to SHULL-CHG-0024: add a unit-level `Quiz` folder,
migrate `Tests-Quizizz` file contents into it, eliminate the `Homework` folder by migrating its file
contents to the loose Section folder, leave `Labs-Case Studies-Projects` untouched.
**Physics Unit 01** (`1_ykbQae1GAKi0hWFn-OWIdvVAWXwc_6D`) — not opened, not modified (separate task).
**Chemistry** — not touched (separate task).

## Authorisation, independently verified before acting

Per this agent's own standard — never act on a relayed claim without checking it directly:

- `standards/DRIVE_ARCHITECTURE.md` read directly: already carries the SHULL-CHG-0024 grammar (`Quiz`
  unit-level, `Labs-Case Studies-Projects` the only section-level folder, no `Homework` at any level).
- `config/drive.json` read directly: `folderGrammar.unitContentFolders` = `["Guided Notes",
  "Presentations", "Quiz"]`, `folderGrammar.sectionContentFolders` = `["Labs-Case Studies-Projects"]`,
  `homeworkFiling` key present and matches.
- `governance/proposals/SHULL-CHG-0024-quiz-unit-level-no-homework-folder.md` read directly: Decision
  "Approved. Matt, direct instruction, live conversation, 2026-09-16."
- Git internals read directly (`.git/logs/HEAD`, `.git/refs/heads/claude/gracious-galileo-drxzqh`):
  branch head is exactly `07fc50965ed5ddbb7c4ac7f1eaca7cd5e1281a25`, log entry "commit: Record
  SHULL-CHG-0024: Quiz to unit level, no Homework folder" — matches the relayed SHA and branch name.

Verified independently. Proceeding.

## Prior state

19-or-20 units in scope, see note below — 10 Geology + 10 Physics units actually exist and were
in scope; 98 sections (54 Geology + 44 Physics), each built minutes/hours earlier today under the
SHULL-CHG-0023 grammar: 2 unit-level folders (`Guided Notes`, `Presentations`) + 3 section-level
folders (`Homework`, `Tests-Quizizz`, `Labs-Case Studies-Projects`). Full IDs for the Geology
unit-level folders and the original 108 pre-SHULL-CHG-0023 section folders are in
`2026-09-16b_geo-retrofit-shull-chg-0023.md`; the Physics build is in
`2026-09-16c_physics-build-shull-chg-0023.md`.

## Note on unit count: 20 built, not 19

The task brief said "Physics: the 9 units you built (00, 02–10)" — but 00, 02, 03, 04, 05, 06, 07,
08, 09, 10 is **10** distinct unit numbers, not 9. This is the same off-by-one already flagged in
`2026-09-16c_physics-build-shull-chg-0023.md` ("task brief's unit count"). A `parentId` search on
the Physics root confirmed 10 Physics unit folders exist beyond Unit 01 (00, 02–10), matching the
44-section total the brief itself states (4+3+7+4+3+3+5+3+6+6 = 44, which only works with 10
units). Geology has 10 units. **Total units actually retrofitted: 20 (10 Geology + 10 Physics),
not 19.** 20 `Quiz` folders were created and verified — one per unit that actually exists in scope.
Flagging this rather than silently building to the "19" the brief asserted.

## Plan (logged before execution)

1. Create one `Quiz` folder as a sibling of `Guided Notes`/`Presentations` in each of the 20 units.
2. Per section: list `Homework` folder contents (paginating with dedupe by file ID if needed), move
   every file found directly into the Section folder via `update_file` (new `parentId` = Section ID).
3. Per section: list `Tests-Quizizz` folder contents (same pagination caution), move every file found
   into that unit's new `Quiz` folder via `update_file`.
4. Independently re-verify (fresh `parentId` search) that every `Homework` and `Tests-Quizizz` folder
   in scope is empty afterward.
5. Leave `Labs-Case Studies-Projects` untouched at every section.
6. No trashing performed by this agent (no trash tool available to this session) — empty
   `Homework`/`Tests-Quizizz` folders are logged below for the orchestrating session to seek approval
   and execute trashing separately.

## Step 1 — 20 `Quiz` folders created, verified

Created as a direct child of each unit folder (sibling of `Guided Notes`, `Presentations`, and the
Section folders). Verified by fresh `parentId` search on two units (Geology Unit 01, Physics Unit
00) confirming `Quiz` sits alongside `Guided Notes`/`Presentations`/Sections, not inside any of them.

| Course | Unit | Quiz folder ID |
|---|---|---|
| Geology | 01 - The Universe & Solar System | `1NUPLYgUeRNgt6NL9cUL_6r02YpJ54jAF` |
| Geology | 02 - Geologic Time | `1Uh27Il551PgSLZWL3FUo4i-6mN0vc6nX` |
| Geology | 03 - Rocks & Minerals | `12bkr9qOamCSjBBF8lIW2AaX15jpIgXMB` |
| Geology | 04 - Plate Tectonics | `1QHXv5XFcchSDD4oRaumMi4f6oQNBH8Xr` |
| Geology | 05 - Volcanoes | `1jLqjXRxWpYO0MbmmwHCTE_I6sJzBjacY` |
| Geology | 06 - Earthquakes | `1Jodk1rj1esSl0lWmWaFQRZoVBg1cfq6p` |
| Geology | 07 - Caves | `1pxqajIeEUZ_5TjY0QriuB0xCvtdL4jHt` |
| Geology | 08 - Glacial Geology | `16KifwdQAPD3GFDQEOKKgPqSDUdhzDfBf` |
| Geology | 09 - Oceans & Climate | `1aUZ24pi7Bf_MkBzqKMoHIDF6D6lkoFqs` |
| Geology | 10 - Earth's Resources | `1GuWPLCBf5TJezitEnj40VMzw9iwZyqGl` |
| Physics | 00 - Physics Math Review | `1sMc9IVkvLaP19vd2s8p8faDry4BaLvCb` |
| Physics | 02 - Motion in Two Dimensions | `1cRsw2mysBKPAUjqDmEJE_fGGS4Zg9LBW` |
| Physics | 03 - Forces and Motion | `1MnuIBURUxh2z0MGJ6WgQl3ub1zspB_6o` |
| Physics | 04 - Work, Energy & Power | `1Nj69K4SK6cR0s57uwIW3CzKxPlarDssU` |
| Physics | 05 - Momentum & Impulse | `1iIFzPQabwfFzOgw0pAv1uniSmiRqtdQ7` |
| Physics | 06 - Circular Motion & Gravitation | `1prnJkHmxjX4exfJyzQYXnhJw3WSIanoC` |
| Physics | 07 - Waves | `1rlEQ0ZWeyqvJ5hTUbyQw3vVmlGnv7HU-` |
| Physics | 08 - Optics | `15r2uhXis6dx9V0ltFmLjqhb5ZDoinbrO` |
| Physics | 09 - Electricity & Magnetism | `1FnZ9o7IFZct-oRWBrCZ2OJKNYJq3QRSq` |
| Physics | 10 - Nuclear & Modern Physics | `1SDyxXh5LcEgroSiZrsTpqmRiC4JbaQ-9` |

## Step 2 — every section's `Homework` and `Tests-Quizizz` folder listed and checked

All 98 sections (54 Geology + 44 Physics) had their `Homework` and `Tests-Quizizz` subfolder IDs
retrieved by a `parentId` search on the Section folder, then each of those 196 folders was listed
directly (`parentId` search on the Homework/TQ folder itself) to check for files. No folder returned
more than one file in any response — pagination/dedupe was not triggered in practice, but every
listing was still an independent, fresh query, not an assumption.

**Result: 194 of 196 folders were empty, exactly as expected. Two were not** (both `Homework`, both
in Geology Unit 01) — see below. **All 98 `Tests-Quizizz` folders, in both courses, were empty; zero
files were moved into any `Quiz` folder.**

## Exception found: two non-empty `Homework` folders (Geology 01.1, 01.2)

Contrary to the task's stated expectation that nothing had been filed since these folders were built,
two contained one real file each:

| Section | Homework folder ID | File found | File ID |
|---|---|---|---|
| Geology 01.1 - The Big Bang | `1jivuBFMG9b63mLzEwQ3oYYfg3ytvr6V4` | `GEO_U1_S1.2_RedShift_Gizmo_Worksheet.docx` | `1R3xSaEU-SNfn6bwIMvinwiE6erGMWi5Q` |
| Geology 01.2 - Formation of the Universe & Early Stars | `15fMFp7rCs9gsDi499pf4pwbzpcWfQb9q` | `GEO_U1_S1.3_NebularTheory_CutGlue_Timeline.docx` | `1wvGpz507BotmSCkXN8GvdLdsuIScf5u6` |

**Naming/location mismatch flagged, not resolved by this agent:** each filename cites the section
*after* the one whose `Homework` folder it was sitting in (a file named `S1.2` was in `01.1`'s
`Homework`; a file named `S1.3` was in `01.2`'s `Homework`) — a one-section offset. This could be a
genuine misfile from whatever process populated these two folders, or the filenames could be wrong.
**This agent did not guess which is correct.** Per this task's instruction — move whatever is found
in a section's `Homework` folder into that same section's folder — both files were moved to the
Section folder matching their **current parent's section**, not their filename. Matt should check
both filenames against their new location (Geology 01.1 and 01.2 respectively) and rename or move
again if the content doesn't actually belong there.

Both moves executed via `update_file` (reparent, ID preserved) and independently verified by a fresh
`parentId` search on both destination Section folders (files now present there) and both source
`Homework` folders (now empty):

- `1R3xSaEU-SNfn6bwIMvinwiE6erGMWi5Q` → new `parentId` `11wZLJrE72jHKRFidfJ9_PK5qogJqlwmZ` (Section
  01.1), confirmed. Old `Homework` folder `1jivuBFMG9b63mLzEwQ3oYYfg3ytvr6V4` confirmed empty.
- `1wvGpz507BotmSCkXN8GvdLdsuIScf5u6` → new `parentId` `18rWs7VKd8-cEg1RS3sCrRZ_HOFIZuO7n` (Section
  01.2), confirmed. Old `Homework` folder `15fMFp7rCs9gsDi499pf4pwbzpcWfQb9q` confirmed empty.

After this move, all 196 `Homework`/`Tests-Quizizz` folders in scope are confirmed empty.

## Full table — 196 confirmed-empty `Homework`/`Tests-Quizizz` folders, ready for trash approval

Every ID below was independently verified empty (by the checks above, including the two exceptions
after their file was moved out). None has been trashed — no trash tool is available to this agent
(see prior reports for the same limitation). Awaiting the orchestrating session's request for
Matt's approval and execution.

### Geology (54 sections x 2 = 108 folders)

| Unit | Section | Homework ID | Tests-Quizizz ID |
|---|---|---|---|
| 01 | 01.1 | `1jivuBFMG9b63mLzEwQ3oYYfg3ytvr6V4` | `1Ks38SOi8zW0TetFQbNCVgvWN7asmPc7Q` |
| 01 | 01.2 | `15fMFp7rCs9gsDi499pf4pwbzpcWfQb9q` | `1iWPqzeHBUOuXaB-uYTAmLVGU1nd08Wfz` |
| 01 | 01.3 | `1cxbKI07fw22rRKRHZZHOgiYLii1No-l1` | `1V1PudMCN920oSdmVBjqm5ZwNCpig8-FF` |
| 01 | 01.4 | `1pETRHRDmwPqlvByY9nPXCfy98Er_Vmmy` | `1_stxOxr5ypqSulhE0NzN3u7tSqi3o0YE` |
| 01 | 01.5 | `18mTVTRiyIrEL6pumBJ_9gzB6z-iLT-n4` | `1S9MhLbYdfeLEsvNuahurarIGcGN_QMDH` |
| 01 | 01.6 | `1AFERlfgOX3Pvmb5PPDSBaEvF5ZX0Jj2h` | `14gaDidHT8GVc2umQPuM4qnTVKwlZQJwC` |
| 02 | 02.1 | `1tdddhP6iEt_2wnm10mR9S4JDzk5dAkwZ` | `1GhNoYEQ3Axq83Iha4A8NwAm1kHCpxkfp` |
| 02 | 02.2 | `1nUxXCafReTrf32zmFtHyzlqG8CNslFBT` | `1YBpTEuJj8cGo3dl7ELmemO5K3T5I_tDY` |
| 02 | 02.3 | `1QaIt4NOYZpmRIs4f1jMpROeWMYFVB4Pa` | `1kUDpE61Vw16BTJs1UtMSzfayfzYV60WB` |
| 02 | 02.4 | `1MTorJAdHEgzFKAGoUTJzk5IJqGKb63IE` | `1cyqZzW7ZjFfa_2GjgXczExr7x9zY6nmb` |
| 02 | 02.5 | `1n8SIOk46sA7CJ0BTB95y2jGmJzFhBkUc` | `1jndscUY4JWAu-Eo_9KhrnzNPuNHj7IME` |
| 03 | 03.1 | `1bg4Pu1l7xd3xt4k1-zLoYpY_1N-BAL4o` | `1Y8DvKKPl05i1KDhLtUx1tfNUKfBxLbJR` |
| 03 | 03.2 | `1v4acn_YTwu8qeCinSObN4wL-azQ1kyNi` | `1iAHmH2K9ff2Dtr-y7QmUTkK9aJtkDeu-` |
| 03 | 03.3 | `10e8pCzGKNpK08-_Eq2YoQ-DhrnS8kUQi` | `1i2viBHCnH5lQqlGFdQ7UumXM-Qlta-Bm` |
| 03 | 03.4 | `1oYK-gQnF27fiFxBj-e4Fo3XQTpk4BR5k` | `1QRXFhr1RmDZ2KfX3YTu-9dmFaiXco7GG` |
| 03 | 03.5 | `10bfRjtR39NxpvWQlaxjXV1T5oGYWmyvi` | `1eE9npwlczbmGDgBhVaRgk5eaDc6cpQ8u` |
| 04 | 04.1 | `1-HfrSHuOCY5wL_BZ2qI9yw4dQm17tKAg` | `1ji-RbL1Mvjfm40PXOJ_dC8txe8LlLiJ7` |
| 04 | 04.2 | `1C_S4f3LUf1ToYiNpjdxKQcW2ciF6S01t` | `1bhV7i9SSnzYBeXXi_TSH9uJOo0Ve9nwY` |
| 04 | 04.3 | `1IwUptWnAfpU7UMMsm6p4xteVoDl2veLL` | `1BCN9OpOvvP6px0veC_UPhzUu7Mlqn8Cw` |
| 04 | 04.4 | `1gsbxtdiqS5-PJ0a7aR-mVrByjT4euIb8` | `1ES-nUyZlGg8q9oYH-Y7VQzPVlCeEGTQN` |
| 04 | 04.5 | `1REqLo3n9u0foHU0wAMegcEZBq4qrUyWl` | `1v7HPk1KDQkivRrhSr_MzXJ3mlYdRdizN` |
| 05 | 05.1 | `1lq0kAHscWWA1Of8VEdx-Br7HRD0UcL-0` | `1Eh1HD0WHORGdNsAfXTPUPz6581-lBY3F` |
| 05 | 05.2 | `1Aw8lg4mwkCzatsY6UO08yUlJVda8n1Av` | `1UnGCk9d3ifcNz2NbL498r8i5xULVeogv` |
| 05 | 05.3 | `11H0TuiblRRS98hix4sW2_tuBrWFIFZoq` | `1er545FolCAElS7RViSlCULlocxwF3lUA` |
| 05 | 05.4 | `1q7lCRpHjdFX4kV76YWRb-ytSYIANi8cc` | `1jx13TsfdITwwiMpMEFzf5SKbHFsuGhNR` |
| 05 | 05.5 | `10JQOXrBaSK29vZ-6nbghEla2WuFBdU5W` | `1uXNNPDQMbFlFn0eulILRsqDf_47unf1x` |
| 06 | 06.1 | `1FJl6cO_h5espKPHcQsFE8psgBZal5UWQ` | `1z7vGjj4pYkcDlTCg-swKjH-Yrl9O8X2y` |
| 06 | 06.2 | `1-ImotzOoW8MMTHARqd7NTEOLN_KFUyrn` | `1VU8p6dWFMGZXby4Oq9BRfsuWgZiLhQXq` |
| 06 | 06.3 | `11S6iQ50TJLF5P22niwVWXeofYRIt-J4c` | `1JzWnudlBdxYWrTd0Z-VfbrnN0tWtyUOj` |
| 06 | 06.4 | `1yLic6FQqY1SK-pVe6nNKK-_z9tbBMRU7` | `1fnwi3or-ej6hB-sddda0Yq4n_mwW_KLG` |
| 06 | 06.5 | `1WdCCiVKdON564cHoHrfgCzuRlPGN1yod` | `1QRDi_FR3S_pIBwQzppzG7aebyTkh1QpL` |
| 07 | 07.1 | `1DC-6lBzyhHkAp4DSrOjMqhAz8o_i6wtI` | `1fvxpFB4rv5NsScwMDmCVHVALJYmebv6T` |
| 07 | 07.2 | `1QA_mO8Ph_42sKg_f-MMibsGrk4i4ZPn_` | `1Xonasn0FAMJWtwjuk2VnUzensLFMYP0L` |
| 07 | 07.3 | `1zVHLCUZWDqOGZmtOSRnoVEIfBcN8L9ge` | `1QxDqGvNa0DnFLxPgSH7By4G9H4gHYNWY` |
| 07 | 07.4 | `1r1KtQheQqJgPWoy9_FKjpVtx9B2TFPFd` | `1heMPY2AcavLryaAxtuAQb-RBCAyCbeev` |
| 07 | 07.5 | `1W4vpmjCLajrCWhw2FOaPF7WeK0GrjR6S` | `1llr0W1hACGCKX9_qErMfBIEaq29hfyUF` |
| 08 | 08.1 | `1k2IsOfH2XQL1i3k7xGykEtNbPsBz1meL` | `1q0GRLsWHoi4w3zOLWLeWKXMlIAuNc9UD` |
| 08 | 08.2 | `1nD7m4vrzIFrTbXvFAtjZAvzR_-97OZRd` | `1Zt6Yv8tdjyIT65kd_pDhH6j1l1tp9gVc` |
| 08 | 08.3 | `1m2Mq7sKtov6H88odEBTQ1BF2Z2thXXyV` | `1towhD1cpGpkkqTEi0CgiQDocPuyZwgXa` |
| 08 | 08.4 | `1cE5zCJuAzOemnMBuTJ3--o0Iw_cBvaD8` | `1ZJJaCQmXdAbhQm7Ib_92CFyGFqU8V-1C` |
| 08 | 08.5 | `1DAAFhSv3kQytZIToHF80iVAM1rYaYmx3` | `1iKfY5nqJYrWDFnZlYrR2S_TZZSQqnesk` |
| 08 | 08.6 | `1zZC7aG6vopKHMd30d52wnlzlt2_SHQ9w` | `1SCHq8BqASmpemWOehhpKuOAZvZ5fQA1-` |
| 09 | 09.1 | `18MGddd6uMro3qWUzuja7OxmfS2o3vfsI` | `13qTzZ2qrCwJD67le1pkFiTqAVXCx9dZJ` |
| 09 | 09.2 | `1aV6juFsxjzlRDgD40nY_LcBlsEEAXc7R` | `1ZhBdrNUzaV4OzljxvGNELfxr1mVNLj2S` |
| 09 | 09.3 | `1Qcq2Ei4b65XpIGFfHPDYrSn-suY_glU-` | `1QTWWFccAfBqJchYocMH-5czxk8e0H80I` |
| 09 | 09.4 | `18BhAGVnqZsEFfjOfp-3F7m9TmHl3tQvF` | `1gkTYjlv9z14D-9yBRI74DK5q80N-IsMs` |
| 09 | 09.5 | `1td4qvHKLfENK572ERDqEVa6JB5hjhea1` | `1LAogauLrf4oBu2ndPluSYhKr2xoly0ha` |
| 09 | 09.6 | `1UfpsIZr-OZ3x7uF93ALwHMSGFCqEsa7S` | `1rUjn4R_MgETLLmICIL4OqgRxZdfWDbC2` |
| 10 | 10.1 | `1i-NTX9D7le1ly1X8CjN9Ga_L_fPlIgcp` | `1Fz3ImixOnpty7lhfsxY25n-eTnl0osxE` |
| 10 | 10.2 | `121gJBrxRsJ4J0WDIwadF_KkXTE6E1-dH` | `1sQae0DI8K3i00uOYFPwc2kX5LdqMp7dz` |
| 10 | 10.3 | `1XAHMR1_YYpXV7Gu0CV4_dg6DGQb2PtXf` | `1K6oaEre5FwDcBwHJMtzqubNJDKY4_yok` |
| 10 | 10.4 | `1XK1U4nudiM6vTjcEOUuFyZ0db_vdNfB-` | `1epaIrCtbYYjrd9ugFFGPsmTqVfdiz0P7` |
| 10 | 10.5 | `1ASJetnzIsZmzp2TcfD6_WAgJe0Nzle3C` | `1xakLVQUwhpaCDQ58SRM2wCtRR5PkYJEH` |
| 10 | 10.6 | `1pre-WwR__HtqViCybE9NOEUGCF0dPM6h` | `14_ICcORp12xRunM-4oPzAukw1OuaVRO7` |

### Physics (44 sections x 2 = 88 folders)

| Unit | Section | Homework ID | Tests-Quizizz ID |
|---|---|---|---|
| 00 | 00.1 | `1zppMzLc9QU4n0KeW6Jn5bNZdd54lrzGK` | `1cz7npHJKUtAWhvS7Q828KJhvVGC3w69F` |
| 00 | 00.2 | `1_LWQAD_ZHgFulhMPAXTUZZqM52HL_L-J` | `1jA71AHfXlzMxf4qYeMocAivzS3QFq4C-` |
| 00 | 00.3 | `1q3SeyywsA_PJUgHLZmMYNSNV_0uXiTND` | `179Fm705u6Fym-UapB9XCnPm_c87Qkwiy` |
| 00 | 00.4 | `1eDL9bQ1YzQad2DQn7bNOO7GjeJQ1nxHK` | `1r9zUaz1g2uDG6YdYnW6noNCE7NhvBelQ` |
| 02 | 02.1 | `19mGwFUeUF97y-kxoaKTdc65a2z1FMUr2` | `10uy9sp4fAXd35YUfI4gd5-Fv4iojtq-j` |
| 02 | 02.2 | `1mVMpbZbAQMhoIijLHSpG86RLlcx811td` | `1npXHlgegJeeJw0ITbrjeg9L81diPCDX_` |
| 02 | 02.3 | `1G7e5pYo5ZxPfcYJ5jHHHq308QbqLZ5BI` | `1IXllLgo0SshWpWTtGZMs3BvyZqnEdpHk` |
| 03 | 03.1 | `1SWb-ptX6Q5MY6KL4rzZ8eTzPj4pwk1Uk` | `13Y_XR05CNFLyQRUWSowQwS85Tqp8Yhll` |
| 03 | 03.2 | `1wAQxsPzwLazeAQOpPFrtfNBXGQ6sCVBf` | `1wajpxZCDKGOhU_1bdEEYl1d4UWvnsDMh` |
| 03 | 03.3 | `1I1UztIiZHqLNuT1h_mpoXSBYxZfuB_Zr` | `1J4LgaQS-RSosJtoTvP-1b5zDKa4zUGtV` |
| 03 | 03.4 | `1m11MMQj7khbnEOM9ip2clj4g2ryFksgu` | `130O4NjsF-FAsZlEal5NM2lvZFpZ-TU21` |
| 03 | 03.5 | `1nRSbT7gTrQ6rr2zMH1cv2_Kw94QJWRls` | `1jmCPI1JRz4JkJONc-FJJOixZLrVZUOS8` |
| 03 | 03.6 | `1CMtYD0_uzPj6DKwdohZrgWuzEJMzKvds` | `19w6Nqg-vDC7nd1LTgbEvjvJzgH1zAvpK` |
| 03 | 03.7 | `1Zm5bTxzAu4vx2FRE9QTUiOwXOhPe9KET` | `15Uk7u5HWTpRry3N7ZtONHwqukfDFydxH` |
| 04 | 04.1 | `1e6VXsEEvA_Fe8hsmjvE5pyO0KFAVjXss` | `1JNd6JtOTQ9HpldBBc559IP9Z2W5J9bb0` |
| 04 | 04.2 | `1950OW8AS8l790yIR71Zdw6bChChB3CZ_` | `1w0W-2NSM1oTw5_c_V3rTRbOm9YJkC8oJ` |
| 04 | 04.3 | `1TIpETW6HOp8GSZpLFJZeF-nN9QbMgLG-` | `17krE821AorWF_GQ8zza9SpKh3YyKlPwJ` |
| 04 | 04.4 | `1dm7WonHvX1tNuWrkz_VDv6J4l_GGDXvH` | `14QFknqP4Kof4lLBA7y3LFAm4llvT3NqN` |
| 05 | 05.1 | `1zX5yzTiDfn_z0acrUM7iIILS_0bm4Kdx` | `1KAu6AiS08l5x9ozjOCXJzM2Clb2_8i56` |
| 05 | 05.2 | `1pudzksqBGlDPzjo5nxTw69T5ct7sDtFM` | `1tYw2qzn4y40p4wdFMuR583u1YkoAAo_T` |
| 05 | 05.3 | `1Hj1Nm-J9DPFh-mZJRIip4FwGwKauiSeR` | `1gjhgBO2ZuWeaZm-pzs5XTJNIYYct0IZo` |
| 06 | 06.1 | `1zBT46sEcsdDGyfo6ylI63SkDNb58GZUN` | `1SR4fllYMIcs5vPJeY9NnoOmFnGC2ysU5` |
| 06 | 06.2 | `1Xn9taTjXNsE86Gt26ycyeBzaiGR2H1Zg` | `1qZ5555yfvkT5Nj-VV9CGdqmUrKap9Oj2` |
| 06 | 06.3 | `1Aaoyo_Kf4Xk7dmDsv2gxFGdbDw7UbiXE` | `1y9SlV04HCmcdRedfjEiJR71axF77e2fc` |
| 07 | 07.1 | `1vo_6NSNNXQ9rAnNM5hYhaDJtMRVGsBkR` | `1rjRat9LcuFODVnqQdS116GhLIDBAan6r` |
| 07 | 07.2 | `1HasWPKGhvqcjiIQJlWRen-31iEszMlwY` | `1T33Mv-vNnb5qU4lP3umH3xLHG83-Mdqc` |
| 07 | 07.3 | `1KO79cCzAL754dmIbD9yUPzAAIp0CG9gn` | `1z4pY4FxOzybcKhcO1bw9rFJi87lC19aQ` |
| 07 | 07.4 | `1vkFX4GofonGS5U04kyQYkXj809Fxxz7M` | `19WXajQlx0aatWZlAJRkJ36UioSPws-Sk` |
| 07 | 07.5 | `1KxE45nY7jZSkCJKKxBQiQP8hkAM4pBz9` | `1ER83f5CXXksSwJCNQDtjHhGFoeY3Fo4W` |
| 08 | 08.1 | `1CdUpeOFHXfDyeLfLplk03CJ9X1RXa9Gs` | `15vfor3qbzz1G7HGdIKlrM_ezfU5gyiiS` |
| 08 | 08.2 | `17Y0rL05fqW0UG1EJNS-Nw08PkOUVOGMZ` | `1a1i4aJpuov-GPIbI3Y_JMet3qkWBgUbH` |
| 08 | 08.3 | `19RD8olPMVvqJwbsQEPwFPbtbcxIhAyAK` | `1I1R1GTJ5lF_r1xkRn9ff3G2e-TWGXGqO` |
| 09 | 09.1 | `1Qr7EkERIx4r6EY6-Xmhft53zZzJAPZYu` | `1Gc6qYlWrzE02pGmsqtoFs91jMldk9aEm` |
| 09 | 09.2 | `1WEVxipkETkRZj2Nw3Itd6sYnhZul_ZNh` | `1vbfxJCX6ePPyeg-HuSmk081GCL0B2Mt-` |
| 09 | 09.3 | `1NyINYv-rZ-yYlIy_nFTt2DQ2qGZSWcAv` | `1dcnWVD6mF5X5KCjxyjwRdOsRahY1mudk` |
| 09 | 09.4 | `1jldfg9_XIZQqyCnXBeebGRyOgfttKQ5m` | `11XHQFjaZq8dO72BAymJ-kbpf5Dr3zvrZ` |
| 09 | 09.5 | `1wHQ6L07AH3gHuykPG4sZpDBjWVImS-vU` | `13jiag0DYyALe5uiFyrtz16jINWjJoKTK` |
| 09 | 09.6 | `1ZvpP2T1dGylzimsXiKw0pkfn7TtMWlXZ` | `1oZg2HYUPr8-jA59sXH5bMIF_q79M2WMH` |
| 10 | 10.1 | `1h8T318lpe8ho3VtcqHwBM4gLaOWEPR2u` | `1hJh-YrMr-4knpRP8GYVE68O53ZG7CZvu` |
| 10 | 10.2 | `1FFEyCiOxg2UFNqeBDIU0SaKAtO0AtiG0` | `1p2XOdpGw3wPvCHmWaVhmg9QMOnowKg47` |
| 10 | 10.3 | `1pd3D0ZnERc9QcYLBzob8pSETgLwYfyGD` | `1rnZHgf0RKjVCBDkPHuu08oUBqjIVQc2c` |
| 10 | 10.4 | `14YgjV8pUEM-j7ctouWKiYGX-lQNztaCy` | `1rIO2hNQmj0j5cow8o-WtkDOSWrGHWFaZ` |
| 10 | 10.5 | `14dkioIqg7M9GH6p5RQX0mMS9K15EZun7` | `1QKDem2MLf2UTojU9kn1VDEsh-435OgEe` |
| 10 | 10.6 | `1biMvZPpFj9hBafLZIFpq9FwwIEyfFxWX` | `1Tvm_lBaorXU1ovI9aYrnugcrR-7NmOzG` |

**Total logged for trash: 196 folders (108 Geology + 88 Physics), all independently confirmed empty
as of this report.**

## Before/after summary

| | Before this retrofit | After this retrofit |
|---|---|---|
| Unit-level `Quiz` folders | 0 | 20 (new, verified) |
| Section-level `Homework` folders (old placement) | 98, 2 non-empty | 98 — all confirmed empty, not yet trashed (no tool) |
| Section-level `Tests-Quizizz` folders (old placement) | 98 | 98 — all confirmed empty, not yet trashed (no tool) |
| Files migrated Homework → Section | 0 expected | 2 (see exception above) |
| Files migrated Tests-Quizizz → Quiz | 0 expected | 0 |
| Section-level `Labs-Case Studies-Projects` | 98 | unchanged, untouched |

## Trash tool unavailable — same limitation as prior sessions

As in `2026-09-16b_geo-retrofit-shull-chg-0023.md`, this session's tool set (`Read`, `Glob`, `Grep`,
`Write`, and the Google Drive MCP tools `search_files`, `get_file_metadata`, `read_file_content`,
`download_file_content`, `create_file`, `update_file`, `copy_file`, `list_recent_files`) does not
expose a trash/delete tool. This is a tool-availability limit for this session, not a Drive
permission and not a decision being declined. The 196 folders above are confirmed empty and safe to
trash whenever a session with that tool, and Matt's approval, is available.
