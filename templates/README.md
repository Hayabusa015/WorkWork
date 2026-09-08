# templates

Build sources for generated artifacts — principally the twelve-layout slide template.

`templates/slide-template/src/` holds `tokens.js` and `build.js`. Change a token, run
`node build.js`, and all twelve layouts follow. `build.js` selects its token module from
`process.env.SHULL_TOKENS`, so a course palette variant supplies its own file rather than forking
the build. **That indirection is the best engineering in the legacy system — preserve it.**

Generated from `brand/tokens.json`. Never hand-edit a token here.

*Status: both templates are migrated and on the token system. The lab template landed in Phase 9
(SHULL-CHG-0010); the twelve-layout slide
template has not been migrated yet.*
