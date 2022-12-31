#!/usr/bin/env python3

# --- IMPORTS ---

import datetime as dt
import random
import smtplib

# --- CONSTANTS & GLOBAL VARIABLES ---

MY_EMAIL = "august.hornet72@gmail.com"
MY_PASSWORD = "dmufwdyiuopwyyxd"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=MY_PASSWORD,
        )
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="rhc.iv@icloud.com",
            msg=f"Subject: Monday Motivation!\n\n{quote}".encode(
                "utf-8"),
        )
