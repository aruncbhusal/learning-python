from flask import Flask, render_template, request, redirect, url_for
# For sqlalchemy, we'll need to import lots of stuff
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, text

# The inspiration for today's project comes from libraryanything.com where we can
# rate books that we have read, and they will be stored there
# In order to store a large amount of data, we need a database, which is what we'll do

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class Base(DeclarativeBase):
    pass

    

app = Flask(__name__)

# SQLAlchemy is an ORM (Object Relational Mapping) library which maps the fields into
# objects, each table is a class and each row is an object, the fields then become the
# attributes of the object. This way the relationships in database are mapped to objects
# From the SQLAlchemy docs: https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/
# We need to have a class that inherits the DeclarativeBase class for initialization 
db = SQLAlchemy(model_class= Base)
# Now to connect our app with the database we need to make an initialization
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

# We also need to subclass the db.ModelClass to create a new table
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique= True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
# This only sets up the model but does not create it in the database, if we want to create it
# we need to use create_all later. We can also create tables directly but those are mostly used
# for associations between two tables whose models are usually defined.
with app.app_context():
    db.create_all()
# This creates the schema for the table we have set the models for


all_books = []

# We are given an empty list and two empty functions for each route we need to code
# For the home route, the first challenge is to have a page that says "My Library"
# and a link that says "Add New Book"

@app.route('/')
def home():
    # We can see that each time we reload the server, all books disappear, since the 
    # list all_books is reinitialized, to solve this we need to learn about data
    # persistence and how to use database with Flask
    all_books = db.session.execute(db.select(Books).order_by(Books.id)).scalars()._allrows()
    # I winged the _allrows but ;looks like it works, so great!
    return render_template('index.html', books=all_books)


@app.route("/add", methods= ["GET", "POST"])
def add():
    if request.method == "POST":
        # all_books.append({
        #     # I kinda forgot how to access this data that was received, I need to
        #     # see the solution code since I didn't find any good info in the docs
        #     # Oh after looking at some other site, I realized what I had forgotten
        #     "title": request.form.get('title'),
        #     "author": request.form.get('author'),
        #     "rating": request.form.get('rating'),
        # })
        # Now a challenge is to add the data to the database instead:
        book = Books(
            title = request.form.get('title'),
            author = request.form.get('author'),
            rating = float(request.form.get('rating'))
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
        
    return render_template('add.html')

@app.route("/edit_rating", methods=["GET", "POST"])
def edit_rating():
    # I was thinking this could be the case, and only after looking at StackOverflow
    # am I sure now that this is what it is
    id = request.args.get('id', type= int)
    book = db.get_or_404(Books, id)
    if request.method == "POST":
        book.rating = request.form.get('new_rating')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit_rating.html", book= book)
    
@app.route("/del", methods=["GET"])
def delete_book():
    id = request.args.get('id', type=int)
    book = db.get_or_404(Books, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

# Done! This took quite a while too. At least now I know more about Database!