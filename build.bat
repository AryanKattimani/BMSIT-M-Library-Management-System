@echo off
setlocal
python -m pip install -r requirements.txt
python -m PyInstaller --clean --noconfirm BMSIT-Library.spec
python -m PyInstaller --clean --noconfirm BMSIT-Library-Server.spec
if errorlevel 1 exit /b 1
echo.
echo Builds are in dist\
pause
