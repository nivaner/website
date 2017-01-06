# encoding=utf-8
from app import app
from flask import render_template,request,redirect,url_for,g
from forms import PurchaseForm,SaleForm,LoginForm,RegisterForm,PeopleForm,ProduceForm
import os, sys, string
import MySQLdb
from datetime import datetime

# conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
# # # 创建游标
# cursor = conn.cursor()
#
# # sql语句
# sql = "select name from gonghuoshang_tbl"
# # 执行sql语句
# cursor.execute(sql)
# # # 获取所有结果
# result = cursor.fetchall()
# # # 关闭游标
# cursor.close()
# # # 执行完毕的时候关掉文件句柄
# conn.close()
# #
# print result
# for re in result:
#     print re[0]
#
# 那就关掉它



# conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
# 创建游标
# cursor = conn.cursor()
#
# sql语句
# sql = "select * from gonghuoshang_tbl"
# sql = "insert into gonghuoshang_tbl(name) VALUES ('zhi')"
# # 执行sql语句
# c = cursor.execute(sql)
# # 获取所有结果
# result = c.fetchall()
# 提交事物
# conn.commit()
# 关闭游标
# cursor.close()
# conn.close()
# print c


# try:
#     conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='SqlHomework')
    # conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
# except Exception, e:
#     print e
#     sys.exit()
#
#
# conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
# cursor = conn.cursor()


# 仓库
@app.route('/library')
def library():

    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
    # # 创建数据库的链接
    cursor = conn.cursor()
    # # 创建数据库的游标
    sql = " select * from library"
    print sql
    # 执行sql语句
    cursor.execute(sql)
    # # 获取所有结果
    results = cursor.fetchall()
    # # 关闭游标
    cursor.close()
    # # 执行完毕的时候关掉文件句柄
    conn.close()
    for rs in results:
        print rs
    return render_template("library.html", results=results)

# 生产
@app.route('/produce', methods=['GET','POST'])
def produce():
    form = ProduceForm()
    if form.validate_on_submit():
        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
        # 创建游标
        cursor = conn.cursor()
        # sql语句
        sql = "insert into library(name,num) VALUES ('{0}','{1}')".format(form.name.data,form.num.data)
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有结果
        result = cursor.fetchall()
        # 提交事物
        conn.commit()
        # 关闭游标
        cursor.close()
        conn.close()
        print result
        return redirect(url_for('success'))

    return render_template("produce.html",form=form)

# 供货商管理
@app.route('/purchase')
@app.route('/purchase/gonghuoshang',methods=['GET','POST'])
def gonghuoshang():
    # 连接数据库
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
    # # 创建游标
    cursor = conn.cursor()
    # sql语句
    sql = "select * from gonghuoshang_tbl"
    # 执行sql语句
    cursor.execute(sql)
    # # 获取所有结果
    results = cursor.fetchall()
    # # 关闭游标
    cursor.close()
    # # 执行完毕的时候关掉文件句柄
    conn.close()

    return render_template("gonghuoshang.html", title='gonghuoshang', results=results)

# 入库
@app.route('/rukuform',methods=['GET','POST'])
def rukuform():
    # 获取当前时间
    # nowtime = datetime.now()
    form = PeopleForm()

    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
    # # 创建数据库的链接
    cursor = conn.cursor()
    # # 创建数据库的游标
    # sql = " select * from order_tbl WHERE order_date = '{0}'".format(nowtime.date())
    sql = " select * from order_tbl"
    print sql
    # 执行sql语句
    cursor.execute(sql)
    # # 获取所有结果
    results = cursor.fetchall()
    # # 关闭游标
    cursor.close()
    # # 执行完毕的时候关掉文件句柄
    conn.close()
    for rs in results:
        print rs

    if form.validate_on_submit():
        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
        # # 创建数据库的链接
        cursor = conn.cursor()
        # # 创建数据库的游标
        for rs in results:
            sql = " insert into library(name,num) values('{0}',{1})".format(rs[1],rs[3])
            print sql
            cursor.execute(sql)
            # 用游标操作数据库，sql数据库行为，函数的实参
            conn.commit()
        conn.close()

        return redirect(url_for('home'))

    return render_template("rukuform.html",results=results,form=form)

# 订单
@app.route('/purchase/gonghuoshang/order',methods=['GET','POST'])
def order():
    # 获取当前时间
    nowtime = datetime.now()

    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
    # # 创建数据库的链接
    cursor = conn.cursor()
    # # 创建数据库的游标
    # sql = " select * from order_tbl WHERE order_date = '{0}'".format(nowtime.date())
    sql = " select * from order_tbl "
    print sql
    # 执行sql语句
    cursor.execute(sql)
    # # 获取所有结果
    results = cursor.fetchall()
    # # 关闭游标
    cursor.close()
    # # 执行完毕的时候关掉文件句柄
    conn.close()
    for rs in results:
        print rs
    return render_template("order.html",results=results)

# 所有商品
@app.route('/purchase/gonghuoshang/allgoods/',methods=['GET','POST'])
def alldetail_gonghuoshang():
    # 网页请求装饰器后执行此函数此函数有一个形参
    print id
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
    # # 创建数据库的链接
    cursor = conn.cursor()
    # # 创建数据库的游标
    sql = " select * from goods_tbl g inner join gonghuoshang_tbl ghs on g.gonghuoshang_name = ghs.name "
    # 执行sql语句
    cursor.execute(sql)
    # # 获取所有结果
    results = cursor.fetchall()
    # # 关闭游标
    cursor.close()
    # # 执行完毕的时候关掉文件句柄
    conn.close()
    for rs in results:
        print rs
    return render_template("allgoods.html", results=results)

# 厂商对于商品
@app.route('/purchase/gonghuoshang/detail/<id>/',methods=['GET','POST'])
# 用flask装饰器把函数包裹起来，此函数接受一个参数。<id>是形参的名称
def detail_gonghuoshang(id):
    form = PurchaseForm()
    # 网页请求装饰器后执行此函数此函数有一个形参
    print id
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
    # # 创建数据库的链接
    cursor = conn.cursor()
    # # 创建数据库的游标
    sql = " select * from goods_tbl g inner join gonghuoshang_tbl ghs on g.gonghuoshang_name = ghs.name where ghs.name = '{0}'".format(id)
    # 执行sql语句
    print sql
    cursor.execute(sql)
    # # 获取所有结果
    results = cursor.fetchall()
    # # 关闭游标
    cursor.close()
    # # 执行完毕的时候关掉文件句柄
    conn.close()
    for rs in results:
        print rs
    if form.validate_on_submit():
        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
        # 创建数据库的链接
        cursor = conn.cursor()
        # 创建数据库的游标
        # sql = " insert into order_tbl(name,num,order_date) values('{1}',{2},'{3}')".format(form.purchase_partname.data,form.Purchase_partnumber.data, form.purchasedate.data)
        # sql = " insert into order_tbl(name,num) values('{1}',{2})".format(form.purchase_partname.data,form.Purchase_partnumber.data)
        # sql = "insert into order_tbl(name,num) values('filco',200)"
        sql = "insert into order_tbl(name,num) values('{0}',{1})".format(form.purchase_partname.data,form.purchase_partnumber.data)
        # 执行sql语句
        print sql
        cursor.execute(sql)
        # 用游标操作数据库，sql数据库行为，函数的实参
        conn.commit()
        # 数据库提交操作
        conn.close()
        return redirect(url_for('home'))

    return render_template("goods.html", results=results,form=form)

@app.route('/purchase/gonghuoshang/add/',methods=['GET','POST'])
# 用flask装饰器把函数包裹起来，此函数接受一个参数。<id>是形参的名称
def add_gonghuoshang():
    # pass
    key = request.args.get('key')
    print "ddddddds"
    print key
    if key == "":
        msg = u"不能为空"
        return render_template("gonghuoshang.html",msg=msg)
    else:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
        # 创建数据库的链接
        cursor = conn.cursor()
        # 创建数据库的游标
        sql = "insert into gonghuoshang_tbl(name) values('{0}')".format(key)
        cursor.execute(sql)
        # 用游标操作数据库，sql数据库行为，函数的实参
        conn.commit()
        # 数据库提交操作
        conn.close()
        # return redirect(url_for('gonghuoshang'))
    return render_template("gonghuoshang.html", title='gonghuoshang')


@app.route('/gonghuoshang/del/<id>/')
# 用flask装饰器把函数包裹起来，此函数接受一个参数。<id>是形参的名称
def delete_gonghuoshang(id):
    # 网页请求装饰器后执行此函数此函数有一个形参
    print id
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
    # 创建数据库的链接
    cursor = conn.cursor()
    # 创建数据库的游标
    sql = 'delete from gonghuoshang_tbl WHERE gonghuoshang_id = ' + "'{0}'".format(id)
    cursor.execute(sql)
    # 用游标操作数据库，sql数据库行为，函数的实参
    conn.commit()
    # 数据库提交操作
    conn.close()
    # 数据库关闭
    return redirect(url_for('gonghuoshang'))

#
@app.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html", title="Gunxiaocun")
#
#
# @app.route("/purchas", methods=["GET","POST"])
# def purchase():
#     form = PurchaseForm()
#     sql = "select name from gonghuoshang_tbl"
#     if form.validate_on_submit():
#
#         # print form.Purchase_partnumber.data
#         # sql = "insert into purchase(purchasedate,purchase_name, purchase_partname,purchase_code,purchase_partunit,Purchase_partnumber) values (%s, %s, %s,%s,%s,%s)"% (form.purchasedate.data, form.purchase_partname.data,form.purchase_code.data,form.purchase_partunit.data,form.Purchase_partnumber.data,)
#         # try:
#         #     cursor.executemany(sql)
#         # except Exception, e:
#         #     print e
#         return redirect(url_for('success'))
#
#     return render_template('produce.html')
#
@app.route('/sale',methods=['GET','POST'])
def sale():
    form = SaleForm()
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
    # # 创建数据库的链接
    cursor = conn.cursor()
    # # 创建数据库的游标
    sql = " select * from library"
    print sql
    # 执行sql语句
    cursor.execute(sql)
    # # 获取所有结果
    results = cursor.fetchall()
    # # 关闭游标
    cursor.close()
    # # 执行完毕的时候关掉文件句柄
    conn.close()
    for rs in results:
        print rs
    if form.validate_on_submit():
        conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='jinxiaocun')
        # # 创建数据库的链接
        cursor = conn.cursor()
        sql1 = "select num from library where id = {0} ".format(form.id.data)
        cursor.execute(sql1)
        results = cursor.fetchall()
        # 使用异常处理
        try:
            results[0][0]
        except:
            print u"chao chu fanwei "
            return redirect(url_for('unsuccess'))
        else:
            print results[0][0]
            # 创建数据库的游标
            num = results[0][0] - form.num.data
            if num < 0:
                return redirect(url_for('unsuccess'))
            elif num == 0:
                sql = "delete from library where id = {1}".format(num, form.id.data)
                cursor.execute(sql)
                # 用游标操作数据库，sql数据库行为，函数的实参
                conn.commit()
                conn.close()
                return redirect(url_for('success'))
            else:
                sql = "update library set num = {0} where id = {1}".format(num,form.id.data)
                cursor.execute(sql)
                # 用游标操作数据库，sql数据库行为，函数的实参
                conn.commit()
                conn.close()
                return redirect(url_for('success'))
    return render_template('sale.html',form=form,results=results)




#

@app.route('/success', methods=['GET','POST'])
def success():
    return render_template("success.html")


@app.route('/unsuccess', methods=['GET','POST'])
def unsuccess():
    return render_template("unsuccess.html")

#
#
# @app.route('/login',methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
        # print form.name.data
        # print type(form.name.data)
        #
        # sql = "select * from User"
        # b = cursor.execute(sql)
        # b = cursor.fetchall()
        # print b
        #
        # sql = "select password from User where name = "+ " '{}' ".format(form.name.data)
        # print sql
        # a = cursor.execute(sql)
        # row_1 = cursor.fetchone()
        # print a
        # print row_1[0]
        # if a==1:
        #     if row_1[0] == form.password.data:
        #         return redirect(url_for('success'))
    # return render_template('login.html',form=form)
#
#
# @app.route('/register', methods=['GET','POST'])
# def register():
#     form = RegisterForm()
    # if form.validate_on_submit():
    #     # sql = "insert into User VALUES ( " + " '{}' ".format(form.name.data) + ",'{}'".format(form.password.data)+")"
    #     # print sql
    #     sql1 = "insert into User(name,password) values( '{0}','{1}')".format(form.name.data,form.password.data);
    #     print sql1
    #     a = cursor.execute(sql1)
    #     # print a
    #     # sql2 =  "select password from User where name = "+ " '{}' ".format(form.name.data)
    #     # cursor.execute(sql2)
    #     # b = cursor.fetchone()
    #     # print b
    #     # sql = "<div class="row">
    #
    #     # c = cursor.fetchall()
    #     # print c
    #     conn.commit()
    #     # cursor.close()
    #     # conn.close()
    #     return redirect(url_for('success'))
    # return render_template('register.html',form=form)

# @app.route('/library', methods=['GET','POST'])
# def library():
#     return render_template('library.html')
#
#
#
#

