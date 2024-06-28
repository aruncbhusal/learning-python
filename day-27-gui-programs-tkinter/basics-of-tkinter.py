# The first GUI OS was developed by the Palo Alto research facility, Xerox Parc
# which had also invented Ethernet, and the first OOP Language Smalltak-80
# Apple Mac Lisa and later Windows adopted GUI and the point-and-click in their OSes

# In Python, we have the inbuilt Tkinter module that allows us to create GUI programs
# by breaking out of the confinement of the console and working with program windows
import tkinter
# We could also use "from tkinter import *" to import everything and save time
# Since we can omit "tkinter." when using any of the classes/modules inside
# I'm using this module for the first time so for familiarity's sake I'll keep it as it is

window = tkinter.Tk()
window.title("GUI-chan")
window.minsize(width= 600, height= 400)
# This is similar to the screen class in the Turtle module

label = tkinter.Label(text= "Hello sansar!", font= ("Segoe UI", 28, "italic"))
# Just this wouldn't be enough to get the label on the screen, we need to use:
label.pack()
# In VSCode it lists the arguments but in Pycharm it doesn't list all of them when using
# these methods unlike methods in turtle or others, it contains **kw instead, which allows
# for variable number of arguments to a function
# The pack() method also has "side" argument for center, left, right, bottom,...
            # label["text"] = "Overwritten MUAHAHAA"
# We can access the arguments similar to a dictionary like this as well, or we can use
label.config(font = ("Comic Sans", 20))
# We can also use the config() method to change the args
# Notice that the font didn't need all the elements of the tuple to work, they are optional

# In order to have things apart from label, we can take a look at the documentation
# Let's insert a button into the window as well
            # button = tkinter.Button(text = "Click Me!!")
# Now for this to appear on screen, we have to give it a layout, so we'll use
            # button.pack()
# I thought if I just leave it as it is, it would be placed on top of the label.
# Relieving to see that I don't have to worry about that.

# Our challenge is to create a button that, when clicked, will display a text with
# "I got clicked" on the label, instead of "Hello sansar!"
count = 0
def button_clicked():
    # label["text"] = "I got clicked!"
    global count
    # Seems I couldn't use count normally until I used this, so here it goes.
    count += 1
    label.config(text = f"Click count: {count}")

    
button = tkinter.Button(text = "Click Me!", command = button_clicked)
# It no longer does this since I have changed the function later but it was necessary

button.pack()
# I did that, but now I want to create a click counter, so let's do that.

input = tkinter.Entry(width = 45)
# Docs for entry: http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
# While creating this input, we won't get the entered text in the input, it is an object
input.pack()
# Docs for pack() : http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# More docs: https://docs.python.org/3/library/tkinter.html#the-packer
# We use Entry.get() to get the actual entered string
# We can use the insert() method to set a default text when program starts first
input.insert(tkinter.END,"Type something")
# It has two positional arguments: index(str) and string(str)
# The index can just be set to "0" if there's no text before it

# Our task is to get the entry to be stored in a variable, and change label to that
# So I'll write another function above called button_action to implement that
def button_action():
    label.config(text = input.get())

button.config(command = button_action)

# We can create multiple line text inputs the following way
textinput = tkinter.Text(width = 30, height = 5)
# Here the width and height are number of characters accomodated inside it
# That's why the same width here and in Entry will cause two areas with different pixel width
textinput.insert(tkinter.END,"Multiple lines go brrrr, I can't believe this spans 5 lines.")
# This has two positional arguments index and chars
# The index is a type _TextInput which is basically "line_number.char_position"
# The course had this constant "END" but I have no idea why my code doesn't work with it 
# OH, I now know it was imported from the tkinter module
# It probably goes to the position after the last currently available character position
textinput.focus()
# This puts the cursor in the textbox
text = textinput.get("1.0", tkinter.END)
# This extracts all text from 0th character in the first line to the last character
textinput.pack()

# Next we can have a spinbox(basically a counter type input)
# This class also has the command argument, we can call it whenever spinbox is used
def spinbox_used():
    """Prints to console the square of value in spinbox when it is used"""
    print(int(spin.get())**2)
    # Apparently the spinbox contains a string??
spin = tkinter.Spinbox(from_ = 0, to = 20, width = 5, command = spinbox_used)
# When we set the max value with to, any value above it will be discarded
# We can input a value within range but it will only count as using the spinbox
# once we either increment or decrement our value
spin.pack()

# The Scale is basically same as this, just it has a slider.
# For the scale I won't create another function but it too as a command argument
scale = tkinter.Scale(from_ = 0, to = 100, width = 10)
scale.pack()

# A checkbox has something peculiar about it, its value can be stored in a variable
# but that variable has an object type, and we use get on it and not the checkbox itself
cbox_state = tkinter.IntVar()
cbox = tkinter.Checkbutton(text = "Check it Check it!", variable = cbox_state)
print(cbox_state.get())
# Of course this will just print 0 once since initially it is unchecked
cbox.pack()

# Now for radiobutton, it isn't as straightforward, since we need to create one for each
radio_state = tkinter.IntVar()
radio1 = tkinter.Radiobutton(text = "Option 1", value = 1, variable = radio_state)
radio2 = tkinter.Radiobutton(text = "Option 2", value = 2, variable = radio_state)
# Both of the radio's states will be tied to the radio_state IntVar
# A discovery I made random checking was that a value of 0 would turn radio on by default
radio1.pack()
radio2.pack()

# Finally it is the listbox
def list_used(event):
    print(lbox.get(lbox.curselection()))
    # So there's yet another peculiarity here, gets current selection from listbox
lbox = tkinter.Listbox(height = 5)
people = ["Skylar", "Gracie", "Packard", "Layla", "Josh"]
for item in people:
    lbox.insert(people.index(item),item)
# We need to give an index as well it seems
# To bind it to a function we use bind() instead of an argument
lbox.bind("<<ListboxSelect>>", list_used)
lbox.pack()

window.mainloop()
# This statement acts as a while True loop which keeps waiting for user input
# Otherwise the window will close rihgt after it opens, because there's nothing to do
# It must be after all other code at the end of the code.