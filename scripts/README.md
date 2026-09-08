# scripts — enforcement

| Script | Fails the build when |
|---|---|
| `validate_layers.py` | A course fact (unit title, section code, calendar date, grading percentage) appears in a skill |
| `validate_codes.py` | A `U#/S#.#` code appears anywhere without existing in the matching `courses/*/DECISIONS.md` |
| `validate_tokens.py` | A raw hex value is typed outside `tokens.json` |
| `publish_standards.py` | — publishes `standards/` and `brand/` to Drive `_Brand/Standards/`, one direction only |

`legacy/` is excluded from every validator.

These three checks would have caught, respectively: the Chemistry skill that was ordered trimmed
and never was; the Geology numbering offset, before a packet printed with the wrong footer; and
every palette conflict in the system, all of which came from the same hex being typed into two
files by hand.

*Status: not yet written. Phase 9.*
