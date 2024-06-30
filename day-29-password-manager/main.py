# Today, the project is a GUI Password Manager App "MyPass"
# The dividers were the only things given by the course, alongside the logo 
from tkinter import *
# In order to use the messagebox module, we need to import it separately
# since the above import will only get the classes, functions, constants but not module
from tkinter import messagebox
# Now this random module is for the password generator:
import random
# In the course, only the required functions were imported, but I'll just keep it like this
import pyperclip
# Seems like I already had this installed, what a pleasant surprise!

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# We created a random password generator in one of the early days, and we'll reuse the
# same code again here. I'll just copy paste the code in the course resources

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# I don't want to add these into the function, I'll just leave them as global for now

def pass_generator():
    # There used to be three variables that stored the random number of characters,
    # symbols, and numbers to be put in the password and I didn't touch them but
    # in the course, they were incorporated into the list creation statement so I did same

    password_list = []
    # A challenge here was to convert the for loops that were in the following format
    # into list comprehensions that we learnt some days earlier:
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]
    # In the course three separate lists were created and later joined, but this looks cooler 😎

    random.shuffle(password_list)

    password = "".join(password_list)
    # This is a way to join any iterables into a string with something between the characters
    # In this case, nothing needs to be added so we leave that string empty
                # for char in password_list:
                #     password += char
    # We replaced the above lines of code with the join statement
    
    # Even though the task was to just make it work using list comprehension, I took
    # the liberty of completing the entire code. When the button is pressed,
    # the current password in the password field is erased and a new random
    # password is generated.
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    
    # The final functionality is to be able to copy the password when we generate it
    # So that we can just paste it somewhere else. We use a module called pyperclip for it
    # it is a community module so I need to install it, and then I will import it
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# We need to save our password to a file called "data.txt" when user presses "Add"
# Then the data in the entry fields of website and password must be cleared out
def add_pwd():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    
    # We also need a method to validate the input so that if user left any field empty
    # It will show a warning
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title = "Empty Field!",
                             message = "You have left one or more fields empty.\n"
                             "Please fill all the fields before trying again!")
        # The course used showinfo() method but I prefer the showwarning() as it has a sound
    else:
        # I originally reused the is_ok variable, but before watching course solution
        # this felt like a better idea, and the course had the same thing. Nice!
        # We need to create a messagebox to ask the user to confirm their info
        is_ok = messagebox.askokcancel(title = "Are you sure?",
                                    message = f"You entered the following credentials:\n"
                                    f"website: {website}\n"
                                    f"Email/Username: {email}\nPassword: {password}\n"
                                    "Do you want to continue saving this info?")
        
        # Now only if the user presses ok, i.e. is_ok is true, then it should save else cancel so
        if is_ok:
            # Let's add data to the file
            with open("day-29-password-manager/data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                
            # Now to clear the fields, we use the delete() method
            website_input.delete(0, END)
            pass_input.delete(0, END)
            # This will delete the entry contents from start (index 0) to last (END)
            # If we omit the END, it will only remove one character from the entry from 0 index

# ---------------------------- UI SETUP ------------------------------- #

# TODO 1: Setup the window anad canvas as per course requirements
window = Tk()
window.title("Password Manager-chan")
window.config(padx = 100, pady = 50)

canvas = Canvas(width = 200, height = 200)
logo = PhotoImage(file = "day-29-password-manager\logo.png")
canvas.create_image(100, 100, image = logo)
# Since the image is approx 200x200,
# the canvas size and picture position are set accordingly

# Now we need to set up the grid, the layout was given in the course.
# I will just attempt to replicate that layout. This one must be in the middle
canvas.grid(column = 0, row = 0, columnspan=3)

website_label = Label(text = "Website:")
email_label = Label(text = "Email/Username:")
pass_label = Label(text = "Password:")
website_label.grid(column = 0, row = 1)
email_label.grid(column = 0, row = 2)
pass_label.grid(column = 0, row = 3)

website_input = Entry(width = 42)
#Let's add the focus to this entry when the app launches
website_input.focus()
website_input.grid(column = 1, row = 1, columnspan = 2)
# This columnspan attribute makes it span across two columns, else it would try to
# fit the whole element inside a single column by expanding the column

email_input = Entry(width = 42)
# We might reuse our email from one service to another so let's set a value by default
email_input.insert(0, "sharpy@gmail.com")
# We could use the Tkinter constant "END" instead of 0 and it would put the cursor
# at the end of the text, while setting it at 0 would take it to the beginning
email_input.grid(column = 1, row = 2, columnspan = 2)

pass_input = Entry(width = 21)
pass_input.grid(column = 1, row = 3)

generate_btn = Button(text = "Generate Password", command = pass_generator)
generate_btn.grid(column = 2, row = 3)

add_btn = Button(text = "Add", width = 36, command = add_pwd)
add_btn.grid(column = 1, row = 4, columnspan = 2)

# Even by replicating the code, it didn't replicate the output
# so I might need to tweak stuff, now the canvas spans 3 cols and widths changed

window.mainloop()