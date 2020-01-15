#IMPORTS
from flask import Flask
from flask_socketio import SocketIO
from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user 
from .models import User
#INITIALISATION DE FLASK
app = Flask(__name__)


app.config.update(
    SECRET_KEY = 'secret_xxx'
)


#INITIALISATION SOCKET IO
socketio = SocketIO(app)

#INITIALISATION LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "loginpage"



#IMPORT DES VIEWS
import HelloFlask.models
import HelloFlask.views