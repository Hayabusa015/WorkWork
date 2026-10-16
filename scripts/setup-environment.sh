#!/usr/bin/env bash
# SHULL OS build environment setup.
#
# Idempotent. Safe to re-run. Wired to SessionStart in .claude/settings.json so a
# fresh container comes up able to build and, more importantly, able to QA.
#
# Verified 2026-09-08: a stock container has NONE of this. soffice is installed
# but cannot load a file without the writer/impress filters, poppler is absent,
# and every Python and Node build library is missing. The QA gate's first step -
# render it and look at it - cannot run until this has.
set -uo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
log(){ printf '[shull-setup] %s\n' "$*"; }

# 1. Fonts ---------------------------------------------------------------------
log "installing Archivo / Archivo Narrow"
mkdir -p "$HOME/.fonts" "$HOME/.config/fontconfig/conf.d"
cp -f "$REPO"/brand/fonts/*.ttf "$HOME/.fonts/" 2>/dev/null
cp -f "$REPO"/brand/fonts/trade-gothic-next.conf "$HOME/.config/fontconfig/conf.d/50-shull.conf"
fc-cache -f >/dev/null 2>&1
if fc-match "Trade Gothic Next" 2>/dev/null | grep -qi archivo; then
  log "  Trade Gothic Next -> Archivo  OK"
else
  log "  WARNING: Trade Gothic Next does not resolve to Archivo. QA renders will be wrong."
fi

# 2. Document conversion and rasterisation -------------------------------------
if ! command -v pdffonts >/dev/null 2>&1 || ! ls /usr/lib/libreoffice/share/registry/writer.xcd >/dev/null 2>&1; then
  log "installing libreoffice filters + poppler (needed for the QA render)"
  apt-get update -qq >/dev/null 2>&1
  apt-get install -y --no-install-recommends \
    libreoffice-writer libreoffice-impress poppler-utils >/dev/null 2>&1 \
    && log "  apt OK" || log "  WARNING: apt failed. .docx/.pptx cannot be rendered for QA."
fi

# 3. Python build libraries ----------------------------------------------------
log "installing python build libraries"
python3 -m pip install --quiet --disable-pip-version-check \
  python-docx python-pptx pymupdf pillow weasyprint fonttools jsonschema \
  rdkit mendeleev pint 2>&1 \
  | grep -vi "warning: running pip" || true

# 4. Node libraries for the slide template ------------------------------------
# The twelve layouts are pptxgenjs slide masters. python-pptx can fill a layout but
# cannot define one, and "New slide -> Layout -> pick one" is the whole point of the
# template - so this dependency is load-bearing, not a preference.
SLIDE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/templates/slide"
if [ -d "$SLIDE_DIR" ] && ! ( cd "$SLIDE_DIR" && node -e "require('pptxgenjs')" ) >/dev/null 2>&1; then
  log "installing pptxgenjs for the slide template"
  ( cd "$SLIDE_DIR" && npm install pptxgenjs --no-audit --no-fund --silent >/dev/null 2>&1 ) \
    && log "  pptxgenjs OK" || log "  WARNING: npm failed. The slide template cannot be built."
fi

# 4b. Google Workspace CLI -----------------------------------------------------
# Uploads built .docx/.pptx/.pdf to Drive from disk. The Drive connector cannot: its
# create_file takes content inline, so a real deck is too big for it. The CLI needs
# credentials in GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE (an environment secret); without
# them it installs but cannot call the API. Drive scope only; see the Drive standard.
if ! command -v gws >/dev/null 2>&1; then
  log "installing Google Workspace CLI"
  npm install -g @googleworkspace/cli --no-audit --no-fund --silent >/dev/null 2>&1 \
    && log "  gws OK" || log "  WARNING: gws install failed. Drive uploads fall back to the manual route."
fi

# 4c. Google Workspace CLI credentials -----------------------------------------
# The environment secret GWS_CREDENTIALS_B64 holds `gws auth export --unmasked`, base64
# encoded so quotes and line breaks survive an environment-variable box. (GWS_CREDENTIALS_JSON,
# the raw text, is accepted too.) The CLI wants a file path, so write the secret to a
# private file and point GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE at it. Never printed or committed.
GWS_DIR="$HOME/.config/gws"
if [ -n "${GWS_CREDENTIALS_B64:-}" ] || [ -n "${GWS_CREDENTIALS_JSON:-}" ]; then
  mkdir -p "$GWS_DIR" && chmod 700 "$GWS_DIR"
  if [ -n "${GWS_CREDENTIALS_B64:-}" ]; then
    ( umask 077; printf '%s' "$GWS_CREDENTIALS_B64" | base64 -d > "$GWS_DIR/credentials.json" ) 2>/dev/null \
      || log "  WARNING: GWS_CREDENTIALS_B64 is not valid base64"
  else
    ( umask 077; printf '%s' "$GWS_CREDENTIALS_JSON" > "$GWS_DIR/credentials.json" )
  fi
  if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
    echo "export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=$GWS_DIR/credentials.json" >> "$CLAUDE_ENV_FILE"
  fi
  log "  gws credentials written (not shown)"
else
  log "  gws credentials not set (GWS_CREDENTIALS_B64); Drive uploads need them"
fi

# 4d. Session-start marker --------------------------------------------------------
# scripts/find_session_files.py reads this file's modification time as "when the session
# started". Written once, so a resume does not move it later and hide earlier documents.
[ -e "$HOME/.shull-session-start" ] || touch "$HOME/.shull-session-start"

# 5. Report --------------------------------------------------------------------
log "toolchain:"
python3 - <<'PY'
import importlib, shutil
for m in ["docx","pptx","fitz","PIL","weasyprint","fontTools","jsonschema"]:
    try: importlib.import_module(m); print(f"    {m:11} OK")
    except Exception: print(f"    {m:11} MISSING")
for b in ["soffice","pdffonts","pdftoppm","node","npm"]:
    print(f"    {b:11} {'OK' if shutil.which(b) else 'MISSING'}")
PY
( cd "$SLIDE_DIR" 2>/dev/null && node -e "require('pptxgenjs')" ) >/dev/null 2>&1 \
  && log "    pptxgenjs   OK" || log "    pptxgenjs   MISSING"
command -v gws >/dev/null 2>&1 && log "    gws         OK" || log "    gws         MISSING"
log "done"
