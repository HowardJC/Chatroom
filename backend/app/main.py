from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
app.config['SECRET_KEY']= 'Cool'
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///../Chat.db"

import app.sockets.SocketSetup as sockets

from app.routes.register import *



if __name__ == "__main__":
    sockets.socketio.run(app)

