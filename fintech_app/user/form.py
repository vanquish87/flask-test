
# When you have to work with form data submitted by a browser view code quickly becomes very hard to read.
# There are libraries out there designed to make this process easier to manage.
# WTForms which we will handle it. It will validates the data before it gets to database.
from wtforms import validators, StringField, PasswordField, TextAreaField, SelectField

# for validating a mobile no with otp, emailid
from wtforms.fields.html5 import EmailField, IntegerRangeField, TelField


