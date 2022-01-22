# Welcome to MoChat!

Hi! this project is a sample of web socket programming chat by using python flask as a backend and html, CSS ,... for front end and for api we use ajex lib.


## Data Base
We use MySQL for store our users, so we need a MySQL data base called `mochat`,  user of db should be `root`.  No password for db user.
You can custom above items in [index.py](https://github.com/momen7899/SocketProgramming/blob/master/Project/Server/index.py) line 18, 19 & 20.

    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'mochat'	
 
To Create `user` table enter the below code.

    CREATE TABLE user ( id int NOT NULL AUTO_INCREMENT, user_name varchar(255) NOT NULL,password varchar(255), PRIMARY KEY (id));

`user` table should be like this.
|Name | type|
|--|--|
| id | int |
| user_name | varchar(255) |
| password | varchar(255) |




## Run project

To run project you should install [python](https://www.python.org/downloads/) first.
Then enter below code to install other libs.
 

    pip install Flask
    pip install flask-mysqldb
    pip install flask-socketio

last thing you should do is connect run below code in terminal for linux and max and cmd for windows of [this](https://github.com/momen7899/SocketProgramming/tree/master/Project/Server) folder : `/Project/Server`

    python index.py


## Points
This project use port number 80 to run flask server.
You can change it by change `socketIo.run(app, port=80, debug=True)` in line 111 of [index.py](https://github.com/momen7899/SocketProgramming/blob/master/Project/Server/index.py).
Or you can be sure that another program is not using this port as [xampp](https://www.apachefriends.org/index.html).
