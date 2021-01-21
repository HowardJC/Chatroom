from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity

app=Flask(__name__)
CORS(app)
app.config['SECRET_KEY']= 'Cool'
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///../Chat.db"
app.config["JWT_SECRET_KEY"]="Clown_Car"
jwt = JWTManager(app)
import app.sockets.SocketSetup as sockets


from app.routes.login import *
from app.routes.register import *




if __name__ == "__main__":
    sockets.socketio.run(app)

