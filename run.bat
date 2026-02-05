@echo off
REM Design System Agent - Quick Start Script
echo ========================================
echo  Design System Agent - Starting Server
echo ========================================
echo.

REM Activate virtual environment
echo [1/3] Activating virtual environment...
call .venv\Scripts\activate.bat

REM Check if required packages are installed
echo [2/3] Checking dependencies...
pip show uvicorn >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
)

REM Start the server
echo [3/3] Starting uvicorn server...
echo.
echo Server will be available at: http://127.0.0.1:8000
echo API Documentation: http://127.0.0.1:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

E:\design-system-agent\.venv\Scripts\python.exe -m uvicorn design_system_agent.api.main:app --reload --host 0.0.0.0 --port 8000

pause
