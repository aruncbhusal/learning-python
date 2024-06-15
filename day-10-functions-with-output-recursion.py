# In today's lessons I'll be learning about functions with outputs
# The final flavor of functions after functions without and with inputs
# The return keyword is used to set an output to a function
# The first task was to input name and return it in title case (first letter capital)
def format_name(f_name,l_name):
  # Apparently there's an entire function called title() that can get it done
  fullname = (f_name + " " + l_name).title()
  # We can also have multiple returns or even empty returns in a function
  if f_name == "" or l_name == "":
    return
    # This will return nothing if both inputs are empty
  return fullname
  #Instead of this we could also have used the formatted string like in print:
            # formatted_f_name = f_name.title()
            # formatted_l_name = l_name.title()
            # return f"{formatted_f_name} {formatted_l_name}"
  
print(format_name("DoNalD", "RobINsON"))
print(format_name(input(), input()))
# In the above case, it seems it prints "None" instead of just nothing

# In the interactive code challenge for today, we had to find th number of days
# in any given month of any given year, and we were given a is_Leap() function
# First I turned the is_Leap() from printing status to returning True or False
# Then I worked with a function which already had a list of no. of days:

        # def days_in_month(year, month):
        #   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
          # if is_leap(year) and month == 2:
          #   return 29
          # else:
          #   return month_days[month-1]
# I'm not sure whether the solution would be the same as this though
# Wow, unexpected but it was ditto. Think like a programmer huh

# We can create our own docstrings (sort of like instruciton documentations
# for our function); when we hover over function or press opening parantheses
# The first line inside the function must have it inside triple quotes for that
def mynameis():
  """A function that just prints my name. (Prank)"""
  print("I don't have a name")
mynameis() # As I was writing this, it promped me with the documentation I wrote

# Next is a simple calculator app that has a single history feature too
# The course suggested I go along with it, but I want to give it a try first
# First the mandatory art from the course:
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
from os import system
def operation(a,b,op):
  if op == "+":
    return a+b
  elif op == "-":
    return a-b
  elif op == "*":
    return a*b
  elif op == "/":
    return a/b

def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b

operations = {
  "+" : sum,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  print(logo)
  num1 = float(input("Please enter the first number: "))
  # This was initially "int" but we want to be able to handle float as well so added it here
  #operator = ""
  #while operator != "+" or operator != "-" or operator != "*" or operator != "/":
  # I don't feel like above 2 lines were very relevant for this problem.
  # So I'll comment them until necessary
  # to_reset = False
  # while to_reset == False:  
            # operator = input("+\n-\n*\n/\nPick your operation: ")
  # Since we have a dictionary, we can instead write it this way
  for op in operations:
    print(op)
  operator = input("Pick your operation: ")
  num2 = float(input("Please enter the second number: "))
  # The following code is my initial implementation without using dictionaries or separate fns
            # result = operation(num1, num2, operator)
  # Now this code is what I think was used in the course to replicate it all:
  function = operations[operator]
  result = function(num1, num2)
  
  print(f"{num1} {operator} {num2} = {result}")
  to_continue = input("Do you want to continue with this result (y) or start with a new one? (n): ")
  if to_continue == "y":
    num1 = result
  else:
    system("cls")
    calculator()
    # Not much point in making this recursive but well that's what it is.
    # to_reset = True

calculator()
# Though the course mentions the use of dictionary, I will need to update the
# above code accordingly for that
# But it works just as the demo showed, so no problem with that I guess.
# The first difference with the method in the course is that
# she had multiple functions, one for each operation, rather than the same one for all
# Okayyy so she uses the dictionary to mimic my ease of access, by putting operators as keys
# and the individual functions as values, makes sense since each operator would call specific fn
# I feel like I should give it a go as well. I might comment out my original code then

# One of the differences between printing to the console vs returning the value fromt the function
# is that we can then use the value that was returned in another function or some other place

# In the course, recursion was used instead of while(True) which causes certain overhead
# but for learning purposes it should be fine so I'll implement that as well discarding while(True)