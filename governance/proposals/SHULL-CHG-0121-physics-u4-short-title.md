# SHULL-CHG-0121 — Physics U4 short title "Work & Energy"

> **No conflict with a LOCKED rule.** One new row in a table that exists to take new rows, plus a
> decision-log entry. Nothing CONFLICT, PROVISIONAL or UNKNOWN is converted.
>
> **One layer: Path A, a course fact** (`governance/CHANGE_CONTROL.md` §1). A short title affects
> Physics only (CLAUDE.md §2 test). No standard, skill or template is touched.
>
> **Precedent:** SHULL-CHG-0116 (`governance/proposals/SHULL-CHG-0116-chem-u6-short-title.md`),
> the same change for Chemistry U6.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0121 |
| **Date** | 2026-11-26 |
| **Source** | User. Matt, main session, 2026-11-26. Asked "What short title should Physics Unit 4 files use? (The full title is too long for file names.)", with the option "Work & Energy (Recommended)" described as "Files: 'Unit 4 Reading - Work & Energy' and 'Unit 4 Reading Key - Work & Energy'.", Matt chose "Work & Energy (Recommended)". |
| **Current Rule** | `courses/physics/DECISIONS.md`, "Short titles": the only unit row is `\| U1 \| 1D Motion \|`, followed by section rows `0.4`, `1.1`–`1.4` and `3.1`. U4 has no row, so under the table's own rule ("A section or unit with no row here gets no topic in its filename") and `standards/NAMING.md` §2, a U4 unit-level file takes no topic, e.g. `Unit 4 Reading`. |
| **Proposed Rule** | In "Short titles", a new row directly after `\| U1 \| 1D Motion \|`, keeping unit rows together and in numeric order: `\| U4 \| Work & Energy \|`. A decision-log entry goes at the top of the Physics decision log (draft below). The curriculum-map unit title stays **"U4 · Work, Energy & Power"**, unchanged. |
| **Supersedes** | None. A new short-title row; no rule replaced. |
| **Reason** | Without a U4 row, the names Matt chose (`Unit 4 Reading - Work & Energy`, `Unit 4 Reading Key - Work & Energy`) cannot be produced: `templates/_shull_name.py` gives no topic when there is no row, and a builder may never shorten the full title "Work, Energy & Power" on its own (NAMING §2; "Short titles" preamble: "Never shorten a title automatically; add a row when the user approves one."). "Work & Energy" is 13 characters, inside the 20-character limit checked by `scripts/validate_codes.py` line 102. The row's code starts with `U`, so line 100 skips the section-exists check; the row passes as written. |
| **Affected Agents** | Textbook Page Designer and the Roadmap builder (names they produce), Overseer (intake and filing), Librarian (files under the new name), Auditor (checks the name). Secretary (implementation only, and only on approval). |
| **Affected Skills** | None. `naming` reads `standards/NAMING.md` and the decisions file and holds no copy of any short title. |
| **Affected Courses** | Physics only. |
| **Risk** | Low. (1) **Future builds only.** Once the row exists, every Physics U4 unit-level file built afterwards takes the topic: `Unit 4 <Type> - Work & Energy`, e.g. `Unit 4 Reading - Work & Energy` and `Unit 4 Reading Key - Work & Energy`. Files already built keep their names until a confirmed, logged rename (NAMING §5). (2) **No existing file is affected** as checked in this working tree: no `output/physics/u04/` files, and no Physics U4 entry in `reports/filing-queue.md`. (3) Section-level files (`4.1`–`4.4`) are unaffected; they have no rows and this record adds none. |
| **Recommendation** | Approve. Declining leaves U4 unit-level files with no topic (`Unit 4 Reading`). |
| **Decision** | 2026-11-26, user, in the main session, answering "What short title should Physics Unit 4 files use? (The full title is too long for file names.)" (option text: "Files: 'Unit 4 Reading - Work & Energy' and 'Unit 4 Reading Key - Work & Energy'."): "Work & Energy (Recommended)". |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | `6b51962e4cfc332605961d7ab17ea8cfe57678a1` (`courses/physics/DECISIONS.md` "Short titles" and "Decision log", and this record only). |
| **Verified** | Yes. Run by the main session (not the implementer), 2026-11-26. (1) `validate_codes.py` OK. (2) `validate_references.py` OK. (3) `validate_change_ids.py` OK. (4) `_shull_name`: `short_title('physics','U4')` = "Work & Energy"; `document_name` gives `Unit 4 Reading - Work & Energy.pdf` and `Unit 4 Reading Key - Work & Energy.pdf`. (5) The unit title line is unchanged: `**U4 · Work, Energy & Power**`. |

---

## What changes, exactly

| File | Change | Protected? |
|---|---|---|
| `courses/physics/DECISIONS.md` "Short titles" | Insert `\| U4 \| Work & Energy \|` on a new line between `\| U1 \| 1D Motion \|` and `\| 0.4 \| Physics Graphing \|` | Yes, Secretary only |
| `courses/physics/DECISIONS.md` "Decision log" | New entry at the top, above "2026-11-12 — Lab equipment inventory" (draft below) | Yes, Secretary only |

Not changed: the curriculum-map line `**U4 · Work, Energy & Power** — 4 sections`, the U4 section
titles, the Drive folder name `Unit 04 - Work, Energy & Power`, and every other file.

## Draft decision-log entry (for the top of the Physics log)

The quoted words are the ones in the Decision field once the main session records it; the implementer
copies them from there, verbatim.

```markdown
### 2026-11-26 — U4 short title
U4 Work, Energy & Power gets the short title "Work & Energy", so its unit-level files are named
`Unit 4 [Type] - Work & Energy`, e.g. `Unit 4 Reading - Work & Energy` and
`Unit 4 Reading Key - Work & Energy`. The unit title stays "Work, Energy & Power". Files already built
under U4 keep their names until a confirmed, logged rename. Decided by Matt 2026-11-26 ("Work & Energy
(Recommended)"), answering the question on the Physics U4 short title.
Supersedes: None (new short-title row; no rule replaced).
Status: CONFIRMED · SHULL-CHG-0121
```

## Verification plan (for a checker other than the implementer, after approval)

1. `git diff` of the implementing commit touches only `courses/physics/DECISIONS.md` (the two edits
   above), plus this record's `Implemented By`/`Verified` and its `change-log/CHANGELOG.md` row.
2. `python3 scripts/validate_codes.py` passes, with no Short titles error for U4.
3. With `templates/_shull_name.py`: `short_title('physics','U4')` returns `Work & Energy`;
   `document_name("Reading", ["4.1","4.2","4.3","4.4"], 4, unit_title="Work & Energy", ext="pdf")`
   returns `Unit 4 Reading - Work & Energy.pdf`; with `key=True`, `Unit 4 Reading Key - Work & Energy.pdf`.
4. The curriculum-map line still reads `**U4 · Work, Energy & Power**`.
5. `python3 scripts/validate_references.py` and `python3 scripts/validate_change_ids.py` pass.
6. Fill in `Implemented By` with the commit SHA and `Verified` with the results.
