# To create a game of Hangman, we will follow the flowchart described in the course
# The code at the top will be commented with each next step that modifies it
# It is to document each revision of the code. So it may look like a big part of this is just comments
# The process begins with a list of words, for the word generator.
# A word will be chosen at random for each playthrough of the game


# Since we already have the word list from hangman_words, I've commented this initial list:
#word_list = ["aardvark", "baboon", "camel"]

# From course: Randomly choose a word from the word_list and assign it
# to a variable called chosen_word.
            # chosen_word = random.choice(word_list)        
# Also from course: Ask the user to guess a letter and assign their answer
# to a variable called guess. Make guess lowercase.
            # guess = input("Guess a letter: ").lower()      
# Also from coutse: Check if the letter the user guessed (guess) is
# one of the letters in the chosen_word.
            # if guess in chosen_word:
            #     print("Yes")
# Since the above code checks only the first occurence, I might want to make a loop
# to check for each position and print the status for each letter
            # for ch in chosen_word:
            #   if ch == guess:
            #     print("Present")
            #   else:
            #     print("Nope")

# After going through course soln I realized it was almost exactly the same as mine
# With this, first step is complete, now in 2nd step, these were course instructions

# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"]
# with 5 "_" representing each letter to guess.
          # display = []
          # for ch in range(len(chosen_word)):
          #   # Here I could have just used ch in chosen_word but opted to use range because I felt like it.
          #   display += "_"
          # print(display)
# Next instruction: Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then
# reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple",
# then display should be ["_", "p", "p", "_", "_"].
              # i = 0
              # for ch in chosen_word:
              #   if ch == guess:
              #     display[i] = guess
              #   i +=1
# Finally: Print 'display' and you should see the guessed letter in the
# correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter.
              # print(display)          
# Okay so far so good, now time to see the course solution and see if it matches mine
# I used an iterator variable for the for loop in the reveal section, but after looking at the course
# Now I feel like range would be more appropriate, seems I mixed up the usage huh
# Anyway here's the loop from the course, though I haven't fully watched the solution yet:
              # for position in range(len(chosen_word)):
              #   if chosen_word[position] == guess:
              #     display[position] = guess

# Next step - Use a while loop to let the user guess again. The loop should only stop once the
# user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.
# ___ For this I'll need to comment out everything that will need to get looped, so the word guess and update
              # while '_' in display:
              #   guess = input("Guess a word: ").lower()
              #   for pos in range(len(chosen_word)):
              #     if chosen_word[pos] == guess:
              #       display[pos] = guess
              #   print(display)
              # print("Wow you win!")
# In the course the condition for while was defined separately as a boolen flag "end_of_game"
# It would be true "if '_' not in display" and that would work better with multiple endgame states
# Like end of game for game over and for player win. But for this purpose, I felt the above code to be enough

# Now the next challenge had us implement the losing condition too, so I'll probably need that flag var now
# (UP UNTIL THIS STEP, THERE WERE NO HANGMAN ASCII ARTS BUT NOW THEY'RE ADDED TO THE TOP OF THE FILE)
# Since this is almost the last phase of the code, I may as well bring all variable definitions here
# And customize it accordingly, so I'll just comment out everything above except for ASCII and word list
import random
import os

from hangman_art import stages,logo
from hangman_words import word_list 

end_of_game = False
chosen_word = random.choice(word_list)
display = []
# Task: Create a variable called 'lives' to keep track of the number of lives left. 
# Set 'lives' to equal 6.
lives = 6

for ch in chosen_word:
  display += '_'

print(logo)
print("\nWelcome to Hangman, let's try not to Hang...man.. ;)")
guess_history = [] 

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    # This next LOC was briefly mentioned as a replit module, but for global usage, I used os
    os.system('cls')
    if guess in guess_history:
        print(f"You have already guessed {guess}, please try a different letter.")
    else:
        guess_history += guess
        for pos in range(len(chosen_word)):
            if chosen_word[pos] == guess:
                display[pos] = guess
        # Task 2: If guess is not a letter in the chosen_word, then reduce 'lives' by 1.
        if guess not in chosen_word:
            lives -= 1
            print(f"The letter {guess} was not in the word, you lost a life.")
        else:
            print(f"Nice! The letter {guess} was in the word")
            # If lives goes down to 0 then the game should stop and it should print "You lose."
            if lives == 0:
                end_of_game = True
                print("\n\nGame Over! You lose")
        if '_' not in display:
            end_of_game = True
            print("Wow you win!")

    # Task 3: print the ASCII art from 'stages' that corresponds to the current number of 'lives'
    print(stages[lives])
    # Join all the elements in the list and turn it into a String.
    # This code is directly from the starting replit for this step,
    # I had to make it stop looking like a list
    # every time it is printed, and the join() function seems to work opposite to split()
    print(f"{' '.join(display)} \n")
    
    # This is an extra thing I thought would be cool to add, not covered in the course:
    print(f"Your guesses so far: {' '.join(guess_history)}")    

# On going through solution, I realized I need not display and simply say game over if lives reach 0
# Though it's more of a UX thing, I shifted the game over condition from the end to the current position

# Next up is the UI/UX things and for that I'll have two more files for word list and art
# Both of the files are from the course obviously. I'll import them and use the files from there.