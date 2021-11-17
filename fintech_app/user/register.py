# app is an instance of the Flask from __init.py file which is our main object & mail from flask mail
from flask import render_template, session, redirect, url_for, flash

from fintech_app import db

# for using(access) user in database and writing review in profile pa
from user.models import User

# for filling up the form & validating in html file, use login form for logging in
from user.form import RegisterForm_user_temp, RegisterForm_user

# for communications to user
from user.sms_email import send_OTP_email

# bcrypt password hashing and key derivation
import bcrypt


def user_register():
    # session.clear() 
    form = RegisterForm_user_temp()
    error = None
    if session.get('email'):
        return redirect(url_for('home'))
    else:
        if form.validate_on_submit():
            #Check for unique email first & if not pass 'error' to html page
            if form.email.data:
                    session['email'] = form.email.data
                    session['password'] = form.password.data
                    # send OTP sms via api here
                    send_OTP_email( session['email'])
                    return redirect(url_for('register_full'))
            else:
                error = 'please enter valid email'
            # user = User.query.filter_by(email=form.email.data).first()
            # if user:
            #     error = 'This email is already registered.'
            # else:
        return render_template('user/register.html', form=form, error=error, action='temp')



def user_register_full():
    # creating instance of RegisterForm_user form user.form which has all of Form feature too(subclass)
    form = RegisterForm_user()
    # first time we run this no error but variable 'error' is defined here
    error = None
    # for saving indian mobile numbers filhaal later gonna expand to the world
    # isd_code = Isd_code.query.filter_by(countries_name='india').first()
    
    if session.get('mobile_register'):
        user = User.query.filter_by(mobile=session['mobile_register']).first()
    if session.get('mobile'):
        return redirect(url_for('home'))

    elif session.get('email') and session.get('password'):
        form.email.data = session['email']
        
        if form.validate_on_submit():
            # some deep rooted issue with session that's why str is used it shows something else in FLASH but saves different value in db
            if form.otp_verify.data.isdigit() == True and form.otp_verify.data == str(session['OTP']):
                # 'salt' is a random string that is used to crypt
                salt = bcrypt.gensalt()
                # 'hashed_password' for the first time, with a randomly-generated salt
                # it makes the password input by user a crypted string as 'hashed_password'
                hashed_password =  bcrypt.hashpw(session['password'], salt)
                user = User(
                    # data is a method to fetch from POST method from HTTP the content
                    form.email.data,
                    hashed_password,
                    fullname=None,
                    mobile=None,
                    is_validity_active=False,
                    is_daddy=False
                    )
                # insert entries into the database using add(user) using SQLAlchemy
                db.session.add(user)
                # flush will mimic the entry in database to give back 'id' just to check further
                db.session.flush()
                # now let's check if User id is there.
                if user.id:
                     # transaction or multiple insertion in databases using commit() using SQLAlchemy
                    db.session.commit()
                    message = "Hi! %s,\nWelcome to ShutupNwait.com\nYou have been registered." %user.email
                    # send_sms(user.mobile_ind, message)
                    session.clear()
                    flash('Registered succefully, please log-in')
                    return redirect(url_for('login'))
                else:
                    # If any gadbad then just rollback like nothing happened & let's pass an error back
                    db.session.rollback()
                    error = "Oops! something went wrong."
            else:
                error = "invalid OTP, try again."
        return render_template('user/register.html', form=form, error=error, action='register-full')
    else:
        return redirect(url_for('register'))


def user_resend_OTP():
    if session.get('email'):
        # send OTP sms via api here
        send_OTP_email( session['email'])
        return redirect(url_for('register_full'))
        
    else:
        abort(404)