import pandas as pd
import numpy as np

def calculate_indicators(df):
    """
    Applies mathematical calculation for SMA 4, EMA 50, EMA 200, 
    and Stochastic Oscillator (5, 1, 1) to match Katie's setup.
    """
    if len(df) < 200:
        return df

    # Calculations for Technical Moving Averages
    df['sma_4'] = df['close'].rolling(window=4).mean()
    df['ema_50'] = df['close'].ewm(span=50, adjust=False).mean()
    df['ema_200'] = df['close'].ewm(span=200, adjust=False).mean()

    # Stochastic Oscillator (5, 1, 1)
    # %K = ((Close - Low_5) / (High_5 - Low_5)) * 100
    low_5 = df['low'].rolling(window=5).min()
    high_5 = df['high'].rolling(window=5).max()
    
    # Avoid division by zero
    denom = high_5 - low_5
    df['stoch_k'] = np.where(denom == 0, 50.0, ((df['close'] - low_5) / denom) * 100)
    
    # Smoothing parameters match Katie's 1, 1 configuration (raw value is kept)
    df['stoch_d'] = df['stoch_k'].rolling(window=1).mean()
    
    return df

def check_katie_logic(df):
    """
    Evaluates specific entry rules from Katie's video instructions.
    - PRE-SIGNAL: White line (EMA 200) crosses/is near the candle, or trend direction matches
    - ACTUAL SIGNAL: SMA 4 and EMA 50 cross over matching momentum alignment
    """
    if df.empty or len(df) < 2:
        return "NEUTRAL", 0.0

    current = df.iloc[-1]
    previous = df.iloc[-2]

    price = current['close']
    ema200 = current['ema_200']
    sma4 = current['sma_4']
    ema50 = current['ema_50']
    stoch_k = current['stoch_k']

    prev_sma4 = previous['sma_4']
    prev_ema50 = previous['ema_50']

    # --- BUY / LONG MATRIX ---
    # Actual Confirmation Cross: Green line crosses above Red line while above White line
    if price > ema200 and prev_sma4 < prev_ema50 and sma4 >= ema50:
        if stoch_k > 70:  # Confirmed in stochastic uptrend zone
            return "BUY NOW", price
            
    # Pre-Signal Mitigation: Trend is bullish but lines are still converging before intersection
    if price > ema200 and sma4 < ema50:
        # Distance checks to ensure proximity threshold
        distance = (ema50 - sma4) / price
        if distance < 0.002:
            return "PRE-BUY (Setup Forming)", price

    # --- SELL / SHORT MATRIX ---
    # Actual Confirmation Cross: Green line crosses below Red line while below White line
    if price < ema200 and prev_sma4 > prev_ema50 and sma4 <= ema50:
        if stoch_k < 30:  # Confirmed in stochastic downtrend zone
            return "SELL NOW", price
            
    # Pre-Signal Mitigation: Trend is bearish but lines are still converging before intersection
    if price < ema200 and sma4 > ema50:
        distance = (sma4 - ema50) / price
        if distance < 0.002:
            return "PRE-SELL (Setup Forming)", price

    return "NEUTRAL", price
