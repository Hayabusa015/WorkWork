# SHULL OS desktop

Extract the entire Windows ZIP, then open `SHULL OS.exe`. Keep the resources folder beside the executable. Python and LibreOffice are included in the prepared distribution. No Node.js or terminal is required to run it. The app is currently unsigned; school device policies may require IT approval.

Saved work lives in the Windows user's Electron application-data folder (`shull-os-desktop/data`), outside the installation. The Workspace menu opens it. Each computer has separate data. API keys remain in memory and must be reconnected after quitting; AI features require internet and Anthropic credits.

To migrate existing local work, close SHULL OS, copy `state.json`, document run folders and `reports` from your old `app/data` into the desktop data folder, and reopen SHULL OS. Back up both folders first. Do not copy `venv` or overwrite newer desktop work. Browser panel layouts are separate and do not migrate.

Development: run `npm ci` at the repository root, then `npm run desktop`. Populate `desktop/vendor/python` with a standalone Windows Python distribution and python-docx, fonttools, pillow, pymupdf; populate `desktop/vendor/LibreOffice` with a portable LibreOffice distribution. These third-party runtimes retain their bundled licenses and are excluded from Git. Set SHULL_PYTHON and SHULL_SOFFICE for development if vendor runtimes are absent.

Run `npm test` and `npx electron desktop/smoke.cjs` to verify. `npm run desktop:dist` builds a Windows ZIP with Electron and the repository resources. Electron's backend binds an available loopback port and requires a random per-launch token added by the desktop session. The renderer uses sandboxing and context isolation without Node access. Download files through the normal interface; print from an opened PDF using Ctrl+P.

GitHub stores source code. It does not automatically sync documents, settings or API balance between computers. Automatic updates and signing are future work.
