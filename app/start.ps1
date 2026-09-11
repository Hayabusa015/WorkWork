$env:SHULL_PYTHON=Join-Path $PSScriptRoot 'data/venv/Scripts/python.exe'
if (-not (Test-Path $env:SHULL_PYTHON)) { throw 'Create the Python virtual environment described in README.md first.' }
$renderer=Join-Path $PSScriptRoot '../../work/tools/renderer/SourceDir/LibreOffice/program/soffice.exe'
if (Test-Path $renderer) { $env:SHULL_SOFFICE=$renderer }
node (Join-Path $PSScriptRoot 'server.mjs')
