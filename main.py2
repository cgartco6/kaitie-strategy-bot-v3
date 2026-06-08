import time
from src.engine import process_market_analysis

def main():
    print("==================================================")
    print("🚀 KATIE STRATEGY DISPATCH ENGINE RUNNING LIVE 🚀")
    print("==================================================")
    
    # Running operational polling loop indefinitely
    while True:
        try:
            process_market_analysis()
        except Exception as e:
            print(f"🔥 Critical Execution Error in Polling Loop: {e}")
            
        # Tick cycle frequency matches 1-minute candlestick bounds
        print("💤 Polling cycle finished. Sleeping for 60 seconds...")
        time.sleep(60)

if __name__ == "__main__":
    main()
