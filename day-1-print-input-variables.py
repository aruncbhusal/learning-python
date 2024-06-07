# Some code to make use of print, escape character to reuse quotes and the newline escape character, as well as string concatenation features
print("Hello world!")
print("I just said \"Hello world!\" did you hear?")
print('This is on multiple\nlines??? wow')
print("String conc" + "atenation??")

# Input function can be nested within print. That's kinda neat!
print("Wow you like " + input("Favorite drink? ") + "! Me too!")

# Pretty nice to have a dedicated inbuilt function for length of string too
saysmth = str(input("Say something: "))
print("The string \"" + saysmth + "\" has " + str(len(saysmth)) +
      " characters in it")
# Something like print(len(input())) should work well too.

# Now let's make a simple swap block
a = 10
b = 20
print("a:",a," b:",b)
# Let's swap now
c=a
a=b
b=c
print("After swapping: a:",a," b:",b)
'''I also found out we can make
multiline comments using triple single or double quotes before and after comment'''

# Now let's make a band name generator (Almost replicating the one in the Udemy course)
print("Welcome, let's give your band a name!")
city = input("What city did you happen to grow up in?\n")
petname = input("What name would you give to your new pet?\n")
print("Okay how about this for a band name: " + city + " " + petname)
# Okay we're done with the first day. Will continue tomorrow.