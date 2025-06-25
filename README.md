
# 📈 Stock Price Change Alert with News and SMS Notifications

## 🔖 Project Title
Stock Alert with News Headlines via Twilio SMS

## 📝 Description
This Python script monitors stock price changes (Tesla Inc.), calculates the percentage difference between the last two trading days, and sends SMS alerts with news headlines via Twilio if there's any movement. It uses Alpha Vantage for stock prices, NewsAPI for latest news, and Twilio to deliver SMS alerts.

---

## 🚀 Features
- Fetch stock price data (from Alpha Vantage or local JSON)
- Compute price change percentage between two days
- If any change detected, fetch latest news articles about Tesla
- Send alerts via Twilio SMS including stock change and top 3 news headlines

---

## 📂 Project Structure
```
📦 EASY_STOCK
 ┣ 📄 main.py        # Main logic for fetching prices, news, and sending SMS
 ┣ 📄 data.json      # Pre-saved Alpha Vantage stock data
```

---

## 🔧 How It Works
1. Load stock data from `data.json`.
2. Compare yesterday's and the day-before's closing prices.
3. If there is **any percentage change**, get latest 3 Tesla news articles.
4. Send all 3 articles as SMS to your phone using Twilio.

---

## 🧪 APIs Used

### 🟡 Alpha Vantage (Stock Data)
- API Key: `ALPHA_VANTAGE_API_KEY`
- Endpoint: `https://www.alphavantage.co/query`
- Get Free Key: https://www.alphavantage.co/support/#api-key

### 🟡 NewsAPI (News Headlines)
- API Key: `NEWS_API_KEY`
- Endpoint: `https://newsapi.org/v2/everything`
- Get Free Key: https://newsapi.org/register

### 🟡 Twilio (SMS Sending)
- Requirements:
  - Twilio Account: https://www.twilio.com
  - Phone number (verified)
- Install Library:
  ```bash
  pip install twilio
  ```
- Get:
  - `account_sid`
  - `auth_token`
  - `from_` (Twilio number)
  - `to` (Your verified phone number)

---

## 🧰 How to Run

### 1. Install Required Libraries
```bash
pip install requests twilio
```

### 2. Replace Keys in Code
Update in `main.py`:
```python
ALPHA_VANTAGE_API_KEY = "your_alpha_key"
NEWS_API_KEY = "your_news_api_key"
account_sid = "your_twilio_sid"
auth_token = "your_twilio_auth_token"
```

### 3. Run the Script
```bash
python main.py
```

---

## 🔐 Caution
- **Do not commit real API keys or auth tokens** to GitHub.
- Use `.env` file or environment variables in production.

---

## 📱 SMS Output Example

Here's how the Twilio trial SMS alert looks when received:

<img src="https://github.com/user-attachments/assets/23d7a5a0-0637-47f5-819c-5fbefb34e961" alt="SMS Preview" width="300"/>


- You receive **three messages** for each article if stock price change is detected.
- Each message includes:
  - 📉 Stock symbol and % change
  - 📰 News headline
  - ✉️ News brief (if available)

---


## 📌 GitHub Tags
```
#Python #Twilio #SMSAlert #StockTracker #NewsAPI #AlphaVantage #Tesla #APIAutomation #FinanceTool
```

---

## 👨‍💻 Author
Made with ❤️ by Mithil Dabhi

