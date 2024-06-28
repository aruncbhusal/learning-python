# This lesson also goes into more types of arguments passed into functions in Python

# Advanced function arguments: We can set default values to arguments if we want
# Those values then become optional when calling the function later
def something(text, a = 2, b = 5):
    print(f"Your text: {text} and the sum of a and b: {a+b}")

# We can simply omit the arguments which have default values set and call the function
something("Sayonara Sunshine")
# The arg with no default value set can be used with positional argument, rest can be
# used with keyword arguments if provided, since position might be hard to remember for all
# In the below statement, "a = 15, b = 14" could just be replaced with "15, 14"
something("Skies cries fries", a = 15, b = 14)

# *args (can use any name we like) can be used to accept unlimited arguments from the user
# A challenge in the course was to create a function that prints the sum of however many nums
def add(*args):
    sum = 0
    # The "args" here is a tuple of all the arguments passed into the function
    # Using args[index] we can access any posiiton of the passed arguments
    for n in args:
        sum += n
    return sum
print(f"The sum of 6 7 15 24 56 76 is: {add(6, 7, 15, 24, 56, 76)}")
# They are all positional arguments, since their position is the position in the tuple

# **kwargs can be used to accept many keyword arguments, in contrast to *args positional args
# Instead of being a tuple, it is instead stored as a dictionary, so we can access the key to
# see the variable name assigned in the call statement, and work with it accordingly.
# This time let's see with a class definition so we can compare with the Tkinter module
class GraphicsCard:
    def __init__(self, **kwargs):
        self.manufacturer = kwargs["manufacturer"]
        # We can just use normal dictionary access method to access the value for the arguments
        # Though this bracket method of retrieval will crash the program if the specified key
        # can not be located in the dictionary, in this case if the argument was not supplied
        # during the initialization call. So we can instead use the following way instead:
        self.series = kwargs.get("series")
        self.generation = kwargs.get("gen")
        self.card_name = kwargs.get("name")
        for argument in kwargs:
            print(f"{argument.title()} = {kwargs[argument]}")

my_card = GraphicsCard(manufacturer = "NVIDIA", series = "Geforce GTX", card_name = "1650Ti")
# In the Tkinter module, kwargs are used since they imported the functions from something called
# Tk, which is not a part of python, and they imported all of its functions and put them in a dict
# That is why we can access them by using the keyword arguments but they won't appear in PyCharm
