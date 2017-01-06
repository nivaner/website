# encoding=utf-8
from flask_security import forms as security_forms
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import TextField, StringField, DateTimeField, SubmitField, DateField,IntegerField,PasswordField


# 入库
class PeopleForm(FlaskForm):
    name = StringField(u'负责人',validators=[DataRequired()])
    submit = SubmitField(u'入库')

# 采购
class PurchaseForm(FlaskForm):
    purchasedate = DateTimeField(u'订购日期', validators=[DataRequired()])
    # purchase_name = StringField(u'采购人员名字', validators=[DataRequired()])
    purchase_partname = StringField(u'定购物品', validators=[DataRequired()])
    # purchase_code = StringField(u'货号',validators=[DataRequired()])
    # purchase_partunit = StringField(u'订购型号', validators=[DataRequired()])
    purchase_partnumber = IntegerField(u'物品数量',validators=[DataRequired()])
    submit = SubmitField(u'提交')


class ProduceForm(FlaskForm):
    name = StringField(u'产品',validators=[DataRequired()])
    num = IntegerField(u'数量', validators=[DataRequired()])
    date = DateTimeField(u'生产日期', validators=[DataRequired()])
    submit = SubmitField(u'生产')

class SaleForm(FlaskForm):
    id = IntegerField(u'货号', validators=[DataRequired()])
    num = IntegerField(u'数量',validators=[DataRequired()])
    submit = SubmitField(u'出售')

class LoginForm(FlaskForm):
    name = StringField(u'名字',validators=[DataRequired()])
    password = PasswordField(u'密码',validators=[DataRequired()])
    submit = SubmitField(u'提交')

class RegisterForm(FlaskForm):
    name = StringField(u'名字', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'提交')