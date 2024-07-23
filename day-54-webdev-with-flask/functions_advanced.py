# Functions in python have a lot of options
# We can just use vanilla functions and call them by their name
# We can have functions that take arguments
# We can have functions that return a value
# But there's much more to functions in Python

# Functions in python are called First-class objects, meaning we can pass them
# as an argument to some other function, and call them within the other function
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def calc(operation, a, b):
    return operation(a,b)
print(calc(add,5,10))

# In this way we can treat functions just like we treat other objects like int,string

# Another feature for functions in python is that they can be nested within each other
def outer_f():
    print("You are outside")
    
    # Now I can have another function inside this function that can only be accessed here
    def inner_f():
        print("You are inside")
        
    # Now I could call it here, but there's another property of functions, they can be
    # returned by a function, just like any other object
    return inner_f

inner_function = outer_f()
# Now we can access the inner function since it was returned by the outer function before
inner_function()

# Now finally to the crux of the issue, the Python Decorator Function
# A decorator function is just a function that wraps another function that is supplied as
# its argument, and adds functionality before or after it.
# An example of decorator in effect:

def decorator_func(function):
    def wrapper_func():
        print("\nThe function will run shortly...")
        # Some code to run before running the function
        function()
        # We can even run the function twice
        function()
        # Some code to run after running the function
        print("Thanks for using the decorated function\n")
    return wrapper_func

@decorator_func
def hello():
    print("Hello there!")
# Here before the function definition we have used the '@' to have the function be decorated
# whenever it is called. This is called "Syntactic Sugaring", and it makes it easier to
# see that we are using a decorator function with this function

# What if we use it without any syntactic sugaring, let's define another function to do that:
def kenobi():
    print("General Kenobi")

# Calling the syntactic sugaring included function:
hello()
# Now for the other function:
decorated_func = decorator_func(kenobi)
decorated_func()
# We can easily tell which one is easier to discern and use.

# Finally, there was a code challenge for decorators, where we needed to measure the time taken
# by a function and print it. The two functions were given and we needed to create a decorator
# function to print the time taken to run that function. I also modified the functions a bit
# so that they return the function names to be used for printing. This was my solution:

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 
# The above lines were given already and I only wrote the decorator function below as well as
# the slight modifications to the functions

def speed_calc_decorator(funct):
  def wrapper_func():
    time1 = time.time()
    funct()
    time2 = time.time()
    name = funct.__name__
    # This didn't show up when I tried first, but seems it was in the hints already
    # What a waste of my intellectual prowess /s
    print(f"{name} run speed: {time2 - time1}")
  return wrapper_func

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
# Looks like this still returns the name "__main__" so I need to try something else
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()