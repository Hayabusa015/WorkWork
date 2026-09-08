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
  python-docx python-pptx pymupdf pillow weasyprint fonttools jsonschema 2>&1 \
  | grep -vi "warning: running pip" || true

# 4. Report --------------------------------------------------------------------
log "toolchain:"
python3 - <<'PY'
import importlib, shutil
for m in ["docx","pptx","fitz","PIL","weasyprint","fontTools","jsonschema"]:
    try: importlib.import_module(m); print(f"    {m:11} OK")
    except Exception: print(f"    {m:11} MISSING")
for b in ["soffice","pdffonts","pdftoppm"]:
    print(f"    {b:11} {'OK' if shutil.which(b) else 'MISSING'}")
PY
log "done"
