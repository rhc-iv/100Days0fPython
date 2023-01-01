#!/usr/bin/env python3

# --- IMPORTS ---

import smtplib

from twilio.rest import Client

# --- CONSTANTS, DICTS, GLOBALS, LISTS ---

TWILIO_SID = "ACbebd7e652ab71daec5fe10762cbac2fd"
TWILIO_AUTH_TOKEN = "fb88d2fef757271f41eeee68118e7c34"
TWILIO_VIRTUAL_NUMBER = "+17207072233"
TWILIO_VERIFIED_NUMBER = "+15042501250"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "august.hornet72@gmail.com"
MY_PASSWORD = "dmufwdyiuopwyyxd"


# --- METHODOLOGY ---


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n"
                        f"{google_flight_link}".encode('utf-8')
                )
