# Along with simple decorators which simply run the function with some additional
# code before/after it, we may want to add more control to it by using arguments
# We can also specify *args and **kwargs so that whenever we're using the decorator
# The argument passed to the function to be decorated is now an argument to the
# decorator as well

# Suppose we want to create a bank account class that holds money
class Account():
    def __init__(self, name):
        self.name = name
        self.balance = 0
        
# Let's add a decorator that only gives the person the candy if their balance
# is greater than 10
def check_balance_decorator(function):
    def wrapper(*args, **kwargs):
        print("\nPlease wait, payment processing...")
        if args[0].balance>=10:
            # We want to access the first positional argument so we used index 0
            # And the argument specified below is an "Account" object
            function(args[0])
        else:
            print("Insufficient balance, earn first!")
    return wrapper

# Let's say the user can buy candy with the money
@check_balance_decorator
def buy_candy(person:Account):
    print(f"Here, {person.name} you go, have a candy!")
    
jack_acc = Account("Jack")
buy_candy(jack_acc)
# Without any decorator, the function will give Jack a candy every time
# even though he has a zero balance
# But with the decorator added, Jack will not be able to buy a candy
# Let's now get Julia, who is rich enough
julia_acc = Account("Julia")
julia_acc.balance = 10000
buy_candy(julia_acc)
# Now we can see that Jack isn't given the candy but Julia is.
# This is how we can use decorators in a more advanced way

# Now the Interactive Code Exercise No.36
# The last of thisexercise in this course, and it's another advanced decorator task
# The task was to return the name of the function as well as the value it returned
# without modifying the original function, by just using decorators
# This was my solution:

inputs = [1,2,3]
# This was the decorator function I wrote:
def logging_decorator(function):
  def wrapper(*args):
        # print(f"You called {function.__name__}{tuple([arg for arg in args])}")
    # Looks like I made it overly complicated and I could have just used args
    # and it would have given me the same as my tuple converted list comprehension
    print(f"You called {function.__name__}{args}")
    print(f"It returned: {function(*args)}")
    # The course solution didn't include this usage of *args, but hey at least I
    # discovered something on my own by trial and error. Good start
    # The course solution took all three args by their indices and produced result
  return wrapper

# I only added the next line below, everything else was given in question
@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])