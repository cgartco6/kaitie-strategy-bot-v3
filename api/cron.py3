from flask import Flask, jsonify, render_template_string
import os
import sys
from config import BOT_MODE

# Ensure parent path resolution works seamlessly in Serverless deployments
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.engine import process_market_analysis

app = Flask(__name__)

# Fallback string delivery configuration mapping for seamless file injection within serverless architectures
with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates', 'dashboard.html'), 'r') as html_file:
    HTML_TEMPLATE = html_file.read()

@app.route('/', methods=['GET'])
def index_dashboard():
    """Renders visual web UI template directly to browsing clients."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/cron', methods=['GET', 'POST'])
def run_cron():
    """
    Trigger endpoint intended for execution via Vercel Cron Schedules or UI refresh ticks.
    Keeps the bot operating completely serverless.
    """
    try:
        report_data = process_market_analysis()
        return jsonify({
            "status": "success", 
            "bot_mode": BOT_MODE,
            "results": report_data
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
