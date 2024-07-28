# On the 57th day we used Jinja to create a blog website that was really simple
# We used the template that was in the course files, but this time we'll be leveraging
# the templating that Bootstrap offers. There are many websites from where we can find
# the inspiration for our website design. Following are some:
# https://bootstrapmade.com/
# https://getbootstrap.com/docs/5.0/examples/
# https://www.creative-tim.com/bootstrap-themes/free
# The project aim for today is to create a fully fledged multi page website using Bootstrap
# and we will be adding dynamic content generation for the blog pages
# The navbar will be made fully responsive as well. So let's begin

# The first step is to select a template and download it in the way that Flask demands it
# This is the template used: https://startbootstrap.com/previews/clean-blog
# Since we will be hosting the site using it, and let's also set up the Flask app while at it
# I also need to have two folders templates and static to have the content for the website
# After downloading all the HTML, CSS, JS and image files, I also created header and footer html
from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/")
def homepage():
    # We need to make an API call to get the blog posts in a JSON format
    # Instead of using the default blog posts provided in the course, I used ChatGPT
    # to generate me random content. Also the one in the course didn't have author
    # name or date of post, so I had to do it all myself, took a while
    blog_response = requests.get('https://api.npoint.io/1ec6ddcf693c57328f6d').json()
    return render_template("index.html", all_posts = blog_response)
# Since 127.0.0.1 is also called "localhost", our site is available at localhost:5000

@app.route("/post/<int:post_id>")
def post(post_id):
    all_blogs = requests.get('https://api.npoint.io/1ec6ddcf693c57328f6d').json()
    specific_post = all_blogs[post_id - 1]
    return render_template("post.html", post= specific_post)

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug= True)