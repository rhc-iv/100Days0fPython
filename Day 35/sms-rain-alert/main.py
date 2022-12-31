#!/usr/bin/env python3

# Note! For the code to work you need to replace all the placeholders
# with your own details. e.g., account_sid, lat/lon, from/to phone
# numbers.

# --- IMPORTS ---

import requests
import os
from twilio.rest import Client

# --- CONSTANTS, DICTS, GLOBALS, LISTS ---

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = os.environ.get("OWN_API_KEY")
account_sid = "ACbebd7e652ab71daec5fe10762cbac2fd"
auth_token = os.environ.get("TWL_AUTH_TKN")

weather_params = {
    "lat": 41.006300,
    "lon": -85.759420,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

# --- METHODOLOGY ---

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(
        account_sid,
        auth_token,
    )
    message = client.messages \
        .create(
            body="Nasty weather ahead! Bring an umbrella! ⛈️🌨️🌧️",
            from_="+17207072233",
            to="+15042501250",
        )
