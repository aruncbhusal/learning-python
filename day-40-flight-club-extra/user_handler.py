import requests

USERBASE_ENDPOINT = "<SHEETY_ENDPOINT>"
BEARER_TOKEN = "<SHEETY_BEARER_TOKEN>"

print("Welcome to FlightClub-chan! We provide you with unbelievable flight deals.")
print("Please fill up the given data to join our club.\n")
f_name = input("Enter your first name:\n")
l_name = input("Enter your last name:\n")
match= False
while not match:
    email = input("Enter your email:\n")
    conf_email = input("Type the email again:\n")
    if email == conf_email:
        match = True
    else:
        print("The emails didn't match, try again maybe?\n\n")

headers = {
    "Content-Type": "application/json",
    "Authorization": BEARER_TOKEN,
}
data = {
    "user":{
        "firstName": f_name,
        "lastName": l_name,
        "email": email,
    }
}
response = requests.post(url= USERBASE_ENDPOINT, headers= headers, json= data)
response.raise_for_status()
print(response.text)

print("Welcome aboard! Remember, first rule of Flight Club 🤐")