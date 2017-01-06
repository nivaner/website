#encoding=utf-8
from flask import Flask,redirect, url_for, g, render_template
from forms import SearchForm
from flask_script import Manager
from flask_admin import Admin
from sqlalchemy import and_

# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from flask.ext.sqlalchemy import SQLAlchemy

import sys




# Base.metadata.drop_all()
# Base.metadata.create_all()

# session = DBSession()
#
# a = citys(city_name=u'北京市', postcode='100001')
# b = citys(city_name=u'东城区', postcode='100010')
#
# session.add(a)
# session.add(b)
#
# session.commit()

# print get_result(rs):
#     print '-' * 20
#     for citys in rs:
#         print citys.city_name

import os
from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object('config')
manage = Manager(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

admin = Admin(app, name=u"邮编查询", template_mode='bootstrap3')


import flask.ext.whooshalchemy as whooshalchemy
# MAX_SEARCH_RESULTS =50
class City(db.Model):
    __tablename__ = 'citys'
    # __searchable__ = ['city_name']

    city_name = db.Column(db.String(50))
    postcode = db.Column(db.String(20), primary_key=True)

    def __repr__(self):
        return '<City %r>' % self.city_name


from flask_admin.contrib.sqla import ModelView
class CityAdmin(ModelView):
    column_display_pk = True
    column_labels = {
        'city_name':u'城市',
        'postcode': u'邮编'
    }
    form_columns = ['city_name','postcode']
    column_searchable_list = ['city_name','postcode']

admin.add_view(CityAdmin(City, db.session, name=u"城市邮编查询"))


# whooshalchemy.whoosh_index(app, City)
# if sys.version_info >= (3, 0):
#     enable_search = False
#
# else:
#     enable_search = True
#     import flask.ext.whooshalchemy as whooshalchemy

# Base = declarative_base(app)
#
# class citys(Base):
#     __tablename__ = 'citys'
#     __searchable__ = ['city_name']
#
#     city_name = Column(String(50))
#     postcode = Column(String(20), primary_key=True)
#
#     if enable_search:
#         whooshalchemy.whoosh_index(app,city_name)

# engine = create_engine('mysql+pymysql://root:''@loaclhost:3306/citys')
# DBSession = sessionmaker(bind=engine)













@app.before_request
def before_request():
    g.search_form = SearchForm()

@app.route('/')
def home():
    return render_template("home.html",title="search")


@app.route('/search', methods=['POST'])
def search():
    # form = SearchForm
    if not g.search_form.validate_on_submit():
        return redirect(url_for('sorry'))
    query = g.search_form.search.data
    # query = City.query.filter(City.city_name.like(u'%query%')).all()
    return redirect(url_for('search_results', query=query))


@app.route('/sorry')
def sorry():
    return render_template("sorry.html",title="so sad")

#
@app.route('/search-results/<query>', methods=['GET', 'POST'])
def search_results(query):
    # results = City.query.filter_by(city_name=query).all()
    # w = [u'%query%']
    # print query
    results = City.query.filter(City.city_name.like(u'%{}%'.format(query))).all()
    # for i in results:
        # print i
    # words = '%query%'
    # rule = and_(*[City.city_name.like(w) for w in words])
    # results = City.query.filter(rule)
    # results = City.query.all()
    # results = City.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
    return render_template('search_results.html',
            query = query,
            results = results)



if __name__ == '__main__':
    # manage.run()
    app.run(debug='True',port=2222)