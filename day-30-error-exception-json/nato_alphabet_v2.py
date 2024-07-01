# Now we're going to apply error handling in the phonetic alphabet project we did on day 26
# We can test and see that if we enter a number while giving our input, it will return a KeyError
# We need to make it so that if the input is not a string, the input will keep repeating, until
# a string is input by the user

import pandas
df = pandas.read_csv("day-26-list-dictionary-comprehension/nato-alphabet-project/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index,row) in df.iterrows()}

def phonetics():
    input_word = input("Enter a name: ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        phonetics()
    else:
        print(phonetic_list)
    # I can't lie it took me quite a while to realize I needed to mimick a loop, and the try block
    # couldn't be used to imitate recursion, and I needed to have the try block INSIDE the function
    # for it to be possible to have a recursion. Glad to see this was the exact same soln as in the course
        
phonetics()