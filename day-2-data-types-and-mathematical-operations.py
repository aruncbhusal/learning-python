# Python has primitive data types like int, float, str, bool
# and others are yet to be revealed in the course
print(type(123), "\n" ,type(123.45), "\n" ,type(123_456), "\n" ,type("123"))
#We can also typecast like this:
print("\n" + str(456) + str(954) + "\n", float("145.5") + float("34.8"))

# The following code can add two digits of a variable called two_digit_number:
# print(int(str(two_digit_number[0])) + int(str(two_digit_number[1])))
# instead, if the two_digit_number is defined as = input() then the type of this
# variable can be seen to be a string, so we can then omit the string casting
# in the above line of code

# The BMI is calculated by dividing a person's weight (in kg) by
# the square of their height (in m)
height=input("\nBMI Calculator\nEnter height: ")
weight=input("Enter weight: ")
bmi=float(weight)/float(height)**2
print("Your BMI is: " +str(bmi))

#Or we can just use f-Strings to avoid all type casting in print as:
print(f"Your height is {height}, weight is {weight} and BMI is {bmi}")

# Now this is a challenge that was given in the course:
age=int(input("\nREMAINING WEEKS CALCULATOR\nEnter your age: "))
print(f"If you live to 90, you have {(90-age)*52} weeks left to live.")

#Making a tip calculator as asked in the course:
bill = float(input("\nTip Calculator\nWhat is the total bill amount? $"))
tip = 0.01 * int(input("What percentage for the tip? 10/12/15? "))
people = int(input("How many people to split the bill? "))
to_pay = "{:.2f}".format(round((bill + tip * bill)/people,2))
print(f"Each person should pay: ${to_pay}")