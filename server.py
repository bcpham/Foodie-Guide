"""Server for Foodie Guide"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
from pprint import pformat

import os
import crud
import json
import pprint
import requests
import sys
import urllib

app = Flask(__name__)

# A secret key is needed to use Flask sessioning features
app.secret_key = 'dev'

YELP_API_KEY = os.environ['YELP_API_KEY']
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = StrictUndefined

#############################################################################

# For Yelp Fusion API
# Search by term and location:
SEARCH_URL = 'https://api.yelp.com/v3/businesses/search' 

# Business ID will come after slash, search by business ID.
BUSINESS_URL = 'https://api.yelp.com/v3/businesses/'#business ID
REVIEWS = '/reviews'
HEADER = {}
HEADER["Authorization"] = "Bearer " + YELP_API_KEY

#############################################################################

@app.route("/")
def homepage():
    """Show homepage."""

    data = []

    return render_template('homepage.html', 
                            pformat=pformat,
                            data=data)
#############################################################################

@app.route("/create-account")
def create_account():
    """Shows Create Account page."""
    
    return render_template("create_account.html")

#############################################################################

@app.route("/create-account", methods=["POST"])
def register_user():
    """Create a new user."""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        #flash("This e-mail is already registered with another account. Try again.")
        
        return render_template("/create_account.html", account="already-exists")

    else:
        user = crud.create_user(fname, lname, email, password)
        db.session.add(user)
        db.session.commit()
        #flash(f"Account created for {user.fname}! Return to home page to log in.")

        return render_template("/create_account.html", account="create", user=user)

#############################################################################

@app.route("/login", methods=['POST'])
def process_login():
    """Process user login"""

    #Don't need this for AJAX
    # email = request.form.get("email")
    # password = request.form.get("password")

    #Need this for AJAX
    email = request.json.get("email")

    password = request.json.get("password")

    print("email: ", email)
    print("password: ", password)
    
    user = crud.get_user_by_email(email)

    print("user: ", user)

    if not user or user.password != password:
        return "False"
    
    else:
        #Log in user by storing the user's user_id in session
        session["logged_in_user_id"] = user.user_id
        return "True"
        
        #return f"Currently logged in: {user.fname}!"

    #Don't need this for AJAX
    #return redirect("/")

#############################################################################

@app.route("/logout")
def process_logout():
    """Process user logout"""

    #This clears the session of the user, which has the base 64 encoding

    if "logged_in_user_id" in session:
        del session["logged_in_user_id"]
    
        #I noticed that there was still a cookie (not able to encode) left
        #This line completely clears cookies 
        session.clear()

    return redirect("/")

#############################################################################

@app.route("/restaurant-search", methods = ["POST"])
def find_restaurant_via_yelp():
    """Search for restaurant from Yelp and return business_ID. Query the Yelp Business API by a business ID."""
    #Similar to the submit-order.js from AJAX review

    #These are the keys in the JSON dict, passed via AJAX request
    term = request.json.get("rname")
    location = request.json.get("city")

    #A search will return 1 restaurant
    limit = 1

    url_params = {
        'term': term,
        'location': location,
        'limit': limit
    }

    search_request = requests.get(SEARCH_URL, headers=HEADER, params=url_params).json()
    business_id = search_request['businesses'][0]['id']
    
    business_details = requests.get(BUSINESS_URL+business_id, headers=HEADER).json()
    reviews = requests.get(BUSINESS_URL+business_id+REVIEWS, headers=HEADER).json()

    #This is the combined dictionary of both business_details and reviews dictionaries
    business_details.update(reviews)
    
    #reviews_only = reviews['reviews'][0]['rating']
    #print(business_details)
    #return redirect(f"/restaurant/{bus_id}")
    return business_details

#############################################################################

@app.route("/user-favorites")
def user_favorites():
    """Show user's My favorites page"""

    user = crud.get_user_by_user_id(session["logged_in_user_id"])
    favorites = crud.get_favorites_by_user_id(session["logged_in_user_id"])

    return render_template("user_favorites.html", user=user, favorites=favorites)

#############################################################################    

@app.route("/add-favorites", methods=['POST'])
def create_favorite():
    """Create a favorite resaurant by the user."""

    #GET Yelp Fusion API's id for restaurant.
    #This value is passed from the hidden value of "Bookmark this restaurant" form
    
    #Before AJAX
    #revealed_yelp_rest_id = request.args.get('hidden-rest-id')
    #rname = request.args.get('hidden-rest-name')

    #After AJAX
    revealed_yelp_rest_id = request.json.get("revealed_yelp_rest_id")
    rname = request.json.get("rname")

    
    if "logged_in_user_id" in session: 
        user = crud.get_user_by_user_id(session["logged_in_user_id"])

        #Add searched restaurant to the database if doesn't exist
        restaurant = crud.get_restaurant_by_yelp_id(revealed_yelp_rest_id)
        if restaurant == None:
            restaurant = crud.create_restaurant(rname, revealed_yelp_rest_id)
            db.session.add(restaurant)
            db.session.commit()

        #Finally, bookmark the searched restaurant!
        favorite = crud.get_favorite_by_user_and_rest_id(user.user_id, restaurant.restaurant_id)
        if favorite == None:
            favorite = crud.create_favorite(user, restaurant, comment="")
            db.session.add(favorite)
            db.session.commit()
            #flash(f"You just favorited {restaurant.rname}!")
            return "True"
        
        else:
            #flash(f"You already favorited {restaurant.rname}!")
            return "already-favorited"
    

    else:
        return "False"

        #Before AJAX
        #flash("You must be logged in to bookmark this restaurant!")
        #return redirect("/")

    #Before AJAX
    #return render_template("homepage.html", user=user, restaurant=restaurant, favorite=favorite)

#############################################################################

@app.route("/delete-favorite", methods=['POST'])
def delete_favorite():
    """Delete a favorite restaurant by the user."""


    user_id = session["logged_in_user_id"]
    restaurant_id = request.json.get("userFavToDelete")
    rnameToDelete = request.json.get("rnameToDelete")
    
    fave_to_delete = crud.get_favorite_by_user_and_rest_id(user_id, restaurant_id)

    if fave_to_delete:
        db.session.delete(fave_to_delete)
        db.session.commit()

        return {"success": True,
                "restaurant_id": restaurant_id,
                "rname": rnameToDelete,
                "msg": f"Successfully deleted {rnameToDelete} from your bookmarks!"}
    else:
        return {"success": False,
                "restaurant_id": restaurant_id,
                "rname": rnameToDelete,
                "msg": f"An error occurred while deleting {rnameToDelete}. Please try again."}

#############################################################################

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)