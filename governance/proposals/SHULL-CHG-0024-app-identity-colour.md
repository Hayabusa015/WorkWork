---
id: SHULL-CHG-0024
title: The SHULL OS application gains its own identity colour — Signal Green, screen only
status: IMPLEMENTED
opened: 2026-09-20
decided: 2026-09-20
source: User
decided_by: Matthew Shull
---

# SHULL-CHG-0024 — The app's own colour

## What he asked for

> "Use that icon and theme in the full design"
>
> — 2026-09-20, sent with a SHULL OS badge logo he had made. The badge is committed at
> `build/icon-source.png` and is already the Windows app icon (`build/icon.ico`,
> `scripts/build_app_icon.py`).

The icon half of that instruction was already satisfied. The **theme** half was not: the badge
carries a green the token file had never heard of, and the app was wearing a borrowed colour.

## Current Rule

The app took its accent from `courses.geology.primary` — Terra Teal `#16B8A6`. `scripts/build_app_css.py`
says so in as many words:

> `# Geology's Terra Teal is the app's own accent: the workspace is not a course,`
> `# and this is the identity the shipped app already carried.`

That comment is honest about why it was done — the workspace is not a course and had no colour of
its own, so one was borrowed. It was a stand-in. **The app is not Geology**, and a workspace that
wears a course's colour teaches the wrong thing every time a Geology document is open beside it.

## Proposed Rule

`identity.signal` — **Signal Green `#00C84C`** — is the SHULL OS application accent. It is a new
top-level `identity` block in `brand/tokens.json`, sitting between `courses` and `semantic` because
it is neither.

- **Course colours are unchanged.** Chemistry, Physics and Geology keep their palettes and still
  scope by course; a Chemistry card still cannot end up wearing a Geology accent.
- **Signal Green is screen-only.** The app is a dark workspace and this colour is specified against
  that ground.

## The measurements

These are the reason the decision is safe, and the reason its limits are hard:

| Against | Ratio | Verdict |
|---|---|---|
| Asphalt `#14161B` | **8.07:1** | Clears the 5.5 SHULL type target with margin. AAA band. |
| White `#FFFFFF` | **2.24:1** | **NOT type on a light ground.** Fill, rule, border or block only. |
| Grayscale | **126** | See conflicts below. |

The app ground is asphalt, which is the ground this colour was chosen for. On white it is not type
and no amount of wanting it to be will change that.

No `measured` block was hand-written into `brand/tokens.json`. `scripts/measure_tokens.py` computes
those, and a hand-edited one is a defect.

## Conflicts found

`rules.grayscaleSeparationMin` is **20**. Signal Green is grayscale **126**, and it is closer than
the floor to two colours that carry a categorical distinction:

| Pair | Separation | Floor |
|---|---|---|
| `identity.signal` (126) vs `courses.geology.primary` Terra Teal (134) | **8** | 20 |
| `identity.signal` (126) vs `semantic.success` (137) | **11** | 20 |

Both are under the floor. `rules.note` is explicit about what follows: any two colours carrying a
categorical distinction that are closer than the floor **MUST differ additionally by border and
label**, never by fill alone. Two consequences, both binding:

**a) Status badges.** A "good" status badge in the app is `semantic.success`, and it sits beside the
accent. In greyscale the two collapse into each other — 11 levels apart. A success badge **must
carry a glyph and a border**, not fill alone. Fill-only green-on-green is now a defect, not a taste
question.

**b) Geology surfaces beside app chrome.** A Geology surface is within 8 levels of the accent.
Geology course cards already carry a course-name label and a left border, which satisfies the
escape hatch exactly as written — **nothing further is required**. It is recorded here so the next
person to measure it does not rediscover it and think it is a new problem.

This is the same shape of finding as the note on `courses.geology`, where the display pair sits 6
levels apart. The escape hatch is a real hatch, not a waiver: it costs a border and a label.

## Risk

**Medium.** It changes every screen in the app, and it pushes two colour pairs onto the
border-and-label escape hatch rather than clearing the greyscale floor outright. Nothing printed is
affected, and no course decision is touched.

## Supersedes

`scripts/build_app_css.py`:

- the line `  --accent:       var(--t-geo);` (and the `--accent-bright` / `--accent-deep` /
  `--accent-ink` mixes derived from `--t-geo`), and
- the comment above `APP = c["geology"]` claiming Geology's teal as the workspace identity.

## Deliberately NOT changed

**Print.** No deep variant is proposed and none should be invented. At **2.24:1 on white** this
colour cannot be type on paper, and a `signalDeep` conjured to make it so would be a new colour
nobody sampled from the badge. The print templates keep taking course colour from `courses.*`,
which is where a printed page's identity belongs — a worksheet belongs to a course, not to the
application that built it.

## Verification

Pending. The token block is in place and the record is written; the generated app CSS and the app
itself are Matthew's to update, and the accent swap is not verified until a screen has been looked
at. **IMPLEMENTED is not verified.**

**Implemented By:** pending
**Verified:** pending
