import shared
from main import Main

#specify the complete path to the Google Chrome binary.
options = shared.Options()
options= shared.uc.ChromeOptions()
options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
driver = shared.uc.Chrome(use_subprocess=True, options=options)
driver.maximize_window()

#Take the user input to obtain the URL of the website to be scraped, and web scrape the page.
VAL= "https://www.ubereats.com/ca/near-me"
wait = shared.WebDriverWait(driver, 10) #10 seconds before timing out
driver.get(VAL) #loads the web page in the selected browser session
get_url = driver.current_url #get the url of the current page
wait.until(shared.EC.url_to_be(VAL)) #EC.url_to_be checks the current url to become the expected URL "val"
if get_url == VAL:  #ensure that the correct url has been opened
    page_source = driver.page_source # get the entire HTML source code of a webpage as a string

driver.implicitly_wait(120)
driver.switch_to.window(driver.window_handles[0])
shared.time.sleep(3)

element= driver.find_element(shared.By.CSS_SELECTOR, "input[aria-controls='location-typeahead-home-menu']")
element.send_keys(user_address)
shared.time.sleep(3)
element.send_keys(shared.Keys.RETURN)

driver.implicitly_wait(130)
shared.time.sleep(3)

element= driver.find_element(shared.By.CSS_SELECTOR, "input[aria-controls='search-suggestions-typeahead-menu']")
element.send_keys(requested_restaurant)
shared.time.sleep(3)
element.send_keys(shared.Keys.RETURN)
driver.implicitly_wait(120)


try:
    restaurant_container = driver.find_element(shared.By.XPATH, "//div[@data-testid='store-card']")
    restaurant = restaurant_container.find_element(shared.By.XPATH, f".//h3[contains(text(), '{requested_restaurant}')]")
    restaurant.click()
    driver.implicitly_wait(120)
    shared.time.sleep(5)

    price_element = driver.find_element(shared.By.XPATH, "//span[contains(text(), '$') and contains(text(), 'Delivery Fee')]")
    if price_element is not None:
        price = price_element.text.split()[-3]
        print("\n\tUber Eats' Delivery fee:" + price)
    else:
        print("\n\tUber Eats' Delivery fee: Restaurant is closed on Uber Eats")
    
except shared.NoSuchElementException:
    print("Restaurant not found.")
