# Start the Design System Agent API (Development)

Write-Host "Starting Design System Agent API..." -ForegroundColor Green
Write-Host "====================================" -ForegroundColor Green

# Check if .env file exists
if (-not (Test-Path .env)) {
    Write-Host "Warning: .env file not found. Copying from .env.example" -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host "Please update .env with your API keys" -ForegroundColor Yellow
}

# Start the API server
Set-Location design_system_agent\api
Write-Host "`nStarting server with hot reload..." -ForegroundColor Cyan
Write-Host "API will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host "API docs available at: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host "`nPress Ctrl+C to stop the server`n" -ForegroundColor Yellow

uvicorn main:app --reload --host 0.0.0.0 --port 8000
