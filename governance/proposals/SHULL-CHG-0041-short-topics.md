---
id: SHULL-CHG-0041
title: Short topics in filenames — a short title per section, from the course decisions file
status: PENDING
opened: 2026-10-15
source: User
decided_by:
---

# SHULL-CHG-0041 — Short topics

## What he asked for

"Shorter filenames." Asked which way, he chose **keep a short topic** over dropping the topic.
Some names under SHULL-CHG-0024 are still long because the topic is the full section title, for
example `1.3 Lab - Position-Velocity-Acceleration Graphing Motion Graphs Version 1.pdf` (66 characters).

## Current Rule

`standards/NAMING.md` §2: the topic is the section title (or unit title) as written in the course
`DECISIONS.md`. If it is not there, leave the topic off.

## Proposed Rule

1. **The topic in a filename is a short title of at most 20 characters.** It is stored once per
   section and per unit in a table in that course's `courses/<course>/DECISIONS.md`
   (heading "Short titles"). The section title is a course fact; so is its short form.
2. **No automatic shortening.** Cutting a title at a word boundary produced "Formation of a Solar",
   "Position-Velocity-Acce" and "Tides &". If a section has no short title, the name has **no topic**
   (`1.3 Lab.pdf`). A short title is added when the user approves one.
3. **A descriptor stays** after the short title when it tells two files apart (`Longhand`,
   `Day 2`, `Extended`). A descriptor that repeats the short title is dropped.
4. Everything else in the grammar is unchanged: section-led, no course prefix, `Version N`, `Key`.

Examples:

| Now | With short topics |
|---|---|
| `1.3 Lab - Position-Velocity-Acceleration Graphing Motion Graphs Version 1.pdf` | `1.3 Lab - Motion Graphs Version 1.pdf` |
| `1.1 Practice Set Key - Distance, Displacement & Velocity.docx` | `1.1 Practice Set Key - Distance & Velocity.docx` |
| `Unit 1 Test A - Motion in One Dimension.docx` | `Unit 1 Test A - 1D Motion.docx` |
| `2.3 Practice Set - Electron Configurations Longhand.docx` | `2.3 Practice Set - Electron Configs Longhand.docx` |

## Proposed short titles (for the sections and units that have files on Drive now)

Edit any you do not like. Each is at most 20 characters.

| Course | Code | Full title | Short title |
|---|---|---|---|
| Chemistry | Unit 1 | Matter & Atomic Structure | Matter & Atoms |
| Chemistry | 0.4 | Scientific Observations | Observations |
| Chemistry | 1.1 | Matter & Changes | Matter & Changes |
| Chemistry | 1.4 | Isotopes | Isotopes |
| Chemistry | 1.5 | Average Atomic Mass | Average Atomic Mass |
| Chemistry | 2.3 | Electron Configurations | Electron Configs |
| Physics | Unit 1 | Motion in One Dimension | 1D Motion |
| Physics | 0.4 | Physics Graphing | Physics Graphing |
| Physics | 1.1 | Distance, Displacement & Velocity | Distance & Velocity |
| Physics | 1.2 | Acceleration & Kinematic Equations | Acceleration |
| Physics | 1.3 | Position-Velocity-Acceleration Graphing | Motion Graphs |
| Physics | 1.4 | Free Fall | Free Fall |
| Geology | Unit 2 | Geologic Time | Geologic Time |

The other sections (about 180) get a short title when a document is first built for them. The
builder asks; it never invents one.

## Where it lands

| Place | Change |
|---|---|
| `courses/<course>/DECISIONS.md` | New "Short titles" table per course (Secretary, against this record) |
| `standards/NAMING.md` §2 | Topic is the short title; no automatic shortening |
| `templates/_shull_name.py`, `templates/shull_name.cjs`, app | Read the short title; fall back to no topic |
| `.claude/skills/naming/SKILL.md` | Procedure steps 4 to 5 |
| Drive | A second rename of the files already renamed today: a plan table with old and new names for you to approve first, as before |

## Also

A defect found while checking: the section-title reader cuts some Geology titles where the decisions
file wraps a line ("The Scale of the", "Tides &", "Air"). It would be fixed in the same change.

## Risk

low for the repository. The Drive rename is the second in a day, and links by name break again;
links by ID are not affected.

## Supersedes

`standards/NAMING.md` §2, the rule for the topic part (SHULL-CHG-0024).

Decision:
Status: PENDING
Implemented By:
Verified:
