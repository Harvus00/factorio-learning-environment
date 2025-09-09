
# Check if the .venv folder exists
if (Test-Path ".venv\Scripts\Activate.ps1") {
    Write-Host "Activating virtual environment..."
    .\.venv\Scripts\Activate.ps1
} else {
    Write-Host "Virtual environment not found. Please create it using 'python -m venv .venv'"
}
