[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=1
UseLongFileName=1
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=N
InstallPrompt=This will install SHULL OS on your computer.
DisplayLicense=0
FinishMessage=SHULL OS was installed and is ready to use.
TargetName=C:\Users\Shull\Documents\Codex\2026-09-10\ar\outputs\SHULL-OS-Setup-0.1.0.exe
FriendlyName=SHULL OS Setup
AppLaunched=powershell.exe -NoProfile -ExecutionPolicy Bypass -File install.ps1
PostInstallCmd=<None>
AdminQuietInstCmd=powershell.exe -NoProfile -ExecutionPolicy Bypass -File install.ps1
UserQuietInstCmd=powershell.exe -NoProfile -ExecutionPolicy Bypass -File install.ps1
SourceFiles=SourceFiles
[SourceFiles]
SourceFiles0=C:\Users\Shull\Documents\Codex\2026-09-10\ar\work\WorkWork-sync-20260911\installer
[SourceFiles0]
SHULL-OS-0.1.0-Windows.zip=C:\Users\Shull\Documents\Codex\2026-09-10\ar\work\WorkWork-sync-20260911\installer
install.ps1=C:\Users\Shull\Documents\Codex\2026-09-10\ar\work\WorkWork-sync-20260911\installer
