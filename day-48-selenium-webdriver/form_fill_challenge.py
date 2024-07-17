# This challenge involves going to a test website and filling the form there
# We will be using the webdriver keys class here as well

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# In the page, there are three input fields with individual names
# Let's fill each with relevant data first

fname_box = driver.find_element(By.NAME, "fName")
# It is necessary to be careful about case sensitivity of the locator string
fname_box.send_keys("random_name")

lname_box = driver.find_element(By.NAME, "lName")
lname_box.send_keys("random_surname")

email_box = driver.find_element(By.NAME, "email")
email_box.send_keys("hehe@huhu.com")
# We can use the following to just press enter after entering everything:
            # email_box.send_keys("hehe@huhu.com", Keys.ENTER)
# But let's try something else

# Now instead of pressing Enter, let's try to click the Sign Up button
signup_btn = driver.find_element(By.CSS_SELECTOR, ".form-signin button")
signup_btn.click()

driver.close()