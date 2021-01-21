from app.main import app
from flask import Flask,request,jsonify
from app.database.Database_Setup import *
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity,get_jwt_claims
from app.main import jwt;


def getUsers(email,password):
    ActiveUsers=Account.query.get(email)
    if ActiveUsers == None:
        print("Picked up None")
        return False
    else:
        if ActiveUsers.Password == password:
            return ActiveUsers
        else:
            return None

@app.route("/api/chat", methods=["POST"])
@jwt_required
def addMessage():
    print(get_raw_jwt['username'])





