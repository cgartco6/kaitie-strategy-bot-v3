import os

# Telegram Configuration
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_BOT_TOKEN_HERE")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

# Katie's Core Indicator Parameters (From her Pocket Option video)
SMA_PERIOD = 4      # Green Line
EMA_MEDIUM = 50     # Red Line
EMA_LONG = 200      # White Line (Trend Filter)
STOCH_K = 5
STOCH_D = 1
STOCH_S = 1

# Assets to Monitor (Major Forex Pairs and Crypto Equivalents for continuous feed)
MAJOR_PAIRS = ["EUR/USDT", "GBP/USDT", "BTC/USDT", "ETH/USDT"]

# Mode Selection: "REAL" to fetch live CCXT exchange data, "DEMO" to use mock data loop
BOT_MODE = os.getenv("BOT_MODE", "DEMO")
