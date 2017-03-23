#!/user/bin/env python
# coding: utf-8

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import  StringField, TextAreaField, SubmitField
from flask_security.forms import RegisterForm

class ExtendedRegisterForm(RegisterForm):
    nickname = StringField(u'用户名', validators=[DataRequired()])

class PostForm(FlaskForm):
    body = TextAreaField("你的想法是什么", validators=[DataRequired()])
    submit = SubmitField(u'提交')