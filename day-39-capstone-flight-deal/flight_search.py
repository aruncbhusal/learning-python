# Since I dont have the access to course suggested Kiwi API, I will have to settle for using two APIs
# FlightAPI and Amadeus API

# Let's first have an independent function that returns just the AITA code since it uses Amadeus
# The rest of the code will probably use FlightAPI, so creating a distinction
import requests
import random
import datetime
from flight_data import FlightData

AMADEUS_API_KEY= "<AMADEUS_API_KEY>"
AMADEUS_SECRET_KEY= "<AMADEUS_SECRET_KEY>"
AMADEUS_ENDPOINT= "https://test.api.amadeus.com/v1"
AMADEUS_TOKEN= "<AMADEUS_BEARER_TOKEN>"

API_NINJA_KEY= "<API_NINJA_KEY>"

# headers={
#     "Content-Type": "application/x-www-form-urlencoded"
# }
# data=f"grant_type=client_credentials&client_id={AMADEUS_API_KEY}&client_secret={AMADEUS_SECRET_KEY}"

# token_receive_ep = "/security/oauth2/token"
# response = requests.post(url= f"{AMADEUS_ENDPOINT}{token_receive_ep}", headers= headers, data= data)
# response.raise_for_status()
# print(response.text)

# def get_codes(city):
#     # The AMADEUS API docs page didn't load so I'll have to deal with api-ninjas Airport API for this
#     apininja_endpoint = "https://api.api-ninjas.com/v1/airports"
#     parameters = {
#         "city": city
#     }
#     headers= {
#         "X-Api-Key": f"{API_NINJA_KEY}"
#     }
#     response = requests.get(url= apininja_endpoint, params= parameters, headers= headers)
#     response.raise_for_status()
#     print(response.json())
#     return response.json()["iata"]
    
    

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.origin = "LON"

    
    def get_cheapest(self, data):
        # dates_endpoint = "/shopping/flight-dates"
        # parameters= {
        #     "origin": self.origin,
        #     "destination": dest,
        #     "oneWay": "false",
        #     "maxPrice": str(maxp),
        # }
        # headers= {
        #     "Authorization": AMADEUS_TOKEN,
        # }
        
        # Since the API didn't work, I'll just make up random data
        flights = []
        for city in data:
            time_to_flight = datetime.timedelta(days = random.randint(1,60))
            now = datetime.datetime.now()
            fly_day = now + time_to_flight
            that_day = fly_day.strftime("%Y-%m-%d")
            to_be_fed = {
                "origin": self.origin,
                "destination": city["iataCode"],
                "price": round(random.random()*3*city["lowestPrice"],2),
                "flight_date": that_day,
            }
            difference = city["lowestPrice"] - to_be_fed["price"]
            if difference > 0:
                flights.append((to_be_fed, difference))
        try:
            cheapest = flights[0]
            for flight in flights:
                if flight[1] > cheapest[1]:
                    cheapest = flight
            flight_data = FlightData(cheapest[0])
        except IndexError:
            flight_data = None
        return flight_data
        # response = requests.get(url= f"{AMADEUS_ENDPOINT}{dates_endpoint}", params= parameters, headers= headers)
        # response.raise_for_status()
        # print(response.json())