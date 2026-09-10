# Setup script for Windows (PowerShell)
# Usage: .\setup.ps1

Write-Host "Creating Python virtual environment (.venv)..."
python -m venv .venv

Write-Host "Activating virtual environment..."
& ".\.venv\Scripts\Activate.ps1"

Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

Write-Host "Installing dependencies..."
pip install -r requirements.txt

Write-Host ""
Write-Host "=========================================="
Write-Host "Setup complete!"
Write-Host "=========================================="
Write-Host ""
Write-Host "To activate the virtual environment, run:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host ""
Write-Host "To set your OpenAI API key:"
Write-Host "  `$env:OPENAI_API_KEY='sk-...'"
Write-Host ""
Write-Host "To run the experiment:"
Write-Host "  python main.py"
Write-Host ""
