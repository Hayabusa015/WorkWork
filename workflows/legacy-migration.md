# Workflow — Legacy migration

How a legacy artifact becomes SHULL OS. Status and mapping:
`docs/SKILL_MIGRATION_MAP.md`.

---

## The rule

**Nothing is copied.** Every legacy artifact is decomposed:

```
LEGACY ARTIFACT
├── a RULE          → standards/ or brand/
├── a COURSE FACT   → courses/<course>/DECISIONS.md
├── a PROCEDURE     → .claude/skills/<skill>/SKILL.md
└── a DECISION      → governance/ + change-log/
                      or brand/palette-archive/ if superseded
```

A skill that "just needs a light edit" is one that was already obeying the one-fact-one-home rule.
Inspection found none that were.

## Order

1. **Snapshot first.** `legacy/` before any decomposition. Nothing can be lost after that point.
2. **Governance** — the rules for making rules.
3. **Tokens, design system, palette archive.**
4. **Remaining standards.**
5. **Course decisions** — Chemistry, then Physics, then Geology.
6. **Agents.** They can now point at something authoritative.
7. **Skills.** They can now point at both.
8. **Validators and hooks.**
9. **Workflows.**
10. **The weekly review, last.**

**Standards before agents, always.** An agent written before the standard it points at will invent
rules, which is the failure this whole system exists to prevent.

## Classification

Every extracted rule gets a `governance/GOVERNANCE.md` §4 label.
**Never silently convert CONFLICT, PROVISIONAL, or UNKNOWN into LOCKED.**

Where a rule is CONFLICT, the destination is **BLOCKED** and names the question. It does not get a
best guess.

## Preserving what was good

> **When revising an existing teacher-created file, preserve its useful personality and routines.**

This governs the migration, not just documents. The lab template is the worked example: its
structure, wording, blocks and locked rules were kept byte-for-byte, and only brand values moved.
The voice in it — *"'It changed' is not an observation"* — is the reason it exists and is not
something to regenerate.

## Retiring the legacy skills

**Not until T-7 passes.** Until then the ten installed SHULL skills stay installed and untouched;
they are still the working system. `legacy/` holds the byte-identical snapshot either way.
