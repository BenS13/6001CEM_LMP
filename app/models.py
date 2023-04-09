from flask_login import UserMixin
from . import db


class Role(db.Model):
    __tablename__ = 'role'
    roleName = db.Column(db.String(10), primary_key=True)
    roleDescription = db.Column(db.String(50))


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userEmail = db.Column(db.String(50), unique=True, nullable=False)
    userPassword = db.Column(db.String(32), nullable=False)
    userName = db.Column(db.String(50), nullable=False)
    userLevel = db.Column(db.Integer, nullable=False)
    avatar_image = db.Column(db.String(100))