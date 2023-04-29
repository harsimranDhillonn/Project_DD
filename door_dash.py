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
from main import Main

class Door_dash:
    def run(self):
        #specify the complete path to the Google Chrome binary.
        options = Options()
        options= uc.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
        driver = uc.Chrome(use_subprocess=True, options=options)

        driver.maximize_window()

        #Take the user input to obtain the URL of the website to be scraped, and web scrape the page.
        VAL= "https://www.doordash.com/en-CA/"
        wait = WebDriverWait(driver, 10) #10 seconds before timing out
        driver.get(VAL) #loads the web page in the selected browser session
        get_url = driver.current_url #get the url of the current page
        wait.until(EC.url_to_be(VAL)) #Calls the method provided with the driver as an argument until the return value does not evaluate to False. EC.url_to_be checks the current url to become the expected URL "val"
        if get_url == VAL:  #ensure that the correct url has been opened
            page_source = driver.page_source # get the entire HTML source code of a webpage as a string


        driver.implicitly_wait(120)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

        element= driver.find_element(By.CSS_SELECTOR, "input[class='Input__InputContent-sc-1o75rg4-3 froUFe']")
        element.send_keys(Main.user_address)
        time.sleep(3)
        element.send_keys(Keys.RETURN)

        driver.implicitly_wait(130)
        time.sleep(3)

        element= driver.find_element(By.CSS_SELECTOR, "input[class='Input__InputContent-sc-1o75rg4-3 froUFe']")
        element.send_keys(Main.requested_restaurant)
        time.sleep(3)
        element.send_keys(Keys.RETURN)
        driver.implicitly_wait(120)


        def check_if_closed():
            """
            Docstring
            """
            try:
                exit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Close the \"this store is closed\" modal']")
                if exit_button.is_displayed():
                    exit_button.click()
            except NoSuchElementException:
                pass

        try:
            restaurant_container=driver.find_element(By.XPATH,"//div[@data-anchor-id='StoreLayoutListContainer']")
            restaurant= restaurant_container.find_element(By.XPATH, f".//span[@data-telemetry-id='store.name' and contains(text(), '{requested_restaurant}')]") #stores all shown restaurant names
            restaurant.click()
            driver.implicitly_wait(120)
            time.sleep(5)
            #exit out of the currently closed notif
            check_if_closed()
            #going to placed into its own function
            menu_container=  driver.find_element(By.XPATH, "//div[@data-anchor-id='MenuItem']")
            menu = menu_container.find_element(By.XPATH, f"//button[contains(@aria-label, '{Main.requested_food_item}')]")
            price= re.search(r'\$(\d+\.\d+)', menu.text).group(1)
            print(price)

        except NoSuchElementException:
            print("Restaurant not found.")
            
        driver.close()
