from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # cho phép tất cả origin
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
# GET ALL USERS (Cacheable)
# -------------------
@app.route("/users", methods=["GET"])
def get_users():

    if not check_auth():
        return {"error": "Unauthorized"}, 401
    print("API called")
    response = make_response(jsonify(users))

    # Cache trong 60 giây
    response.headers["Cache-Control"] = "private, max-age=60"

    return response


# -------------------
# GET USER BY ID (Cacheable)
# -------------------
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    if not check_auth():
        return {"error": "Unauthorized"}, 401
    print("API called")
    for u in users:
        if u["id"] == user_id:

            response = make_response(jsonify(u))

            # Cache 60 giây
            response.headers["Cache-Control"] = "private, max-age=60"

            return response

    return {"error": "User not found"}, 404


# -------------------
# ADD USER (không cache)
# -------------------
@app.route("/users", methods=["POST"])
def add_user():

    if not check_auth():
        return {"error": "Unauthorized"}, 401
    print("API called")
    data = request.json
    users.append(data)

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)