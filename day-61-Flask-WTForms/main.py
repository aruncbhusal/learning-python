from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4
# In the docs Bootstrap4 and 5 were both used, but let's see what Bootstrap5 can do
# So the BS5 didn't have Jumbotron class it seems, I have resorted to BS4

# In yesterday's lessons we used HTML Forms to integrate with Flask to send data
# from our forms to be used in the server, but today we're working with a Flask
# extension called WTForms, it is used to reduce redundancy, ease data validation
# like @ in emails, and provide Cross Site Request Forgery (CSRF) protection.
# I'm using the starting files given in the project, that has a requirements.txt
# using which I created a virtual environment with all the dependencies installed.


'''
Course Instructions:
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# From the Flask-WTF docs, we will need to use a class with inheritance to
# create a form using WTForms, https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/
class LoginForm(FlaskForm):
    # We need to create two fields for email and password, we can also have CSRF
    # protection, which I will use just for the sake of it, and it is apparently
    # auto generated in recent WTForms versions
    # Both the fields are StringFields with 30 characters max, and no validation
    
    # Now in the next step, we finally add validation, since we pass a list of
    # validator objects, we first start with making both these fields required
    # Challenge: Validate the presence of @ and . in the email and 8 characers min pass
    email = StringField(label="Email", validators=[DataRequired(),
                                                   Email(message='Email must have @ and .')])
    # So the email validator requires the email validator package to be installed
    # Since the errors generated are too generic, we can specify our own messages
    
    # Since a StringField displays all characters that are typed, but we don't want
    # that to happen to the password field, we will change it to PasswordField
    # Also I had already added the keyword arguemnts, while in the quickstart  the
    # label was passed as a normal positional argument
    password = PasswordField(label="Password", validators=[DataRequired(),
                                                           Length(min=8, message='At least 8 characters required, bozo!')])
    # These validators generate an error in the forms if requirements are not met
    # Finally the submit field, instead of having it as an Input we can use a WTfield??
    submit = SubmitField(label= "Log In")


app = Flask(__name__)
# By default CSRF protection will use the same secret key as the Flask app, so
app.secret_key= "some random string"

# Now we need to add the bootstrap functionality to our app, but it can be done with
# a python extension called Bootstrap-Flask, instead of having to add the links manually
# Apparently it cannot work together with Flask-Bootstrap, which is some other package,
# if it was installed, we would need to uninstall it to use this one.
bootstrap = Bootstrap4(app)

@app.route("/")
def home():
    return render_template('index.html')

# The first challenge here is to make the page work by adding a login page
# Since in the index, a url_for is specified, we need to adhere to that naming
@app.route("/login", methods= ["GET", "POST"])
def login():
    login_form = LoginForm()
    # Now in order to implement the validation, we need to get the data from there
    # which means we need to add this function as a recipient for requests
    # Since this validate on submit runs for both get and post requests to this page
    # We need to use an if to separate get from post, while here it will only get
    # validated on a post request so we can run code assuming post request there
    if login_form.validate_on_submit():
        # We can now access the form data using the .data suffix here
        # Challenge was to show success page if credentials match given ones, else
        # display the denied page
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template("denied.html")
    # Since we have this validation, the browser wants to validate itself as well
    # So we want to turn off browser validation in the HTML
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
