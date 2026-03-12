from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bookstore.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.books import books_bp
    from app.routes.users import users_bp
    from app.routes.reviews import reviews_bp

    app.register_blueprint(books_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(reviews_bp)

    return app