from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

# Error 발생시, pip install PyJWT
import jwt
from datetime import datetime, timedelta

from flask_paginate import Pagination, get_page_parameter

# 비밀번호 암호화.
import hashlib

from pytz import timezone


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbgroups

SECRET_KEY = 'MySecretKey'

now = datetime.now()

# 페이지 렌더링
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def MoveToSignup():
    return render_template('signup.html', current_time=now.strftime("%A %d. %B %Y"))

@app.route('/login')
def MoveToLogin():
    return render_template('login.html', current_time=now.strftime("%A %d. %B %Y"))


@app.route('/mypage')
def MoveToMypage():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        target_id = payload['id']
        page = request.args.get(get_page_parameter(), type=int, default=1)
        per_page = 3
        offset = (page - 1) * per_page
        total = db.agroup.count_documents({})
        items = list(db.agroup.find({'userid':target_id}).skip(offset).limit(per_page))
        pagination = Pagination(
            page=page, 
            per_page=per_page,
            total=total,
            prev_label="<<",  # 전 페이지와,
            next_label=">>",  # 후 페이지로 가는 링크의 버튼 모양을 알려주고,
            format_total=True,  # 총 몇 개의 포스트 중 몇 개의 포스트를 보여주고있는지 시각화,
            )
        
        return render_template('mypage.html',current_time=now.strftime("%A %d. %B %Y"), items=items,pagination=pagination,
    page = request.args.get(get_page_parameter(), type=int, default=1))
    except:
        return jsonify({'result': 'fail'})
    
@app.route('/register')
def registerpage():
    return render_template('register.html', current_time=now.strftime("%A %d. %B %Y"))



@app.route('/listpage')
def listpage():
    # glist = list(db.agroup.find({}))
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 3
    offset = (page - 1) * per_page
    total = db.agroup.count_documents({})
    items = list(db.agroup.find().skip(offset).limit(per_page))
    pagination = Pagination(
        page=page,
        per_page=per_page,
        total=total,
        prev_label="<<",  # 전 페이지와,
        next_label=">>",  # 후 페이지로 가는 링크의 버튼 모양을 알려주고,
        format_total=True,  # 총 몇 개의 포스트 중 몇 개의 포스트를 보여주고있는지 시각화,
    )
    return render_template('listpage.html', current_time=now.strftime("%A %d. %B %Y"), items=items, current_time2=now.strftime('%H:%M:%S'), pagination=pagination,
                           page=request.args.get(get_page_parameter(), type=int, default=1))

# API 회원가입
@app.route('/signup', methods=['POST'])
def signup():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    teacher_receive = request.form['teacher_give']

    sports_checked = request.form['sports_give']
    coding_checked = request.form['coding_give']
    etc_checked = request.form['etc_give']

    doc = {
        'id': id_receive,
        'pw': pw_hash,
        'teacher': teacher_receive,
        'sports': sports_checked,
        'coding': coding_checked,
        'etc': etc_checked,
    }
    db.user.insert_one(doc)
    return jsonify({'result': 'success'})

# API 로그인
@app.route('/login', methods=['POST'] )
def login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    user = db.user.find_one({'id':id_receive, 'pw':pw_hash},{'_id':False})

    if user == None:
        return jsonify({'result': 'fail'})
    else:
        # 토큰 발행
        payload = {
            'id' : user['id'],
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        # print(token)
        return jsonify({'result': 'success', 'token': token})



# # API 취미 수정
@app.route('/mypage/hobbySelected', methods=['GET'])
def showHobby():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        target_id = payload['id']

        hobby = list(db.user.find({'id': target_id}, {
                    '_id': 0, 'pw': 0, 'teacher': 0}))
        return jsonify({'result': 'success', 'hobby': hobby})
    except:
        return jsonify({'result': 'fail'})


@app.route('/mypage', methods=['PUT'])
def editHobby():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        target_id = payload['id']

        sports_checked = request.form['sports_give']
        coding_checked = request.form['coding_give']
        etc_checked = request.form['etc_give']

        db.user.update_one(
            {'id': target_id},
            {'$set': {
                'sports': sports_checked,
                'coding': coding_checked,
                'etc': etc_checked,
            }}
        )
        return jsonify({'result': 'success'})
    except:
        return jsonify({'result': 'fail'})

# API 비밀번호 수정
@app.route('/mypage', methods=['POST', 'PATCH'])
def editPassWord():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        target_id = payload['id']

        user = db.user.find_one({'id': target_id})

        if request.method == 'POST':
            teacher_receive = request.form['teacherName_give']
            if teacher_receive == user['teacher']:
                return jsonify({'result': 'success'})
            else:
                return jsonify({'result': 'fail'})
        elif request.method == 'PATCH':
            pw_receive = request.form['modPassWord_give']
            pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
            db.user.update_one({'id': target_id}, {'$set': {'pw': pw_hash}})
            return jsonify({'result': 'success'})
    except:
        return jsonify({'result': 'fail'})
    

global num
num = 0

@app.route('/register', methods=['POST'])
def postgroup():
    token_receive = request.cookies.get('mytoken')
    global num
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        target_id = payload['id']

        hobby_receive = request.form['hobby_give']
        comment_receive = request.form['comment_give']
        # img_receive = request.files['image_give']
        start_receive = request.form['start_give']
        end_receive = request.form['end_give']
        maxpeople_receive = request.form['maxpeople_give']
        create_time = datetime.now(timezone('Asia/Seoul'))
        num += 1

        doc = {
            'hobby': hobby_receive,
            'comment': comment_receive,
            # 'img' : img_receive,
            'create_time': create_time,
            'userid': target_id,
            'start': start_receive,
            'end': end_receive,
            'maxpeople': maxpeople_receive,
            'nickname': num,
            'nowpeople': 1,
        }
        db.agroup.insert_one(doc)

        doc2 = {
            'userid': target_id,
        }
        db['g'+str(num)].insert_one(doc2)
        return jsonify({'result': 'success'})

    except:
        return jsonify({'result': 'fail'})


@app.route('/listpage_hall', methods=['GET'])
def showlist():
    registerList = list(db.agroup.find(
        {}, {'_id': False}).sort('create_time', -1))
    return jsonify({'result': 'success', 'registerList': registerList})


@app.route('/listpage_hall', methods=["POST"])
def attend():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        target_id = payload['id']

        num = request.form['num']
        oneGroup = db.agroup.find_one({'nickname': int(num)})
        maxpeople = int(oneGroup['maxpeople'])
        new_nowpeople = int(oneGroup['nowpeople'])+1
        if maxpeople >= new_nowpeople:
            user = db['g'+str(num)].find_one({'userid': target_id})
            if user == None:
                db['g'+str(num)].insert_one({'userid' : target_id})
                db.agroup.update_one({'nickname': int(num)}, {'$set':
                                                            {'nowpeople': new_nowpeople}})
                return jsonify({'result': 'success'})
            else:
            #     # 이미 참가한 모임입니다.
                return jsonify({'result': 'already'}) 
        else:
            # 꽉 찼습니다.
            return jsonify({'result': 'full'})
    except:
        return jsonify({'result': 'fail'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
