# Today there's only one thing, and that one thing is a Herculean project compared
# to whatever has been done so far. Let's work on a blackjack game today
# In order to maintain simplicity, not everything will be implemented here
# It is a one day project so these are the rules we will implement acc to the course
# 1. Infinite size deck, so list of cards will remain static no matter how many draw
# cards = [11, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 10, 10, 10]
# 2. J,K,Q are all worth 10 and A is 11 or 1 depending on if the total is > or <= 21
# 3. The rule of the game is to get the highest total points, without exceeding 21
# 4. The computer is the dealer and only one of their first 2 cards is known
# 5. We either draw (hit) another card or stop/halt (stand)
#  After stopping the computer makes its choices and winner is then decided
# With all this in mind, and disregarding rules like double bet, split and so on...
# Let's start with the project, there were 4 difficulty levels but obv I'm taking expert

import random
from os import system
# I had defined the cards list here, but it wasn't used anywhere apart from dealing function
# So I just cut-pasted it into that function for better readability like the course
# The logo file was from the course as usual:
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def drawcard(player):
  '''This function is less efficient so I don't use it in the main program logic anymore'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player.append(random.choice(cards))
  # It seems we can't use += instead of append since += is shorthand for extend()
  # which is used to add lists with lists(iterables), and not individual elements
  # We could make it work by enveloping the card with square brackets to make it a list
  return player
# The function in the course just returns a random card, which seems like a better idea
# than my method of returning a brand new list, mine is more intensive.

def deal_card():
  '''This basically returns a random card, and takes no input so can be used for both'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def checkAce(player):
# This and blackjack check were both done in a calculate_score() function in the course.
  if 11 in player:
    player[player.index(11)] = 1
  return player

def comparescore(user,computer):
  userSum = sum(user)
  computerSum = sum(computer)
  if userSum > 21:
    print("You busted! You lose 🤯")
  # Changed the order of this, since regardless of computer's draw, if we bust we lose
  elif userSum == computerSum:
    print("The game ends in a draw 🥱")
  elif userSum == 21 and len(user) == 2:
    print("You had a Blackjack! You win! 🥵")
  elif computerSum == 21 and len(computer) == 2:
    print("The computer had a blackjack. You lose 🥺")
  elif computerSum > 21:
    print("The computer busted! You win 😎")
  elif userSum > computerSum:
    print("Nice call! You win 🥳")
  else:
    print("Aw no, you lose 😢")

def blackjack():
  userHand = []
  userSum = 0
  computerHand = []
  computerSum = 0
  print(logo)
  print("Welcome to blackjack! I, the computer will be your dealer today.")
                # userHand = drawcard(userHand) 
                # userHand = drawcard(userHand)
  # Replaced the above two with the new deal_card() function from the course:
  for _ in range(2):
    userHand.append(deal_card())
  # Could have used a for loop like the course but for only 2 repititions, really?
  # On second thought, to make the logic similar to blackjack, we deal both the user and
  # the computer two cards first, then only show one to user, so maybe should use for loop
                # computerHand = drawcard(computerHand)
    computerHand.append(deal_card())
  to_stop = False
                    # if userSum == 21:
                    #   print("Blackjack!")
                    #   to_stop = True
  # I had the above code, but thought I'd give the player the autonomy to lose even with BJ
  while not to_stop:
    userSum = sum(userHand)
    if userSum > 21:
      userHand = checkAce(userHand)
    # This was before hand info printing, but it actually needs to be accounted beforehand
    print(f"    Your hand: {userHand}    Total: {userSum}")
    print(f"    Computer's first card: {computerHand[0]}    Total: {computerHand[0]}")
    if userSum > 21:
      to_stop = True
    else:
      next_move = input("\nDo you want to hit[draw] (y) or stand[stop] (n): ").lower()
      if next_move != 'y':
        to_stop = True
      else:
                        # userHand = drawcard(userHand)
        userHand.append(deal_card())
  # From playing the blackjack game in the website, I learnt the rule that as long as the
  # dealer's hand is 16 or less, they must draw a card. Over that they might stop
  # In my program I'll use that simple logic to stop if hand > 16 (not all dealers are same)
  computerSum = sum(computerHand)
  while computerSum < 17:
                        # computerHand = drawcard(computerHand)
    computerHand.append(deal_card())
    if computerSum > 21:
      computerHand = checkAce(computerHand)
    # This if was positioned later in the code, but I felt this was a more fitting position
    computerSum = sum(computerHand)
  # could replace it all by replacing computerSum with just sum(computerHand) but meh
  print(f"\n    Your final hand: {userHand}    Total: {userSum}")
  print(f"    Computer's final hand: {computerHand}    Total: {computerSum}")
  # At this point (last video) I have realised that having a Blackjack is just a gimmick
  # for the most part, and it's only to show that you have a blackjack
  # I didn't have the function comparescore() and all ifs were here, but I made the function
  comparescore(userHand,computerHand)
  play_again = input("\nDo you want to play again? (y/n)").lower()
  if play_again == 'y':
    return True
  else:
    return False

if input("Hey do you want to play a game of Blackjack? (y/n)").lower() == 'y':
  play_game = True
else:
  play_game = False
while(play_game):
  system("cls")
  play_game = blackjack()
print("Thank you for your time! I hope you visit the program for some Blackjack soon.")

# In the course, I felt there were more functions than necessary, but those that I felt
# were actually helpful, I replaced them in my code as well. I noticed some flaws with
# the course code as well, and those didn't exist in mine, so a pat on the back to myself

# That's it for today. This definitely took some time.