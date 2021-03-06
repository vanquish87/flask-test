# flask_wtf :Simple integration of Flask and WTForms, including CSRF, file upload and Recaptcha integration
from flask_wtf import Form

# When you have to work with form data submitted by a browser view code quickly becomes very hard to read.
# There are libraries out there designed to make this process easier to manage.
# WTForms which we will handle it. It will validates the data before it gets to database.
from wtforms import validators, StringField, PasswordField, TextAreaField, SelectField

# for validating a mobile no with otp, emailid
from wtforms.fields.html5 import EmailField, IntegerRangeField, TelField
# flask_wtf.html5 is deprecated. Import directly from wtforms.fields.html5. 

class RegisterForm_user_temp(Form):
    email = EmailField('Email', [
        validators.Required(),
        validators.Length(max=80, message="please enter Indian mobile")],
        description="Enter Email"
        )

    password = PasswordField('Password', [
        validators.Required(),
        validators.Length(min=8, max=60, message="password must contain at least 8 characters.")
        ])
    
# creating a subclass of Form so that it inherits all the stuff
class RegisterForm_user(Form):
    email = EmailField('Email', [
        validators.Required(),
        validators.Length(max=80, message="please enter Indian mobile")],
        description="Enter Email"
        )
        
    otp_verify = TelField('OTP', [
        validators.required(),
        validators.Length(min=6, message="invalid OTP, try again.")]
        )
    