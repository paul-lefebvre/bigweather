from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user 



#CLASSE USER 
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = ""
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)