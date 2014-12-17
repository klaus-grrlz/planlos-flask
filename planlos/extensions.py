# coding: utf-8
from flask.ext.mail import Mail
from flask.ext.mongokit import MongoKit
from flask.ext.login import LoginManager

login_manager = LoginManager()
db = MongoKit()
mail = Mail()
