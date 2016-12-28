# encoding=utf-8
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import MigrateCommand,Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
manage = Manager(app)
bootstrap = Bootstrap(app)

migrate = Migrate(app,db)
manage.add_command('db', MigrateCommand)


from app import views
