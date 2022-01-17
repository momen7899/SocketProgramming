import hashlib
from dataclasses import dataclass

from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_socketio import SocketIO


@dataclass
class User:
    id: int
    username: str


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mochat'
mysql = MySQL(app)
socketIo = SocketIO(app)


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/home')
def home():
    userId = request.values['id']
    userName = request.values['username']
    return render_template("home.html", id=userId, userName=userName)


@app.route('/chat', methods=['POST', 'GET'])
def chat():
    print(request.values)
    return render_template("chat.html")


def md5(password):
    md5 = hashlib.md5(password.encode()).hexdigest()
    return md5


def messageReceived():
    print('message was received!!!')


@socketIo.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketIo.emit('my response', json, callback=messageReceived)


@app.route('/api/login')
def loginApi():
    name = request.values['username']
    md = md5(request.values['password'])
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * from user WHERE user_name = %s AND password = %s''', (name, md))
    mysql.connection.commit()
    records = cursor.fetchall()

    user = (0, "NotFound!")

    for row in records:
        user = User(row[0], row[1])
    cursor.close()

    return jsonify(user)


@app.route('/api/getUsers')
def getUserApi():
    userId = request.values['userId']
    cursor = mysql.connection.cursor()

    cursor.execute(''' SELECT * FROM user WHERE id != %s''', str(userId))
    mysql.connection.commit()
    records = cursor.fetchall()

    users = []

    for row in records:
        users.append(User(row[0], row[1]))

    cursor.close()
    return jsonify(users)


if __name__ == '__main__':
    socketIo.run(app, port=5000, debug=True)
