#!/usr/bin/env python3

# --- IMPORTS ---

import smtplib

import lxml
import requests
from bs4 import BeautifulSoup

# --- CONSTANTS, DICTS, GLOBALS, LISTS ---

MY_EMAIL = "august_hornet72@gmail.com"
MY_PASSWORD = "dmufwdyiuopwyyxd"

BUY_PRICE = 100.00
PRODUCT = "https://www.amazon.com/gp/product/B09BRG3GRR/ref" \
          "=ox_sc_saved_title_7?smid=ATVPDKIKX0DER&th=1"

# --- METHODOLOGY ---

response = requests.get(
    PRODUCT,
    headers={
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 "
                      "Safari/605.1.15"
    }
)
soup = BeautifulSoup(response.text, "lxml")
title = soup.find(id="productTitle").get_text().strip()

# --- METHODOLOGY ---

price_whole = soup.find("span", class_="a-price-whole")
price_fraction = soup.find("span", class_="a-price-fraction")
price_as_float = ("$" + price_whole.text + price_fraction.text)

if price_as_float > str(BUY_PRICE):
    message = f"{title} is now ${price_whole}.{price_fraction}"

    with smtplib.SMTP(smtp.gmail.com, port=587) as connection:
        connection.starttls()
        result = connection.login(
            MY_EMAIL,
            MY_PASSWORD,
        )
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="rhc.iv@cloud.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )

print("$" + price_whole.text + price_fraction.text + " " + title)
