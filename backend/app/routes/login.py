from app.main import app
from flask import Flask,request,jsonify
from app.database.Database_Setup import *

def getUsers(email):
    ActiveUsers=Account.query.get(email)
    if ActiveUsers == None:
        print("Picked up None")
        return False
    else:
        return ActiveUsers

@app.route("/api/login", methods=["POST"])
def login():
    try:
        Email=request.json["Email"].lower()
        Password=request.json["Password"]
        ActiveUsers=getUsers(Email)
        if ActiveUsers!=False:

            print("Proper Login")
            return jsonify({"answer":"True"})
        else:
            print("Email Already Registered")
            return jsonify({"error": "Email already registered"})
    except Exception as e:
        return jsonify({"error": e})




