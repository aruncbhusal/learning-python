# Important Note: The code will not work since there are functions that have not been defined
# It is done for a good cause, so read the documentation to see what the purpose was

# Functions are blocks of code that are designed to do one specific job.
# Python has a lot of built-in functions, but we can define our own as well.
# Functions like abs(), len(), range(), int(), print(), type(), etc are built-in
# We can define our own functions using the def keyword
def turn_left():
  print("Lefter than before.")
def move():
  print("One step forward.")
# Functions help to improve code readability and reduce repitition
# Say we had a code to turn left but none to turn right
# We can define our own function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# Here the indentation is very important, breaking this gets us out of the function
# To call the function, we simply need to type the name of the funciton
turn_right()
# The problem was in the website Reeborg's World and in next one I had to
# get the robot to the flag, and since I noticed there were 6 hurdles to jump
# I created a jump function and this is how it went:
def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

for i in range(1,7):
  jump()
# Now these codes will not run as they are meant for some other place
# So I'll create some dummy functions at the start for good measure
# We can instead use a while loop that loops until the i/step reaches 6 from 1
# while loop is preferred when we don't know the exact count of the iterations
# So if we had say a condition to check if we're at the goal, we would use while
i = 0
while i < 6:
  jump()
  i += 1
# For functions that return a boolean, we can check for a condition != True or
# just simply "not condition" to check for the negation.
# The Reeborg's World Code is hard to transport here while retaining meaning
# So I'll just do it there and add the last challenge's code here.

# A challenge had walls at random position so I had to use a function wall_in_front
# and if there's a wall, jump over it, else just move forward. Simple logic
                # def jump():
                #   count = 0
                #   turn_left()
                #   while wall_on_right():
                #     move()
                #     count +=1
                #   turn_right()
                #   move()
                #   turn_right()
                #   move()
                #   for i in range(1,count):
                #     move()
                #   turn_left()
  # Though instead of this, there was a much more elegant solution without for loop
  # Because I missed the fact that there was a front_is_clear() function
  # And that the floor too counted as a wall, so we could just write the above as:
          # def jump():
          #   turn_left()
          #   while wall_on_right():
          #     move()
          #   turn_right()
          #   move()
          #   turn_right()
          #   move()
          #   while front_is_clear():
          #     move()
          #   turn_left()
                
                # while not at_goal():
                #     if wall_in_front():
                #         jump()
                #     else:
                #         move()

# The last challenge was a maze where we're given a hint of the algorithm
# We move right whenever possible, else we move forward, but if that is not possible
# We turn left and see the options until we reach the end
# I used the following logic to get me through to the end:
while not at_goal():
  if right_is_clear():
      turn_right()
      move()
  elif front_is_clear():
      move()
  else:
      turn_left()
# But even this simple progam has en edge case where it fails
# Resulting in an infinite loop, so I have to now follow the course
# Since I can't think of a way to solve this bug. End of Thinking Capacity?
# The problem I overlooked is that there is never wall on the right in these cases
# So I need to get it to somewhere where there is in fact a wall on the right
# There were three test cases which caused the infinite loop and with this info
# I was able to get through them by adding another while loop before the if block
# that moved to the wall in front of it and ensured a wall on the right with a
# whie not wall_in_front and front_is_clear() but on further testing, it caused
# an infinite loop on some other test case I noticed, so I resorted to the course
# The solution included ensuring a wall on the right by moving forward until
# there was a wall at front, then turning left so that this wall was on the right
# So we add the follwing before the while block:
while front_is_clear():
  move()
turn_left()
# I wonder how long this would have taken me, but if I took too long, my day
# would be wasted, so I'm glad I just looked up the solution
# This is it for today, Hangman tomorrow I think