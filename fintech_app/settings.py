import os

# secret keys are used to encode sessions in Flask
# secret_key can be changed anytime database stored password are retrieved without problem
SECRET_KEY = "nCwF0aIg8r5AT4sJuxaVBnx7DmGHzhqWBWIPLUWWKIcXxg5tLAfJZWu5"

# DEBUG used in Development environment
DEBUG = True

# --------------------------
# SQLAlchemy URI value to start doing things with databsase
DB_USERNAME = 'root'
DB_PASSWORD = ''
WEBSITE_DATABASE_NAME = 'website'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, WEBSITE_DATABASE_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
# To supress warning on runserver --just to take kum space on shell
SQLALCHEMY_TRACK_MODIFICATIONS = True
# ----------------------------

# for sending sms via API http://10seconds.in/pricing/ contact Rahul +91 9899338847
SEND_SMS = False

# for sending email via SMTP servers
SEND_EMAIL = False

# if db created by migrations for 1st time
MIGRATION = True

# ------------- Gateway stuff----------------
INSTAMOJO_TEST = True
if INSTAMOJO_TEST == True:
    # test instamojo stuff
    API_KEY = "test_e81a4e65fb7d640d5967081041f"
    AUTH_TOKEN = "test_110e6fd8897fe1d6f4208a7c09c"
    PRIV_SALT = "a2b3aabe19b94563a15dc6109c22493f"
else:
    #instamojo stuff LIVE
    API_KEY = "931abee575d7e62453f2a2cd1a0227c0"
    AUTH_TOKEN = "aa0fd13351a622ba1e3c2acac4ec348b"
    PRIV_SALT = "b7bbacc776c4876ec7d5de1f7118ce3b"
# -------------------------------------------

# mail settings
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_SERVER = 'smtp.zoho.com'
MAIL_PORT = 587

# zoho authentication
MAIL_USERNAME = 'valueguyz-admin@valueguyz.com'
MAIL_PASSWORD = 'code4ruby@feb14'

# mail accounts
MAIL_DEFAULT_SENDER = 'valueguyz-admin@valueguyz.com'