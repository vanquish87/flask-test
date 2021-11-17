# app is an instance of the Flask from __init.py file which is our main object & mail from flask mail
from flask import render_template, session, redirect, url_for, flash

from fintech_app import db

# for using(access) user in database and writing review in profile pa
from user.models import User

# for filling up the form & validating in html file, use login form for logging in
from user.form import RegisterForm_user_temp

# for communications to user
from user.sms_email import send_OTP_email

# bcrypt password hashing and key derivation
# import bcrypt


def user_register():
    form = RegisterForm_user_temp()
    error = None
    if session.get('email'):
        return redirect(url_for('home'))
    else:
        if form.validate_on_submit():
            #Check for unique email first & if not pass 'error' to html page
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                error = 'This email is already registered.'
            else:
                if form.email.data:
                    session['email'] = form.email.data
                    session['password'] = form.password.data
                    # send OTP sms via api here
                    send_OTP_email( session['email'])
                    return redirect(url_for('register_full'))
                else:
                    error = 'please enter valid email'
            
        return render_template('user/register.html', form=form, error=error, action='temp')
