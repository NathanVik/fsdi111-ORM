from datetime import datetime
from flask import Flask, request

from app.database import delete, scan, read, insert, update, delete

app = Flask(__name__)


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
    out["body"] = scan()
    return out

@app.route("/users/<int:pk>")
def get_single_user(pk):
    out = {
        "status": "ok",
        "message": "Success"
    }
    out["body"] = read(pk)
    return out


@app.route("/users", methods=["POST"])
def create_user():
    out = {
        "status": "ok",
        "message": "Success"
    }
    user_data = request.json
    out["user_id"] = insert(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
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

