import os
import time
from api.cron import app  # <--- Exposes the top-level "app" Vercel wants!
from src.engine import process_market_analysis

def run_local_loop():
    print("==================================================")
    print("🚀 KATIE STRATEGY DISPATCH ENGINE RUNNING LOCAL LOOP 🚀")
    print("==================================================")
    while True:
        try:
            process_market_analysis()
        except Exception as e:
            print(f"🔥 Critical Execution Error in Polling Loop: {e}")
            
        print("💤 Polling cycle finished. Sleeping for 60 seconds...")
        time.sleep(60)

# If run via start.bat/start.ps1 locally, it triggers the background engine loop.
# If loaded by Vercel, it ignores this block and runs the 'app' instance imported above.
if __name__ == "__main__":
    run_local_loop()
