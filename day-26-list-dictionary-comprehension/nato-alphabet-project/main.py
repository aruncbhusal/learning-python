# NATO Phonetic Alphabet is used when we need to discern two letters by their sound
# like when spelling our name out, we can say A for Apple, and so on so that the other
# party clearly understands what we want to say.
# NATO has its own list of phonetic alphabets that are used in the millitary
# Those are available in the csv in this folder

#TODO 1. Create a dictionary from the CSV with the alphabet and corresponding word
import pandas
df = pandas.read_csv("day-26-list-dictionary-comprehension/nato-alphabet-project/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index,row) in df.iterrows()}
# If we simply used to_dict() method it would not be in the dictionary format we want
# I can't believe even the variable names were ditto compared to the course

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter a name: ").upper()
phonetic_list = [phonetic_dict[letter] for letter in input_word]
print(phonetic_list)

# Pretty simple if you ask me.