from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Now I will read the documentation and use the objects as per that
# There's a MenuItem class that replicates MENU and cost from last day
# A Menu class with get_items() and find_drink(name) methods
# CoffeeMaker class with report, resource check and make coffe methods
# MoneyMachine class with report, make payment methods

# Let us first make the objects:
menu = Menu()
machine = CoffeeMaker()
drawer = MoneyMachine()
# First we need to set up the loop:
machine_on = True
while machine_on:
    order = input(f"What would you like to have? {menu.get_items()}: ").lower()
    if order == "off":
        machine_on = False
        print("The machine is turning off..")
    elif order == "report":
        machine.report()
        drawer.report()
        # I didn't look at the docstring and thought they returned strings
        # So I put them inside a print, but realized they print themselves
        # only while watching the course lecture.
    elif menu.find_drink(order) in menu.menu:
        drink = menu.find_drink(order)
        if machine.is_resource_sufficient(drink):
            if drawer.make_payment(drink.cost):
                # Didn't read docstring for this either so forgot it returned bool
                machine.make_coffee(drink)
            
# This took a lot longer than I would like to admit but I don't know why
# my brain just refused to work for all this while.