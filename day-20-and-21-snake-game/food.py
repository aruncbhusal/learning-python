# We will use this file to inherit from the Turtle class
# and make the food its own Turtle like object, just with
# additional features of itself

from turtle import Turtle
import random
SCREEN_LENGTH = 600
SCREEN_WIDTH = 600

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        # Now we can just use the methods from Turtle in Food
        self.shape("circle")
        self.penup()
        # We want the dot to be small, say 10x10px so we use it
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        # It takes stretch_wid, stretch_len and/or the outline
        # Since the values are float, they are relative, not px
        self.color("green")
        self.speed(0)
        # 0 means the fastest speed so I'll skip the animations
        # Next we need it to appear at a random location
        self.good_xpos = SCREEN_LENGTH/2 -20
        self.good_ypos = SCREEN_WIDTH/2 -20
        xpos = random.randint(-self.good_xpos, self.good_xpos)
        ypos = random.randint(-self.good_ypos, self.good_ypos)
        self.goto(xpos, ypos)
        
    def refresh(self):
        """A new food will be generated someplace else"""
        xpos = random.randint(-self.good_xpos, self.good_xpos)
        ypos = random.randint(-self.good_ypos, self.good_ypos)
        self.goto(xpos, ypos)