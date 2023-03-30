from flask import Blueprint, render_template
from . import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/account')
def account():
    return render_template('user_preferences.html')

'''Function to initaliase the Database'''
@main.route('/initdb')
def initdb():
    from .models import User
    db.create_all()
    return 'DB CREATED'