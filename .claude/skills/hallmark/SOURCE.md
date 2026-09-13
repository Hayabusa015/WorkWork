# Source

Vendored verbatim from [nutlope/hallmark](https://github.com/nutlope/hallmark), commit `13ac0ec`,
2026-09-13. MIT licensed — see `LICENSE` in this folder. Not written for or by SHULL OS.

## Scope in this repository

**This is a website-UI design/audit skill.** It builds and audits HTML/CSS pages — it has no
concept of a `.docx`/`.pptx`/`.pdf` print document, a course palette, or a `U#/S#.#` code. Nothing
in the five SHULL document systems (lab, notes, worksheet, slide, assessment) is a website, so
Hallmark has no reason to trigger on them and shouldn't be asked to.

**The one place it applies here is `app/`** — the Codex-built local application's HTML/CSS/JS front
end (`app/public/index.html`, `app/public/style.css`, `app/public/app.js`). That app is its own
track, outside SHULL OS governance (see `change-log/CHANGELOG.md`'s note on the `app/`/`desktop/`
additions), so Hallmark is scoped to it the same way: added for that surface, not folded into the
SHULL build/QA system.

## Not to be confused with `anti-ai-slop`

This repo already has its own `.claude/skills/anti-ai-slop/` — the QA pass for SHULL print
documents (voice, task design, accuracy, the standing audit). Hallmark's own tagline is "Anti-AI-Slop
design skill," but it is a different tool for a different medium. Same phrase, two unrelated skills:
`anti-ai-slop` never touches a website, and `hallmark` never touches a classroom document.

## Not re-vendored automatically

This is a point-in-time copy, not a live dependency. Updating it means re-pulling from upstream and
diffing by hand — there's no mechanism here that tracks or applies nutlope/hallmark's own updates.
