# encoding=utf-8

from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

class User(UserMixin,db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    punch = db.relationship('Punch', backref='users')

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
#
#     def is_authenticated(self):
#         return True
#
#     def is_active(self):
#         return True
#
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return unicode(self.id)  # python 2
#
#     def __repr__(self):
#         return '<User %r>' % (self.nickname)


class Punch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(255))
    year = db.Column(db.String(255))
    month = db.Column(db.String(255))
    day = db.Column(db.String(255))
    hour = db.Column(db.String(255))
    description = db.Column(db.String(255))
    worktime = db.Column(db.Float)
    name = db.Column(db.String(256), db.ForeignKey('user.nickname'))

    def __repr__(self):
        return '<Punch %r>' % self.name


#这个回调用于从会话中存储的用户 ID 重新加载用户对象。它应该接受一个用户的 unicode ID，并返回相应的用户对象。
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))