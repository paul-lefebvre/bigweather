import os
from HelloFlask import app, socketio
from flask_socketio import SocketIO

#LOGGER DE L'API
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#DEMARRAGE DU WEBUI FLASK-SOCKETIO 
if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=8080)