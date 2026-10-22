# schemas

Machine-readable shapes for things the system produces.

| Schema | Validates |
|---|---|
| `change-proposal.schema.json` | A Secretary change record |
| `task-report.schema.json` | A completion report — WORK COMPLETE requires a verified artifact at a verified path |

*Status: written (Phase 8–11). Both schemas are behaviour-tested by `validate_schemas.py`, not
merely valid JSON Schema.*
