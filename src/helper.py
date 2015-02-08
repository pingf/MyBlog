from src import app

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.login import LoginManager
from flask_wtf.csrf import CsrfProtect

manager = Manager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


login_manager = LoginManager(app)
protector = CsrfProtect(app)

@protector.error_handler
def csrf_error(reason):
    print(reason)
    return 'csrf error'
