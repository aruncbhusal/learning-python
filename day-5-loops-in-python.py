import random
# Loops are used to run a block of code multiple times
# for loops are the most basic loop statements that can iterate through a list:
games = ["Fortnite", "GTA V", "Minecraft", "God Of War"]
for game in games:
    print("I like to play " + game)
print(games)
# Here a list item variable game iterates through the list games, take each value
# from the list. Then after the loop ends, the list of games is printed.

# To make use of for loops, the coding exercise needed me to find average number
# Use of len() and sum() was forbidden, so I had to implement them with a loop
# The input was in the form of a list of numbers, I substituted the input below
student_heights = "156 178 165 171 187".split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# My solution begins from here, the code above was pre written for me
sum = 0
count = 0
for height in student_heights:
  sum += height
  count += 1

average = round(sum / count)
print(f"\ntotal height = {sum}")
print(f"number of students = {count}")
print(f"average height = {average}")

# Next challenge involved finding the highest score in a list of scores
# But for the sake of simplicity, I will do it with the above list of heights
max=0
for height in student_heights:
  if height > max:
    max = height
print(f"The tallest person in the group is {max} cm tall")

# The range() function can be used instead to create a list with a range of values
sum_to_100 = 0
for number in range(1,101):
  sum_to_100 += number
print(f"Sum from 1 to 100: {sum_to_100}")

# The coding exercise asked to calculate sum of even numbers so let's get that done:
sum_even = 0
for number in range (2, 245, 2):
  # We can also do this without step size, using modulo to check even
  sum_even += number
print(f"Sum of even numbers from 2 to 244: {sum_even}")
# One thing to remember about the range function is that
# the end of the range is not included, so a range (a,b) is essentially a to b-1

# Next coding challenge was the "FizzBuzz" game where we say numbers starting from 1
# and if number is divisible by 3, replace number with "Fizz", if divisible by 5,
# replace it with "Buzz" and if divisible by both, replace with "FizzBuzz"
# The task was to print numbers from 1 to 100 in this format
            # toprint = ""
            # for number in range(1,101):
            #   if number%3 == 0:
            #     toprint += "Fizz"
            #   if number%5 == 0:
            #     toprint += "Buzz"
            #   if not (number%3 == 0 or number%5 == 0):
            #     toprint = str(number)
            #   print(toprint)
            #   toprint = ""
# The above solution is horrendous but I wanted to try something different
# Let's do it the tried and tested way now:
for number in range(1,101):
  if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")
  elif number%3 == 0:
    print("Fizz")
  elif number%5 == 0:
    print("Buzz")
  else:
    print(number)
# This also seems to be the solution presented in the challenge
# This challenge was the last for until Day 8 so only lectures till then

# Now the final part of today: The Password Generator
# It asks the user how many letters, symbols and numbers for their password
# Then generates a random string which matches the requirements
# The list of letters, symbols and numbers below, I copied from the course replit:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# I need the random library for this so I added that to the top
print("Password Generator, Choose your characters!")
num_letter=int(input("How many letters? "))
num_symbol=int(input("How many symbols? "))
num_number=int(input("How many numbers? "))
# I have several ways of doing this, so let me try all
# and see which matches the course
# First one: Fill a password string with 0, then gradually replace with requirement
# Okay I give up on this one, seems like I don't have enough python skills for
# this method, so I'll move on to the second
pass_length = num_letter + num_symbol + num_number
character = [letters, symbols, numbers]
lengths = [num_letter, num_symbol, num_number]
password = ""
for i in range(0, pass_length):
  charchoose = random.randint(0, 2)
  if lengths[charchoose] > 0:
    password += character[charchoose][random.randint(0, len(character[charchoose]) -1)]
    lengths[charchoose] -= 1
print(f"Your password is: {password}")

# Now for the method that is likely used in the course:
# To make use of more than just randint(), I will include choice() and shuffle()
passkey = []
for i in range(0, num_letter):
  passkey += random.choice(letters)
for i in range(0, num_symbol):
  passkey += random.choice(symbols)
for i in range(0, num_number):
  passkey += random.choice(numbers)
print("Before shuffle: " + str(passkey))
# The shuffle() function doesn't seem to work, maybe choice() will though?
# Apparently, the string doesn't support item reassignment like a list does
# So I'll have to create a brand new string to do it for us
passkey_new = ""
for i in range(0, pass_length):
  passkey_new += random.choice(passkey)
print(f"After faulty shuffle (before converting to list): {passkey_new}")
# But the issue with this is that the same character can be repeated multiple times
# defeating the purpose of the input. So I'll just follow the course now.
# Okay so the course solution is in line with my observation that we need to use a list
# But when I tried to do so, it failed the append process.
# I'll just rework the above code so it works with a list rather than a string.

# Now using the shuffle method:
random.shuffle(passkey)
print("With shuffle: " + str(passkey))
passkey_final = ""
for char in range(0, pass_length):
  passkey_final += passkey[char]
print(f"The final password: {passkey_final}")