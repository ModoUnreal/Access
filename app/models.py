"""

(c) 2019 - ModoUnreal

app/models.py

"""


from app import db


class User(db.Model):

    # The db columns will be defined here.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    forename = db.Column(db.String(128))
    surname = db.Column(db.String(128))
    email = db.Column(db.String(128))

    # This might get changed to a list of services that can be modified
    # rather than just a string value, as I feel like this isn't as
    # configurable.
    service = db.Column(db.String(128))
    preferences = db.Column(db.String(128)) # As before make it a list


class Post: # Post = parent
    pass

class Listing(Post): # This is child of post
    pass

class Categories: # Main one made by devs
    pass

class Subcat: # Other one made by users.
    pass
