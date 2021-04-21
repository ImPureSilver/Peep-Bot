import gc
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

rtx3060_sku = []
amazon_sku = []

bestbuy_login = ["EMAIL HERE", "PASSWORD HERE"]

with open("bestbuy-rtx3060.txt", "r") as sku_file:
    for line in sku_file.readlines():
        rtx3060_sku.append(str(line).strip('\n'))
    pass


def add_to_cart(page_source):
    # For BestBuy
    # buttonState\":\"SOLD_OUT\
    # "buttonState\":\"ADD_TO_CART\
    result = page_source.find("buttonState\":\"ADD_TO_CART\\\\")

    if result < 0:
        return False

    return True


def checkout():
    # todo: step by step procedure for checking out

    # These are just click events, no need for variables

    # Add to cart
    driver.find_element_by_xpath("xpath=//div[2]/div/div[2]/div/div/div/div/button").click()
    # Go to cart
    driver.find_element_by_xpath("xpath=//div[8]/div/div/div/div/div/div/div/div[3]/a")
    # Password box
    password_box = driver.find_element_by_xpath("xpath=//input")
    # password_box.send_keys.send_keys(bestbuy_login[1])
    password_box.click().send_keys(Keys.ENTER)
    # continue to payment
    driver.find_element_by_xpath("xpath=//div[2]/div/div/button/span")

    # These fields need to be filled in
    # cc number
    driver.find_element_by_xpath("xpath=//div/input")
    # first name
    # last name
    # address
    # city
    # state
    # zipcode

    # place order
    pass


def check_stock():
    # api_link = "https://api.bestbuy.com/click/-/%s/pdp"

    for sku in rtx3060_sku:

        # format the link with the sku
        # pass in the link to the webdriver to open
        driver.get(f"https://api.bestbuy.com/click/-/{sku}/pdp")
        # look for the add to cart
        # if it's there, add it to cart and follow checkout procedure
        if add_to_cart(driver.page_source):
            os.system('play sound1.wav')
            checkout()
        # else, check on the next sku

    #     Close out browser and relaunch it to regain some memory
    driver.close()


driver = webdriver.Firefox()

while True:
    check_stock()
    gc.collect()
    time.sleep(250)
    driver = webdriver.Firefox()

# todo: future plan: make these run in parallel
