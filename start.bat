@echo off
setlocal enabledelayedexpansion

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Downloading and installing Python 3.12...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe' -OutFile 'python-installer.exe'"
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
    echo Python installed successfully. Please restart this script or your command prompt for changes to take effect.
    pause
    exit
) else (
    echo Python is already installed.
)

python -c "import win32api" >nul 2>&1
if %errorlevel% neq 0 (
    echo pywin32 not found. Installing pywin32...
    python -m pip install pywin32
    echo pywin32 installed successfully.
) else (
    echo pywin32 is already installed.
)

python lockcursor.py

echo.
echo The script has finished running.
echo To use it again:
echo 1. Launch Minecraft Bedrock and enter a world.
echo 2. Run this start.bat file again.
echo Controls:
echo - Alt+1: Pause/resume cursor lock.
echo - Alt+2: Stop the script.
echo - Ctrl+C: Emergency stop in the console.
pause