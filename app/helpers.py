#Helper functions for app such as connection to database ect.
#Import all required modules
#Set databse
#Set secrect key

import flask
from flask import render_template, request, redirect, url_for
from flask import g
import sqlite3


DATABASE = 'database.db'
UPLOAD_FOLDER = 'uploads'


app = flask.Flask(__name__)

app.config.update(
    SECRET_KEY="secr3!t",
    SESSION_COOKIE_SAMESITE='Strict',
    UPLOAD_FOLDER=UPLOAD_FOLDER
)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

'''
Function to query db
params:- query eg."SELECT * FROM users WHERE email=%s"
       - values eg. email of user
output:- returns
'''
def query_db(query, values, one=False):
    app.logger.info("QUERY:%s, Value:%s", query, values)
    cur = get_db().execute(query, values)#Open connection to DB and execute query
    result = cur.fetchall()#Collect the response from DB
    cur.close()#Close DB connection
    return (result[0] if result else None) if one else result#If one is true - return result[0] if result exists else return result

#Initialise the DB and apply the schema "https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('../schema.sql', mode='r') as file:
            db.cursor().executescript(file.read())
        db.commit()

#Close the connection to the database
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()