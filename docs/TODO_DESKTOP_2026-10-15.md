# To do at the desktop (updated 2026-10-15)

## Done

- [x] Google Workspace CLI installed and logged in (`drive.file` only)
- [x] Cloud project `shull-science-drive-2026`, OAuth client `GWS`
- [x] `GWS_CREDENTIALS_B64` saved in the Onboarding environment
- [x] Test upload landed in `SHULL Science / Upload Inbox` and was read back
- [x] Drive renames for groups A, B and C (77 files)
- [x] SHULL-CHG-0024 (short filenames), 0025 (humanize skill), 0026 (upload flow) implemented

## Do now

- [ ] **Trash the test file.** In Drive, open `SHULL Science / Upload Inbox` and move `gws-upload-test.txt` to the trash. (The repo's safety hook stops Claude doing it.)
- [ ] **Replace the OAuth client secret.** It appeared in a screenshot on 2026-10-15.
  1. Cloud Console, `shull-science-drive-2026`, APIs & Services, Credentials, open `GWS`.
  2. Add a new secret, then delete the old one. Download the new JSON.
  3. Save it as `C:\Users\Shull\.config\gws\client_secret.json` (replace the old file).
  4. `gws auth logout`
  5. `gws auth login --scopes https://www.googleapis.com/auth/drive.file`
  6. `gws auth status` and confirm only `drive.file` plus the sign-in scopes.
  7. Export and update the variable (see "Re-export the login" below).
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

- [ ] `SHULL_PHYS_Practice_Set_U01_S1.1.docx` would get the same new name as another file in its folder. Duplicate to trash, or a different version?
- [ ] The group D files (no unit or section code): Element Builder, Atomic Theory Jigsaw, Guided Notes variants, Lab Equipment, Math Skills Pretest and others. What unit and section, or leave alone? The list is in `reports/drive-operations/2026-10-15_rename-plan.md`, section D.
- [ ] The three duplicates in the `pdf` staging folder (Geologic Timeline 4 Pages Cenozoic, Cutouts 38 Events, Time Reference Guide): trash them?

## Later

- [ ] Physics and the other Geology units: Drive folders for them are not checked yet.
- [ ] `Unit 02 - Geologic Time` has a `Quiz` folder instead of the standard `Tests-Quizizz`.
- [ ] The Desk in the local app does not list governance proposals. Ask Claude to scope it if you want that.

## If something breaks

- **PowerShell says scripts are disabled:** `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`, or use `npm.cmd` and `gws.cmd`.
- **"OAuth client was not found":** `client_secret.json` holds the wrong Client ID. Re-download it from the `GWS` client.
- **A session says credentials are not set:** the variable is empty or went in the wrong box, or the session started before it was saved. Check the settings, then start a new session.
- **Cut off access completely:** `myaccount.google.com/permissions`, find **Shull Drive Upload**, remove access.
