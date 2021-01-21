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

@app.route("/api/login", methods=["POST"])
def login():
    try:
        Email=request.json["Email"].lower()
        Password=request.json["Password"]
        ActiveUsers=getUsers(Email,Password)
        if ActiveUsers!=False:
            print("Proper Login", ActiveUsers)
            token=create_access_token(identity=ActiveUsers);

            return jsonify({"token":token});
        else:
            print("Error Logging in")
            return jsonify({"error": "Wrong Email/Password"})
    except Exception as e:
        return jsonify({"error": e})



@jwt.user_identity_loader
def add_claims_to_access_token(ActiveUsers):
    print("Works", ActiveUsers)
    print(ActiveUsers.Username)
    return {'username': ActiveUsers.Username,
            'email': ActiveUsers.Email}


