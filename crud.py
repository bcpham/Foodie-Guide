"""CRUD operations."""

from model import db, User, Favorite, Restaurant, connect_to_db

#############################################################################
#Handler functions for creating NEW user, restaurant, and favorite objects:
#############################################################################

def create_user(fname, lname, email, password):
    """Create and return a new user."""

    user = User(fname=fname, lname=lname, email=email, password=password)
    return user

def create_restaurant(rname, yelp_id, google_id=""):
    """Create and return a new restaurant (to save)"""
    
    restaurant = Restaurant(rname=rname, yelp_id=yelp_id, place_id=google_id)
    return restaurant

def create_favorite(user, restaurant, comment):
    """Create and return a favorited restaurant"""

    favorite = Favorite(user=user, restaurant=restaurant, comment=comment)
    #favoriting a restaurant means to equate fave_id restaurant_id?

    return favorite

#############################################################################
#Handler functions for queries:
#############################################################################


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_by_user_id(user_id):
    """Return a user by user_id."""

    return User.query.filter(User.user_id == user_id).first()

#The CRUD function below is the only one I'm not using,
#but it will be good to keep it for troubleshooting purposes
def get_restaurant_by_id(restaurant_id):
    """Return a restaurant by primary key."""

    return Restaurant.query.get(restaurant_id)    

def get_restaurant_by_yelp_id(yelp_restaurant_id):
    """Return a restaurant by yelp id."""

    return Restaurant.query.filter_by(yelp_id = yelp_restaurant_id).first()   

def get_favorites_by_user_id(user_id):
    """Return all favorited restaurants by user."""

    return Favorite.query.filter(User.user_id == user_id).all()

def get_favorite_by_user_and_rest_id(user_id, rest_id):
    """Return all favorited restaurants by user."""
    print("***********USER ID =")
    print(user_id)
    print("***********REST ID =")
    print(rest_id)
    return Favorite.query.filter(Favorite.restaurant_id == rest_id, Favorite.user_id == user_id).first()

def get_favorite_by_user_and_yelp_id(user_id, yelp_id):
    """Return all favorited restaurants by user."""

    return Favorite.query.filter(Favorite.restaurant.has(yelp_id=yelp_id), Favorite.user_id == user_id).one()
    
#############################################################################

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
