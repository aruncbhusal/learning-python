# This time the topic is API (Application Programming Interface)
# API is a set of commands that are specified by an external system that allow
# us to access a specific set of data from the external system
# The API needs an API Endpoint, which specifies the location(or the URL) from where
# we are able to extract the data, which is often in the JSON format

# We need to create an API request to be able to access the data in the system
# Once the request is accepted, with or without authentication, we are served the data
# We use the "requests" Python module to use API features, not a part of Python itself

import requests

# We will be using the API for the ISS (International Space Station) which is a large
# space station maintained in lower Earth orbit by the collaboration of NASA, CSA(Canada),
# Ruscosmos, JAXA(Japan) and ESA(Europe). It it the largest SS ever built. [Wikipedia]
response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# The source website for the API: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
                        # print(response)
# The get() method returns a response from the API Endpoint, which when printed will give
# a response code, rather than a JSON that appears when the API Endpoint is accessed via
# a web browser. In order to get the JSON string, I will have to watch the next video.
# The Response Code means the result of the HTTP request we sent. The meaning can be:
# 1XX: Informational
# 2XX: Success
# 3XX: Redirection
# 4XX: Client Error
# 5XX: Server Error
# A better explanation: https://www.webfx.com/web-development/glossary/http-status-codes/
# We can check for the response code using:
                        # print(response.status_code)
# We can use this status code to find out whether our request was successful, and if not
# we can raise an exception. But as we can see from the website above, there are too
# many status codes for us to write:
                # if response.status_code == 404:
                #     raise Exception("What you asked for does not exist")
# So we can instead use the method mentioned in the docs for the requests library
response.raise_for_status()
# So if I make a typo in the request URL, I will get a 404 error raised

# An API may be the term given to the API Specification or the API Implementation.
# Specification defines the API calls/ ways to access the API as defined by the provider
# Implementation is the way that the programmer who is using the API makes use of it
# The API provides the programmer with data that makes a greater use than the UI which the
# end user is provided when trying to access the original service.
# We can also separate an API from its implementation and have multiple implementations for 
# the same API, similar to how Scala and Java compile to the same bytecode, allowing Scala
# to be able to use any APIs that can be used with Java
# APIs differ from ABI(Application Binary Interface), Operating systems provide their own
# APIs like the POSIX API or Windows API, Linux provides an ABI
# WebAPI can be used to request JSON or XML(eXtensible Markup Language) using a HTTP request
# APIs can be private, partner or public. Public APIs must take care of possible attacks like
# SQL Injection or Denial-of-Service(DoS). An API Documentation is necessary to describe the
# ways that the API can be used to extract information from the system. [Wikipedia]

# In order to get the JSON from the response we generated using the get() method, we use:
data = response.json()
# This method returns a json that can be used just like a Python library to access the data
                        # print(data)
# By printing the JSON we find out the entire contents in the response we received, and now
# we can use it to gather the latitude and longitude information of the ISS at any time
position = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])
# We could have used multiple variables for this, but I'll keep it compact for now
# We can now use this position data in: https://www.latlong.net/Show-Latitude-Longitude.html
# Which will show us the current position of the ISS in the map of the Earth
# print(position)


# Some APIs may have an associated API Parameter, which are basically the same as function
# parameters, which we can supply for them to work with the parameters to provide us the data
# that is relevant to the supplied parameters. One such API is the Sunrise-Sunset API
# This API has two required and other optional parameters, the required parameters are the
# latitude and longitude values, since we need that to know the Sunrise and Sunset times
import datetime

MY_LAT = 27.704291
MY_LONG = 85.322768
# These are the latitude and longitude values for some place in Kathmandu
# The way parameters are to be arranged is defined in the API Documentations
# We arrange our parameters in the form of a dictionary as:
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Kathmandu"
}
# The key names here are as defined as the documentation

response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
# If we submit the get request with just the URL, we would receive a Response Code 400
response.raise_for_status()
# Response Code 400 means Bad Client Request, which means the server believes we made a mistake
# So we have to include the parameters in the request with an attribute "params"
                # print(response.json())
# We can see there's a lot of data being given with this JSON so it's pretty hard to tell the
# structure of the dictionary. So we can just use the JSON Viewer Awesome extension to view the
# JSON in the browser. The way to use parameters in the browser is by using the following format:
# <api-url-for-json>?<param1>=<value1>&<param2>=<value2>...
# The ? symbol separates the API Endpoint URL from the parameters and & separates from each other

# After looking at the JSON structure, I know that we can get the sunrise and sunset times as:
data = response.json()
                        # sunrise = data["results"]["sunrise"]
                        # sunset = data["results"]["sunset"]
                        # print(sunrise)
# Notice that initially, with only the required parameters set, the time here is formatted in a
# 12 hour format, which is not the formatting that the datetime module would provide:
now = datetime.datetime.now()
                        # print(now)
# It is because the optional parameter "format" in the Sunrise Sunset API is set to 1 as default
# which means it will format the data in the 12 hour format, rather than the UNIX 24 hr format
# which resembles the datetime module. So we can add it to the parameters dictionary to make it same
# The output is not exactly the same, but it is close
# Since the output is a string, we can now separate it with the help of split() method
# First we split it from the "T" in the middle that separates the date and time, then we separate it
# with the colon(:) which separates the different units of time. Since the split() method returns a
# list of all the items formed by the slpit, we can use it as the data

# In this case, we are only interested in the hour of sunrise and sunset so we use
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# This gets the second element of the list separated by T, then takes the first element of that list
# separated by a colon. And now the current hour can be retrieved by simply using the datetime module
hour_now = now.hour
print(sunrise)
print(sunset)
print(hour_now)
# One thing I noticed is that the sunrise and sunset times are UTC times, which means we need to specify
# our timezone for it to match the one provided by the datetime module. So I added another parameter