import requests

S_BEARER_TOKEN = "<SHEETY_BEARER_TOKEN>"
S_ENDPOINT = "<SHEETY_ENDPOINT>"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.header = {
            "Authorization": S_BEARER_TOKEN,
        }
    
    def get_sheet_info(self) -> dict:
        response = requests.get(url= S_ENDPOINT, headers= self.header)
        response.raise_for_status()
        return response.json()

    # def update_sheet(self, data):
    #     updated_rows = []
    #     for city in data["prices"]:
    #         city["iataCode"] = get_codes(city["city"],city["country"])
    #         updated_rows.append()
    #     print(updated_rows)
        
    #     # Apparently the city of "Paris" is everywhere in the US. Paris,Texas, Paris,Kentucky
    #     # and it's gonna list every airport in the list
    #     # So I think I'll just have to do the updating thing manually
    #     # I'm tired
        
    #     row_count = 0
    #     for rows in updated_rows:
    #         updated_data = {
    #             "prices": rows
    #         }
    #         response = requests.put(url= f"{S_ENDPOINT}/{row_count}", headers= self.header, json= updated_data)
    #         response.raise_for_status()
    #         row_count += 1
            
            
        # for code in get_codes():
        #     response = requests.put(url= S_ENDPOINT, headers= self.header, json= )
        #     response.raise_for_status()