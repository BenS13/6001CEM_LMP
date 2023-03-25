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
        email = flask.request.form.get("email")#Request email from form
        password = flask.request.form.get("password")
        app.logger.info("Attempt login %s:%s", email, password)
        
        query = 'SELECT * FROM users WHERE email=?'
        q_result = query_db(query, email)

        if q_result is None:
            flask.flash("No such user with inputted email")
        else:
            app.logger.info("USER IS VALID")
            if q_result["password"] == password:
                app.logger.info("Sign in Success %s", email)
                #set up session for user
                flask.flash("Sign In Succesful")
                return redirect(url_for("index"))
            else:
                flask.flash("Password incorrect")
    else:
        return render_template("login.html")




#Route to initialise the database
@app.route("/initdb")
def database_init():
    init_db()
    return "Finished"