from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import c
from classes import GraphicalLocator
from functions import login, search_for_img

import time

driver = webdriver.Chrome(c.PATH)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get(c.WOOZWORLD)

# Login
login(c.EMAIL_ADDRESS, c.PASSWORD, driver)
time.sleep(3)

# Load game client
driver.get(c.GAME_CLIENT)
time.sleep(12)

# Check for news menu X
search_for_img(c.NEWS_X, driver)
time.sleep(1)

# Check for second news menu X
search_for_img(c.NEWS_X_2, driver)