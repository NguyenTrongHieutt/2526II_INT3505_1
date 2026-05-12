from app import db
from app.models import User


def get_users():
    return User.query.all()


def get_user(user_id):
    return User.query.get(user_id)


def create_user(data):
    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return user


def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return None
    db.session.delete(user)
    db.session.commit()
    return user
