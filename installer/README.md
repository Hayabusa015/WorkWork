# Installer

## Installing it (what a teacher does)

1. Go to **<https://github.com/Hayabusa015/WorkWork/releases/latest>**
2. Under **Assets**, download `SHULL-OS-Setup-<version>.exe`
3. Run it.

Windows will show a blue **"Windows protected your PC"** box, because the installer is not
code-signed. **More info → Run anyway.** A school-managed PC may refuse outright; that needs IT.

It installs for the current user only — no administrator rights — into
`%LOCALAPPDATA%\Programs\SHULL OS`, with a Start Menu and desktop shortcut, and opens when it
finishes. Saved work lives in the Electron user-data folder, **outside** the installation, so
reinstalling or updating does not touch it.

**Python is bundled.** Building Word documents works out of the box.
**LibreOffice is not bundled** — it is larger than everything else combined. Without it you still
get the `.docx` to open and print from Word; what you lose is the in-app PDF preview and the print
ink/page audit. Install LibreOffice normally and the app finds it on its own
(`desktop/main.cjs` checks Program Files, Program Files (x86) and LocalAppData).

## Making one (what Matthew does)

Nothing is built by hand, and nothing is built on Linux — NSIS needs Windows, and the bundled
Python is a Windows build. `.github/workflows/windows-installer.yml` does it on a Windows runner.

**To test a build without publishing anything:** Actions tab → **Windows installer** →
**Run workflow**. The installer is attached to that run; download it from the run page.

**To publish a release people can link to:**

```bash
npm version 0.2.0 --no-git-tag-version   # optional; the tag sets the version anyway
git tag v0.2.0
git push origin v0.2.0
```

The workflow runs the tests, bundles Python, verifies that the bundled Python can really build a
worksheet, boots the app and reads its UI back, builds the installer, and attaches it to a new
GitHub Release. **Any of those failing stops the release** rather than shipping a broken one.

The tag is the version. `electron-builder` names the artifacts from `package.json` and writes that
same version into `latest.yml` — so the workflow rewrites `package.json` from the tag to keep them
in step. A release tagged `v0.2.0` is what makes every installed `0.1.0` update itself, without
anyone being asked.

`latest.yml` is the release asset that makes that work: it names the installer and carries its
SHA-512, and the app refuses a download whose hash does not match. The workflow fails rather than
publish a release without it. Do not delete it from a release, or every installed copy stops
seeing updates — they read that file, not the release page.

## The two files beside this one are superseded

`install.ps1` and `SHULL-OS-Setup.sed` are how the 0.1.0 installer was made: IExpress wrapping a
ZIP and a PowerShell script. **Neither works anywhere but the machine they were written on** —
`SHULL-OS-Setup.sed` names absolute paths under
`C:\Users\Shull\Documents\Codex\2026-09-10\...`, and the ZIP it wraps
(`SHULL-OS-0.1.0-Windows.zip`) is gitignored and not in the repository.

The NSIS installer electron-builder produces does the same job — per-user install, shortcuts,
launch on finish — from a configuration that lives in `package.json` and runs anywhere. These two
files are kept for now only so the old mechanism is on the record; they are not a fallback, and
following them will not produce an installer.
