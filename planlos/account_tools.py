# coding: utf-8

from planlos.passwordgen import Password_Generator
from flaskext.mail import Message
from planlos.extensions import mail, db
from documents import User, Group, Group_Admin, User_Exists_Exception
from flask import current_app as app
from datetime import datetime
import uuid

# signals
from planlos.signals import user_requested


def generate_activation_code():
    return unicode(uuid.uuid1())

def find_all_group_members(group):
    #db.User.find(
    pass


def create_user(username, password, email):
    if db.User.find_one({'username': username}) == None and db.Group.find_one({'name': username}) == None:
        # create group
        g = db.Group()
        g.name = username
        g.desc = u'User Group'
        g.save()

        # create user
        user = db.User()
        user.username = username
        user.password = password
        user.signup_email = email
        user.activation_key = generate_activation_code()
        user.groups = [ g ]
        user.save()

        ga = db.Group_Admin()
        ga.group = g._id
        ga.admins = [user._id]
        ga.save()

        return user
    else:
        raise User_Exists_Exception()


def remove_user(username):
    user = db.User.find_one({'username': username})
    group = db.Group.find_one({'name': username})
    groupadmin = db.Group_Admin.find_one({'group': group._id})
    groupadmin.delete()
    user.delete()
    group.delete()


    # remove other groups if empty
    # remove user
    # send email?
    # signal admin dashboard


def request_user_account(username, password, email,
                         send_activation_code=True):
    user = create_user(username, password, email)
    # send activation email
    if send_activation_code:
        # email activation link
        # TODO: send this with some message_queue to avoid hanging app
        activation_msg = Message("Hello",
                                 sender="accounts@planlosbremen.de",
                                 recipients=[user.signup_email])
        activation_msg.body = """Click this link:
        http://localhost:5000/users/%s/activation/%s
        """ % (user.username, user.activation_key)
        mail.send(activation_msg)
    # signal Admin (dashboard the new user added)
    user_requested.send(app._get_current_object(),
                        user=user)

def request_group(groupname, owner, public=False, desc=''):
    pass
