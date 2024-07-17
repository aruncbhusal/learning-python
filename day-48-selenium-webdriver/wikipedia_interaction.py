# The next challenge was involving the Wikipedia page
# We have to use the Selenium webdriver to extract data from the Wikipedia homepage
# First let's import the webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By
# For the keyboard keys, we need another package
from selenium.webdriver.common.keys import Keys
# For test
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# First task is to extract the number of articles in Wikipedia
# It is located inside id called "articlecount" in an anchor tag
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
                # print(f"{article_count.text}")
# I found it's easy to confuse while putting the CSS Selector
# I tend to keep putting . instad of # even for an id

# Now how about trying to click on something?
# Since the article_count is a selenium element, we can simply use
                # article_count.click()
# And it will click the link and take us to the stats page for Wikipedia

# Instead of clicking on a web element found this way, we can use specific
# locator for Link Texts which can make searching easier
# We cann simply copy the link text and it will find it and give us the element
# Say we wanted to access the link that says "Wikibooks"
wikibooks_link = driver.find_element(By.LINK_TEXT, "Wikibooks")
                # wikibooks_link.click()
# And voila!

# Now how do we type in the searchbar then?
# We need to first get a hold of the input element for search
# In the course, the search bar appeared itself, but since Wikipedia has revamped
# their UI a bit, the search button seems to be collapsed at first, so I'll need
# to first click the search button, and then only will I get the search bar
search_btn = driver.find_element(By.CSS_SELECTOR, "#p-search a")
search_btn.click()
# Now I think it should work, and yup work it did, though with errors
# I might be able to fix it with a sleep timer, let's check
time.sleep(1)
# Yup, just as I expected, I clicked and then typed too quick, the search bar
# didn't get to properly load, giving me errors, though search was completed
search_bar = driver.find_element(By.NAME, "search")
# Now we need to import another class called Keys from the selenium package
search_bar.send_keys("Science", Keys.ENTER)
# In this way we can type in some words, then use another parameter to specify
# a special keyboard action like shift, tab, and in this case enter

driver.close()