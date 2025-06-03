# Today's project is building upon the blog site we made in the past and adding RESTful routing to it
# Given: imports set up, Bootstrap set up with CSRF security, Flask app set up
# Rest of it is left initiated and are marked as TODOs so we'll build upon them
# This time we're pulling the psots not from a JSON dump but an actual database inside the /instance folder


from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import time # For delay

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
# We also need to create a CKEditor here, to add formatted inputs
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO1(done): Query the database for all the posts. Convert the data to a python list.
    # Since the template is almost made for us, we just need to populate the posts list from the db
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    # Single line, nice
    return render_template("index.html", all_posts=posts)

# TODO2(done): Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # TODO2(done): Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    # Another single liner, nice
    # In the course the following line was used instead, which might be better maybe?
    # requested_post = db.get_or_404(BlogPost, post_id)
    
    # Since post_id is our primary key it might actually be more efficient, but I'm sticking to mine for now
    return render_template("post.html", post=requested_post)


# TODO3(done): add_new_post() to create a new blog post

# We also need a form class for the WTForms + CKField (textarea) combo
class PostForm(FlaskForm):
    title = StringField('Post Title', validators=[DataRequired()])
    subtitle = StringField('Post Subtitle', validators=[DataRequired()])
    author = StringField("Author's Name", validators=[DataRequired()])
    bg_img = StringField('Background Image URL', validators=[URL(), DataRequired()])
    body = CKEditorField('Blog Body')
    submit = SubmitField('Submit', validators=[DataRequired()])
    


@app.route("/new-post", methods = ["GET", "POST"])
def add_new_post():
    # Since we need to display a form as well as submit into the database from this page, we need both GET and POST
    # I think I'll need to look at the docs for this one
    # Okay now that I've created the form, next my job is to render the form in the html file
    form = PostForm()
    
    if form.validate_on_submit():
        new_post = BlogPost (
            title = form.title.data,
            subtitle = form.subtitle.data,
            date = date.today().strftime("%B %d, %Y"),
            author = form.author.data,
            body = request.form.get('body'),
            # We could also just use form.body.data here. The CKEditor has data in HTML format
            # Inside the post.html, we have used post.body|safe, where safe means a filter
            # It allows body to be treated as a HTML and not just text. We didn't sanitize it
            # So it means someone can inject a malicious <script> into it and break something
            img_url = form.bg_img.data
        )
        
        db.session.add(new_post)
        db.session.commit()
        
        # I want to try the Flask flash method this time, as recommended by GPT
        # flash("The post has been added successfully!", "success")
        # Well the message couldn't even be seen because I didn't add any such element in template
        # Honestly I'll just leave it as is, no drama
        
        # I got an idea, we should just redirect it to the new post that user created so there's no confusion
        return redirect(url_for("show_post", post_id = new_post.id))
        
    
    return render_template("make-post.html", form = form)


# TODO4(done): edit_post() to change an existing blog post
@app.route("/edit-post/<int:id>", methods = ["GET", "POST"])
def edit_post(id):
    # This is usually a PUT/PATCH request but since we're using forms to do it, we need POST
    post_to_edit = db.session.execute(db.select(BlogPost).where(BlogPost.id == id)).scalar()
    form = PostForm(
        title = post_to_edit.title,
        subtitle = post_to_edit.subtitle,
        body = post_to_edit.body,
        author = post_to_edit.author,
        bg_img = post_to_edit.img_url
    )
    # As per the course instructions, I just populated the form before displaying it
    
    if form.validate_on_submit():
        post_to_edit.title = form.title.data
        post_to_edit.subtitle = form.subtitle.data
        post_to_edit.author = form.author.data
        post_to_edit.body = request.form.get('body')
        post_to_edit.img_url = form.bg_img.data
        # We're not editing the date or the id for obvious reasons
        
        db.session.commit()
        return redirect(url_for('show_post', post_id = id))
        # It was while doing this that I figured out we could do this in the new_post one too
    
    
    return render_template("make-post.html", form = form, edit = True)

# TODO5(done): delete_post() to remove a blog post from the database
@app.route("/delete-post/<int:id>")
def delete_post(id):
    # This one is simple, we just delete then reload the home page, since the delete button is on the home page
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == id)).scalar()
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('get_all_posts'))
    

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
