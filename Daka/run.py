#coding: utf-8

from app import app
app.run(debug=True)
# app.run(host='0.0.0.0', port=8888,debug=True, threaded=True)

# from flask import Flask,render_template,json,request
# from flask_login import LoginManager
# 
# app = Flask(__name__)
# loginManager = LoginManager(app)
# 
# loginManager.session_protection = "strong"
# loginManager.login_view = "login"
# 
# class User(db.Document):
#     name = db.StringField()
#     password = db.StringField()
#     email = db.StringField()
# 
#     def to_json(self):
#         return {"name": self.name,
#                 "email": self.email}
# 
#     def is_authenticated(self):
#         return True
# 
#     def is_active(self):
#         return True
# 
#     def is_anonymous(self):
#         return False
# 
#     def get_id(self):
#         return str(self.id)
# 
# @app.route('/')
# def home():
#     return render_template("index.html")
# 
# @app.route('/login', methods=['POST'])
# def login():
#     info = json.loads(request.data)
#     username = info.get('username', 'guest')
#     password = info.get('password', '')
# 
#     user = User.objects(name=username,
#                         password=password).first()
#     if user:
#         login_user(user)
#         return jsonify(user.to_json())
#     else:
#         return jsonify({"status": 401,
#                         "reason": "Username or Password Error"})
# 
# 
# if __name__ == '__main__':
#     app.run()
