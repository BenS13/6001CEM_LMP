from .helpers import * #Import functions from helper file(eg. init_db)
from flask import render_template


#Route for root page
@app.route("/")
def index():
    return redirect(url_for("login"))


#Route for login
@app.route("/user/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        #recvive data from login form
        #perform secure login
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        app.logger("Attempt login %s:%s", email, password)
        return None
    else:
        return render_template("login.html")




#Route to initialise the database
@app.route("/initdb")
def database_init():
    init_db()
    return "Finished"