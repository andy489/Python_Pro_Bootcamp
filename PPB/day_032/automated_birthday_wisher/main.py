import smtplib
import datetime as dt
import pandas as pd
import random

# Python smtplib Documentation: https://docs.python.org/3/library/smtplib.html

GOOGLE_SMTP = "smtp.gmail.com"
FROM_EMAIL = "YOUR_EMAIL_HERE"
FROM_PASS = "YOUR_THIRD_PARTY_PASSWORD_HERE[16_SYMBOLS_WITHOUT_SPACES]"
TO_EMAIL = "RECIPIENT_EMAIL_HERE"
PORT = 587

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")

birthdays_dict = {}
for (index, data_row) in data.iterrows():
    date_key = (data_row.month, data_row.day)

    if date_key not in birthdays_dict:
        birthdays_dict[date_key] = []

    birthdays_dict[date_key].append(data_row)

if today_tuple in birthdays_dict:
    birthdays_list = birthdays_dict[today_tuple]

    for birthday in birthdays_list:
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday["name"])

        with smtplib.SMTP(GOOGLE_SMTP, port=PORT) as connection:
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=FROM_PASS)
            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
