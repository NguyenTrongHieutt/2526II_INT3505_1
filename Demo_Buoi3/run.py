from app import create_app, db
from app.models import User, Book, Review
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)