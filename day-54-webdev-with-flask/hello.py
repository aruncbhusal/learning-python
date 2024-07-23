# In today's lesson's we're shifting away from Web Scraping and into Web Development
# Web Development has Front End and Back End, combined form Full Stack
# Typically Front End contains HTML, CSS, JS and back end can have any other language
# A website can be divided into client, server and database.
# Instead of using languages, we can use frameworks in the languages for Development
# Angular and React are popular front end frameworks
# In python there are multiple back end frameworks but Flask and Django are most popular
# Flask is mostly used for small size and beginner projects while Django for larger

# A framework is different from a library. In a libarry, we use the methods/ tools given
# in the library in our own way, but for a framework, we need to follow the structure and
# rules specified by the specific framework, and we only define the content in the framework
# The calling part is done by the framework itself.

# The Flask framework needs to be first installed and imported to our project
# Since we need to create environment variables, I have created a virtual environment for this
# day and probably the days after as well.
# We can use "pip" to install packages which are available in PyPi
from flask import Flask

# From the flask page in PyPi: https://pypi.org/project/Flask/
# And quickstart guide: https://flask.palletsprojects.com/en/3.0.x/quickstart/

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/secret")
def secret_page():
    return "<p>How did you discover my secret page???</p>"

# I copied the above programlet from the quickstart guide page.
# To run this we need to go through some steps
# While saving our programs, we should never name them in a way that it conflicts with the module
# we're using since the interpreter doesn't know what we're importing in such case
# In the current quickstart guide, there is nothing about the environment variable we need to se
# But in the course video, back then there seemed to be a requirement
# In Mac, export is used, while in Windows, set is used as a terminal command to set env variable
# The variable name should be saved as "set FLASK_APP=hello.py" since our program is named that
# but since currently the implementation seems to have been updated, we will follow that

# From the quickstart guide, the terminal commands currently used seem to be:
# flask --app hello run
# whereas it used to be "flask run" after setting the env var before
# let's run the program now, using the command, not the python interpreter

# After running, it gives us an IP address for our locally created Web Server, this is the link
# where we can see the contents of our website, for now the website only has "Hello world!"
# The IP address was: https://127.0.0.1:5000 and it would be there until I close it using Ctrl+C
# We can't create multiple flask servers on the same IP because it would conflict so to run the
# program agaain, we would need to first close this server.

# Now to explain the code above, the new thing here is that we're running the code from the
# terminal instead of the python interpreter, and that too by specifying command line arguments
# or in the case of the course lecture, environment variables.
# We could instead use the following code and run this app the way we used to run before:
if __name__ == "__main__":
    app.run()
# The significance of __name__ in this is that it contains the name of the file we're running this
# line of code on. By checking with __main__ we confirm that we are actually running from the current
# file i.e. hello.py instead of some module.
# We could use random.__name__ and it would have the value "random" since it is run from within the
# random module. In our case, we're running outside of any modules and inside of our hello file, so it
# will contain the value __main__
# In the python docs, __name__ : name of the class, function, method, descriptor or generator instance

# Line number 26 essentially means when we go to the homepage (i.e. website followed by a /) we should
# run the function. We haven't seen that way of using a function, and it is called a "decorator"
# We could even add another function for when the URL has a /bye at the end. Adding it after the hello

# This was it for the first lesson, we created our first Web Server using Flask