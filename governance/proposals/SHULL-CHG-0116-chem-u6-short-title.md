# SHULL-CHG-0116 — Chemistry U6 short title "Nomenclature"

> **No conflict with a LOCKED rule.** One new row in a table that exists to take new rows, plus a
> decision-log entry. Nothing CONFLICT, PROVISIONAL or UNKNOWN is converted.
>
> **One layer: Path A, a course fact** (`governance/CHANGE_CONTROL.md` §1). A short title affects
> Chemistry only (CLAUDE.md §2 test). No standard, skill or template is touched.
>
> **ID note.** The Secretary that drafted this record has no shell and could not `git fetch origin
> main`. 0116 is the next integer after the highest record in the local checkout (SHULL-CHG-0115) on
> branch `claude/ecstatic-pascal-9cro1w`, which the main session reported up to date with `main`
> through SHULL-CHG-0115. Nothing outside `legacy/` mentions 0116 or higher. Under §2 the ID is real
> only once this file is pushed to `origin/main`; the main session confirms that before citing it.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0116 |
| **Date** | 2026-11-25 |
| **Source** | User. Matt, main session, 2026-11-25, while planning the Chemistry U6 unit reading. SHULL-CHG-0099 (`governance/proposals/SHULL-CHG-0099-chemistry-u6-four-sections.md`, lines 28–29) left the U6 short title open, with `Nomenclature` suggested. Decision D2 of the U6 reading plan asked: "U6 short title for the file name — Recommendation: 'Nomenclature', so the file is 'Unit 6 Reading - Nomenclature'. Apply it to the unfiled U6 Roadmap too." Matt answered: "Yeah do that". Asked separately whether to rename the unit to "Molecular Nomenclature", he answered: "Keep 'Chemical Nomenclature'". |
| **Current Rule** | `courses/chemistry/DECISIONS.md`, "Short titles": the unit rows are `\| U1 \| Matter & Atoms \|` and `\| U7 \| The Mole \|`. U6 has no row, so under the table's own rule ("A section or unit with no row here gets no topic in its filename") and `standards/NAMING.md` §2, a U6 unit-level file takes no topic: `output/chemistry/u06/Unit 6 Roadmap.pdf`. |
| **Proposed Rule** | In "Short titles", a new row directly after `\| U1 \| Matter & Atoms \|`, keeping unit rows in numeric order: `\| U6 \| Nomenclature \|`. A decision-log entry goes at the top of the Chemistry decision log (draft below). The curriculum-map unit title stays **"U6 Chemical Nomenclature"**, unchanged. |
| **Supersedes** | None. A new short-title row; no rule replaced. (It closes the open item in SHULL-CHG-0099 lines 28–29, which added no row.) |
| **Reason** | Without a U6 row, the name Matt asked for (`Unit 6 Reading - Nomenclature`) cannot be produced: `templates/_shull_name.py` gives no topic when there is no row, and a builder may never shorten the full title "Chemical Nomenclature" (21 characters, one over the limit) on its own (NAMING §2; "Short titles" preamble). "Nomenclature" is 12 characters, inside the 20-character limit checked by `scripts/validate_codes.py` line 102. The row's code starts with `U`, so line 100 skips the section-exists check; the row passes as written. |
| **Affected Agents** | Textbook Page Designer and the Roadmap builder (names they produce), Overseer (intake and filing), Librarian (files under the new name), Auditor (checks the name). Secretary (implementation only, and only on approval). |
| **Affected Skills** | None. `naming` reads `standards/NAMING.md` and the decisions file and holds no copy of any short title. |
| **Affected Courses** | Chemistry only. |
| **Risk** | Low. (1) **Future builds only.** Once the row exists, every Chemistry U6 unit-level file built afterwards takes the topic: `Unit 6 Reading - Nomenclature`, `Unit 6 Reading Key - Nomenclature`, `Unit 6 Roadmap - Nomenclature.pdf`. Files already built keep their names until a confirmed, logged rename (NAMING §5). (2) **One unfiled file is affected:** `reports/filing-queue.md` line 14 lists `output/chemistry/u06/Unit 6 Roadmap.pdf` (status Ready, not filed). Filed as-is after this change, it would carry a name that no longer matches the rule. See "Follow-up". (3) `templates/unit-roadmap/specs/chem_u06.json` carries no filename or title (its `_comment` says titles come from the decisions file), so no spec edit is needed. |
| **Recommendation** | Approve. Declining leaves U6 unit-level files with no topic (`Unit 6 Reading.pdf`). |
| **Decision** | PENDING. Recorded by the main session only (`governance/CHANGE_CONTROL.md` §4). |
| **Status** | **PENDING** |
| **Implemented By** | — |
| **Verified** | — |

---

## What changes, exactly

| File | Change | Protected? |
|---|---|---|
| `courses/chemistry/DECISIONS.md` "Short titles" | Insert `\| U6 \| Nomenclature \|` on a new line between `\| U1 \| Matter & Atoms \|` and `\| U7 \| The Mole \|` | Yes, Secretary only |
| `courses/chemistry/DECISIONS.md` "Decision log" | New entry at the top, above "2026-11-24 — U7 short title" (draft below) | Yes, Secretary only |

Not changed: the curriculum-map line `**U6 Chemical Nomenclature** (6 section codes, 4 taught)`, the
U6 section titles, and every other file.

## Draft decision-log entry (for the top of the Chemistry log)

The quoted words are the ones in the Decision field once the main session records it; the implementer
copies them from there, verbatim.

```markdown
### 2026-11-25 — U6 short title
U6 Chemical Nomenclature gets the short title "Nomenclature", so its unit-level files are named
`Unit 6 [Type] - Nomenclature`, e.g. `Unit 6 Reading - Nomenclature` and
`Unit 6 Roadmap - Nomenclature.pdf`. The unit title stays "Chemical Nomenclature". Files already built
under U6 keep their names until a confirmed, logged rename. Decided by Matt 2026-11-25 ("Yeah do
that"), answering the plan's question on the U6 short title; he also chose to keep "Chemical
Nomenclature" ("Keep 'Chemical Nomenclature'").
Supersedes: None (new short-title row; no rule replaced).
Status: CONFIRMED · SHULL-CHG-0116
```

## Verification plan (for a checker other than the implementer, after approval)

1. `git diff` of the implementing commit touches only `courses/chemistry/DECISIONS.md` (the two edits
   above), plus this record's `Implemented By`/`Verified` and its `change-log/CHANGELOG.md` row.
2. `python3 scripts/validate_codes.py` passes, with no Short titles error for U6.
3. With `templates/_shull_name.py`: `short_title('chemistry','U6')` returns `Nomenclature`;
   `document_name("Reading", ["6.1","6.2","6.3","6.4"], 6, unit_title="Nomenclature", ext="pdf")`
   returns `Unit 6 Reading - Nomenclature.pdf`; with `key=True`, `Unit 6 Reading Key - Nomenclature.pdf`;
   and the Roadmap equivalent returns `Unit 6 Roadmap - Nomenclature.pdf`.
4. The curriculum-map line still reads `**U6 Chemical Nomenclature**`.
5. `python3 scripts/validate_references.py` and `python3 scripts/validate_change_ids.py` pass.
6. Fill in `Implemented By` with the commit SHA and `Verified` with the results.

## Follow-up (not part of this record)

The unfiled U6 Roadmap (`reports/filing-queue.md` line 14, `output/chemistry/u06/Unit 6 Roadmap.pdf`)
should be rebuilt, or renamed under a logged, confirmed rename, so it carries the topic
(`Unit 6 Roadmap - Nomenclature.pdf`) before it is filed. That is classroom work and routes through
the Overseer (CLAUDE.md §6). This record does not touch the file or the queue.
