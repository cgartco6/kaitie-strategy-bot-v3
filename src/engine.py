import time
import random
import pandas as pd
import ccxt
from config import BOT_MODE, MAJOR_PAIRS
from src.indicators import calculate_indicators, check_katie_logic
from src.telegram_bot import broadcast_signal

def generate_mock_ohlcv(length=210):
    """Generates mock data sequence mimicking 1-minute historical candlestick rows"""
    current_time = int(time.time() * 1000) - (length * 60 * 1000)
    data = []
    base_price = 1.0850
    
    for i in range(length):
        base_price += random.uniform(-0.0005, 0.0006)
        high = base_price + random.uniform(0.0001, 0.0003)
        low = base_price - random.uniform(0.0001, 0.0003)
        close = base_price + random.uniform(-0.0001, 0.0001)
        
        data.append([current_time, base_price, high, low, close, random.uniform(10, 100)])
        current_time += 60 * 1000
    return data

def process_market_analysis():
    """
    Core runner engine that orchestrates data calculation.
    Returns metrics tracking dictionary structures directly back to the caller UI.
    """
    print(f"🤖 Processing cycle initiated in Mode: {BOT_MODE}")
    ui_report_payload = {}
    
    exchange = None
    if BOT_MODE == "REAL":
        exchange = ccxt.binance({'enableRateLimit': True})

    for pair in MAJOR_PAIRS:
        try:
            if BOT_MODE == "REAL":
                ohlcv = exchange.fetch_ohlcv(pair, timeframe='1m', limit=210)
            else:
                ohlcv = generate_mock_ohlcv()

            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df = calculate_indicators(df)
            status, final_price = check_katie_logic(df)
            
            # Extract final metrics state to dump upstream to HTML Dashboard
            latest = df.iloc[-1]
            ui_report_payload[pair] = {
                "status": status,
                "price": final_price,
                "indicators": {
                    "sma_4": float(latest['sma_4']),
                    "ema_50": float(latest['ema_50']),
                    "ema_200": float(latest['ema_200']),
                    "stoch_k": float(latest['stoch_k'])
                }
            }
            
            if status != "NEUTRAL":
                broadcast_signal(pair, status, final_price)
                
        except Exception as e:
            print(f"❌ Error compiling calculations for {pair}: {e}")
            ui_report_payload[pair] = {"status": "ERROR/OFFLINE", "price": 0.0, "indicators": {"sma_4":0,"ema_50":0,"ema_200":0,"stoch_k":0}}
            
    return ui_report_payload
