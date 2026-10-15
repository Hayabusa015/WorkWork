# To do at the desktop (updated 2026-10-15)

## Done

- [x] Google Workspace CLI installed and logged in (`drive.file` only)
- [x] Cloud project `shull-science-drive-2026`, OAuth client `GWS`
- [x] `GWS_CREDENTIALS_B64` saved in the Onboarding environment
- [x] Test upload landed in `SHULL Science / Upload Inbox` and was read back
- [x] Drive renames for groups A, B and C (77 files)
- [x] SHULL-CHG-0024 (short filenames), 0025 (humanize skill), 0026 (upload flow) implemented

## Do now

- [x] Test file `gws-upload-test.txt` trashed (by the user, 2026-10-15; checked: no longer found in Drive).
- [x] OAuth client secret: user confirmed it is fine (2026-10-15).

- [ ] **Check the first real upload.** Ask Claude to build one file and file it through the Upload Inbox. Confirm it lands in the right folder under its new name.

## Re-export the login (whenever the login changes)

```powershell
cd $HOME\Documents
gws auth export --unmasked | Out-File -Encoding ascii credentials.json
[Convert]::ToBase64String([IO.File]::ReadAllBytes("$HOME\Documents\credentials.json")) | Set-Clipboard
(Get-Clipboard).Substring(0,20)      # must start with: ew
Remove-Item $HOME\Documents\credentials.json
```

Then open the environment settings (gear next to **Onboarding**). Keep the Name as `Onboarding`. In the **Environment variables** box, set `GWS_CREDENTIALS_B64=` followed by a paste. Save, and start a new session.

## Decisions Claude is waiting on

- [ ] **Approve the second Drive rename** (short topics, SHULL-CHG-0041): `reports/drive-operations/2026-10-15_rename-plan-2.md`. 51 files; longest name 81 to 55 characters.
- [ ] `SHULL_PHYS_Practice_Set_U01_S1.1.docx` would get the same new name as another file in its folder. Duplicate to trash, or a different version?
- [ ] The group D files (no unit or section code): Element Builder, Atomic Theory Jigsaw, Guided Notes variants, Lab Equipment, Math Skills Pretest and others. What unit and section, or leave alone? The list is in `reports/drive-operations/2026-10-15_rename-plan.md`, section D.
- [ ] The three duplicates in the `pdf` staging folder (Geologic Timeline 4 Pages Cenozoic, Cutouts 38 Events, Time Reference Guide): trash them?

## Later

- [ ] Physics and the other Geology units: Drive folders for them are not checked yet.
- [x] Geologic Timeline files stay in `Unit 02 - Geologic Time / Homework`. User decision 2026-10-15: leave them there. This is a recorded exception to SHULL-CHG-0030 (no Homework folder).
- [ ] The Desk in the local app does not list governance proposals. Ask Claude to scope it if you want that.

## If something breaks

- **PowerShell says scripts are disabled:** `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`, or use `npm.cmd` and `gws.cmd`.
- **"OAuth client was not found":** `client_secret.json` holds the wrong Client ID. Re-download it from the `GWS` client.
- **A session says credentials are not set:** the variable is empty or went in the wrong box, or the session started before it was saved. Check the settings, then start a new session.
- **Cut off access completely:** `myaccount.google.com/permissions`, find **Shull Drive Upload**, remove access.
