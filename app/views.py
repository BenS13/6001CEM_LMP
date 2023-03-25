from .helpers import * #Import functions from helper file(eg. init_db)
from flask import render_template


#Route for root page
@app.route("/")
def index():
    return render_template("index.html")







#Route to initialise the database
@app.route("/initdb")
def database_init():
    init_db()
    return "Finished"