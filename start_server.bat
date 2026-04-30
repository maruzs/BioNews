@echo off
REM ============================================================
REM  BioNews - Script de inicio del servidor
REM  Levanta en paralelo:
REM    1. Backend FastAPI  (puerto 8000)
REM    2. Scheduler        (scrapers cada hora, 7am-7pm)
REM    3. Frontend Vite    (puerto 5173)
REM
REM  Acceso remoto via Tailscale:
REM    Web:    http://<IP-Tailscale>:5173
REM    API:    http://<IP-Tailscale>:8000
REM ============================================================

setlocal

REM Ruta al directorio del proyecto (ajustar si es necesario)
set PROJECT_DIR=%~dp0

REM Activar entorno virtual
call "%PROJECT_DIR%.venv\Scripts\activate.bat"

echo.
echo ============================================================
echo   BioNews - Iniciando servicios...
echo ============================================================
echo.

REM 1. Backend FastAPI (en nueva ventana)
echo [1/3] Iniciando Backend FastAPI en puerto 8000...
start "BioNews - Backend API" cmd /k "cd /d %PROJECT_DIR% && call .venv\Scripts\activate.bat && uvicorn server:app --host 0.0.0.0 --port 8000"

REM Esperar 3 segundos para que el backend arranque antes del scheduler
timeout /t 3 /nobreak >nul

REM 2. Scheduler de scrapers (en nueva ventana)
echo [2/3] Iniciando Scheduler de scrapers...
start "BioNews - Scheduler" cmd /k "cd /d %PROJECT_DIR% && call .venv\Scripts\activate.bat && python scheduler.py"

REM 3. Frontend Vite (en nueva ventana)
echo [3/3] Iniciando Frontend Vite en puerto 5173...
start "BioNews - Frontend" cmd /k "cd /d %PROJECT_DIR%web && npm run dev"

echo.
echo ============================================================
echo   Servicios iniciados correctamente.
echo.
echo   Frontend : http://localhost:5173
echo   API      : http://localhost:8000
echo   API Docs : http://localhost:8000/docs
echo.
echo   Para acceso remoto via Tailscale:
echo   Reemplaza "localhost" con la IP Tailscale del servidor.
echo ============================================================
echo.
pause
