# In today's lessons we'll be learning about Advanced Authentication
# and the POST/PUT/DELETE Requests from the requests module
# By the end of the day, I'll have created a habit tracker in which we can
# specify a habit name, and then every day, update it so it shows our progress on
# that day. It will be using and API called pixela
# This will look similar to the GitHub user commit tracker (from what I can see)

import requests
# We'll be working with APIs so we're gonna need this
import datetime

TOKEN = "<USER_TOKEN>"
USER_NAME = "<YOUR_USER_NAME>"
GRAPH_ID = "<GRAPH_NAME>"

# We have used the requests.get() to get a piece of data from an API Endpoint to use
# in our program, but that is not all that APIs have to offer.
# We can send our own data to an API Endpoint using the requests.post() method
# To update said data, we acnn use requests.put() and to delete any such data, we can
# use the requests.delete() method

# From the pixela docs, or their homepage: https://docs.pixe.la/
# We first need to create an account through an API call. To do that we use the post() method
pixela_endpoint = "https://pixe.la/v1/users"

user_info = {
    "token": TOKEN,
    # The token is basically something we can generate ourselves and send it to the endpoint
    # and it will be saved and hashed. This will be associated to our user account and is required
    # Tokens must be 8-128 characters in length so safe to say mine is
    "username": USER_NAME,
    # Just a random username, if unavailable it will generate an error so it's not set in stone
    # until the account is confirmed
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
    # All of these are required stuff we need to give to the endpoint to create our account
}

# Google Docs and other sites have similar APIs too, where we can send our data to be saved or
# processed by the API providers, which we can automate if we want to, or package into our
# own programs/softwares.

# Since this POST request is to create a new account, we only need to run it once. Then we can
# make it inaccessible by commenting or deleting it.
response = requests.post(url= pixela_endpoint, json= user_info)
# In contrast to the get request, we pass a JSON here, notice that all the keys and values in the
# user_info dictionary are strings. That is the typical look of a JSON document.
# We don't pass parameters here since we are the ones giving them data,and it will be a JSON
print(response.text)
# We used to get a hold of the json file, but we won't be doing anything with it, so using .text

# Next step is actually creating a tracking graph for our habits.
# Let's say we want to track how much we ran each day. This needs a new graph to be created in our
# pixela account, and then update it as we add data every day
# From the pixela docs for a new graph, we will have to use a different API endpoint compared to
# what we used when we created the user account
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_info = {
    # In this JSON, we provide details about the graph so that the API Knows how to tailor it
    "id": GRAPH_ID,
    # The id is what will be used to identify our graph, the graph name is just an alias
    # Validation rule: ^[a-z][a-z0-9-]{1,16}
    # This means we can't start with a number, we have to start with an alphabet, then we can
    # tag along any numbers at the end only.
    "name": "Running Tracker",
    # This will set the name for the "pixelation graph"
    "unit": "Kilometre",
    # This is the units of the action we want to track, it can be kilogram, calory, commits, etc
    "type": "float",
    # only int and float types are supported, floats are necessary here for accurate distances
    "color": "sora",
    # shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black)
    # are supported as color kind. Since the app was made by Japanese team, these are the options
    # There are other parts to the request body like isSecret, and timezone, but these are the ones
    # which were required so we'll be working with these only for now
    
    # Notice we don't have any way of identifying the user in the request body.
    # That is because an advanced authentication is used in this case.
}

headers = {
    "X-USER-TOKEN": TOKEN,
    # The headers are separately sent as a part of the request. In the news API, I had noticed that
    # there were three authentication options, one using API Key in the parameters, and the others
    # including the API key as a part of the headers.
    # This method is a lot mor preferred since it it more secure than passing the api key as a param
    # When we use an API key in the parameters it means if anyone has access to what requests we have
    # sent, such as the data from our web browser, they could easily find out and exploit our API Key
    # In order to avoid such a possibility, headers are send as kwargs and not supplied as a part of
    # the parameters that can be seen in the web address of the actual request
}

response = requests.post(url= graph_endpoint, json= graph_info, headers= headers)
print(response.text)
# if we don't supply the header, the API provider has no way to authenticate the user, so the request
# will naturally be denied. So in this method of encryption, headers must be supplied with any request

# Now we can visit the our graph by going to our graph_endpoint/<graph_id>.html address in the browser
# This code is also used only once per graph, so basicallt post requests are usually done only once

# Now updating the graph or more precisely, adding a pixel to the graph was given as a challenge
# So let's try to complete that now by looking at the relevant documentation for the aciton

post_pxl_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# If we wanted to post the data for today, not just a fixed day every time, we could use the
# datetime module to get the today's date
                        # today = datetime.now()
# Instead, if we want to update for a particular day, we can use the following way:
day_to_update = datetime.datetime(year= 2024, month= 7, day= 7)
# But since this is not in the format we need, we need to use a datetime method called strftime
# It takes a datetime object and formats it by using the data that can be obtained from it
# The format codes need to be specified inside a string and they will format exactly that way
formatted_date = day_to_update.strftime("%Y%m%d")
# There are lots of other codes which can be found at: https://www.w3schools.com/python/python_datetime.asp
# Like the day of the year, month name in short/full version, year without century, etc

# Similarly, we can input the quantity of the action from the user, then the pixel data can be made free
# from any hard coded forced additions. All data to be sent can be customized easily
run_distance = "11.56"

# This too will be a POST request, so let's set up the request body JSON
post_pxl_data = {
    "date": formatted_date,
    # From my yesterday's wasted research, I had found out that this is the ISO Date format,
    # where we supply the date without any separators in the format yyyyMMdd
    "quantity": run_distance
    # Validation rule: int ^\-?[0-9]+, float ^\-?[0-9]+\.[0-9]+
    # This will be the quantity of our action associated with this date
}

# Now since the header will be the same as when creating the graph, let's just use that
response = requests.post(url= post_pxl_endpoint, json= post_pxl_data, headers= headers)
print(response.text)
# Now that this was a success, a new pixel should have been added at today's date
# i.e. July 8th, 2024

# The date data is hardcoded here, but what if we wanted to prompt some user input or just
# use today's date whenever we wantot add a new pixel? We need to work with the datetime
# module for that.

# In the webpage, when there are more than one pixels, the color scheme will adjust its
# intensity relative to the minimum, maximum and average values automatically

# The next challenge was to use the docs as a reference and update a pixel. So let's comment out
# the pixel posting code. Now we need to use the PUT() request instead of POST()
# The API endpoint will need to be updated as well:
update_endpoint = f"{post_pxl_endpoint}/{formatted_date}"
# We can just work with the variables we already have since we're just updating the data
actual_run_distance = "3.66"

update_data = {
    "quantity": actual_run_distance,
    # Since the API Endpoint itself contains the date, we need not provide it here
    # Here the quantity is optional, to create there must be a quantity given, but
    # a data is already there, so we can choose to not send a data as well, though what is the
    # point of sending an empty update request anyway
}

response = requests.put(url= update_endpoint, json= update_data, headers= headers)
print(response.text)

# Finally, to delete a pixel from the graph, we use the DELETE() request
# The API Endpoint is the same as the update request, so we'll leave that as is

# In this case, we need not supply a json at all, since all data is already given in the endpoint
# So we just have to give it the header and we'll be good to go

response = requests.delete(url= update_endpoint, headers= headers)
print(response.text)