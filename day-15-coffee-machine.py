# In today's lesson we're first working with Pycharm. Though I'm using VSCode
# I will be using Pycharm and them copying it off of there to end it.
# In fact, I'm writing this in Pycharm. There's a few features we should know:
# 1. Pycharm has spellcheck for English words, that text editors like Replit don't
# 2. We can right-click and split screen to work with two projects in the same window
# 3. Built-in linter to take care of PEP-8 style guides
# 4. We can check the built-in coding history and revert back if needed.
# 5. The code structure, and all vars, functions, etc. can be seen and accessed.
# 6. We can refactor and rename all instances of a function name/var name easily.
# In pycharm, we can use double shift to search everywhere,
# Alt + Enter to make suggested changes, Ctrl+Shift+/ to comment, etc.
# We can use Alt+Shift+Select to write same thing on multiple consecutive lines

# In today's project, we will be making a Coffee Machine (Simulator?)
# We are given a menu and a list of resources from the course, and we have to
# work with it to satisfy the customer's orders. There's a code requirement
# so that it matches with the demo project, so here are the requirements:
# #TODO 1: Ask customer what to order : (Espresso, Latte, Cappuccino)
# #TODO 2: Turn the coffee off if input is 'off'
# #TODO 3: Print a report of remaining ingredients and cash if input is "report"
# #TODO 4: If customer's request can't be met, return items insufficient.
# #TODO 5: Ask for coins after selecting drink and calculate based on values:
# #TODO 5: quarter = $0.5, dime = $0.1, nickel = $0.05 and cent = $0.01
# #TODO 6: Check transaction status depending on coins given and the cost
# #TODO 7: Make coffee, add cash to cash register and update resource values

from os import system

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# These dictionaries were imported from the course start Replit
# Okay since I don't have the demo at hand, I'll have to wing it from instructions

machine_on = True
cash_register = 0


def print_report():
    """Lets us know the state of the machine, resources and cash"""
    # I used the demo preview from the video to see this one's behavior
    for key in resources:
        print(f"{key.title()} : {resources[key]}")
    print(f"Money: ${cash_register}")


def has_resources(drink):
    dont_have = []
    for stuff in MENU[drink]["ingredients"]:
        if resources[stuff] < MENU[drink]["ingredients"][stuff]:
            dont_have.append(stuff.title())
    if len(dont_have) > 0:
        print(f"Sorry, there's not enough {', '.join(dont_have)}.")
        return False
    else:
        return True


def ask_money(drink):
    """Simulates the coffee machine asking for coins"""
    total = 0
    print("Please insert coins")
    # The following code I changed a bit to make it look cooler.
    # The user experience and functionality is (almost) unchanged.
    money = {
        "quarters" : 0.25,
        "dimes" : 0.1,
        "nickels" : 0.05,
        "cents" : 0.01
    }
    for coin in money:
        total += int(input(f"How many {coin} (${money[coin]}) ? => ")) * money[coin]
    # total = quarters*0.25 + dimes*0.1 + nickels*0.05 + cents*0.01
    # I had the above code when I had separate variables for each coins
    # But to achieve the purpose, course soln was fine, so used that.
    if total < MENU[drink]["cost"]:
        return 0
    else:
        return total


def transaction(drink):
    if has_resources(drink):
        money = ask_money(drink)
        if money == 0:
            print("Not enough money for the drink. Refunded.")
            return 0
        else:
            item_cost = MENU[drink]['cost']
            if money > item_cost:
                print(f"Here's your change: {round(money - item_cost,2)}")
            return item_cost
    else:
        return 0


def use_ingredients(drink):
    new_state = {}
    for stuff in resources:
        if stuff in MENU[drink]["ingredients"]:
            new_state[stuff] = (resources[stuff] - MENU[drink]["ingredients"][stuff])
        else:
            new_state[stuff] = resources[stuff]
    return new_state


def cost(index):
    """Returns the price of each beverage, was not in the course"""
    menu_item = ["espresso", "latte", "cappuccino"]
    return MENU[menu_item[index]]["cost"]


while machine_on:
    print("\nWhat would you like to have today?")
    user_input = input(f"(Espresso ${cost(0)} /"
                       f"\nLatte ${cost(1)} /"
                       f"\nCappuccino ${cost(2)}):\n").lower()
    if user_input == "off":
        print("The coffee machine is turning off...")
        machine_on = False
    elif user_input == "report":
        print_report()
    elif user_input in MENU:
        newcash = transaction(user_input)
        cash_register += newcash
        resources = use_ingredients(user_input)
        if newcash > 0:
            print(f"Please enjoy your {user_input} ☕.")
    else:
        print("Please choose a drink!")
    # For a better user experience, I'll add a clear screen functionality
    input("\nPress enter to continue...")
    system("cls")

# I had so much fun while coding this up. Added some things I didn't see in the course
# I am yet to see the course solution, and I'm already almost at the 11 pm mark
# I need to wrap it up quickly so let me test against all the requirements first
# I'll add a second hash in front of TODOs once they are done
# Alright this was it for today. It's already 11:30 so I'm getting late. Must submit
