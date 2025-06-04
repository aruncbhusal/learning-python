from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO1(done): Create a RegisterForm to register new users
# This is the first task we need to do tackle, to allow a user to register into the website
class CreateRegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")
# Now I'll go to the register route and template for register and render this form there


# TODO5a: Create a LoginForm to login existing users
# Similar to previously
class CreateLoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


# TODO8: Create a CommentForm so users can leave comments below posts
# Onto the start of the final task
class CreateCommentForm(FlaskForm):
    body = CKEditorField('Comment')
    # Can't believe I had to go back to docs after having done it literally yesterday
    submit = SubmitField("Submit")
