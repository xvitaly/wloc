@echo off

rem SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
rem
rem SPDX-License-Identifier: GPL-3.0-or-later

title Building release binaries for Windows...

set RELVER=101
set GPGKEY=A989AAAA
set PYTHONOPTIMIZE=1

if [%CI_HASH%] == [] (
    set PREFIX=wloc_%RELVER%
) else (
    set PREFIX=snapshot_%CI_HASH%
)

echo Removing previous build results...
if exist results rd /S /Q results

echo Starting build process using PyInstaller...
pyinstaller ^
    --log-level=INFO ^
    --distpath=results\dist ^
    --workpath=results\build ^
    --clean ^
    --noconfirm ^
    --onefile ^
    --noupx ^
    --name=wloc ^
    --version-file=assets\version.txt ^
    --manifest=assets\wloc.manifest ^
    --icon=assets\wloc.ico ^
    ..\..\src\wloc\app\run.py

echo Signing binaries...
if [%CI_HASH%] == [] (
    "%ProgramFiles(x86)%\GnuPG\bin\gpg.exe" --sign --detach-sign --default-key %GPGKEY% results\dist\wloc.exe
)

echo Compiling Installer...
"%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe" inno\wloc.iss

echo Signing built artifacts...
if [%CI_HASH%] == [] (
    "%ProgramFiles(x86)%\GnuPG\bin\gpg.exe" --sign --detach-sign --default-key %GPGKEY% results\%PREFIX%_setup.exe
)

echo Removing temporary files and directories...
del wloc.spec
rd /S /Q "%LOCALAPPDATA%\pyinstaller"
rd /S /Q "results\build"
rd /S /Q "results\dist"
