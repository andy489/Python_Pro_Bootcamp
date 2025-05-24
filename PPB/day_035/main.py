import os
import json
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

load_dotenv()

owm_api_key = os.environ["OWM_API_KEY"]
print(owm_api_key)
twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
print(twilio_account_sid)

twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# Open Weather Map Condition IDs and Condition Codes: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# Find Place that's raining using Ventusky: https://www.ventusky.com/

forecast_params = {
    "lat": 42.69,
    "lon": 23.32,
    "cnt": 4,
    "appid": owm_api_key,
}

response = requests.get(OWM_Endpoint, params=forecast_params)
response.raise_for_status()
weather_data = response.json()
# weather_data_formatted = json.dumps(weather_data, indent=4)

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER",
    )

    print(message.status)
