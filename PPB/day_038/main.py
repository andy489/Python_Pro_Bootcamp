import requests
import json
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

# Setup API Credentials and Google Spreadsheet: https://docs.google.com/spreadsheets

GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 176
AGE = 36

# Get Exercise Stats with Natural Language Queries: https://www.nutritionix.com/
# Nutritionix API Documentation: https://docx.syndigo.com/developers/docs/nutritionix-api-guide
# Natural Language for Exercise API Documentation: https://docx.syndigo.com/developers/docs/natural-language-for-exercise

# Get your API_ID and API_KEY: https://www.nutritionix.com/business/api

APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

# Create Google Spreadsheet Table: https://docs.google.com/spreadsheets
# Use Table Header: Date|Time|Exercise|Duration|Calories

# Setup Your Google Sheet with Sheety: https://sheety.co/

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(json.dumps(result, indent=4))

# Adding date and time
datetime_now = datetime.now()
datetime_now_offset = datetime.now() + timedelta(hours=3)
today_date = datetime_now_offset.strftime("%d/%m/%Y")
now_time = datetime_now_offset.strftime("%X")

# Sheety Project API. Check your Google sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "myWorkout"
sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

# Sheety API Call & Authentication
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety Authentication Option 1: No Auth
    """
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    """

    # Sheety Authentication Option 2: Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"],
        )
    )

    # Sheety Authentication Option 3: Bearer Token
    """
    bearer_headers = {
        "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )    
    """
    print(f"Sheety Response: \n {sheet_response.text}")
