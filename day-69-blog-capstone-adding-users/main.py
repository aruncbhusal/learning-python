# Our final task with the blog project is to add users so that they can login, and leave comments on the blogs
# We need to use what we learnt yesterday i.e. authentication, to make it possible
# We will go through each TODOs and finally complete the full blog project today
# Given: imports set up, forms class created in forms.py, and the rest is normally where we left off in last capstone

from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash,get_flashed_messages
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from typing import List #doing it because GPT told me to
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, CreateRegisterForm, CreateLoginForm, CreateCommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO4: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Next we will need to have a callback to load_user function to load the user
@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
# Our next change is a big one. We will need to delete the entire database and createa a new one
# In this new database, our Users table will have a One-to-Many relationship with the BlogPost table
# Since we need to give access to users to post what they want and they can edit/delete their posts as well
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped['User'] = relationship(back_populates='posts')
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments: Mapped[List['Comment']] = relationship(back_populates='parent_blog')

# Now that the author field has User object instead of the name, we need to modify index and post.html


# TODO2: Create a User table for all your registered users.
# Since I already have a reference to a table creation above, it feels like cheating
# But these rules are all made by people anyway so not remembering a syntax and having to reference something else is not a weakness
# I think I'll add UserMixin as a base class as well, because I'll need to use it later for auth anyway
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    # One user can have multiple blogs
    posts: Mapped[List['BlogPost']] = relationship(back_populates='author')
    # One user can also have multiple comments
    comments: Mapped[List['Comment']] = relationship(back_populates='author')
    
# After doing all this I was frustrated because I felt I had done everything right but
# there was no "posts" field in user table, nor "author" field in blog_posts table
# Then I asked GPT and I found out these relationships are just ORM level abstractions
# and not something actually stored in the database. They just let me access blog's author or user's posts
# The foreign key is stored, and python just calls SQL command to retrieve the user/post(s) based on it

# Now we need a new table to store the comments
class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String, nullable=False)
    # We also need a one-to-many relationship from user-comment and blog_post-comment
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    author: Mapped['User'] = relationship(back_populates='comments')
    post_id: Mapped[int] = mapped_column(ForeignKey('blog_posts.id'))
    parent_blog: Mapped['BlogPost'] = relationship(back_populates='comments')


with app.app_context():
    db.create_all()
    
# Final task is to create Gravatar for comments and use it
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# TODO3: Use Werkzeug to hash the user's password when creating a new user.
# Using the same salting procedure as last time probably
@app.route('/register', methods = ["GET", "POST"])
def register():
    form = CreateRegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        if db.session.execute(db.select(User).where(User.email == email)).scalar():
            flash("An account with the entered email already exists, log in with the email instead!", "redirect")
            return redirect(url_for('login'))
        
        hashed_pw = generate_password_hash(form.password.data,
                                           method = "pbkdf2:sha256",
                                           salt_length = 8)
        new_user = User(
            name = form.name.data,
            email = email,
            password = hashed_pw,
        )
        db.session.add(new_user)
        db.session.commit()
        # flash("The account has been created successfully. You may now login.", "success")
        # Since this message can't be displayed as they'll be leaving the page, I'll omit it
        login_user(new_user)
        return redirect(url_for('get_all_posts'))
        
    return render_template("register.html", form = form)


# TODO5: Retrieve a user from the database based on their email. 
@app.route('/login', methods = ["GET", "POST"])
def login():
    login_form = CreateLoginForm()
    if login_form.validate_on_submit():
        # First we see if the user account exists
        user = db.session.execute(db.select(User).where(User.email == login_form.email.data)).scalar()
        if not user:
            flash("No account exists with the provided email. Please try again!")
            return redirect(url_for('login'))
        # Then we check the password using Werkzeug tools
        if check_password_hash(user.password, login_form.password.data):
            login_user(user)
            return redirect(url_for('get_all_posts'))
        else:
            flash("The password for the given account is incorrect. Please try again!")
            return redirect(url_for('login'))
    
    return render_template("login.html", form = login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO8.1: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    comment_form = CreateCommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to be logged in in order to post a comment.")
            return redirect(url_for('login'))
        new_comment = Comment(
            text = comment_form.body.data,
            parent_blog = requested_post,
            author = current_user
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('show_post', post_id = post_id))
    return render_template("post.html", post=requested_post, form=comment_form)


# TODO7: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# Let's create a decorator here that can be used to stop a user if they're not admin(id=1)
# The name stays, but it does something different now. The person can edit post if they are the author
def admin_only(f):
    @wraps(f)
    def wrapper(post_id, *args, **kwargs):
        post = db.get_or_404(BlogPost, post_id)
        if current_user and current_user.id == post.author_id:
            return f(*args, **kwargs)
        return abort(403)
        # The solution uses != logic, I'll just keep mine the straightforward way, both will return anyway
    return wrapper
# Have I gotten so bad at understanding docs that I had to resort to ChatGPT because I didn't realize I wasn't returning f
        

# TODO7: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO7: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
