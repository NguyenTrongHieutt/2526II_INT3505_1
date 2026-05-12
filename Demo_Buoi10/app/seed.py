from app import db
from app.models import Book, Review, User


def seed_database():
    if User.query.first() or Book.query.first() or Review.query.first():
        return

    users = [
        User(username="alice", email="alice@example.com"),
        User(username="bob", email="bob@example.com"),
    ]

    books = [
        Book(title="Clean Code", author="Robert C. Martin"),
        Book(title="The Pragmatic Programmer", author="Andrew Hunt"),
    ]

    db.session.add_all(users + books)
    db.session.commit()

    reviews = [
        Review(rating=5, comment="Great book", book_id=books[0].id, user_id=users[0].id),
        Review(rating=4, comment="Very useful", book_id=books[1].id, user_id=users[1].id),
    ]

    db.session.add_all(reviews)
    db.session.commit()
