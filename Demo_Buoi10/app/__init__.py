import os

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from app.logging_config import setup_logging
from app.monitoring.metrics import init_metrics

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    os.makedirs(app.instance_path, exist_ok=True)
    os.makedirs(os.path.join(app.root_path, "..", "logs"), exist_ok=True)

    database_path = os.path.join(app.instance_path, "bookstore.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{database_path}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    setup_logging(app)

    from app.routes.books import books_bp
    from app.routes.users import users_bp
    from app.routes.reviews import reviews_bp

    app.register_blueprint(books_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(reviews_bp)

    init_metrics(app)

    @app.get("/health")
    def health_check():
        return jsonify({"status": "ok"})

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify({
            "error": {
                "code": 404,
                "message": "Route not found"
            }
        }), 404

    @app.errorhandler(500)
    def internal_error(_error):
        app.logger.exception("Unhandled server error")
        return jsonify({
            "error": {
                "code": 500,
                "message": "Internal server error"
            }
        }), 500

    return app
