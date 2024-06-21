# In today's lessons, I'll be learning more about the turtle module
# And tuples, and the GUI. Turtle is used to create Graphics in Py
# It is good to use the documentation to see how we can achieve our
# goal with the program. Google it and read that part of docs for it.

import turtle as t
import random
# Just like the last time, let's name this turtle gary
gary = t.Turtle()
# Changing the turtle shape and color like last time:
gary.shape("turtle")
# Other possible options(from docs): circle, classic, arrow...
gary.color("lawngreen")
# The Turtle module uses tkinter to render the graphics so the
# colors are also from its specifications: https://trinket.io/docs/colors

gary.forward(100)
gary.right(90)
# The above code moves turtle 100 steps forward then right by 90 degrees

# Our first challenge is to draw a 100x100 square anywhere, so I'll start:
for i in range(4):
    gary.forward(100)
    gary.left(90)

# Now our next challenge is to draw a dashed line (alternating draw and no draw)
# But I don't yet know how to not draw, everywhere gary goes, he draws
# So I will take a look at the documentation to see what's up
# I found out we can use pendown(), pd() or down() to set turtle down (draw)
# and penup(), pu() or up() to set turtle up (not draw) so I'll use that:
gary.color("Black")
gary.shape("arrow")
for i in range(50):
    gary.down()
    gary.forward(5)
    gary.up()
    gary.forward(5)
# Combined with the last move, this will create a black dash line after green square

# Next challenge is to draw polygons starting from a triangle*, each side 100 length
# The color of each polygon must be random.

for sides in range (3,10):
    angle = round(360/sides,1)
    line_color = random.choice(["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue"
                                , "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"])
    gary.color(line_color)
    for line in range(sides):
        gary.forward(100)
        gary.right(angle)
# Instead of this simple nested loop, we can set a shape drawing algorithm to a function
# Then later loop the function itself.

# Now the next challenge is to generate a random walk, with each step the same length
# We need to read the documentation and figure out how to make the line thicker, and
# adjust the turtle speed as well. Each step should be a different color.
# This is used to model real life events and studies.

def set_direction():
    return random.choice([0,90,180,270])
    
def set_color():
    """Sets a random color from the full spectrum as the pen color"""
    r = random.randint(0, 255)    
    g = random.randint(0, 255)    
    b = random.randint(0, 255)
    # In the course the challenge was to return a tuple 
    rgb = (r, g, b)
    return rgb
    

t.colormode(255)
# This specifies whether we have 8 bit color sequence or color intensity. Values 1.0 or 255
# The rgb values used in pencolor can be a colorstring, or a tuple of (r, g, b)
gary.shape("arrow")
step_size = 50
# The speed of turtle can be changed as:
gary.speed(10) # same as gary.speed(fast)
# Arguments: 1 -> Slowest, 10 -> Fast, 0 -> Fastest. In the range 1-10 it is relative speed
# Now to change the size of the paintbrush
gary.pensize(10)
# We can also use the width() method which will have the same effect. 
        # gary.resizemode("user")
# This allows us to actually change the width
        # gary.shapesize(5,1,5)
# Parameters: (lateral width, forward width, outline)
# The above lines can be used to change the shape of the acutal turtle (shape we set)
for _ in range(100):
    # We can use gary.seth(0) to reset current direction to East before starting
    # but since it's random anyway, I don't think it makes too much difference
                    # gary.left(set_direction())
    # I initially had the above LOC but then after looking at the course, this seems better:
    gary.setheading(set_direction())
    gary.pencolor(set_color())
    # We can also use gary.color instead
    gary.forward(step_size)

# Next challenge is to create a spirograph i.e a bunch of overlapping circles which have a
# single point of contact and the same radius, their radii if joined also forms a circle
# Now to scour through documentation to see what we can do it with:
# gary.circle(radius, angle*) can be used to draw a circle upto angle degrees (180 = semi)
# The tilt maybe I can achieve by just looping through 1-360 of setheading() so let's try
def set_color():
    """Sets a random color from the full spectrum as the pen color"""
    r = random.randint(0, 255)    
    g = random.randint(0, 255)    
    b = random.randint(0, 255)
    # In the course the challenge was to return a tuple 
    rgb = (r, g, b)
    return rgb
    

t.colormode(255)
radius = 100
gary.speed("fastest")
gary.pensize(1.5)
gap = 5
for _ in range(int(360/gap)):
    # Initially the gap was fixed, but having a changeable gap felt meaningful so I did
    gary.setheading(_*gap)
    gary.pencolor(set_color())
    gary.circle(radius)
    

# To keep the screen on, we'll need the screen features too so
a_screen = t.Screen()
a_screen.exitonclick()
# This will keep the screen until exited on click

# There are multiple ways to import a module in Python:
                # import turtle
# This will just import the module as is and to access the Turtle class:
                # eg_turtle = turtle.Turtle()
# When we need to use something many times, this becomes repetitive so
                # from turtle import Turtle
# This will only import Turtle class so we can just use it by its name
                # eg_turtle = Turtle()
# We can also import everything from the module to be used like this:
                # from turtle import *
# But this might create confusion when using the things inside the module
# Since we wouldn't always know where the class/attribute/methods is from
# In order to import a module not a part of the python standard library
                # import prettytable
# We would first need to install it, else it would not work

# Final challenge today is to recreate Damien Hirst's dot painting, in the main.py file