from app.models import User
from app import db

def get_users():
    return User.query.all()

def create_user(data):
    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return user