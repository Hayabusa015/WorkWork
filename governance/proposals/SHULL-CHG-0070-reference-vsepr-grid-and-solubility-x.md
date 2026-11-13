# SHULL-CHG-0070 — Reference packet: VSEPR as a grid, and an X mark on the solubility grid

**Path A — a course change.** Only `courses/chemistry/DECISIONS.md` is affected, and within it only
items 3 and 9 of "## Reference packet contents" (the section set by SHULL-CHG-0068), plus one
decision-log entry on approval. No standard or skill is edited by this record. Both edits bring the
course file into line with what the built sheets already do and with what the user chose after the
`verify-content` review of 2026-11-10.

| Field | Value |
|---|---|
| **Change ID** | SHULL-CHG-0070 |
| **Date** | 2026-11-10 |
| **Source** | User, 2026-11-10, after the `verify-content` review of the built Chemistry reference packet. |
| **Current Rule** | `courses/chemistry/DECISIONS.md`, "## Reference packet contents", items 3 and 9, verbatim — see "Current Rule (verbatim)" below. |
| **Proposed Rule** | Replace items 3 and 9 with the text under "Proposed Rule (verbatim)" below. Item 3: VSEPR becomes a grid (rows 2–6 electron domains labelled with electron geometry, columns 0–3 lone pairs; hatched where no combination exists), same information, one landscape page. Item 9: cells are S / SS / I with stated thresholds, or X where the ions react instead of forming the compound; the rules summary is five rules plus one line explaining X. Nothing else in the section changes. |
| **Supersedes** | `courses/chemistry/DECISIONS.md` § "Reference packet contents", item 3 (VSEPR column list) and item 9 (three-way S/SS/I grid with a five-line summary), both as set by SHULL-CHG-0068. |
| **Reason** | (1) VSEPR: the built sheet is a grid; the course file describes a column table. The grid carries the same information on one landscape page, and the user chose it. (2) Solubility: `verify-content` (2026-11-10) found that X is chemically correct for cells such as Al2(CO3)3, Fe2S3, the Group 2 sulfides, FeI3 and CuI2, where the ions react with each other or with water instead of forming the compound. Marking those cells S, SS or I alone would misstate them. Until the course file says so, the built sheet contradicts its own source of truth (CLAUDE.md §2 precedence: the decisions file wins). |
| **Affected Agents** | None directly. Builders and checkers read the course file. |
| **Affected Skills** | `build-document` (builds against this list), `verify-content` (checks against this list). Neither skill file is edited: a search of `.claude/` for "VSEPR" and "solubility" finds nothing, so there is no stale copy to report. |
| **Affected Courses** | Chemistry. |
| **Risk** | low — two list items in one course file; the built sheets already match the proposed text, so nothing is rebuilt. |
| **Recommendation** | Approve. Both edits make the course file describe the sheets the user has already reviewed and kept. |
| **Decision** | User, 2026-11-10, in chat, answering the VSEPR layout question and judgement calls 1–7 (call 1 being "keep X"): "keep all, use the grid" |
| **Status** | **IMPLEMENTED** |
| **Implemented By** | 7204bf4 |
| **Verified** | yes — DECISIONS items 3 and 9 checked against the built sheets Reference - VSEPR Shapes.pdf and Reference - Solubility.pdf by the main session. Secretary check: the edited items 3 and 9 and the new decision-log entry in `courses/chemistry/DECISIONS.md` match this record's Proposed Rule and drafted entry word for word. |

---

## Current Rule (verbatim)

From `courses/chemistry/DECISIONS.md`, "## Reference packet contents":

```markdown
3. **VSEPR Geometry** — up to 6 electron domains. Columns: domains, bonding vs lone pairs,
   electron geometry, molecular geometry, bond angle, drawn shape.
```

```markdown
9. **Solubility Grid** — cations × anions (polyatomic anions included). Each cell is soluble,
   slightly soluble, or insoluble, marked by letter so it reads in greyscale. Plus a five-line
   rules summary.
```

## Proposed Rule (verbatim)

### Edit 1 — item 3

Replace the item 3 block above with

```markdown
3. **VSEPR Geometry** — a grid on one landscape page. Rows are 2–6 electron domains, each row
   labelled with its electron geometry; columns are 0–3 lone pairs. Each cell shows the drawn
   shape, molecular geometry, bonding and lone-pair counts, bond angle and AXE notation.
   Combinations that do not exist are hatched.
```

### Edit 2 — item 9

Replace the item 9 block above with

```markdown
9. **Solubility Grid** — cations × anions (polyatomic anions included). Each cell is S (soluble,
   >1 g/100 mL), SS (slightly soluble, 0.1–1 g/100 mL), I (insoluble, <0.1 g/100 mL), or X (the
   ions react with each other or with water instead of forming the compound — e.g. Al2(CO3)3,
   Fe2S3, Group 2 sulfides, FeI3, CuI2), marked by letter so it reads in greyscale. Plus a rules
   summary: five rules and one line explaining X.
```

Note on wording: the user stated the SS range as "0.1–1 g"; the "/100 mL" is carried over from the
S threshold in the same sentence so all three thresholds read in the same unit. If the user prefers
the shorter form, it changes no meaning.

## Context only — no edit

On the same `verify-content` review (2026-11-10) the user kept every other judgement call as built
("keep all"):

- Electronegativities: Pauling/CRC values (e.g. Pb 2.33), padded to 2 decimals.
- Specific heats: ice 2.06, steam 2.01.
- Sr(OH)2 marked SS on the solubility grid.
- Six strong acids on the Strong Acids & Bases sheet.
- Phosphite written PO3^3−.
- Ni3+ and Mn3+ listed on Metals with Multiple Charges.

Each is consistent with the current course-file text (items 5, 6, 8, 9, 11, 12 state no value that
contradicts them), so none needs an edit. They are recorded here so a later sweep does not
re-raise them as findings.

## Decision-log entry (append at the top of the Chemistry decision log on approval)

```markdown
### 2026-11-10 — Reference packet: VSEPR grid, solubility X mark
Sheet 3 (VSEPR Geometry) is a grid on one landscape page: rows 2–6 electron domains labelled with
electron geometry, columns 0–3 lone pairs, impossible combinations hatched; same information as
before. Sheet 9 (Solubility Grid) marks each cell S, SS, I, or X, where X means the ions react with
each other or with water instead of forming the compound; the rules summary gains one line
explaining X. Found by verify-content 2026-11-10; every other judgement call on that review was
kept as built. Full text in "Reference packet contents".
Supersedes: Reference packet contents, items 3 and 9 (SHULL-CHG-0068).
Status: CONFIRMED · SHULL-CHG-0070
```
