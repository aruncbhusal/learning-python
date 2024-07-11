class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.origin = data["origin"]
        self.dest = data["destination"]
        self.price = data["price"]
        self.date = data["flight_date"]