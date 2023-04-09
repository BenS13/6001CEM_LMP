from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



db = SQLAlchemy()




def make_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secr3!t'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    

    db.init_app(app)

    login_manager = LoginManager()#Create an instance of the login manager
    login_manager.login_view = 'auth.login'#Tell login manager what view to navigate to
    login_manager.init_app(app)#Initialise with the app

    from .models import User#Import User class/schema
    #Function to allow login manager request the user ID of a user
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    

    #Blueprint for auth routes eg .login
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #Blueprint for non auth parts of the web application
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Blue print for administrator views
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app

