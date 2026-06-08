import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def broadcast_signal(pair, status, price):
    """
    Dispatches alerts to the destination Telegram channel.
    Handles structural variations for warning markers and direct actions.
    """
    if "PRE" in status:
        icon = "🟡"
        header = "⚠️ PRE-SIGNAL WARNING (WATCHING) ⚠️"
        strategy_note = "Prepare to open the pair trade window. Confirm asset trend direction."
    else:
        icon = "🟢" if "BUY" in status else "🔴"
        header = f"🚀 {status} EXECUTION ALERT 🚀"
        strategy_note = "Intersection matched on indicators. Momentum is highly verified."

    message = (
        f"{header}\n\n"
        f"✨ {icon} *Pair:* {pair}\n"
        f"✨ 📊 *Action:* {status}\n"
        f"✨ 💰 *Execution Price:* {price}\n\n"
        f"📈 *Timeframe:* 1M (Heikin Ashi Structure)\n"
        f"💡 *Strategy Context:* {strategy_note}\n"
        f"❌ *Risk Management:* NONE (Pure Katie Style Engine)"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=payload, timeout=10)
        if response.status_code != 200:
            print(f"[Telegram Error] API returned status code {response.status_code}: {response.text}")
        return response.status_code == 200
    except Exception as e:
        print(f"[Telegram Critical Error] Failed to reach API endpoints: {e}")
        return False
