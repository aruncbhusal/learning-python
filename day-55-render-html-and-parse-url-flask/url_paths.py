# In today's lessons we dive deeper into Flask and deal with the URL paths we see
# What if we wanted to customize the content in the page we display depending on
# the route the client has specified. Maybe take input from the url as well
# Let's first set up the basic flask app, without any help first

from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

# Now what if I wanted to display the name of the person, provided they visit the
# website with their name in the route
@app.route("/<name>/<int:roll>")
def sup(name, roll):
    # The variable names here must match the ones given above
    return f"What's up {name}, haven't seen you in a while! Your roll number is {roll}"
# The default value for the variable in the route is a string without a slash
# if we are to use a slash, we must specify a "path:" before the variable name
# For the integer roll number, I used int: above
# Each time we save code changes, it automatically restarts the server with changes loaded

# All that is fine and all, but what if I wanted to have more than just text on the site
# If we inspect any pages we have, everything is bundled within the body tag
# In order to add HTML to our page, we can just write it all inside the return
@app.route("/cat")
def cat():
    return '<h1 style="text-align: center">Presenting, CAT</h1>' \
            '<p>Just a picture of a cat</p>' \
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTFpNjYxaDg4aDk5M3dhb3RreDBjM2lkdTN6N2F2bHZybGRhcjE2ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BBNYBoYa5VwtO/giphy.gif" width=400px>'
# Notice I have used single quotations here while I used double before, it is so that
# it doesn't conflict with the double quotes used for attribute values
# And the '\' is handy to split the text to multiple lines so that it doesn't look a mess
# The image tag supports gifs so the page is exciting to say the least
# The page contains multiple elements, and one with inline style as well

# Now for a little challenge regarding decorators, what we're aiming for is a page:
# let's call the page: "kachow"
                    # @app.route("/kachow")
                    # def kachow():
                    #     return "<u><em><b>Kachow chow chow</b></em></u>"
# The above code will return the text with bold(b), italic/emphasized(em) and underlined(u)
# styles, but rather than having them all in strings, which looks awkward to return, we need
# to implement three decorators that will add the bold, emphasis and underline tags to a text

# Let's first create the three decorators:
def make_bold(function):
    def wrapper_func():
        return f"<b>{function()}</b>"
    return wrapper_func

def make_emphasized(function):
    def wrapper_func():
        return f"<em>{function()}</em>"
    return wrapper_func

def make_underlined(function):
    def wrapper_func():
        return f"<u>{function()}</u>"
    return wrapper_func

@app.route("/kachow")
@make_bold
@make_emphasized
@make_underlined
def kachow():
    return "Kachow chow chow"
# No problem, done with no issues whatsoever


# Now for the final challenge for today
# We need to have a random number guesser game running in our website
# We will first generate a random number and then the user can visit
# numbers indexed 0-9 and try to guess the number by visiting the correct route

# Let's start by first generating the number
magic_number = random.randint(0,9)
# Now the homepage for the game
@app.route("/game/")
# From the docs of Flask, I read that we can specify the forward slash at the end
# to indicate that there are other pages inside this directory
# If we don't specify that, using it in the URL would give us an error
# And since we will have a page for each number, we'll use the slash
def gamepage():
    # Let's let the user know about the game here
    return '<h1 style="text-align:center">Guess-chan</h1>' \
        '<p>Go to the correct page (0-9) inside this to guess the number</p>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=400px>'
    # I used the image given in the assignment instructions because I couldn't find a better
    # one in giphy

# Now for the pages to guess
# I'll just make three decorators that will add the elements as per the guess status
# def guess_page_decorator(function):
#     def wrapper(*args):
#         args[0]   
#     return wrapper
# If it's for just a single function, I don't see the point of having these decorators in place
@app.route("/game/<int:guess>")
def guess_page(guess):
    too_high_gif = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzI0am0xMjFkZ2t4dnA1MmgxcXg2cHVtbGltZnp3dHVscmVhMHdpciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/w3J7mstYCISqs/giphy.gif"
    too_low_gif = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGkyOWd3eTVsMmEyMXY2dTRmNzc0cjRieGg3dXlsMmloMGdqbHU4NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nR4L10XlJcSeQ/giphy.gif"
    correct_gif = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3c1bndueWRldGZxamJiOW1vd2IybnhkYThvd3pjaG94aWJyOXd4dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.gif"
    overflow_gif = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXp4eWxlaXFxNDAzd3RrNjRveHlzMmRlbGIxd201cmVtOTh5aXo1ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qZgHBlenHa1zKqy6Zn/giphy.gif"
    # The assignment included a challenge to have each page have a different color
    # which means low should have one color, high should have some other
    # Since the return should be different for all, I'll just have to specify a string
    # that has the html elements within it
    if guess == magic_number:
        heading_element = f'<h1 style="background: black; color: green; text-align: center">You guessed it right!</h1>'
        guess_gif = f'<img src="{correct_gif}" width= 800/>'
    elif guess > 9:
        heading_element = f'<h1 style="background: black; color: blue; text-align: center">That was wayyyy off</h1>'
        guess_gif = f'<img src="{overflow_gif}" width= 800/>'
    elif guess < magic_number:
        heading_element = f'<h1 style="background: black; color: aqua; text-align: center">Too low! Try again.</h1>'
        guess_gif = f'<img src="{too_low_gif}" width= 800/>'
    elif guess > magic_number:
        heading_element = f'<h1 style="background: black; color: red; text-align: center">Too high! Try again.</h1>'
        guess_gif = f'<img src="{too_high_gif}" width= 800/>'
    return f"{heading_element} {guess_gif}"


if __name__ == "__main__":
    # app.run()
    # When the above line has no arguments passed, the debug mode for the server is off
    # When we turn on the debug mode, we can see code changes reflected in the site
    # without having to stop and restart the server, it also provides us the debugger
    app.run(debug = True)
    # Here we have received a debug pin, which we can use in case our code changes cause
    # an error, which will be displayed in the webpage itself, and it will let us use the
    # console on the page since the one here would be used by the Flask server itself