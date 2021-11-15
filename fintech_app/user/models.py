# for inseting utc date & time
import datetime 

# models are database operations in flask in MVC Pattern & called models

# db is instance of SQLAlchemy from __init__.py file
from fintech_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    # isd_code_id = db.Column(db.Integer, db.ForeignKey('isd_code.id')) 
    mobile = db.Column(db.String(16))
    password = db.Column(db.String(60))

    # DateTime is a SQLAlchemy method to support python internal datetimer
    # registered_on, corfimed, confirmed_on_utc for email verification purposes 
    registered_on = db.Column(db.DateTime, nullable=False)
    # confirmed_email = db.Column(db.Boolean, nullable=False, default=False)

    # members validity is active or not
    is_validity_active = db.Column(db.Boolean, nullable=False, default=False)

    #if user is a admin(author) for blog to edit create wagarah wagarah
    is_daddy = db.Column(db.Boolean, nullable=False, default=False)

    # for user this one to many relationship
    # isd_code = db.relationship('Isd_code', backref='user')

    # for instance of user
    def __init__(self, email, password, fullname=None, mobile=None, is_validity_active=False, is_daddy=False):
        self.fullname = fullname
        self.email = email
        self.mobile = mobile
        self.password = password

        # prints time in UTC format and stores it
        self.registered_on = datetime.datetime.utcnow()
        self.is_validity_active = is_validity_active
        self.is_daddy = is_daddy

    # for fetching object from shell this will be seen
    def __repr__(self):
        return '<User is : %r>' % self.email