Write-Host "Running D:\Dropbox\Projects\BEE\FixDate\install.ps1..." -ForegroundColor Yellow
if (Test-Path -Path $env:PROJECT_DIR\pyproject.toml) {pip install --no-cache-dir -e .[dev]}
pip install -e D:\Dropbox\Projects\BEE\displayfx
pip install -e D:\Dropbox\Projects\BEE\beetools
