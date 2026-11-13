# SHULL OS desktop

**Install it from <https://github.com/Hayabusa015/WorkWork/releases/latest>** — download
`SHULL-OS-Setup-<version>.exe` under Assets and run it. It installs for the current user, needs no
administrator rights, and no Node.js or terminal. `installer/README.md` covers the whole path,
including how a new installer gets built.

There is also a ZIP on each release for anyone who would rather not run an installer: extract all
of it and open `SHULL OS.exe`, keeping the resources folder beside the executable.

Python is bundled, so documents build out of the box. LibreOffice is not — install it normally and
the app finds it; without it you still get the `.docx`, but no in-app PDF preview and no print
audit. The app is unsigned, so Windows SmartScreen warns on first run (More info → Run anyway) and
school device policies may require IT approval.

Saved work lives in the Windows user's Electron application-data folder (`shull-os-desktop/data`), outside the installation. The Workspace menu opens it. Each computer has separate data. API keys remain in memory and must be reconnected after quitting; AI features require internet and Anthropic credits.

To migrate existing local work, close SHULL OS, copy `state.json`, document run folders and `reports` from your old `app/data` into the desktop data folder, and reopen SHULL OS. Back up both folders first. Do not copy `venv` or overwrite newer desktop work. Browser panel layouts are separate and do not migrate.

Development: run `npm ci` at the repository root, then `npm run desktop`. Populate `desktop/vendor/python` with a standalone Windows Python distribution and python-docx, fonttools, pillow, pymupdf; populate `desktop/vendor/LibreOffice` with a portable LibreOffice distribution. These third-party runtimes retain their bundled licenses and are excluded from Git. Set SHULL_PYTHON and SHULL_SOFFICE for development if vendor runtimes are absent.

Run `npm test` and `npx electron desktop/smoke.cjs` to verify. `npm run desktop:dist` builds a Windows ZIP with Electron and the repository resources; `npm run desktop:installer` builds the NSIS installer, and needs Windows. `.github/workflows/windows-installer.yml` runs all of it on a Windows runner and is the only supported way a release is made. Electron's backend binds an available loopback port and requires a random per-launch token added by the desktop session. The renderer uses sandboxing and context isolation without Node access. Download files through the normal interface; print from an opened PDF using Ctrl+P.

GitHub stores source code and, on each release, the built installer. It does not sync documents, settings or API balance between computers. Updates are automatic: the installed app checks this repository's releases about eight seconds after it opens and every six hours after that, downloads a newer version in the background, and installs it the next time the app is closed. `latest.yml`, published beside the installer, carries the SHA-512 `electron-updater` checks the download against; a download that does not match it is refused. Settings shows the state and offers an immediate restart. Nothing happens until at least one release exists, and nothing at all when running from source — there is no installation to replace. Signing is still future work, so the first install still passes through SmartScreen; an update does not, because it is the running app replacing itself.
