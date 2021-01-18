from app.main import app
from flask import Flask,request,jsonify
from app.database.Database_Setup import *

@app.route("/api/messagehistory/", methods=["GET","POST"])
def users():
    method = request.method
    if (method.lower() == "get"):
        return jsonify([{"id":i.id, "username": i.username, "email": i.email, "password": i.pwd} for i in users])
    elif (method.lower() == "post"):
        username=request.json['username']
        message=request.json['message']
        user=Users(username,message)
        db.session.add(user)
        db.session.commit()

