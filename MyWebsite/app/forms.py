#!/user/bin/env python
# coding: utf-8
#
from wtforms.validators import DataRequired
from wtforms.fields import  StringField
from flask_security.forms import RegisterForm

class ExtendedRegisterForm(RegisterForm):
    nickname = StringField(u'用户名', validators=[DataRequired()])
