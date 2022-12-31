#!/usr/bin/env python3

# Below are illustrations of the use of both the SMTPLIB module and
# the DATETIME module built into Python.

# --- IMPORTS ---

import datetime as dt
import smtplib

# Insert our email/password (app password in Gmail) as CONSTANTS:

# --- CONSTANTS & GLOBAL VARIABLES ---

MY_EMAIL = "august.hornet72@gmail.com"
MY_PASSWORD = "dmufwdyiuopwyyxd"

# Create a new object ("connection") from the "SMTP" class:

connection = smtplib.SMTP("smtp.gmail.com")

# Add secure encryption to the process with .starttls() method:

connection.starttls()

# Provide our login credentials via the .login() method:

connection.login(
    user=MY_EMAIL,
    password=MY_PASSWORD,
)

# Send mail using the .sendmail() method. There needs to be a sending
# address (from_addr) and a receiving address (to_addrs). Finally,
# the contents of the email are added using the "msg" argument:

connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs="rhc.iv@icloud.com",
    msg="Hello. This is a test of the Python smtplib module.".encode("utf-8"),
)

# We also need to close the connection so that the email is not sent
# on an infinite loop:

connection.close()

# With the datetime module, we can get the current time & date by
# using the .now() method:

now = dt.datetime.now()

# Further, we can access various attributes of the .now() method:

year = now.year
month = now.month
weekday = now.weekday()
day = now.day
hour = now.hour
minute = now.minute

# We can also use the datetime module to store specific data. If we
# wanted to store our own birthday:

dob = dt.datetime(
    year=1972,
    month=8,
    day=2,
)

print(dob)