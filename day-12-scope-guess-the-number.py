# In day 12, we will be learning about scope and namespaces first.
# A scope is dependent upon where a variable, function or anything in a namespace
# is defined. A scope can be local or global. To demonstrate, here is my example:
# These are global variables, and have a global scope:
temperature = 20
enemies = 2

def in_house():
  # We can access the global variables from this function too
  print(f"Temp: {temperature}, Enemies: {enemies} in house.")
  # temperature = 30     This is not allowed because of naming conflict
  # This is a local variable with a scope only inside in_house()
  temper = 30
  print(f"House temp increase to {temper}")
  
  def in_room():
    # This is a function nested inside in_house
    temperature = 40
    pet = "Jenny"
    print(f"{pet} lives in the room with temperature {temper}")
    print(f"Global temperature changed to {temperature}? or maybe not?")
    # See that temper can be accessed in this function as well because within scope
    if 2>1:
      cat = 24
    else:
      cat = 0
    print(f"Number of cats: {cat}")
    # I defined cat inside if but I could still access it outside of it
    # So there is no such thing as block scope in python, if, for, while, nothing

  # But print(pet) wouldn't work here since it is out of scope of in_room()
  # I can't access 'cat' either since it is bound to the scope of in_room() too
  in_room()

in_house()
print(f"The temperature here is {temperature} and enemy count is {enemies}")
# We can see the temperature in global scope stays the same even if we change it
# inside of a function, since the variable there would be a local variable

# It is possible to modify global variables within a function
def more_enemies():
                  # enemies = 5
  # This code above creates a local variable with value 5
  # But we know the value will revert when we go out of scope. So we can do:
  global enemies
  enemies += 10
  # If we hadn't used the global keyword, the LOC above would have an error
  # We have read permission for global variables, but for writing, we need to
  # make it clear, and this is an error prone way so returning and assigning is good
  print(enemies)
more_enemies()
print(enemies)
# See how the enemies value will stay the same as inside the function?

# Global variables should be minimized but there are cases where it is used best
# Like defining a global constant, since we only need to read their value
# Naming convention in python is to have it all in upper case for better identity
PI = 3.1415926
def area(rad):
  return PI*rad*rad
print(area(3))

# The final task for today is the number guessing game, and this time, we're not given
# any hints, not that I'd be using them, but there's a demo to see how it goes but since
# I have an idea , I'll just explain the game here and then get on with the project:
# 1. A random number will be chosen at the start of each game betn 1 and 100
# 2. A prompt to choose the difficulty: Easy - 5 lives, Hard - 10 lives
# 3. The player keeps guessing and game lets them know their guess is low or high
# 4. If they guess it before lives run out, they win, otherwise they lose
# Okay simple enough, let's get started, but before that I'll see the demo once.

import random
art ="""
 ██████  ██    ██ ███████ ███████ ███████     ████████ ██   ██ ███████     ██████  ██  ██████  ██ ████████ ███████ 
██       ██    ██ ██      ██      ██             ██    ██   ██ ██          ██   ██ ██ ██       ██    ██    ██      
██   ███ ██    ██ █████   ███████ ███████        ██    ███████ █████       ██   ██ ██ ██   ███ ██    ██    ███████ 
██    ██ ██    ██ ██           ██      ██        ██    ██   ██ ██          ██   ██ ██ ██    ██ ██    ██         ██ 
 ██████   ██████  ███████ ███████ ███████        ██    ██   ██ ███████     ██████  ██  ██████  ██    ██    ███████ 
                                                                                                                   
                                                                                                                   
"""
# Used the text to ASCII art generator for this
# I didn;t see any replay functionality in the demo game. I don't see why
# people would want to replay this anyway, so I'll omit that too
print(art)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)

def set_difficulty():
  difficulty_not_set = True
  # Demo set difficulty to hard if there was any typo in saying easy
  # But I'm not so evil, I'll let them choose again
  while difficulty_not_set:
    difficulty = input("Pick your difficulty: Type 'easy' or 'hard': ").lower()
    difficulty_not_set = False
    if difficulty == "easy":
      return 10
    elif difficulty == "hard":
      return 5
    else:
      print("Please type the preferred difficulty in the next attempt.")
      difficulty_not_set = True

def gameover(lives,guess,number):
  if guess == number:
    print("Wow you guessed it! You win!")
    return True
  elif lives == 0:
    print("Aw no, you lost all your lives. You lose!")
    return True
  else:
    return False

def make_guess(guess):
  while not (guess > 0 and guess <= 100):
    guess = int(input(f"\nYou have {lives} lives left.\nMake your guess: "))
    if not (guess > 0 and guess <= 100):
      print("The number is between 1 and 100, pleasse try again.")
  return guess
# Dividing into functions though not strictly necessary because I put too much
# into error checking and user experience.

def check_guess(lives, guess, number):
  """Checks high or low (not equal) and returns the reduced number of lives"""
  if guess < number:
    print("Too low, try again.")
  elif guess > number:
    print("Too high, try again.")
  return lives-1

# My difficulty setting code is long, so I feel it's better to make it a function
# Just like it was done in the course, though mine has more features ;)
lives = set_difficulty()
guess = 0
while not gameover(lives,guess,number):
  guess = make_guess(0)
  lives = check_guess(lives, guess, number)

# Okay with all the coding and testing done, and not enough documentation
# Let me see the course solution for this and adjust my code accordingly
# Alright this is it for day 12, I might complete day 13 module today as well.