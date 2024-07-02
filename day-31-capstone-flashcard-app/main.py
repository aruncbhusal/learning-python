# Today the goal is to create a flashcard app that helps us memorize a
# new language, in this case French. But I think I'll use Japanese instead

# In order to do this, we will first need the list of words, for that we can
# use a "frequency list" which orders words by how often they are used
# Wiktionary has a page for frequency list of a lot of websites:
# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
# We can instead use a list created from media like subtitles to movies and stuff
# which can be found on the Github page of Dave Hermit:
# https://github.com/hermitdave/FrequencyWords/tree/master/content/2018
# I will be using the "ja" folder's first 200 words for this project

# The words are only in Japanese so we need translations as well. For that we can
# make use of Google Sheets. First we get all the Japanese words to the sheet
# then in the sheet beside, we can use =GOOGLETRANSLATE(<text>,<s_language>,<t_language>)
# I have translated and downloaded the files as a csv file from the sheets into this folder
import pandas
import random
from tkinter import *
# Since I'm working with a csv and in a GUI app, I need the above modules

BACKGROUND_COLOR = "#B1DDC6"
# ^ This comes from the starting file of the project
# I have also imported the icon images from the course


# The UI is done so let's now extract the data from the CSV

# The final job is the button behaviors:
# If a word has been known (right button clicked), the word should be removed form the list
# i.e. a file words_to_learn.csv will contain the words that are yet to learn
# We use that file to serve the words, but if it doesn't exist, work with original file

try:
    words_df = pandas.read_csv("day-31-capstone-flashcard-app/words_to_learn.csv")
except FileNotFoundError:
    words_df = pandas.read_csv("day-31-capstone-flashcard-app/japanese_words.csv")
# This should be enough to open one file or the other if that doesn't exist
# Now we use this dataframe to generate a dictionary
words_to_learn = words_df.to_dict(orient = "records")
# Using the orient attribute, we can specify how the dictionary is to be arranged
# By using the default(dict) value, we get Column -> (Index -> Value) but since we have
# no need of index, we use records which gives Column -> Value
# So since our column names are Japanese and English, the dictionary items would look like:
# {"Japanese" : <jp_word>, "English" : <en_word>}

# Now for the "Don't know yet" button, nothing has to change, all it needs to do is fetch
# a random word from the dictionary without any modifications.
# But when the "Known" button is pressed, we should remove the word and place the rest in the
# words_to_learn.csv file
current_word = {}
# I thought I could get with not having to create this variable, but in order for the word to
# be removed from the dictionary, we will need to get a hold of it. So let's use this

def known_word_next():
    global words_to_learn, current_word
    words_to_learn.remove(current_word)
    updated_df = pandas.DataFrame(words_to_learn)
    updated_df.to_csv("day-31-capstone-flashcard-app/words_to_learn.csv", index = False)
    # If we didn't set the index to false, it would add an index to each row of the file
    # every time we run this program. Since we don't want that we turn that off
    next_word()
    

delay = None

def flip_card():
    lang = "English"
    # window.after_cancel(delay)
    # Turns out the cancel process is only needed for the new_word() function
    canvas.itemconfig(card, image = card_back)
    # The card must face the opposite side when showing the english word
    canvas.itemconfig(language, text = lang, fill = "white")
    canvas.itemconfig(lg_word, text = current_word[lang], fill = "white")
    # The text fill was changed from black to white
    

# Generate a random word to display in the flash card:
def next_word():
    global delay, current_word
    # In the course, the word was also set as a global variable but since we pass it as
    # an argument in our case, as we only ever need it once we call this function first
    # I think my implementation will have a better variable privacy
    window.after_cancel(delay)
    # We should avoid using other delay functions like time.sleep() as they would halt the
    # entire program execution, and not just count the time
    # Yet again, the course has bested me, I need to have the window.after before the function
    # is called for the first time in order for this to work, so I'll do that below
    current_word = random.choice(words_to_learn)
    lang = "Japanese"
    # Since after flipping, the text color and image are chnaged, we need to change it back
    canvas.itemconfig(card, image = card_front)
    canvas.itemconfig(language, text = lang, fill = "black")
    canvas.itemconfig(lg_word, text = current_word[lang], fill = "black")
    # Okay now let's watch the video... and it was the same
    # Next we need to add a functionality that after 3 seconds of a new word,
    # the card should change to english, which means changing both the image and text
    delay = window.after(3000, flip_card)
    # We need to get the english word after a 3 second delay
    
    
# Let's create the UI for now:
window = Tk()
window.title("Flashcard-chan")
# I will be following the guidelines without watching the video first and will watch the
# video only if I find myself stuck somewhere. Padding as defined by the demo program:
window.config(padx = 50, pady = 50, background = BACKGROUND_COLOR)
delay = window.after(3000, flip_card)


# Now let's add the actual flashcard, I think since we'll be overlaying text on top of it
# we should use a canvas element for this
canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness = 0)
# The image had some transparent parts which showed some of the canvas' white background
# so I had to change the bg to the background color as well. This was while watching video
# Both the card images are 800x526 so we can just use this as the baseline for the canvas
card_back = PhotoImage(file = "day-31-capstone-flashcard-app/images/card_back.png")
card_front = PhotoImage(file = "day-31-capstone-flashcard-app/images/card_front.png")
card = canvas.create_image(400, 263, image = card_front)
# In the start the image should be back of the card, later if clicked on it, it turns

language = canvas.create_text(400, 150, text = "Language", font = ("Ariel", 40, "italic"))
lg_word = canvas.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))
# The text sizes were set as per the course guidelines as well
canvas.grid(column = 0, row = 0, columnspan = 2)

# Now we need to add the right and wrong buttons. These buttons offer flashcard functionality:
# The right button means that you know the word and it will not be shown to you going forwards
# The wrong button means you don't know the word fully yet, so it will show it to you again later
unsure_img = PhotoImage(file = "day-31-capstone-flashcard-app/images/wrong.png")
known_img = PhotoImage(file = "day-31-capstone-flashcard-app/images/right.png")
unsure_btn = Button(image = unsure_img, borderwidth = 0, highlightthickness = 0, command = next_word)
known_btn = Button(image = known_img, borderwidth = 0, highlightthickness = 0, command = known_word_next)
# I noticed I can't get rid of the green outside the supposed icon border since it already exists
# inside the picture, so the best I can do is remove all else around it, like border and highlight
unsure_btn.grid(column = 0, row = 1)
known_btn.grid(column = 1, row = 1)
# Okay I got the files set up, loaded the canvas and the buttons and set the border width of the
# buttons to 0, and the background of the window to the color in the course, with back face of 
# the card showing to the user when they launch the app. Also set highlight thickness to 0 for btn
# I noticed the highlightthickness was already advertised in the course html so I just did borders
next_word()
# When the app starts, the function should be called immediately, showing a word at the start

window.mainloop()