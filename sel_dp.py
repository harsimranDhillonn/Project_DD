from selenium import webdriver # to obtain the ChromeDriver compatible with the version of the browser being used

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC #provides a set of predefined conditions that can be used to wait for specific events to occur on a webpage.

from bs4 import BeautifulSoup #BeautifulSoup is needed as an HTML parser, to parse the HTML content that is scraped

import codecs #Codecs are used to write to a text file.

import re #Re is imported in order to use regex to match our keyword

from webdriver_manager.chrome import ChromeDriverManager

#specify the complete path to the Google Chrome binary.
options = Options()
options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)


#driver=webdriver.Chrome(service=Service(ChromeDriverManager().install())) #Obtain the version of ChromeDriver compatible with the browser being used.

#Take the user input to obtain the URL of the website to be scraped, and web scrape the page.
val = input("Enter a url: ")
wait = WebDriverWait(driver, 10) #10 seconds before timing out
driver.get(val) #loads the web page in the selected browser session
get_url = driver.current_url #get the url of the current page
wait.until(EC.url_to_be(val)) #Calls the method provided with the driver as an argument until the return value does not evaluate to False. EC.url_to_be checks the current url to become the expected URL "val"
if get_url == val:  #ensure that the correct url has been opened
    page_source = driver.page_source # get the entire HTML source code of a webpage as a string


#Use BeautifulSoup to parse the HTML content obtained.
#page_source: contains the HTML source code of the webpage that you want to parse.
soup = BeautifulSoup(page_source,features="html.parser") #The "html.parser" is the built-in Python HTML parser.
keyword=input("Enter a keyword to find instances of in the article:")

#find_all() method is used search for all the text elements that match the specified keyword. It returns a list of all the matching text elements, which is assigned to the matches variable.
#re.compile(keyword) is a regular expression that is used to match the keyword.
matches = soup.body.find_all(string=re.compile(keyword))
len_match = len(matches)
title = soup.title.text #the text in the title tag found within the soup object is extracted.


#Store the data collected into a text file.
file=codecs.open('article_scraping.txt', 'a+') #open text file using codes method, name file. mode for opening a file in append mode. In "a+" mode, any data written to the file is automatically added to the end of the file.
file.write(title+"\n") #add the title extracted in line 38 as the title of the txt file
file.write("The following are all instances of your keyword:\n")
count=1
for i in matches:
    file.write(str(count) + "." +  i  + "\n")
    count+=1

file.write("There were "+str(len_match)+" matches found for the keyword.")
file.close()  #close file
driver.quit() #close the browser window that was opened by the web driver.
