; SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
;
; SPDX-License-Identifier: GPL-3.0-or-later

#define VERSION GetVersionNumbersString("..\results\dist\wloc.exe")
#define BASEDIR "..\results\dist"

#if GetEnv('CI_HASH') == ''
#define _RELEASE 1
#endif

[Setup]
AppId={{D9243A3E-8574-4475-9460-66F544B4D07B}
AppName=Wi-Fi geolocation tool
AppVerName=Wi-Fi geolocation tool
AppPublisher=EasyCoding Team
AppPublisherURL=https://www.easycoding.org/
AppVersion={#VERSION}
AppSupportURL=https://github.com/xvitaly/wloc/issues
AppUpdatesURL=https://github.com/xvitaly/wloc/releases
DefaultDirName={localappdata}\wloc
DefaultGroupName=Wi-Fi geolocation tool
AllowNoIcons=yes
LicenseFile=..\..\..\LICENSE
OutputDir=..\results
OutputBaseFilename={#GetEnv('PREFIX')}_setup
SetupIconFile=..\assets\wloc.ico
UninstallDisplayIcon={app}\wloc.exe
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=commandline
ShowLanguageDialog=auto
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
MinVersion=6.1sp1
ChangesEnvironment=yes
VersionInfoVersion={#VERSION}
VersionInfoDescription=Wi-Fi geolocation tool
VersionInfoCopyright=(c) 2015-2022 EasyCoding Team. All rights reserved.
VersionInfoCompany=EasyCoding Team

[Messages]
BeveledLabel=EasyCoding Team

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl,locale\en\cm.isl"; InfoBeforeFile: "locale\en\readme.txt"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl,locale\ru\cm.isl"; InfoBeforeFile: "locale\ru\readme.txt"

[Types]
Name: system; Description: "{cm:TypeSystemDescription}"
Name: standard; Description: "{cm:TypeStandardDescription}"
Name: nokeys; Description: "{cm:TypeNoKeysDescription}"

[Components]
Name: "core"; Description: "{cm:ComponentCoreDescription}"; Types: standard system nokeys; Flags: fixed
Name: "apikey"; Description: "{cm:ComponentAPIKeySubDescription}"; Types: standard system nokeys; Flags: exclusive
Name: "apikey\sysenv"; Description: "{cm:ComponentAPIKeySysEnvDescription}"; Types: system; Flags: exclusive
Name: "apikey\launcher"; Description: "{cm:ComponentAPIKeyLauncherDescription}"; Types: standard; Flags: exclusive
Name: "apikey\nokeys"; Description: "{cm:ComponentAPIKeyNoKeyDescription}"; Types: nokeys; Flags: exclusive

[Tasks]
Name: "addtopath"; Description: "{cm:TaskAddToPath}"; GroupDescription: "{cm:TaskCategoryAddToPath}"; Components: core

[Files]
Source: "{#BASEDIR}\wloc.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: core
Source: "{tmp}\wlocc.cmd"; DestDir: "{app}"; Flags: external; Components: apikey\launcher

#ifdef _RELEASE
Source: "{#BASEDIR}\wloc.exe.sig"; DestDir: "{app}"; Flags: ignoreversion; Components: core
#endif

[Registry]
Root: HKCU; Subkey: "Environment"; ValueType: string; ValueName: "APIKEY_GOOGLE"; ValueData: "{code:GetAPITokenGoogle}"; Flags: uninsdeletevalue; Components: "apikey\sysenv"
Root: HKCU; Subkey: "Environment"; ValueType: string; ValueName: "APIKEY_MOZILLA"; ValueData: "{code:GetAPITokenMozilla}"; Flags: uninsdeletevalue; Components: "apikey\sysenv"
Root: HKCU; Subkey: "Environment"; ValueType: string; ValueName: "APIKEY_YANDEX"; ValueData: "{code:GetAPITokenYandex}"; Flags: uninsdeletevalue; Components: "apikey\sysenv"
Root: HKCU; Subkey: "Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{code:PathNewEntry|{app}}"; Tasks: addtopath; Check: PathIsClean(ExpandConstant('{app}'))

[Code]
var
    APIKeyPage: TInputQueryWizardPage;

procedure AddAPIKeyPage();
begin
    APIKeyPage := CreateInputQueryPage(wpSelectTasks, CustomMessage('APIKeyPageCaption'), CustomMessage('APIKeyPageDescription'), CustomMessage('APIKeyPageAdditionalText'));
    APIKeyPage.Add(CustomMessage('APIKeyPageInputFieldGoogleToken'), False)
    APIKeyPage.Add(CustomMessage('APIKeyPageInputFieldMozillaToken'), False)
    APIKeyPage.Add(CustomMessage('APIKeyPageInputFieldYandexToken'), False)
end;

procedure InitializeWizard();
begin
    AddAPIKeyPage()
end;

function GetAPITokenGoogleInternal(): String;
begin
    Result := APIKeyPage.Values[0]
end;

function GetAPITokenGoogle(Value: String): String;
begin
    Result := GetAPITokenGoogleInternal()
end;

function GetAPITokenMozillaInternal(): String;
begin
    Result := APIKeyPage.Values[1]
end;

function GetAPITokenMozilla(Value: String): String;
begin
    Result := GetAPITokenMozillaInternal()
end;

function GetAPITokenYandexInternal(): String;
begin
    Result := APIKeyPage.Values[2]
end;

function GetAPITokenYandex(Value: String): String;
begin
    Result := GetAPITokenYandexInternal()
end;

function VerifyAPICredentials(): Boolean;
begin
    Result := (Length(GetAPITokenGoogleInternal()) < 10) and (Length(GetAPITokenMozillaInternal()) < 4) and (Length(GetAPITokenYandexInternal()) < 10)
end;

function IsKeylessInstallation(): Boolean;
begin
    Result := WizardIsComponentSelected('apikey\nokeys')
end;

function GenerateLauncher(FileName: String): Boolean;
var
    Contents: TArrayOfString;
begin
    SetArrayLength(Contents, 8);
    Contents[0] := '@echo off';
    Contents[1] := '';
    Contents[2] := 'title Wi-Fi geolocation tool';
    Contents[3] := 'set APIKEY_GOOGLE=' + GetAPITokenGoogleInternal();
    Contents[4] := 'set APIKEY_MOZILLA=' + GetAPITokenMozillaInternal();
    Contents[5] := 'set APIKEY_YANDEX=' + GetAPITokenYandexInternal();
    Contents[6] := '';
    Contents[7] := '.\wloc.exe %*';
    Result := SaveStringsToFile(FileName, Contents, False)
end;

function PathIsClean(InstallPath: String): Boolean;
var
    CurrentPath: String;
begin
    if RegQueryStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', CurrentPath) then
        begin
            Result := Pos(InstallPath, CurrentPath) = 0
        end
    else
        begin
            Result := True
        end
end;

function PathNewEntry(InstallPath: String): String;
var
    CurrentPath: String;
begin
    if not RegQueryStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', CurrentPath) then
        begin
            CurrentPath := ''
        end;
    if Length(CurrentPath) > 0 then
        begin
            if CompareStr(Copy(CurrentPath, Length(CurrentPath), 1), ';') = 0 then
                begin
                    Result := CurrentPath + InstallPath + ';'
                end
            else
                begin
                    Result := CurrentPath + ';' + InstallPath + ';'
                end
        end
    else
        begin
            Result := InstallPath + ';'
        end
end;

procedure PathRemoveEntry(InstallPath: String);
var
    CurrentPath: String;
    Position: Integer;
    LI, RI: Integer;
begin
    if RegQueryStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', CurrentPath) then
        begin
            Position := Pos(InstallPath, CurrentPath);
            if Position > 0 then
                begin
                    if CompareStr(Copy(CurrentPath, Position, 1), ';') = 0 then LI := 1 else LI := 0;
                    if (CompareStr(Copy(CurrentPath, Length(CurrentPath), 1), ';') = 0) and (LI = 1) then RI := 0 else RI := 1;
                    Delete(CurrentPath, Position - LI, Length(CurrentPath) + RI);
                    RegWriteStringValue(HKEY_CURRENT_USER, 'Environment', 'Path', CurrentPath)
                end
        end
end;

function ShouldSkipPage(CurPageID: Integer): Boolean;
begin
    if CurPageID = APIKeyPage.ID then
        begin
            Result := IsKeylessInstallation()
        end
    else
        begin
            Result := False
        end
end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
    if CurPageID = APIKeyPage.ID then
        begin
            if (VerifyAPICredentials()) then
                begin
                    MsgBox(CustomMessage('APIKeyPageErrorMessage'), mbError, MB_OK);
                    Result := False
                end
            else
                begin
                    Result := GenerateLauncher(ExpandConstant('{tmp}\wlocc.cmd'));
                end
        end
    else
        begin
            Result := True
        end
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
    if CurUninstallStep = usPostUninstall then
        begin
            PathRemoveEntry(ExpandConstant('{app}'))
        end
end;
