# Legacy snapshot — slide template source

**READ ONLY. Never edited.** Retrieved from Drive `_Brand/Templates/` on 2026-09-08.

| File | Drive ID | Bytes | Drive modified | Verified |
|---|---|---|---|---|
| `build.js` | `1sLqG7h-JevP0-3c__aSpG3T8Nc1YIO3R` | 27,880 | 2026-09-06 | byte count matches Drive metadata |
| `tokens.js` | `14XeahgFiuLyv0iIioztfueq6-IxtK8Kx` | 1,329 | 2026-09-05 | byte count matches Drive metadata |
| `tokens.phys.js` | `1Y7ZuwDkBhv4u-4w1X4Nyqa-5hViGk5Dk` | 1,863 | 2026-09-06 | byte count matches Drive metadata |

## Not snapshotted, and why

`SHULL_Science_Slide_Template.pptx` (`1eAeIvhA-i1ou3FWzzlg2aqmhWxFzoKlo`, 20,658,366 bytes) is the
**output** of `build.js`, not a source. It is 20 MB because `build.js` embeds seven full-resolution
photographs directly into the slide masters — see finding 4 of
`governance/proposals/SHULL-CHG-0013-slide-template.md`. It stays in Drive, untouched.

The seven `.png` files and `demo_u1.js`, `make_art.py`, `regrade.py` in the same Drive folder are
image assets and utilities, not template source. They are untouched and unmigrated. That
`_Brand/Templates/` holds loose images at all is a filing defect for the Janitor, not for this
migration.

## What this snapshot is for

It makes the migration provable. Every change SHULL-CHG-0013 records can be diffed against these
three files, and a claim that the new template "preserves the structure" can be checked rather than
believed.
