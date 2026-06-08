from flask import Flask, jsonify, render_template_string
import os
import sys

# Ensure parent path resolution works seamlessly
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from config import BOT_MODE
from src.engine import process_market_analysis

app = Flask(__name__)

TEMPLATE_PATH = os.path.join(base_dir, 'templates', 'dashboard.html')

def get_html_template():
    try:
        with open(TEMPLATE_PATH, 'r', encoding='utf-8') as html_file:
            return html_file.read()
    except Exception as e:
        return f"<h3>UI Dashboard Template Load Error</h3><p>{str(e)}</p>"

@app.route('/', methods=['GET'])
def index_dashboard():
    return render_template_string(get_html_template())

@app.route('/api/cron', methods=['GET', 'POST'])
def run_cron():
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
