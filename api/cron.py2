from flask import Flask, jsonify
import os
import sys

# Ensure parent path resolution works seamlessly in Serverless deployments
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.engine import process_market_analysis

app = Flask(__name__)

@app.route('/api/cron', methods=['GET', 'POST'])
def run_cron():
    """
    Trigger endpoint intended for execution via Vercel Cron Schedules.
    Keeps the bot operating completely serverless.
    """
    try:
        process_market_analysis()
        return jsonify({"status": "success", "message": "Katie algorithm processed metrics successfully."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
