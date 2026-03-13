@echo off
setlocal enabledelayedexpansion

echo ============================================================
echo   🌌 MASTER CV EXPORT SYSTEM: Global Career Launch 🌌
echo ============================================================
echo.
echo Preparing to generate 16 Master CV PDFs...
echo.

REM Check if node is installed
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Node.js is not installed!
    echo Please install Node.js from https://nodejs.org/ to use this tool.
    pause
    exit /b
)

echo [1/2] Installing/Running PDF Engine (md-to-pdf)...
echo This may take a few moments for the first run...
echo.

REM Run the batch conversion
npx -y md-to-pdf "Master-CVs/01-Web3-Solana/*.md"
npx -y md-to-pdf "Master-CVs/02-Eth-Base/*.md"
npx -y md-to-pdf "Master-CVs/03-Mobile-Flutter/*.md"
npx -y md-to-pdf "Master-CVs/04-AI-Automation/*.md"
npx -y md-to-pdf "Master-CVs/05-GameFi-Degen/*.md"
npx -y md-to-pdf "Master-CVs/06-Community-Growth/*.md"
npx -y md-to-pdf "Master-CVs/07-Web3-Strategy/*.md"
npx -y md-to-pdf "Master-CVs/08-Fintech-Payments/*.md"

echo.
echo [2/2] PDFs generated successfully in their respective folders!
echo.
echo ============================================================
echo   ✅ SUCCESS: Your 16 Master CVs are ready for use!
echo ============================================================
echo.
pause
