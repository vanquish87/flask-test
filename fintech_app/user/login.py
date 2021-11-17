# app is an instance of the Flask from __init.py file which is our main object & mail from flask mail
from flask import session, flash, redirect, url_for, abort


def user_logout():
    if session.get('email'):
        session.clear()
        flash('You have logged out. See you later Dost ')
        return redirect(url_for('register'))
    else:
        abort(404)