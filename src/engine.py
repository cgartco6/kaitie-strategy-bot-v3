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
    Core runner engine that orchestrates the data retrieval, 
    indicator processing mathematical evaluation, and alert dispatches.
    """
    print(f"🤖 Processing cycle initiated in Mode: {BOT_MODE}")
    
    exchange = None
    if BOT_MODE == "REAL":
        # Connects via standard multi-exchange protocol layer
        exchange = ccxt.binance({'enableRateLimit': True})

    for pair in MAJOR_PAIRS:
        try:
            if BOT_MODE == "REAL":
                print(f"📡 Fetching live data for {pair} from Exchange API...")
                # Fetching 1-minute historical data bars
                ohlcv = exchange.fetch_ohlcv(pair, timeframe='1m', limit=210)
            else:
                ohlcv = generate_mock_ohlcv()

            # Map raw array responses into pandas processing dataframes
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            
            # Apply mathematical calculations for indicators
            df = calculate_indicators(df)
            
            # Extract decision status metrics
            status, final_price = check_katie_logic(df)
            
            print(f"➔ Asset: {pair} | Status Result: {status} | Latency Price: {final_price}")
            
            if status != "NEUTRAL":
                broadcast_signal(pair, status, final_price)
                
        except Exception as e:
            print(f"❌ Error compiling calculations for {pair}: {e}")
