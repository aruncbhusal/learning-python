# This was done on the same day as day 18 because it's Friday!
# In this lesson I'll be learning about an important part of games
# INTERACTIVITY. Event listeners are functions that take user input
# to make changes to the program, like a click or a keystroke
# The turtle library has a listen() method in Screen class for it

from turtle import Turtle, Screen

gary = Turtle()
screen = Screen()

        # def moveforward():
        #     # I'll be using this function on a keypress to demonstrate
        #     gary.forward(10)

gary.pensize(2)

screen.listen()
            # screen.onkey(key="space", fun=moveforward)
# Here, the onkey is a higher order function, that takes another function
# i.e. it binds the function to the key press
# as an argument, and when we do this, we don't use the parentheses,
# because we want the function to be triggered only when the event is True

# Our goal now is to create an Etch-And-Sketch program which we can use
# To draw anything on the screen. The following key bindings to be used:
# 1. Move forward - 'w', move backward - 's'
# 2. Turn left a bit - 'a', Turn right a bit - 'd'
# 3. Clear the screen - 'c'
def moveforward():
    # In order to use a function as an argument for higher order function,
    # We need the called function to have no arguments of itself
    gary.fd(10)
    
def turn_left():
    gary.left(10)
    
def turn_right():
    gary.right(10)
    # We can also use the setheading() method to increase heading by 10
            # gary.setheading(gary.heading() + 10)

def movebackward():
    gary.bk(10)
    
def clearscreen():
    screen.reset()
    # I knew I took the easy route with this one, the course uses a method
    # that I did think of, but felt that this was a lot more straightforward
                # clear() -> up() -> home() -> down()
    # Using the above sequence of turtle methods we can replicate the above
    # If we used the screen method clear() the turtle would get deleted too.
    
screen.onkey(key = "w", fun = moveforward)
# It is suggested to use keyword argument here because we might get confused
# about the position of the arguments in functions we didn't define ourself
screen.onkey(key = "a", fun = turn_left)
screen.onkey(key = "d", fun = turn_right)
screen.onkey(key = "s", fun = movebackward)
screen.onkey(key = "c", fun = clearscreen)
# onkeypress() is basically the same as this one, but defaults to any key if not given
# onkeyrelease() method is similar but it triggers when key is released, not pressed

 

screen.exitonclick()
# We still need to hold the screen to see the effect