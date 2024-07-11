import smtplib
import requests
import time
from flight_data import FlightData

APP_PASS = "<GOOGLE_APP_PASS>"
MY_EMAIL= "<MY_ADDRESS>"

USERS_ENDPOINT = "<SHEETY_ENDPOINT>"
BEARER_TOKEN = "<SHEETY_BEARER_TOKEN>"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.src = f"{MY_EMAIL}"
        
    def get_user_info(self):
        header = {
            "Authorization": BEARER_TOKEN,
        }
        response = requests.get(url= USERS_ENDPOINT, headers= header)
        response.raise_for_status()
        user_data = response.json()["users"]
        users = [{
            "f_name": item["firstName"],
            "l_name": item["lastName"],
            "dest_email": item["email"],
        } for item in user_data]
        return users
        
    
    def send_mail(self, data):
        if data != None:
            users = self.get_user_info()
            for user in users:
                body = f"Hi {user['f_name']} {user['l_name']}, we've got something for you!\n\
                Only ${data.price} to fly from {data.origin} to {data.dest}\n\
                Flight Date: {data.date}. Don't miss the opportunity!"
                
                with smtplib.SMTP(host= "smtp.gmail.com", port= 25) as connection:
                    connection.starttls()
                    connection.login(user= MY_EMAIL, password= APP_PASS)
                    connection.sendmail(
                        from_addr= self.src,
                        to_addrs= user["dest_email"],
                        msg= body
                    )
                print(f"Sending email to {user['dest_email']}")
                time.sleep(0.5)
                print(f"Send successful!")
        else:
            print("No relevant cheap flights were found.")