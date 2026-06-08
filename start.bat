@echo off
TITLE Katie Strategy Signal Bot Launcher
echo ==================================================
echo 🚀 INITIALIZING DEPENDENCIES AND RUNTIME
echo ==================================================

:: Prompt user for Configuration Variables
set /p TOKEN="Enter Telegram Bot Token: "
set /p CHAT_ID="Enter Telegram Chat ID: "
set /p MODE="Enter Operation Mode (DEMO or REAL): "

:: Export environmental strings
set TELEGRAM_TOKEN=%TOKEN%
set TELEGRAM_CHAT_ID=%CHAT_ID%
set BOT_MODE=%MODE%

echo.
echo Installing internal dependencies from requirements manifests...
pip install -r requirements.txt

echo.
echo ==================================================
echo 🔥 STARTING CORE LOCAL MONITORING ENGINE
echo ==================================================
python main.py
pause
