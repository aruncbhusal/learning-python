# In this program, we're replacing the data.txt with a data.json file
# JSON (JavaScript Object Notation) is a popular way to store data in a way similar
# to the Python dictionary, though it is originally from JavaScript
# Python has a built-in module for dealing with json files and we'll use that here

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pass_generator():
    password_list = []

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_input.delete(0, END)
    pass_input.insert(0, password)
    
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_json(data):
    # This will get rid of the repitition of code that was happening in the try-except block
    with open("day-30-error-exception-json/data.json", "w") as file:
                json.dump(data, file, indent = 4)

def add_pwd():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    
    # Since a JSON contains data in the format of a dictionary, we need to set up the dict
    # first so that it can be later added to the JSON file
    data_dict = {
        website : {
            "Email" : email,
            "Password" : password
        }
    }
    # Now we can use this dictionary later to update the JSON file
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title = "Empty Field!",
                             message = "You have left one or more fields empty.\n"
                             "Please fill all the fields before trying again!")
    else:
        # There was a block of code to confirm the saving, but I'll remove it for simplicity
        
        # In order to work with JSON, there are three methods we use:
        # To read data from a json file: json.load()
        # To write data to a json file: json.dump()
        # To update data from a json file: json.update()
        # Since a JSON is stored in a specific format, we can't use the append mode with it
        # We need to read, update then write to the file in order to mimick append functionality
        
        # It gives me an error if the json file either doesn't exist, or is empty. So we need to
        # have some sort of exception handling in this case
        
        # Let's first open the file to read it
        try:
            with open("day-30-error-exception-json/data.json", "r") as file:
                data = json.load(file)
                # We take the data in the json file and store it into a dictionary.
                # If we use typecheck on "data" it will confirm that it is a dictionary
        except FileNotFoundError:
            # This will work for when the file doesn't exist
            write_to_json(data_dict)
            # But what if the file exists but it is empty? We need another except statement
            # I was tempted to use the standard standalone except block but then I thought
            # I may as well see what the error was and be more specific, so that I can know
            # if there's some other error apart from that too
        except json.JSONDecodeError:
            write_to_json(data_dict)
            # This made me wonder, since I'm using the same code in both the blocks, can't I
            # just use an or operator to handle both the errors the same way?
            # On testing, turns out it doesn't work. Let's see how the course handles it
            # Seems like the course didn't handle this error at all, probably since the file
            # either exists, or it contains some data either way. That makes sense too, but
            # as for me I'll just keep this code here because it feels like it covers ground
        else:
            data.update(data_dict)
            write_to_json(data)
        finally:
            # We can even put this as a decoration, though it's not very necessary,
            # It would run regardless of the status of the try block
            website_input.delete(0, END)
            pass_input.delete(0, END)
            
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pwd():
    website = website_input.get()
    
    if len(website) == 0:
        messagebox.showwarning(title = "Why Empty?",
                               message = "The website field is empty, please "
                               "type the name of a website to search for it in the database.")
    else:
        try:
            with open("day-30-error-exception-json/data.json", "r") as file:
                data = json.load(file)
                email = data[website]["Email"]
                password = data[website]["Password"]
        except FileNotFoundError:
            messagebox.showwarning(title = "Empty vault!",
                                   message = "The password vault is empty, "
                                   "please add a password first before trying again.")
        except KeyError:
            # In the course, this is instead implemented in the else block in the form of an if
            # for "if website in data" and show the popup in its else, but I'm shooting two birds
            # with one stone here, and though I did think of that at the start, while I was writing
            # this code, I felt like this would be good enough for it, since it is not something that
            # needs to go to the else block in the first place
            messagebox.showwarning(title = "Not Found!",
                                   message = f"No data available for {website}. "
                                   "Please check for a typo or try adding the website first")
            # The course actually covered this, stating we should stick to if-else if it is possible
            # For cases of actual errors, where we can't check for it, like File Not Found
            # In the case of Key Error, we can just check if the key exists and be done with it
            # It is a lot simpler just using if-else rather than complicating the code, but since
            # my method takes care of two exceptions at the same time, it should still be good enough
        else:
            messagebox.showinfo(title = "User Data Found!",
                                message = f"The following data was found for the website '{website}'"
                                f"\nEmail: {email}\nPassword: {password}")
        # Well this seems to work flawlessly, now I can watch the course solution without a worry
        # From the course: exceptions are meant to be exceptional, handle frequently occuring events
        # as cases rather than exceptions whenever possible

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager-chan")
window.config(padx = 100, pady = 50)

canvas = Canvas(width = 200, height = 200)
logo = PhotoImage(file = "day-29-password-manager\logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(column = 0, row = 0, columnspan=3)

website_label = Label(text = "Website:")
email_label = Label(text = "Email/Username:")
pass_label = Label(text = "Password:")
website_label.grid(column = 0, row = 1)
email_label.grid(column = 0, row = 2)
pass_label.grid(column = 0, row = 3)

website_input = Entry(width = 21)
website_input.focus()
website_input.grid(column = 1, row = 1)
# The columnspan for this was changed from 2 to 1 so width will be halved naturally

email_input = Entry(width = 42)
email_input.insert(0, "sharpy@gmail.com")
email_input.grid(column = 1, row = 2, columnspan = 2)

pass_input = Entry(width = 21)
pass_input.grid(column = 1, row = 3)

generate_btn = Button(text = "Generate Password", command = pass_generator)
generate_btn.grid(column = 2, row = 3)

add_btn = Button(text = "Add", width = 36, command = add_pwd)
add_btn.grid(column = 1, row = 4, columnspan = 2)

# In the v2, we'll add a button to search through the saved passwords to find a email-pass
# combination for a particular website. It is covered in the last lecture but I'll try to
# implement it before I watch the course itself
search_btn = Button(text = "Search", width = 15, command = search_pwd, )
# I wasn't anticipating having to setup its width but here we are
# Since it will be right beside the "Website" Entry as we'll be searching for the combination
# that is associated with that website, we will be adjusting its columnspan to 1 as well
search_btn.grid(column = 2, row = 1)

# It still bothers me that buttons look different on Mac than on Windows, Mac looks cleaner

window.mainloop()