# Looks like in today's lesson we're going to be working with yesterday's project
# Just continued by modifying the contact page so that it can take the input data and
# send it to us via email.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login", methods= ["POST"])
def receive_data():
    # Looks like methods is a keyword argument for the decorator function
    # Since the methods accepts a list, we can use both GET & POST at the same time
    # Flask has a request method of itself to get the data from the method in HTML
    # By default it accepts only get requests, but we can modify it as we like
    # We can instead also use @app.get or @app.post to handle with diff functions
    # get is usually used to show the login form, and post to submit the form
    name = request.form['username']
    pwd = request.form['password']
    # Our goal here was to display the submitted information in h1
    return f"<h1>Name: {name}, Password: {pwd}</h1>"
    # Looks exactly the same as solution code
    

if __name__=="__main__":
    app.run(debug= True)