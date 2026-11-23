# 2026-11-05 — Chemistry U4/U5 content folders, and moving the U4-U5 files into them

Matt's direct instruction, 2026-11-05: "can you just make them for me. Quiz's, Test,
Presentations + Guided Notes, Worksheets". Logged before execution.

This overrides SHULL-CHG-0035 (the system creates no content folders) for these two units, by the
user's instruction in the current conversation (CLAUDE.md §2 precedence 1). The names also differ
from the recognised set in config/drive.json (Guided Notes, Presentations, Quiz): "Test",
"Worksheets" and the combined "Presentations + Guided Notes" are Matt's own. Recording them as the
standard for every unit needs a Secretary change record; this log does not do that.

## Unit 04 - Chemical Bonding (1kc9YcPBNIev4ibE5_B0oFic99XxahqAC)
Matt created the four folders by hand, 2026-11-05 14:53 UTC. Reused exactly, not recreated:
Quiz 19f78LexUifu7EEsPCrKCIEdsHSYnf_9M · Test 1cCLAotx38R25_y1Hfh3Beest4nzf_5wh ·
Worksheets 1oq5XZlg61Xv606Yn2RzYg2qO90Zg1-T3 · Presentations + Guided Notes 1ItO2Nvb5xUuhzJ7T1_SctH9YNswNRpn_

## Unit 05 - Molecular Structure & Intermolecular Forces (1Xp4LtakhP04hhftD6sEw4I6-H-Mp97AM)
Empty before this operation. Create the same four, same spelling: Quiz, Test,
Presentations + Guided Notes, Worksheets.

## Moves (reparent; IDs kept). Prior parent for all: Unit 04 root 1kc9YcPBNIev4ibE5_B0oFic99XxahqAC
| File | ID | New parent |
|---|---|---|
| SHULL Chemistry Units 04-05 - Bonding and Molecular Structure.pptx | 1EceFjASf0wuEHJWAi8qMpZJk2KB1bSZb | Presentations + Guided Notes (U04) |
| Unit 4-5 Guided Notes.docx | 1pxby3YJdMYiPNUJ4PWK9dYj9-Qb6BFCU | Presentations + Guided Notes (U04) |
| Unit 4-5 Guided Notes Key.docx | 13SiegaOWhfJnIwuIPme7nP5TGOOXZKsS | Presentations + Guided Notes (U04) |
| Unit 4-5 Guided Notes.pdf | 1GwZg7kjQGstk7dWx0t0e7ngz4_R_I4ZJ | Presentations + Guided Notes (U04) |

## Result (verified by parentId lookup, 2026-11-05)

Unit 05 folders created: Quiz 1ZJt1ZooNbRu2zD6OzAsM4n5TNLUFZi7L · Test 1g0vI7dG7EfuH-_Gd5RZ1HSgT3ezDfxay ·
Presentations + Guided Notes 1RFXL3qYVvuO46TYlBmc8UeoW9YspfId8 · Worksheets 1lY7mPWFkKvm7xkPkYJJ-VMM16n_igM4T.

All four files now have parent Presentations + Guided Notes (U04) 1ItO2Nvb5xUuhzJ7T1_SctH9YNswNRpn_,
IDs unchanged. The Unit 04 root now holds only the four content folders.

Open: config/drive.json recognisedUnitFolders lists Guided Notes, Presentations, Quiz. Matt's set
(Quiz, Test, Presentations + Guided Notes, Worksheets) is not yet recorded there; needs a Secretary
change record so future filings route into these folders.
