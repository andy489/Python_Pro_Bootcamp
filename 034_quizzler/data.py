import requests
# https://opentdb.com/api_config.php

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
    "difficulty": "medium",
}

# response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
response = requests.get("https://opentdb.com/api.php", params=parameters)
data = response.json()

question_data = data["results"]

# https://www.w3schools.com/html/html_entities.asp
# https://www.freeformatter.com/html-escape.html
# https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string