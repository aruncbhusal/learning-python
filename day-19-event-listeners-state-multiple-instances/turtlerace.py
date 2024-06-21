import turtle as t
import random

screen = t.Screen()

screen.setup(width=1000, height=800)
# The parameters can be in float to indicate a percentage of the screen
# As integers, they indicate the number of pixels on the screen

user_bet = screen.textinput(title="Turtle Picker"
                 , prompt="Which turtle do you think will win? Enter a color:")

# To understand the turtle co-ordinate, we need to observe that when a
# Turtle object is created, it is at co ordinate 0,0 which is at center
# so in our case, the width=1000 and height=800 so the co ordinates will
# look like X:(-500,500) and Y:(-400,400)

# For the turtles, the colors will be from the rainbow:
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# In the course, there was a list for y positions too but it was
# much cooler to let the code handle that by itself.
# Let's create an initializer function for the turtles that will race
def newturtle(index):
    # Since we know we have 6 turtles, we can adjust it for that
    gary = t.Turtle(shape = "turtle")
    gary.resizemode("user")
    gary.shapesize(stretch_wid=2, stretch_len=2)
    # We can initialize gary as a turtle from the constructor itself
    gary.up()
    # Since we won't be drawing anyway, we can keep it up the whole time
    gary.color(colors[index])
    y_pos = -180 + index*60
    # Since 6 turtles spaced out by 60 will be 360 so start from -180
    gary.goto(x= -480, y=y_pos)
    # The X position is close to left border but not incident on it 
    # Looks decent but I think the size should be bigger soo
    # I put them above since I want them large to begin with, not end
    return gary

garies = []
for i in range(6):
    garies.append(newturtle(i))
    
# For the race the main idea is to have a random movement between 1 and 10
# The race will not start until user has placed their bet
race_continue = False
if user_bet:
    race_continue = True

finishline = 440
# A turtle is 40x40 by default, but we have doubled its size so in order to
# have the turtle just touch the finishline, we have to finish 40 pixels ago

# Let's draw the finishline while at it:
def draw_finishline():
    f_line = t.Turtle()
    f_line.hideturtle()
    f_line.up()
    f_line.goto(x=finishline+40, y=350)
    f_line.pensize(20)
    f_line.down()
    f_line.setheading(270)
    f_line.fd(700)

draw_finishline()

while race_continue:
    for gary in garies:
        gary.forward(random.randint(0,10))
        if gary.pos()[0] >= finishline:
        # We could use gary.xcor() instead of this complex thing as per course
            winner = gary
            # We can instead get the winner's color with gary.pencolor()
            race_continue = False

winner_color = colors[garies.index(winner)]
# We could use winner.color() but it returns a tuple of pencolor and fillcolor
# This is why you should take a look at documentation rather than doing it yourself
if winner_color == user_bet.lower():
    print(f"Congratulations! {winner_color.capitalize()} turtle won the race!")
else:
    print(f"You lose! {winner_color.capitalize()} turtle won the race.")
screen.exitonclick()