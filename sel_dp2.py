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
import sys


#specify the complete path to the Google Chrome binary.
options = Options()
options= uc.ChromeOptions()
options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
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
element.send_keys("82 Huber street")
time.sleep(3)
element.send_keys(Keys.RETURN)

driver.implicitly_wait(120)
time.sleep(3)

driver.close()