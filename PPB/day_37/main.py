import requests
from datetime import datetime, date, timedelta

# Pixela Website: https://pixe.la/
# Pixela API Documentation: https://docs.pixe.la/
# Requests Module Documentation: https://requests.readthedocs.io/en/latest/api/

USERNAME = "andy4489"
TOKEN = "saoIfn2of4eAoi"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": "andy4489",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# My profile page: https://pixe.la/@andy4489

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# My newly created Graph: https://pixe.la/v1/users/andy4489/graphs/graph1.html


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
yesterday = date.today() - timedelta(days=1)
specific_day = datetime(year=2025, month=5, day=20)
the_day = today
# print(the_day)

pixel_data = {
    "date": the_day.strftime("%Y%m%d"),
    "quantity": "6.03",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{the_day.strftime("%Y%m%d")}"

new_pixel_data = {
    "quantity": "7.94"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{the_day.strftime("%Y%m%d")}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
