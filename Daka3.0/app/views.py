# encoding=utf-8
from app import app, db
from flask import render_template, redirect, request, jsonify, redirect, g, url_for
from flask_login import login_required, login_user, current_user, logout_user
from .models import User, Punch
from sqlalchemy.sql import func

@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/register')
def register():
    nickname = request.args.get('nicknameValue')
    password = request.args.get('passwordValue')
    user = User(
        nickname=u'{}'.format(nickname),
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"result": "success"})


@app.route('/login', methods=['GET', 'POST'])
def login():
    nickname = request.args.get('nicknameValue')
    password = request.args.get('passwordValue')

    print nickname
    print password

    user = User.query.filter_by(nickname=nickname).first()
    print user
    if user is not None and user.verify_password(password):
        login_user(user)
        return jsonify({"result": "success"})
    elif user is None:
        return jsonify({"result": "Invalid_user"})
        # return redirect(url_for('home'))
    return jsonify({"result": "error"})


@app.route('/punch')
def punch():
    dsc = request.args.get('descript')
    time = request.args.get('time')
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    hour = request.args.get('hour')
    worktime = request.args.get('worktime')

    # if (dsc == 'the whole day'):
    #     worktime = 1
    # else:
    #     worktime = 0.5
    print g.user.nickname
    # print dsc
    # print time
    punch = Punch(
        time=time,
        description=dsc,
        worktime=worktime,
        name=g.user.nickname,
        year=year,
        month=month,
        day=day,
        hour=hour,
    )
    db.session.add(punch)
    db.session.commit()

    return jsonify({"result": "success"})


@app.route('/test')
def test():
    result = Punch.query.filter_by(name="123").all()
    print result
    hello = [1, 2, 3, 4, 5]
    return render_template("test.html", hello=hello, result=result)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/getuserdata')
def getuserdata():
    print g.user.nickname
    result = db.session.query(Punch.day,Punch.worktime,Punch.description,Punch.name,Punch.month,Punch.year,).filter(Punch.month == 4).filter( Punch.name == g.user.nickname).all()
    print result
    return jsonify(result=result)

@app.route('/getusermonthdata')
def getusermonthdata():
    # sql = "select Punch.month, sum(Punch.worktime) as worktime from punch group by punch.month where punch.name == g.user.nickname "
    result = db.session.query(Punch.month, func.sum(Punch.worktime)).filter(Punch.name == g.user.nickname).group_by(Punch.month).all()
    # db.session.query(Punch.month, Punch.worktime).filter(Punch.name == '123').group_by(Punch.month).all()
    # db.session.execute("select Punch.month, sum(Punch.worktime) as worktime from punch group by punch.month where punch.name == g.user.nickname" )
    #
    # result = db.session.query(Punch).filter(Punch.year == '2017').group_by(Punch.month).all()
    # result= db.session.execute("select Punch.month, sum(Punch.worktime) as worktime from punch group by punch.month ")

    # print result
    print result
    return jsonify(result=result)
