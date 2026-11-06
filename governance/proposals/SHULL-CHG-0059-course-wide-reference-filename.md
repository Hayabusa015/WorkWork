# SHULL-CHG-0059 — A course-level filename form for whole-year documents

**Path B — a standards change.** This record covers **two** standards edits: `standards/NAMING.md`
(the filename grammar) and `standards/DRIVE_ARCHITECTURE.md` (the course-level `Reference` folder).
It also requires builder and test changes in `templates/` and `app/`. Those directories are not
Secretary-governed, so the main session implements them (see "Builders and tests").

**Amended 2026-11-06** to state exactly the changes the main session offered to resolve this
record's open points. See "Resolved".

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0059 |
| **Date** | 2026-11-06 |
| **Source** | User. Raised by the Chemistry reference packet (SHULL-CHG-0058), a whole-year document. |
| **Current Rule** | `standards/NAMING.md` §2 "The grammar", and `standards/DRIVE_ARCHITECTURE.md` §1 (the tree, the `Snow Day` grammar bullet, "What goes where"), verbatim. See "Current Rule (verbatim)" below. Every name starts with a section code (`S.S`) or `Unit X`; `Snow Day` is the one course-level folder. |
| **Proposed Rule** | A course-level filename form `Reference - [Topic].pdf`, with no course word in the name, used **only** when a document spans the whole year and **only** for type `Reference`. Course-level topics come from `REF` rows in the course `DECISIONS.md` "Short titles" table, at most 20 characters. Course-level Reference files are filed in a user-made `[Course]/Reference/` folder, recognised the way `Snow Day` is. Exact text under "Proposed Rule (verbatim)". |
| **Supersedes** | Nothing is removed. Extends `standards/NAMING.md` §2 (the grammar block, the parts table, the scope rule, the worked examples) and the §2 Authority line. Amends `standards/DRIVE_ARCHITECTURE.md` §1: the tree, the grammar bullet "**`Snow Day` is the one course-level folder** (SHULL-CHG-0057)" (which is no longer true once `Reference` is added), and the "What goes where" table; plus an "Amended by" line in its header. No conflict with SHULL-CHG-0024: the name carries no course word, so "the folder path carries the course" still holds. |
| **Reason** | A whole-year course packet has neither a section nor a unit, so under the current grammar it cannot be named, and under the current Drive architecture it has nowhere to be filed. |
| **Affected Agents** | Librarian (names and files the document; confirms `[Course]/Reference/` exists before filing). |
| **Affected Skills** | Any skill that names a built file through the builders; `build-document` in particular. No skill text is edited by this record. |
| **Affected Courses** | Chemistry, Physics, Geology (the form is available to all three; Chemistry is the first user, SHULL-CHG-0058). |
| **Risk** | medium — two standards files, both filename builders, and a new course-level folder. |
| **Recommendation** | Approve as amended. |
| **Decision** | User, 2026-11-06, in chat: "approve 0058 and 0059 with your changes" |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | 0ba1b27 (standards: `NAMING.md`, `DRIVE_ARCHITECTURE.md`); de467b1 (builders and tests: `templates/`, `app/`) |
| **Verified** | yes — `npm test` 38/38 pass, including the new course-level test in `app/design.test.mjs`; new `templates/test_shull_name.py` 4/4 pass; the `standards/NAMING.md` §2 worked examples are now pinned by both builders' tests. |

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

`standards/DRIVE_ARCHITECTURE.md` §1, the tree:

```
└── [Course]/                        Chemistry · Physics · Geology
    ├── Snow Day/                    course level; snow-day assignments and keys (SHULL-CHG-0057)
    └── Unit ## - Unit Name/
```

§1 "Grammar":

> - **`Snow Day` is the one course-level folder** (SHULL-CHG-0057). A snow-day assignment belongs to no
>   unit or section, so it is filed in `[Course]/Snow Day/`, a sibling of the Unit folders. The user
>   created it in all three courses on 2026-11-05. Match it case-insensitively; if a course lacks one,
>   ask before creating it, as with any folder outside §2 rule 3.

§1 "What goes where" files `Reference` documents only at the Section level:

> | *(no folder — loose in Section)* | Section | Activities and any other file for a single section with no matching folder, including `Reference` and `Organizer` files (SHULL-CHG-0035). |

## Proposed Rule (verbatim)

### Edit 1 — `standards/NAMING.md`

**1a.** Line 3, the Authority line. Replace

```markdown
**Authority:** SHULL-CHG-0024 (short, section-led names), SHULL-CHG-0041 (short topics).
```

with

```markdown
**Authority:** SHULL-CHG-0024 (short, section-led names), SHULL-CHG-0041 (short topics),
SHULL-CHG-0059 (course-level Reference names).
```

**1b.** §2, the grammar block. Replace

```
Section-level:  [S.S] [Type] [Version] [Key] - [Topic].[ext]
Unit-level:     Unit [X] [Type] [Version] [Key] - [Unit Title].[ext]
```

with

```
Section-level:  [S.S] [Type] [Version] [Key] - [Topic].[ext]
Unit-level:     Unit [X] [Type] [Version] [Key] - [Unit Title].[ext]
Course-level:   Reference - [Topic].pdf
```

**1c.** §2 parts table. Replace the `Topic` / `Unit Title` row

```markdown
| `Topic` / `Unit Title` | the **short title** (at most 20 characters) from the "Short titles" table in the course `DECISIONS.md`. **No row, no topic**: the name is `1.3 Lab.pdf`. Never shorten a title automatically, and never use the full title. |
```

with

```markdown
| `Topic` / `Unit Title` | the **short title** (at most 20 characters) from the "Short titles" table in the course `DECISIONS.md`. **No row, no topic**: the name is `1.3 Lab.pdf`. Never shorten a title automatically, and never use the full title. A course-level topic is a row whose code is `REF`; a course-level name always has a topic, so with no `REF` row there is no course-level name (SHULL-CHG-0059). |
```

**1d.** §2, the scope rule. Replace

```markdown
A document that covers **more than one section** is unit-level. A document that covers one is
section-level.
```

with

```markdown
A document that covers **more than one section** is unit-level. A document that covers one is
section-level. A document that spans **the whole year** is course-level (SHULL-CHG-0059).
Course-level is used only then, and only for type `Reference`: it has no version and no key, and
it is always a PDF. A document that spans several units but not the year is still unit-level. As
with every other name, the course is not in it; the folder path (`[Course]/Reference/`,
`standards/DRIVE_ARCHITECTURE.md`) carries it.
```

**1e.** §2 "Worked examples". Replace the code block

```
Unit 1 Guided Notes - Matter & Atoms.docx
1.3 Lab - Motion Graphs.pdf
1.3 Lab Key - Motion Graphs.pdf
2.3 Practice Set - Electron Configs Longhand.docx
1.4 Slides - Isotopes.pptx
Unit 1 Test B - Matter & Atoms.docx
1.3 Lab.pdf                                        (a section with no short title)
```

with

```
Unit 1 Guided Notes - Matter & Atoms.docx
1.3 Lab - Motion Graphs.pdf
1.3 Lab Key - Motion Graphs.pdf
2.3 Practice Set - Electron Configs Longhand.docx
1.4 Slides - Isotopes.pptx
Unit 1 Test B - Matter & Atoms.docx
1.3 Lab.pdf                                        (a section with no short title)
Reference - Polyatomic Ions.pdf                    (course-level, whole year)
Reference - Multi-Charge Metals.pdf                (course-level, whole year)
Reference - Full Packet.pdf                        (course-level, all sheets combined for printing)
```

The sentence after the examples ("Builders and the app take the name from ... pinned to the
examples above by their tests.") is unchanged; it becomes true for the new examples only once the
builder and test work below is done.

### Edit 2 — `standards/DRIVE_ARCHITECTURE.md`

**2a.** Header. After the paragraph that begins `**Amended by SHULL-CHG-0035** (2026-10-15)` and
before `**Folder IDs and operational notes:**`, insert

```markdown
**Amended by SHULL-CHG-0059**: a second course-level folder, `Reference`, for whole-year Reference
documents. See `governance/proposals/SHULL-CHG-0059-course-wide-reference-filename.md`.
```

**2b.** §1 tree. Replace

```
    ├── Snow Day/                    course level; snow-day assignments and keys (SHULL-CHG-0057)
    └── Unit ## - Unit Name/
```

with

```
    ├── Reference/                   course level; whole-year Reference documents (SHULL-CHG-0059)
    ├── Snow Day/                    course level; snow-day assignments and keys (SHULL-CHG-0057)
    └── Unit ## - Unit Name/
```

**2c.** §1 "Grammar". Replace the Snow Day bullet

```markdown
- **`Snow Day` is the one course-level folder** (SHULL-CHG-0057). A snow-day assignment belongs to no
  unit or section, so it is filed in `[Course]/Snow Day/`, a sibling of the Unit folders. The user
  created it in all three courses on 2026-11-05. Match it case-insensitively; if a course lacks one,
  ask before creating it, as with any folder outside §2 rule 3.
```

with

```markdown
- **Two course-level folders are recognised: `Snow Day` and `Reference`.**
  - `Snow Day` (SHULL-CHG-0057). A snow-day assignment belongs to no unit or section, so it is
    filed in `[Course]/Snow Day/`, a sibling of the Unit folders. The user created it in all three
    courses on 2026-11-05. Match it case-insensitively; if a course lacks one, ask before creating
    it, as with any folder outside §2 rule 3.
  - `Reference` (SHULL-CHG-0059). A whole-year Reference document (course-level name,
    `standards/NAMING.md` §2) belongs to no unit or section, so it is filed in
    `[Course]/Reference/`, a sibling of the Unit folders. Match it case-insensitively. The system
    does not create it (SHULL-CHG-0035): before filing, the Librarian confirms it exists in that
    course, and if it does not, asks the user.
```

**2d.** §1 "What goes where" table. After the `Labs-Case Studies-Projects` row and before the first
`*(no folder — loose in Section)*` row, insert

```markdown
| Reference | Course | Whole-year Reference documents, named at course level (`Reference - [Topic].pdf`, `standards/NAMING.md` §2): each sheet and the combined print packet. Section-scope `Reference` files stay loose in their Section (row below). **SHULL-CHG-0059.** |
```

The Snow Day folder has no row in this table today; this record does not add one.

## Builders and tests

`templates/` and `app/` are not Secretary-governed directories, so **the main session implements
these**. They are part of this change: NAMING.md §2 says the builders are pinned to its examples by
their tests, so Edit 1e is not true until this is done.

1. **`templates/_shull_name.py`** — `document_name()` picks the head from the section list (one
   section gives `S.S`, otherwise `Unit X`). Add a course-level path that produces
   `Reference - [Topic].pdf`: type fixed to `Reference`, no version, no key, extension `pdf`, topic
   required and at most 20 characters. Add a course-level topic lookup that reads the `REF` rows of
   the course "Short titles" table. The existing `short_title()` returns the first matching row
   only, so it cannot serve several `REF` rows as written.
2. **`templates/shull_name.cjs`** — the same course-level path and lookup.
3. **`app/design.test.mjs`** — add the three course-level worked examples from Edit 1e.
4. **New Python test for `templates/_shull_name.py`** — none exists today (searched for
   `document_name` / `_shull_name` across test files). Create a small one pinned to the NAMING.md
   §2 worked examples, the course-level ones included.

## Resolved

The record previously carried a "Conflict with an existing rule" section and four open points. The
main session offered the changes below on 2026-11-06, and this record now states them. The user's
reply referred to them as "with your changes". The user's decision itself is recorded in
`Decision:` and `Status:` by the main session, not here.

1. **Course word in the name (the former conflict with SHULL-CHG-0024).** Dropped. The form is
   `Reference - [Topic].pdf`. SHULL-CHG-0024's "the folder path carries the course; the name does
   not repeat it" is followed, so there is no conflict.
2. **Reference only, or any type?** Reference only.
3. **Short-title key and limit for course-level topics.** `REF` rows in the course `DECISIONS.md`
   "Short titles" table, at most 20 characters. The builders gain a course-level path that reads
   those rows.
4. **Drive location.** A user-made course-level folder `[Course]/Reference/`, a sibling of the Unit
   folders, recognised the way `Snow Day` is (SHULL-CHG-0057). The system does not create it
   (SHULL-CHG-0035); the Librarian confirms it exists before filing. This record covers that
   `DRIVE_ARCHITECTURE.md` edit as well as the `NAMING.md` edit.
