#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service(
    "/Users/rhc.iv/Development/chromedriver_mac_arm64/chromedriver")
op = webdriver.ChromeOptions()
op.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=op)

driver.get(
    "https://web.archive.org/web/20220120120408/https://secure-retreat-92358"
    ".herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR,
#                                     "#articlecount a")
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT,
#                                   "Current events")
# all_portals.click()

reg_first = driver.find_element(By.NAME, "fName")
reg_first.send_keys("Robert")
reg_last = driver.find_element(By.NAME, "lName")
reg_last.send_keys("Carr")
reg_email = driver.find_element(By.NAME, "email")
reg_email.send_keys("rhc.iv@icloud.com")
registration = driver.find_element(By.CSS_SELECTOR, "body > form > button")
registration.send_keys(Keys.ENTER)