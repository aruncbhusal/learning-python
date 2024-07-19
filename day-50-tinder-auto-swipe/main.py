# In today's halfway milestone project, we're building an auto swiper for Tinder
# Since Tinder has a cap of 100 swipes per day, I might not have the best testing
# options available for a single day project, but I'll try

# I will follow the course instructions as usual
# The first step is the login. Let me set up selenium for this project first

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

URL = "https://www.tinder.com"
FACEBOOK_EMAIL = "<YOUR_LOGIN_EMAIL/PHONE>"
FACEBOOK_PASS = "<YOUR_FB_PASS>"
# Since Facebook/Google is the most straightforward option for login, I have used FB
# During login, I don't need to keep verifying my phone number that way, so it becomes
# easier to automate

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Since the website needs permissions to be able to access location and stuff
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.geolocation": 1})

driver = webdriver.Chrome(options= chrome_options)
driver.get(URL)

# First let's decline all cookies. Since the class names look all random, I'll have to
# rely on the XPath to make these actions this time
time.sleep(5)
decline_cookies = driver.find_element(By.XPATH, '//*[@id="q1503199108"]/div/div[2]/div/div/div[1]/div[2]/button')
decline_cookies.click()

# Now the login button too can't be obtained without the XPath it seems
time.sleep(1)
login_btn = driver.find_element(By.XPATH, '//*[@id="q1503199108"]/div/div[1]/div/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')
login_btn.click()

# Why does it feel like there's nothing that can be done without an XPath here
time.sleep(1)
facebook_btn = driver.find_element(By.XPATH, '//*[@id="q-225181968"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_btn.click()

# Now for the facebook login part, there seems to be a bit more ease to things
time.sleep(2)
# But first we need to switch to the newly created window
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
# This will get each window configurations in a variable to be selected later
driver.switch_to.window(fb_window)

fb_email_field = driver.find_element(By.CSS_SELECTOR, "#email_container input")
fb_email_field.send_keys(FACEBOOK_EMAIL)

fb_pass_field = driver.find_element(By.CSS_SELECTOR, "#pass")
fb_pass_field.send_keys(FACEBOOK_PASS, Keys.ENTER)
# I could have used the login button but this feels more convenient to just press enter
# Let me switch back now
driver.switch_to.window(base_window)
time.sleep(5)
# Looks like there might be a captcha in the next step so I'll need to be careful
# and sleep for the right amount of time
try:
    # Here I will try to click the allow location button
    allow_location = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="allow"]')
    allow_location.click()
except NoSuchElementException:
    time.sleep(10)
    # This is for if a verification page pops up instead of the actual swiping page
    allow_location = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="allow"]')
    allow_location.click()

# Now to disable the location settings:
time.sleep(2)
try:
    deny_notifs = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="decline"]>div>div>div')
    deny_notifs.click()
    # To make sure I'm pressing the button at the right spot, I had to narrow it down to the div
    # that contains the text, that way I don't get ElementNotInteractableException
except:
    pass
# Now for the actual swiping:
# The keyboard shortcuts are:
# Left Arrow = Nope, Right Arrow = Like, Up Arrow = Profile, Down Arrow = Close Profile
# Enter = Super Like, Space = Next Photo

time.sleep(4)
like_profile = driver.find_element(By.XPATH, '//*[@id="q1503199108"]/div/div[1]/div/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')
like_profile.click()

while(True):
# Since I'd like to make sure I see all photos, I'll maybe press next photo 10 times
# Then I'll like the profile
# If keyboard shortcuts don't work, I'll have to map to specific buttons instead
# Let's select the first div inside the main tag to make sure keys work
    # time.sleep(2)
    # main_page = driver.find_element(By.CSS_SELECTOR, "body main>div")
    # for _ in range(10):
    #     time.sleep(2)
    #     # main_page.send_keys(Keys.SPACE)
    #     # Since this didn't work, we'll just press on the photo and scroll through
    #     try:
    #         next_photo = driver.find_element(By.XPATH, '//*[@id="q1503199108"]/div/div[1]/div/div/div/main/div/div/div[1]/div/div[2]/div[1]/div[1]/span[1]/div')
    #     except:
    #         break
    # The picture swipe didn't work, so I'll just let myself do it manually and then like it
    # automatically, or just like it without anything else on it
    try:
        time.sleep(4)
        # main_page.send_keys(Keys.ARROW_RIGHT)
        like_profile = driver.find_element(By.XPATH, '//*[@id="q1503199108"]/div/div[1]/div/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button')
        # So in the first swipe, it is in the 3rd div while in subsequent swipes it's in the 4th??
        # I'll just take the first action out and then do this for the rest
        like_profile.click()
    except:
        print("Error!")
        raise

# driver.quit()