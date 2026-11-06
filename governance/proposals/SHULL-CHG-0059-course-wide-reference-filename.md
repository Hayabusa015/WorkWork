# SHULL-CHG-0059 — A course-level filename form for whole-year documents

**Path B — a standards change.** Edits `standards/NAMING.md` and, through the open points below,
touches `standards/DRIVE_ARCHITECTURE.md` and the two filename builders.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0059 |
| **Date** | 2026-11-06 |
| **Source** | User. Raised by the Chemistry reference packet (SHULL-CHG-0058), a whole-year document. |
| **Current Rule** | `standards/NAMING.md` §2 "The grammar", verbatim — see "Current Rule (verbatim)" below. Every name starts with a section code (`S.S`) or `Unit X`. |
| **Proposed Rule** | Add a third, course-level form: `<Course> Reference - <Topic>.pdf`. Used **only** when a document spans the whole year. See "Proposed Rule (verbatim)" below. |
| **Supersedes** | Nothing is removed. It extends `standards/NAMING.md` §2 (the two-line grammar block and the parts table). It **conflicts** with one sentence of §2 (SHULL-CHG-0024) — see "Conflict with an existing rule". |
| **Reason** | A whole-year course packet has neither a section nor a unit, so under the current grammar it cannot be named at all. |
| **Affected Agents** | Librarian (names and files the document). |
| **Affected Skills** | Any skill that names a built file through the builders; `build-document` in particular. No skill text is edited by this record. |
| **Affected Courses** | Chemistry, Physics, Geology. |
| **Risk** | low–medium (the record's `low \| medium \| high` scale has no such value; the brief gave "low–medium". The medium part is the conflict with SHULL-CHG-0024 and the builder change.) |
| **Recommendation** | Decide the conflict first (open point 1). If the course name in the filename is accepted, approve with open points 2–4 answered, since each one changes what gets implemented. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | — (not implemented) |
| **Verified** | no — not implemented |

---

## Current Rule (verbatim)

`standards/NAMING.md` §2:

```
Section-level:  [S.S] [Type] [Version] [Key] - [Topic].[ext]
Unit-level:     Unit [X] [Type] [Version] [Key] - [Unit Title].[ext]
```

The relevant rows of its parts table:

```markdown
| `S.S` | the section code exactly as the course `DECISIONS.md` writes it: `1.2`, `10.4`. Not padded. |
| `Unit X` | the unit number, not padded: `Unit 3` |
| `Topic` / `Unit Title` | the **short title** (at most 20 characters) from the "Short titles" table in the course `DECISIONS.md`. **No row, no topic**: the name is `1.3 Lab.pdf`. Never shorten a title automatically, and never use the full title. |
```

And the scope rule beneath it:

> A document that covers **more than one section** is unit-level. A document that covers one is
> section-level.

## Proposed Rule (verbatim)

Add to `standards/NAMING.md` §2, after the two grammar lines:

```
Course-level:   [Course] Reference - [Topic].pdf
```

```markdown
| `Course` | `Chemistry`, `Physics` or `Geology`. Course-level names only. |
```

> A document that spans **the whole year** is course-level. Course-level is used only then; a
> document that spans several units but not the year is still unit-level.

Worked examples:

```
Chemistry Reference - Equations.pdf
Chemistry Reference - Polyatomic Ions.pdf
```

## Conflict with an existing rule

**Marked, not resolved.** `standards/NAMING.md` §2, from SHULL-CHG-0024 ("Short section-led
filenames; no course prefix"), says verbatim:

> Names are short so they stay readable in a narrow folder window. The **folder path carries the
> course**; the name does not repeat it.

The proposed form puts the course in the name. Either the course-level form is an explicit
exception to that sentence (and §2 says so), or the course word is dropped (`Reference -
Equations.pdf`), which would then rely on the folder for the course as everything else does. The
user decides.

## What implementation would also have to change

These are the parts of the system that encode the current grammar. Approval of this record would
need to cover them, or they become separate records.

1. **Builders.** `templates/_shull_name.py` `document_name()` and `templates/shull_name.cjs` both
   pick the head from the section list: one section gives `S.S`, otherwise `Unit X`. Neither has a
   course-level path. Both need one.
2. **Tests.** `standards/NAMING.md` §2 says both builders "are pinned to the examples above by their
   tests". The JS side is tested in `app/design.test.mjs` (via `app/curriculum.mjs`, which loads
   `shull_name.cjs`). **No Python test of `templates/_shull_name.py` was found** in the repository
   (searched for `document_name` / `_shull_name` across test files). New course-level examples
   would need adding to the JS test; whether a Python test is created is part of this decision.
3. **Short titles for course-level topics.** The 20-character topic comes from the "Short titles"
   table in the course `DECISIONS.md`, keyed by a unit (`U1`) or a section (`1.3`) code
   (`_shull_name.py` `short_title()` normalises only those two key shapes). A course-level topic has
   no code, so there is no row to read and "no row, no topic" would give `Chemistry Reference.pdf`
   for every sheet. A rule is needed: what key a course-level topic row uses, and that it is held
   to the same 20 characters. Four of SHULL-CHG-0058's sheet titles are over 20 (see that record).
4. **A filing location.** `standards/DRIVE_ARCHITECTURE.md` has no place for a course-level file
   other than snow-day work. Verbatim, §1 "Grammar":

   > **`Snow Day` is the one course-level folder** (SHULL-CHG-0057). A snow-day assignment belongs to no
   > unit or section, so it is filed in `[Course]/Snow Day/`, a sibling of the Unit folders.

   and §1 "What goes where" files `Reference` documents only at the Section level:

   > | *(no folder — loose in Section)* | Section | Activities and any other file for a single section with no matching folder, including `Reference` and `Organizer` files (SHULL-CHG-0035). |

   and §2 rule 4:

   > **If the unit or section is unclear, ask.** Never default to a misc folder.

   So a course-level file currently has nowhere to go. Options (the user's choice, not this
   record's): loose directly in `[Course]/`; or a user-created course-level folder recognised the
   way `Snow Day` is (the system creates no content folders, SHULL-CHG-0035). Either way
   `DRIVE_ARCHITECTURE.md` needs an edit, which is a second Path B change to `standards/`.

## Open points

1. Course word in the name, or not? (the conflict above)
2. Is the course-level form limited to `Reference`, or open to any type (a year-long `Organizer`,
   say)? The proposed grammar fixes the type to `Reference`.
3. The short-title key and limit for course-level topics (item 3 above).
4. The Drive location (item 4 above).
