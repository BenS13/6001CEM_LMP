import datetime
from flask_login import UserMixin
from . import db


class Role(db.Model):
    __tablename__ = 'role'
    roleName = db.Column(db.String(10), primary_key=True)
    roleDescription = db.Column(db.String(50))


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userRole = db.Column(db.Integer, db.ForeignKey(Role.roleName), nullable=False)
    userEmail = db.Column(db.String(50), unique=True, nullable=False)
    userPassword = db.Column(db.String(32), nullable=False)
    userName = db.Column(db.String(50), nullable=False)
    userLevel = db.Column(db.Integer, nullable=False)
    avatar_image = db.Column(db.String(100))

class Module(db.Model):
    __tablename__ = 'module'
    moduleId = db.Column(db.Integer, primary_key=True)
    moduleCode = db.Column(db.String(20), nullable=False)
    moduleName = db.Column(db.String(20), nullable=False)
    moduleLevel = db.Column(db.Integer, nullable=False)


class Enrolment(db.Model):
    __tablename__ = 'enrolment'
    enrolmentId = db.Column(db.Integer, primary_key=True)
    moduleCode = db.Column(db.Integer, db.ForeignKey(Module.moduleCode), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

class Post(db.Model):
    __tablename__ = 'post'
    postId = db.Column(db.Integer, primary_key=True)
    moduleId = db.Column(db.Integer, db.ForeignKey(Module.moduleId), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    postTitle = db.Column(db.String(50))
    postBody = db.Column(db.String(200))
    createdAt = db.Column(db.DateTime, default=datetime.datetime.now)

class Content(db.Model):
    __tablename__ = 'content'
    contentId = db.Column(db.Integer, primary_key=True)
    moduleId = db.Column(db.Integer, db.ForeignKey(Module.moduleId), nullable=False)
    contentTitle = db.Column(db.String(50))
    contentBody = db.Column(db.String())
    createdAt = db.Column(db.DateTime, default=datetime.datetime.now)

class File(db.Model):
    __tablename__ = 'file'
    fileId = db.Column(db.Integer, primary_key=True)
    contentId = db.Column(db.Integer, db.ForeignKey(Content.contentId), nullable=False)
    fileName = db.Column(db.String(20), nullable=False)
    fileSize = db.Column(db.Integer, nullable=False)
    fileType = db.Column(db.String(10), nullable=False)
    fileData = db.Column(db.LargeBinary, nullable=False)
