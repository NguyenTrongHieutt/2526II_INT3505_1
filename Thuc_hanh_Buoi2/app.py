from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for u in users:
        if u["id"] == user_id:
            return jsonify(u)
    return {"error": "User not found"}, 404

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    users.append(data)
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)