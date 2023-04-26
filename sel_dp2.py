# importing required libraries
import ctypes
import time
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

import sys


#specify the complete path to the Google Chrome binary.
options = Options()
options= uc.ChromeOptions()
options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
#chrome_driver_binary = "/usr/local/bin/chromedriver"
#options.add_argument('--headless')
driver = uc.Chrome(use_subprocess=True, options=options)

driver.maximize_window()

#Take the user input to obtain the URL of the website to be scraped, and web scrape the page.
val = "https://www.doordash.com/en-CA/"
wait = WebDriverWait(driver, 10) #10 seconds before timing out
driver.get(val) #loads the web page in the selected browser session
get_url = driver.current_url #get the url of the current page
wait.until(EC.url_to_be(val)) #Calls the method provided with the driver as an argument until the return value does not evaluate to False. EC.url_to_be checks the current url to become the expected URL "val"
if get_url == val:  #ensure that the correct url has been opened
    page_source = driver.page_source # get the entire HTML source code of a webpage as a string


driver.implicitly_wait(120)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

element= driver.find_element(By.CSS_SELECTOR, "input[class='Input__InputContent-sc-1o75rg4-3 froUFe']")
element.send_keys("")
time.sleep(3)
element.send_keys(Keys.RETURN)

driver.implicitly_wait(130)
time.sleep(3)

element= driver.find_element(By.CSS_SELECTOR, "input[class='Input__InputContent-sc-1o75rg4-3 froUFe']")
element.send_keys("Korean Garden")
time.sleep(3)
element.send_keys(Keys.RETURN)
driver.implicitly_wait(120)

restaurant_container= driver.find_element(By.XPATH,"//div[@data-anchor-id='StoreLayoutListContainer']")

def checkIfClosed():
        try:
            exitButton = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Close the \"this store is closed\" modal']")
            if exitButton:
                 exitButton.click()
        except NoSuchElementException:
            pass

try:
    restaurant= restaurant_container.find_element(By.XPATH, ".//span[@data-telemetry-id='store.name' and contains(text(), 'Korean Garden')]") #stores all shown restaurant names
    restaurant.click()
    driver.implicitly_wait(120)
    time.sleep(5)
    #exit out of the currently closed notif
    checkIfClosed()

    driver.implicitly_wait(120)
    #going to placed into its own function 
   
    menu_container=  driver.find_element(By.XPATH, "//div[@data-anchor-id='MenuItem']")
    menu = menu_container.find_element(By.XPATH,"//button[contains(@aria-label, 'House Roll')]")
    price= re.search(r'\$(\d+\.\d+)', menu.text).group(1)
    print(price)

except NoSuchElementException:
    print("Restaurant not found.")


#driver.close()
