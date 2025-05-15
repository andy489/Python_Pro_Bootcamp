import requests
import datetime as dt
import smtplib
import time

# Sunrise and Sunset Times API: https://sunrise-sunset.org/api
# https://api.sunrise-sunset.org/json?lat=42.697708&lng=23.321867

# w3schools Python split() method Documentation: https://www.w3schools.com/python/ref_string_split.asp
# Find Your Current Latitude and Longitude Tool: https://www.latlong.net/

MY_EMAIL = "MY_EMAIL"
MY_PASSWORD = "MY_PASS"
MY_LAT = 42.697708
MY_LNG = 23.321867

ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_ENDPOINT = "https://api.sunrise-sunset.org/json"


def is_iss_overhead():
    response = requests.get(url=ISS_ENDPOINT)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # My position is within +5 or -5 degrees of the iss position.
    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
            MY_LNG - 5 <= iss_longitude <= MY_LNG + 5)


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(SUNRISE_SUNSET_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    return time_now >= sunset or time_now <= sunrise


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("MY_SMTP_ADDR")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
