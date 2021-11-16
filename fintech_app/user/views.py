# views are controller (which has to route) in flask in MVC Pattern
# app is an instance of the Flask from __init.py file which is our main object & mail from flask mail
from fintech_app import app

from user.register import user_register

@app.route('/login')
def login():
    return 'hello user'


# route to register user with email temporarily
@app.route('/register', methods=('GET', 'POST'))
def register():
    return user_register()