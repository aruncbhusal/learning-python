# In this lesson, we will enter a topic I was actually curious about
# And I've been kinda waiting for. Just like the break statement yesterday
# We'll be exploring List and Dictionary comprehensions in Python

# This can almost be called exclusive to Python since I don't know any other
# languages that supports this, but it helps to shorten the code slightly

numberss = [1, 2, 3, 4, 5, 6]
# If we wanted to create a new list from an existing list, we would use:
normal_method = []
for n in numberss:
    new_n = n + 1
    normal_method.append(new_n)
print(normal_method)

# Rather than this we can instead use list comprehension with syntax:
# new_list = [new_item for item in list]
comp_method = [n+1 for n in numberss]
print(comp_method)
# Both serve the same purpose but one is a lot more readable and short

# let us try converting a string to list now
# The course wanted us to find out what the code does but I somehow know
name = "Simpson"
name_list = [letter for letter in name]
print(name_list)
# Yeah just as I expected

# Next challenge was to create a list from a range where all numbers
# in the range need to be doubled
range_list = [n * 2 for n in range(1,5)]
print(range_list)

# With list comprehensions, we can also have conditions at the end of it
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# If we had to make a list of names 5 or more characters long, then we can use
# Also we need to make the name all caps
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# Interactive Exercise 1: Square a list and create a new list using comprehension
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)

# Interactive Exercise 2: Filter out odd numbers from a list
# First we had to convert a list of strings to numbers, I did that
string_list = "1, 1, 2, 3, 5, 8, 13, 21, 34, 55".split(",")
nums = [int(s) for s in string_list]
non_even_nums = [n for n in nums if n%2 == 0]
print(non_even_nums)

# Interactive Exercise 3(Hard): List of common numbers from two files
# I wrote a lengthy code which I will need to learn from the solution but here it is:
        # with open("file1.txt") as file1:
        #   file_one = file1.readlines()
        # file_one_list = [int(line.strip()) for line in file_one]

        # with open("file2.txt") as file2:
        #   file_two = file2.readlines()
        # file_two_list = [int(line.strip()) for line in file_two]

        # resfrom1 = [data for data in file_one_list if data in file_two_list]
        # resfrom2 = [data for data in file_two_list if data in file_one_list]
        # exclusive_in_resfrom2 = [data for data in file_two_list if data not in resfrom1]
        # result = resfrom1 + resfrom2

        # print(result)
# My idea was that if data is in file 1 and in file 2 as well, there could be some other
# data in file 2 that was common to a data in file 1 but not appear in common list????
# I have realized me fault. Result should just be the res1 list. I haven't even test run it.
# After this quick fix, the course solution reminded me that I can just get the integer when
# using list comprehension, and it would strip any newlines itself.

# Next is the dictionary comprehension and it works similarly with only syntactic differences
# new_dict = {new_key:new_value for item in list(iterable)}
# Here an iterable is list, range, string, tuple...
# If we want to create a dictionary from an existing dictionary then:
# new_dict = {new_key:new_value for (key,value) in dict.items()}

# As an example, let's use the names list we had earlier
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# If we were to create random scores for these, we would use:
import random
student_scores = {student:random.randint(0,100) for student in names}
print(student_scores)
# Next we can use this dictionary to create another one, for passed students
# Say the pass score is 50, then we can just use:
passed_students = {student:score for (student,score) in student_scores.items() if score >= 50}
print(passed_students)

# Dictionary Interactive Exercise 1: Create dictionary of length of words in a sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# We need to generate a dictionary for the above sentence, where the key-value pairs will be
# the individual words, and their lengths respectively. First get the words separately in a list
word_list = sentence.split()
# When left empty, it will split the string for any whitespace character
word_length = {word:len(word) for word in word_list}
# We can shorten this further by replacing word_list above by sentence.split() and removing above
print(word_length)

# Dictionary Interactive Exercise 2: Create dictionary of Fahrenheit from one of Celsius
weather_c = eval('{"Monday": 12, "Tuesday": 14, "Wednesday": 15,\
                 "Thursday": 14,"Friday": 21, "Saturday": 22, "Sunday": 24}')
# I used the backslash to "continue line" since it was too long to fit
# Also I had to make sure the double quotes inside dictionary wouldn't conflict with the
# ones enclosing the whole eval string, as it resulted in an error otherwise

# The eval function seen in exercise can evaluate an expression inside its arguments
# In this case, it converted the string into a dictionary. It can be used in multiple ways
# eval(4+5) would give 9, eval('print(55)') would print 55 even if the code was in a string
# I can already see uses for it in dynamic programming
weather_f = {day:(temp*9/5 +32) for (day,temp) in weather_c.items()}
# The items() method will return a list of key-value tuples from a dictionary
print(weather_f)

# We can also loop through the pandas dataframe similar to lists and dictionaries
import pandas
stud_data = {
    "Name" : ["Brian", "Grant", "Lily", "Stacy", "Miles"],
    "Score" : [45, 67, 36, 76, 95]
}
stud_data_df = pandas.DataFrame(stud_data)
# We needed to have a dictionary with list values so needed to create a new one for it
        # for (key, value) in stud_data_df.items():
        #     print(value)
# The above code would just give us the columns one by one but we usually work with rows
# For it, the pandas library has a handy method called iterrows()
for (index,row) in stud_data_df.iterrows():
    # print(row)
    # ^ This would print all the rows as dataframe objects but we can go further
    if (row.Score > 70):
        print(row.Name)
# This would print the names of students who have a score of 70+

# This is it for learning, now on to project making