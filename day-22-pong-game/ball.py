# In this one we're going to be making a ball and makking it move

from turtle import Turtle
WALL = 380
BOUND = 600
PADDLE_POS = 530

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.shape("circle")
        # In the original pong game, the ball was a square
        self.orientation = 45
        self.pace = 12
        self.setheading(self.orientation)
        
    def move(self):
        self.forward(self.pace)
        # Yet again, in the course, she uses the following:
        # new_x = self.xcor() +10
        # new_y = self.ycor() +10
        # self.goto(new_x, new_y)
        # I wonder why. I like the setheading() method, but maybe
        # she's trying to stay true to the actual graphics roots?
    
    def collide_with_wall(self):
        if self.ycor() < -WALL or self.ycor() > WALL:
            return True
        else:
            return False

    def deflect(self, direction):
        self.orientation = 360 - self.heading()
        # The vertical reflection can be done easily with 360-x
        if direction == "horizontal":
            self.orientation = (self.orientation + 180) % 360
            # I wonder why this worked but it did.
            # For horizontal reflection, I just used 360-x+180
        self.setheading(self.orientation)
        # In the course, this is achieved by using co ordinate
        # just like in geometry by (x,y) -> (x,-y) for reflection
        # The method used in the course seems to be a neater way
        # to do this, but I like my solution too, since it took some
        # effort from my side as well, so I'll keep it until it breaks
        
    def hit_paddle(self, Paddle):
        # We can't just use the distance attribute since it measures
        # distance from the center, and the center of the paddle is
        # 50px away from the edge in our case, so we need 2 conditions
        if (self.xcor() < -PADDLE_POS or self.xcor() > PADDLE_POS)\
            and self.distance(Paddle) <= 50:
            self.pace = int(self.pace * 1.1)
            return True
        else:
            return False
        
    def miss(self):
        if self.xcor() < -BOUND:
            self.miss_side = "left"
            self.pace = 12
            return True
        elif self.xcor() > BOUND:
            self.miss_side = "right"
            self.pace = 12
            return True
        else:
            return False
            
    def regen(self):
        self.goto(0,0)
        # if self.miss_side == "left":
        #     self.orientation = 45
        # elif self.miss_side == "right":
        #     self.orientation = 225
        # self.setheading(self.orientation)
        # In the course, the orientation was set as the horizontal mirror
        # let's imitate that
        self.deflect("horizontal")
        # self.miss = ""