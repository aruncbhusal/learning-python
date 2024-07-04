# Code that was already present in the starting file:
# 1. Declaration for my latitude and longitude
# 2. Retrival of ISS Latitude and Longitude from the ISS API
# 3. Set up of parameters for the Sunrise Sunset API apart from time zone
# 4. Retrieval of sunrise and sunset times from the API
# 5. Type conversion of lat/long and sunrise/sunset times to float and int respectively

import requests
from datetime import datetime
# Since I have to send an email I need the smtplib module
import smtplib
import time

MY_LAT = 27.704291
MY_LONG = 85.322768

# I had forgotten the data would only be generated once for the entire program execution so
# since I needed to check for the status every time the while loop was running, I had to
# wrap individual elements into their own functions then call them whenever necessary so that
# I could get fresh data to check for each time
# It's a shame I only realized that after sending three emails and noticing that the coordinates
# of the ISS for all three emails were exactly the same

# def get_iss_coords():
# This function extracted the current co ordinates of the ISS, but after seeing that
# is_night() was used to check for night time in the course, I believe this should also be made
# a single function rather than splitting and dealing with a global variable    

# Your position is within +5 or -5 degrees of the ISS position.
# Let's create a fuunction that checks for this:
def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    lat_diff = iss_latitude - MY_LAT
    long_diff = iss_longitude - MY_LONG
    if lat_diff >= -5 and long_diff >= -5 and lat_diff <= 5 and long_diff <= 5:
        # I was today years old when I found out we can also do:
        # if -5 <= lat_diff <= 5 and -5 <= long_diff <= :
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Kathmandu"
}

# def get_rise_set_time():
# In the course, a function "is_night()" returns true by doing all the comparisons within
# itself, so that we don't need to worry about it in the actual loop. Why didn't I think of that?
# Anyways, I will shift the code from this function to the new is_night function as well, so yeah

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # I don't want to have to deal with global variables anymore
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if (time_now.hour >= sunset or time_now.hour <= sunrise):
        return True
    else:
        return False
    


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# It's probably necessary to have my email credentials before I start with the code process
my_email = "<email>@gmail.com"
my_pass = "<pass>"
second_mail = "<email2>@outlook.com"

# Let's create a while loop to get this done. Since the code will run continuously, we will
# need a while True loop
while True:
    if is_night() and is_close():
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user = my_email, password = my_pass)
            connection.sendmail(from_addr = my_email, to_addrs = second_mail,
                                msg = "Subject:Look up!\n\n"
                                "The ISS is overhead, have a look.")
            # In my initial code, I had a feature to attach the ISS location every time the mail
            # was sent, but since the co ordinates are now local variables, I can't do that anymore
            print("done")
    # Now to run it every 60 seconds, maybe I should add a time delay:
    time.sleep(60)