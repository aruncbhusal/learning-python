# This is the final challenge for the day, where we have to automate a game.
# The goal in this game to to maximize our cookied per second.
# There was supposed to be a solution video but since I don't have the soln
# I'll have to rely on my own skills to see it through to the end

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# To schedule the shop test and game end
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# We don't need to close this as we close it on our own accord
# Let's get the elements and start from there
cookie = driver.find_element(By.ID, "cookie")
item_tags = [item.get_attribute("id") for item in driver.find_elements(By.CSS_SELECTOR, "#store div")]

# First let's set up an infinite loop to decide ourselves when to quit
# According to the course, we need to stop the game after 5 mins
# So from a StackOverflow question given int the solution html,
# https://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-n-amount-of-time
# I found out how I can time a certain thing using the time module
end_time = time.time() + 60*5
five_sec_later = time.time() + 5
while(time.time()<end_time):
    cookie.click()
    # This will click the cookie forever
    # But we need to add upgrades as a feature as well
    # The idea was to check the store every 5 seconds and make the most expensive upgrade available
    if (time.time() >= five_sec_later):
        # We need to compare our money with the sore items now
        # Let's get our cookie currency value
        money_now = int("".join(driver.find_element(By.ID, "money").text.split(",")))
        # Now we need to get the upgrades/store items as well
        # Since we need to click at the div, it's better to keep this here
        # Now we need to click at the highest one that we can buy right now
        # I can see there'a a class called "grayed" which is on when we can't buy the item yet
        # What if I iterate from the end and click at the first item which isn't grayed
        # for idx in range(-1,-len(store_items)-1,-1):
            # if store_items[idx].get_attribute("class") != "grayed":
            #     store_items[idx].click()
            #     break
            # Even though the above code might work, I wouldn't be making use of the money value
            # So I'll need to calculate the difference and select the smallest number that way instead
            # Well it works, but now I got to figure out a way to make it work using the money and not
            # the class name
            
            # Inside the div, there is a <b> tag which contains a number with a string, let me print
            # ans see the result first
            # price_text = store_items[idx].find_element(By.TAG_NAME, "b").text
            # if price_text != "":
            #     this_item_price = int("".join(price_text.split(" ")[-1].split(",")))
            # One of the prices appeared empty so I had to remove it
            # Okay looks like I'm in luck, and they are separated by spaces, and numbers are in a
            # comma separated format, so all I need to do is get the int values and compare
            # Wow that is a long line of code
            # store_items[idx].click()
            # print("Clicked!")
            # break
            # Looks like in this method, the max value might not be selected, so I'll have to
            # resort to using multiple lists and for loops instead
        
        affordable_upgrades = []
        affordable_prices = []
        for item in driver.find_elements(By.CSS_SELECTOR, "#store>div"):
            price_text = item.find_element(By.TAG_NAME, "b").text
            # Okay since the div contains another div as well, it might be added too
            # So we need to make a distinction by only taking ids
            if price_text != "":
                this_item_price = int("".join(price_text.split(" ")[-1].split(",")))
            if this_item_price <= money_now:
                affordable_upgrades.append(item)
                affordable_prices.append(this_item_price)
        
        affordable_upgrades[affordable_prices.index(max(affordable_prices))].click()          
        
        five_sec_later = time.time()+5
        # This should work

print(f"Cookies per second finally: {driver.find_element(By.ID, "cps").split(" ")[-1]}")