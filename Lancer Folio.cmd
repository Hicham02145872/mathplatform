@echo off
cd /d "%~dp0"
if not exist node_modules\vite\bin\vite.js (
  echo Les dependances sont absentes. Executez npm install dans ce dossier.
  pause
  exit /b 1
)
if not exist dist\index.html (
  node node_modules\vite\bin\vite.js build
  if errorlevel 1 (
    pause
    exit /b 1
  )
)
node node_modules\vite\bin\vite.js preview --host 127.0.0.1 --port 5180 --open
pause
