"""Server for Foodie Guide"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, session, redirect
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


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("homepage.html")

#############################################################################

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("This e-mail is already registered with another account. Try again.")
    else:
        user = crud.create_user(fname, lname, email, password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {user.fname}! Please log in.")

    return redirect("/")

#############################################################################

@app.route("/login", methods=['POST'])
def process_login():
    """Process user login"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["logged_in_user_email"] = user.email
        flash(f"Welcome back, {user.fname}!")

    return redirect("/")

#############################################################################

@app.route("/logout")
def process_logout():
    """Process user logout"""

    del session["logged_in_user_email"]
    flash("Logged out.")
    return redirect("/")

#############################################################################

@app.route("/user_favorites/<user_id>")
def user_profile(user_id):
    """View the user's My Favorites page."""

    logged_in_email = session.get("logged_in_user_email")
    
    if logged_in_email is None:
        flash("You must log in to enter My Favorites.")
    else:
        user = crud.get_user_by_id(user_id)

    return render_template("user_favorites.html", user=user)

#############################################################################

@app.route("/restaurant/search", methods=['POST'])
def find_restaurant_via_yelp():
    """Search for restaurants from Yelp."""

    rname = request.form.get("rname")
    pass


#############################################################################

@app.route("/restaurant/google_detail")
def find_restaurant_detail_via_google():
    """Return restaurant details from Google."""

    pass



#############################################################################

@app.route("/restaurant/yelp_detail")
def find_restaurant_detail_via_yelp():
    """Return restaurant details from Yelp."""

    pass

#############################################################################

@app.route("/profile/<user_id>/favorites")
def create_favorite():
    """Create a favorite resaurant by the user."""

    logged_in_email = session.get("user_email")
   
    user = crud.get_user_by_email(logged_in_email)
    restaurant = crud.get_restaurant_by_id(restaurant_id)
    
    favorite = crud.create_favorite(user, restaurant, comment)
    db.session.add(favorite)
    db.session.commit()

    flash(f"You just favorited {Restaurant.rname}.")

    return render_template("user_profile.html", restaurant=restaurant)

#############################################################################

@app.route("/profile/<user_id>/favorites/all")
def all_favorited_restuarants(user_id):
    """Return all favorited restaurants by the user."""
    
    all_favorites = crud.get_favorite_by_user_id(user_id)
    
    return render_template("user_profile.html", )




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)