import requests
import json
from datetime import datetime

USERNAME = "andy489"
TOKEN = "qwer1234"
GRAPH_ID = "graph489"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# 1. Create user account

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# https://pixe.la/@andy489
# print(json.dumps(response.json(), indent=4))

# 2. Create a graph definition
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# 3. Get the graph
# https://pixe.la/v1/users/{a-know}/graphs/{test-graph}
# https://pixe.la/v1/users/andy489/graphs/graph489.html

# 4. Post value to the graph
# https://docs.pixe.la/entry/post-pixel
PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# https://www.w3schools.com/python/python_datetime.asp
# today = datetime.now()
today = datetime(year=2025, month=2, day=4)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "22.84",
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
# print(response.text)
# print(today.strftime("%Y%m%d"))

# 5. Browse again
# https://docs.pixe.la/entry/put-pixel
# https://docs.pixe.la/entry/delete-pixel

UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "14.5"
}

# requests.put(url=UPDATE_ENDPOINT, params=new_pixel_data, headers=headers)

DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)
