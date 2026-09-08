# Skills — how a repeatable task is performed

A skill states **procedure**. A standard states **rule**. Where a skill needs a rule, it links to
the standard. **No skill restates a hex, a font name, a margin, or a course fact** —
`scripts/validate_tokens.py` and `scripts/validate_layers.py` enforce that.

Skills are focused and reusable. Do not build a skill that tries to contain the whole system; that
is what the legacy `shull-studio` became, and decomposing it is most of this migration.

Planned: `build-document` · `build-presentation` · `build-assessment` · `build-lab` ·
`apply-shull-design` · `verify-content` · `audit-deliverable` · `retrieve-drive-file` ·
`shelve-drive-file` · `naming` · `weekly-system-review` · `anti-ai-slop`

*Status: not yet written. Phase 9.*
