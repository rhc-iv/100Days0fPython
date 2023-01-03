#!/usr/bin/env python3

# --- IMPORTS ---

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# --- CONSTANTS, DICTS, GLOBALS, LISTS ---

ACCOUNT_EMAIL = "rhc.iv@icloud.com"
ACCOUNT_PASSWORD = "h#72^pjf8nkFD&XFwr25Znbzep$4sx$j"

JOB_SEARCH = "https://www.linkedin.com/jobs/search/?currentJobId=3409544447" \
             "&f_AL=true&f_BE=%5B%5D&f_C=%5B%5D&f_E=1%2C2&f_EA=%5B%5D&f_F" \
             "=%5B%5D&f_FCE=%5B%5D&f_I=%5B%5D&f_JC=%5B%5D&f_JIYN=%5B%5D&f_JT" \
             "=F%2CP%2CC%2CT%2CI%2CO&f_PP=%5B%5D&f_SB2=%5B%5D&f_T=%5B%5D" \
             "&f_TPR=r2592000&f_WT=2&keywords=python%20developer&sortBy=DD"

chrome_driver_path = Service(
    "/Users/rhc.iv/Development/chromedriver_mac_arm64/chromedriver")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)

# --- METHODOLOGY ---

driver.maximize_window()
driver.get(JOB_SEARCH)

sign_in_button = driver.find_element(By.LINK_TEXT,
                                     "Sign in")
sign_in_button.click()

time.sleep(3)

email_field = driver.find_element(By.ID,
                                  "username")
email_field.send_keys(ACCOUNT_EMAIL)

password_field = driver.find_element(By.ID,
                                     "password")
password_field.send_keys(ACCOUNT_PASSWORD)

enter_button = driver.find_element(By.XPATH,
                                   "//*[@id='organic-div']/form/div[3]/button")
enter_button.click()

next_btn = driver.find_element(By.CLASS_NAME,
                               value="jobs-save-button")
next_btn.click()

next_btn.send_keys(Keys.END)

message_overlay = driver.find_element(By.ID, value="ember99")
message_overlay.click()

follow_button = driver.find_element(By.CLASS_NAME,
                                    value="follow")
follow_button.click()
