# views are controller (which has to route) in flask in MVC Pattern

# app is an instance of the Flask from __init.py file which is our main object
# for database operation using SQLAlchemy & uploading images
from fintech_app import app

@app.route('/')
@app.route('/home')
def home():
    return "Hello World!"