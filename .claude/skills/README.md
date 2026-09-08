# Skills — how a repeatable task is performed

A skill states **procedure**. A standard states **rule**. Where a skill needs a rule, it links to
the standard. **No skill restates a hex, a font name, a margin, or a course fact** —
`scripts/validate_tokens.py` and `scripts/validate_layers.py` enforce that.

Skills are focused and reusable. Do not build a skill that tries to contain the whole system; that
is what the legacy `shull-studio` became, and decomposing it is most of this migration.

| Skill | Owns |
|---|---|
| `build-document` | Practice sets, guided and Cornell notes, study guides, Geology activities |
| `build-presentation` | Section decks from the twelve-layout template |
| `build-assessment` | Quizzes, tests, parallel versions, keys |
| `build-lab` | Lab handout and teacher key from the locked template |
| `apply-shull-design` | Applying tokens and the design system to a deliverable |
| `anti-ai-slop` | The quality pass, run before anything ships |
| `verify-content` | Scientific and curricular accuracy |
| `audit-deliverable` | The QA gate, run independently |
| `naming` | Filenames and document codes |
| `retrieve-drive-file` | Finding and reading in the Drive library |
| `shelve-drive-file` | Filing, folder creation, destination verification |
| `weekly-system-review` | The recurring health and learning review — report-only |

Enforced by `scripts/validate_layers.py` and `scripts/validate_tokens.py`, which run on the Stop
hook. A skill that restates a rule fails the build.
