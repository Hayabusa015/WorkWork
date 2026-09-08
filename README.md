# SHULL OS

A source-controlled operating system for Matthew Shull's teaching workflow —
Chemistry, Physics, and Geology at James A. Garfield Local Schools.

**Status: Phase 6 of 14 — architecture and migration analysis complete. Nothing is built yet.**

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

## Current contents

Analysis only. Read in this order:

| Document | What it is |
|---|---|
| [`docs/SHULLOS_IMPLEMENTATION_PLAN.md`](docs/SHULLOS_IMPLEMENTATION_PLAN.md) | Environment inspection, recommended architecture, and the 14-phase build sequence |
| [`docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md`](docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md) | 267 rules extracted from 16 legacy sources, each classified |
| [`docs/CONFLICT_REPORT.md`](docs/CONFLICT_REPORT.md) | 28 conflicts found across the legacy system, severity-ranked |
| [`docs/SKILL_MIGRATION_MAP.md`](docs/SKILL_MIGRATION_MAP.md) | How each legacy skill decomposes into standards, skills, and agents |
| [`docs/DECISIONS_2026-09-07.md`](docs/DECISIONS_2026-09-07.md) | **Read with the conflict report.** Decisions resolving 6 of 7 critical conflicts |

## Decided

| | |
|---|---|
| Chemistry | Lab Lime `#A3E635` + Aqua `#22D3EE` |
| Physics | Quantum Gold `#F5B82E` + Deep Purple `#8B5CF6` |
| Geology | Terra Teal `#16B8A6` + Rust Orange `#E85D24` |
| Background | White `#FFFFFF` default; Parchment `#EDF0E5` special-purpose only |
| Typography | Trade Gothic Next, falling back to Archivo / Archivo Narrow |
| Coloured type on white | Deep variants — Chem `#4D730E`, Phys `#896107`, Geo `#0E766A` |
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
