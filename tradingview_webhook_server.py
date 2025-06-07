from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8116695588:AAGFuoRFWgeZzLX6b9V8cuqstlOTHF3xIY0"
CHAT_ID = "6210637507"
TELEGRAM_URL = f"https://api.telegram.org/bot{{TELEGRAM_TOKEN}}/sendMessage"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", "⚠️ Новий сигнал з TradingView (але без тексту)")

    payload = {
        "chat_id": CHAT_ID,
        "text": f"📡 TradingView Сигнал:\\n{{message}}"
    }
    r = requests.post(TELEGRAM_URL, json=payload)
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
