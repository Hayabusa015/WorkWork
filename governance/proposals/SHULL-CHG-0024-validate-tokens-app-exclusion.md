Change ID:        SHULL-CHG-0024
Date:             2026-09-18
Source:           Janitor (weekly-system-review, 2026-W38)
Current Rule:     `scripts/validate_tokens.py` scans every file in the repository (excluding
                  `legacy/`) for a raw hex value and fails the build if one appears outside
                  `brand/tokens.json`.
Proposed Rule:    Two options, not adjudicated here:
                  (a) Exclude `app/public/` from `validate_tokens.py`'s scan, on the same footing
                  as `legacy/` — the desktop app's UI chrome is not a teaching deliverable and was
                  never in scope when the rule and the design system were written.
                  (b) Leave the rule as-is and have the desktop app's `app/public/style.css`
                  consume `brand/tokens.json` (via the same generated-token pipeline
                  `build_slide_tokens.py` / `build_lab_css.py` use), so the app's chrome is
                  brand-consistent with everything else SHULL OS produces.
Supersedes:       none — this is a gap, not a contradiction of a prior rule
Reason:           `validate_tokens.py` currently FAILs on 13 raw hex values in
                  `app/public/style.css` (lines 32–34): `#00bdb0 #143c3b #168e85 #42dbc5 #4a8e89
                  #5ac6b8 #71d9cf #77e8d9 #83e4d7 #8de3d6 #9af0e2 #a3f4e8 #ffb497`. None of these
                  match the locked course palettes in `brand/tokens.json`. The validator is doing
                  exactly what it was built to do (Phase 9, SHULL-CHG-0006's sibling rule) — the
                  gap is that the desktop app (added 2026-09-11, after the validator was written)
                  was never accounted for as a category. Option (a) treats the app as out-of-scope
                  software UI, matching how `legacy/` is already excluded. Option (b) treats it as
                  in-scope and brings it under brand governance, at the cost of the app losing its
                  independent colour choices and needing a build step to consume the token file.
Affected Agents:  none directly; `validate_tokens.py` is run by every agent's Stop-hook validation
                  pass and by `weekly-system-review`
Affected Skills:  none
Affected Courses: none
Risk:             low — either option is a small, contained change (a path exclusion, or a CSS
                  variable swap); the risk is choosing wrong, not choosing hard
Recommendation:   Option (a). The desktop app is a local tool for running the agent workflow, not a
                  student- or teacher-facing deliverable, and the design system's whole purpose
                  (§brand/SHULL_DESIGN_SYSTEM.md) is course identity for print and slides. Forcing
                  it onto `tokens.json` would import course-specific colour choices into
                  general-purpose software chrome for no benefit. This is a recommendation, not a
                  decision — the user may prefer (b) for a simpler mental model ("one palette,
                  everywhere").
Decision:
Status:           PENDING
Implemented By:
Verified:
