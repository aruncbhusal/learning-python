# This time we're learning conditional statements and logical operators it seems
# Let's first make the roller coaster mini program in the course
print("Welcome to the Roller Coaster Ride!")
height = int(input("Enter your height(in cms): "))
if height >= 120:
  print("Go on right in, you can ride the thingy!")
  # This revision to the above program was done after the odd/even program below:
  # This time nested if statements are used to set the ticket prices
  # The ticket prices are dependant on the age of the person
  age = int(input("Enter your age: "))
  ticket = 0;
  if age <12:
    ticket = 5
    print(f"Hey buddy, the child ticket price is ${ticket}.")
    # Now we're working with elif statements too.
  elif age<=18:
    # We need not put >=12 condition here because that is already confirmed
    # by the non-execution of the previous if statement
    ticket = 7
    print(f"Hi. The teen ticket price is ${ticket}.")
  # This next LOC was added after learning about logical operators
  # Basically, if the person is having a midlife crisis, they get a free ticket
  # So I made an elif to separate out those people and give them default 0$ ticket
  elif age>=45 and age<=55:
    print(f"The midlife crisis ticket price is ${ticket}. Enjoy the free ride!")
  else:
    ticket = 12
    print(f"The adult ticket price is: ${ticket}.")
  # Now I've modified the above print statements for multiple if example
  # Now a variable stores the ticket price and age class is specified in print
  
  want_photo=input("Do you want a photo taken? (Y/N): ")
  if want_photo=="Y":
    ticket += 3
  # I initially had an else statement here, but that mandated two print statements
  # So I took the print statement out of the if block so it would run in any case
  print(f"Your final ticket price is ${ticket}.")

else:
  print("Oh dear, you're too short for the ride, maybe after you grow taller! :(")

# Okay the mandatory Odd/Even Program now
number = int(input("Enter a number to find odd or even"))
if number%2==0:
  print("It is even!")
else:
  print("It is odd!")

# Now extending on last day's BMI calculator
height=float(input("\nBMI Calculator\nEnter your height in m: "))
weight=int(input("Enter your weight in kg: "))
bmi = round(weight/height**2,2)
if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi<25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi<30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi<35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

# Let's check for a leap year now
# I'm gonna do this without logical operators (using nested loop)
# as those have not yet been introduced in the course
year=int(input("\nLeap Year Checker\nEnter a year: "))
if year%4==0:
  if year%400==0:
    print("It is a leap year!")
  elif year%100==0:
    print("It is not a leap year.")
  else:
    print("It is a leap year!")
  # As I'm writing this, I know that I could just nest it again
  # While solving the interactive exercise, I nested them all up like the solution
  # to check for 100 and 400 but I thought I should make use of elif instead
else:
 print("It is not a leap year.") 

# Onto a mini program to automate pizza order selection:
print("Welcome to the Pizza Plaza!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# For the sake of this challenge, base pizza is $15,$20,$25 for S,M,L
# Pepperoni costs 2$ for small and 3$ for medium and large and extra cheese is $1
price = 0
if size=="S":
  price = 15
elif size=="M":
  price = 20
elif size=="L":
  price = 25
# At this point I thought I may as well add some error checking
# Though it doesn't alter the control flow because that hasn't been taught yet
else:
  print("Invalid input! Disregard the next input")

if add_pepperoni == "Y":
  if size=="S":
    price += 2
  else:
    price += 3
if extra_cheese == "Y":
  price +=1
print(f"Your final bill is: ${price}.")

# Next up was love calculator where we are given two names and
# we calculate love score by counting how many times the letters in
# "true" and "love" appear in total in the names
# lower() and count() are the functions used for this program

print("\nLove Calculator")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
# In my attempt, I applied the functions to both names separately,
# which made it a whole lot messy. So this time I'll do as hinted in the course
# by first concatenating the names before applying the functions
name = name1 + name2
name = name.lower()

count_true=0
count_love=0
# In the course each letters are kept count individually
# But I found it more convenient to do it all in one line
count_true += (name.count("t") + name.count("r") + name.count("u") + name.count("e"))
count_love += (name.count("l") + name.count("o") + name.count("v") + name.count("e"))

love_score = int(str(count_true)+str(count_love))
if love_score<10 or love_score>90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>40 and love_score<50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")

# For the final challenge for the day we will create a CYOA game
# It will have a few options to choose from, most will lead to game over
# There's one path that leads to the good ending
# So we got to use nested if-else to achieve the process
# We use ASCII art from ascii.co.uk/art and delimit with triple single quotes
# That way we can print a multiline string without terminating the print

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')
print("Welcome to:")
# This was not in the course but I thought it would be cool to add some funky text
# So I looked up Text to ASCII generators and used this:
print('''
___________                                                     ___ ___               __   
\__    ___/______   ____ _____    ________ _________   ____    /   |   \ __ __  _____/  |_ 
  |    |  \_  __ \_/ __ \\__  \  /  ___/  |  \_  __ \_/ __ \  /    ~    \  |  \/    \   __\__
  |    |   |  | \/\  ___/ / __ \_\___ \|  |  /|  | \/\  ___/  \    Y    /  |  /   |  \  |  
  |____|   |__|    \___  >____  /____  >____/ |__|    \___  >  \___|_  /|____/|___|  /__|  
                       \/     \/     \/                   \/         \/            \/      
''')
print("You are stranded on a deserted island. All you know is you have to find the treasure.")
print("You have two options to choose from. You can either go left or right.")
direction = input("Which direction do you want to go? Left or Right: (L/R) ")
if direction.lower()=="l":
  print("You come across a river. You can choose to swim across or wait for a boat.")
  river = input("Do you want to swim or wait? (S/W) ")
  if river.lower()=="w":
    print("You come across a house with three doors. One is Red, one is yellow and one is blue")
    door = input("Which door do you want to enter? (R/Y/B)")
    if door.lower() == "y":
      print("Congratulations, you found the treasure! You Win!")
    elif door.lower() == "r":
      print("There was fire beyond the door. You were burnt. Game Over!")
    else:
      print("You were attacked by a beast. Game Over!")
  else:
    print("You were eaten by trout. Game Over!")
else:
  print("You fell into a hole. Game Over!")