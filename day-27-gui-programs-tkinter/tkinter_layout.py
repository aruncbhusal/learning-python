# The other program got long and has too much information
# So I created a new file to add some other info apart from that
from tkinter import *

window = Tk()
window.title("Just learning")
window.minsize(width = 600, height = 400)
# We can also add padding to the window or the individual widgets to
# do some UI cleanup work
window.config(padx = 50, pady = 50)

label = Label(text = "Just a test text", font = ("Arial", 12, "bold"))
# We used the pack() method to set the layout in the other file
# It stacks elements on top of each other, but we can also choose other
# ways to place items. pack() has a limited freedom in positioning
            # label.place(x = 100, y = 100)
# This will place the label at the abolute position 100x100
# To make it consistent with rest of the code, swtiching to grid
label.grid(column = 0, row = 0)
# Let's add some padding to the label
label.config(padx = 20, pady = 20)

button1 = Button(text = "Click pleaseeee")
# We can also use the grid layout to place the widgets, and it will
# divide the window into grids where we can place the items relatively
# Since this is the second item I will use 1,1 position
button1.grid(column = 1, row = 1)
# Since initially the label is set with a place() layout, this goes to
# the top corner, as if it were the only element in the grid
# We can't use grid() and pack() in the same window, that would give error
button1.config(padx = 10, pady = 10)
# This is a special button with special padding treatment .... /s
# So it seems the button padding adds the padding around the text inside
# the clickable area, but not the button itself. I wonder how to fix that

button2 = Button(text = "Me tooooooo")
# Grid is more preferred compared to the other layouts since the others
# pack() has too little freedom and place() has too much
# So it becomes too tedious to try to position everything perfectly
# if using place(). So we'll stick with grid
button2.grid(column = 2, row = 0)

input_stuff = Entry(width = 30)
# The course task was to put the label in 0,0 button1 in 1,1
# button2 in 2,0 and entry in 3,2 so let's complete that
input_stuff.grid(column = 3, row = 2)

window.mainloop()