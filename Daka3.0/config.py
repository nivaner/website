#coding: utf-8

import os
SECRET_KEY = os.urandom(24)

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'daka.db')