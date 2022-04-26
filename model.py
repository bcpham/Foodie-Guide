"""Models for Foodie Guide."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#############################################################################

class User(db.Model):
    """A User."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(50))

    def __repr__(self):
        return f"<User user_id={self.user_id} fname={self.fname} lname={self.lname} email={self.email}>"

#############################################################################

class Favorite(db.Model):
    """A user's favorite restaurant."""

    __tablename__ = "favorites"

    fave_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.restaurant_id"))
    comment = db.Column(db.Text)

    user = db.relationship("User", backref="favorites")
    restaurant = db.relationship("Restaurant", backref="favorites")

def __repr__(self):
        return f"<Favorite fave_id={self.fave_id} comment={self.comment}>"

#############################################################################

class Restaurant(db.Model):
    """A restaurant."""

    __tablename__ = "restaurants"

    restaurant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rname = db.Column(db.String(50))
    yelp_id = db.Column(db.String)
    place_id = db.Column(db.String)

def __repr__(self):
        return f"<Restaurant restaurant_id={self.restaurant_id}>"

#############################################################################

def connect_to_db(flask_app, db_uri="postgresql:///food", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    
    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    
    connect_to_db(app)