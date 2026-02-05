# Start the Design System Agent API (Production)

Write-Host "Starting Design System Agent API (Production Mode)..." -ForegroundColor Green
Write-Host "=====================================================" -ForegroundColor Green

# Check if .env file exists
if (-not (Test-Path .env)) {
    Write-Host "Error: .env file not found!" -ForegroundColor Red
    Write-Host "Please create .env file with your configuration" -ForegroundColor Red
    exit 1
}

# Set environment to production
$env:ENVIRONMENT = "production"

# Start the API server
Set-Location design_system_agent\api
Write-Host "`nStarting server in production mode..." -ForegroundColor Cyan
Write-Host "API will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host "`nPress Ctrl+C to stop the server`n" -ForegroundColor Yellow

uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
