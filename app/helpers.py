#Helper functions for app such as connection to database ect.

import flask
from flask import g
from flask_mysqldb import MySQL

DATABASE = 'database.db'
UPLOAD_FOLDER = 'uploads'


app = flask.Flask(__name__)

app.config.update(
    SECRET_KEY="secr3!t",
    SESSION_COOKIE_SAMESITE='Strict',
    UPLOAD_FOLDER=UPLOAD_FOLDER
)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USR'] = 'root'
app.config['MYSQL_PASSWORD'] = 'seed'
app.config['MYSQL_DB'] = 'database'

mysql = MySQL(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = mysql.connect(DATABASE)
    return db




def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('../schema.sql', mode='r') as file:
            db.cursor().executescript(file.read())
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()