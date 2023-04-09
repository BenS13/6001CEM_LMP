from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db


main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    enrolled_modules = ['5003CEM', '6003CEM', '7004CEM']
    return render_template('account.html', name=current_user.name, enrolled_modules=enrolled_modules)



#-----ROUTE TO ACCESS A MODULE------#
@main.route('/module')#First we load the posts for the module
@login_required
def module():
    module_code = request.args.get('module')#Get module code from URL
    type = request.args.get('type')#Get type eg. Community, Journey(materials), Journey(assignments)

    #Query the enrollement table
    #Find out what modules this user is enrolled in
    #save to a list such as the one below
    enrolled_modules = ['5003CEM', '6003CEM', '7004CEM']
    #pass this list into all the module pages
    

    #Check if user is enrolled in the module
    #IF NO do something
    #ELSE load requested page.
    if module_code not in enrolled_modules:
        print("Error user not enrolled in this course")
        return "Error you are not enrolled in this module"

    else:

        if type == 'materials':#?module=X&type=materials
            materials = "MATERIALS"
            return render_template('index.html',name=current_user.name, code=module_code, content=materials, enrolled_modules= enrolled_modules)
        #Get the posts for that module ?module=X
        elif type == 'assignments':#?module=X&type=assignments
            assignments = "ASSIGNMENTS"
            return render_template('index.html', name=current_user.name, code=module_code, content=assignments, enrolled_modules= enrolled_modules)
        else:#?module=X&type=community or none
            posts = "POSTS"
            return render_template('index.html', name=current_user.name, code=module_code, content=posts, enrolled_modules= enrolled_modules)




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