#!/usr/bin/env python3

# --- IMPORTS ---

# Import the Requests library for use with API calls. It is not
# pre-built into Python so therefore must be installed via PIP.

from datetime import datetime
import requests

# --- METHODOLOGY ---

# Use the .get() method (in the Requests library) to pass a string
# argument in the form of a URL & then save that to a variable:

# response = requests.get(
#     url="http://api.open-notify.org/iss-now.json"
# )

# The Request library has a built-in method that will raise
# exceptions for the end-user. This method is the raise_for_status()
# method:

# response.raise_for_status()

# Using the .json() method in Requests, we can receive the API data
# in .json format and save that to a variable:

# data = response.json()

# We can extract different key:value pairs from the .json data
# response by using a list to enumerate different keys, then those
# keys will provide the corresponding values:

# latitude = response.json()["iss_position"]["latitude"]
# longitude = response.json()["iss_position"]["longitude"]

# We can create a tuple using the variables above to show both the
# latitude & longitude values that we've extracted:

# iss_position = (latitude, longitude)
# print(iss_position)

# As an aside, there are lots of interesting geographic tools at our
# disposal on the Internet at:

# https://www.latlong.net/geo-tools

MY_LAT = 41.006302
MY_LNG = -85.759422

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json",
    params=parameters
)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(int(sunrise) - 5)
print(int(sunset) - 5)

time_now = datetime.now()

print(time_now.hour)
