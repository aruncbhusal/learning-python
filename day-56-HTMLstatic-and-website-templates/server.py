# Yesterday we dealt with returning multiple HTML elements with Flask
# But that is not what we have been used to. We are used to dealing with
# separate files for HTML and CSS. And today we're learning just that
# How to work with those files in Flask

# First let's create a basic hello world main page for our Flask app to start

from flask import Flask, render_template
# We need to import a function called render_template to render own HTML

app = Flask(__name__)

# In order to render our own HTML page, we can look to the documentation.
# We can see that in the "rendering templates" section it specifies how we can
# put HTML files on the server. We need to have them inside a folder called
# templates in the current directory, so let me create that folder and a simple
# index website to go along with it
@app.route("/")
def home():
    # return "Hello World!"
    return render_template("index.html")
# The next challenge after adding the static image file was to add a styles.css to
# work with the index file. Let me see if having a "styles" folder inside templates
# will do the work, or I should have it inside the static folder, let me try first
# Well it didn't show so let me try to put it inside the static folder
# And yup, I needed to have it inside the static folder
## One thing to keep in mind when testing for these changes in the static files is
## that chrome likes to cache our static files so that it doesn't have to download
## them too much for the same website. So in order to view the changes, we must do a
## hard refresh (hold shift while refreshing) and it should update the cache

# A challenge was to download the "Resume site" and modify it, and use that as template
# So I did that
@app.route("/me")
def about_me():
    return render_template("cv_site.html")
# When downloading the site, it may download as ".htm" since some servers are only
# compatible with file extensions upto 3 letters
# One thing I noticed here was that the image wouldn't load like it normally should
# Upon looking at the course lecture, I realized the Flask Framework specifies that
# we must store all our static files in a folder called "static"
# So after including our photo in the static folder, it should load with no problems

# Apparently we made a personal website on day 43 and 44?? The only thing I made was
# a motivational poster page. I don't remember having such a detailed project on those days
# but anyway, I downloaded the one from the course resources and modified it, so let's
# now have it be displayed on our server too
@app.route("/myself")
def about_me_2():
    return render_template("personal_site/index.html")

# We can also use templates from someone else like we did here, by going to websites
# like https://html5up.net/ which have a lot of templates to choose from
# We could also use SquareSpace but it is not free to use
# We can download the HTML and CSS files from HTML5Up and edit them to our liking
# There are multiple ways to edit a page to what we like
# We can simply go to our html file and make changes from there
# or we can use the chrome developer tools. We have an option in the console to use
# Javascript code to allow edits on the page: "document.body.contentEditable=true"
# The "true" bool in JS is lowercase as opposed to uppercase in python.
# Since the changes are all temporary and will be removed in next refresh, we need
# to download and replace the original file with this new html file to make the changes

# For the final project for today we'll be creating a name card webpage, using a template
# from the HTML5up website. The course used the "Identity" template from the site, but
# I couldn't find identity in the site, so I'll just have to use something else
# I thought HTML5up was community driven, but seems like they're just a free service site
# I looked at "Miniport" but it was too simplistic, I liked "Fractal" and "Hyperspace" but
# they weren't what the course was after. Now my options are "Ethereal", "Aerial" & "Astral"
# I'll use Aerial, since Astral was too simplistic and Ethereal too generic for my tastes
@app.route("/project")
def project_page():
    return render_template("project/index.html")

if __name__ == "__main__":
    app.run(debug = True)