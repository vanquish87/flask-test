# views are controller (which has to route) in flask in MVC Pattern
# app is an instance of the Flask from __init.py file which is our main object & mail from flask mail
from fintech_app import app

from user.login import user_logout

from user.register import user_register, user_register_full, user_resend_OTP

@app.route('/login')
def login():
    return 'hello user'

@app.route('/logout')
def logout():
    return user_logout()


# route to register user with email temporarily
@app.route('/register', methods=('GET', 'POST'))
def register():
    return user_register()

@app.route('/register-full', methods=('GET', 'POST'))
def register_full():
    return user_register_full()

@app.route('/resendOTP', methods=('GET', 'POST'))
def resend_OTP():
    return user_resend_OTP()