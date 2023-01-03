#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# TODO 1: the path where the chrome_driver resides:

chrome_driver_path = Service(
    "/Users/rhc.iv/Development/chromedriver_mac_arm64/chromedriver")

# TODO 2: constructing a ChromeOptions object to influence the behavior of
#  the webdriver:

op = webdriver.ChromeOptions()

# TODO 3: constructing the driver object with options declared above:

driver = webdriver.Chrome(service=chrome_driver_path, options=op)

# TODO 4: using the driver to scrap event_name & event date:

driver.get("https://www.python.org/")
names = []
for event_number in range(1, 6):
    event_name = driver.find_element(By.XPATH,
                                     f'//*[@id="content"]/div/section/div['
                                     f'3]/div[2]/div/ul/li[{event_number}]/a')
    names.append(event_name.text)

times = []
for event_number in range(1, 6):
    event_date = driver.find_element(By.XPATH,
                                     f'//*[@id="content"]/div/section/div['
                                     f'3]/div[2]/div/ul/li['
                                     f'{event_number}]/time')
    times.append(event_date.text)

# TODO 5: converting the name and time list into a single python_events
#  dictionary:

python_events = {}
for name in names:
    for time in times:
        python_events[name] = time

print(python_events)

driver.quit()
