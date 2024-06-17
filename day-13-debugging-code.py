# In the 13th day module (which I did on the same day as I did 12th), we need to
# debug some code. The inital codes were given already, we just need to debug
# I'll mention any debugging I've done with documentation, others are from course

# The first step as per course: Describe Problem
def my_function():
  # for i in range(1, 20): <-------- Original LOC
  for i in range(1, 21): # Could also change to i == 19 but it is what it is
    if i == 20:
      print("You got it")
my_function()
# My solution in comments (assuming we need to print at the last step)
# Okay it was exactly the same as the course so let's move on


# Next step is to: Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
dice_num = randint(0, 5)
# It took me a while because I thought 6 wasn't included, but it is not range soo
# the index for list is from 0 to 5, not 1 to 6
# In the course, we tested by replacing randint() with possible values to see error
# i.e. dice_num = 1, dice_num = 2 and so on until 6 where we find the error
print(dice_imgs[dice_num])

# Another method is to: Play Computer
year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
if year > 1980 and year <= 1994:
  # We're assuming anyone born in 1994 is a millenial and covering that case
  # Otherwise there would be no result for an input 1994
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# # Fix the Errors (given by the IDE/Interpreter)
age = int(input("How old are you?"))
# First there was an IndentationError which I so indented the if block code
# Next, there was a TypeError in 41 which stated 'str' so age must be string
# To fix it, I casted the input function to an integer in the above code
if age > 18:
  # Then an error not shown by the IDE: a missing f inside print, causing the string
  # to not act as an intended fstring. Fixed it through coding prowess, as one should
  print(f"You can drive at age {age}.")

# Next tip: Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
# Since result came out as 0, let's check both the operand's values first:
        # print(f"{pages} {word_per_page}")
# From here we can see that word_per_page is stuck at 0. So looking at the line in
# which it was assigned. The LHS and RHS seem fine. Oh there's a double equals sign
# So it has been checking for equality rather than assigning a value. Fixed it.
# Job done so commenting out the print statement
total_words = pages * word_per_page
print(total_words)

# Final tip: Use a Debugger: For this one using pythontutor
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
# From the code it looks like the code is trying to double each element of a_list
# and append it to the empty b_list and then print it. I can see the bug right away
# but let's use the debugger(visualizer) and see at which step it is unexpected
# In the visualization, we see that the b_list doesn't get updated for each item in
# a_list since the appending line is not indented so it isn't inside for. Fixing that
# We can choose to set a breakpoint to see the execution of a particular line as well

# Some more tips from the course for debugging:
# Take a break and come back with a fresh mind
# Ask a friend or a mentor preferrably a developer
# Run the code and test it often, don't wait until end of production to see many bugs
# Search StackOverflow, and last resort, ask in StackOverflow

# Now this is the last batch of Interactive Coding Problems until day 26th. Let's go:

# 1. Debugging Odd or Even. The problem code: (Debugged by trial running)
number = int(input())
if number % 2 == 0:
# There was a single equals only above so I made it 2
  print("This is an even number.")
else:
  print("This is an odd number.")

# 2. Debugging Leap Year Code: (Debugged by trial running)
# It's a shame I couldn't debug by eye, but I wanted to be quick so I ran the code
# The int() cast was missing in the input so year stored a string, fixed that.
year = int(input())
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# 3. Debugging FizzBuzz Code: (Debugged by Eye then Trial Running)
# There were 3 bugs here, 2 I solved by eye but next I had to run
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
  # Bug 1: FizzBuzz is for when divisible by both, not any, else all is FizzBuzz
  # so I replaced 'or' with 'and' above
    print("FizzBuzz")
  elif number % 3 == 0:
  # Bug 3: This one I had to run the code for, there are multiple if statements
  # while there must only be one if...elif.. so changed both 'if's to elif
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    # Bug 2: print([number])
    # Replaced the above code, removing the brackets, which was making it a list
    print(number)

# That's it for this module. It's only 6:15 pm now, so I might get done with the
# next day's code as well. That will get me in line with my days of the challenge
# At least a bit close to it.