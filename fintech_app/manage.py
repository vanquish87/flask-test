import os, sys

# tells python the starting point of this project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# The Flask-Script extension provides support for writing external scripts in Flask.
# This includes running a development server, a customised Python shell, scripts to set up your database,
# cronjobs, and other command-line tasks that belong outside the web application itself.
from flask.ext.script import Manager, Server 

# from __init__ file of meditate
from fintech_app import app


# to use Migrate library to update databases & tables
# from flask.ext.migrate import MigrateCommand

# for login purposes intializing login manager
# from flask.ext.login import LoginManager,login_user

# flask login uses it's own AnonymousUserMixin class. The following snippet shows how to override it
# with flask security's AnonymousUser class
# from flask.ext.security import AnonymousUser

manager = Manager(app)

# migration called from shell for 'migrate' or 'upgrade' or any other command like 'init'
# manager.add_command('db', MigrateCommand)


# The Server command runs the Flask development server
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT', 5000))
    ))

if __name__ == "__main__" :
    manager.run()