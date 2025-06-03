# Authentication is a way by which we can associate some data to a user in a database
# That way no one but the user themselves can access their private data
# It can also be used to provide permissions for certain contents to certain users
# Authentication is more concerned with the security of the data rather than the UX

# In this task, the routes are pre-established, and the pages are almost all completed
# The login and signup pages are made for us, we just need to be able to use them to add authentication features

# Currently the passwords in our database are stored using plaintext, but we need to store them securely
# Our next task is to use hashing and salting using werkzeug tools


from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'UTTE756it8NO89B7Tr6'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
# I wonder why we're using the posts.db file instead of users.db, both have a table called user with same fields
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Instantiate Login Manager:
login_manager = LoginManager()
login_manager.init_app(app)

# Create the load_user function
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
# I was getting crazy about how to implement the User class for Flask-Login
# After looking at the hints and still not understanding, I had to look at the solution
# So it said "multi-inheritance" because I had to add it as the base class for this class

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    # The first task is to update this page so that we add the user to the database
    # And after registering, the user should be sent into the secrets page
    if request.method == "POST":
        # I wonder if the solution gets everything from the form beforehand and then creates an object
        
        # We also need a flash method to notify user if their email is already in the database, 
        # before attempting to create duplicate, which is not allowed and throws an error
        email = request.form.get('email')
        if db.session.execute(db.select(User).where(User.email == email)).scalar():
            flash("This email has already been used in another account.", "error")
            return redirect(url_for('register'))
        
        # or uses it inside the instantiation itself. Well I'll try to only do the password field first
        pass_hash = generate_password_hash(
            request.form.get('password'),
            method = "pbkdf2:sha256",
            salt_length=8
        )
        # Looks like my approach coincided with the course solution, so I'm golden for now
        # Also, we were tasked to use pbkdf2, which is less recommended than scrypt, well that's that
        
        new_user = User(
            name = request.form.get('name'),
            email = email,
            password = pass_hash
        )
        db.session.add(new_user)
        db.session.commit()
        
        # Now we need to login the user and authenticate them to the secrets page
        login_user(new_user)
        
        # had to look at the solution for this one, because I had no method to send the name via redirect
        # Turns out the way was to render the page from this function itself, rather than from secrets function
        # return render_template("secrets.html", name = new_user.name)
        # I could also have used request.form.get('name') here but that would be redundant
        return redirect(url_for('secrets'))
        # In the end I returned to the same redirect method because now we can validate authentication
    return render_template("register.html")
    # In the course solution, the hiding of buttons was done by passing current_user.is_authenticated
    # into each of these template renders, but I just used it inside the templates themselves


@app.route('/login', methods = ["GET", "POST"])
def login():
    # We will need to handle this part using the Flask-Login
    if request.method == 'POST':
        user = db.session.execute(db.select(User).where(User.email == request.form.get('email'))).scalar()
        print(user)
        if not user:
            # If no user exists with the given email then we must alert the user
            # We were suggested to use the flash method to do this
            flash("No account with the given email was found!", "error")
            return redirect(url_for('login'))
        
        if check_password_hash(pwhash = user.password, password = request.form.get('password')):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            # Similarly another flash message if password is wrong
            flash("The entered credentials do not match our data. Try again!", "error")
            return redirect(url_for('login'))
            
    return render_template("login.html")

# Now final thing is the addition of @login_required, as well as the logout logic which is just a single line
@app.route('/secrets')
@login_required
def secrets():
    # The task here is to only allow secrets.html to be rendered if the user is logged in
    # We need to use Flask-login to make sure that is done
    return render_template("secrets.html", name = current_user.name)
    # We can use current_user to get the object of the authenticated user


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    # Our second task is to allow for a download to take place, so we modify secrets.html for href to this route
    # Then we need to look at the documentation for a flask method called send_from_directory
    return send_from_directory(
        'static', 'files/cheat_sheet.pdf'
    )
    # Well this was simple, but I didn't understand the docs at first and was trying to use app.config[] dictionary,
    # without putting the value for the download folder


if __name__ == "__main__":
    app.run(debug=True)
