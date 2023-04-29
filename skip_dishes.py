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
driver = uc.Chrome(use_subprocess=True, options=options)
driver.maximize_window()

#Take the user input to obtain the URL of the website to be scraped, and web scrape the page.
VAL= "https://www.skipthedishes.com/"
wait = WebDriverWait(driver, 10) #10 seconds before timing out
driver.get(VAL) #loads the web page in the selected browser session
get_url = driver.current_url #get the url of the current page
wait.until(EC.url_to_be(VAL)) #EC.url_to_be checks the current url to become the expected URL "val"
if get_url == VAL:  #ensure that the correct url has been opened
    page_source = driver.page_source # get the entire HTML source code of a webpage as a string

driver.implicitly_wait(120)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

element= driver.find_element(By.CSS_SELECTOR, "input[aria-label='Enter Your Address - Use the up and down arrow keys to navigate address suggestions.']")
element.send_keys("")
time.sleep(3)
element.send_keys(Keys.RETURN)
time.sleep(3)
find_restaurants = driver.find_element(By.CSS_SELECTOR, "button[class*='MuiButton-containedSizeLarge-']")
find_restaurants.click()

driver.implicitly_wait(120)
element= driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Cuisines, Restaurants, or Items']")
element.send_keys("Kimchi Sushi")

driver.implicitly_wait(120)
time.sleep(2)

restaurant_path= driver.find_element(By.CSS_SELECTOR, "span[class='styles__Title-czubko-4 hLParj']")
try:
    price_element = driver.find_element(By.XPATH, "//span[contains(text(), '$') and contains(text(), 'Delivery Fee')]")
    price = price_element.text.split()[-3]
except IndexError:
    print("Restaurant Not Found")
else:
    print("\n\tSkip the dishes' Delivery fee: "+ price)
