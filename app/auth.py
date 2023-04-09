from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import *
from . import db

auth = Blueprint('auth', __name__)#Create blueprint for this file called auth


#--------------LOGIN--------------#
@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(userEmail=email).first()#Check if user exists

    #check supplied password(-> Hashed) against password in DB(Hashed)
    if not user or not check_password_hash(user.userPassword, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    #If check above passes, user has entred correct info
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))



#***------------SIGNUP---------------------------------****#
@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')#Get email from signup form
    name = request.form.get('name')#Get name from signup form
    password = request.form.get('password')
    level = request.form.get('level')
    #print(email,name,password,level)

    user = User.query.filter_by(email=email).first()

    if user:
        flash("User already exists:{}".format(email))
        #print("USer exists already")
        return redirect(url_for('auth.signup'))
        
    
    new_user = User(email=email,  password=generate_password_hash(password, method='sha256'), name=name, level=level)#Create new user based on User class

    db.session.add(new_user)#Add new user to users table
    db.session.commit()#Commit changes to DB

    #app.logger.info("New user created: {}".format(email))
    return redirect(url_for('auth.login'))



#--------------LOGOUT-------------------#
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))