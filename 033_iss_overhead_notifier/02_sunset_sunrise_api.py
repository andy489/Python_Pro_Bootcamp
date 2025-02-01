import requests
import json
from datetime import datetime

# https://sunrise-sunset.org/api
# https://api.sunrise-sunset.org/json
# https://www.w3schools.com/python/ref_string_split.asp

MY_LAT = 42.697708
MY_LNG = 23.321867

# https://www.latlong.net/
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted=0")
response.raise_for_status()
data = response.json()
# print(data)
print(json.dumps(data, indent=4))

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()
print(time_now)

print(sunrise)
print(sunrise.split("T")[1].split(":")[0])


