import requests
from datetime import datetime, timedelta
import json
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


ALPHA_VANTAGE_API_KEY = "BKZQCQ3CNYTPMFXW"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY
}
f = open('EASY_STOCK/data.json')
data = json.load(f)
print(data)

dates = sorted(data.keys(), reverse=True)

yesterday = dates[0]
day_before_yesterday = dates[1]
print(yesterday, day_before_yesterday)


#2- Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = data[day_before_yesterday]["4. close"]
day_before_yesterday_closing_price = float(day_before_yesterday_closing_price)
print(day_before_yesterday_closing_price)
# Get yesterday's closing price
yesterday_closing_price = data[yesterday]["4. close"]
yesterday_closing_price = float(yesterday_closing_price)
print(yesterday_closing_price)

#3- Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
if diff < 0:
    print(f"Change in Stock Price is Lower by {round(abs(diff),2)} $")
else:
    print(f"Change in Stock Price is Lower by {diff}$")

#4- Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round(float((diff / day_before_yesterday_closing_price)* 100),2)
print(f"The change in percentage {percentage_diff}%")

#5- If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage_diff) > 0:
    print("Get News")
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    NEWS_API_KEY = "c6b294eb29764f4684eeb02f8b48b121"  # Replace with your NewsAPI key

    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 3
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json().get("articles", [])[:3]
    for article in articles:
        print(f"Headline: {article['title']}")
        print(f"Brief: {article['description']}\n")


#6 - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    top_3_articles = articles[:3]   
    headlines = [f"Headline: {article['title']}" for article in top_3_articles]
        
    account_sid = "AC5ab45a8aa0e17ff9b0399cd330ce7ca0"
    auth_token = "9c3fb4a0d9ca9e552e0b08bddb833a7c"

    if diff < 0:
        client = Client(account_sid,auth_token)
        message = client.messages.create(
            body=f"{STOCK_NAME}: {'🔺' if percentage_diff > 0 else '🔻'}{abs(percentage_diff)}%\nHeadline: {article['title']}\nBrief: {article['description']}",
            from_='+17246045389',
            to='+919173298372'
        )
        print(message.sid)

#7- Create a new list of the first 3 article's headline and description using list comprehension.
article_summaries = [
    f"Headline: {article['title']}\nBrief: {article['description']}" 
    for article in articles[:3]
]
print(article_summaries)

#8- Send each article as a separate message via Twilio. 
for article in articles[:3]:
    message_body = (
        f"{STOCK_NAME}: {'🔺' if percentage_diff > 0 else '🔻'}{abs(percentage_diff)}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}"
    )
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_='+17246045389',
        to='+919173298372'
    )
    print(message.sid)


