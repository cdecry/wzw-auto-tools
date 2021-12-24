from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from waiting import wait

import c
from classes import GraphicalLocator
from functions import login, img_found, search_for_img

import time

driver = webdriver.Chrome(c.PATH)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get(c.WOOZWORLD)

# input email
email = input()
# input password
password = input()


# Login
login(email, password, driver)

# Load game client
driver.get(c.GAME_CLIENT)

# Check for news menu X
wait(lambda: img_found(c.NEWS_X, driver), timeout_seconds=30, waiting_for="news x button found")
search_for_img(c.NEWS_X, driver)

# Check for second news menu X
wait(lambda: img_found(c.NEWS_X_2, driver), timeout_seconds=30, waiting_for="news x 2 button found")
search_for_img(c.NEWS_X_2, driver)

# Search for navigator icon
wait(lambda: img_found(c.NAVIGATOR, driver), timeout_seconds=30, waiting_for="navigator button found")
search_for_img(c.NAVIGATOR, driver)