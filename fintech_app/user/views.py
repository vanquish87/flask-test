# views are controller (which has to route) in flask in MVC Pattern
# app is an instance of the Flask from __init.py file which is our main object & mail from flask mail
from fintech_app import app

@app.route('/login')
def login():
    return 'hello user'