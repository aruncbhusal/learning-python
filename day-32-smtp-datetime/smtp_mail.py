# In today's lessons I will be learning how to use the Python smtplib module
# to automate wishing people their birthdays.
# SMTP is Simple Mail Transfer Protocol, a means by which email is sent/received
import smtplib
import datetime as dt
import random

# Let's first store our email into a variable to access later
email = "<email>@gmail.com"
password = "<pass>"
# This password is an app password I set up for python_auto_sender app inside the
# google account securities tab
# Also the password shouldn't have any spaces here, or it won't work

# In order to set up a connection with the SMTP mail server, we need to create a new
# SMTP object, which works similar to a file object. So we could open it like this:
# connection = smtplib.SMTP("smtp.gmail.com")
# And then close the object after the whole operation has been completed with:
# connection.close()
# But instead a cleaner way would be using the "with" keyword, similar to the files

# The course challenge was to send a quote from the quote.txt from the course resources to our
# email if the day of the week is Wednesday(supposed to be Monday but we can't test that today)
# So I'll import the datetime module here and start with the thing
time_now = dt.datetime.now()
if time_now.weekday() == 2:
    # Since Monday is 0, Wednesday must be 2
    with open("day-32-smtp-datetime/quotes.txt") as quotes:
        quote_list = quotes.readlines()
    random_quote = random.choice(quote_list).strip()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # Here the url is the host of the smtp mail server for Gmail. If my sending mail
        # was a Yahoo mail then it would be smtp.mail.yahoo.com
        # Until I set a port number to the mail server, the email didn't go through so I had to
        # look at the hints after the course video to have this work for me, took so long
        connection.starttls()
        # Transport Layer Security (TLS) will encrypt our data and protect from MITM
        connection.login(user = email, password = password)
        # connection.sendmail(from_addr = email,
        #                     to_addrs = "....@outlook.com",
        #                     msg = "Subject: Test msg\n\n This message is to test the current level")
        # I tried so hard and got so far trying to create a Yahoo account to replicate the
        # course, but alas, I had to resort to my Microsoft Account to make up for the contrast
        # If we omitted the Subject section there would be a high likelihood of the Email ending
        # up in the recipient's spam, so we use a distinction and two newlines so that the smtplib
        # (As a sidenote, it still sent the mail to the junk)
        # method knows to discern the Subject from the body of the email
        # We can put multiple addressess in a sequence in to_addrs, so it is plural but not from_addr
        
        connection.sendmail(from_addr = email, to_addrs = "<email>@outlook.com",
                            msg = "Subject:Today's Quote\n\n"
                            f"{random_quote}")

# The final thing in today's course was the website Pythoneverywhere where we can upload our files and
# host them in the cloud, so that they are run routinely every day or so, at the same exact time, like
# using a birthday wisher to check for bday everyday
    