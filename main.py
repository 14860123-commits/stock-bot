import requests
import random
import os

stocks = ["2330.TW", "2317.TW", "2454.TW"]

stock_id = random.choice(stocks)

try:
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={stock_id}"
    res = requests.get(url)
    data = res.json()

    result = data["quoteResponse"]["result"]

    if result:
        price = result[0]["regularMarketPrice"]
        name = result[0]["shortName"]
        message = f"{name} ({stock_id})\n現價: {price}"
    else:
        message = "抓不到股價資料"

except Exception as e:
    message = f"錯誤: {str(e)}"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if BOT_TOKEN and CHAT_ID:
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": message}
    )
else:
    print("缺少 BOT_TOKEN 或 CHAT_ID")
