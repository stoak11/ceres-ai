# Copy refreshed mart from reference repo (run on Stan's machine only)
$legacy = "C:\Users\stani\Documents\ml-farm-recolt-forecast"
$here = Split-Path $PSScriptRoot -Parent
$src = Join-Path $legacy "data\processed\modeling_mart.csv"
$dst = Join-Path $here "data\mart\modeling_mart.csv"
if (-not (Test-Path $src)) { Write-Error "Legacy mart not found: $src"; exit 1 }
Copy-Item $src $dst -Force
Write-Host "Copied -> $dst"
