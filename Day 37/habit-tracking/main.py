#!/usr/bin/env python3

# --- IMPORTS ---

from datetime import datetime
import requests

# --- CONSTANTS, DICTS, GLOBALS, LISTS ---

GRAPH_ID = "graph2022"
USERNAME = "rhciv72"
TOKEN = "rV%@RZpRG!6g9$3gH%Dhndr@htb%%JRo"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Python Learning",
    "unit": "Hours",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
f"/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%m-%d-%y"),
    "quantity": "1.00",
}

pix_headers = {
    "X-USER-TOKEN": TOKEN,
}

# --- METHODOLOGY ---

# response = requests.post(
#     url=pixela_endpoint,
#     json=user_params,
# )

# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers,
# )

# response = requests.post(
#     url=pixel_creation_endpoint,
#     json=pixel_data,
#     headers=pix_headers,
# )

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/" \
                  f"{today.strftime('%m-%d-%y')}"

new_pixel_data = {
    "quantity": 2.0,
}

response = requests.put(
    url=update_endpoint,
    json=new_pixel_data,
    headers=headers,
)

print(response.text )