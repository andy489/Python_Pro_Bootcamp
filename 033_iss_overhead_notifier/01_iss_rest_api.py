import requests

# https://pypi.org/project/requests/

# https://open-notify.org/Open-Notify-API/ISS-Location-Now/
END_POINT = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=END_POINT)
response.raise_for_status()

data=response.json()
print(data)

iss_position = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])
print(iss_position)

# https://www.latlong.net/Show-Latitude-Longitude.html