#!/user/bin/env python
# coding: utf-8

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import  StringField, TextAreaField, SubmitField
from flask_security.forms import RegisterForm
from flask_pagedown.fields import  PageDownField

class ExtendedRegisterForm(RegisterForm):
    nickname = StringField(u'用户名', validators=[DataRequired()])

class PostForm(FlaskForm):
    title = StringField(u'标题', validators=[DataRequired()])
    body = PageDownField(u"给我留言（markdown）", validators=[DataRequired()])
    submit = SubmitField(u'提交')

class EditForm(FlaskForm):
    title = StringField(u'标题', validators=[DataRequired()])
    category = StringField(u'标签', validators=[DataRequired()])
    body = PageDownField(u"编辑博客内容", validators=[DataRequired()])
    submit = SubmitField(u'提交')
