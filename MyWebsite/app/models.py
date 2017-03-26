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
    # posts = db.relationship('Post', db.ForeignKey('users.id'))



class Post(db.Model):
    __name__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.Text)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    # author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_tag = db.Column(db.String(64), db.ForeignKey('categorys.tag'))

    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py

        seed()
        for i in range(count):
            p = Post(body=forgery_py.lorem_ipsum.sentences(randint(1, 3)),
                     timestamp=forgery_py.date.date(True))
            db.session.add(p)
            db.session.commit()

    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = [
            'a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
            'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
            'h1', 'h2', 'h3', 'p', 'img','center'
        ]
        # 需要提取的标签属性，否则会被忽略掉
        attrs = {
            '*': ['class','center','&nbsp;'],
            'a': ['href', 'rel'],
            'img': ['src', 'alt']
        }
        target.body_html = bleach.linkify(
            bleach.clean(
                markdown(value, output_format='html'),
                tags=allowed_tags,
                attributes=attrs,
                strip=True
            )
        )

db.event.listen(Post.body, 'set', Post.on_changed_body)


class Category(db.Model):
    __tablename__ = "categorys"
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(64))
    posts = db.relationship("Post", backref="category")


# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#     posts = db.relationship('Post', secondary=roles_users,
#                             backref=db.backref('tags', lazy='dynamic'))
#
# # 多对多关系
# posts_tags = db.Table('posts_tags',
#                        db.Column('post_id', db.Integer(), db.ForeignKey('posts.id')),
#                        db.Column('tag_id', db.Integer(), db.ForeignKey('tags.id')))



