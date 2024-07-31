import sqlite3

# Let's learn about how to work with a database first
# We need to create a database file

db = sqlite3.connect('book_collection.db')
# In order to open the .db file we need some other software

# Next we need a cursor to control the database
cursor = db.cursor()
# Our database needs to be fed SQL Commands it seems. It is great that I
# have DBMS in our course already, so it is very familiar to me
        # cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,\
        #     author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# Since the cursor will be doing all the databse work, we will use that to execute
# the SQL commands. The code is pretty simple, we're just passing a string of SQL commands
# that creates a new table called books with id, title, author and rating. We don't want any
# of these data to be null so we used criterion for them, and the id is primary key as usual
# In order to view the database/make changes, we'll be using the SQLite DB Browser
# I downloaded the portable version since I don't want to have too many apps, also I wasn't
# able to use the MySQL workbench for this purpose so this is kinda the backup route
# The course suggested we do this, but I didn't really want to, yet here we are

# After running the create command and opening the database in DB Browser, we can see the table
# Here we can view the (empty) contents as well as add our own if we want to
# But we're going to do it here instead
# Since the database is locked when it is being used (Serializability I see you!)
# we will need to close the connection there before making any commands here
# Also, the table has been created already so we can work on it, shouldn't have the create line
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'JK Rowling', '9.8')")
# I was wondering what was going wrong, and then I realized we need to commt changes to db
db.commit()
# Now we've got the data there
# Since the SQL Commands are so prone to errors, and most of the time we wouldn't even realize
# an error, we'll be scratching our heads the whole time, so we instead use SQLAlchemy to make
# these queries
# We'll use them in the library project folder