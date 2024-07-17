# In today's lesson we will be working with an advanced web scraping method
# In contrast to BeautifulSoup, we can automate actions like typing and clicking
# in the selenium webdriver, and can be used to automate repititive tasks
# Each browser has its own webdriver but well be using Chrome just like the couse

from selenium import webdriver
# Python Selenium docs: https://selenium-python.readthedocs.io/
from selenium.webdriver.common.by import By

# Let's set up the Chrome options for detatch
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Let's create an instance for the browser first, since we're working with chrome
driver = webdriver.Chrome(options= chrome_options)
# In order to open a website, we can use a familiar get() method
                # driver.get("https://www.youtube.com")
# The page opened but it closed as soon as it finished loading/ program finished
# To prevent this from happening, we need to keep it running (detach it) using options

# Okay lot's of things in the next video, and I'll get them all here
# We can use the selenium webdriver to get elements from the webpage like BeautifulSoup
# But we have the convenience of opening it in our browser instead of sending a request
# so all the headers will have already been sent, and we'll see the data we should
# Let's try to solve yesterday's Amazon problem using Selenium:
                # driver.get("https://www.amazon.de/dp/B082BCLDWW/")
# The price was location in the a-price-whole and a-price-fraction classes, so we use them
# For that, we need to search by class, but we need to import the By class for that
# After importing BY, we can simply use the followings to get the price data:
                # price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
                # price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
                # print(f"The price is ${price_dollar.text}.{price_cents.text}")
# We need to use the text property to get the actual content, otherwise it will return
# a Selenium element instead.
# In just 3 lines, we could do stuff that took so long yesterday. Easy enough
# The usage of these "locators" can be found in the official Selenium docs:
# https://www.selenium.dev/documentation/webdriver/elements/locators/
# It is easier with Selenium than BeautifulSoup when the website has more of JS, React in it

driver.get("https://python.org")
# We can also search by other elements, like "name":
# In the python website, the searchbar has a name attribute with a value q. We can get it:
search_bar = driver.find_element(By.NAME, "q")
print(f"{search_bar.tag_name}")
# The HTML tag name for the search bar is "input"
print(f"{search_bar.get_attribute('placeholder')}")
# This gives the value of the attribute "placeholder" for the search bar

# Similarly the Go button has an ID of submit. so we can use it to get the Go button
go_button = driver.find_element(By.ID, "submit")
print(f"{go_button.tag_name}")
# This will return "button" as it should.

# Now some elements in the page might have no easily identifiable class/id/name. In such cases
# we can use the CSS Selector option, which is a more versatile option
# For example in the Jobs section of the widgets in the website, the link has no class
jobs_link = driver.find_element(By.CSS_SELECTOR, ".jobs-widget a")
print(f"{jobs_link.text}")

# Even if all else fails and there is no way to easily extract an element by selection, we can
# use the XPath method, in which we inspect the particular element then copy its XPath from the
# Chrome inspector, then we can use it to get the exact element easily.
issue_tracker_link = driver.find_element(By.XPATH, '//*[@id="container"]/li[8]/ul/li[2]/a')
# We have to be careful not to use double quotes since the XPath itself has it too
print(f"{issue_tracker_link.text}")

# Next, a challenge which involves the python.org page as well
# We need to create a dictionary which contains 5 items, each having an index of its own as key
# and each index has a dictionary in itself which contains the date and title of the events section
# Upon inspection of the page, I found out that the data lies inside the class event-widget

# Similar to the find_element function, we have its plural counterpart as well, which will give a list
dates = [item.get_attribute("datetime").split("T")[0] for item in driver.find_elements(By.CSS_SELECTOR, ".event-widget time")]
# Since each element has the date in an attribute called 'datetime', we'll use list comprehension
# The date was in the form YYYY-MM-DDTHH:mm:ss... so I had to split by T and get the first element too
                    # print(dates)
# Perfect, similarly, we'll extract the data associated with each date in a list as well
event_list = [item.text for item in driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")]
                    # print(event_list)
# Apparently I missed the fact that the "More" button is also a link inside the widget, so to remove it
# I'll have to be more specific and use the class .menu to get inside the actual menu
# In the course, the specificity is maintained using li instead of the class of ul, which works too

# Now let's get them all in a dictionary
events = {}
for idx in range(len(dates)):
        events[f"{idx}"] = {
            "time": dates[idx],
            "name": event_list[idx],
        }
print(events)
# And done!

# In order to close the tab after program is complete, we use:
driver.close()
# But we can also close the entire browser on completion, using
# driver.quit()
# When using the webdriver, the page will say "Chrome is being controlled by
# automated test software" to let us know that this page is run by the driver