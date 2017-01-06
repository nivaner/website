# encoding=utf-8
from flask import Flask, redirect, url_for, g, render_template
from forms import SearchForm

import os, sys, string
import MySQLdb



# 连接数据库　
try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='citys')
except Exception, e:
    print e
    sys.exit()





#     插入数据

# sql = "insert into test1(name, age) values (%s, %s)"
# val = (("李四", 24), ("王五", 25), ("洪六", 26))
# try:
#     cursor.executemany(sql, val)
# except Exception, e:
#     print e

# 获取cursor对象来进行操作
cursor = conn.cursor()
#
#查询出数据
sql = "select * from citys WHERE city_name = '南京市'"
cursor.execute(sql)
alldata = cursor.fetchall()
# 如果有数据返回，就循环输出, alldata是有个二维的列表
if alldata:
    for rec in alldata:
        print rec[0], rec[1]


cursor.close()
conn.close()

app = Flask(__name__)
app.config.from_object('config')


@app.before_request
def before_request():
    g.search_form = SearchForm()


@app.route('/')
def home():
    return render_template("home.html", title="search")


@app.route('/search', methods=['POST'])
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('sorry'))
    query = g.search_form.search.data
    return redirect(url_for('search_results', query=query))


@app.route('/sorry')
def sorry():
    return render_template("sorry.html", title="so sad")


@app.route('/search-results/<query>', methods=['GET', 'POST'])
def search_results(query):

    # 查询出数据
    sql = "select * from citys WHERE city_name = u'{}'".format(query)
    cursor.execute(sql)
    alldata = cursor.fetchall()
    # 如果有数据返回，就循环输出, alldata是有个二维的列表
    if alldata:
        for rec in alldata:
            print rec[0], rec[1]

    results = alldata
    # results = City.query.filter(City.city_name.like(u'%{}%'.format(query))).all()
    return render_template('search_results.html',
                           query=query,
                           results=results)


if __name__ == '__main__':
    app.run(debug='True', port=2222)
    cursor.close()
    conn.close()
