import shared
from main import Main


#specify the complete path to the Google Chrome binary.
options = shared.Options()
options= shared.uc.ChromeOptions()
options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
driver = shared.uc.Chrome(use_subprocess=True, options=options)
driver.maximize_window()

#Take the user input to obtain the URL of the website to be scraped, and web scrape the page.
VAL= "https://www.skipthedishes.com/"
wait = shared.WebDriverWait(driver, 10) #10 seconds before timing out
driver.get(VAL) #loads the web page in the selected browser session
get_url = driver.current_url #get the url of the current page
wait.until(shared.EC.url_to_be(VAL)) #EC.url_to_be checks the current url to become the expected URL "val"
if get_url == VAL:  #ensure that the correct url has been opened
    page_source = driver.page_source # get the entire HTML source code of a webpage as a string

driver.implicitly_wait(120)
driver.switch_to.window(driver.window_handles[0])
shared.time.sleep(3)

element= driver.find_element(shared.By.CSS_SELECTOR, "input[aria-label='Enter Your Address - Use the up and down arrow keys to navigate address suggestions.']")
element.send_keys(user_address)
shared.time.sleep(3)
element.send_keys(shared.Keys.RETURN)
shared.time.sleep(3)
find_restaurants = driver.find_element(shared.By.CSS_SELECTOR, "button[class*='MuiButton-containedSizeLarge-']")
find_restaurants.click()

driver.implicitly_wait(120)
element= driver.find_element(shared.By.CSS_SELECTOR, "input[placeholder='Search Cuisines, Restaurants, or Items']")
element.send_keys(requested_restaurant)

driver.implicitly_wait(120)
shared.time.sleep(2)

restaurant_path= driver.find_element(shared.By.CSS_SELECTOR, "span[class='styles__Title-czubko-4 hLParj']")
try:
    delivery_element= driver.find_element(shared.By.CSS_SELECTOR, "span[class*='styles__DeliveryFeeText']")
    price_element = delivery_element.find_element(shared.By.XPATH, ".//span[contains(text(), '$')]")
    price = price_element.text
except IndexError:
    print("Restaurant Not Found")
else:
    print("\n\tSkip the dishes' Delivery fee: "+ price)
