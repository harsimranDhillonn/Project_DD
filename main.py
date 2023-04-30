
import shared

def door_dash():
    '''
    Purpose: Using user input, get food item's price and delivery fee from the restaurant on Doordash
    '''
    #specify the complete path to the Google Chrome binary.
    options = shared.Options()
    options= shared.uc.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
    driver = shared.uc.Chrome(use_subprocess=True, options=options)

    driver.maximize_window()

    #URL of the website to be scraped, and web scrape the page.
    VAL= "https://www.doordash.com/en-CA/"
    wait = shared.WebDriverWait(driver, 10) #10 seconds before timing out
    driver.get(VAL) #loads the web page in the selected browser session
    get_url = driver.current_url #get the url of the current page
    wait.until(shared.EC.url_to_be(VAL)) #Calls the method provided with the driver as an argument until the return value does not evaluate to False. EC.url_to_be checks the current url to become the expected URL "val"
    if get_url == VAL:  #ensure that the correct url has been opened
        page_source = driver.page_source # get the entire HTML source code of a webpage as a string

    driver.implicitly_wait(120)
    driver.switch_to.window(driver.window_handles[0])
    shared.time.sleep(3)

    #find search bar to input address for delivery
    element= driver.find_element(shared.By.CSS_SELECTOR, "input[class='Input__InputContent-sc-1o75rg4-3 froUFe']")
    element.send_keys(user_address)
    shared.time.sleep(3)
    element.send_keys(shared.Keys.RETURN)

    driver.implicitly_wait(130)
    shared.time.sleep(3)
    
    #find search to input restaurant's name
    element= driver.find_element(shared.By.CSS_SELECTOR, "input[class='Input__InputContent-sc-1o75rg4-3 froUFe']")
    element.send_keys(requested_restaurant)
    shared.time.sleep(3)
    element.send_keys(shared.Keys.RETURN)
    driver.implicitly_wait(120)

    try:
        #find list of restaurants produced by the previous search for a specific restaurant
        restaurant_container=driver.find_element(shared.By.XPATH,"//div[@data-anchor-id='StoreLayoutListContainer']")
        restaurant= restaurant_container.find_element(shared.By.XPATH, f".//span[@data-telemetry-id='store.name' and contains(text(), '{requested_restaurant}')]") #find the specific restaurant
        restaurant.click() #click on the restaurant
        driver.implicitly_wait(120)
        shared.time.sleep(5)

        #from the list of menu items, find the specified food item by the user
        menu_container=  driver.find_element(shared.By.XPATH, ".//div[@data-anchor-id='MenuItem']")
        menu = menu_container.find_element(shared.By.XPATH, f"//button[contains(@aria-label, '{requested_food_item}')]")
        price= shared.re.search(r'\$(\d+\.\d+)', menu.text).group(1)
        print("\nFood price: $"+price +"\n\tDoorDash Delivery fee: $0 <First time Orders>")

    except shared.NoSuchElementException:
        print("Restaurant not found.")
    driver.close()

def skip_dishes():
    '''
    Purpose: Using user input, get delivery fee from the restaurant on Skip the Dishes
    '''
    options = shared.Options()
    options= shared.uc.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
    driver = shared.uc.Chrome(use_subprocess=True, options=options)
    driver.maximize_window()

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
     
    #find search bar to input address for delivery and enter the address
    element= driver.find_element(shared.By.CSS_SELECTOR, "input[aria-label='Enter Your Address - Use the up and down arrow keys to navigate address suggestions.']")
    element.send_keys(user_address)
    shared.time.sleep(3)
    element.send_keys(shared.Keys.RETURN)
    shared.time.sleep(3)

    #after inputting address click "Find restaurants"
    find_restaurants = driver.find_element(shared.By.CSS_SELECTOR, "button[class*='MuiButton-containedSizeLarge-']")
    find_restaurants.click()
    driver.implicitly_wait(120)

    #find search bar to input restaurant's name
    element= driver.find_element(shared.By.CSS_SELECTOR, "input[placeholder='Search Cuisines, Restaurants, or Items']")
    element.send_keys(requested_restaurant)
    driver.implicitly_wait(120)
    shared.time.sleep(2)
    restaurant_path= driver.find_element(shared.By.CSS_SELECTOR, "span[class='styles__Title-czubko-4 hLParj']")
    
    #get delivery fee and print it otherwise restaurant was not found in the search
    try:
        delivery_element= driver.find_element(shared.By.CSS_SELECTOR, "span[class*='styles__DeliveryFeeText']")
        price_element = delivery_element.find_element(shared.By.XPATH, ".//span[contains(text(), '$')]")
        price = price_element.text
    except IndexError:
        print("Restaurant Not Found")
    else:
        print("\n\tSkip the dishes' Delivery fee: "+ price)
    driver.close()

def uber_eats():
    '''
    Purpose: Using user input, get delivery fee from the restaurant on Uber eats
    '''
    options = shared.Options()
    options= shared.uc.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
    driver = shared.uc.Chrome(use_subprocess=True, options=options)
    driver.maximize_window()

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

    #find search bar to input address for delivery and enter the address
    element= driver.find_element(shared.By.CSS_SELECTOR, "input[aria-controls='location-typeahead-home-menu']")
    element.send_keys(user_address)
    shared.time.sleep(3)
    element.send_keys(shared.Keys.RETURN)
    driver.implicitly_wait(130)
    shared.time.sleep(3)
    #find search bar to input restaurant name for delivery
    element= driver.find_element(shared.By.CSS_SELECTOR, "input[aria-controls='search-suggestions-typeahead-menu']")
    element.send_keys(requested_restaurant)
    shared.time.sleep(3)
    element.send_keys(shared.Keys.RETURN)
    driver.implicitly_wait(120)

    #find the restaurant and get its delivery fee to print otherwise print restaurant is not found or restaurant is closed
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
    driver.close()

'''
Get User input: Address, restaurant, and food item
'''
user_address= input("Please enter where you would like the food to be delivered?")
requested_restaurant= input("Please enter from which restaurant you would like to order food?")
requested_food_item= input("Please enter what food item you would like to order?")
door_dash()
uber_eats()
skip_dishes()

