from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        
    def create_snake(self):
        for pos in START_POS:
            self.create_part(pos)

    def create_part(self,position):
        part = Turtle(shape = "square")
        part.up()
        part.color("white")
        part.goto(position)
        self.body.append(part)
        
    def extend_snake(self):
        self.create_part(self.body[-1].position())
    
    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.body[0].fd(MOVE_DIST)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
           
    def reset_snake(self):
        for part in self.body:
            part.forward(1500)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]