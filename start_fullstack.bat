@echo off
echo ========================================
echo  Agentic AI System - Full Stack
echo ========================================
echo.
echo Starting Backend API Server...
echo.

start cmd /k "cd /d "%~dp0" && .venv\Scripts\activate && python api_server.py"

timeout /t 3 /nobreak > nul

echo Starting Frontend Development Server...
echo.

start cmd /k "cd /d "%~dp0frontend" && npm run dev"

echo.
echo ========================================
echo  Both servers are starting!
echo ========================================
echo.
echo Backend API: http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo Frontend: http://localhost:3000
echo.
echo Press any key to open frontend in browser...
pause > nul

start http://localhost:3000
