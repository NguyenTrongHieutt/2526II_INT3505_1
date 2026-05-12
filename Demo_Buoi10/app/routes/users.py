from flask import Blueprint, request

from app.services.user_service import create_user, delete_user, get_user, get_users
from app.utils.response import error_response, success_response

users_bp = Blueprint("users", __name__, url_prefix="/api/v1/users")


@users_bp.get("")
def list_users():
    users = get_users()
    return success_response([user.to_dict() for user in users])


@users_bp.get("/<int:user_id>")
def get_user_by_id(user_id):
    user = get_user(user_id)
    if not user:
        return error_response("User not found", 404)
    return success_response(user.to_dict())


@users_bp.post("")
def create_new_user():
    data = request.get_json(silent=True) or {}
    if not data.get("username") or not data.get("email"):
        return error_response("username and email are required", 400)
    user = create_user(data)
    return success_response(user.to_dict(), 201)


@users_bp.delete("/<int:user_id>")
def remove_user(user_id):
    user = delete_user(user_id)
    if not user:
        return error_response("User not found", 404)
    return success_response(None, 204)
