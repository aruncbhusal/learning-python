# Today, we'll be looking at the errors that might happen while writing
# some code, and how to handle such errors. Some of the errors may be:

# File not found error:
# When trying to read a file, if the file doesn't exist, it will return this
# and the program will crash
            # with open("random.txt") as random:
            #     random.readlines()

# Key Error:
# When using a dictionary, if we try to access a key that doesn't exist
# in the dictionary, it will cause an error as well
            # test_dict = {
            #     "mango" : "Yellow inside green",
            #     "Watermelon" : "Red inside green"
            # }
# print(test_dict["apple"])

# Index not found Error:
# When using a list/tuple/string, we might try to access an index that doesn't exist
            # arr = [5, 6, 7, 3, 1]
            # print(arr[5])
# Only upto index 4 exists, but 5 doesn't so it will throw an error

# Type Error:
# We might be taking advantage of dynamic typing and then in some instance, it may not
# work as we expected and a string got into a variable meant for an integer
            # a = "Test String"
            # a += 5
            
# In order to handle these errors, we use a combination of statements:
# try: It includes the code that might cause an exception (unexpected output)
# except: It includes the code to execute if the try block does cause an exception
# else: This code will run if there was no exception when executing the try block
# finally: It will run either way, and mostly used as a cleanup after the try block

# Let's use this to handle the File not found error
try:
    # This block will contain some code that might cause an error
    file = open("day-30-error-exception-json/random_file.txt")
    test_dict = {"key" : "value"}
    test_dict["abc"]
except FileNotFoundError:
    # This block will be executed in the case that there was an error while executing
    # the try block
    # One thing to note is that if we just leave it as "except:" it will throw any and
    # all errors into this block, which is not what we want
    # In order for it to throw only errors associated to the file, we need to add to it
    file = open("day-30-error-exception-json/random_file.txt", "w")
    # This code will create the file so that in the next run, the try block will not
    # raise any exceptions.
except KeyError as error_msg:
    # If instead, a keyerror occurs, this code will be run.
    # We want to be able to handle all types of errors in their own ways, so this is
    # necessary, since creating a file wouldn't solve a KeyError or vice versa
    print(f"The key {error_msg} wasn't found!")
    # We can also grab the error message that we would normally get when an exception
    # is thrown, so that we can know what key actually caused the error 
else:
    # This block will run if there were no exceptions in the try block
    file.read()
finally:
    # This block is not used very often, but it can be used to do some cleanup whenever
    # it is necessary, like closing a file that might've opened in some other blocks
    file.close()
    
# We can also decide to raise an exception ourself, when a value is not what we expected
# For example, the human height should be in the range 20cm to 300cm
# So if a user tries to input an unrealistic value, we can raise an error

height = int(input("Enter your height in cms: "))

if height < 20:
    raise ValueError("I'm sorry, this question wasn't for ants, enter a valid value")
elif height >300:
    raise ValueError("What are you? Godzilla? When did you grow over 300cm tall?")
# Similar to the valueError, we can use any other error like KeyError, TypeError, etc

print(f"Your height in metres: {height/100}") 

# Interactive Coding Exercise 1: IndexError Handling
# We are given a list of fruits and a function that returns the fruit name with a pie
# If the index doesn't exist, we are to just return "Fruit Pie"
# This was my solution:
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit pie")
  else:
    print(fruit + " pie")

make_pie(4)

# Interactive Coding Exercise 2: KeyError Handling
# We are given a dictionary of Facebook post statistics, with Likes, Comments, Shares
# as the keys, but not all posts will have Likes or Comments or Shares, so for those
# cases, the like key doesn't exist, we need to handle this error and make it so that
# those posts with no likes are skipped, and total likes are summed up
# This was my solution:
facebook_posts = [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1},
                  {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},
                  {'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass
# I wonder how the course handled this, I just took the easiest way out, since there was
# only one line of code to run/test. There was nothing to do for the else/finally blocks
# There was nothing to do for except either since they are meant to be skipped so I passed
# The course had the exact same solution so yay : )
print(total_likes)

# Exception handling is not used by everyone but it is a very nice tool to use