from turtle import Turtle

# Here we will have a paddle class that will be on the right edge
# of the game boundary. Since my game has a resolution 1200x800
# instead of the 800x600 suggested in the video, I will just double
# everything and test it first

WIDTH = 20
MOVEMENT = 30

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.up()
        self.speed(0)
        self.shape("square")
        # It will be moving up and down only so this makes sense?
        self.setheading(90)
        # Since a turtle is 20x20px I can use it to set size 20x100
        self.shapesize(stretch_len = 5, stretch_wid = 1)
        self.goto(pos)
        # self.speed(6)
    
    # def on_side(self, dir):
    #     if dir == "left":
    #         self.goto(POSITION[0])
    #     elif dir == "right":
    #         self.goto(POSITION[1])
    # This function was for when the class didn't take position as input
    
    # In the course, the move functionalities were implemented with just
    # a goto and then a higher or lower co ordinate, since the heading for
    # the turtle was still set to 0. I think this is more efficient tho.
    def move_up(self):
        if not self.ycor() > 350:
            self.sety(self.position()[1] + MOVEMENT)
        
    def move_down(self):
        if not self.ycor() < -350:
            self.sety(self.position()[1] - MOVEMENT)