$ErrorActionPreference = 'Stop'

$payload = Join-Path $PSScriptRoot 'SHULL-OS-0.1.0-Windows.zip'
$installRoot = Join-Path $env:LOCALAPPDATA 'Programs\SHULL OS'
$tempExtract = Join-Path $env:TEMP ('shull-os-install-' + [guid]::NewGuid().ToString('N'))

New-Item -ItemType Directory -Force -Path $tempExtract | Out-Null
try {
  Expand-Archive -LiteralPath $payload -DestinationPath $tempExtract -Force
  New-Item -ItemType Directory -Force -Path (Split-Path $installRoot) | Out-Null
  if (Test-Path -LiteralPath $installRoot) {
    Remove-Item -LiteralPath $installRoot -Recurse -Force
  }
  Move-Item -LiteralPath $tempExtract -Destination $installRoot
  $exe = Join-Path $installRoot 'SHULL OS.exe'
  if (-not (Test-Path -LiteralPath $exe)) { throw 'SHULL OS.exe was not found in the extracted package.' }

  $shell = New-Object -ComObject WScript.Shell
  $startMenu = Join-Path $env:APPDATA 'Microsoft\Windows\Start Menu\Programs\SHULL OS.lnk'
  $desktop = Join-Path ([Environment]::GetFolderPath('Desktop')) 'SHULL OS.lnk'
  foreach ($linkPath in @($startMenu, $desktop)) {
    $link = $shell.CreateShortcut($linkPath)
    $link.TargetPath = $exe
    $link.WorkingDirectory = $installRoot
    $link.Description = 'SHULL OS teaching workspace'
    $link.Save()
  }
  Start-Process -FilePath $exe -WorkingDirectory $installRoot
}
finally {
  if (Test-Path -LiteralPath $tempExtract) { Remove-Item -LiteralPath $tempExtract -Recurse -Force -ErrorAction SilentlyContinue }
}
