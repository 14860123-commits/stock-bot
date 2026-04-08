import requests
import random
import os

stocks = ["2330.TW", "2317.TW", "2454.TW"]

stock_id = random.choice(stocks)

url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={stock_id}"

res = requests.get(url)
data = res.json()

result = data["quoteResponse"]["result"]

if result:
    price = result[0]["regularMarketPrice"]
    name = result[0]["shortName"]

    message = f"{name} ({stock_id})\n現價: {price}"
else:
    message = "抓不到資料"

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(send_url, data={
    "chat_id": CHAT_ID,
    "text": message
})
