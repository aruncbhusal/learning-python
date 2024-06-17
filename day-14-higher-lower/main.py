# On my last "Beginner" python day (The same day I did day 12 and 13) i.e day 14
# I'll be coding the Higher-Lower game which compares peoples' follower counts
# The game data (information of people) will be from the code, I will make own art
# So let us start from scratch by breaking down the problem:

# 1. Display art and randomly select two people to compare
# 2. Load all the info and display in a user friendly format
# 3. Prompt user for input A or B and check the follower counts
# 4. For correct, clear screen and print current score before same window
# 5. For wrong, clear screen and print final score then exit

logo = """
    __  ___       __                        
   / / / (_)___ _/ /_  ___  _____           
  / /_/ / / __ `/ __ \/ _ \/ ___/           
 / __  / / /_/ / / / /  __/ /               
/_/ /_/_/\__, /_/ /_/\___/_/                
        /____// /   ____ _      _____  _____
             / /   / __ \ | /| / / _ \/ ___/
            / /___/ /_/ / |/ |/ /  __/ /    
           /_____/\____/|__/|__/\___/_/     

"""
versus = """
____    ____   _______.
\   \  /   /  /       |
 \   \/   /  |   (----`
  \      /    \   \    
   \    / .----)   |   
    \__/  |_______/    

"""

import random
from game_data import data
from os import system

def correct_ans(A,B):
    '''Returns the correct answer as either A or B'''
    if A['follower_count'] > B['follower_count']:
        return 'A'
    elif A['follower_count'] < B['follower_count']:
        return 'B'
    else:
        return 0
    
def printable(person):
    '''Initially all inside the print, this function is used to declutter'''
    return f"{person['name']}, a {person['description']}, from {person['country']}"
    
def game():
    print(logo)
    total = len(data)
    game_over = False
    # The game shall go on until it's over, when the answer is wrong
    score = 0
    personA = data[random.randint(0,total-1)]
    # Until looking at course solution I had forgotten random.choice() existed,but meh
    personB = personA
    while not game_over:
        print(f"\nCompare A: {printable(personA)}")
        # It would look much cleaner if the above code had its own function so I did.
        print(versus)
        while personA == personB:
            personB = data[random.randint(0,total-1)]
        print(f"\nAgainst B: {printable(personB)}")
        
        user_input = 0
        while user_input != 'A' and user_input != 'B':
            user_input = input("Who has more followers? 'A' or 'B'? ==> ").upper()
        answer = correct_ans(personA,personB)
        if answer == 0:
            answer = user_input
        # This was just to ensure user is correct if both have the same follower count.
        # Pretty unlikely but hey, chance isN chance
        system('cls')
        print(logo)
        
        if user_input == answer:
            score += 1
            personA = personB
            print(f"\nThat's correct! Current score is {score}")
        else:
            print(f"\nSorry, that was wrong. Final score: {score}")
            game_over = True
        
game()

# Okay my game is done in like half an hour. So now I'll be going through the course