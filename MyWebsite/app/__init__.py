# --*-- coding: utf-8 --*--

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_bootstrap import Bootstrap
from forms import ExtendedRegisterForm
from flask_babelex import Babel
# pagedown使用js实现客户端Markdown到html的转换
from flask_pagedown import PageDown

app = Flask(__name__)
app.config.from_object('config')

manage = Manager(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app,db)
manage.add_command('db', MigrateCommand)
babel = Babel(app)
pagedown = PageDown(app)

from app import views
from models import User, Role, roles_users

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form = ExtendedRegisterForm)