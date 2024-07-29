from flask import Flask, render_template, request
import requests
import smtplib

EMAIL= "<YOUR_EMAIL>"
EMAIL_TWO= "<RECIPIENT_EMAIL(Can be the one acquired from the post request)>"
APP_PASS= "<MAIL_APP_PASSWORD>"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/1ec6ddcf693c57328f6d").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")
# This was combined with the login submit function to handle both
# post and get requests using the same function


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

# First task here was to add a route for form-entry where we display a h1 text
# "Successfully submitted your information", and print the collected data in terminal
@app.route("/contact", methods= ["GET","POST"])
# The route for this was "/form-entry" but instead since we're using the same route
# i.e. /contact for both post and get, we'll just have to combine and compare
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        # Finally, instead of printing all these values, let's send them via email
        # print(f"Name= {name}\nEmail= {email}\nPhone: {phone}\nMessage: {message}")
        with smtplib.SMTP(host="smtp.gmail.com",
                          port= 587,) as mailer:
            mailer.starttls()
            mailer.login(user= EMAIL,
                         password= APP_PASS)
            mailer.sendmail(from_addr= EMAIL,
                            to_addrs= EMAIL_TWO,
                            msg= f"Contact Form\n\nName= {name}\nEmail= {email}\nPhone: {phone}\nMessage: {message}")
    # There was an else statement for GET here, but since we're passing the same
    # value either way, I thought I may as well unify things
    return render_template("contact.html", method= request.method)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
