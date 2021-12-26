from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from waiting import wait

import c
from classes import GraphicalLocator
from functions import login, img_found, click_img, drag_img

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
canvas = driver.find_element_by_id(c.CANVAS_ID)
actions = ActionChains(driver)

# Check for news menu X
wait(lambda: img_found(c.NEWS_X, driver), timeout_seconds=30, waiting_for="news x button found")
click_img(c.NEWS_X, driver)

# Check for second news menu X
wait(lambda: img_found(c.NEWS_X_2, driver), timeout_seconds=30, waiting_for="news x 2 button found")
click_img(c.NEWS_X_2, driver)

# Search for navigator icon
wait(lambda: img_found(c.NAVIGATOR, driver), timeout_seconds=30, waiting_for="navigator button found")
click_img(c.NAVIGATOR, driver)

# Search for resource tab
wait(lambda: img_found(c.RESOURCES, driver), timeout_seconds=30, waiting_for="resources button found")
click_img(c.RESOURCES, driver)

# The forest
wait(lambda: img_found(c.FOREST, driver), timeout_seconds=30, waiting_for="forest tab")
click_img(c.FOREST, driver)

# Zoom select (test later)
# wait(lambda: img_found(c.ZOOM_1, driver), timeout_seconds=30, waiting_for="resources button found")
# drag_img(c.ZOOM_1, driver, 0, 50)

# Up arrow
# wait(lambda: img_found(c.UP, driver), timeout_seconds=30, waiting_for="up arrow")
# click_img(c.UP, driver)

# up
actions.move_to_element_with_offset(canvas, 696, 306)
actions.click()
actions.perform()

# label
wait(lambda: img_found(c.SHOW_LABELS, driver), timeout_seconds=30, waiting_for="show labels button")
click_img(c.SHOW_LABELS, driver)

"""
room 1
up 696. 306
down 800, 672

room 1 - up:
up 840, 250

room 1 - down

"""