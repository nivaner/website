from app import  app
from flask import  render_template,g
from flask_login import current_user
from flask_security import login_required

@app.route('/')
# @login_required
def home():
    return  render_template("index.html")

@app.before_request
def before_request():
    g.user = current_user
