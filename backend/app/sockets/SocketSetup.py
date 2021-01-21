from flask import Flask
from flask_socketio import SocketIO,send
from app.main import app





socketio=SocketIO(app)
app.debug=True
app.host='localhost:5000'
socketio = SocketIO(app,cors_allowed_origins='*')


@socketio.on('message')
def handle_message(message):
    print('recieved message: '+ message)
    send(message)