import requests
import json
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "STOCK_API_KEY"
NEWS_API_KEY = "NEWS_API_KEY"

TWILIO_SID = "MY_TWILIO_SID"
TWILIO_AUTH_TOKEN = "MY_TWILIO_AUTH_TKN"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 20 - 40 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp
up_down = None
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# print(difference)

# Calc the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)

# If diff percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 5:
    # print("Get News")

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    # Use Python slice operator to create a list that contains the first 3 articles.
    # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # print("Get News")

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Create a new list of the first 3 article's headline and description using list comprehension.
    # To send a separate message with each article's title and description to your phone number.
    three_articles = articles[:3]
    # print(articles[:3])

    formatted_articles = [(f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
                           f"Headline: {article['title']}. "
                           f"\nBrief: {article['description']}")
                          for article in three_articles]

    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Format the message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="VIRTUAL_TWILIO_NUM",
            to="VERIFIED_NUM"
        )
