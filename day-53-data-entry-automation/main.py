# Today is a Capstone Project Day, where we put all the things we've learnt over
# the past 10 days or so to the test, with both BeautifulSoup and Selenium
# We will scrape a house/rent price website called Zillow and create a spreadsheet
# So basically a data entry job automated in the project
# But since Zillow as a site may be modified and the scope of the project might
# become larger than anticipated, we are given a static Zillow Clone which we can
# scrape from and fill the data in a Google Forms we can create.
# To scrape data from the Zillow Clone webpage we will use BeautifulSoup
# And to fill the Forms, we will use Selenium

FORMS_LINK = "https://forms.gle/******************"
ZILLOW_CLONE_LINK = "https://appbrewery.github.io/Zillow-Clone/"

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# First let's scrape the data from the clone website
response = requests.get(ZILLOW_CLONE_LINK)
soup = BeautifulSoup(response.text, "html.parser")
# Forgot I needed to add a parser, again

# Since the filters required are already pre applied, we only need to find the
# required elements and parse them accordingly.
# I think I should create a list of dictionaries with property address, price and link
# On second thought, maybe I should have three separate lists since they'll have same indices

# First, the list of property links:
# Oh, I also need to add a list comprehension so that only the text inside the elements will
# be stored instead of the whole element
links = [item.get("href") for item in soup.find_all(name= "a", attrs= {"data-test": "property-card-link"})]
# Some attributes like class and id can be used as kwargs while others like data-*** or name
# can't because of the way code is written, or because 'name' is already another argument
# So we need to use the attrs argument to pass in a dictionary of attributes we need to match

# Now similarly for the addresses and prices
prices = [item.get_text().split("+")[0].split("/")[0] for item in soup.find_all(name= "span", attrs= {"data-test": "property-card-price"})]
# Here instead of using split twice, I could have used a split function defined in the
# "re" module called re.split() which can use multiple delimiters, but since I know it
# that's enough I guess 🤷‍♂️
addresses = [item.get_text().strip() for item in soup.find_all(name= "address", attrs= {"data-test": "property-card-addr"})]

# print(links)
# print(prices)
# print(addresses)
# There appear to be a lot of newlines and white spaces to let's clear them up first
# Link was fine as was, but the prices need to be cleaned since some prices have + and some
# have /mo at the end. We need to get rid of all and only have $price
# Next with addresses, we need to clean up the leading and trailing whitespaces, that is simple

all_items = [links, prices, addresses]
# Maybe having these all in a single list would make it easier to just put them into the inputs
# one-on-one, in just two lines of code (not that three is too many but it's still cooler this way)
# Perfect, finally, we need to now use Selenium to automate the form filling with all this data

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get(FORMS_LINK)
time.sleep(2)

# I don't exactly know how I'm actually supposed to automate the forms since there's nothing that
# can identify the fields to fill, but XPATH is an option. Though I will instead iterate through
# the inputs, since there's only three, and it will also make indexing easier.

for idx in range(len(links)):
    time.sleep(1)
    fields = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"] input')
    # Looks like there were hidden buttons in the page I failed to account for, so just using
    # "input" as the tag to be selected wouldn't work
    # I had these before the loop but since it would return "stale element reference", I had
    # to move them inside so it would get the element each time the page refreshes
    
    # Got to iterate for the whole list
    for jdx in range(len(fields)):
        # I could just have written 3 but meh
        fields[jdx].send_keys(all_items[jdx][idx])
    # Now we need to finish this entry by submitting the form and getting a new one
    submit_btn = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Submit"]')
    submit_btn.click()
    time.sleep(0.5)
    # Now we'll be cheeky with the new form submission button as well
    next_entry = driver.find_element(By.CSS_SELECTOR, 'a[href*="docs"]')
    next_entry.click()

# driver.quit()