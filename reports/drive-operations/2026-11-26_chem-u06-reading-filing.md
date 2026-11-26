# 2026-11-26 — Chemistry Unit 6 Reading (Nomenclature) filing

Approval relayed by the coordinator: Matt, in the main session 2026-11-26, "Moved. File it."
Filing-queue row: Unit 6 Reading - Nomenclature, Status Ready (textbook audit PASS, Round 5).
Logged before any mutation.

## Pre-flight

| Check | Result |
|---|---|
| Unit code | U6 Chemical Nomenclature, 6.1–6.4 taught; short title "Nomenclature" (courses/chemistry/DECISIONS.md, 2026-11-23 and 2026-11-25) |
| Names | `Unit 6 Reading - Nomenclature` / `Unit 6 Reading Key - Nomenclature` match standards/NAMING.md (Reading type) |
| Hash, student PDF | 85b86d2bc5c1d39558b2379e142d175e256e9d2b0832e9c5c51f147ea481f95d, 543492 bytes (matches 85b86d2b…) |
| Hash, key PDF | c7ce54557fe9a067ad55ece37ddec3934c726cbd4b70bdbea0aa537dbb6125d8, 155056 bytes (matches c7ce5455…) |
| Hash, student DOCX | a55738e255721263c66b36d2df7ecce90b538c0556aa867b920d5e731a4ebc17, 507753 bytes |
| Hash, key DOCX | 8454ab0d5cfe7e467e4d9ce7122314f1c748b239257fa5f545511777695ee122, 51463 bytes |
| Unit folder | `Chemistry / Unit 06 - Chemical Nomenclature`, 1C3ln5w958kkA9QS9Dmt9cMerhTiBNhG3. Found by a parentId listing of Chemistry (1dA5kKA9vQxaWX0CZMhXIoBMYGfDhMxH6). It is the only Unit 06 folder and is not trashed |
| Unit direct children | Only the four Section folders: 06.1 Covalent Names & Formulas (1X6gWTpwuIVivLTYN5qAumZ-wq0iKvPyh), 06.2 Polyatomic Ions (17aOmOyFbUkEsRBZsNRg8nYxDIIWQYIh3), 06.3 Ionic Names & Formulas with Transition Metals (1h89d23N2lNf-Sg38lb_VKeO2upeNIKMd), 06.4 Naming Acids & Formulas (1ZUO6emNGbO4muVKHiA0lMtTPmXrd6rBS) |
| Section children | 06.1 holds `SHULL_Chemistry_Chemical_Nomenclature (1).pptx` (15bOPjF9SqSH95Ro3EcmJiN5yyQfuUB6I). 06.2–06.4 are empty. The ancestors search finds no other file anywhere under Unit 06 |
| Earlier edition | None. A title search for "Unit 6 Reading", "Unit 06 Reading", and Reading + Nomenclature returns nothing on Drive |
| Layout test | Steps 1–3: no match. Step 4: no file with a readable step-4 type. **Step 5: match.** The deck has moved from the unit root into Section 06.1, but its name is unchanged and still has no Type word (NAMING §2). Step 4 looks anywhere inside the unit, so its type still cannot be read. Result: **Stop. Report and ask** |

## First pass result: NOT FILED. Blocked at layout-test step 5

No upload was made and nothing on Drive was changed. The survey's P-10 gate
(2026-11-25_chem-folder-survey.md) said the deck needed to be renamed **and** moved. It has been
moved but not renamed, and the connector cannot rename it (canEdit false).

Note: a Reading goes loose in the unit folder under either layout (new layout: "anything with no row
above"; legacy layout: "unit-scope files with no matching folder"). So the destination does not
depend on how step 5 is resolved. But the standard says to stop at step 5, and this agent may not
override it. The upload needs Matt's decision first.

## Matt's decision: step 5 overridden

The coordinator relayed Matt's answer from the main session, 2026-11-26: "Gile it anyway" (a typo
for "file it anyway"). This chooses option 2 from the first-pass report: file the Reading loose in
Unit 06 without settling the unit's layout. Logged before execution.

- **Override:** the layout-test step-5 stop is waived **for this filing only**, on Matt's direct
  instruction. The unit's layout is **still unsettled**. Run the test again before the next filing
  into Unit 06, especially for a step-4 type (Slides, Guided Notes, Quiz, Test, Practice Set,
  Activity, Organizer), where the layout does decide the folder.
- **Still open:** `SHULL_Chemistry_Chemical_Nomenclature (1).pptx` (15bOPjF9SqSH95Ro3EcmJiN5yyQfuUB6I)
  in Section 06.1 still has no name that follows the standard. The connector reports canEdit false,
  so only Matt can rename it, in Drive.
- **Re-checked just before upload:** all four hashes and sizes are unchanged (pre-flight table).
  Unit 06 still has only its four Section folders, and Drive still has no "Unit 6 Reading" file.

## Intended operations

These are new objects, so they have no prior name or prior parent. Route: Drive connector
`create_file` with a file reference (`sha256:<hex>:<path>`), `disableConversionToGoogleType: true`,
and parentId 1C3ln5w958kkA9QS9Dmt9cMerhTiBNhG3 (loose in the unit). This is the same route as the
U7 re-file (2026-11-25_chem-u07-reading-filing.md). Rollback: trash the new files, which needs user
approval.

| # | Final name | contentMimeType | Bytes | New ID | Result |
|---|---|---|---|---|---|
| 1 | Unit 6 Reading - Nomenclature.docx | application/vnd.openxmlformats-officedocument.wordprocessingml.document | 507753 | 1hmvgfEM6EgRFhKQcMs5fIufAN3__Zl5d | Filed, verified |
| 2 | Unit 6 Reading - Nomenclature.pdf | application/pdf | 543492 | 1HLLO0akKAAnJQ5ZMuwHkLCvP0ih2yeTQ | Filed, verified |
| 3 | Unit 6 Reading Key - Nomenclature.docx | application/vnd.openxmlformats-officedocument.wordprocessingml.document | 51463 | 1Be0t-VBY2xLfcv8rwZ3l4B6wfrQlF011 | Filed, verified |
| 4 | Unit 6 Reading Key - Nomenclature.pdf | application/pdf | 155056 | 11fmCUuInMwQwS9W-nmZlYj4TmXibMiG0 | Filed, verified |

## Result: FILED

After creation, each file was checked with its own `get_file_metadata` call, and Unit 06 was then
listed by parentId:

| ID | parentId = Unit 06 | Title exact | Size = local | mimeType (not converted) |
|---|---|---|---|---|
| 1hmvgfEM6EgRFhKQcMs5fIufAN3__Zl5d | yes | Unit 6 Reading - Nomenclature.docx | 507753 = 507753 | application/vnd.openxmlformats-officedocument.wordprocessingml.document |
| 1HLLO0akKAAnJQ5ZMuwHkLCvP0ih2yeTQ | yes | Unit 6 Reading - Nomenclature.pdf | 543492 = 543492 | application/pdf |
| 1Be0t-VBY2xLfcv8rwZ3l4B6wfrQlF011 | yes | Unit 6 Reading Key - Nomenclature.docx | 51463 = 51463 | application/vnd.openxmlformats-officedocument.wordprocessingml.document |
| 11fmCUuInMwQwS9W-nmZlYj4TmXibMiG0 | yes | Unit 6 Reading Key - Nomenclature.pdf | 155056 = 155056 | application/pdf |

All four are not trashed. The connector reports canEdit, canMoveItemWithinDrive and canTrash as true
on all four.

**Unit 06 listing** (parentId 1C3ln5w958kkA9QS9Dmt9cMerhTiBNhG3): the four files above, plus
Section 06.1–06.4. Nothing else.

Filing-queue row updated: Status Filed, path, folder ID, four file IDs, date 2026-11-26. Box not
ticked. Nothing committed.
