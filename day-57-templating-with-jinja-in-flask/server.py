# In today's lessons we will be learning about templating with a templating tool
# built for python "Jinja"
# It can be used to make similar pages without having to rewrite the code, and we
# can dynamically change only the coentent we want to change in all those sites.

# let's first set up our flask application to show the index.html in the homepage
from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    random_num = random.randint(0,9)
    year_now = datetime.datetime.now().year
    return render_template("index.html", num = random_num, year = year_now)
# We might have noticed that this html is just static but we have to bring it here
# and call it a "template". That is because we can use templating languages to make
# the HTML dynamic and make it act as a template.
# Jinja is python specific and is bundled with flask. We can simply use double curly
# braces to encapsulate python expressions and they will be rendered that way
# If we need some form of import, we do the coding part in server, and then we can
# send the result as a kwarg into the template file
# Let's print a random number each time the user refreshes

# A challenge here was to use two APIs "Agify" and "Genderize" to take a name that is
# in the route, and give the user an age and a gender based on their name through API
@app.route("/guess/<name>")
def guess_game(name:str):
    # Let's get the gender and age first
    response = requests.get("https://api.genderize.io", params= {"name": name})
    gender = response.json()["gender"]
    response = requests.get("https://api.agify.io", params= {"name": name})
    age = response.json()["age"]
    return render_template("guess_game.html", name= name.title(), gender= gender, age= age)

# Okay we can pass in variables fine, but what if we want to write multiline python script
# so that the data can have looping or branching. Then we need to use another syntax in Jinja
# Since we'll mostly be working with JSON for passing these data from our server to the page
# we need to create our own json, for that we can use https://www.npoint.io/
# it lets us create an API for ourself without even needing to login, and we can use the link
# generated to get the content we need for our webpage through it
# The course had a json with 3 blog posts, so let's create a html page and route for it
@app.route("/blog/<int:id>")
def blog_page(id):
    endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_posts = requests.get(endpoint).json()
    return render_template("blog.html", posts= blog_posts, id = id)

if __name__ == "__main__":
    app.run(debug= True)