from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(200))
    year = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year
        }


@app.before_first_request
def create_tables():
    db.create_all()

    if Book.query.count() == 0:
        books = [
            Book(title="Clean Code", author="Robert C. Martin", year=2008),
            Book(title="Fluent Python", author="Luciano Ramalho", year=2015),
            Book(title="Python Crash Course", author="Eric Matthes", year=2019),
            Book(title="Deep Learning", author="Ian Goodfellow", year=2016),
            Book(title="Design Patterns", author="Erich Gamma", year=1994),
            Book(title="Effective Python", author="Brett Slatkin", year=2015),
        ]

        db.session.bulk_save_objects(books)
        db.session.commit()


@app.route("/books", methods=["GET"])
def get_books():

    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 3, type=int)

    query = Book.query

    if search:
        query = query.filter(
            (Book.title.ilike(f"%{search}%")) |
            (Book.author.ilike(f"%{search}%"))
        )

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "total": pagination.total,
        "page": page,
        "per_page": per_page,
        "pages": pagination.pages,
        "data": [book.to_dict() for book in pagination.items]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)