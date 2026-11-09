# SHULL-CHG-0066 — One worksheet entry may cover a span of sections (study guides)

> No known conflict with a LOCKED rule. Two CONFIRMED rules are amended **in part**, for an entry that
> opts in and nowhere else. One is SHULL-CHG-0019's "`sections` agrees with `sectionsContent`", which
> is reworded, not dropped. The other is the README's "Each section starts a new page". **One premise
> of the finding is contradicted by the builder:** the Time Walk table does not count as Geology
> visual work, so `proseOnly` is needed. See section 4. That is the one question for Matt (section 5).

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0066 |
| **Date** | 2026-11-09 |
| **Source** | User request, relayed by an Overseer routing pass, 2026-11-09. Matt wants a Geology Unit 2 study guide / unit summary covering 2.1–2.5: a "Big Ideas" fill-in-the-blank block and a compact period-by-period "Time Walk" table, about 3 pages and 4 at most. No verbatim quote of Matt's words was relayed, so none is given here. |
| **Current Rule** | See section 1, verbatim, with file and line. |
| **Proposed Rule** | See section 2. |
| **Supersedes** | In part, and only for an entry that sets `coversSections`: (1) `templates/worksheet/README.md` line 45, "Each section starts a new page."; (2) `templates/worksheet/README.md` line 180, rule 2, and the matching bullet of SHULL-CHG-0019 ("Mechanism, not documentation", lines 92-93), "`sections` agrees with `sectionsContent`". This one is reworded so a spanned entry contributes its listed codes. The rule stays one fact. (3) The behaviour of `templates/worksheet/build_worksheet_docx.py` lines 946-949, 989 and 1043-1056, and of `templates/worksheet/build_worksheet_key_docx.py` lines 147-149 and 162. If Matt answers Q1 with option A, it also supersedes in part (4) `templates/worksheet/README.md` line 37, which says what `proseOnly` is for (SHULL-CHG-0022, line 36). |
| **Reason** | The worksheet builder cannot produce this document. It requires one `sectionsContent` entry per code in `sections` (builder lines 946-949), and every entry starts a new page with its own header and Name / Date / Period / Score row (lines 1043-1056). A five-section study guide is therefore at least five pages against a target of three. Its Time Walk table, one continuous run of periods, would also be cut into pieces under 2.3, 2.4 and 2.5. The codes are real: Geology U2 has exactly five sections, `2.1`–`2.5` (`courses/geology/DECISIONS.md` lines 23-25), so this span is the whole unit. |
| **Affected Agents** | Designer (implements in `templates/` and builds the study guide). Auditor (`scripts/audit_worksheet.py` measures the spanned entry against its own `pagesPerSection`, unchanged; see section 2). Secretary (records). |
| **Affected Skills** | `build-document`: one pointer line to the README near line 93 (page budget), with no restatement. `build-assessment` "Study guides" (lines 57-61) is unchanged; its content rule (do not copy the assessment's questions) still governs what goes in the guide. |
| **Affected Courses** | All three, because the builder is shared. Only the Geology U2 study guide uses the option at first. |
| **Risk** | Low. It is opt-in and off by default: an entry without the key goes down the unchanged code path. The remaining risk is that a range header such as `S2.1-S2.5` claims every section in between. The gap check in section 2 covers that. |
| **Recommendation** | Approve section 2. Answer Q1 (section 5), which decides whether README line 37 changes too. The follow-ups in section 6 are out of scope and are **not** bundled here. |
| **Decision** | *(blank: recorded by the main session per `governance/CHANGE_CONTROL.md` §4)* |
| **Status** | **PENDING** |
| **Implemented By** | |
| **Verified** | *(blank. Plan in section 7.)* |

---

## 1. Current Rule (verbatim)

`templates/worksheet/build_worksheet_docx.py` lines 946-949. There must be one content entry per code:

```python
    declared = [s["code"] for s in sections]
    if declared != list(spec["sections"]):
        return refuse(f"sections {spec['sections']} but content for {declared}. "
                      "The two lists are the same fact and must agree.")
```

Lines 1043-1046 and 1055-1056. Every entry after the first gets a page break, a header, and an ID row:

```python
    for si, sec in enumerate(sections_to_build):
        if si:
            page_break(doc)
        header(sec, sec["title"], kind)
        ...
        gap(doc, 5)
        id_row(("NAME", "DATE", "PERIOD", "SCORE"), [3.05, 1.75, 1.10, 1.60], total)
```

Line 989. The header prints one code:

```python
        pp = para(hr, f"{unit} / S{sec['code']}", 11, bold=True, color=pal.accent,
```

`templates/worksheet/build_worksheet_key_docx.py` lines 147-149 (a page break per entry) and line 162
(`f"{unit} / S{sec['code']}"`) behave the same way.

`templates/worksheet/README.md` lines 44-45:

> Header → Name / Date / Period / **Score** → REMEMBER → BEFORE YOU START → equations →
> directions → question cards → close. Each section starts a new page.

`templates/worksheet/README.md` line 180, under "Rules the builder enforces rather than trusts":

> 2. `sections` and `sectionsContent` name the same sections — they are one fact.

`templates/worksheet/README.md` line 37:

> A sheet that genuinely is a reading response sets `"proseOnly": true` and is allowed through.

## 2. Proposed Rule

> A `sectionsContent` entry may set **`"coversSections": ["2.1", "2.2", "2.3", "2.4", "2.5"]`** to
> cover several sections of one unit as a single entry: one header, one Name / Date / Period / Score
> row, and one continuous page flow. An entry without the key builds exactly as before.

**Why a list and not a range string.** A list such as `"2.1-2.5"` would need parsing. A list also
names every code outright, so it can be checked one code at a time against the decisions file, the
same way `sections` already is.

**Validation.** Each of these refuses the build and names SHULL-CHG-0066. All apply only to an entry
that sets the key.

1. `coversSections` is a list of at least two codes, and the entry's `code` equals its first item.
   That keeps every existing use of `sec["code"]` (error messages, the audit's page-budget key)
   working without change.
2. **One fact, kept.** Flatten the entries in order: each entry contributes its `coversSections`,
   or `[code]` if it has none. The result must equal `spec["sections"]`. Rule 2 is reworded to say
   this. It is not dropped.
3. Every listed code exists in `courses/<course>/DECISIONS.md`. This is already enforced on
   `spec["sections"]` (lines 940-945) and needs no new code. See section 4, item 2, for how loose
   that check is.
4. **New:** every listed code belongs to `spec["unit"]`, which here means a `2.` prefix. The builder
   does not check this today for any spec. The check is added for spanned entries only, so existing
   specs are unaffected.
5. **New:** no gap. Every section of that unit in the decisions file that falls numerically between
   the first and last listed code must be listed. The header prints a range, so `S2.1-S2.5` must
   not quietly omit 2.3.

**Rendering.**

- Header, right cell: `U02 / S2.1-S2.5`. It uses a hyphen, the same form the running footer already
  builds at lines 959-960. The flattened text still begins `U02/S2.1`, so `audit_worksheet.py`'s
  section-start regex (line 66) finds it, and its per-entry `pagesPerSection` lookup (lines 46-49,
  keyed on `sec["code"]`) works unchanged. **No audit change is needed.**
- The type label comes from `docType` as now, giving `STUDY GUIDE`.
- Blocks render in spec order. A page breaks only where a block sets `pageBreakBefore`, which
  already exists. A long `table` repeats its header row on the next page (`w:tblHeader`, line
  534).
- The score total is summed over the one entry, as now.
- The key builder prints the same spanned header. Its `key.blocks` handling is unchanged.
- The entry declares its own budget: `"pagesPerSection": 3` for this guide. Four is Matt's ceiling
  for this document. It is not proposed as a builder rule.
- The filename needs no change. With several sections, `document_name()` already gives
  `Unit 2 Study Guide - <unit short title>` (`templates/_shull_name.py` lines 56-59; SHULL-CHG-0037,
  SHULL-CHG-0041). It files loose in the unit folder (`standards/DRIVE_ARCHITECTURE.md` line 84).

**Documentation.** The README changes in four places, each citing SHULL-CHG-0066. "The page shape"
gets: "Each section starts a new page, unless one entry covers a span (`coversSections`)."
"Section and spec options" gets the key. "Rules the builder enforces" rule 2 is reworded. The
profile table's Geology page-budget cell (line 24) gets a note that a spanned study guide declares
its own budget. `build-document` gets one pointer line to the README and nothing restated.

**Tests.** `scripts/validate_profiles.py` gains three refusals (a span that crosses units, a span
with a gap, `code` not equal to the first listed code). It also gains one allowance: a spanned
Geology study guide builds.

## 3. Who implements

The Designer edits `templates/` and `.claude/skills/build-document/` after approval. Neither is a
Secretary-only path (CLAUDE.md §4). The commit still carries SHULL-CHG-0066, as with
SHULL-CHG-0055, the precedent for an opt-in builder change made through a record. The Secretary
then fills `Implemented By` and `Verified`. Nothing in `brand/`, `standards/` or `courses/`
changes, so no course decision-log entry is needed.

## 4. What the builder and README contradict in the finding: stated plainly

1. **`proseOnly` is needed.** The Time Walk table does **not** count as Geology visual work. Only
   `diagram`/`draw` questions and the block kinds `cards`, `slots`, `draw`, `diagram`, `sort`,
   `match` and `outline` count (`build_worksheet_docx.py` lines 836-838). The refusal at line 848
   fires on any Geology section with none of these. `table` and `notes` are not on the list, and
   README line 23 says the same: "**required**: diagram, draw, cards, slots, sort, match or
   outline". A study guide made only of a `notes` Big Ideas block and a `table` Time Walk is refused
   unless it sets `"proseOnly": true`. The table is structured content in plain English, but not to
   the builder.
   - README line 37 and SHULL-CHG-0022 (line 36) describe `proseOnly` as the escape "for a sheet
     that genuinely is a reading response". A study guide is not that. Using the flag here works
     mechanically but widens its stated meaning, so Q1 asks Matt.
2. **"The builder already validates this" is true but loose.** `known_sections()`
   (`templates/_shull_docx.py` lines 78-81) is a regex that collects every `d.d` pattern in the
   decisions file above "## Course sequencing rules". It returns an unordered set. It checks that a
   code is mentioned, not that it is a live section of the right unit. That is why validation items
   4 and 5 are new, and why item 5 compares numbers instead of relying on file order.
3. **The key builder never checks that `sections` agrees with `sectionsContent`**
   (`build_worksheet_key_docx.py` lines 110-118). The student builder does. This record makes the
   key builder honour `coversSections` for the header only. It does **not** add the general check,
   because that would not be opt-in and could refuse existing specs. Reported as a separate finding
   (section 6).
4. **README profile table, line 24:** the Geology page budget is "**1** normally; 2 for a
   cut-and-glue". A 3–4 page study guide falls outside that stated norm. The budget is declared per
   spec and not enforced by the builder, so nothing refuses it, but the README needs the note in
   section 2.
5. **There is no fill-in-the-blank block in the worksheet builder.** Big Ideas can only be `notes`
   items with typed blanks. Their answers would have to be written again in `key.blocks` (the key
   renders only `table` and `notes`, lines 174-182). That puts the same sentence in the spec twice,
   which CLAUDE.md §1 forbids. Not fixed here (section 6).

## 5. Question for Matt (one, because the answer changes what is built)

**Q1. A Geology study guide is refused unless it has something visual or sets `proseOnly`. Which do
you want?**

- **A.** The study guide sets `"proseOnly": true`, and README line 37 adds "or a study guide" to
  what the flag is for. There is no builder change for this part. *(The finding's proposal.)*
- **B.** No rule change: the guide earns the visual requirement honestly. For example, the Time Walk
  becomes a `sort` (order the periods in place), or a few Big Ideas terms become a `match`. Either
  might cost page space against the 3-page target.

Not offered: counting `table` as visual work. That would change every Geology spec, would not be
opt-in, and would weaken SHULL-CHG-0022.

## 6. Out of scope: not bundled, each would be its own record

- A fill-in-the-blank block whose answers are stored once and drawn on both the student page and
  the key (section 4, item 5).
- The key builder's missing `sections` / `sectionsContent` agreement check (section 4, item 3).
- Tightening `known_sections()` to read each unit's listed codes instead of any `d.d` mention
  (section 4, item 2).

## 7. Verification plan (for `Verified:`)

1. Build every existing spec in `templates/worksheet/specs/` before and after the change. The
   output must be identical, or differ only in metadata. Opt-in means no existing sheet changes.
2. Build the Geology U2 study guide spec with `coversSections` 2.1–2.5. Run `audit_worksheet.py`
   against `pagesPerSection: 3`. Check by eye in a LibreOffice render: one header reading
   `U02 / S2.1-S2.5`, one Name / Date / Period / Score row, and the Time Walk table in one run with
   its header repeated on any continuation page.
3. Build the key from the same spec. Its header carries the same span.
4. `python3 scripts/validate_profiles.py`: the three new refusals fire and the new allowance holds.
   Then `npm test` and `audit_fonts.py` on the render.
5. Grep `templates/worksheet/README.md` and `.claude/skills/build-document/SKILL.md` for
   `coversSections`. Expect the README to define it and the skill only to point at it.
