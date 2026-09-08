# Mobile and Claude Project workflow

**Authority:** spec Part 35 — *"The implementation must explicitly document how Project work enters
the SHULL OS execution workflow. If direct invocation is not technically available, do not pretend
it is."*

This file exists because the honest answer is unsatisfying, and an unsatisfying answer written down
is worth more than a satisfying one that is false. Read
`docs/SHULLOS_IMPLEMENTATION_PLAN.md` §8 for the capability table this rests on.

---

## 1. The one-sentence version

**A Claude Project cannot start a SHULL OS build. You are the bridge, and the bridge is
copy-and-paste.**

There is no webhook, no "run in Claude Code" button inside a Project, no background sync, and no
scheduled job that watches a Project for new requests. If a future release adds one, it gets a
change record and this file gets rewritten. Until then, anything in this file that sounds like
automation is not.

---

## 2. What each surface is actually for

| | Claude Project (phone, browser) | Claude Code (this repo) |
|---|---|---|
| **Good at** | Thinking out loud, drafting prose, reading Drive, answering "what did I decide about X" | Building the artefact, running QA, changing a rule |
| **Cannot** | Run agents, run skills from this repo, write to Git, write to its own Knowledge | Read Project Knowledge |
| **Use it when** | You are in a hallway with four minutes | You are producing something students will hold |

The split is not a preference. A Project has no filesystem and no subagents, so the Overseer →
Designer → Auditor → Librarian chain physically cannot run there. A build attempted in a Project is
a build that skipped QA.

---

## 3. The loop, in the order it actually happens

### 3.1 Capture (phone, Project) — costs you nothing

Talk to the course Project like a colleague. *"U4.2 needs a lab on density columns, 45 minutes, the
Tuesday group will get bored if it's a worksheet."* Let it argue with you. This is where the
thinking belongs, and it is the part that is genuinely good on a phone.

**Ask it to end with a build request** — one paragraph naming the course, the section code, the
deliverable type, and the constraints you just talked through. That paragraph is the payload.

### 3.2 Carry (you) — the bridge

Copy the paragraph. Open Claude Code — web, desktop, or CLI, whichever is in front of you. Paste it.

That is the whole handoff. There is no step being hidden here.

### 3.3 Build (Claude Code) — where the system exists

The paste enters `workflows/build-deliverable.md`. Agents, skills, tokens, QA gate, the naming
grammar, the anti-slop check. Output lands in Drive under the structure in
`standards/DRIVE_ARCHITECTURE.md`, and a task report lands in `reports/`.

### 3.4 Return (Drive) — the shared surface

Both surfaces read the same Drive. The Project can open what Claude Code just built, because it is a
real file in a real folder, not a message in a conversation. This is why Drive is the canonical file
library and not a backup: **it is the only thing both halves of the system can see.**

---

## 4. Keeping the Project honest

A Project's Knowledge goes stale silently, and a stale Project confidently quotes a superseded rule.
Two defences, and only the second one is a mechanism:

**Published standards (mechanism).** `scripts/publish_standards.py` emits the plan to render this
repo's standards into Drive `_Brand/Standards/`. The Librarian executes it. A Project pointed at
that folder reads current rules without you uploading anything.

> One direction only. The repo is the source; the Drive copy is a rendering. **Nothing in
> `_Brand/Standards/` is authoritative**, and a Project must never be asked to edit it.

**Project Knowledge (manual, unavoidable).** Claude cannot write to Project Knowledge from any
surface. If a file must live in Knowledge rather than Drive, you upload it. SHULL OS's obligation is
to hand you a finished file and tell you plainly that it is now your turn — never to imply it
propagated on its own.

---

## 5. What to do on a phone, and what to refuse to do on a phone

**Reasonable on a phone:** capture a request · ask what a rule says · read a built handout · approve
or reject a change proposal · notice a problem and write it down.

**Not reasonable on a phone, and the system should say so rather than comply:** approving a palette,
a standard, or a design-system change. Those decisions are judged by looking at rendered output, and
a phone screen is the wrong instrument. `governance/CHANGE_CONTROL.md` requires the user's approval;
this file adds that a rule change deserves a real screen.

---

## 6. Scheduled work

Claude Code supports Routines. **The weekly system review is report-only, permanently** — see
`governance/GOVERNANCE.md`. A scheduled run may produce a findings report and nothing else. It may
not edit `brand/`, `standards/`, `governance/`, or `courses/`, and no Routine may approve a change
record. A schedule is not a second user.

---

## 7. When this file becomes wrong

Rewrite it, under a change record, the moment any of these becomes true:

- A Project gains the ability to invoke Claude Code, or any tool in this repo.
- Project Knowledge becomes writable by any Claude surface.
- A Drive-watching trigger makes §3.2 unnecessary.

Until one of those ships, §1 is the whole truth: **you are the bridge.**
