# Design System Agent - Quick Start Script (PowerShell)
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Design System Agent - Starting Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment
Write-Host "[1/3] Activating virtual environment..." -ForegroundColor Yellow
& ".\.venv\Scripts\Activate.ps1"

# Check if required packages are installed
Write-Host "[2/3] Checking dependencies..." -ForegroundColor Yellow
$uvicornInstalled = & pip show uvicorn 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Installing required packages..." -ForegroundColor Yellow
    & pip install -r requirements.txt
}

# Start the server
Write-Host "[3/3] Starting uvicorn server..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Server will be available at: " -NoNewline -ForegroundColor Green
Write-Host "http://127.0.0.1:8000" -ForegroundColor White
Write-Host "API Documentation: " -NoNewline -ForegroundColor Green
Write-Host "http://127.0.0.1:8000/docs" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Cyan
Write-Host ""

& E:\design-system-agent\.venv\Scripts\python.exe -m uvicorn design_system_agent.api.main:app --reload --host 0.0.0.0 --port 8000
