# In today's lessons, I will be diving deeper into OOP, creating classes
# And then using those classes to work towards a quiz game by the end.
# To create a class, we use structure similar to a function (eg:)
class User:
    # We are not suggested to leave a class or function empty and
    # It will throw a warning for "Indentation Expected" if empty
    # But we can use the pass keyword to have it empty for now:
                            # pass
    # Now we will define a constructor, which Python understands:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        # We take two positional arguments from the user to set values
        # If the values are not given, it gives an error
        self.age = 18
        # Just using a variable name would cause it to be local to the
        # scope of this function, so we tag it with the class with self
        print(f"Default age: {self.age}")
        # So each time an object is created, age is set to 18
    
    def birthday(self):
        # While defininig a method, self must be an argument so that
        # Python knows which object we are working with
        self.age += 1
        # it can also have other parameters like another object of the class
        # Like when simulating a follow button, one's followers increases,
        # And the other's following increases.
        
# Naming can be done in many ways, PascalCase, camelCase, snake_case
# In python, classes use PascalCase and variables/funcs use snake_case
                    # user_1 = User()
# Now we have an object of the User() class called user_1
# We can set attributes to the objects just like normal variables:
                    # user_1.name = "James"
# But this won't exist for some other object, so to make it more clear
# We can define a constructor inside the class which initializes i.e.
# Sets the attributes to a default value that can be accessed/changed
user_2 = User(1,"Brianna")
# Since now I have initialized age to 18, I can simply access it here
print(user_2.age)
print(f"{user_2.id} : {user_2.username}")
# Now we have default as well as values set by providing arguments
user_2.birthday()
print(f"{user_2.username}'s new age: {user_2.age}")