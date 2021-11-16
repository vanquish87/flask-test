# Let’s create a basic function for sending emails with a little help from Flask-Mail
# which is already installed and setup in project/__init__.py.
# from flask.ext.mail import Message

from flask import session, flash
from meditate import app, mail

import random, datetime

# send OTP sms via api here
def send_OTP_email(email):
    OTP = random.randint(100000,999999)
    session['OTP'] = OTP
    time_expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=40)
    subject = 'OTP for registration at ShutupNwait.com'
    template = 'Use OTP %d on ShutupNwait & it expires at %s' %(OTP, str(time_expiration.strftime('%I:%M%p')))

    # calling another function to use external api for sending server based SMSs
    send_email(email, subject, template)
    flash('An OTP has been sent to your email', 'success')



# simple http api to send sms
# set bulk sms in advance so that we can choose from GET with list or without list (of 91 codes)
def send_sms(mobile, message, bulk=False):
    SENDER_ID = 'VALGUY'
    AUTHKEY = '171496AYGOQos4H599eace8'
    COUNTRY_CODE = '91'
    
    if app.config["SEND_SMS"] == True:
        if bulk == False:
            # this code needs mobile no. prefixed with 91 india code
            requests.get('http://my.msgwow.com/api/sendhttp.php?authkey='+AUTHKEY+'&mobiles=91'+mobile+'&message='+message+'&sender='+SENDER_ID+'&route=4&country='+COUNTRY_CODE+'')
        else:
            # without 91 code which will will added by in list beforehand        
            requests.get('http://my.msgwow.com/api/sendhttp.php?authkey='+AUTHKEY+'&mobiles='+mobile+'&message='+message+'&sender='+SENDER_ID+'&route=4&country='+COUNTRY_CODE+'')
    else:
        flash(mobile)
        flash(message)



# we simply need to pass a list of recipients, a subject, and a template.
def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )

    if app.config['SEND_EMAIL'] == True:
        mail.send(msg)
    
    else:
        flash(subject)
        flash(template)
 