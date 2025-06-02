# The client makes a request to the server, it may be a HTTP request, FTP request or other type of request and the server sees it
# Then it checks if the request can be fulfilled, and if it can't it returns an error code
# If it can fulfill the request, it accesses the database and/or processes the request and gives the client its requested information
# The API bridges this gap between client and server, anad RESTful API is just a architecture for it
# There are other architectures like SOAP, GraphQL, Falcor, etc, but REST is the predominant one for webAPI
# This API was a result of Roy Fielding's PHD research, in order to make the web requests consistent
# The rules to make an API RESTful are: use HTTP request verbs, and use specific pattern of routes/endpoint URLs

# HTTP verbs: GET, POST, PUT, PATCH, DELETE
# The routes may be something like /topic to make changes to entire topic, or add a single subtopic to it, and /topic/subtopic to make changes to the subtopic only
# The difference between PUT and PATCH is that PUT updates the entire object in question, but PATCH only changes a single(or more) attribute/value that actually needs to be fixed.
# Using PATCH reduces the bandwidth spent in correcting a piece of data.

# In today's challenge we need to build an API for a website that gives out cafes in London
# The database is given,, its model and table is created already for us and the empty flask app is set up
# Now our job is to follow the instructions and complete the project


from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# Since there are two different routes that need the same feature: dict conversion, I'll use DRY here
def cafe_to_dict(random_cafe):
    return {
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        # Let's separate hotel attributes and features
        "services" : {
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price
        }
    }

# Here our job is to fetch a random cafe from our database and return it to the user
# The methods part may be omitted as it is available by default on all routes
@app.route("/random", methods = ["GET"])
def give_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    # random_cafe = all_cafes[random.choice(all_cafes)]
    # I seem to have been on the right path, even though I had to look at my past code for it
    # Looking at the solution, I found out that I somehow put random.choice as an index 🤦
    random_cafe = random.choice(all_cafes)
    # It took me a long time to get this to work because somehow the database appeared empty
    # It was fixed after finally creating a .venv folder in the cwd(current working directory)
    
    # I could also use "if all_cafes" to see if the list is empty and return 404 if empty
    
    # print(random_cafe) gives a Cafe object but we want a JSON format, and Flask's jsonify() works only on dicts so I need to first convert the object into a dict
    # After looking at the solution, that appears to be how it was done as well, thanks GPT. I will now implement it myself
    response = jsonify( cafe = cafe_to_dict(random_cafe)) # Though I don't think naming this dict was necessary
    return response

# Another challenge with GET is to list all cafes in our database
@app.route("/all")
def all_cafes():
    cafe_list = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    # cafe_names = [cafe.name for cafe in cafe_list]
    # return f"{cafe_names}"
    # I was planning to only output the names of the cafe but it was too simple
    # So I looked at the solution and saw the whole database being given in a json format so I'll do that now
    elaborated_list = [cafe_to_dict(cafe) for cafe in cafe_list]
    return jsonify({"Cafes" : elaborated_list})

# Final GET challenge was to implement a search functionality according to location
@app.route("/search", methods=["GET"])
def search_cafe():
    loc = request.args.get('loc')
    if not loc:
        return jsonify( error = {
            "status": "failed",
            "reason": "No parameter found. Please add a loc parameter to search for cafe at a location"
        }), 404
    
    # cafe_list = db.session.execute(db.select(Cafe).filter_by(location = loc)).scalars().all()
    # I looked up and found the filter_by method to filter, but the course has suggested where method, and since I've already tried and finished it with filter_by, I'll try where now
    cafe_list = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if not cafe_list:
        return jsonify( error = {
            "status": "Not found",
            "reason": "There exists no cafe in our database at that location"
        }), 404
    
    return jsonify( {
        "Cafes": [cafe_to_dict(cafe) for cafe in cafe_list]
    })
    
# A tool developers use is Postman, which lets us test our APIs, different parameters and such
# Testing in a browser is error prone and tedious, so Postman bridges this gap

# HTTP POST - Create Record
# We can also make POST requests using Postman, and we can simulate forms using it as well.
# In the "body" part of the request, selecting x-www-form-urlencoded allows us to add labels and their values with it
# First we need to create a route to suggest a new hotel, which will add it to the database

@app.route("/suggest", methods = ["POST"])
def suggest():
    # Had to take a look at the solution to see what we were even supposed to do
    # So apparently we don't need to create a form, just take inputs as if the form already exists
    new_cafe = Cafe(
        name = request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_toilet = bool(request.form.get('has_toilet')),
        has_wifi = bool(request.form.get('has_wifi')),
        has_sockets = bool(request.form.get('has_sockets')),
        can_take_calls = bool(request.form.get('can_take_calls')),
        # I kept getting errors and found out bool function needed to be used for 1 and 0 to become booleans
        coffee_price = request.form.get('coffee_price')        
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {'success': 'The cafe was added to the database successfully.'})


# HTTP PUT/PATCH - Update Record
# The next thing on our menu is to update a certain value, like when a certain cafe changes its coffee price. We can use the PATCH verb
# We need to make a /update-price route where we can change only the coffee price. It is possible to make a single /update but its parameters would be tedious

@app.route("/update-price/<int:id>", methods = ["PATCH"])
def update_price(id):
    new_price = request.args.get('new-price')
    # the_cafe = db.get_or_404(Cafe, id)
    # Initially the instruction was to use get_or_404, but then we needed custom error messages so now we need get
    # There was a "try-except" block here but since db.session.get just returns None if not found, I had to go a different approach
    the_cafe = db.session.get(Cafe, id)
    if not the_cafe:
        return jsonify(error = {"Failed" : "The cafe with given id does not exist in the database."}), 404
    the_cafe.coffee_price = new_price
    return jsonify(response = {"success" : f"The coffee price was successfully updated for the cafe: {the_cafe.name}"})

# HTTP DELETE - Delete Record
# Finally we also need a route where we can delete cafes from the db. For this we will secure it using an API key
@app.route("/close-cafe/<int:id>", methods = ["DELETE"])
def close_cafe(id):
    # In the example the API key seems to be passed using a query parameter, but I don't want that
    # I want to test using the actual headers so I'll use that
    api_key = request.headers.get('API-KEY')
    
    the_cafe = db.session.get(Cafe, id)
    if not the_cafe:
        return jsonify(error = {"Not Found" : "The cafe with the id in the URL couldn't be found in the database."}), 404
    
    if api_key != "topSecret":
        return jsonify(error = {"Unauthorized" : "You are not allowed to delete records without the correct API key."}), 403
        # 403 is the "Unauthorized" HTML Status Code
    
    # Finally now that we're clear to delete, we can initiate that process
    db.session.delete(the_cafe)
    db.session.commit()
    
    return jsonify(response = {"Success" : f"The records for the cafe with id {id} have been deleted from the database."})
    
# The last thing we learnt today is that we can get Postman to create the docs from the actions we saved in our collection
# We can then publish the said docs after adding descriptions and making it informative. but since my website is local, no point in publishing the docs online
# This was all for today.

if __name__ == '__main__':
    app.run(debug=True)
