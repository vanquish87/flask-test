from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy 

# to use Migrate library to update databases & tables
# from flask.ext.migrate import Migrate

# The Flask-Mail extension provides a simple interface to set up SMTP with 
# your Flask application and to send messages from your views and scripts.
from flask.ext.mail import Mail

# creating a instance of Flask as app
app = Flask(__name__)

# external settings.py file so that we can make changes while in devlopment or live servers
# this config is from Flask and from_object is a module for doing it
app.config.from_object('settings')


# # create a object of SQLAlchemy with passing app as argument through it
db = SQLAlchemy(app)

# # migrations
# migrate = Migrate(app, db)

# # for setting up mail
mail = Mail()
mail.init_app(app)


# views are controller (which has to route) in flask in MVC Pattern
from website import views
from user import views

# # for saving n updating isd_codes into database
# if app.config["MIGRATION"] == True:
#     from meditate import isd_codes