# I'll be using VSCode from now on since that is what I'm habituated with
# In this day's lesson, I'l be learning about Object Oriented Programming
# When code starts to get complex, like the coffee machine earlier,
# It becomes important to separate out parts from each other,
# Dividing them into different modules, so that each module can do its thing
# Objects are modeled after real world objects, giving the name OOP
# An object can have attributes (modeled with variables), and
# methods (modeled with functions). Multiple objects can be created by
# following a blueprint called the class.

# First we will be using a class from the Python library 'turtle'
# It is used to draw graphics (imagine a turtle dragging a paintbrush)
# We need to import the library first then use the Turtle class for object

import turtle

# A class name is typically PascalCase and followed by parentheses to create
gary = turtle.Turtle()
# Now we can try to print the object and see that it prints an object
                        # print(gary)
# We can use the attributes and methods of the class Turtle to change it
# Initially the turtle appears as a black cursor. Let's make it a blue turtle
gary.shape("turtle")
# The color references are here: https://cs111.wellesley.edu/reference/colors
gary.color("SteelBlue1")
# From the turtle docs: https://docs.python.org/3/library/turtle.html
# I'll be moving the turtle a 100 steps using a method of the class Turtle
gary.forward(100)


# We can create another object of a different class to print in screen
new_screen = turtle.Screen()
# We can see the attributes by just printing it on the console:
print(new_screen.canvheight)
# The following method will keep the screen on until clicked:
new_screen.exitonclick()


# Next we'll be using the Prettytable library that isn't actually pre-installed
# So we need to first install the library to our environment in order to use it
# In the tutorial, a virtual environment is used so it installs for that project
# But since I'm working with my own local environment, it will install the package
# to my own library. To do that I can just type pip install prettytable
# Or I can download it from the python library tab.
# For more open source libraries, we can visit pypi.org (Python Package Index)
from prettytable import PrettyTable
table = PrettyTable()
# Now we need to insert data into the table, we can use the following method:
# I'm following the exact format of the course here, nothing out of pocket
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# We can also set the alignment using the attribute 'align'
table.align = 'l'
# And now we print the table:
print(table)

# I read a 1994 interview of Steve Jobs and found out he was one of the pioneers
# of object oriented programming, from a non-programmer perspective
# and that Microsoft was very slow to adopt OOP for their windows OS

# Now the final thing for today is to recreate the Coffee Machine from yesterday
# but this time using OOP. In fact all the classes are already written and
# we just need to use the objects to do their job to achieve the same goal
# The code will be downloaded and I'll continue my work there now.