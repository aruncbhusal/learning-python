# I didn't want to go through the whole commenting the smtp code, then 
# de-commenting(?) it again later for this, so a brand new file then
# The datetime module is a built-in Python module which we can use

import datetime as dt

now = dt.datetime.now()
# Since the class name is datetime and so is the module name so we used an alias
# This returns a datetime object for the current date and time as a string with
# a very high precision
# We can use print(now) to see YYYY-MM-DD HH-MM-SS-.....

# But we don't have much use for the whole data here, we use only what is needed
# and to access each part of this individually we can use:
year = now.year
month = now.month
# Similarly we can access day, hour, mins etc.
# We can also set our own date time object with our own given time like this:
dob_dt = dt.datetime(year = 2005, month = 2, day = 1, hour = 5)
# The attributes year month and day are mandatory, but the rest like hours, mins, secs
# are optional and have a default value of 0 if not set
today = now.weekday
# This returns what day of the week it is, with Monday = 0 and Sunday = 6
print(f"{year}-{month}, Today is Monday+{today}")
print(dob_dt)