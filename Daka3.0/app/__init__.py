# encoding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_admin import Admin,AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.base import MenuLink

app = Flask(__name__)
app.config.from_object('config')

manage = Manager(app)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = '/home'

admin = Admin(app,
              name=u"打卡",
              template_mode='bootstrap3',
              index_view=AdminIndexView(
                  name=u"主页"
              )
              )


from app import views
from models import User, Punch

class UserAdmin(ModelView):
    column_display_pk = True
    column_labels = {
        'nickname': u'用户名',
        'password_hash': u'密码',
    }
    form_columns = [
        'nickname',]
    column_searchable_list = ['nickname']
    # b = 0
    #
    # def is_accessible(self):
    #     if current_user.roles[0] == 'Admin':
    #         b = 1
    #     return b



class PunchAdmin(ModelView):
    column_display_pk = True
    # 中文化
    column_labels = {
        'name': u'姓名',
        'time': u'日期',
        'worktime': u'工作时长',
        'description': u'描述',

    }
    # 可修改的对象
    form_columns = [
        'name', 'time', 'year', 'month', 'day', 'hour', 'description', 'worktime',
    ]
    column_searchable_list = ['name', 'month']

    # b = 0
    #
    # def is_accessible(self):
    #     if current_user.roles[0] == 'Admin':
    #         b = 1
    #     return b


admin.add_view(UserAdmin(User, db.session, name=u"用户"))
admin.add_view(PunchAdmin(Punch, db.session, name=u"时间"))
admin.add_link(MenuLink(name=u"返回主页", url='/'))
