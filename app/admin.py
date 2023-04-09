from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from functools import wraps
from .models import *
from . import db

admin = Blueprint('admin', __name__)#Create a blueprint with this file called admin


#Define a decorator to check for admin role
def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.userRole == "admin":
            return f(*args, **kwargs)
        else:
            flash("You need to be an admin to view this page")
            return redirect(url_for('main.index'))
    return wrap


#Admin panel#
@admin.route('/admin')
@login_required
@admin_required
def admin_panel():
    return render_template('admin_panel.html')


#User management panel
@admin.route('/admin/usermanagement')
@login_required
@admin_required
def user_management():
    users = User.query.all()
    print(users)
    return render_template('user_management.html', users=users)


#Register a user
@admin.route('/admin/usermanagement/register')
@login_required
@admin_required
def register_user():
    return render_template('register_user.html')

@admin.route('/admin/usermanagement/register', methods=['POST'])
@login_required
@admin_required
def register_user_post():
    role = request.form.get('role')
    email = request.form.get('email')
    password = 'password1'
    name = request.form.get('name')
    level = request.form.get('level')

    user = User.query.filter_by(userEmail=email).first()

    if user:
        flash("User already exists:{}".format(email))
        print("User exists already")

    else:
        new_user = User(userRole=role, userEmail=email,  userPassword=generate_password_hash(password, method='sha256'), userName=name, userLevel=level)#Create new user based on User class

        db.session.add(new_user)#Add new user to users table
        db.session.commit()#Commit changes to DB

        flash("User created:{}".format(email))
    return redirect(url_for("admin.register_user"))


#Module management panel
#Module managment
@admin.route('/admin/modulemanagement')
@login_required
@admin_required
def module_management():
    modules = Module.query.all()
    return render_template('module_management.html', modules=modules)


@admin.route('/admin/modulemanagement/create')
@login_required
@admin_required
def create_module():
    return render_template('create_module.html')

@admin.route('/admin/modulemanagement/create', methods=['POST'])
@login_required
@admin_required
def create_module_post():
    code = request.form.get('module_code')
    name = request.form.get('module_name')
    level = request.form.get('module_level')

    module = Module.query.filter_by(moduleCode=code).first()

    if module:
        flash("Module already exists:{}".format(code))
        print("Module exists already")

    else:
        new_module = Module(moduleCode=code, moduleName=name, moduleLevel=int(level))
        db.session.add(new_module)#Add new user to users table
        db.session.commit()#Commit changes to DB

        flash("Module created:{}".format(code))

    return redirect(url_for('admin.create_module'))


#Enrol user onto module
@admin.route('/admin/modulemanagement/enrol')
@login_required
@admin_required
def enrol_user():
    users = User.query.all()
    modules = Module.query.all()
    enrolment = Enrolment.query.all()

    return render_template('enrol_users.html', users=users, modules=modules, enrolment=enrolment)

@admin.route('/admin/modulemanagement/enrol', methods=['POST'])
@login_required
@admin_required
def enrol_user_post():
    email = request.form.get('email')
    code = request.form.get('code')

    user = User.query.filter_by(userEmail=email).first()
    module = Module.query.filter_by(moduleCode=code).first()
    
    enrol = Enrolment.query.filter_by(moduleId=module.moduleId, userId=user.id).first()

    if enrol:
        flash("User: {} already enrolled on:{}".format(email,code))
        print("Module exists already")
    else:
        new_enrol = Enrolment(moduleId=module.moduleId, userId=user.id)
        db.session.add(new_enrol)#Add new user to users table
        db.session.commit()#Commit changes to DB

        flash("{} succesfully enrolled on: {}".format(email,code))
    return redirect(url_for('admin.enrol_user'))

   