import turtle as t
import random

                # import colorgram as cg
# This package can list out most used 10 colors from a given image
# which can be used as a palette as the base for some other image
# It is a port of a JS package with a 100% result replication

# colorgram.extract(image, no. of colors) will return a list of Color objects
# The color object has rgb, hsl (both named tuples) and a proportion values
                # def color_list():
                #     """Returns a color palette of rgb tuples extracted from image.jpg.
                #        Might take a while."""
                #     rgb_list = []
                #     n = 20
                #     h_colors = cg.extract("day-18-turtle-tuple-hirst-painting\image.jpg", n)
                #     for i in range (n):
                #         r = h_colors[i].rgb.r
                #         g = h_colors[i].rgb.g
                #         b = h_colors[i].rgb.b
                #         rgb_list.append((r, g, b))
                #     return rgb_list

# We actually don't need the code above anymore since our extraction is done.
# We can comment out or delete it and use the results from the extraction only
# First check whether any of the given colors are irrelevant (white/bgcolor)
# We can check in https://www.w3schools.com/colors/colors_rgb.asp

color_list = [(207, 159, 82), (54, 89, 130), (146, 91, 39), (140, 26, 48), (222, 207, 104), (132, 177, 203)
              , (158, 46, 83), (45, 55, 104), (170, 160, 39), (129, 189, 143), (83, 20, 44), (36, 43, 69)
              , (186, 94, 106), (186, 140, 172), (84, 120, 180), (60, 39, 31)]

# The project is to make a 10x10 grid of spots each 20 in size spaced by 50
# I will need to look at the documentation to see how it can be done
gary = t.Turtle()
t.colormode(255)
gary.up()
gary.hideturtle()
gary.speed("fastest")
# Our trusty gary is back in action. I will test the dot first then use it
# Okay I now know how it works, need to figure out the position method now
x = -300
y = -300
for i in range(10):
    for j in range(10):
        color = random.choice(color_list)
        gary.setpos(x,y)
        gary.dot(25, color)
        # One thing to note is that the pen isn't used to draw a dot
        # So pen up can draw a dot too, and pen color isn't dot color
        x += 50
    y += 50
    x -= 500
# As expected the course solution had a single loop upto 100 with an if statement
# at each 10 dots to reposition using setheading() and forward() rather than setpos()

# Need this mandatorily for now
screen = t.Screen()
screen.exitonclick()
