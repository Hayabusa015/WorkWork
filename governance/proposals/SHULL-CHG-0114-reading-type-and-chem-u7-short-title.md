# SHULL-CHG-0114 — New document type `Reading`; Chemistry U7 short title "The Mole"

> **No conflict with a LOCKED rule.** Part A adds one type to the fixed list in `standards/NAMING.md`
> §2 and changes no existing type and no grammar. Part B adds one row to a table that exists to take
> new rows. Nothing CONFLICT, PROVISIONAL or UNKNOWN is converted.
>
> **Two layers, two labelled edits** (`governance/CHANGE_CONTROL.md` §1). Part A is a standard: a
> document type affects all three courses (CLAUDE.md §2 test), Path B. Part B is a course fact: a
> short title affects only Chemistry, Path A. They share one record because one answer from Matt
> produced both, and they can be approved or declined separately.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0114 |
| **Date** | 2026-11-24 |
| **Source** | User. Matt, main session, 2026-11-24, while rebuilding the Chemistry U7 unit reading under `workflows/unit-textbook.md` (SHULL-CHG-0106/0107). He answered "Yes." to a plan whose decision D5 read: "File names: 'Unit 7 Reading - The Mole' and 'Unit 7 Reading Key - The Mole'. I'll file that as a naming proposal." That "Yes." approved the plan and the drafting of this proposal. It is not recorded here as approval of this record (see Decision). |
| **Current Rule** | **A.** `standards/NAMING.md` §2, verbatim: "**Types:** `Slides` · `Guided_Notes` · `Practice_Set` · `Quiz` · `Test` · `Lab` · `Study_Guide` · `Reference` · `Key` · `Rubric` · `Activity` · `Organizer` · `Roadmap`". No type covers a textbook-style unit reading. **B.** `courses/chemistry/DECISIONS.md`, "Short titles": the only unit row is `\| U1 \| Matter & Atoms \|`. U7 has no row, so under NAMING §2 ("No row, no topic") a U7 unit-level file takes no topic: `Unit 7 Reading.pdf`, as `output/chemistry/u07/Unit 7 Roadmap.pdf` already does. |
| **Proposed Rule** | **A.** The Types line becomes "**Types:** `Slides` · `Guided_Notes` · `Practice_Set` · `Quiz` · `Test` · `Lab` · `Study_Guide` · `Reference` · `Key` · `Rubric` · `Activity` · `Organizer` · `Roadmap` · `Reading`". A new paragraph follows the existing `Roadmap` paragraph, separated from it by a blank line, verbatim: "`Reading` is the textbook-style unit reading built under `workflows/unit-textbook.md`: the cover with the unit breakdown, the illustrated reading pages, and the duplex tear-off leaf at the end of the student copy. Always unit-level, since it covers every section of the unit. Its answer key is a separate file: `Unit [X] Reading - [Unit Title].[ext]` and `Unit [X] Reading Key - [Unit Title].[ext]` (SHULL-CHG-0114)." **B.** In "Short titles", a new row directly after `\| U1 \| Matter & Atoms \|`: `\| U7 \| The Mole \|`. A decision-log entry goes at the top of the Chemistry decision log (draft below). |
| **Supersedes** | **A.** `standards/NAMING.md` §2, Types list (extends it; nothing removed). **B.** None. A new short-title row; no rule replaced. |
| **Reason** | **A.** SHULL-CHG-0106/0107 created the unit reading as a repeatable deliverable in all three courses, but NAMING §2 has no type for it. The pilot builder says so itself: `templates/reading/build_reading_docx.py` lines 7–8 read "PILOT DOCUMENT TYPE. standards/NAMING.md has no "Reading" type yet; the spec carries the working filenames Matt gave until a NAMING proposal settles it." No existing type fits. `Guided_Notes` follows the slides and is recall-only (SHULL-CHG-0023/0054). `Reference` is packet material usable on tests. `Study_Guide` is review, not first teaching. **B.** Without a U7 row, the name Matt asked for (`... - The Mole`) cannot be produced: `templates/_shull_name.py` gives no topic when there is no row, and a builder may never shorten the full title "The Mole & Chemical Quantities" (29 characters) on its own (NAMING §2). "The Mole" is 8 characters, inside the 20-character limit. |
| **Affected Agents** | Textbook Page Designer (builds it), Overseer (intake and filing), Librarian (files it), Auditor (checks the name). Secretary (implementation only, and only on approval). |
| **Affected Skills** | `naming` reads `standards/NAMING.md` and holds no copy of the list (checked for SHULL-CHG-0100; nothing has changed since). No skill text changes. |
| **Affected Courses** | **A.** All three. **B.** Chemistry only. |
| **Risk** | Low. (1) **Word collision, not a filename collision:** the pilot builder has a boxed "Reading Check" at the end of each section. That is a block inside the document, not a filename. (2) **Part B renames future U7 builds, not existing files.** Once the row exists, every Chemistry U7 unit-level name built afterwards gets the topic, e.g. a rebuilt Roadmap becomes `Unit 7 Roadmap - The Mole.pdf`. Files already in `output/chemistry/u07/` and on Drive keep their names. Renaming them is a separate, logged, confirmed operation (NAMING §5), not part of this record. (3) **The app's parser:** `app/curriculum.mjs` `documentTypes()` reads every backticked token from `**Types:**` up to the first blank line. The definition paragraph therefore has to stay separate from the Types line, after a blank line, as the `Roadmap` paragraph is. Otherwise its backticked names would show up as fake types. |
| **Recommendation** | Approve both parts. A and B can be decided separately. Declining A leaves the reading with no type in the grammar. Declining B gives `Unit 7 Reading.pdf` with no topic. |
| **Decision** | |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | |

---

## What changes, exactly

| File | Change | Part | Protected? |
|---|---|---|---|
| `standards/NAMING.md` §2 | Append `· \`Reading\`` to the Types line. Add the definition paragraph after the `Roadmap` paragraph, with a blank line before and after it. | A | Yes, Secretary only |
| `courses/chemistry/DECISIONS.md` "Short titles" | Insert `\| U7 \| The Mole \|` after the U1 row | B | Yes, Secretary only |
| `courses/chemistry/DECISIONS.md` "Decision log" | New entry at the top (draft below) | B | Yes, Secretary only |
| `templates/reading/build_reading_docx.py` lines 7–8 | Replace the "PILOT DOCUMENT TYPE ... until a NAMING proposal settles it" sentence with a pointer: "Document type `Reading`, `standards/NAMING.md` §2 (SHULL-CHG-0114)." This is a consequence of Part A and is named here, so it is not an unapproved bundled edit. | A | No |
| `templates/reading/specs/chem_u07_reading.json` `workingFilename.$comment` | Replace the "PENDING: ..." comment with "Names per standards/NAMING.md §2 (`Reading`) and the U7 short title in courses/chemistry/DECISIONS.md (SHULL-CHG-0114)." The two filename values do not change. | A + B | No |

### Code that does **not** need to change (checked)

| File | Why no change |
|---|---|
| `scripts/validate_codes.py` | It holds **no Type list**. It checks `U#/S#.#` codes and the "Short titles" table only. On the new row, line 100 skips the section-exists check because the code starts with `U`, and line 102 checks the length: "The Mole" is 8, under 20. The row passes as written. |
| `templates/_shull_name.py`, `templates/shull_name.cjs` | They accept any type string. `str(type_).replace("_", " ")` gives `Reading`. Only course-level names are restricted to `Reference` (line 69), and a Reading is never course-level. One caller obligation follows from lines 87–90: the helper makes a name unit-level only when it is passed **more than one** section. A Reading builder must pass the unit's full section list, which it already needs for the cover breakdown. This record adds no rule for a one-section unit. |
| `app/curriculum.mjs` | `documentTypes()` parses the Types line from NAMING.md, so `Reading` appears with no code change, provided the blank-line separation above is kept. |
| `app/server.mjs` `CONTENT` | Types with no entry show as `app:false, family:null` ("nothing builds here"). That is accurate: the reading is built from the repository, not the app. Wiring an app entry for `templates/reading/` would be a separate change. |
| `app/design.test.mjs` | It asserts five named types and at least 10 in total. Both still hold. |

## Draft decision-log entry (Part B, for the top of the Chemistry log)

```markdown
### YYYY-MM-DD — U7 short title
U7 The Mole & Chemical Quantities gets the short title "The Mole", so its unit-level files are named
`Unit 7 [Type] - The Mole`, starting with the unit reading (`Unit 7 Reading - The Mole`,
`Unit 7 Reading Key - The Mole`). Files already built under U7 keep their names until a confirmed,
logged rename. Decided by Matt YYYY-MM-DD ("<verbatim>").
Supersedes: None (new short-title row; no rule replaced).
Status: CONFIRMED · SHULL-CHG-0114
```

## Verification plan (for the implementer, after approval)

1. `git diff` touches only the five files in the table above, plus this record and its
   `change-log/CHANGELOG.md` row.
2. `python3 scripts/validate_codes.py` passes, and its output counts the new short-title row.
3. With `templates/_shull_name.py`, `document_name("Reading", ["7.1","7.2","7.3","7.4","7.5"], 7,
   unit_title=<U7 short title read from the decisions file>, ext="pdf")` returns
   `Unit 7 Reading - The Mole.pdf`, and with `key=True` returns `Unit 7 Reading Key - The Mole.pdf`.
4. `node --test app/design.test.mjs` passes, and `documentTypes()` on the edited NAMING.md
   returns the 14 types ending in `Reading`, with no extra token taken from the definition paragraph.
5. `python3 scripts/validate_references.py` and `python3 scripts/validate_change_ids.py` pass.
6. Fill in `Implemented By` with the commit SHA(s). Part A and Part B are labelled edits: two
   commits, or one commit whose message names both parts. Fill in `Verified` with the results.

## Not done by this record

No standard, course file, template or app file was edited. Implementation waits for a committed
record whose `Status:` reads APPROVED and whose `Decision:` quotes Matt verbatim
(`governance/CHANGE_CONTROL.md` §4). The main session records that decision.
