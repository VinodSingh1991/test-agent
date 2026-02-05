# Test Dataset Generation

Write-Host "Testing Summary Dataset Generation..." -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan

# Test if API is running
Write-Host "`nChecking if API is running..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/health" -Method Get -UseBasicParsing
    Write-Host "✓ API is running" -ForegroundColor Green
} catch {
    Write-Host "✗ API is not running. Please start the API first:" -ForegroundColor Red
    Write-Host "  cd design_system_agent\api" -ForegroundColor Yellow
    Write-Host "  python main.py" -ForegroundColor Yellow
    exit 1
}

# Test dataset generation endpoint
Write-Host "`nGenerating summary dataset via API..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/api/v1/generate_dataset" -Method Get -UseBasicParsing
    $result = $response.Content | ConvertFrom-Json
    
    if ($result.status -eq "success") {
        Write-Host "✓ Dataset generated successfully!" -ForegroundColor Green
        Write-Host "  Message: $($result.message)" -ForegroundColor Cyan
    } else {
        Write-Host "✗ Dataset generation failed" -ForegroundColor Red
        Write-Host "  Message: $($result.message)" -ForegroundColor Yellow
    }
} catch {
    Write-Host "✗ Error calling dataset generation endpoint" -ForegroundColor Red
    Write-Host "  Error: $($_.Exception.Message)" -ForegroundColor Yellow
}

# Check if dataset file exists
Write-Host "`nChecking dataset file..." -ForegroundColor Yellow
$datasetPath = "design_system_agent\dataset\summary_queries.jsonl"
if (Test-Path $datasetPath) {
    Write-Host "✓ Dataset file exists: $datasetPath" -ForegroundColor Green
    
    # Count lines
    $lineCount = (Get-Content $datasetPath | Measure-Object -Line).Lines
    Write-Host "  Lines: $lineCount" -ForegroundColor Cyan
    
    # Show first example
    Write-Host "`nFirst example (truncated):" -ForegroundColor Yellow
    $firstLine = Get-Content $datasetPath -First 1
    $example = $firstLine | ConvertFrom-Json
    Write-Host "  Query: $($example.query)" -ForegroundColor Cyan
    Write-Host "  Tabs: $($example.layout.Tabs.Count)" -ForegroundColor Cyan
} else {
    Write-Host "✗ Dataset file not found: $datasetPath" -ForegroundColor Red
}

Write-Host "`nTest complete!" -ForegroundColor Green
