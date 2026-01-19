@echo off
echo ========================================
echo  Agentic AI System
echo  National-Scale Decision Making
echo ========================================
echo.

REM Check if .env exists
if not exist .env (
    echo ERROR: .env file not found!
    echo.
    echo Please create .env file first:
    echo   1. Copy .env.example to .env
    echo   2. Add your API key
    echo.
    echo For FREE setup, see FREE_SETUP.md
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies if needed
echo Checking dependencies...
pip install -q -r requirements.txt

REM Run the application
echo.
echo Starting Agentic AI System...
echo.
python main.py

pause
