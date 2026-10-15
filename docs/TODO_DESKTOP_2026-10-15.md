# To do at the desktop (2026-10-15)

## A. Let Claude upload files to Drive (replaces manual uploading)

- [ ] Install the CLI: `npm install -g @googleworkspace/cli`
- [ ] Create a Google Cloud project (console.cloud.google.com), or use `gws auth setup` if `gcloud` is installed
- [ ] Create an OAuth client, type **Desktop app**; save the JSON to `~/.config/gws/client_secret.json`
- [ ] OAuth consent screen: add your own Gmail address under **Test users**
- [ ] `gws auth login -s drive` (Drive only; gmail.com accounts hit scope limits with more)
- [ ] `gws auth export --unmasked > credentials.json` (keep this file private; never paste it into chat)
- [ ] In the Claude environment settings (cloud environment menu, then Edit):
  - [ ] Network access: allow `www.googleapis.com`, `oauth2.googleapis.com`, `accounts.google.com`
  - [ ] Add the credentials as a secret / environment variable; note the variable name
- [ ] Tell Claude the variable name and that it's done, so it can run a test upload to a scratch folder
- [ ] Optional: consider the `drive.file` scope for narrower access (cannot touch existing files)

## B. Decisions Claude is waiting on

- [ ] Approve or change `governance/proposals/SHULL-CHG-0024-short-filenames.md` (new filename pattern)
- [ ] Approve or change `governance/proposals/SHULL-CHG-0025-humanize-skill.md` (humanizer skill)
- [ ] Drive renames: per course or all at once?
- [ ] `- Copy` files and the AutoRecovery file: trash them, or leave alone?
- [ ] Which unit and section do the unnumbered `SHULL_Geologic_Timeline_*` files belong to?

## C. After approval (Claude does these)

- [ ] Update `standards/NAMING.md`, the naming skill, `scripts/validate_codes.py`, and builders that emit `SHULL_` names
- [ ] Add `.claude/skills/humanize/` and the additive anti-AI-slop standard edits
- [ ] Build the old-to-new rename table with file IDs for your review
- [ ] Log old names to `reports/drive-operations/`, then rename in Drive
- [ ] Verify results and report as a table
