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

def example_data():
    """Create sample data."""

    # In case this is run more than once, empty out existing data
    User.query.delete()
    Favorite.query.delete()
    Restaurant.query.delete()

    # Add sample users, restaurants, and favorites
    u1 = User(fname="Matthew", lname="D", email="test01@test.com", password="test")
    u2 = User(fname="BC", lname="Pham", email="test02@test.com", password="test")

    r1 = Restaurant(rname="The Restaurant 1", yelp_id="123", place_id="")
    r2 = Restaurant(rname="The Restaurant 2", yelp_id="456", place_id="")

    f1 = Favorite(user_id="1", restaurant_id="1", comment="")
    f2 = Favorite(user_id="2", restaurant_id="2", comment="")

    db.session.add_all([u1,u2,r1,r2,f1,f2])
    db.session.commit()

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
    
    connect_to_db(app, echo=False)