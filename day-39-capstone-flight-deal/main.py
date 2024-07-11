# Today is a part of a two-day project that uses different APIs to gather flight
# price data and uses the data to send an SMS if a price lower than the specified
# threshold was found. Since I don't have Twilio and it didn't work for me, I will
# be using SMTPLib instead
# The course suggested I use the Kiwi Flight API and it's natural since it was one
# of the most popular Flight Price APIs back when the course was recorded, but I
# think I'm a couple months too late for that, as they stopped offering APIs to
# developers and now only offer it to business partners.
# So after about an hour of wailing and searching around, I have (So far) settled for
# FlightAPI which offers 10 API Request Credits, which I have no idea what it means
# I hope it doesn't mean that I can only use the API 10 times. That's not even enough
# for testing.

# Anyway seems like the project includes both API and OOPs so I'll be working with the other
# files before using their classes inside this one. First I'll be using the Sheety API to
# fill in the rows with city code (not airport code) which we can use to search with the flightAPI
# So apparently the limit is 100 requests per 30 days for both the FlightAPI and Sheety. I'll
# have to be extra careful then
# I couldn't find a decent API in https://rapidapi.com either

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

from pprint import pprint
# This apparently prints the data in a better format

sheet = DataManager()
data = sheet.get_sheet_info()
searcher = FlightSearch()
flight_data: FlightData = searcher.get_cheapest(data["prices"])

mail_service = NotificationManager()
mail_service.send_mail(flight_data)


# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.