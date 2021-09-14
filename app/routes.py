from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from app.database import User


@app.route("/")
def home():
    out = {
        "status": "ok",
        "message": "Success",
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return out

@app.route("/users")
def get_all_users():
    out = {
        "status": "ok",
        "message": "Success",
    }
    users = User.query.all()                                      # returns all users in table
    out["body"] = []                                             # creates an empty list to later fill
    for user in users:                                           # loop for each user in users
        user_dict = {}                                            # temp dict to store each user
        user_dict["id"] = user.id                                  # map each attribute to corresponding key
        user_dict["first_name"] = user.first_name
        user_dict["last_name"] = user.last_name
        user_dict["hobbies"] = user.hobbies
        user_dict["active"] = user.active
        out["body"].append(user_dict)                           # append the temp dict to our body list
    
    return out                                                  # return the list with all our pushed dicts

@app.route("/users/<int:pk>")
def get_single_user(pk):
    out = {
        "status": "ok",
        "message": "Success"
    }
    user = User.query.filter_by(id=pk).first()
    out["body"] = {
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "hobbies": user.hobbies,
            "active": user.active
            }
        }
    return out


@app.route("/users", methods=["POST"])
def create_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    db.session.add(
        User(
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            hobbies=user_data.get("hobbies")
            )
        )
    db.session.commit()
    
    return out, 201


@app.route("/update", methods=["PUT"])
def update_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    out["user_id"] = update(
        user_data.get("id"),
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    return out

@app.route("/delete", methods=["PUT"])
def delete_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    out["user_id"] = delete(
        user_data.get("id")
        )
    return out

@app.route("/agent")
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s" % user_agent

