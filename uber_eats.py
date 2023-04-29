# pylint: disable=line-too-long
#importing required libraries
import ctypes
import time
import sys
import pandas as pd
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome , ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC #provides a set of predefined conditions that can be used to wait for specific events to occur on a webpage.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re

#get user input
'''
user_address= input("Please enter where you would like the food to be delivered?")
requested_restaurant= input("Please enter from which restaurant you would like to order food?")
requested_food_item= input("Please enter what food item you would like to order?")
'''

#specify the complete path to the Google Chrome binary.
options = Options()
options= uc.ChromeOptions()
options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
#chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = uc.Chrome(use_subprocess=True, options=options)

driver.maximize_window()

#Take the user input to obtain the URL of the website to be scraped, and web scrape the page.
VAL= "https://www.ubereats.com/ca/near-me"
wait = WebDriverWait(driver, 10) #10 seconds before timing out
driver.get(VAL) #loads the web page in the selected browser session
get_url = driver.current_url #get the url of the current page
wait.until(EC.url_to_be(VAL)) #EC.url_to_be checks the current url to become the expected URL "val"
if get_url == VAL:  #ensure that the correct url has been opened
    page_source = driver.page_source # get the entire HTML source code of a webpage as a string

driver.implicitly_wait(120)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

element= driver.find_element(By.CSS_SELECTOR, "input[aria-controls='location-typeahead-home-menu']")
element.send_keys("")
time.sleep(3)
element.send_keys(Keys.RETURN)

driver.implicitly_wait(130)
time.sleep(3)

element= driver.find_element(By.CSS_SELECTOR, "input[aria-controls='search-suggestions-typeahead-menu']")
element.send_keys("Pizza Depot")
time.sleep(3)
element.send_keys(Keys.RETURN)
driver.implicitly_wait(120)


try:
    restaurant_container = driver.find_element(By.XPATH, "//div[@data-testid='store-card']")
    restaurant = restaurant_container.find_element(By.XPATH, ".//h3[contains(text(), 'Pizza Depot')]")
    restaurant.click()
    driver.implicitly_wait(120)
    time.sleep(5)
    '''
    exit_button =driver.find_element(By.CSS_SELECTOR, "path[d='m21.1 5.1-2.2-2.2-6.9 7-6.9-7-2.2 2.2 7 6.9-7 6.9 2.2 2.2 6.9-7 6.9 7 2.2-2.2-7-6.9 7-6.9Z']")
    # click the button
    if exit_button is not None and exit_button.is_displayed():
        exit_button.click()
    '''
    
    price_element = driver.find_element(By.XPATH, "//span[contains(text(), '$') and contains(text(), 'Delivery Fee')]")
    if price_element is not None:
        price = price_element.text.split()[-3]
        print("\n\tUber Eats' Delivery fee:" + price)
    else:
        print("\n\tUber Eats' Delivery fee: Restaurant is closed on Uber Eats")
    
except NoSuchElementException:
    print("Restaurant not found.")
