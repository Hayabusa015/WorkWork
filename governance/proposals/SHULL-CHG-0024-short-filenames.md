---
id: SHULL-CHG-0024
title: Short, readable filenames — section-led, no course prefix
status: APPROVED
opened: 2026-10-15
source: User
decided: 2026-10-15
decided_by: Matthew Shull
---

# SHULL-CHG-0024 — Short filenames

## What he asked for

> "They are too big for the folders. While I open file explorer I can't even see what the file is
> because the name is so long." Pattern given: `Unit [X] Guided Notes: [Unit here]` and
> `1.2 Worksheet [Topic Here]`.

Answers on 2026-10-15: course identified by folder only; space-dash-space separator (the colon is
illegal in Windows and synced filenames); section-led pattern for the other types.

## Current Rule

`standards/NAMING.md` §2: `SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor][_Version].[ext]`

## Proposed Rule

```
Unit-level:     Unit [X] [Type] - [Unit Title]            Unit 3 Guided Notes - Atomic Structure
Section-level:  [S.S] [Type] - [Topic]                    1.2 Worksheet - Balancing Equations
Versions:       [S.S] [Type] [A|B|C] - [Topic]            1.4 Quiz A - Reaction Time
Keys:           [S.S] [Type] [A|B|C] Key - [Topic]        1.4 Quiz A Key - Reaction Time
```

- No `SHULL_` prefix, no course code. The Drive folder path carries the course.
- Section and unit numbers are written unpadded (`1.2`, `Unit 3`), matching the user's examples.
- Types remain the fixed list in NAMING.md §2 (Title Case, spaces for underscores).
- Keys stay separate files.
- `/` and `:` never appear in a name.

## Supersedes

`standards/NAMING.md` §2 grammar, worked examples, and the "why padded" paragraph.

## What it touches

| Place | Change |
|---|---|
| `standards/NAMING.md` | New grammar |
| `.claude/skills/naming/SKILL.md` | Procedure steps 1, 4, 6 |
| `scripts/validate_codes.py` | `FILENAME` regex; the file-to-folder check needs a new matcher |
| Builders and skills that emit `SHULL_` names | `build-*`, `shelve-drive-file`, `templates/lab/build_lab.py` — to be listed by grep before implementation |
| Drive | Rename existing files — a separate, per-file-approved operation |

## Risk

medium. A name no longer states its course, so a downloaded file loses that context. Renames can
break links in a gradebook, Classroom post, or bookmark. Rename keeps file IDs, which protects
links by ID but not links by name.

## Drive findings that affect the rename

- Duplicates: identical names appear in more than one parent folder (for example
  `SHULL_CHEM_Element_Builder_Designed.docx` in three folders). After renaming these collide.
- `- Copy` files and an `AutoRecovery save of…` file exist. Candidates for the trash, not rename.
- Names that already break the current grammar (`S1.1` unpadded, `Day2_ABC`, `Fall2026`).
- Some generic items (`SHULL_Geologic_Timeline_*`) carry no unit or section at all.

## Recommendation

Approve the grammar; implement repo changes first; then run the Drive rename as a reviewed batch.

Decision: Approved by Matthew Shull, 2026-10-15.
Status: APPROVED
Implemented By:
Verified:
