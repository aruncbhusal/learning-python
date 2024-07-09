# Today is a DIY project, with hints of course. This time we'll be using APIs
# that make use of Natural Language Processing. Exciting day
# The project for today is a Workout Tracker Program in which after a workout session
# we can just open the program and use natural language to input our data for the
# day, and the data will be structured and filled to a Google Sheets document from it

import requests
import datetime
# The first API we'll be working with is Nutritionix. Let's get its keys first:
NUTRI_APP_ID = "<APP_ID>"
NUTRI_APP_KEY = "<APP_KEY>"

SHEETY_UID = "<USER_ID>"
SHEETY_KEY = "<SERIAL_KEY>"
# Apparently, a company called "Syndigo" acquired Nutritionix and the docs can be found at
# https://docx.syndigo.com/developers
# I made a copy of the starting Google Sheets, which has one entry, with the columns:
# Date, Time, Exercise, Duration, Calories
# Now for authentication, we only have the option of headers, and since they are better:
nutri_headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_APP_KEY,
    # I had faced a 401 error but I was pretty sure I had the correct keys as I ccopied them
    # straight from the site, but realized the header had "x-app-key" not "x-api-key" 🤦‍♂️
}
# The possible error codes for this API are 400(Validation error),401(Unauth),403,404,409,500
# There are multiple endpoint options provided, like Instant, Search-Item for search functions
# The other two are Natural Language for Nutrients and Exercise, we'll be working with the latter

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# This is divided into the host domain and the endpoint parts, everything before /v2/.. is the host

# For the parameters, we'll be taking a string input.
nutri_body = {
    "query": input("What exercises did you do today? "),
    # "query": "I ran 4 miles today and swam 2.5 kms"
    # There are other parameters too, like height weight and age, but those aren't of our concern
}

response = requests.post(url= nutri_endpoint, json= nutri_body, headers= nutri_headers)
# I was getting a 400 error here, and realized the "params" I was passing should have been json
# I'm debugging without external aid, self pat on the back.
response.raise_for_status()
exercises = response.json()["exercises"]

# Let's first see what the response is like, though it's given in the docs too, I have to test it
# Okay let's see the useful data relevant to the ones to be put in the sheet in here:
# Using JSONviewer, I can see a key "exercises" that contains a list value, which will have a data
# for individual columns of the sheet, so I guess it's useful to just get that single key out to
# start with. Then we have "name" which can be filled in the Exercise column,
# "duration_min" can be filled in Duration, since we don't have distance, we don't need to worry
# Finally "nf_calories" can be entered in the calories field. Good going so far

# Let's also use the datetime module to fetch today's date in the format used in the Sheets example
# dd/mm/yy will have to use strftime() method probably
now = datetime.datetime.now()
today_f = now.strftime("%d/%m/%Y")
now_f = now.strftime("%H:%M:%S")
# %I is used for hour in the 12 hour format, %H gives it in 24 hr format

for exercise in exercises:
    # Now we have to work with the Sheety API, where I have connected to my Google Account, where 
    # the sheets is located in. The API Key seems embedded in the endpoint though.
    # (Retrospection: The API Key seems to be the User ID and not the API Key)
            # sheety_endpoint = f"https://api.sheety.co/{SHEETY_KEY}/myWorkouts/workouts"
    # Weird way to use an API, with no parameters and such transparent "authentication" but ok
    # Initially only the GET request was turned on in the config page so I had to enable the
    # POST request as well, since that is the only thing we'll be doing here, we're just gonna
    # visit the sheet if we want to see the changes we've made. It's nice that they gave us the
    # feature to turn off individual requests, like by disabling PUT and DELETE, I can be sure
    # my data won't be changed, even if more random data might be added using PUT
    # Ok after reading the docs I realized no authentication was just the default setting, since
    # by default, the only request available is GET() and unless there is some sensitive data,
    # basic authentication should fare not too bad.
    # But it has other authentication methods as well, like basic and bearer
    # The basic method has username and password which will be base64 encoded into the auth header
    # and bearer uses just one "secret" key which can be sent in the header instead
    # So after "updating" my key to a random string, this is the new endpoint:
    sheety_endpoint = f"https://api.sheety.co/{SHEETY_UID}/myWorkouts/workouts"
    sheety_header = {
        "Content-Type": "application/json",
        # From the sheety docs, this was suggested
        "Authorization": SHEETY_KEY,
    }
    sheety_body = {
        # I was facing a 400 error just leaving it like this and by looking at the docs I found out
        # we must nest all our records inside a key that has the name of our sheet:
        "workout":{
        # What is wrong with this API?? The sheet name in the URL is "workouts" and I'm supposed to
        # use "workout" here?? Wasted a lot of my time just debugging this stupid implementation
            "date": today_f,
            "time": now_f,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    
    # Now let's create a POST request and see how it goes
    response = requests.post(url= sheety_endpoint, headers= sheety_header, json= sheety_body)
    response.raise_for_status()
    print(response.text)
    # The docs for this API are a joke! What even am I supposed to expect as a response, and it didn't
    # even do its thing and whatt
    # Now I'm gonna try the final act of using camelCase instead of capitalized first letters even
    # though in my sheets they are capitalized, let's see if it works
    # Oh it did... Do I say it was stupid of me to not trust the docs or blame the docs for not telling
    # me that a difference in the case in the sheets and the keys was okay. SMH

# I guess that's the entire project!
# Finally the task was to add the API Keys and Authentication Tokens into the Environment Variablaes
# That way even when hosting our code on sites like Replit, we can make sure our code(which is public)
# does not give away our "secret" API keys and tokens
# Since in Windows, the only way to add a permanent environment variable is by going into system settings
# I will not be doing this task
# But on Mac/Linux, environment variables can be added using "export <VAR_NAME>=<VALUE>"
# There shouldn't be any spaces in the assignment. They can be later accessed using the os module
# os.environ.get(<VAR_NAME>) will give the value held by an environment variable, since the os.environ
# returns a dict type object. They can then be used for sharing the code publicly.
# Meanwhile I'll just redact the sensitive bits of the code instead.
# That's it for today, short project but took me a long while due to the mess of a documentation from Sheety 