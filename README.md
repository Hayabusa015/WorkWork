# SHULL OS

A source-controlled operating system for Matthew Shull's teaching workflow —
Chemistry, Physics, and Geology at James A. Garfield Local Schools.

**Status: Phase 8 of 14 — governance, design system, standards, and agents exist. Skills do not yet.**

Do not build classroom deliverables from this repository until Phase 14 passes. The installed
legacy SHULL skills are still the working system.

## What this repository is for

SHULL OS has five conceptual layers, and this repository is the first one:

| Layer | Lives in |
|---|---|
| **Operating system** — agents, skills, standards, workflows, governance | **This repository** |
| Curriculum — course-specific decisions | `courses/*/DECISIONS.md` (here) |
| Canonical file library — finished teaching documents | Google Drive, `SHULL Science/` |
| Execution — the agent workflow | Claude Code |
| Workspaces — subject context | Claude Projects (Chemistry, Physics, Geology) |

Google Drive is canonical for finished documents. This repository is canonical for the
system itself. Claude Projects are working context, not storage.

**The governing rule:** a fact lives in exactly one place. Where duplication is unavoidable,
the duplicate must point at the authoritative source.

## What exists

| | |
|---|---|
| `brand/` | `tokens.json` — the only place a hex is written, every colour carrying computed contrast and grayscale — plus the design system, the five archived palettes, and the Archivo fonts |
| `standards/` | Anti-slop, voice, naming, Drive architecture, QA gate |
| `governance/` | The two-layer rule, precedence, authority matrix, change control |
| `.claude/agents/` | All seven agents, validated against the authority matrix |
| `.claude/settings.json` | SessionStart hook that builds the environment |
| `legacy/` | Verbatim snapshot of the pre-migration system. Read only. |
| `config/drive.json` | Verified folder IDs, folder grammar, known filing defects |
| `scripts/` | `measure_tokens.py`, `validate_agents.py` |

**Not yet built:** the twelve skills, the workflows, the three course decisions files, the layer and
code validators, and the weekly review.

## The analysis behind it

Read in this order:

| Document | What it is |
|---|---|
| [`docs/SHULLOS_IMPLEMENTATION_PLAN.md`](docs/SHULLOS_IMPLEMENTATION_PLAN.md) | Environment inspection, recommended architecture, and the 14-phase build sequence |
| [`docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md`](docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md) | 267 rules extracted from 16 legacy sources, each classified |
| [`docs/CONFLICT_REPORT.md`](docs/CONFLICT_REPORT.md) | 28 conflicts found across the legacy system, severity-ranked |
| [`docs/SKILL_MIGRATION_MAP.md`](docs/SKILL_MIGRATION_MAP.md) | How each legacy skill decomposes into standards, skills, and agents |
| [`docs/DECISIONS_2026-09-07.md`](docs/DECISIONS_2026-09-07.md) | **Read with the conflict report.** Decisions resolving 6 of 7 critical conflicts |

## Decided

Values live in [`brand/tokens.json`](brand/tokens.json) — the only place a hex is written.

| | |
|---|---|
| Chemistry | Lab Lime + Aqua |
| Physics | Quantum Gold + Deep Purple |
| Geology | Terra Teal + Rust Orange |
| Background | White by default; Parchment as a special-purpose surface only |
| Typography | Trade Gothic Next, falling back to Archivo / Archivo Narrow |
| Coloured type on white | Each course's text-safe deep variant, never the display colour |
| Filenames | `SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor][_Version].[ext]`, zero-padded |
| Geology numbering | Plate Tectonics = U4 |
| Drive | Unchanged — `SHULL Science/`, Unit → Section → five content folders |

## Open — important, not blocking

- **CONFLICT-24** — Chemistry grading: gradebook weights vs. the "daily practice ~10%" framing.
- **CONFLICT-25** — whether Geology has section numbers at all. Blocks Geology renaming and the
  code validator.
- **CONFLICT-26** — the Gizmos rule vs. the built U1 materials that use one.
- **Q-13** — whether to add a `99 Archive/` folder to the Drive content folders.

## What has not happened

No legacy skill has been modified. No Google Drive object has been created, renamed, moved, or
deleted. No standard has been written as authoritative. All Drive access so far has been read-only.
