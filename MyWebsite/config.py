#encoding=utf-8
import os

WTF_CSRF_ENABLED = True
SECRET_KEY = 'super-secret-you-will-never-hack'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'aipatent_main.db')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# flask_security
SECURITY_MAIL_SENDER = "aipatent2016@gmail.com"
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'AIPatent2016'

# email server
MAIL_SERVER = 'smtp.mxhichina.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'no-reply@aipatent.com'
MAIL_PASSWORD = 'AIpatent4YOU'
SECURITY_EMAIL_SENDER = u'AIpatent 智能专利检索平台 <no-reply@aipatent.com>'