# Extraction Taxonomy

What counts as a finding, how to attribute it, and where it lands.

## The provenance rule

Every finding carries who said it. Retrieved chats interleave Matt's turns and Claude's, and
a summary chunk (`kind='summary'`) may have collapsed a Claude recommendation and Matt's
reaction into one phrase like "decided on X." When both a transcript and a summary are
available, **prefer the transcript's wording.**

| Source | Attribution | Max label |
|---|---|---|
| Human turn stating a rule or decision | Matt decided | `CONFIRMED` (proposed, not applied) |
| Human turn correcting Claude's output | Matt decided | `CONFIRMED` (proposed, not applied) |
| Assistant turn proposing, Human approves | Claude proposed, Matt approved the draft | `WORKING` |
| Assistant turn proposing, Human silent | Claude proposed | Not recorded |
| Explicitly hypothetical or brainstorm | Hypothetical | Not recorded |
| Summary chunk only, no transcript | Summary, unverified | `WORKING` at most |

Before writing "Matt decided X," confirm a Human turn actually says it. If the evidence is a
Claude draft he liked, write it as a draft he liked.

## Finding categories

### 1. Locked specifications
A format, constraint, or template Matt fixed. Two-page practice-set limit. The 8-question
tier structure. The 16pt slide floor. Gradebook weights.

→ Tier C if it changes an existing lock. Tier A if it's a lock on something previously
unspecified and Matt stated it directly.

### 2. Conventions and naming
Filenames, doc codes, folder logic, chip styles, footer text.

→ Tier A or B. Cross-check `shull-studio/references/file-routing.md` — if the convention
drifted in practice, that's worth flagging even if neither version is wrong.

### 3. Course content facts
Unit and section titles, lab placements, which labs are purchased vs. built, standards
alignment, pacing decisions.

→ Tier A when new, Tier C when it contradicts the curriculum map. Never invent a section
number to fill a gap — record the gap.

### 4. Classroom operations
Supplies in stock, equipment available, period length, cleanup sequences, disposal rules,
routines like the Friday Reset, binder criteria.

→ Tier A. These change frequently and are exactly what a sweep is good for. A new reagent
in stock is worth a line; the specific volume used in one lab is not.

### 5. Tooling and environment
What renders, what silently fails, library availability, font fallbacks, path requirements.

→ Tier A. The `file://` prefix requirement for WeasyPrint local assets is the model case:
learned once the hard way, saves an hour every time it's remembered.

### 6. Working patterns
Sequence, batch size, correction habits, vocabulary, where he takes over.

→ **Never applied directly.** Reported under "Observed patterns" once seen three times
independently. Matt promotes it or he doesn't.

### 7. Completions
Documents finished, units closed out, materials delivered.

→ Tier A. Keeps the librarian's gap audit accurate. This is the highest-volume, lowest-risk
category and usually the bulk of a sweep.

## Drop it (Tier D)

- A value, number, or wording used once in one document
- Preferences expressed about a single deliverable rather than a class of them
- Claude's own reasoning, plans, or self-assessment
- Anything already recorded — check before adding
- Task chatter: "make it shorter," "try again," "looks good"
- Restatements of something already in the guidelines file

When unsure between D and A, drop it. A finding missed this sweep gets caught next sweep if
it mattered. A wrong entry in the guidelines file propagates into every document built from
it and is much harder to notice.

## Conflict handling (Tier C)

Write the conflict so Matt can resolve it in ten seconds without opening anything:

```
FINDING:      [what the recent chat indicates]
EVIDENCE:     [chat name, date, and who said it]
CONFLICTS:    [the exact existing line, quoted, and where it lives]
IF APPLIED:   [what else changes — other docs, skills, or specs affected]
```

Never resolve a conflict by reasoning about which is more likely correct. The newer statement
is often right, but "often" is not a basis for rewriting a CONFIRMED policy while Matt is
asleep.

## Sanity checks before writing the updated guidelines file

- [ ] Every confidence label still accurate — nothing silently upgraded to CONFIRMED
- [ ] No Tier C change applied
- [ ] No section, unit, date, or policy invented to fill a gap
- [ ] Existing CONFIRMED entries byte-identical unless Matt explicitly changed them
- [ ] Gaps preserved as gaps, not quietly closed
- [ ] The file still parses: valid frontmatter, `name` and `description` intact
- [ ] Diff the draft against the current file and eyeball it — an unexpectedly large diff
      means something went wrong in extraction, not that the sweep was productive
