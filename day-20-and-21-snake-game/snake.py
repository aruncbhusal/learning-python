# This file will contain the snake class and all it's functionalities
# First when we create a snake object, the snake should be initialized
# to its starting positions and all the features will be handled here
from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# These are set as global constants that can be changed when needed

class Snake:
    # Now let's create a snake body
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        # self.head.shape("arrow")
        # self.head.color("red")
        
    def create_snake(self):
        for pos in START_POS:
            # I'll just create the starting snake here itself, no function calls
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
                    # for part in snake:
                    #     part.forward(20)
        # A problem here is that if we try to move, we don't know where to move
        # the other segments, apart from the head. So to counter that
        # We can move from the end to the postition of segment before and then
        # move the first segment in the desired direction
        for i in range(len(self.body)-1, 0, -1):
            # Since range function is derived from C, we can't use keyword args
            # The args are start, stop and step
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.body[0].fd(MOVE_DIST)
        
        # Let's make the snake change the direction now
    def up(self):
        # self.body[0].setheading(90)
        # Since we're using the snake head, let's have it as a separate attribute
        if self.head.heading() != DOWN:
            # We can't let the snake move backwards so
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
    
    
    # The newpart functions are in shambles, I'll make them later if they're no good

    
    # def obsolete_newpart(snake):
    #     # Since each snake body is a separate turtle we have to return
    #     # a new turtle each time a new body part has been added
    #     # To start, I will first make the snake just a 3 turtle-line
    #     part = Turtle(shape = "square")
    #     part.color("white")
    #     # Since a turtle is 20 px wide, we can use that knowledge to line up
    #     part.up()
    #     if snake:
    #     # Since we don't need to draw anything the snake will just be up
    #         last_part_location = (snake[-1].xcor(), snake[-1].ycor())
    #         last_heading = snake[-1].heading()
    #         dir = int(last_heading/90)
    #         part.setheading(last_heading)
    #         # The heading can be 0 90 180 270
    #         # which means even will be right/left(0,2) and odd up/down(1,3)
    #         rel_location = [(-20, 0), (0, -20), (20, 0), (0, 20)]
    #         newpos = (last_part_location[0] + rel_location[dir][0]
    #                 , last_part_location[1] + rel_location[dir][1])
    #         part.goto(newpos)
    #     return part
    # # The above code felt a bit too complex so I'll make a new function
    # # For the purpose with incremental features, like the course

    # def newpart(snake):
    #     part = Turtle(shape = "square")
    #     part.up()
    #     part.color("white")
    #     x = 0
    #     y = 0
    #     if snake:
    #         x = snake[-1].xcor()
    #         y = snake[-1].ycor()
    #         part.goto(x, y)
    #     return part
        
    
            
    
        
    # I wrote a whole lot of code to achieve this but the course focused first on
    # getting the first 3 turtles lined up so she used a list of tuple co-ordintes
    # Then used the tuple to set positions of 3 new turtles all formed in a loop