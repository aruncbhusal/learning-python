# The task for today is a program that can automatically follow the followers of a particular
# profile, with no interaction from our side
# I wanted to sign up for a new account but since Instagram servers aren't letting that happen,
# I'll have to deal with my own account for this

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

FACEBOOK_EMAIL = "<YOUR_FB_EMAIL>"
FACEBOOK_PASS = "<YOUR_FB_PASS>"

# Let's say we wanted to follow from the follower list of Leo Messi
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://instagram.com/leomessi")

# Now we want to log in to our account from this, so we will click on Log In
time.sleep(5)
login_link = driver.find_element(By.LINK_TEXT, "Log in")
login_link.click()

time.sleep(1)
# Now the login with facebook button was hard to get so we'll use XPATH
login_w_fb = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[5]/button')
login_w_fb.click()

time.sleep(2)
# Now to login with Facebook
email_box = driver.find_element(By.ID, "email")
email_box.send_keys(FACEBOOK_EMAIL)

pass_box = driver.find_element(By.ID, "pass")
pass_box.send_keys(FACEBOOK_PASS)

login_btn = driver.find_element(By.ID, "loginbutton")
login_btn.click()

# Now this process might take some time so we'll need to add a long delay
time.sleep(20)

# For the link to followers, I will need to use XPATH
followers = driver.find_element(By.CSS_SELECTOR, 'a[href*="followers"]')
followers.click()
# Apparently we can use:
# button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Click me')]")
# to locate stuff that may not be easily accessible with a XPATH

time.sleep(5)
# Since the follow buttons are all packaged as buttons inside the div with role dialog
follow_btns = driver.find_elements(By.CSS_SELECTOR, 'div[role="dialog"] button')
for button in follow_btns[1:]:
    # The first button was a close button, I failed to have noticed that
    # print(len(follow_btns))
    time.sleep(1)
    button.click()

driver.quit()
# Well I completed today's project without having to rely on the course resources at all
# A sign of me improving probably. And it helps that today's project was a bit short
# since I don't think I can stay up much today.