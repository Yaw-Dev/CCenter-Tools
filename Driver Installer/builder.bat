@echo off

pip install requests
cls

echo.
pyinstaller --noconfirm --onefile --uac-admin --icon NONE --hidden-import "requests" --hidden-import "os" --hidden-import "zipfile" --hidden-import "subprocess" --hidden-import "shutil" -n "CCFix" main.py
rmdir /s /q __pycache__
rmdir /s /q build
del /f / s /q CCFix.spec
echo.
echo Generated executable as CCFix.exe in the dist folder.
echo.
pause
EXIT /B 1