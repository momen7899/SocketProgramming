from flask import Flask, redirect, render_template, flash, request
from flask_mysqldb import MySQL
from flask_socketio import SocketIO
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mochat'
mysql = MySQL(app)
socketio = SocketIO(app)


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/chat/', methods=['POST', 'GET'])
def chat():
    if request.method == 'GET':
        return redirect("http://127.0.0.1:5000/")
    elif request.method == 'POST':
        name = request.form['username']
        md = md5(request.form['pass'])
        cursor = mysql.connection.cursor()
        if request.form['submit'] == 'login':
            cursor.execute(
                ''' SELECT id from user WHERE user_name = %s AND password = %s''', (name, md))
            mysql.connection.commit()
            if cursor.rowcount >= 1:
                cursor.close()
                name = name + ":"
                return render_template("index.html", name=name)
            cursor.close()
            flash("There is no such a user")
            return redirect("http://127.0.0.1:5000/")
        elif request.form['submit'] == 'sign':
            try:
                cursor.execute(
                    ''' INSERT INTO user  (user_name, password) VALUES (%s, %s)''', (name, md))
                mysql.connection.commit()
            except:
                flash("User Name has been used.\nChoose another one")
                return redirect("http://127.0.0.1:5000/")
            if cursor.rowcount >= 1:
                flash("User Successfully Added")
            else:
                flash("Data Error Please Try Again")
            cursor.close()
            return redirect("http://127.0.0.1:5000/")


@app.route('/user/register', methods=['POST', 'GET'])
def register():
    print(request.form['sign-btn'])


def md5(password):
    md5 = hashlib.md5(password.encode()).hexdigest()
    return md5


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
