from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db


main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html', name=current_user.name)



#-----ROUTE TO ACCESS A MODULE------#
@main.route('/module')#First we load the posts for the module
@login_required
def module():
    module_code = request.args.get('module')#Get module code from URL
    type = request.args.get('type')#Get type eg. Community, Journey(materials), Journey(assignments)

    #Check if user is enrolled in the module
    #IF yes load the community page
    #ELSE dont load the page

    
    if type == 'materials':#?module=X&type=materials
        materials = "INSERT MATERIALS HERE"
        return render_template('index.html',name=current_user.name, code=module_code, content=materials)
    #Get the posts for that module ?module=X
    elif type == 'assignments':#?module=X&type=assignments
        assignments = "INSERT ASSIGNMENTS HERE"
        return render_template('index.html', name=current_user.name, code=module_code, content=assignments)
    else:#?module=X&type=community or none
        posts = "INSERT POSTS HERE"
        return render_template('index.html', name=current_user.name, code=module_code, content=posts)




@main.route('/account')
@login_required
def account():
    return render_template('user_preferences.html', name=current_user.name)

'''Function to initaliase the Database'''
@main.route('/initdb')
def initdb():
    from .models import User
    db.create_all()
    return 'DB CREATED'