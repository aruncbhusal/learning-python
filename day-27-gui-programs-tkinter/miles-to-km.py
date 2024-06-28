# The final project for this day, and it's already midnight so it
# took me way too long to get this day done, but it was a lot of content
# Plus, I started very late, at almost 8 pm

# The task is to create a miles to kilometres converter
# The grid layout for the program was given, I just need to implement it

from tkinter import *

window = Tk()
window.title("Miles to Kilometres")
window.minsize(width=300, height= 150)
window.config(padx = 50, pady = 50)

miles = Entry(width = 8)
miles.insert(END, 0)
miles.grid(column = 1, row = 0)


def label_maker(str,col,row_):
    new_text = Label(text = str, font = ("Arial", 14))
    new_text.grid(column = col, row = row_)
    return new_text

miles_text = label_maker("Miles", 2, 0)
equal_text = label_maker("is equal to", 0, 1)
kms_text = label_maker("Km", 2, 1)
kms_val = label_maker("0", 1, 1)


def convert():
    kms_val.config(text = round(float(miles.get())*1.6, 2))

button = Button(text = "Calculate", width = "10", command = convert)
button.grid(column = 1, row = 2)

window.mainloop()