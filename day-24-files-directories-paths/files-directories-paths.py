# Today we'll be learning how to read, write and append to files
# using python built-in function open() and keyword "with"

# First let's read the contents of the test.txt file
file = open("./day-24-files-directories-paths/test.txt")
contents = file.read()
print(contents)
file.close()

# The write mode will create a new file if given file doesn't exist
# If the open mode isn't given, by default it is read
file = open("./day-24-files-directories-paths/new_text.txt", mode = "w")
file.write("Let me try to write something")
file.close()

# We can instead use this indented block method, files are automatically closed
# The append method adds content to the end of the file, unlike write, which
# will remove all contents of the file before rewriting the new data.
with open("./day-24-files-directories-paths/test.txt", mode = "a") as file:
    file.write("\nYour wish has been granted!")


print("\nAfter appending:\n")
# Next was about paths, but since my working directory is the git directory
# I have already been using the absolute file path to access my file
# So now I'll instead use relative file path for the test.txt file to read
# Since I have updated it since the last time it was read
with open("D:/learning-python/day-24-files-directories-paths/test.txt") as file:
    print(file.read())
    
# If the file were say in a folder called "Man" inside a folder called "batman"
# inside the root(in this case D:), then the relative way to address it would be:
# ../../batman/Man/file.txt since the root is two folders up from current working dir