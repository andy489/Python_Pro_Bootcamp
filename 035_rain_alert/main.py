import requests
import os
from twilio.rest import Client

# open weather map
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = os.environ.get("OWM_API_KEY")
LON = 42.697708
LAT = 23.321867
# twilio
ACCOUNT_SID = os.environ.get("ACC_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lon": LON,
    "lat": LAT,
    "appid": OWM_API_KEY,
    "cnt": 4,
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+123_TRIAL_NUMBER",
        to="+123_YOUR_VERIFIED_NUMBER"
    )

    print(message.status)
