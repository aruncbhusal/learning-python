# In today's lessons, the topics covered are API Keys, Authentication and Environment Variables
# Not all APIs are free. Some APIs provide simple data and are readily accessible, but some
# API providers spend money to generate the data for the API, so they wouldn't give it to us
# for free. Even if they would, they would want to limit the API usage(calls) so that they don't
# lose out money. They are basically selling the data that they have.
# Most API providers provide a free tier, and we can sign up to their service to get an API Key
# This API key is a way to authenticate and identify a user. This allows an API provider to
# monitor, manage and limit the usage of API from a certain API key holder.

# First we will be using the OpenWeatherMap API to find out about the weather of our city
# The main project for today is an app that sends us an SMS if it is going to rain today, with
# a suggestion to carry an umbrella. The first step is to find the weather ofcourse

# I created an account on OpenWeatherMap and generated an API key, which I can use as a parameter
# to access their API. It is necessary to read the documentation of any site, when trying to use
# their API, there might be things that will not work until you comply with their structure
# In case of OpenWeatherMap, we can create as many API keys as we want, with a name to identify each
# So if multiple people shared the same free account, they would be under a common usage constraint

my_api_key = '<OWM_API_KEY>'
# Now to test the API Key, I will use it in the browser first and see the result
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# This is the URL suggested to check the current weather in the docs of the API

# Anyway, the first task was to use the API key and the 5 day 3 hr forecast from the website to
# get the weather data for 3 hr intervals for our location, since the parameters includes a
# latitude and longitude, I will have to use latlong to get that for Kathmandu

import requests

# let's set up a parameter dictionary to feed to the API
parameters = {
    "lat" : 27.717245,
    "lon" : 85.323959,
    "appid" : my_api_key,
    "cnt": 4
}
# I created a new API key but it didn't work so I have to keep using the default one for the time being

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
# This is the URL we're working with

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status()
# A 401 (Unauthorized) error usually means something is wrong with our API Key
                    # data = response.json()
# Let's first take a look at the data format in the browser, then make use of the data to show
# only the relevant information
# There are 1552 lines 😭
# So basically the json has a list called "list" which has dictionaries, each of which contain a
# "dt" which is basically the UNIX time. In each dictionary, there are multiple dictionaries like
# "weather", "clouds", "wind", and other key value pairs. One in particular that interested me is
# the "dt_txt" which has the current date time in a familiar datetime module like fashion. So maybe
# I can iterate through that list and print the weather condition only for that particular 3hr time?
data = response.json()
# We can use an online JSON viewer like https://jsonviewer.stack.hu/ to see the contents to see the contents
# The UNIX time is number of seconds that has passed since January 1, 1970
                    # for weatherinfo in data["list"]:
                    #     date_time = weatherinfo["dt_txt"]
                    #     print(f"\nDate/Time: {date_time}")
                    #     weather_main = weatherinfo["weather"][0]["main"]
                    #     weather_desc = weatherinfo["weather"][0]["description"]
                    #     # Oh weather is a list that contains a single dictionary? Great!
                    #     print(f"Weather description: {weather_main} : {weather_desc}")
                    #     # Seems like the temperature is in Kelvin so celsius must be easy
                    #     temp = weatherinfo["main"]["temp"]
                    #     print(f"Temperature: {temp} Celsius\n")
                    #     # I wonder why when I tried to use the dictionary access inside
                    #     # the f-string it gave me syntax error
                    #     # Ok success, took quite a while
                    
# The next challenge now is to get the weather conditions for the next 12 hours (4 data) check if it
# will rain. If it does, we need to print "Bring an umbrella."
# Testing this code would be hard if it weren't monsoon right now so just in time while it's raining out
# On reading the documentation, we can see that we can set a parameter called "cnt" that gives us the
# data only for the specified number of counts, so our list would be smaller and more manageable
# Let's update the parameters and get going.
# If it weren't raining here, we could go to https://www.ventusky.com/ to find a place that was surely
# going to rain, to see if our code would work. But it's definitely raining in Kathmandu soo...

# it is good to use a json viewer to see how we can access the data inside the json
# Inside the JSON, inside the "list" key, in the ith index, in the "weather" key, in the ith index,
# in the "id" key, we can find the weather id, which if less than 700 means some form of precipitation
# Code descriptions: https://openweathermap.org/weather-conditions
will_rain = False
# Why print more than once when you can stop once printed
for weatherdata in data["list"]:
    # The same place can have thunderstorms and snow at the same time, which means there can be more
    # then one items in the "weather" list. We can choose to check that, I think that would be foolproof
    for individual_items in weatherdata["weather"]:
        if int(individual_items["id"])<700:
            print("Bring an umbrella")
            will_rain = True
            break
    if will_rain:
        break
# Since multiple weather info for each hour is rare, I could've avoided using two loops and instead done:
                # for weatherdata in data["list"]:
                #     if int(weatherdata["weather"][0]["id"])<700:
                #         print("Bring an umbrella")
                #         break
# This way, I don't need to go out of my way and create a brand new variable to break out of two loops
# In the course, instead of using break, a variable was created to store a bool of will_rain and once
# out of the loop, if the variable is true, print bring an umbrella. Maybe I got too ahead of myself...

# Well, guess a will_rain was necessary after all. I mean we could skip it and send the SMS inside the
# if statement, but I'd rather not do it inside the for loop, messy code should be avoided
# Anyway, to use the SMS service, I had to sign up to Twilio with my own email and own phone number so that
# it would give me a free trial with about $15 worth of credits to use in the trial.
# I got a default Twilio phone number that can now send SMS to my verified number
# And I have an Account SID, and an Auth Token
from twilio.rest import Client
# To use this API, I need to install the twilio module

phone_no = "<PHONE_NUMBER_FROM_TWILIO>"
acc_sid = "<ACCOUNT_SID>"
my_auth_token = "<AUTH_TOKEN>"
own_phone_number = "<PERSONAL_PH_NO>"

# From the twilio console where it gives basic instructions on messaging, I copied their sample code
# and now I will customize it inside this if block to do what I want it to do

if will_rain:
    account_sid = acc_sid
    auth_token = my_auth_token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_= phone_no,
    body = "It will rain today, take an ☔",
    to= own_phone_number
    )

# print(message.status)
# Let's try sending a message then
# Well on the console it says delivered, and it has deducted credits, but I didn't receive it
# Might take a while. let's continue
# Also how expensive is this thing? I sent two messages and it got me from $15.50 to $13.9
# Rs 100+ to send a single message? Wow

# I would've gone and tried on PythonAnywhere if this had worked but since it didn't I'll just
# summarize what I learned from that video:
# The free PythonAnywhere account provides us with a proxy server instead of a dedicated one so
# we need to use the TwilioHttpClient to make it work. To send the message, we need to let the
# Twilio servers know about the proxy server I'm working with, and then only the servers will be
# able to send the message.
# Then we can schedule the task with a bash command: "python3 main.py" or whatever the name is
# on a UTC time every day. PythonAnywhere has an expiry date for commands on the free accounts
# and we can only schedule a single task per day. I haven't seen a dire need to create an account
# so until then, let's just keep learning and not implementing.

# Finally, the environment variables.
# These are sort of variables that contain strings which can be separated out from the code
# we are using, so that we can switch them up without chaning the code at all, or protect
# our sensitive data from leaking out by not storing them in the same place as our code
# We can see our environment variables using "dir Env:" in the Windows terminal, or just
# "env" on Linux/Mac . To add a value to the environment variables, we can use the command
# "export <Environment Variable Name> = "<Value" " in the bash terminal to store an env variable
# Then we can access it by using the OS module

import os
print(os.environ.get("USERNAME"))
# The above usage returns my username (Username for this PC that I had set up in the past)

# In order to use environment variables, we can set up a script that runs when we want to
# run our program. Our program itself will only contain the os.environ.get() statement that
# will retrieve the key but the key needs to be in the environment first, so we can put lines
# of code before, each with their own "export" commands, that will set up the environment vars
# which can be later retrieved and used, without them being a part of the actual code to be run
# While writing all in one line, we can use semicolons to separate multiple terminal commands.

# For other fun APIs, we can take a look at https://apilist.fun