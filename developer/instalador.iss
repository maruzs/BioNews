[Setup]
AppName=BioNews
AppVersion=1.2.1
; --- AGREGAR ESTO ---
AppPublisher=Maruzs
AppCopyright=Copyright (C) 2026 Maruzs
; -------------------
DefaultDirName=C:\BioNews
DefaultGroupName=BioNews
OutputDir=dist\Installer
OutputBaseFilename=BioNews_Setup
SetupIconFile=assets\planet-earth.ico
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "dist\BioNews\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\BioNews"; Filename: "{app}\BioNews.exe"
Name: "{autodesktop}\BioNews"; Filename: "{app}\BioNews.exe"; Tasks: desktopicon; IconFilename: "{app}\assets\planet-earth.ico"

[Run]
Filename: "{app}\BioNews.exe"; Description: "{cm:LaunchProgram,BioNews}"; Flags: nowait postinstall skipifsilent