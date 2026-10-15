# Change ID renumbering, 2026-10-15

Two older branches (PR #1, the Drive retrofit; PR #2, the notes and worksheet work) were cut before
`main` reached change IDs 0023 to 0032 and reused those numbers for different records. Change IDs
are never reused, so their records were renumbered when the branches were brought up to date.

**PR #1** (`claude/gracious-galileo-drxzqh`)

| Was | Now | Record |
|---|---|---|
| `SHULL-CHG-0023` | `SHULL-CHG-0029` | unit level guided notes presentations |
| `SHULL-CHG-0024` | `SHULL-CHG-0030` | quiz unit level no homework folder |

**PR #2** (`claude/nice-fermat-vehaxv`)

| Was | Now | Record |
|---|---|---|
| `SHULL-CHG-0023` | `SHULL-CHG-0031` | lab master template |
| `SHULL-CHG-0024` | `SHULL-CHG-0032` | notes template retroactive |
| `SHULL-CHG-0025` | `SHULL-CHG-0033` | notes paged redesign |
| `SHULL-CHG-0026` | `SHULL-CHG-0034` | approval recording |
| `SHULL-CHG-0027` | `SHULL-CHG-0035` | drive unit folders |
| `SHULL-CHG-0028` | `SHULL-CHG-0036` | chem s1.4 fold |
| `SHULL-CHG-0029` | `SHULL-CHG-0037` | multi section filenames |
| `SHULL-CHG-0030` | `SHULL-CHG-0038` | notes old headers |
| `SHULL-CHG-0031` | `SHULL-CHG-0039` | selfcheck in work box |
| `SHULL-CHG-0032` | `SHULL-CHG-0040` | unit1 single day test |

On `main`, `SHULL-CHG-0023` to `SHULL-CHG-0028` are: notes are recall, short filenames, humanize skill,
the gws upload flow, the filing gate, and the reconcile-session-files skill.

The dated operation logs and audit reports under `reports/` still use the old numbers. They are history
and were not rewritten. Each renumbered record carries a note saying so.
