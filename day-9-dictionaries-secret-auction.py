# In today's lessons, I'll be learning about dictionaries in python at first
# It is similar to the list, but instead of using the index to access the values,
# we use a different value called the "key". This is how we define a dictionary:
example_dict = {
  "Apples" : "Rs 300",
  "Mango" : "Rs 120", 
}
print(example_dict)
# To add an entry to the dictionary, we can simply use an assignment:
example_dict["Banana"] = "Rs 80"
print(example_dict)
# We can also edit an entry, using a similar assignment with existing key:
example_dict["Mango"] = "Rs 110"
# To access a single entry, we can use the key name just like index in lists:
print(example_dict["Mango"])
# If we use a non existent key for accessing, we will get a KeyError
# To iterate through the dictionary:
for item in example_dict:
  print(item)
  # The above statement will only print out the keys, not the dictionary
  print(example_dict[item])
  # Now this will print the value associated with the key in the dictionary

# In the first interactive exercise, we had to use dictionary to grade students
# The scores were given in a dictionary, I had to write logic to categorize them
# based on their scores. The scores were given as:
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# I was asked to create an empty dictionary called student_grades to start off
student_grades = {}
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
# The print statement was included in the problem already:
print(student_grades)
# I'm surprised the solution code was word for word exactly the same as mine. Nice

# Next, we can nest collection variables like lists and dictionaries in each other
fruits = {
  "Avocado" : "I don't like it too much",
  "Mango" : ["King of fruits", "Available around home", "It's mango duh"],
  "Apple" : {
    "Cost" : "Rs 300 per kg",
    "Color" : "Red",
    "Grown in" : ["Humla", "Jumla", "Mustang"]
  }
}
# Here I had a simple dictionary element, a list as a value,
# and a dictionary with a nested list as a value in a dictionary
for fruit in fruits:
  print(fruit)
  print(fruits[fruit])

# Similarly, we can also nest dictionaries within lists, to make accessing easier
vegetables = [
  {
    "Name" : "Spinach",
    "Color" : ["Green", "Yellow if spoiled"],
    "Nutrient" : "Vitamin A"
  },
  {
    "Name" : "Tomato",
    "Color" : ["Red", "Green if unripe"],
    "Nutrient" : "Vitamin A too I think"
  }
]
for vegetable in vegetables:
  print(vegetable)

# In the next interactive exercise, the task was to add a new entry to a
# list of dictionaries, with inputs given as arguments. This is what I did:
                # def add_new_country(country, visits, list_of_cities):
                #   travel_log.append({
                #     "country" : country,
                #     "visits" : visits,
                #     "cities" : list_of_cities
                #   })
# In the solution, an empty dictionary was made first then all key-value pairs
# were added one by one. Then the append function was used just as I did.

# The final part of today is the Secret Auction/ Blind Auction/ Sealed Auction
# Each bidder will place their bids without knowing rest of the bids
# At the end, the winner of the bid is revealed. So clear the screen after each bid
# The logo for the program will be imported from the program and I will implement
# the logic now, by using dictionary to hold the name and the bid price for each

from os import system      # This is for the clear function
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidders = {}
is_Running = True
highest_bid = 0
highest_bidder = ""
# I'm sure there's a more elegant solution than just creating two variables for it
# But I'll have to watch the course solution to figure that out maybe
# Well the solution has a separate function for determining winner
# But apart from that, the method is basically the same. So yay me I guess?
while is_Running:
  bid = 0
  print(logo)
  print("Welcome to the Secret Auction.")
  name = input("Please enter your name: ")
  while bid <= 0:
    bid = int(input("Enter your bid: $"))
    if bid < 0:
      print("Please enter a valid positive number as the bid")
    # This was totally unnecessary but I can't leave edge cases behind
  bidders[name] = bid
  one_more = input("Are there any more bidders? (y/n) ").lower()
  if one_more != "y":
  # My code will take any other answer apart from "y" as a no
  # The course solution has it the other way, only a "n" will terminate the program
    is_Running = False
  system("cls")
  # I could place this at the start of while, but I'm assuming this is
  # a standalone program, that starts with a clear screen
  

for bidder in bidders:
  if bidders[bidder] > highest_bid:
    highest_bidder = bidder
    highest_bid = bidders[bidder]
print(f"The winner of the bid is {highest_bidder} with a bid of ${highest_bid}")