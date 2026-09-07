# SHULL OS — Implementation Plan

**Prepared:** 2026-09-07
**Owner:** Matthew Shull · James A. Garfield Local Schools (Ohio)
**Repository:** `Hayabusa015/workwork` (SHULL OS root, established 2026-09-07)
**Analysis performed in:** `Hayabusa015/ShullOS`, before the repository split — see CONFLICT-00
**Phase:** 1–6 (inspect, inventory, extract, conflict-report, propose standards, validate)
**Status:** ANALYSIS ONLY. No legacy file was modified, no skill rewritten, no Drive object created,
renamed, moved, or deleted. Every Drive call in this pass was read-only.

Companion documents:
`docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md` · `docs/CONFLICT_REPORT.md` · `docs/SKILL_MIGRATION_MAP.md`
**`docs/DECISIONS_2026-09-07.md` — user decisions resolving 6 of 7 CRITICAL conflicts. Read it with §22.**

---

## 0. Executive summary — read this before anything else

Six things came out of inspection that change the plan you handed me. In priority order:

1. **This repository is not empty and is not a teaching repository.** `Hayabusa015/ShullOS`
   currently holds a Next.js + Neon + Electron web application called "ShullOS — a zero-friction,
   dark-mode Personal Operating System for an ADHD brain." Five commits, unrelated to teaching. The
   name collides exactly. **Decision required before Phase 7** (§1, §23, Q-1).

2. **A fifth Physics palette exists, is marked CONFIRMED, and is already in production.**
   `_Brand/Standards/SHULL_PHYS_Palette_QuietVoltage.md`, dated **2026-09-06** — one day before
   this spec — locks Physics to Violet `#3A2168` / Violet Static `#A97BFF` on Porcelain `#E7DDD7`.
   It ships with a token file (`tokens.phys.js`), a build hook, a regrade script, a measured
   contrast table, and a rebuilt Unit 1 practice set. The spec's Part 8 assigns Physics **Quantum
   Gold `#F5B82E` + Deep Purple `#8B5CF6`** — a pairing that appears in the legacy record only as a
   *rejected back-burner alternate*. This is the single largest conflict in the migration
   (CONFLICT-01). It is not resolved here.

3. **Your Drive is real, reachable, and does not match the Part 23 structure.** Root is
   `SHULL Science`, not `Teaching/`. The real tree uses a **Unit → Section → five named content
   folders** hierarchy; Part 23 proposes **Unit → seven numbered folders** with no Section level.
   Chemistry has all 16 unit folders; Physics has 1 of 11; Geology is empty (§7, §14).

4. **`CHEM_DECISIONS.md` already exists in Drive** and is a well-formed, authoritative course
   decisions file. The two-layer governance model this spec re-derives is already written, already
   CONFIRMED, and already partially migrated. SHULL OS should adopt it, not replace it (§12).

5. **Five files that `shull-studio` tells other skills to read do not exist anywhere** — not in
   the installed skill, not in Drive. Two more (`SHULL_Color_Palette_Library.md`,
   `SHULL_Image_Prompt_Pack.md`) are referenced by filed standards and are also absent. Seven
   broken references (CONFLICT-05, CONFLICT-14).

6. **Nothing in the system can write to itself.** Claude has no write path into installed skills or
   Claude Project Knowledge. The Secretary's "modify system files after approval" step works in
   Git — and only in Git. That is the strongest argument for this repository existing (§8, §17).

---

## 1. Current repository state

| Property | Value |
|---|---|
| Working directory | `/home/user/ShullOS` |
| Remote | `https://github.com/Hayabusa015/ShullOS` |
| Current branch | `claude/shull-os-architecture-planning-jcyy5n` |
| Other branch | `claude/adhd-os-phase-1-e4m32v` |
| Branch divergence | **Zero.** Both point at `99ccb8d`. The planning branch is a label on the ADHD app. |
| Commits | 5 |
| Working tree | Clean |
| `CLAUDE.md` | Absent |
| `.claude/` | Absent |
| `agents/`, `skills/`, `brand/`, `courses/`, `standards/` | Absent |

Commit history, newest first:

```
99ccb8d  Add vercel.json and updated env example for deployment
2cbb876  Add Electron desktop shell over the cloud backend
124e7c9  Add db:migrate runner (Neon driver, no psql dependency)
870ff52  Switch data layer from Supabase to Neon (free serverless Postgres)
eccb79d  Phase 1: core storage schema, dark-mode scaffold, AI ingestion route
```

### The name collision

`README.md` describes ShullOS as *"a zero-friction, dark-mode Personal Operating System for an ADHD
brain"* with domains `teacher · dad_husband · coaching · home_car · hobbies_research`. It is a
personal-productivity capture app. `teacher` is one of five life domains inside it.

SHULL OS as specified is a **teaching** operating system: agents, skills, standards, course
decisions, Drive filing. Different problem, different lifecycle, different audience.

These are two systems with one name in one repository. Both are yours; neither is wrong. But they
cannot share a root directory without the `courses/`, `standards/`, and `skills/` trees sitting
beside `app/`, `db/`, and `electron/` with no relationship to them. **This is Unresolved Question
Q-1 and it blocks Phase 7.** Three options are laid out in §23.

---

## 2. Existing files

Complete inventory of the working tree (excluding `.git/` and `package-lock.json`):

```
.env.local.example      next.config.mjs        tsconfig.json
.gitignore              package.json           vercel.json
README.md               postcss.config.mjs
components.json         tailwind.config.ts
app/globals.css         app/layout.tsx         app/page.tsx
app/api/ingest/route.ts
db/migrations/0001_init.sql
electron/main.cjs       electron/preload.cjs
lib/db.ts               lib/types.ts           lib/utils.ts
scripts/apply-migration.mjs
```

**Nothing here is SHULL OS material.** Nothing here should be deleted as part of this migration —
see §20. `tailwind.config.ts` carries a zinc dark-mode palette belonging to the ADHD app; it is
**not** a SHULL Studio design token source and must not be mistaken for one.

---

## 3. Existing Claude configuration

Config lives at the account level in `/root/.claude`, not in the repository.

| Path | Contents |
|---|---|
| `~/.claude/launcher-settings.json` | Hooks + permissions (below) |
| `~/.claude/skills/synced/<bucket>/` | 27 synced skills incl. 10 SHULL skills |
| `~/.claude/plugins/synced/<bucket>/` | Empty — no plugins installed |
| `~/.claude/mcp-needs-auth-cache.json` | One unauthenticated connector (`HyperFrames_by_HeyGen`) |
| `~/.claude/projects/-home-user-ShullOS/` | This session's transcript |
| `~/.claude/session-start-git-identity.sh` | SessionStart hook script |
| `~/.claude/stop-hook-git-check.sh` | Stop hook script |

`launcher-settings.json`:

```json
{
  "hooks": {
    "SessionStart": [{ "hooks": [{ "type": "command",
      "command": "~/.claude/session-start-git-identity.sh" }] }],
    "Stop": [{ "matcher": "", "hooks": [{ "type": "command",
      "command": "~/.claude/stop-hook-git-check.sh" }] }]
  },
  "permissions": { "allow": ["Skill"] }
}
```

Two observations that matter for the build:

- **Hooks are proven to work in this environment.** Both `SessionStart` and `Stop` are configured
  and firing. SHULL OS validation hooks (§17) are therefore a supported mechanism, not a hope.
- **There is no repository-level `.claude/settings.json`.** Everything SHULL OS adds at
  `.claude/` in the repo will be new, version-controlled, and additive to the account config.

---

## 4. Existing skills

27 skills are installed account-wide in a single synced bucket. Ten are SHULL legacy material —
those are the migration input. The rest are Anthropic-published or unrelated personal skills.

### SHULL legacy skills — the migration input

| Skill | Lines | Role | Inspection note |
|---|---:|---|---|
| `shull-studio` | 292 | Router + build engine; brand, codes, routing, connectors, QA gate | Carries an **appended, unlabeled 2026-09-06 color-decision memo** after §7 that is not part of the skill body. Five referenced files missing. |
| `shull-chemistry-guidelines` | 777 | Chemistry profile | Still carries the full Units 0–15 map, the calendar, grading, reference packet, and a duplicate brand section — all of which `CHEM_DECISIONS.md` now owns. **Not trimmed.** |
| `shull-physics-guidelines` | 167 | Physics profile | §3 says the unit map is **NEEDED**. It exists. Skill is stale. §5 sig-fig rule contradicts the map. |
| `shull-geology-guidelines` | 305 | Geology profile | Carries curriculum, policy, and a palette table. Three live conflicts. |
| `shull-slide-deck-builder` | 127 + 117 ref | `.pptx` decks | `references/slide-standard.md` present. Builds the *old* Parchment/Deep Forest system, not the v2 twelve-layout template. |
| `shull-guided-notes-builder` | 138 | Cornell/guided packets | Clean. Scaffolding ladder indexed to unit number. |
| `test-quiz-generator` | 124 + 3 refs | Assessments | Clean. All three reference files present. |
| `shull-course-librarian` | 185 | Planning, audits, filing, pacing | Strongest legacy artifact. Its known-absorptions table was right when two other files were wrong. |
| `shull-student` | 186 + 1 ref | Overnight learning sweep | Drafts-for-approval model already correct. |
| `anti-ai` | **20** | Anti-AI-slop UI system | Thinnest file in the system. UI/interactive only — does **not** cover documents or slides. |

`shull-practice-set-generator` is **referenced by the routing table and by `shull-studio` §4 but is
not installed.** The v2 rules survive only as a fallback inside `shull-studio` §4.

### Other installed skills

`canvas-design`, `demo-data`, `deployment-audit`, `docx`, `email-triage`, `import-memory`,
`morning`, `pdf`, `pptx`, `practice-plan`, `rls-security-audit`, `skill-creator`, `supabase-sql`,
`ui-audit`, `xlsx`, `session-start-hook`.

Three of these are direct dependencies of the SHULL build chain and must stay reachable:
**`docx`** (guided notes, tests), **`pptx`** (decks), **`pdf`** (practice sets, QA rasterization).

---

## 5. Existing agents

**None.** There is no `agents/` directory, no `.claude/agents/`, and no subagent definition anywhere
in the repository or account config.

The generic subagent types the harness offers in this session are `claude`, `general-purpose`,
`Explore`, `Plan`, `claude-code-guide`, `statusline-setup`. None is SHULL-specific.

**The seven SHULL OS agents do not exist yet and must be built from scratch.** This is genuinely
greenfield — which is good news, because it means no legacy agent conflicts to migrate.

---

## 6. Existing MCP servers and integrations

Connectors surfaced in this session, grouped by relevance. Availability is a property of the
session's connector configuration, not of the repository.

### Load-bearing for SHULL OS

| Server | Status | SHULL OS use |
|---|---|---|
| **Google Drive** | **Live, authenticated as `mshull@jagschools.org`. Verified by read.** | Canonical document library. Librarian's entire surface. |
| **github** | Live (repo-scoped to `Hayabusa015/ShullOS`) | The OS itself; change control; PRs |
| **Google Calendar** | Available | Pacing against the 2026–27 calendar and MP deadlines |
| **Gmail** | Available | Out of scope for V1 |

### Available but not required for V1

`Canva`, `Gamma`, `Brightdeck`, `Slides_AI`, `Descript`, `Glif`, `Higgsfield`, `Mobbin`,
`Supabase`, `Vercel`, `Zapier`, `Swagger`, `Context7`, `AccuWeather`.

Two carry explicit legacy policy that survives into SHULL OS:

- **Higgsfield** — legacy records it as *out of credits*; the Slide System v2 doc confirms
  "Higgsfield is dry." Treat as unavailable. The documented fallback loop (Claude writes the
  prompt → Matt generates externally → Matt attaches → Claude places) is the working path.
- **Mobbin** — UI/UX pattern reference only. Never for print, decks, or Word documents.

### Not available

`HyperFrames_by_HeyGen` is present but unauthenticated. Nothing else in the SHULL workflow depends
on it.

---

## 7. Google Drive integration options

### 7.1 What the tools actually do

Verified present in this session:

| Tool | Capability | Librarian mapping |
|---|---|---|
| `search_files` | Structured query: `title`, `fullText`, `mimeType`, `parentId`, `owner`, dates | **Search, locate, verify** |
| `get_file_metadata` | Single file/folder by ID | **Verification primitive** |
| `read_file_content` | Text extraction: Docs, Slides, Sheets, PDF, docx, xlsx, pptx, images | **Retrieve** |
| `download_file_content` | Raw bytes | Retrieve binaries |
| `create_file` | New file or folder (`mimeType: application/vnd.google-apps.folder`) | **Create, upload, shelve** |
| `update_file` | Modify existing file | **Rename, overwrite** |
| `copy_file` | Duplicate | Safe pseudo-move half |
| `trash_file` | **Move to trash — recoverable** | Delete (soft only) |
| `share_file` / `get_file_permissions` | Sharing | Not used in V1 |
| `list_recent_files` | Recently touched | Janitor sweep input |

### 7.2 Two hard limitations the plan must respect

**(a) There is no permanent-delete tool.** `trash_file` moves an object to Drive trash, from which
you can restore it. This is a *safety feature*, and SHULL OS should lean on it: the Librarian's
"PERMANENT DELETE requires explicit user approval" rule maps onto "the Librarian may propose a
trash operation; only you empty the trash." Permanent deletion is genuinely outside Claude's reach.

**(b) There is no dedicated `move` tool.** Reparenting must be attempted through `update_file`, and
if that does not accept a parent change, the only remaining path is `copy_file` + `trash_file` —
which **changes the file ID and breaks every existing link**. Given the legacy record explicitly
warns that "renames break links Matt may have elsewhere," this is material.

> **Rule for the Librarian, V1:** MOVE is not a deterministic operation until reparenting via
> `update_file` has been tested on a throwaway file. Until then, the Librarian **proposes** moves
> and does not execute them. Testing this is step T-3 in §19.

### 7.3 Markdown-preservation quirk — carry it forward

The legacy record documents that saving markdown to Drive requires
`disableConversionToGoogleType: True` + `contentMimeType: text/plain` to stop Drive converting it
into a Google Doc. Every `.md` file currently in `_Brand/Standards/` shows `mimeType: text/plain`,
which confirms the technique was applied and worked. This must be encoded in the
`shelve-drive-file` skill, not left as folklore.

---

## 8. Claude Project integration — limitations, stated honestly

**A Claude Project cannot invoke Claude Code agents.** There is no supported bridge that lets a
message in a Chemistry Project trigger the Overseer → Designer → Auditor → Librarian chain.

What is actually true:

| Capability | Claude Project | Claude Code (this environment) |
|---|---|---|
| Reads Project Knowledge | Yes | No |
| Reads a Git repository | No | Yes |
| Runs subagents | No | Yes |
| Runs skills | Yes (account skills) | Yes |
| Writes to Google Drive | Via connector | Via connector |
| **Writes to its own Project Knowledge** | **No** | **No** |
| **Writes to installed skills** | **No** | **No** |
| Writes to Git | No | **Yes** |
| Scheduled recurring tasks | Yes | Yes (Routines / cron) |

The legacy governance file states this in its own words and it is worth quoting, because it is the
load-bearing constraint of the whole architecture:

> "I cannot write to Project Knowledge. Every update is a file you upload. I cannot write to
> installed skills. Same. Nothing propagates on its own. There is no background sync."

### The supported bridge — what SHULL OS will actually use

There are three real mechanisms and no fourth:

1. **Git is the write path.** Claude Code commits to this repository. That is the only place in the
   system where an agent can durably change a rule. This is why the Secretary works.
2. **Drive is the shared read path.** Both Claude Projects and Claude Code can read and write
   Google Drive through the same connector. A standards file published to
   `_Brand/Standards/` from the repo is visible to a Project immediately.
3. **The human is the bridge for Project Knowledge.** A Project's Knowledge is updated by you
   uploading a file. SHULL OS's job is to hand you a finished file, not a description of one.

**Therefore the Project → Claude Code handoff is: you paste the request into Claude Code (web,
CLI, or app) yourself.** SHULL OS will document this plainly in `docs/MOBILE_AND_PROJECT_WORKFLOW.md`
rather than implying automation that does not exist.

**Proposed publish loop (Phase 12):** repo `standards/` and `brand/` are the source of truth →
a `publish-standards` script renders them to `_Brand/Standards/` on Drive → Projects read them
there. One direction only. Projects never write back.

---

## 9. Recommended repository architecture

Close to Part 37, with four deliberate changes, each justified.

```
ShullOS/                              (see Q-1 — this root may become shull-os/ or a new repo)
├── CLAUDE.md                         highest-level persistent instructions only
├── README.md
├── .claude/
│   ├── agents/                       ← CHANGE 1: agents live here, not in /agents
│   │   ├── overseer.md      researcher.md    designer.md
│   │   ├── librarian.md     janitor.md       secretary.md
│   │   └── auditor.md
│   ├── skills/                       ← CHANGE 2: skills live here, not in /skills
│   │   ├── build-document/SKILL.md
│   │   ├── build-presentation/SKILL.md
│   │   ├── build-assessment/SKILL.md
│   │   ├── build-lab/SKILL.md
│   │   ├── apply-shull-design/SKILL.md
│   │   ├── verify-content/SKILL.md
│   │   ├── audit-deliverable/SKILL.md
│   │   ├── retrieve-drive-file/SKILL.md
│   │   ├── shelve-drive-file/SKILL.md
│   │   ├── naming/SKILL.md
│   │   └── weekly-system-review/SKILL.md
│   └── settings.json                 hooks + permissions, repo-scoped
├── brand/
│   ├── SHULL_DESIGN_SYSTEM.md        THE authoritative design system
│   ├── tokens.json                   THE only place a hex is typed
│   └── palette-archive/              ← CHANGE 3: deprecated palettes, preserved
│       ├── README.md                 why each was superseded, and when
│       ├── base-parchment-bio-lime.md
│       ├── slide-system-v2-amber-split.md
│       ├── per-course-2026-09-06.md
│       ├── phys-quiet-voltage.md
│       └── geo-earth-tone.md
├── courses/
│   ├── chemistry/DECISIONS.md
│   ├── physics/DECISIONS.md
│   └── geology/DECISIONS.md
├── standards/
│   ├── ANTI_AI_SLOP_STANDARD.md      the quality standard, documents + slides + UI
│   ├── VOICE.md
│   ├── NAMING.md
│   ├── DRIVE_ARCHITECTURE.md         Drive tree + live folder IDs
│   └── QA_GATE.md
├── workflows/
│   ├── build-deliverable.md          the Part 34 completion chain
│   ├── weekly-system-review.md
│   └── legacy-migration.md
├── governance/
│   ├── GOVERNANCE.md                 two-layer rule, precedence, authority matrix
│   ├── CHANGE_CONTROL.md
│   └── proposals/                    Secretary's PENDING/APPROVED/… records
├── config/
│   └── drive.json                    verified folder IDs, machine-readable
├── templates/
│   └── slide-template/src/           tokens.js + build.js → 12-layout .pptx
├── schemas/
│   ├── change-proposal.schema.json
│   └── task-report.schema.json
├── scripts/
│   ├── validate_layers.py            fail if a course fact appears in a skill
│   ├── validate_codes.py             fail if a U#/S#.# code isn't in a DECISIONS.md
│   ├── validate_tokens.py            ← CHANGE 4: fail if a hex is typed outside tokens.json
│   └── publish_standards.py          repo → Drive _Brand/Standards/
├── reports/                          Researcher, Janitor, Auditor output
├── change-log/
│   └── CHANGELOG.md
├── docs/                             this plan + the three companion analyses
└── legacy/                           ← CHANGE 5: verbatim snapshots, never edited
    ├── skills/                       the 10 installed SHULL skills, as-found
    └── drive-standards/              the 6 _Brand/Standards files, as-found
```

**Why the five changes:**

1. **`.claude/agents/`** — Claude Code discovers subagents there. A top-level `/agents` directory
   would be documentation that never executes. Part 37's shape is right; the path is not.
2. **`.claude/skills/`** — same reason. Skills must be discoverable to run.
3. **`brand/palette-archive/`** — Part 29 says deprecated palettes get classified DEPRECATED, and
   Part 47 forbids deleting legacy material. A named archive satisfies both: nothing is lost,
   nothing is live. The legacy system already tried to do this with
   `SHULL_Color_Palette_Library.md` — a file that was specified and never created (CONFLICT-14).
   Putting it in Git is how it stops evaporating.
4. **`scripts/validate_tokens.py`** — Part 39 says "do not create multiple competing palette
   files." Every palette conflict in this system exists because the same hex was typed in two
   places by hand. A rule nobody checks is a rule that drifts. This is the check that enforces it.
5. **`legacy/`** — Parts 26 and 47 both forbid destroying legacy material. Snapshotting the
   as-found state into Git makes the audit reproducible and makes "we changed X from Y" provable.
   `legacy/` is read-only by convention and excluded from every validator.

`reports/` and `change-log/` are kept exactly as Part 37 specifies.

---

## 10. Recommended agent architecture

Seven agents, as specified in Part 3. No additions — inspection produced no demonstrated need for
an eighth.

Each agent is a `.claude/agents/<name>.md` file with YAML frontmatter (`name`, `description`,
`tools`, `model`) and a body that states responsibilities, authority, hard limits, and required
output shape.

### Tool grants — conservative, mapped to Part 4

| Agent | Tools granted | Explicitly denied |
|---|---|---|
| **Overseer** | Read, Glob, Grep, Task tools, Agent, Skill, Write (task reports only) | Drive write, Edit of `brand/` `standards/` `governance/` |
| **Researcher** | Read, Glob, Grep, WebSearch, WebFetch, Drive read tools, Write (`reports/` only) | All Drive writes; all standards edits |
| **Designer** | Read, Glob, Grep, Bash, Write, Edit, Skill, Drive read | Edits outside the assigned deliverable; standards edits |
| **Librarian** | Drive: search, metadata, read, download, create, update, copy. Read, Glob, Grep | **`trash_file` — approval-gated.** Standards edits |
| **Janitor** | Read, Glob, Grep, Bash (read-only), Drive read, Write (`reports/` only) | Every write outside `reports/` |
| **Secretary** | Read, Glob, Grep, Write, Edit (**`governance/proposals/` freely; everything else only on an APPROVED proposal**) | Unapproved edits to any authoritative file |
| **Auditor** | Read, Glob, Grep, Bash (render/rasterize), Drive read, Write (`reports/` only) | **All deliverable edits.** Independence is the point. |

### The three rules that make this work

1. **A returned message is not a completed task.** The Overseer verifies the artifact exists at the
   verified path before writing WORK COMPLETE. Part 34's report format is enforced by
   `schemas/task-report.schema.json`.
2. **Only the Secretary writes to `brand/`, `standards/`, `governance/`, and `courses/`, and only
   against an APPROVED proposal ID.** Everyone else proposes. This is enforced socially by the agent
   definitions and mechanically by a PreToolUse hook (§17).
3. **The Auditor never fixes what it finds.** It reports. The Overseer routes the fix back to the
   Designer. An auditor that patches its own findings is not an audit.

---

## 11. Recommended skill architecture

Eleven skills as listed in Part 22, plus one addition and one important reshaping.

### The addition: `anti-ai-slop`

Part 20 makes the Anti-AI-Slop Standard a *core* standard, and the legacy `anti-ai` skill covers
**only interactive UI** — 20 lines, entirely about React and Tailwind. The 21 KB
`ANTI_AI_SLOP_EDUCATOR_STANDARD.md` on Drive covers documents, voice, and visual tells, and it is
*not* a skill at all; `shull-studio` tells other skills to go find it in Project Knowledge, where
Claude Code cannot see it.

**Recommendation:** the standard's content becomes `standards/ANTI_AI_SLOP_STANDARD.md`
(authoritative). A thin skill `.claude/skills/anti-ai-slop/SKILL.md` points at it and carries the
operative checklist. The legacy `anti-ai` UI rules become a clearly-scoped section of the standard,
not a separate competing document.

### The reshaping: skills point, standards hold

Every skill obeys the Part 2 rule mechanically:

> A skill states **procedure**. A standard states **rule**. Where a skill needs a rule, it links.
> No skill restates a hex, a font name, a margin, or a course fact.

`scripts/validate_tokens.py` enforces the hex half of that. `validate_layers.py` enforces the
course-fact half.

### Skill table

| Skill | Owns | Reads (never restates) |
|---|---|---|
| `build-document` | .docx/.pdf procedure, page budgets | design system, voice, naming, course decisions |
| `build-presentation` | .pptx procedure, 12-layout template, reserved-height rule | design system, slide geometry |
| `build-assessment` | Item construction, parallel versions, keys | course decisions (assessment shape), voice |
| `build-lab` | Lab anatomy, teacher prep section | course decisions (lab philosophy), safety rules |
| `apply-shull-design` | Applying tokens to a deliverable | `brand/tokens.json`, `brand/SHULL_DESIGN_SYSTEM.md` |
| `verify-content` | Accuracy checking procedure | course decisions, Ohio standards |
| `audit-deliverable` | The QA gate, run independently | `standards/QA_GATE.md` |
| `retrieve-drive-file` | Search + read procedure | `config/drive.json` |
| `shelve-drive-file` | Route, create, verify, **confirm destination** | `standards/DRIVE_ARCHITECTURE.md`, `NAMING.md` |
| `naming` | Deterministic filename construction | `standards/NAMING.md` |
| `weekly-system-review` | The Researcher loop, **report-only** | everything; writes only to `reports/` |
| `anti-ai-slop` *(new)* | The slop checklist as a runnable pass | `standards/ANTI_AI_SLOP_STANDARD.md` |

**`build-lab` and a reference-sheet skill were never built in the legacy system.** Both remain
build targets. The Drive already holds a started lab template
(`_Brand/Templates/Lab/build_lab.py` + `README_Lab_Template.md`, created 2026-09-07) — that is
source material for `build-lab`, and Part 17's instruction to preserve the existing lab structure
applies to it.

---

## 12. Recommended governance architecture

**Adopt the existing model. Do not invent a new one.**

`_Brand/Standards/SHULL_System_Governance.md` is CONFIRMED, dated, coherent, and already describes
the two-layer rule, the precedence order, the "course skills must point, never restate" rule, the
change paths, and a fix-list format. It anticipated this entire specification. Rewriting it from
scratch would discard a working decision — exactly what Part 26 warns against.

### What carries over unchanged

- **The one rule:** a fact lives in exactly one place.
- **The line, as a test:** affects all three courses → skill. Affects one course → course decisions.
- **Precedence:** current instruction → course decisions (for course facts) → skill (for build
  mechanics) → CONFIRMED over CARRIED OVER/PROVISIONAL → newer over older.
- **Stale reporting:** when a skill states a course fact that the decisions file contradicts, the
  decisions file wins **and the skill is reported stale** — not silently obeyed, not silently
  ignored.
- **The `Supersedes:` line** in every decision-log entry. This is the mechanism that makes drift
  visible, and it should be mandatory in SHULL OS change records.

### What SHULL OS changes

| Legacy | SHULL OS | Why |
|---|---|---|
| Layer 2 lives in Claude Project Knowledge | Layer 2 lives in `courses/*/DECISIONS.md` in Git | Project Knowledge has no version history and no write path |
| Change = you re-upload a file | Change = a Secretary commit against an APPROVED proposal | Auditable, reversible, diffable |
| Drift found by scheduled sweep | Drift found by sweep **and** by CI validators | A check that runs on every commit beats a check that runs at 3 AM |
| Confidence labels: CONFIRMED / CARRIED OVER / PROVISIONAL / NEEDED | Part 27 labels: LOCKED / INHERITED / PROVISIONAL / CONFLICT / DEPRECATED / ARCHIVE / UNKNOWN | Superset. Mapping in §18. |

### Authority matrix

Part 4's permissions, restated as the enforceable rule:

| | Read | Create deliverable | Modify deliverable | Modify standards | Drive create | Drive rename/move | Drive trash |
|---|---|---|---|---|---|---|---|
| Overseer | ✓ | ✓ | limited | ✗ | ✗ | ✗ | ✗ |
| Researcher | ✓ | reports | ✗ | ✗ | ✗ | ✗ | ✗ |
| Designer | ✓ | ✓ | assigned only | ✗ | ✗ | ✗ | ✗ |
| Librarian | ✓ | ✓ | ✗ | ✗ | ✓ | deterministic only | **approval** |
| Janitor | ✓ | reports | ✗ | ✗ | ✗ | ✗ | ✗ |
| Secretary | ✓ | proposals | ✗ | **approved only** | ✗ | ✗ | ✗ |
| Auditor | ✓ | reports | ✗ | ✗ | ✗ | ✗ | ✗ |

### The change record

Part 32's format, with three fields added from the legacy model:

```
Change ID:        SHULL-CHG-0001
Date:             2026-09-07
Source:           Researcher | Janitor | Auditor | User | Migration
Current Rule:     [verbatim, with file and section]
Proposed Rule:    [verbatim]
Supersedes:       [file §]              ← from legacy governance; makes drift visible
Reason:
Affected Agents / Skills / Courses:
Risk:             low | medium | high
Recommendation:
Decision:
Status:           PENDING | APPROVED | REJECTED | DEFERRED | IMPLEMENTED
Implemented By:   [commit SHA]          ← added; ties the record to the diff
Verified:         [yes/no + how]        ← added; a change is not done until checked
```

---

## 13. Recommended file naming system

### The conflict Part 25 asked me to look for — found

Part 25 proposes `COURSE_UNIT_RESOURCE_DESCRIPTOR_VERSION`, e.g.
`CHEM_U03_Presentation_Periodic_Trends_v1`.

The established, in-use convention is different in four ways:

```
SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor].[ext]
SHULL_CHEM_Slides_U08_S08.2.pptx
```

| | Part 25 proposal | Established convention |
|---|---|---|
| Prefix | none | `SHULL_` |
| Section code | absent | **`S##.#` — required** |
| Version | `_v1` | version **letters** for parallel forms: `_A`, `_B` |
| Type vocabulary | free-form | fixed list |

**The section code is the decisive difference.** `U#/S#.#` is not merely a filename convention —
it is the binder tab, the slide footer, the student organizer, and the folder name, and Part 5.1 of
the legacy record is explicit that these are one system, not four. A naming scheme without `S##.#`
would silently break the binder.

### Recommendation — keep the established convention

```
SHULL_[COURSE]_[Type]_U##_S##.#[_Descriptor][_Version].[ext]
```

- `COURSE` ∈ `CHEM` | `PHYS` | `GEO`
- `Type` ∈ `Slides` `Guided_Notes` `Practice_Set` `Quiz` `Test` `Lab` `Study_Guide` `Reference`
  `Key` `Rubric` `Activity` `Organizer`
- Unit zero-padded to two digits
- **Section: adopt the zero-padded `S##.#` form** (`S08.2`), matching the Drive folder names
  (`Section 01.3 - …`) and the v2 folder-organization standard. This closes a live inconsistency:
  `shull-studio` §2 writes `U08_S8.4` (unpadded) while the v2 folder standard writes `S08.4`
  (padded). See CONFLICT-09.
- Parallel-form version letters append last: `..._S08.4_A.docx`
- Answer keys are always separate files ending `_Key`
- Images are **not** course documents: no `SHULL_` prefix, lowercase
  `[course]_u##_s##.#_[subject].png`

**This is a recommendation, not an enforced rule.** Part 25 requires the final decision to be
documented before enforcement. It is Unresolved Question **Q-6**, and the grammar remains
unfinished for labs, slides, and keys — a legacy open item carried since install (CONFLICT-09).
**Batch renaming stays blocked** until Q-6 and the Geology numbering question (Q-4) both close.

---

## 14. Recommended Drive architecture

### 14.1 What is actually there — verified 2026-09-07, read-only

```
SHULL Science/                        1FsFiaYfkwgSLnA62bpIHt2zGosFwcPec
├── _Brand/                           14Epgk_qgvxzSDljBABn72lSLYY6erF1Q
│   ├── Templates/                    1cFgdQbW8SSJaaXxzfCCr-IZMFjvaMg6J
│   ├── Standards/                    1aLMHcKoF4nrAKh121O2w5WgzVwSqOgZK
│   └── Image Library/                1RBK23kn2fcmBWiYidUDXSsVGk5NWXy3L
│       ├── Chemistry/  Physics/  Geology/  Shared/
├── Chemistry/                        1dA5kKA9vQxaWX0CZMhXIoBMYGfDhMxH6
│   ├── CHEM_DECISIONS.md             1gHwFKp2pcjam04xkselyDYO4JcJHzRrf
│   └── Unit 00 … Unit 15             all 16 unit folders present
├── Physics/                          1NOjl2nEZ1bjcjm32G55V265uGUoTErlk
│   └── Unit 01 - Motion in One Dimension   (1 of 11)
│       ├── Section 01.1 … Section 01.4
└── Geology/                          1lqHHql9cSqOZDGej2ff_121bITWOKZvr
    └── (empty)
```

All five folder IDs recorded in the legacy spec **verified correct**.

### 14.2 Where Part 23 differs from reality — four conflicts

| # | Part 23 proposal | Actual Drive | Verdict |
|---|---|---|---|
| 1 | Root `Teaching/` | Root `SHULL Science` | **Keep `SHULL Science`.** Renaming a Drive root breaks every stored link and every folder ID reference. |
| 2 | `Image Library/`, `Standards/`, `Templates/` as siblings of `_Brand/` | All three are **children of** `_Brand/` | **Keep the real structure.** `_Brand/` exists precisely to hold cross-course material in one place. |
| 3 | `Unit XX – Unit Name/` with **en dash** | `Unit 00 - Foundations of Chemistry` with **hyphen** | **Keep the hyphen.** An en dash would create near-duplicate folders — the exact failure the routing rules forbid. |
| 4 | Unit → seven numbered folders (`01 Presentations/` … `99 Archive/`), **no Section level** | Unit → `Section ##.# - Name/` → **five named folders** | **Keep the real structure.** Dropping the Section level would break the `U#/S#.#` system that ties document, filename, folder, and binder tab together. |

Part 23 also says "Do not arbitrarily redesign this structure" and "inspect the actual Drive
structure and document any differences." That is what this section is. **The recommendation is to
keep what is built and record Part 23's tree as a superseded proposal.** This is CONFLICT-06.

Part 23's one genuinely new idea — a **`99 Archive/`** folder — is worth adopting as an *optional
sixth* content folder rather than a renumbering of the five. Superseded material currently has
nowhere to go, and Part 47 forbids deleting it. That is proposal **P-3**.

### 14.3 Real filing defects found during inspection

| Defect | Detail | Severity |
|---|---|---|
| `_Brand/Templates/` is a dumping ground | Contains 15 PNGs, `make_art.py`, `regrade.py`, `demo_u1.js` — none is a template | should-fix |
| Course document misfiled in `_Brand/` | `GEO_U1_S1.2-S1.4_Guided_Cornell_Notes.docx` sits in `Templates/`. Wrong folder *and* wrong name. | **blocking** |
| Images outside the Image Library | `glassware_warm.png`, `atom_dark.png`, `nucleus_gold.png` etc. are in `Templates/`, not `Image Library/` | should-fix |
| Template source not in `src/` | `tokens.js`, `tokens.phys.js`, `build.js` sit flat in `Templates/`; the spec says `Templates/src/` | should-fix |
| Chemistry Unit 00 has a bare `Labs/` folder | Should be `Section 00.3 - …/Labs-Case Studies-Projects/`. Empty. This is the `Tests` beside `Tests-Quizizz` failure mode. | should-fix |
| Two referenced standards absent | `SHULL_Color_Palette_Library.md`, `SHULL_Image_Prompt_Pack.md` | **blocking** |
| Physics unit map PDF absent from Drive | `SHULL_Physics_Unit_Map_1.pdf` is cited as the source of the confirmed map but is not in Drive | important |

**None of these was touched.** They are the Librarian's and Janitor's first real work order, after
Phase 10.

---

## 15. Mobile workflow

You work from mobile, school, and home. The constraint driving the whole architecture is that
canonical documents must not depend on one local computer — which is why Drive is canonical.

| Device | Capture | Build | Read the OS | Approve a change |
|---|---|---|---|---|
| **Phone** | Claude app / Project | ✗ | Drive; GitHub web | ✓ — reply APPROVED to a proposal |
| **School** | Project or Claude Code web | Claude Code web | ✓ | ✓ |
| **Home** | Claude Code (any surface) | ✓ full chain | ✓ | ✓ |

### The realistic mobile loop

1. **On the phone, in the course Project:** ask the question, get an answer, capture a decision.
   Building a `.pptx` from a phone is not a thing; don't design for it.
2. **A decision gets captured as a decision-log entry**, phrased in the standard format, and lands
   in the course `DECISIONS.md` when you next reach Claude Code.
3. **Weekly review reports land in `reports/`** and are readable on GitHub mobile.
4. **Approvals are text.** A change proposal is a file with a Status line. Approving it is you
   saying so; the Secretary flips the status and commits. That works from a phone.

**What will not work from a phone, stated plainly:** running the agent chain, rendering and
rasterizing a deliverable for QA, executing Drive moves. Those need Claude Code.

---

## 16. Weekly automation strategy

**V1 is report-only. Autonomous self-modification is prohibited (Part 31, Part 47).**

### Available scheduling mechanisms — all verified present

| Mechanism | Granularity | Fits |
|---|---|---|
| `create_trigger` (Routines) — cron, min hourly, fires a fresh or bound session | recurring | **The weekly review.** Recommended. |
| `send_later` | one-shot | Follow-ups |
| `CronCreate` / `CronList` / `CronDelete` | recurring | Alternative |
| Claude Project scheduled tasks | recurring | The legacy 3 AM per-course sweep |

### Proposed loop

```
Sunday 06:00 local  →  Routine fires a fresh Claude Code session
                    →  Overseer dispatches Researcher + Janitor
                    →  Researcher: recent work, recurring corrections, patterns
                    →  Janitor: broken refs, duplicate rules, stale docs, orphans
                    →  Secretary: turns findings into numbered proposals, all PENDING
                    →  commit to reports/YYYY-WW/ and governance/proposals/
                    →  STOP. Notify. Change nothing.
```

Three hard limits, encoded in `weekly-system-review/SKILL.md`:

1. The Researcher **never** edits `brand/`, `standards/`, `governance/`, or `courses/`.
2. Every finding leaves as a PENDING proposal with a Change ID. No finding is self-applied.
3. If the review produces nothing, it says so in one line and commits nothing.

**Cron note:** Routines evaluate cron in UTC. Ohio is UTC−4 (EDT) through 2026-11-01 and UTC−5
(EST) after. A "Sunday 6 AM local" schedule needs the offset applied *and* revisiting at the DST
change. Flagged as **Q-8** rather than silently hardcoded.

**Do not schedule anything until Phase 13.** A recurring job pointed at a half-built system
produces noise that trains you to ignore it.

---

## 17. Security and permissions

### Principles

1. **Least privilege per agent** (§10 table).
2. **Destructive operations are approval-gated, and the destructive operation available is `trash`,
   not permanent delete.** Permanent deletion is outside Claude's reach entirely — a real safety
   property, not a policy promise.
3. **Only the Secretary writes authoritative files, and only against an APPROVED proposal.**
4. **Git is the audit log.** Every rule change is a commit with a Change ID in the message.

### Enforceable controls

| Control | Mechanism | Status |
|---|---|---|
| Agent tool restriction | `tools:` in `.claude/agents/*.md` frontmatter | Supported |
| Block non-Secretary writes to `brand/`, `standards/`, `governance/`, `courses/` | `PreToolUse` hook in `.claude/settings.json` | Supported — hooks proven working in this env |
| Block `trash_file` without an approval token | `PreToolUse` hook matching the Drive trash tool | Supported |
| Reject a hex typed outside `tokens.json` | `scripts/validate_tokens.py`, run by a `Stop` hook and in CI | To build |
| Reject a course fact in a skill | `scripts/validate_layers.py` | To build |
| Reject a `U#/S#.#` code not in a `DECISIONS.md` | `scripts/validate_codes.py` | To build |

### Data-handling notes

- Drive access is authenticated as `mshull@jagschools.org`, a **school district account**.
  Student-identifying data must never enter this repository or any report. Roster data, grades, and
  named student work stay in Drive and the gradebook. **No exception.**
- Repository GitHub scope is limited to `Hayabusa015/ShullOS`. Do not widen it without a reason.
- `.env.local.example` in the current tree references `ANTHROPIC_API_KEY` and `DATABASE_URL` for
  the ADHD app. If Q-1 resolves toward separation, those secrets go with that app, not with SHULL OS.

---

## 18. Migration plan

The Part 26 pipeline, with the actual work at each stage.

```
LEGACY FILES → INVENTORY → EXTRACTION → CONFLICT DETECTION → CLASSIFICATION
→ USER-APPROVED DECISIONS → MASTER STANDARDS → NEW SKILLS → VALIDATION
```

### Stages 1–4 — done, in this pass

Inventory and extraction are in `docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md` (68 rules extracted from 16
sources). Conflicts are in `docs/CONFLICT_REPORT.md` (28 conflicts: 7 CRITICAL, 9 IMPORTANT,
7 NON-BLOCKING, 5 DEPRECATED). Skill mapping is in `docs/SKILL_MIGRATION_MAP.md`.

### Stage 5 — classification

Every extracted rule carries one of the Part 27 labels. Legacy labels map as follows:

| Legacy | Part 27 | Rule |
|---|---|---|
| CONFIRMED (and consistent with this spec) | **LOCKED** | |
| CONFIRMED (and contradicted by this spec) | **CONFLICT** | Never silently promoted |
| CONFIRMED (superseded by a newer decision) | **DEPRECATED** | Archived, not deleted |
| CARRIED OVER | **PROVISIONAL** | Never presented as settled |
| PROVISIONAL | **PROVISIONAL** | |
| NEEDED | **UNKNOWN** | Ask, don't fill |
| (no conflict, consistently supported) | **INHERITED** | |
| historical, no longer operative | **ARCHIVE** | |

**No CONFLICT, PROVISIONAL, or UNKNOWN item becomes LOCKED without you saying so.**

### Stage 6 — user-approved decisions — THIS IS THE GATE

The build does not proceed past Phase 6 until the seven CRITICAL conflicts are resolved. They are
listed in §22 as Q-1 … Q-6 (Q-6 covers both the naming grammar and the Drive structure, which are
one conventions decision) and detailed in the conflict report.

### Stage 7 — master standards

`brand/SHULL_DESIGN_SYSTEM.md` + `brand/tokens.json` are written from the Part 46 locked
decisions **plus** the resolved CRITICAL conflicts. Every superseded palette is written to
`brand/palette-archive/` with a dated note saying what superseded it and when.

### Stage 8 — new skills

Per `docs/SKILL_MIGRATION_MAP.md`. **No legacy skill is copied.** Each is decomposed: rules to
standards, course facts to `courses/*/DECISIONS.md`, procedure to a new focused skill.

### Stage 9 — validation

§19.

### What is explicitly not touched

- The 10 installed skills stay installed and unmodified until Phase 14 passes.
- Drive is not written to until Phase 10, and the first writes are additive only.
- `CHEM_DECISIONS.md` on Drive is *copied into* the repo, not moved or deleted.
- The ADHD app's files are not deleted regardless of how Q-1 resolves.

---

## 19. Testing strategy

| ID | Test | Method | Gate |
|---|---|---|---|
| T-1 | Validators catch what they claim | Seed a course fact into a skill, a stray hex, and a bad `U#/S#.#`; all three must fail | Phase 9 |
| T-2 | Agents cannot exceed authority | Ask Researcher to edit `brand/tokens.json`; must refuse and produce a proposal | Phase 8 |
| T-3 | **Drive reparenting** | On a throwaway file in a scratch folder: can `update_file` change the parent? | **Phase 10 — blocks Librarian MOVE** |
| T-4 | Drive markdown preservation | Write a `.md` with the documented flags; confirm `mimeType: text/plain` | Phase 10 |
| T-5 | Librarian verifies, not claims | Shelve a file, then independently confirm by `parentId` search | Phase 10 |
| T-6 | Approval gate holds | Attempt `trash_file` without approval; must be blocked | Phase 10 |
| T-7 | Full chain end-to-end | Build one real Chemistry deliverable through all seven agents | **Phase 14** |
| T-8 | Auditor independence | Auditor must catch a deliberately clipped/off-palette deliverable | Phase 11 |
| T-9 | Weekly review is report-only | Run it; confirm zero changes outside `reports/` and `governance/proposals/` | Phase 13 |
| T-10 | Task report honesty | Force a failure; confirm the report says INCOMPLETE, not WORK COMPLETE | Phase 14 |

**T-7 is the acceptance test.** Recommended subject: a Chemistry U1 section — Chemistry is fully
mapped, the Drive folders exist, and the legacy record confirms guided notes already exist for
S1.2–S1.5, so there is real material to check against.

---

## 20. Rollback strategy

| Layer | Rollback | Time |
|---|---|---|
| Repository | `git revert` the Change ID commit | seconds |
| A standard | Every change is one commit with one Change ID; revert it | seconds |
| Design tokens | `tokens.json` is versioned; the archive holds every superseded palette | seconds |
| Agents / skills | Versioned files; revert | seconds |
| Drive **create** | `trash_file` the created object | minutes |
| Drive **rename** | `update_file` back to the recorded prior name — **the Librarian must log the prior name before renaming** | minutes |
| Drive **move** | Reparent back — **only if T-3 passes.** If moves are done by copy+trash, the file ID changes and rollback is imperfect. | see T-3 |
| Drive **trash** | Restore from Drive trash | minutes |
| Installed skills | Untouched until Phase 14; the pre-migration state is snapshotted in `legacy/skills/` | — |

### Three rollback rules

1. **Every Drive mutation is logged before it happens** — object ID, prior name, prior parent — to
   `reports/drive-operations/`. A mutation that was not logged cannot be rolled back.
2. **Phases 7–13 are additive.** No legacy file is deleted or overwritten. Rollback is deletion of
   what was added.
3. **The migration is not "committed" until T-7 passes.** Before that, abandoning the branch is a
   complete rollback.

---

## 21. Known limitations

Stated plainly, because Part 36 says do not invent unsupported capabilities.

1. **A Claude Project cannot invoke Claude Code agents.** No bridge exists. §8.
2. **Claude cannot write to Project Knowledge or to installed skills.** Every such update is a file
   you upload.
3. **No permanent Drive delete.** `trash_file` only. (A limitation that is also a safety feature.)
4. **No verified Drive move.** T-3 must run before the Librarian executes any reparenting.
5. **Drive `search_files` has no `parents in` operator** — only `parentId =`. Recursive traversal
   costs one call per folder. A full Drive audit is many calls; the Janitor should scope its sweeps.
6. **Higgsfield is out of credits.** Assume unavailable.
7. **Claude cannot download images from the open web in the build environment** (legacy record;
   Wikimedia, NASA and others were blocked). The prompt → generate → attach → place loop stands.
8. **Trade Gothic Next is almost never present in a render environment.** A documented fallback
   ladder is mandatory, not optional. Part 11 requires determining one — see Q-5.
9. **Past-chat search cannot cross Claude Project boundaries.** Each course sweeps separately.
10. **This session's connector set is not guaranteed to persist.** Google Drive is live *now*;
    SHULL OS should fail loudly, not silently, if it is absent.
11. **The Researcher cannot read your Claude Project conversations from Claude Code.** The Part 31
    learning loop's real input is the repository, Drive, and what you tell it — not chat history.
    Designing around chat-history access would be inventing a capability.

---

## 22. Unresolved questions

These block the build. Six are CRITICAL; the rest are important but can proceed under a stated
assumption.

### Blocking — **6 of 7 answered 2026-09-07**, see `DECISIONS_2026-09-07.md`

| # | Answered |
|---|---|
| Q-1 | New repo **`Hayabusa015/workwork`** — attached and in use |
| Q-2 | Physics = **Quantum Gold `#F5B82E` + Deep Purple `#8B5CF6`**. Quiet Voltage deprecated. |
| Q-3 | Geology = **Terra Teal `#16B8A6` + Rust Orange `#E85D24`**, all media. Earth palette deprecated. |
| Q-4 | **Plate Tectonics = U4.** Geology unit sequence settled U1–U10. |
| Q-5 | **Archivo + Archivo Narrow**, committed to `brand/fonts/`, installed via SessionStart hook. |
| Q-6(b) | Drive stays **exactly as built**; root `SHULL Science`. Part 23 superseded. |
| Q-6(a) | **STILL OPEN** — section-code padding |

**New since:** CONFLICT-28 — the six locked course colours fail as text on the locked white
background (measured). Blocks Phase 8, not Phase 7.

### Original blocking table (retained for context)

| # | Question | Blocks | Detail |
|---|---|---|---|
| **Q-1** | **Repository identity.** SHULL OS and the ADHD app share the name `ShullOS` and one repo. Options: (a) new repo `shull-os`, ADHD app stays — *recommended*; (b) SHULL OS takes this repo, ADHD app moves out; (c) both coexist under `shull-os/` and `adhd-os/` subdirectories. | Phase 7, everything | §1 |
| **Q-2** | **Physics palette.** Quiet Voltage (CONFIRMED 2026-09-06, in production) vs. Quantum Gold + Deep Purple (this spec, 2026-09-07). Did you know Quiet Voltage existed when you wrote Part 8? | Design system, every Physics deliverable | CONFLICT-01 |
| **Q-3** | **Geology palette.** Three live positions: identical-to-Chemistry (skill §7), the confirmed earth-tone palette already used in the built U1 packet (governance §8), and Terra Teal + Rust Orange (this spec). | Design system, every Geology deliverable | CONFLICT-02 |
| **Q-4** | **Geology unit numbering.** Plate Tectonics U4 (skill §5) or U5 (governance §8)? A one-unit offset from U4 onward. | Every Geology code, all batch renaming, Drive folder creation | CONFLICT-03 |
| **Q-5** | **Typography fallback.** Trade Gothic Next is locked as primary but unavailable in render environments. Confirm the ladder: Oswald/Inter → Poppins/Lato → Liberation Sans. | Every deliverable | CONFLICT-04 |
| **Q-6** | **Naming and Drive conventions.** (a) Adopt `SHULL_[COURSE]_[Type]_U##_S##.#` with **zero-padded** section codes, superseding both Part 25's proposal and `shull-studio` §2's unpadded form? (b) Confirm the Drive tree stays as built — root `SHULL Science`, `_Brand/` parenting Templates/Standards/Image Library, hyphen separators, and the Unit → Section → five-folder hierarchy — rather than adopting Part 23's tree? | Batch renaming, `naming` skill, `shelve-drive-file`, the whole Librarian | CONFLICT-09, CONFLICT-06 |

### Important — proceed under a stated assumption, confirm before Phase 12

| # | Question |
|---|---|
| Q-7 | **Geology section numbering.** Does Geology get `S#.#` codes at all? If not, `validate_codes.py` fails every Geology document. |
| Q-8 | **Weekly review time.** Day, local time, and how to handle the Nov 1 DST change. |
| Q-9 | **Chemistry grading framing.** Gradebook says Tests 55 / Quizzes 20 / Labs 15 / Homework 7 / Binders 3. `CHEM_DECISIONS.md` says daily practice ≈10%. Homework 7 + Binders 3 = 10 — but "daily practice" and "homework + binders" are not obviously the same category. |
| Q-10 | **Gizmos exception.** The Geology skill forbids Gizmos; the built U1 S1.2 notes and a worksheet both use the Red Shift Gizmo. Named exception, or replace the activity? |
| Q-11 | **Dark backgrounds.** Part 6 makes light the default and dark occasional. Legacy Slide System v2 makes *dark* the projection ground for structural slides. Confirm dark is now the exception on slides too. |
| Q-12 | **Parchment's remaining role.** Part 7 demotes it from default background to special-purpose surface. It is currently the default content-slide background in `slide-standard.md`. |
| Q-13 | **Archive folder.** Add `99 Archive/` as an optional sixth Drive content folder? (Proposal P-3.) |
| Q-14 | **Physics unit map PDF.** `SHULL_Physics_Unit_Map_1.pdf` is cited as the source of the confirmed map but is not in Drive. Where is it? |
| Q-15 | **Ink-saving vs. white default.** Both point the same way, but the ink rule is a much stronger constraint than "white is the default background." Confirm the ink-saving rules survive into SHULL OS at full strength. |

---

## 23. Exact implementation sequence

Phases 1–6 are complete. Nothing below Phase 7 starts until §22's blocking questions are answered.

### ✅ Phase 1 — Inspect environment and repository
Done. §1–§8.

### ✅ Phase 2 — Inventory legacy files
Done. 10 installed skills + 6 Drive standards + `CHEM_DECISIONS.md` + 2 supplied spec files.
`docs/LEGACY_SKILL_AND_DESIGN_AUDIT.md`.

### ✅ Phase 3 — Extract design and course decisions
Done. 68 rules extracted with source, classification, conflict, and destination.

### ✅ Phase 4 — Conflict report
Done. `docs/CONFLICT_REPORT.md` — 28 conflicts, severity-ranked.

### ✅ Phase 5 — Propose authoritative standards
Done as a proposal. §9–§17. **Not written to disk as authority** — that is Phase 7, after approval.

### ✅ Phase 6 — Validate architecture
Done. Every claimed capability in this plan was checked against the live environment. Anything that
could not be verified is listed in §21 as a limitation, not asserted as a feature.

### ⛔ GATE — user review
Answer Q-1 through Q-6. Nothing below proceeds without them.

### Phase 7 — Repository structure
1. Resolve Q-1; establish the root.
2. Create the §9 tree, empty, with a `README.md` in each directory saying what it owns.
3. Snapshot the 10 installed skills verbatim into `legacy/skills/`.
4. Snapshot the 6 Drive standards + `CHEM_DECISIONS.md` verbatim into `legacy/drive-standards/`.
5. Write `CLAUDE.md` — identity, source-of-truth hierarchy, architectural principles, safety and
   change-control, where standards live, how agents operate. **Short.** Detail goes in standards.
6. Write `config/drive.json` with the seven verified folder IDs.
7. Commit. *Deliverable: a navigable, empty, documented skeleton.*

### Phase 8 — Standards, then agents
1. `brand/tokens.json` and `brand/SHULL_DESIGN_SYSTEM.md` from Part 46 + resolved Q-2…Q-5.
2. `brand/palette-archive/` — all five superseded palettes, each with a dated supersession note.
3. `standards/` — ANTI_AI_SLOP, VOICE, NAMING, DRIVE_ARCHITECTURE, QA_GATE.
4. `governance/GOVERNANCE.md` and `CHANGE_CONTROL.md`, adopting the legacy two-layer model.
5. **Then** the seven `.claude/agents/*.md`. Standards first — an agent with nothing authoritative
   to point at will invent rules, which is the failure this whole system exists to prevent.
6. Run T-2. *Deliverable: a governed system with no build capability yet.*

### Phase 9 — Skills and validators
1. The twelve skills from §11, each pointing at standards and restating nothing.
2. `validate_layers.py`, `validate_codes.py`, `validate_tokens.py`.
3. `.claude/settings.json` hooks: PreToolUse authority gates, Stop validator run.
4. Run T-1. *Deliverable: build capability, mechanically prevented from drifting.*

### Phase 10 — Drive integration
1. **Run T-3 first.** The Librarian's MOVE authority depends on the answer.
2. T-4, T-5, T-6.
3. `retrieve-drive-file` and `shelve-drive-file` against the real tree.
4. Librarian verification protocol: every operation logged before execution, destination confirmed
   by an independent `parentId` search after.
5. Resolve the §14.3 filing defects — **as proposals, executed only on approval.**
   *Deliverable: verified read/write to the real library.*

### Phase 11 — QA and deployment workflows
1. `workflows/build-deliverable.md` — the Part 34 seven-step chain.
2. `audit-deliverable` skill: render → rasterize → inspect. **Never ship a document unseen.**
3. `schemas/task-report.schema.json`; WORK COMPLETE only on a verified artifact at a verified path.
4. Run T-8. *Deliverable: a deliverable cannot ship unaudited.*

### Phase 12 — Course integration
1. `courses/chemistry/DECISIONS.md` — adopt `CHEM_DECISIONS.md` from Drive. **Chemistry first: it
   is fully mapped and is the reference implementation.**
2. `courses/physics/DECISIONS.md` — 11 units / 48 sections, confirmed. Record Q-14.
3. `courses/geology/DECISIONS.md` — **only after Q-3, Q-4, Q-7.** Until then it holds the confirmed
   unit list with numbering explicitly marked CONFLICT, and nothing is built against a Geology code.
4. `scripts/publish_standards.py` → `_Brand/Standards/`; document the Project read path.
   *Deliverable: three courses, one authoritative decisions file each.*

### Phase 13 — Weekly Researcher reporting
1. `weekly-system-review` skill — report-only, three hard limits (§16).
2. A Routine, at the time confirmed in Q-8.
3. Run T-9. *Deliverable: a system that notices its own drift and changes nothing on its own.*

### Phase 14 — Test the complete system
1. Run T-7 end-to-end on one real Chemistry section.
2. Run T-10.
3. Janitor's first full sweep; Auditor's independent review of the build.
4. Only after T-7 and T-10 pass: retire the legacy installed skills, replacing them with SHULL OS
   equivalents. **Until then both coexist and the legacy set stays untouched.**
   *Deliverable: SHULL OS V1.*

---

## Appendix A — Verified Drive folder IDs

| Location | ID | Verified |
|---|---|---|
| `SHULL Science/` (root) | `1FsFiaYfkwgSLnA62bpIHt2zGosFwcPec` | ✓ 2026-09-07 |
| `_Brand/` | `14Epgk_qgvxzSDljBABn72lSLYY6erF1Q` | ✓ |
| `_Brand/Templates/` | `1cFgdQbW8SSJaaXxzfCCr-IZMFjvaMg6J` | ✓ |
| `_Brand/Standards/` | `1aLMHcKoF4nrAKh121O2w5WgzVwSqOgZK` | ✓ |
| `_Brand/Image Library/` | `1RBK23kn2fcmBWiYidUDXSsVGk5NWXy3L` | ✓ |
| `Chemistry/` | `1dA5kKA9vQxaWX0CZMhXIoBMYGfDhMxH6` | ✓ 16 unit folders |
| `Physics/` | `1NOjl2nEZ1bjcjm32G55V265uGUoTErlk` | ✓ 1 unit folder |
| `Geology/` | `1lqHHql9cSqOZDGej2ff_121bITWOKZvr` | ✓ empty |

Owner on every object: `mshull@jagschools.org`.

---

## Appendix B — What this pass did and did not do

**Did:** read the repository; read account Claude config; read all 10 legacy SHULL skills; read 6
Drive standards documents and `CHEM_DECISIONS.md`; enumerate the Drive tree read-only; verify all
five previously-recorded folder IDs; enumerate available connectors; write four analysis documents
under `docs/`.

**Did not:** modify or delete any legacy skill; modify, create, rename, move, or trash any Drive
object; modify Claude Project Knowledge; write any standard as authoritative; resolve any conflict;
promote any PROVISIONAL or CONFLICT item to LOCKED; delete anything.

