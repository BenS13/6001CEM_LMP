from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import *
from sqlalchemy import select
from functools import wraps

main = Blueprint('main', __name__)

#Define a decorator to check for educator role
def educator_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if current_user.userRole == "educator":
            return f(*args, **kwargs)
        else:
            flash("You need to be an admin to view this page")
            return redirect(url_for('main.index'))
    return wrap

#Function to get current enrolled modules for current user
def get_enrolled_modules():
    enrolled_modules= []
    query = select(Enrolment).where(Enrolment.userId == current_user.id)
    enrolment = db.session.execute(query)
    for x in enrolment:
        for y in x:
            enrolled_modules.append(y.moduleCode)
    return enrolled_modules


@main.route('/')
@login_required
def index():
    enrolled_modules= get_enrolled_modules()#Run function defined above
    #print(current_user.userRole)
    if current_user.userRole == "admin":
        return redirect(url_for('admin.admin_panel'))
    else:
    
        return render_template('account.html', enrolled_modules=enrolled_modules)



#-----ROUTE TO ACCESS A MODULE------#
@main.route('/module')#First we load the posts for the module
@login_required
def module_home():
    module_code = request.args.get('module')#Get module code from URL
    
    
    enrolled_modules= get_enrolled_modules()

    #Check if user is enrolled in the module
    #IF NO do something
    #ELSE load requested page.
    if module_code not in enrolled_modules:
        print("Error user not enrolled in this course")
        return "Error you are not enrolled in this module"
    else:
        content = "POSTS"
        return render_template('index.html', code=module_code, content=content, enrolled_modules= enrolled_modules)

#Learning materials
@main.route('/module/materials')
@login_required
def module_materials():
    module_code = request.args.get('module')
    
    enrolled_modules= get_enrolled_modules()

    if module_code not in enrolled_modules:
        print("Error user not enrolled in this course")
        return "Error you are not enrolled in this module"
    else:
        content = "Materials"
        return render_template('index.html', code=module_code, content=content, enrolled_modules= enrolled_modules)

#Assignments
@main.route('/module/assignments')
@login_required
def module_assignments():
    module_code = request.args.get('module')

    enrolled_modules= get_enrolled_modules()

    if module_code not in enrolled_modules:
        print("Error user not enrolled in this course")
        return "Error you are not enrolled in this module"
    else:
        content = "Assignments"
        return render_template('index.html', code=module_code, content=content, enrolled_modules= enrolled_modules)



#Route for educator to manage module
@main.route('/module/manage')
@login_required
@educator_required
def module_manage():
    enrolled_modules= get_enrolled_modules()
    module_code = request.args.get('module')
    return render_template('manage_module.html', code=module_code, enrolled_modules=enrolled_modules)


@main.route('/account')
@login_required
def account():
    return render_template('user_preferences.html')

'''Function to initaliase the Database'''
@main.route('/initdb')
def initdb():
    db.create_all()
    return 'DB CREATED'