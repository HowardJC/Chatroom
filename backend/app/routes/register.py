from app.main import app
from flask import Flask,request,jsonify
from app.database.Database_Setup import *

def getUsers(email):
    ActiveUsers=Account.query.get(email)
    if ActiveUsers == None:
        print("Picked up None")
        return False

@app.route("/api/register", methods=["POST"])
def register():
    try:
        Email=request.json["Email"]
        Username=request.json["Username"]
        Password=request.json["Password"]
        if getUsers(Email)==False:
            NewAccount=Account(Email,Username,Password)
            Chat.session.add(NewAccount)
            Chat.session.commit()
            print("New Email Registered")
            return jsonify({"answer":"True"})
        else:
            print("Email Already Registered")
            return jsonify({"error": "Email already registered"})
    except Exception as e:
        return jsonify({"error": e})



