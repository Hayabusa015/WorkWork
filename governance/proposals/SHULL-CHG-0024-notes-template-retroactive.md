# SHULL-CHG-0024 — Retroactive record: seven unrecorded guided-notes template commits

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0024 |
| **Date** | 2026-09-23 (record written). The changes themselves were committed 2026-09-16 to 2026-09-23 — see §3. |
| **Source** | User — six of the seven commits were made on the user's direct instruction (verbatim in §3). **Not all of it is user-sourced:** `2a02a58` had no user instruction, and the protect fix in `e59ba21`, the must-write border fix in `f76fea6` and the `borders()` schema fix in `4234b69` were the orchestrating session's own bug fixes, found while verifying. |
| **Current Rule** | See §1 — verbatim, from `governance/proposals/SHULL-CHG-0014-guided-notes-template.md` and `templates/notes/README.md` |
| **Proposed Rule** | See §3 — the seven changes as already committed. **This record proposes nothing new.** It asks the user to acknowledge changes that were applied without a record. |
| **Supersedes** | Parts of SHULL-CHG-0014 — see §4. Named individually there; nothing in 0014 is superseded in full. |
| **Reason** | Seven commits changed the shared guided-notes template, which all three courses build from — a Path B build change under `governance/CHANGE_CONTROL.md` §1 — and none went through a change record, carried a Change ID, or appeared in `change-log/CHANGELOG.md`. See §2. |
| **Affected Agents** | Designer (builds from this template; is rebuilding it now under SHULL-CHG-0025). Auditor (no pass was run — see §5). Secretary (this record). |
| **Affected Skills** | `build-document` — the notes template it builds from changed. `templates/notes/README.md` describes none of the seven changes (§6, finding 3). |
| **Affected Courses** | All three — Chemistry, Physics, Geology. The template is shared. The worksheet builders share `templates/_shull_docx.py` and are also touched (§6, finding 2). |
| **Risk** | **Medium** as a change (shared template, three courses). As a process failure, the risk is not the diffs — it is that a reading of the rules existed under which a build change for all three courses needed no record. |
| **Recommendation** | Acknowledge the record as written. **Do not rewrite git history** — no amend, rebase, or force-push; §2 says why. Treat SHULL-CHG-0025 as the change that settles the template's final form. Several of these seven changes are reversed there. Consider an Auditor pass on the template as it stands after 0025 lands, since none was run on these seven. |
| **Decision** | **Approved by the user, 2026-09-23**, in the main session. Verbatim: *"yes approve 0024 too"*. Recorded under SHULL-CHG-0026. |
| **Status** | **IMPLEMENTED** (2026-09-23. The seven commits predate the record; see Implemented By) |
| **Implemented By** | `ed41fa0` · `e59ba21` · `2a02a58` · `fcdd544` · `f76fea6` · `9766298` · `4234b69` (full SHAs in §3). **These were committed before this record existed.** That is the defect this record documents. It is not a normal implementation. |
| **Verified** | **Partly, by the session that made the changes. Not independently.** See §5. The orchestrating session reports running four checks: `pdffonts` showing Archivo only, a `scripts/audit_print_ink.py` pass, a rebuild of the Geology and Physics specs for backward compatibility, and visual inspection. **No independent Auditor pass was run on any of the seven commits.** The Secretary did not re-run any of these checks for this record. **Update 2026-09-23:** the seven commits themselves stay unverified by any independent check, and that gap is permanent. SHULL-CHG-0025 (`71e5e05`) has since replaced most of what they added (0025 §4). 0025's template did pass an independent Auditor with no blocking rows, as the `71e5e05` commit message records. What survives from these seven commits into 0025 (0025 §4, "Not superseded") was covered by that pass as part of the current template. |

---

## 1. Current Rule — verbatim, as it stood before `ed41fa0`

### 1a. `governance/proposals/SHULL-CHG-0014-guided-notes-template.md`, "What is preserved"

> - The section rhythm: header bar → learning target → Cornell rows → summary box.
> - **The closed-notes summary** — "close your notes before you write this" — and the self-check.
> - The unit wrapper: brand bar, name/date/period, targets ∥ key terms, "how these notes work",
>   section checklist.
> - The close: "pulling it together", checklist, big picture, **"still fuzzy on"**.

### 1b. SHULL-CHG-0014, Finding 1 (palette table, must-write row)

> | **Must-write rule** | **sage green** | Geology `primary` (Terra Teal) — a fill/rule, never type |

### 1c. SHULL-CHG-0014, Finding 4

> Fixed by replacing every fill with a rule: the brand bar, section heads and close banner are now a
> hairline above and a heavy accent rule below; the cue column is separated by its border alone, which
> is the Cornell convention anyway. Hierarchy is unchanged.

### 1d. `templates/notes/README.md`, "The structure, and why it is this way"

> - **Section rhythm:** header bar → learning target → Cornell rows → summary.
> - **Must-write:** prefix a notes line with `*` in the spec. It renders as an accent rule down the
>   left. One per idea — not one per line.

*(Read from the working tree on 2026-09-23. It describes none of the seven changes, so it appears
the README was not updated with them. The Secretary had no shell in this session and could not
check this against `git show`. See §6, finding 3.)*

### 1e. `governance/proposals/SHULL-CHG-0018-cue-column.md`, Decision 1 — context for `9766298`

> **The split is 1.28 in / 6.22 in.** The cue is a prompt, not a second body column.

---

## 2. What went wrong — stated plainly

Between 2026-09-16 and 2026-09-23, seven commits changed `templates/notes/build_notes_docx.py` and
`templates/_shull_docx.py`. All three courses use that template. This is a **Path B build change**
under `governance/CHANGE_CONTROL.md` §1: *"A change record is written, approved, and only then
applied."*

- **None of the seven commits went through a change record.**
- **None carries a Change ID.** §6 requires one: *"One change, one commit, and the Change ID in the
  message."*
- **None is in `change-log/CHANGELOG.md`.**
- **Several commits bundle more than one change.** `4234b69` carries seven distinct changes.
  `e59ba21`, `fcdd544` and `f76fea6` each carry two or three. That also breaks §6's "one change, one
  commit".

**How it happened.** The orchestrating session made the edits directly, on the user's instruction.
It reasoned that `templates/` is not one of the four Secretary-gated directories (`brand/`,
`standards/`, `governance/`, `courses/`). That reading is true about *who may write the file*. It
skipped the sentence that opens `CHANGE_CONTROL.md`:

> **Any permanent change** to brand, palette, typography, design standards, agent responsibilities,
> skill behaviour, governance, or a course-wide convention **must be recorded.**

A change to the shared notes template is a course-wide convention in all three courses at once. It
had to be recorded, whichever directory the file sits in. **The user caught this. The session did
not.**

**History is not rewritten.** This follows the precedent in `change-log/CHANGELOG.md`, "A known gap
in this log's own coverage": rewriting history so the commits carry an ID they never had *"would be
forging an audit log to make it look like it was always followed."* The seven SHAs stay as they
are. This record points at them, and the gap is recorded going forward.

---

## 3. Proposed Rule — the seven changes, as committed

Dates are commit dates (UTC), taken from the reflog. The user's words are verbatim, typos included.

| # | SHA | Date | Change | User's words |
|---|---|---|---|---|
| 1 | `ed41fa01268a2c2543623fc66346967c37634af5` | 2026-09-16 | Each section starts on a new page. The front matter becomes a standalone title page. New optional `titleImage` spec field (Bohr model). | "Each new section shpuld start in a new page. The first oage should be a thorough title page. Add thisnimage of the board model on the title page" |
| 2 | `e59ba216648b7d86aee794f4a00182ace2d5b103` | 2026-09-16 | New shared `fillin_table()` primitive and a per-row `"table"` spec key. `one_cell(protect=True)` stops the section summary box splitting across pages. | "Can you add tables and charges where necessary... Apply graphic organizers when possible. Don't just needlessly add more boxes to fill in. Allow students to compartmentalize items that belong together and to reduce length of notes" — *the `protect` fix was the orchestrator's own bug fix, made while verifying, not asked for* |
| 3 | `2a02a58a9efda534a63dcd67ee68a59b62aa143c` | 2026-09-16 | The closing "pulling it together" box is protected from splitting. A single orphaned line was landing on a blank page. | **No user instruction.** A bug fix found during verification. |
| 4 | `fcdd5440f1cb7e0bd4de67bf1d0156ae63ea090e` | 2026-09-16 | `add_watermark()`: a floating behind-text header image on every page. It also pulls `header_distance` in to the top margin, which fixed a spurious blank page. `study_recap_page()`: a standing last page, with a soft warning when absent. | "Add this as a faint watermark on all pages." / "On the last page of the notes, can we have like a nice little recap infographic of the entire guided notes chapter... Always have a single last oage with this -topic breakdown - key points - consuming points - things to remember" |
| 5 | `f76fea600f2902ce2785889868cf785cfa6cf74d` | 2026-09-17 | Capture-not-synthesis content pass (`DEFINE:` / `Fill in:` / `Copy:` prompts). New `matter_flowchart()`. The must-write accent bar moves from a paragraph border, which LibreOffice did not render, to a cell border. | "the guided notes are just there so that the children can write down what's on the board while also paying attention at the same time and kind of be prompted for what to write... if there's a matter flow chart, I kind of just want them to fill in their own matter flow chart on the paper... a prompt that has like the word and then it says define" |
| 6 | `97662984bb4b1b9f8939054e52c9997def81bdd6` | 2026-09-17 | A rule line under each cue question. A standing "EXTRA — anything else from the slide" box on every row. | "so on these, give recall, also add box to add anything from the slide 'Extra'" |
| 7 | `4234b695ca87eaa5438c993cb6e02d618b6c9387` | 2026-09-23 | Visual pass. The watermark goes to 3 in wide, 80% of the way down the page, with ink measured. The cue column gets an accent rail. Border weights become a named ladder. Rows get numerals. EXTRA is demoted to grey. The title image is framed. `borders()` schema fix: it was writing duplicate `w:tcBorders`. | "Make these look a bit 'prettier' the ui design is a bit lacking in the slides. Maybe siding could improve? I'm not sure." |

---

## 4. Supersedes — which parts of SHULL-CHG-0014 these changed

| SHULL-CHG-0014 said | Changed by | Now |
|---|---|---|
| Unit wrapper on page 1: *"brand bar, name/date/period, targets ∥ key terms, 'how these notes work', section checklist"* | `ed41fa0` | A standalone title page, with an optional image |
| Section rhythm *"header bar → learning target → Cornell rows → summary box"*, flowing continuously | `ed41fa0` | The same rhythm, but every section starts on a new page |
| The close: *"'pulling it together', checklist, big picture, 'still fuzzy on'"* as the end of the packet | `fcdd544` | Still there, but no longer last. A standing Study Recap page follows it. |
| Cornell rows are cue plus notes lines, and nothing else (implicit in 0014 "What is preserved") | `e59ba21`, `f76fea6`, `9766298` | A row may also carry a fill-in table or the matter flowchart, and always carries an EXTRA box |
| Must-write: course `primary` rule down the left (Finding 1), drawn as a paragraph border | `f76fea6` | Same colour, drawn as a cell border |
| Finding 4: *"the cue column is separated by its border alone"* | `4234b69` | The cue column also carries a course-accent rail |
| Finding 4: *"a hairline above and a heavy accent rule below"*, weights unnamed | `4234b69` | A named border-weight ladder |
| No watermark on notes pages (0014 is silent. `brand/SHULL_DESIGN_SYSTEM.md` §8 governs opacity.) | `fcdd544`, `4234b69` | A header image watermark on every page |

**Also touched, outside 0014.** `9766298` puts a rule line, which is a write surface, inside the cue
column. SHULL-CHG-0018 narrowed that column because *"the cue is a prompt, not a second body
column."* The 1.28 in width was not changed. But the column's stated purpose was, and no record says
so. This is recorded here and not resolved. SHULL-CHG-0025 removes those lines.

---

## 5. Verification — at the time, and what is missing

What the orchestrating session reports running. **The Secretary has not seen the output and did
not re-run anything.** No output from these checks is in `reports/` or anywhere else in the
repository.

| SHA | `pdffonts`: Archivo only | `audit_print_ink.py` | Geology + Physics specs rebuilt (backward compatibility) | Visual inspection | Independent Auditor pass |
|---|---|---|---|---|---|
| `ed41fa0` | Reported pass | Reported pass | Reported done | Orchestrating session | **None** |
| `e59ba21` | Reported pass | Reported pass | Reported done | Orchestrating session. The summary-box split was found this way. | **None** |
| `2a02a58` | Reported pass | Reported pass | Reported done | Orchestrating session. The orphaned-line blank page was found this way. | **None** |
| `fcdd544` | Reported pass | Reported pass | Reported done | Orchestrating session | **None** |
| `f76fea6` | Reported pass | Reported pass | Reported done | Orchestrating session. The unrendered must-write border was found this way. | **None** |
| `9766298` | Reported pass | Reported pass | Reported done | Orchestrating session | **None** |
| `4234b69` | Reported pass | Reported pass | Reported done | Orchestrating session | **None** |

**What this verification does not cover:**

- **No independent check.** Every check was run by the session that made the change. That is part
  of the gap, not separate from it.
- **The new features were not exercised by an in-repo spec.** The backward-compatibility rebuild
  used `templates/notes/specs/geo_u01_s01.2-s01.4.json` and `phys_u01_s01.1-s01.4.json`. Neither
  uses `titleImage`, the `"table"` key, the flowchart or the recap page. No Chemistry notes spec is
  in `templates/notes/specs/` as of 2026-09-23. So the rebuild shows the old specs still build. It
  does not show that the new features render correctly from anything in the repository.
- **The worksheet builders were not listed as rebuilt.** See §6, finding 2.

---

## 6. Findings

### Finding 1 — the code cited the wrong Change IDs

Comments added in these commits cite Change IDs that already belong to other, unrelated
proposals that have been implemented:

| Comment cites | For | That ID actually is |
|---|---|---|
| `SHULL-CHG-0018` | Title page. Study-recap page. | Cue-column narrowing — `governance/proposals/SHULL-CHG-0018-cue-column.md` |
| `SHULL-CHG-0019` | Matter flowchart | Worksheet template — `governance/proposals/SHULL-CHG-0019-worksheet-template.md` |
| `SHULL-CHG-0020` | Recall lines. EXTRA box. | Master Physics layout — `governance/proposals/SHULL-CHG-0020-master-physics-layout.md` |

As read in the working tree on 2026-09-23, they sit at `templates/notes/build_notes_docx.py` lines
34 (0019), 288 (0018), 384 and 445 (0020), and 490 and 500 (0018). Line 500 is inside a printed
warning, so the wrong ID also reached build output.

**This is worse than no citation.** An absent ID sends a reader looking. A wrong ID sends them to a
real record that seems to answer the question and does not. The audit trail in the code pointed at
the wrong records.

**Status: being corrected.** The designer agent rebuilding the template under SHULL-CHG-0025 is
removing these mis-citations. The Secretary has not verified that removal. It should be checked when
0025 is implemented.

### Finding 2 — the shared primitives also reach the worksheet template

`borders()` (schema fix, `4234b69`) and `one_cell()` (the `protect` parameter, `e59ba21`) live in
`templates/_shull_docx.py`. Both are also imported by `templates/worksheet/build_worksheet_docx.py`
and `templates/worksheet/build_worksheet_key_docx.py` (SHULL-CHG-0019). The `borders()` fix changes
the XML every worksheet cell border is written with. The reported verification names the notes specs
only. **The Secretary has no evidence the worksheets were rebuilt and checked after `4234b69`.**
Recorded as unverified. It is not claimed to be broken.

### Finding 3 — the README was not updated

`templates/notes/README.md` still describes the pre-change template. It has no title page, no
watermark, no recap page, no fill-in tables and no EXTRA box, and it does not mention the new spec
keys. A reader who trusts the README gets the old template. The designer is updating it under
SHULL-CHG-0025.

### Finding 4 — the fill-in table and an existing open question

The CHANGELOG has an open question: *"Notes specs cannot express a table inside a Cornell cell — his
Physics equation table flattened to text"* (SHULL-CHG-0016). `e59ba21`'s `"table"` key may answer
it. **It is not closed here.** Nobody has checked that the new key can express his Physics 4×2
equation table.

---

## 7. What in `CHANGE_CONTROL.md` a retroactive record cannot satisfy

| Requirement | Why it cannot be met |
|---|---|
| §1 Path B — *"written, approved, and only then applied"* | The changes were applied first. Nothing written now can restore that order. |
| §6 — the Change ID in the commit message | The seven commits have none. Adding one means rewriting history, which is declined in §2. |
| §6 — one change, one commit | Four of the seven commits bundle changes. They cannot be split without rewriting history. |
| §3 — IMPLEMENTED means *"applied, with a commit SHA and a verification note"* | The SHAs exist, but the status is PENDING because the user has not acknowledged the record. The status table has no state for "applied without approval". This record uses PENDING and says why. It does not invent a status. |
| §2 `Verified:` — *"a change is not done until it has been checked"* | Checked only by the session that made the changes. No output was kept. No Auditor pass. |
| §5 — decision-log entry at the top of the affected course's log | Not written. This record may not edit `courses/`. The entry would also be premature before acknowledgement. Earlier template records (0014 to 0020) set no precedent for per-course entries on a shared-template change. |
