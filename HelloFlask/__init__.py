#IMPORTS
from flask import Flask
from flask_socketio import SocketIO
from itsdangerous import URLSafeTimedSerializer

#INITIALISATION DE FLASK
app = Flask(__name__)

socketio = SocketIO(app)

#IMPORT DES VIEWS
import HelloFlask.views