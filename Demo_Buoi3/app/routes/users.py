from flask import Blueprint, request
from app.services.user_service import *
from app.models import User
from app import db
from app.utils.response import success_response, error_response

users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/api/v1/users"
)


@users_bp.route("", methods=["GET"])
def list_users():

    users = get_users()

    data = [
        {"id": u.id, "username": u.username, "email": u.email}
        for u in users
    ]

    return success_response(data)


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):

    user = User.query.get(user_id)

    if not user:
        return error_response("User not found", 404)

    data = {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }

    return success_response(data)


@users_bp.route("", methods=["POST"])
def create_new_user():

    data = request.json
    user = create_user(data)

    response_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }

    return success_response(response_data, 201)


@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    user = User.query.get(user_id)

    if not user:
        return error_response("User not found", 404)

    db.session.delete(user)
    db.session.commit()

    return success_response(None, 204)