from turtle import Turtle
import random
SCREEN_LENGTH = 600
SCREEN_WIDTH = 600

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("green")
        self.speed(0)
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