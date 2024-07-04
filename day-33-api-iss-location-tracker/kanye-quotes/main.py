from tkinter import *

import requests
# Everything apart from this import and the get_quote() function was predefined
# and I just copied them from the course resources. That is not our objective
# Our goal is to get the get_quote to return a quote from Kanye, the api for which
# can be found at the following website: https://kanye.rest/

def get_quote():
    response = requests.get(url = "https://api.kanye.rest/")
    response.raise_for_status()
    # This is something that's easy to forget, but is good to have to know what has
    # actually gone wrong when something doesn't go as expected
    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text = quote)
    # Okay this is it, that's enough



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="day-33-api-iss-location-tracker/kanye-quotes/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE",
                                width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="day-33-api-iss-location-tracker/kanye-quotes/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()