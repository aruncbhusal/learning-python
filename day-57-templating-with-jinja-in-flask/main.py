from flask import Flask, render_template
import requests
from post import Post
# Okay now time for the final project for today
# I'll be using the template for the blog app pre created, and will be adding
# functionality for traversal of paegs into the site
# the basic structure for each website, as well as the CSS is already there
# I just have to do the templating work now

app = Flask(__name__)

@app.route('/')
def home():
    # We need to use the same JSON api as before for the blog posts
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("project/index.html", posts= all_posts)

# Now for the post page, I wonder why I was given a class, but maybe I should just
# have a class with simply some attributes and no content?
# I wonder what the idea behind having a class here would be but anyway
@app.route("/post/<int:post_id>")
def single_post(post_id):
    # Maybe I'll use the post class to pull in all data and put into attributes
    post = Post(post_id)
    return render_template("project/post.html", post= post.jsonify())
    # Apparently the HTML cannot show us attributes from a class, so we'll need to
    # pass in data in the format it can understand

# And done! That's all for today.

if __name__ == "__main__":
    app.run(debug=True)
