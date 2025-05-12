import smtplib
import datetime as dt
import random

# 101 Monday Motivational Quotes from the Positivity Blog: https://www.positivityblog.com/monday-motivation-quotes/

MONDAY_IND = 0

GOOGLE_SMTP = "smtp.gmail.com"
FROM_EMAIL = "YOUR_EMAIL_HERE"
FROM_PASS = "YOUR_THIRD_PARTY_PASSWORD_HERE[16_SYMBOLS_WITHOUT_SPACES]"
TO_EMAIL = "RECIPIENT_EMAIL_HERE"
PORT = 587

now = dt.datetime.now()
weekday = now.weekday()

if weekday == MONDAY_IND:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP(GOOGLE_SMTP, port=PORT) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=FROM_PASS)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
