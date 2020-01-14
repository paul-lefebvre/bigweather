#IMPORTS
from flask import Flask
from flask_socketio import SocketIO

#INITIALISATION DE FLASK
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

#IMPORT DES VIEWS
import HelloFlask.views