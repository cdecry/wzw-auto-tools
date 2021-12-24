from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import c
from classes import GraphicalLocator

def login(email: str, password: str, drv: any):
    email_form = drv.find_element_by_name(c.EMAIL_FORM_NAME)
    email_form.send_keys(c.EMAIL_ADDRESS)

    password_form = drv.find_element_by_name(c.PW_FORM_NAME)
    password_form.send_keys(c.PASSWORD)
    password_form.send_keys(Keys.RETURN)

def search_for_img(img_path: object, drv: any):
    img_check = GraphicalLocator(img_path)
    img_check.find_me(drv)

    is_found = True if img_check.threshold['shape'] >= 0.8 and \
                    img_check.threshold['histogram'] >= 0.4 else False

    canvas = drv.find_element_by_id(c.CANVAS_ID)
    actions = ActionChains(drv)

    if (is_found):
        actions.move_to_element_with_offset(canvas, img_check.center_x / 2, img_check.center_y / 2)
        actions.click()
        actions.perform()
    else:
        print("Object not found!")