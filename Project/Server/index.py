from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
from flask_socketio import SocketIO
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'mochat'
# mysql = MySQL(app)
socketio = SocketIO(app)


@app.route('/')
def login():
<<<<<<< HEAD
    return render_template("login.html")


@app.route('/chat/', methods=['POST', 'GET'])
def chat():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        name = request.form['username']
        md = md5(request.form['pass'])
        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' SELECT id from user WHERE user_name = %s AND password = %s''', (name, md))
        mysql.connection.commit()
        if cursor.rowcount >= 1:
            cursor.close()
            name = name + ":\t"
            return render_template("index.html", name=name)

        cursor.close()
        return "There Is No such a User"
=======
    return render_template("index1.html")


# @app.route('/chat/', methods=['POST', 'GET'])
# def chat():
#     if request.method == 'GET':
#         return render_template("index1.html")
#     elif request.method == 'POST':
#         name = request.form['username']
#         md = md5(request.form['pass'])
#         cursor = mysql.connection.cursor()
#         cursor.execute(
#             ''' SELECT id from user WHERE user_name = %s AND password = %s''', (name, md))
#         mysql.connection.commit()
#         if (cursor.rowcount >= 1):
#             cursor.close()
#             return render_template("index1.html")
#
#         cursor.close()
#         return "There Is No such a User"
>>>>>>> 4dd63dde3070018f10f76e2db63c9f8b77a11987


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
