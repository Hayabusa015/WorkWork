# Trash the three staging duplicates, 2026-11-06

Approval: user in chat 2026-11-06, "trash the 3 staging duplicates". Trash is recoverable; nothing is
permanently deleted.

Each is a copy in the `pdf` staging folder (`13bjAwZfmIxrt0g0W1ozt8lBFfIojWpra`) of a file that is
filed in `Geology / Unit 02 - Geologic Time / Homework` (`1W9L10dhOpAt4IPg0zhHQiQPl59cIy9DI`). The
byte sizes match, checked by lookup before trashing.

| Staging file (to trash) | ID | Bytes | Kept copy (ID) |
|---|---|---|---|
| SHULL_Geologic_Timeline_4_Pages_Cenozoic.pdf | 1i1OFCFVkXhyoDC8LChmOLvOAIjs4iYkt | 48971 | Unit 2 Activity - Geologic Timeline 4 Pages Cenozoic.pdf (1BXJDvWDtvcBGxrbQ9xG62vL0MHEZuhuR) |
| SHULL_Geologic_Cutouts_38_Events.pdf | 1rGAm9mHYXFy0FZjLr_7xCzcI0ogtiSRh | 1341669 | Unit 2 Activity - Geologic Cutouts 38 Events.pdf (1iGVmY30TKjkTIVp_Naykdpp58wbWbyK4) |
| SHULL_Geologic_Time_Reference_Guide.pdf | 1tgQZfLGzy2KRnl0XwxsisdLyBkgmJpsi | 42960 | Unit 2 Reference - Geologic Time Reference Guide.pdf (1-rPhjbQaO4BY_v6eG6NNwy2czy61Gos9) |

Prior parent of each: the `pdf` staging folder. Rollback: restore from Drive trash.

## Result

All three `trash_file` calls returned success, after the approval manifest
`approved-trash/2026-11-06_staging-duplicates.txt` listed the three IDs. Independent lookup: a
search of the staging folder for the three names returns nothing, and the three kept copies are
still in `Unit 02 - Geologic Time / Homework` with the same byte sizes. They are in Drive trash and
can be restored from there.
