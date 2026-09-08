# Governance

**Adopted, not invented.** This is `_Brand/Standards/SHULL_System_Governance.md` — which was already
CONFIRMED and largely correct — carried forward with one substantive change and the Part 4 authority
model added. Verbatim source: `legacy/drive-standards/SHULL_System_Governance.md`.

---

## 1. The one rule

> **A fact lives in exactly one place.**

Duplication is the defect. Not forgetting to update, not disorganisation — duplication.

Every conflict this system has had came from the same fact being written twice: the Geology palette
sat in both an export and a skill file; the curriculum map sat in both; the base palette was typed
by hand into three skills. When one copy changed, the others went quietly stale.

If duplication is genuinely unavoidable, **the duplicate must point at the authoritative source
rather than restate it.**

## 2. The two layers

**Layer 1 — standards and skills own the build.** How a document is made. Course-independent.
Changes once or twice a year. Brand, layout, structure, design philosophy, doc-code grammar, folder
routing, the QA gate, voice, the anti-slop rules.

**Layer 2 — course decisions own the content.** What is taught in one class. Course-specific.
Changes constantly. Curriculum map, pacing, calendar, policies, population and rigor, assessment
shape, lab and activity philosophy, reference packet, real-world themes.

### The line, stated as a test

> Changing it affects **all three courses** → Layer 1.
> Changing it affects **one course** → Layer 2.

A thinner summary-box border is a Layer 1 change. Moving Plate Tectonics from U4 to U5 is Layer 2.

### The change from the legacy model

Layer 2 lived in Claude Project Knowledge. It now lives in `courses/<course>/DECISIONS.md` in this
repository, **because Project Knowledge has no version history and no write path.** Everything else
about the model is unchanged.

### Course skills point, never restate

A course profile says how that course differs *in build terms* — rigor level, which document types
it uses, which conventions apply. **It must not carry the curriculum map, the calendar, the grading
policy, or the section list.** Where it does, the content is replaced with a pointer:

> **Curriculum map.** Lives in `courses/geology/DECISIONS.md`. Read it there. Never build against a
> unit or section code that isn't in that file.

That single change is what stops a skill needing an edit every time a course adjusts.

## 3. Precedence

1. Matt's direct instruction in the current conversation
2. **For course facts** — the course `DECISIONS.md`
3. **For build mechanics** — the standard, then the skill
4. **LOCKED** over **INHERITED** over **PROVISIONAL**
5. Newer dated entry over older

> When a skill states a course fact that the decisions file contradicts, **the decisions file wins
> and the skill is reported stale.** It is not silently obeyed and it is not silently ignored.

When the layers genuinely overlap and it is not clear which is which: **stop and ask. One question.
Do not guess, and do not build on the guess.**

## 4. Classification

| Label | Meaning |
|---|---|
| **LOCKED** | Explicitly approved by the user |
| **INHERITED** | Consistently supported across the system, no meaningful conflict |
| **PROVISIONAL** | Useful, not sufficiently established |
| **CONFLICT** | Two or more incompatible rules exist |
| **DEPRECATED** | Superseded by a newer decision |
| **ARCHIVE** | Historical, preserved for reference, not active |
| **UNKNOWN** | Insufficient evidence |

> **Never silently convert CONFLICT, PROVISIONAL, or UNKNOWN into LOCKED.**
> **Never present a PROVISIONAL or CARRIED OVER item as CONFIRMED.**

Inference must never quietly become an authoritative rule.

## 5. Authority

| | Read | Create deliverable | Modify deliverable | Modify standards | Drive create | Drive rename/move | Drive trash |
|---|---|---|---|---|---|---|---|
| **Overseer** | ✓ | ✓ | limited | ✗ | ✗ | ✗ | ✗ |
| **Researcher** | ✓ | reports only | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Designer** | ✓ | ✓ | assigned only | ✗ | ✗ | ✗ | ✗ |
| **Librarian** | ✓ | ✓ | ✗ | ✗ | ✓ | deterministic only | **approval** |
| **Janitor** | ✓ | reports only | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Secretary** | ✓ | proposals | ✗ | **approved only** | ✗ | ✗ | ✗ |
| **Auditor** | ✓ | reports only | ✗ | ✗ | ✗ | ✗ | ✗ |

### The three rules that make this work

1. **Only the Secretary writes to `brand/`, `standards/`, `governance/`, and `courses/`, and only
   against an APPROVED proposal ID.** Everyone else proposes.
2. **The Auditor never fixes what it finds.** It reports; the Overseer routes the fix.
3. **A returned message is not a completed task.** A task is complete only when the deliverable has
   been verified to exist at a verified location.

### Not authorised, at any level

Permanent deletion of legacy material · destructive Drive operations · autonomous modification of
core standards · autonomous rewriting of the design system · autonomous weekly system changes.

## 6. Checks

**Before any build** — confirm the unit and section code exists in that course's `DECISIONS.md`.
Never build against a code from a skill file alone.

**On every commit** — `validate_layers.py` (a course fact in a skill), `validate_codes.py` (a code
with no decisions entry), `validate_tokens.py` (a hex outside `tokens.json`),
`measure_tokens.py --check` (stale measurements). `legacy/` is excluded from all four.

**Weekly** — the Researcher and Janitor sweep. **Report-only.** See
`workflows/weekly-system-review.md`.

**Every audit output uses one format**, sorted blocking first, then shortest fix first:

| # | File | Problem | Your action | Time |
|---|---|---|---|---|

No prose, no preamble. Anything over ten minutes gets broken into smaller rows.

## 7. What the system cannot do

Stated plainly so nothing is built on top of it:

- **Claude cannot write to Claude Project Knowledge.** Every such update is a file the user uploads.
- **Claude cannot write to installed skills.** Same.
- **Nothing propagates on its own.** There is no background sync.
- **A Claude Project cannot invoke Claude Code agents.** No bridge exists.
- **Drive objects cannot be permanently deleted.** Only trashed.
- Past-chat search cannot cross Claude Project boundaries.

**Git is the only durable write path in this system.** That is the entire argument for this
repository, and it is why the Secretary can exist at all.

## 8. Why this shape

The system cannot organise itself. So the design compensates in the other direction: **make drift
impossible to miss rather than impossible to happen.**

Three things do that work. One home per fact, so drift is rare. A code check before every build, so
drift cannot reach a printed page. Validators that fail a commit, so drift cannot survive review.

> **A to-do list inside a document is not a mechanism.** The legacy governance file carried a
> well-written fix list naming seven specific cuts to one skill. Nobody worked through it, and the
> drift it described was still live days later. That is why §6 is validators and not a table.
