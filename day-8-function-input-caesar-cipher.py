# First thing we're learning today is functions with inputs
# First let's make an example function recalling what we learnt in Day 6
def greet():
  print("Howdy! The weather's nice today innit?")
greet()

# Next we'll add an input to the function to make the function more useful
def greet(name):
  print(f"Hey {name} how do you like the weather today?")
greet("Mark")
greet("Emily")
# See how one function can cater to multiple people just by giving their name
# The variable "name" in the function definition will store the value
# that is passed while calling the function.
# In this example, name is called a parameter, and the actual names are arguments

# We can allow the function to take multiple inputs as well, for more specificity
def greetfrom(name, location):
  print(f"Hi {name} I heard you're from {location}, how is the weather there?")
greetfrom("Stan", "Holland")
# Positional Arguments: In this example, we called the function with the arguments
# "Stan" and "Holland", with their position corresponding to the parameters we want
# to associate them with. Let's see what happens if we reverse the position:
greetfrom("Holland", "Stan")
# This is not the intended output. However we can disregard the position if we use
# Keyword Arguments: Use assignment in the argument to bind the value with parameter
greetfrom(location = "Tasmania", name = "Stacy")

# The interactive challenge was to solve a math problem using function inputs
# We needed to calculate number of paint cans required to paint a wall, size given
# A formula was given, which we needed to round up (even if it's 2.1 make it 3)
# Anyway, this is how I went through it, but a stackoverflow link was given as well
def paint_calc(height, width, cover):
  cans = int((height * width)/cover)
  if cans%cover != 0:
    cans += 1
  print(f"You'll need {cans} cans of paint.")
paint_calc(width = 11, height = 5, cover = 6)
# Here cover means number of square units of wall that a can of paint can cover
# From StackOverflow I learned about two things:
# 1. You can be cheeky and leverage the fact that a boolean is either 1 or 0:
# cans = int((height*width)/cover) + ((height*width)%cover)
# 2. You can import ceil from math module and use it as:
# cans = math.ceil((height*width)/cover)

# The next interactive exercise was a prime checker with a number as input
# And since I've already done it like a hundred times, this was a breeze
# I'm looking forward to see what the solution suggested in the course is. Mine:
def prime_checker(number):
  factors = []  # Check below code to see reason for this
  prime = True
  for i in range (2,int(number/2)+1):
  # As expected, the course includes the range (2,number)
    if number%i == 0:
      factors.append(i) # Out of scope for the given question
      prime = False
  if prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    # I had to look the following up, I have yet to learn inline for loop though
    print(f"Divisible by: {', '.join(str(i) for i in factors)}")
prime_checker(247)
# As a personal touch, I want to add a list to this to keep a record of
# the factors of a number, if it is not a prime. So I'll now add it

# Now the final part of today, the Caesar Cipher, a text encoding technique
# used since Julius Caesar's times, by shifting each letter by a fixed number
# i.e. 'a' becomes 'e' if the shift is set to 4, and so on
# The following code was already given in the course so we'll just work from there
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
# This art file was provided in the last part: User Experience

# In the last part, restarting the game was an added functionality, so I add it here:
keep_going = "yes"
print(logo)
while(keep_going == "yes"):
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) % 26
  # An edge case was for when shift is greater than 26. To fix it we get a modulo
  
  # Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
  def cipher(text, shift):
  # It is good practice to not name parameters and arguments the same, but meh
    encrypted_text = ""
  # Inside the 'encrypt' function, shift each letter of the 'text'
  # forwards in the alphabet by the shift amount and print the encrypted text.
    for ch in text:
      if ch in alphabet:
        new_index = alphabet.index(ch) + shift
        if new_index > (len(alphabet)-1):
        # In the course, the index out of range issue was handled by duplicating
        # the elements of the list at the end, since index only returns the position
        # of first encounter. I used this because space complexity and more logical
          new_index -= len(alphabet)
          # I'm using len(alphabet) instead of 26 for no particular reason
        encrypted_text += alphabet[new_index]
      else:
        encrypted_text += ch
        # This was for the case where a space or any other character is in the text
        # Unsuprisingly, this was not included in the encrypt lecture of the course
        # And unsuprisingly, it was included in the last lecture, so one more step ahead..
    print(f"Result text: {encrypted_text}")
    # Originally had it as "encoded text" but I'm using it for decode too sooo
  
  if direction == "encode":
    cipher(text,shift)
  elif direction == "decode":
    cipher(text, -shift)
  else:
    print("Are you dumb? That's not what I asked you to write! Try again")

  # This LOC was added in the final step:
  keep_going = input("Do you want to do it again? [yes/no]").lower()
print("Thanks for using the Caesar Cipher!")

# In the course, it was suggested that I create a new decode function
# But instead I'll try adding some code to the function above to make it work
# by just making the shift variable negative.
# One thing that makes this easy is that in python negative index means go from back
# which means I won't need another if to avoid an out of range for negative index
# I can't believe I didn't have to change the function at all (except print) for this

# Wow, in the next video, she just suggested to combine the two functions
# A step ahead, am I now, and as I expected, she passed "direction" as an input too
# And her method also included the shift *= -1 line, I anticipated that from the start

# That's it for today I guess