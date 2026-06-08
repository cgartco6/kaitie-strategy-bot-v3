Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "🚀 INITIALIZING DEPENDENCIES AND RUNTIME (POWERSHELL)" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

# Prompt user configurations natively via shell variables
$TelegramToken = Read-Host -Prompt "Enter Telegram Bot Token"
$TelegramChatId = Read-Host -Prompt "Enter Telegram Chat ID"
$BotMode = Read-Host -Prompt "Enter Operation Mode (DEMO or REAL)"

# Inject string into process lifecycle memory scope
$env:TELEGRAM_TOKEN = $TelegramToken
$env:TELEGRAM_CHAT_ID = $TelegramChatId
$env:BOT_MODE = $BotMode

Write-Host "`nInstalling required Python standard processing modules..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host "`n==================================================" -ForegroundColor Green
Write-Host "🔥 RUNNING ENGINE PIPELINE CORE PROCESS" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
python main.py
