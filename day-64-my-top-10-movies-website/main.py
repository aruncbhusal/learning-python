from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

headers = {
    "accept": "application/json",
    "Authorization": "Bearer <YOUR_BEARER_TOKEN>"
}

# Probably my last day with this course, before I decide some day to continue again
# Exams are right on the doorstep and I don't think I can get much further in the days
# to come, so after today's project, python will be halted for me.

# In this one, we're making a TOp 10 movie display website, one tha tactually has some
# styling, rather than just looking like the 90s, like the day 63 sql learning project was
# The basic Flask app structure, websites structure and styles have been given
# Now we just need to make it functional
# The inspiration is probably from the tons of website that have made similar lists, and
# a website that is just about people making lists: https://www.listchallenges.com/

# After running the app, I saw that a lot more had been done than I would have expected
# The look of the website was set in stone, we just needed to work with the data entry
# and storage stuff. Basically just a database project.


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

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    # The table has a lot of fields to take care of
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    # Had to turn off nullable for review, ranking and rating to avoid IntegrityError
    # And it still doesn't work. Huh, let me send some placeholder text then
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()
    
# Test:
# with app.app_context():
#     second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(second_movie)
#     db.session.commit()

# Let's set up a form for the update rating section
class EditMovieForm(FlaskForm):
    new_rating = FloatField(label= "Your rating out of 10 (eg 4, 7.5)",
                            validators=[DataRequired()])
    new_review = StringField(label="Your Review", validators=[DataRequired()])
    done = SubmitField(label="Done")

# Now a single input form for Adding new movie
class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Search")
    

# Now we need to make sure the movies appear on the homescreen, so we'll now use the queries
# and display the data in the homescreen
@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    # Now since all these movies will be ordered by ranking in ascending order
    # and we need to display in descending, I will send the data reversed
    # Since I don't know if there's any argument for order_by that can let us do that
    
    # Okay now the final task is to set every movie's ranking dynamically each time the homepage
    # loads so that any change in the database is reflected each time
    # Now the movies are ordered by their rating, so I can just assign the smallest number to
    # the one at first, and so on
    # Ok instead of using _allrows, maybe I can use all, and see how it goes
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies)-i
    db.session.commit()
    # It works exactly the same, who would have guessed? 🤦‍♂️
    return render_template("index.html", movies = all_movies)

@app.route("/edit", methods= ["GET", "POST"])
def edit_movie():
    # I had been seeing errors and had forgotten we needed to pass a form object to the
    # template, and not the class itself
    form = EditMovieForm()
    id = request.args.get('id')
    movie = db.get_or_404(Movie, id)
    if form.validate_on_submit():
        movie.rating = form.new_rating.data
        movie.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie= movie, form = form)

# Now we need to add a feature to delete the movie
@app.route("/delete")
def delete_movie():
    id = request.args.get('id')
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

# Now for the Add movies section, we will need to make an API call to The Movie Database
# (TMDB) after only asking for the name of the movie from the user
@app.route("/add", methods=["GET", "POST"])
def add_movie():
    
    form = AddMovieForm()
    if request.method == "POST":
        url= "https://api.themoviedb.org/3/search/movie"
        parameters= {
            "query": form.title.data
        }
        response = requests.get(url,params=parameters, headers=headers).json()
        all_movies = [movie for movie in response["results"]]
        return render_template("select.html", movies = all_movies)
    else:
        return render_template("add.html", form = form)
    
@app.route("/select")
def select_movie():
    movie_id = request.args.get('id')
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(url, headers= headers).json()
    print(response)
    new_movie = Movie(
        title = response["title"],
        year = response["release_date"].split("-")[0],
        description = response["overview"],
        img_url = f"https://image.tmdb.org/t/p/w500{response['poster_path']}",
        rating = 0,
        ranking = 0,
        review = "None"
    )
    db.session.add(new_movie)
    db.session.commit()
    movie_id= db.session.execute(db.select(Movie).where(Movie.title == response["title"])).scalar_one().id
    return redirect(url_for('edit_movie', id= movie_id))
    

if __name__ == '__main__':
    app.run(debug=True)