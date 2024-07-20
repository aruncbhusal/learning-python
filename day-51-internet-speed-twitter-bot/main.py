# In today's lesson, we'll be driving two apps, one is speedtest.net and another
# is twitter, and if the internet speed is less than what was promised, the twitter
# bot sends a tweet with the observed speed and expected speed

# Import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# First we need to define a few constants, like the expected speed for the internet
PROMISED_DOWN = 200
PROMISED_UP = 200
TWITTER_USERNAME = "<TWITTER_USERNAME>"
TWITTER_PASS = "<TWITTER_PASSWORD>"

# X usually asks for user authentication for login so if that happens this time as well,
# I'm basically screwed. We have Elon Musk to thank for that
# Anyway, first we need to simulate the speedtest.net website and find out our speeds

# The project suggests using a class since the structure can get a bit complex while
# having to use multiple drivers for the two purposes. So we'll do that

class InternetSpeedBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        
        self.driver = webdriver.Chrome(options = chrome_options)
        self.up = 0
        self.down = 0
    
    def get_internet_speed(self):
        self.driver.get("https://speedtest.net")
        time.sleep(2)
        start_btn = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start_btn.click()
        while(True):
            time.sleep(10)
            try:
                res_label = self.driver.find_element(By.CSS_SELECTOR, 'div[class="result-data"] a')
                if res_label.text == "":
                    raise TypeError
            except:
                continue
            else:
                print(f"FOund at Result ID: {res_label.text}")
                break
            # This will ensure the program will only continue once the result page has loaded
        self.down = float(self.driver.find_element(By.CSS_SELECTOR, ".result-data .download-speed").text)
        self.up = float(self.driver.find_element(By.CSS_SELECTOR, ".result-data .upload-speed").text)
        # print(self.down)
        # print(self.up)
        # Okay the code for this section is complete, now on to the actual hard part: Twitter/X
        # self.driver.close()
        
    def tweet_at_isp(self):
        # This segment is not hard because coding here is hard, but it's because of the darned
        # authentication that X forces me to do
        self.driver.get("https://www.x.com")
        time.sleep(2)
        # Let me first get rid of the "Welcome to X" at the bottom
        close_welcome = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="xMigrationBottomBar"]')
        close_welcome.click()
        time.sleep(0.5)
        # Now let's press the login button
        signin_btn = self.driver.find_element(By.CSS_SELECTOR, 'a[data-testid="loginButton"]')
        signin_btn.click()
        time.sleep(5)
        # Now the class format in X looks script generated too so unless I use XPath, the only
        # option I have is to make cheeky choices of CSS selectors
        # For the username field:
        enter_username = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
        enter_username.send_keys(TWITTER_USERNAME, Keys.ENTER)
        time.sleep(3)
        # For the password, we need to wait for another page, so in this page for pass:
        enter_pass = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        enter_pass.send_keys(TWITTER_PASS, Keys.ENTER)
        time.sleep(5)
        while(True):
            try:
                # If in 5 seconds, the twitter homepage hasn't opened, it would mean there was an
                # authentication check, so we'll allow some time to complete the authentication
                # We'll do this by trying to find the "message" element which will certainly only
                # appear once the user has entered the homepage:
                self.driver.find_element(By.CSS_SELECTOR, 'a[href="/messages"]')
            except:
                time.sleep(10)
                # We will let 10 more seconds of time to pass before trying to check again
            else:
                break
        # Now I can still see the Welcome to X button so since that may or may not appear, I'll
        # need exception handling again in case it doesn't appear
        close_welcome = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="xMigrationBottomBar"]')
        close_welcome.click()
        
        # Now let's try to access the tweet box:
        input_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0RichTextInputContainer"]')
        input_box.click()
        time.sleep(0.5)
        # Now finally the input box will show an option to enter some data
        input_box = self.driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
        input_box.send_keys(f"Hey (ISP) why is my internet speed {self.down} down / {self.up} up"
                            f" when it should be {PROMISED_DOWN} down/{PROMISED_UP} up?")
        # Now to press the "post" button
        post_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="tweetButtonInline"]')
        post_btn.click()
        # self.driver.close()
    
internet_bot = InternetSpeedBot()
internet_bot.get_internet_speed()
internet_bot.tweet_at_isp()
# Now that I have created the structure for the class as well as defined the calling functions,
# I should now add the functionalities to each method