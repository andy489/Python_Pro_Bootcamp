import os
import requests
import json
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

# Stock Market API: https://www.alphavantage.co/
# Dig in Documentation for Stock Market API: https://www.alphavantage.co/documentation/#daily
# Get Articles Related with the Company Name: https://newsapi.org/
# Dig in Documentation for News API: https://newsapi.org/docs/endpoints/everything

load_dotenv()

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API_KEY,
}

MIN_DIFF_PERCENTAGE = 0.4

stock_response = requests.get(ALPHA_VANTAGE_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]
# print(json.dumps(data, indent=4))

data_list = [value for key, value in data.items()]

# Get yesterday's closing stock price
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = ["🔺", "🔻"][difference > 0]

diff_percent = difference / float(yesterday_closing_price) * 100

if abs(diff_percent) > MIN_DIFF_PERCENTAGE:
    # Get top 3 articles related to the COMPANY_NAME
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:2]
    # print(json.dumps(three_articles, indent=4))

    # Create a new list of the first 3 articles headline and description using list comprehension.
    formatted_articles = \
        [(f"{STOCK_NAME}: {up_down}{round(diff_percent, 1)}%\nHeadline: {article['title']}. "
          f"\nBrief {article['description']}") for article in three_articles]

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.getenv("https_proxy")}
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
    # print(formatted_articles)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )

        print(message.status)
