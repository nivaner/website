import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'super-secret-you-will-never-hack'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'daka.db')
SQLALCHEMY_COMMIT_ON_TEARDOWN= True