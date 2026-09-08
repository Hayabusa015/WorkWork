# legacy — READ ONLY

Verbatim snapshots of the pre-migration system, taken 2026-09-07/08 before any decomposition began.

**Never edit anything in this directory.** It is excluded from every validator. Its purpose is that
the migration is reproducible and that "we changed X from Y" is provable.

| Directory | Contents |
|---|---|
| `skills/` | The ten installed SHULL skills, copied byte-identical from the account skill bucket |
| `drive-standards/` | Standards documents retrieved read-only from Google Drive `_Brand/Standards/` |

## Why the skills snapshot matters

Skills were installed through the Claude UI, and **a reinstall overwrote user edits once.** There
was no version history and no diff between what was intended and what was installed. Some content —
notably the colour memo appended below `shull-studio` §7 with no heading and no date — arrived by
paste and would not have survived another reinstall.

## A note on the Drive snapshots

Retrieved through the Drive connector, which returns markdown with escaped punctuation. The escapes
have been normalised so the files are readable markdown; the wording is unchanged. Byte-identical
copies remain in Drive.
