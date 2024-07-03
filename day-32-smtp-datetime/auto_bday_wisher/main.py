# There were three difficulty levels: Normal, Hard and Extra Hard so naturally
# I chose the extra hard level, since I didn't live my 20 years so far for nothing

import pandas
import smtplib
import datetime as dt
import random

##################### Extra Hard Starting Project ######################
# The numbered todo list below is from the course, I will just write my code in each
# of those sections as a way of separating them

my_email = "<email>@gmail.com"
my_pass = "<password>"

# 1. Update the birthdays.csv
# Done, I put today's date and my email in the second spot

# 2. Check if today matches a birthday in the birthdays.csv
bdays_dt = pandas.read_csv("day-32-smtp-datetime/auto_bday_wisher/birthdays.csv")
birthdays = bdays_dt.to_dict(orient = "records")
# In the course, a tuple was needed in the date field, so a dictionary comprehension was used:
# bday_dict = {(row_data.month, row_data.day): row_data for (index, row_data) in data.iterrows()}
# I had forgotten about the iterrows() method completely but that's because I've only ever used once
# Though I wonder why row_data was used as value instead of just the email
now = dt.datetime.now()
# In the course the current month and day are stored in a tuple,
# The hint was apparently in the normal difficulty code, but hey I made it work though
for person in birthdays:
    # Needless to say, this loop was eliminated by just using if (month,day) tuple in the dictionary
    # And now I have realized that the course took the entire row since we can't access the keys
    # and should have the date in the values as well in order to access them
    if person["month"] == now.month and person["day"] == now.day:
        # Now that the condition is done, let's see step 3
        # 3. If step 2 is true, pick a random letter from letter templates and replac
        # the [NAME] with the person's actual name from birthdays.csv
        
        # Since the letters are named letter_(numbers from 1-3), I could maybe use this
        filename = f"day-32-smtp-datetime/auto_bday_wisher/letter_templates/letter_{random.randint(1,3)}.txt"
        with open(filename) as template:
            contents = template.read()
            contents = contents.replace("[NAME]", person["name"])
            # I had messed this up, by forgetting we have a name for each person in the list
            # Only before reaching that segment in the video did I notice this, as well as below
            # I hadn't used the appropriate accessing of the person's email and used my own
            print(contents)
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user = my_email, password = my_pass)
            connection.sendmail(from_addr = my_email,
                                to_addrs = person["email"],
                                msg = "Subject:Happy birthday!\n\n"
                                f"{contents}")
            
# My code seems to be incredibly inefficient since I didn't take advantage of the basic benefit
# of using a dictionary: the keys. I could have used the keys to directly check for the birthday,
# but instead I iterated through all the entries in the list of dictionaries.
# Noted for future reference.
            
# Obviously for privacy reasons, the source code is stripped off any personal emails/passkeys
# Replacing with your own credentials will work fine.