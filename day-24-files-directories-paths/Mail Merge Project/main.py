# The starting code was given from the course I just need to solve it

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: Using the readlines() method
# Step 1: Create a letter using starting_letter.txt
start = open("day-24-files-directories-paths/Mail Merge Project/Input/Letters/starting_letter.txt")
letter = start.read()
# I had used the readlines() method but I can simply use read to get the whole file in the string
start.close()

name_file = open("day-24-files-directories-paths/Mail Merge Project/Input/Names/invited_names.txt")
names= name_file.readlines()
# Above LOC will return the lines of the name file as a list
for i in range(len(names)):
    names[i]= names[i].strip()
    # I forgot that name is just a variable to hold the value of each line
name_file.close()
# Rather than stripping here, in the course they were stripped right when they were used
# That is something I thought of but didn't implement

for name in names:
    with open(f"day-24-files-directories-paths/Mail Merge Project/Output/ReadyToSend/letter_to_{name}.txt",
                mode= "w") as new_letter:
    #Hint2: Using the string.replace() method
        new_letter.write(letter.replace("[name]", name))
    #Hint3: string.strip() can be used to remove surrounding whitespaces

# Okay I almost gave up but after a google search, I did it.
# I'd be beating myself up if I had to resort to course solution for something as simple as this
# The basic structure of the solution matches the one in the course, I'm satisfied.