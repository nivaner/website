# coding:utf-8
from app import app, db
from flask import g, redirect, render_template, jsonify, request, url_for
from flask_login import current_user
from flask_security import login_required
from .forms import PostForm, EditForm
from .models import Post, Category

from werkzeug.utils import secure_filename
import time
import os
import base64


# -------------------------  * 请求登录 * -------------------------------
@app.before_request
def before_request():
    g.user = current_user


# *********************************************************************
# ------------------------- * 上次图片 * -------------------------------
UPLOAD_FOLDER = 'static/imgs'  # 设置图片保存路径
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
# 允许上传的图片后缀名
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'tiff', 'pdf', 'jpeg', 'JPG', 'PNG', 'gif', 'GIF'])


# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload')
def upload():
    return render_template('upload.html')


# 上传图片
@app.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myImage']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型

        fname = secure_filename(f.filename)  # 增加安全性

        try:
            ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        except IndexError:
            # 如果图片为中文名
            ext = fname.rsplit('.', 1)[0]  # 获取文件后缀

        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext  # 基于unix时间修改了上传的文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到static下的upload目录
        token = base64.b64encode(new_filename)
        print token
        pic = base64.b64decode(token)
        src = url_for('static', filename='imgs/{}'.format(pic))  # 生成URL
        # return render_template("success.html",token=src)
        return src
    else:
        return jsonify({"errno": 1001, "errmsg": "上传失败"})


@app.route('/')
@app.route('/home')
# @login_required
def home():
    return render_template("index.html")


# *********************************************************************
# -------------------------  * 二维码 * -------------------------------

# show wechat QRcode
@app.route('/wechat')
def wechat():
    return render_template("wechat.html")


# *********************************************************************
# -------------------------  * 编辑博客 * -------------------------------

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    print 'sssss'
    if form.validate_on_submit():
        if Category.query.filter_by(tag='{}'.format(form.category.data)).first() is None:
            category = Category(tag=form.category.data)
            db.session.add(category)
            db.session.commit()
            post = Post(body=form.body.data, title=form.title.data, category_tag=form.category.data)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog'))
        else:
            post = Post(body=form.body.data, title=form.title.data, category_tag=form.category.data)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog'))
    return render_template("edit.html", form=form)

# *********************************************************************
# -------------------------  * 留言 * -------------------------------
@app.route('/message', methods=['GET', 'POST'])
def message():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, title=form.title.data)
        db.session.add(post)
        return redirect(url_for('message'))
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=3, error_out=False)
    posts = pagination.items
    return render_template("message.html", form=form, posts=posts, pagination=pagination)


# *********************************************************************
# -------------------------  * 显示博客主页 * -------------------------------

@app.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=3, error_out=False)
    posts = pagination.items
    return render_template("blog.html", posts=posts, pagination=pagination)


# *********************************************************************
# -------------------------  * 文章固定连接 * -------------------------------

@app.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template("post.html", post=post)
