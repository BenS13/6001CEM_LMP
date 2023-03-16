from .helpers import *


@app.route("/")
def index():
    return "Test Page"








@app.route("/initdb")
def database_init():
    init_db()
    return "Finished"