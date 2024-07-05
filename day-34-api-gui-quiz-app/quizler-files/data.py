# In this file, there was a question_data list of dictionaries that contained 10 questions
# copied from the JSON from the OpenTrivia API. The current code has the same list but it
# contains data directly obtained from the API, with fresh questions each time, rather than
# the same 10 questions on every run. This was the first step, before making the app GUI

# The API url given in OpenTrivia: https://opentdb.com/api.php?amount=10&type=boolean
# Let's break it down to extract what we need
import requests
import json

parameters = {
    "amount" : 10,
    "type" : "boolean"
}

response = requests.get(url = "https://opentdb.com/api.php", params = parameters)
response.raise_for_status()
# The list of dictionaries is inside the key "results" so let's extract the question data
question_data = response.json()['results']
# Okay now the quiz works as expected, with fresh questions each time the game starts