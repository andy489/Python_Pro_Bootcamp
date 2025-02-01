import smtplib
import datetime as dt
import random

MY_EMAIL = "my_email@yahoo.com"
MY_PASS = "my_pass(3rd party)"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}")
