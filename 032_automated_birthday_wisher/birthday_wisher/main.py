# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com
import random
# https://docs.python.org/3/library/smtplib.html

from datetime import datetime
import pandas
import smtplib

MY_EMAIL = "my_mail@yahoo.com"
MY_PASS = "my_pass(3rd party)"

today = datetime.now()
today_tuple = (today.month, today.day)

df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_template/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")\

# Host your code in the cloud:
# https://www.pythonanywhere.com/
