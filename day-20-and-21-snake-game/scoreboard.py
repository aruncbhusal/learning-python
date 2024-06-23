# In this file we're going to have a new class Scoreboard
# which will also inherit from turtle and it will display score
# I need to take a look at the documnetation to see how to do it

from turtle import Turtle
import time
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ALIGNMENT = "center"
FONT_SIZE = 15
# ^ This was unnecessary
FONT = ("Arial", FONT_SIZE, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # We need to use the turtle method write() to do it
        # but first let's take the turtle to the top
        self.hideturtle()
        # Maybe needed I don't know
        self.color("white")
        self.up()
        self.goto(0, SCREEN_HEIGHT/2 - 20)
        # Need to set x as 0 for center
        # Now let's define the fstring for the score
        self.score = 0
        self.show_score()
        
    def show_score(self):
        # Finally we can now call the write() method
        self.write(arg = f"Score: {self.score}", move = False
                   , align = ALIGNMENT, font = FONT)
        # move = True would have set position to corner
        
    # def strobe(self):
    #     self.color("green")
    #     time.sleep(0.1)
    #     self.color("white")
    # I want to make it work but I don't know how so maybe later
    
    def score_up(self):
        self.score += 1
        self.clear()
        self.show_score()
                # self.strobe()
                # # Just wanted to add this as an added functionality
                
    def game_over(self):
        self.goto(0, 0)
        self.write(arg = f"GAME OVER", move = False
                   , align = ALIGNMENT, font = FONT)