from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, ValidationError
import csv

# In today's project we're building a Cofee and Wifi website, all the required stuff
# like html pages, Jinja templating, server setup has been done, we only need to make
# sure the ened result matches the one shown in the course
# The things that have to be done were in the requirements in the course, we will be
# working with that

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Since we need to validate and check whether the maps link is a URL, we use:
# def validate_url(form, url):
#     if url.data[:4] != "http":
#         raise ValidationError("You must submit a maps URL here")
# From the solution I realized there was a validation object called URL() already
    
def validate_time(form, time):
    # While we're at it let's also validate the opening and closing times
    if not (time.data[-1] == "M" and (time.data[-2] == "A" or time.data[-2] == "P")):
        raise ValidationError("Please enter the data in the specified format")

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField(label= 'Cafe Location (URL)', validators=[DataRequired(), URL()])
    open_time = StringField(label= 'Opening Time (eg. 6:30 AM)', validators=[DataRequired(), validate_time])
    close_time = StringField(label= 'Closing Time (eg. 4:30 PM)', validators=[DataRequired(), validate_time])
    coffee_rating = SelectField(label= 'Coffee Rating', validators=[DataRequired()], choices=['☕☕☕☕☕'[:n+1] for n in range(5)])
    wifi_rating = SelectField(label= 'Wifi Strength Rating', validators=[DataRequired()], choices=['💪💪💪💪💪'[:n] if n>0 else '✘' for n in range(6)])
    power_rating = SelectField(label='Power Socket Availability', validators=[DataRequired()], choices=['🔌🔌🔌🔌🔌'[:n] if n>0 else '✘' for n in range(6)])
    submit = SubmitField(label= 'Submit')
    

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    # Looks like form.data gives us a dictionary of all data items in the form
    # with key names being the variable names. Perfect for iteration
    if form.validate_on_submit():
        with open("./cafe-data.csv", 'a', encoding="UTF-8") as cafe_data:
            cafe_data.write("\n")
            for (field_name,value) in form.data.items():
                cafe_data.write(f"{value}")
                if field_name != "power_rating":
                    cafe_data.write(",")
                else:
                    break
                # Had to put this cause there were other data that was hidden to me
                # The course solution has all the items written individually, fine.
        # Since the page seems to change after submitting, and rather than setting the
        # other function as a POST and this one only as GET, I'll use the redirect method
        # return redirect("localhost:5000/cafes", code= 200)
        # Okay this seems a bit too clunky for my tastes, I'll just see the solution
        # Who would have thought?? It's using the redirect method
        return redirect(url_for('cafes'))
        
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
