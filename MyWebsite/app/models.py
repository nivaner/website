#coding: utf-8

from app import db
from flask_security import UserMixin, RoleMixin
from datetime import datetime
from markdown import markdown
# markdown转换的html需要bleach清理
import bleach

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
            backref=db.backref('users', lazy='dynamic'))
    posts = db.relationship('Post', db.ForeignKey('users.id'))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    summury = db.Column(db.Text)
    summury_html = db.Column(db.Text)

    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'blockquote', 'em', 'i',
                        'strong', 'li', 'ol', 'pre', 'strong', 'ul', 'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True)
        )

    @staticmethod
    def on_changed_summury(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'blockquote', 'em', 'i',
                        'strong', 'li', 'ol', 'pre', 'strong', 'ul', 'h1', 'h2', 'h3', 'p']
        target.summury_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True)
        )


db.event.listen(Post.body, 'set', Post.on_changed_body)
db.event.listen(Post.summury, 'set', Post.on_changed_summury)


class Category(db.Model):
    __tablename__ = "categorys"
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(64))
    count = db.Column(db.Integer)
    posts = db.relationship("Post", backref="category")


class Like(db.Model):
    __tablename__ = "Like"
    id = db.Column(db.Integer, primary_key=True)
    like_count = db.Column(db.Integer)
