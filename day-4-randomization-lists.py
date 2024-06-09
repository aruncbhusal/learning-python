
# Looks like we're starting today with random number generation
# For this we need the random module
import random

# First let's do as in the course and get a random int and a random float
random_int = random.randint(1,10)
print(random_int)
random_float = random.random()
print(random_float)
# Since the random() method returns between 0.0 and 1.0 (Right non inclusive)
# We need to multiply it with a number for larger ranges
large_random_float = 10 * random.random()

# As per the challenge, let's flip a coin, heads when 1 and tails when 0
hot = random.randint(0,1)
if hot == 1:
  print("Heads")
else:
  print("Tails")

# And since the course heads towards list, these are some more things I read
# about the random module from askpython.com
random.seed(1)
state = random.getstate()
print("Here is a sequence of two random numbers: ")
print(random.randint(1,1000))
# Since a pseurandom number is based on the previous number, I'll reset the state
random.setstate(state)
print(random.randint(1,1000))
# We can also print over exponential distributions, Normal, Gaussian, etc.
# We can also shuffle and choose from a list but let's first learn list from course.

# So list is a data structure that can even be inverted in place, neat!
# I took a list from the course repo and let's see how it works:
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# We can access and assign values to the list using the index
print(dirty_dozen[3])
dirty_dozen[5]="Mango"
# When displaying the entire list, it displays in the format that we would input it
print(dirty_dozen)
# There's a whole lot of methods for lists, but Angela suggested to not try
# to remember them, but know what they make possible, so we know where to look later
dirty_dozen.append("Banana")
# Okay this next line it outta pocket but I don't want to print the whole list sooo
print(dirty_dozen[len(dirty_dozen)-1])

# Now the test problem that requires us to randomly choose a name from a list
# The person who is unlucky will pay for the meal
names = ["John", "Michael", "Julia", "Andrew", "Shila"]
unlucky = random.randint(0,len(names)-1)
print(names[unlucky] + " is going to buy the meal today!")
# In the test, a string method is used to create a list of names from a string
# We can use split() method to create a list from a string when the list items
# are separated by something, that delimiter must be placed as a parameter to split

# List can also be nested inside each other it seems. I'll create one myself
# since we seem to have used the one used in the course already above
boy_names = ["Grey", "Shawn", "Mike", "Brad", "Austin"]
girl_names = ["Margaret", "Jennifer", "Brianna"]
child_names = [boy_names, girl_names, "Charlie"]
# Accessing them is a bit tricky since we have to be wary of the indices
# The first index is to select the element within the main list
# if there's a second index, it means the index of element within selected sublist
print(child_names)
print(child_names[0])
print(child_names[2])
print(child_names[1][2])

# Now this is a "difficult" challenge given in the test series
# I did it one way, but upon looking at the solution, I saw yet another way to do it
# There was a blank treasure map where we needed to mark an X as per player's input
# The input is in the format "(alphabet)(number)" from A1 to C3
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")
# This is the way I solved it:
row = int(position[1]) - 1
column = 0
if position[0] == 'B':
  column = 1
elif position[0] == 'C':
  column = 2
# But there's another way to solve it as well, using the index() method:
letter=position[0].lower()
alpha=['a','b','c']
column=alpha.index(letter)

map[row][column]='X'
# Now the next line was already in the challenge, to print the final map:
print(f"{line1}\n{line2}\n{line3}")

# The final task for the day is the rock, paper, scissors game player vs computer
# The ASCII art for all of these options were provided in the course so I'll use it
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Here begins my solution:
print("Rock Paper Scissors")
choice = [rock, paper, scissors]
player_choice = int(input("Choose your move: Rock (0), Paper (1), Scissors (2): "))
if player_choice >=3 or player_choice<0:
    print("Invalid choice, try again!")
else:
    print(choice[player_choice])
    print("Computer Chose: ")
    computer_choice = random.randint(0, 2)
    print(choice[computer_choice])

    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice ==0) or (player_choice == 2 and computer_choice ==1):
        print("You win!")
    else:
        print("You lose.")
# One thing to notice here is that I didn't put an error checking in place, so an invalid value will cause an error
# So even though it looks like I did the error checking, I actually added it on later

# Now I basically bruteforced my way through with multiple scenarios to get my code working
# But in the course, another way, which I did think of while solving this, appeared
# apart from the case in which player choice is 0 and computer choice is 2,
# we can see that the higher number wins so we can have a whole if-elif block for an exception for 0 and 2
# and then a general elif for user choice > computer choice
# the rest of the outcomes are where user loses. The course actually had conditions for both user winning and losing
# but instead I intend to have the user losing in just the else block. This is what I came up with:
# if (user == 0 and comp == 2) or (user>comp and user !=2):
#     print("You win")
# elif user == comp:
#     print("It's a draw!")
# else:
#     print("You lose")