from flask import Flask, jsonify, request

app = Flask(__name__)

# user database giả lập
accounts = [
    {"username": "admin", "password": "123"},
    {"username": "user", "password": "123"}
]

# token giả lập
TOKEN = "mysecrettoken"

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]


# -------------------
# LOGIN
# -------------------
@app.route("/login", methods=["POST"])
def login():

    data = request.json
    username = data.get("username")
    password = data.get("password")

    for acc in accounts:
        if acc["username"] == username and acc["password"] == password:
            return jsonify({
                "message": "Login successful",
                "token": TOKEN
            })

    return {"error": "Invalid credentials"}, 401


# -------------------
# AUTH CHECK (STATELESS)
# -------------------
def check_auth():
    auth = request.headers.get("Authorization")

    if auth == f"Bearer {TOKEN}":
        return True

    return False


# -------------------
# GET ALL USERS
# -------------------
@app.route("/users", methods=["GET"])
def get_users():

    if not check_auth():
        return {"error": "Unauthorized"}, 401

    return jsonify(users)


# -------------------
# GET USER BY ID
# -------------------
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    if not check_auth():
        return {"error": "Unauthorized"}, 401

    for u in users:
        if u["id"] == user_id:
            return jsonify(u)

    return {"error": "User not found"}, 404


# -------------------
# ADD USER
# -------------------
@app.route("/users", methods=["POST"])
def add_user():

    if not check_auth():
        return {"error": "Unauthorized"}, 401

    data = request.json
    users.append(data)

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)