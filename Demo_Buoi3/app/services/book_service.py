from app.models import Book
from app import db

def get_books():
    return Book.query.all()

def get_book(book_id):
    return Book.query.get(book_id)

def create_book(data):
    book = Book(title=data["title"], author=data["author"])
    db.session.add(book)
    db.session.commit()
    return book

def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return None
    db.session.delete(book)
    db.session.commit()
    return book