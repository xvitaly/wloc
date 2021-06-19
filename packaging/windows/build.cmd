@echo off

rem SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
rem
rem SPDX-License-Identifier: GPL-3.0-or-later

title Building release binaries for Windows...

set RELVER=070
set GPGKEY=A989AAAA
set PYTHONOPTIMIZE=1

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
    ..\..\wloc\app\run.py

echo Signing binaries...
"%ProgramFiles(x86)%\GnuPG\bin\gpg.exe" --sign --detach-sign --default-key %GPGKEY% results\dist\wloc.exe

echo Compiling Installer...
"%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe" inno\wloc.iss

echo Signing built artifacts...
"%ProgramFiles(x86)%\GnuPG\bin\gpg.exe" --sign --detach-sign --default-key %GPGKEY% results\wloc_%RELVER%.exe

echo Removing temporary files and directories...
del wloc.spec
rd /S /Q "results\build"
rd /S /Q "results\dist"
