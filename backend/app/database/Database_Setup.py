from flask_sqlalchemy import SQLAlchemy
from app.main import app


Chat = SQLAlchemy(app)

class Message(Chat.Model):
    __tablename__="message"
    id = Chat.Column(Chat.Integer,primary_key=True)
    username=Chat.Column(Chat.String(24))
    Message=Chat.Column(Chat.String(1000))
    user_id=Chat.Column(Chat.Integer,Chat.ForeignKey('account.Email'))
    def __init__(self,username,Message):
        self.username=username
        self.Message = Message

class Account(Chat.Model):
    Email = Chat.Column(Chat.String(1000),primary_key=True)
    Username=Chat.Column(Chat.String(24))
    Password=Chat.Column(Chat.String(1000))
    post = Chat.relationship('Message',backref='account',lazy=True)
    def __init__(self,Email,Username,Password):
        self.Email=Email
        self.Username=Username
        self.Password=Password

if __name__ == "__main__":
    print("Creating Database")
    Chat.create_all()