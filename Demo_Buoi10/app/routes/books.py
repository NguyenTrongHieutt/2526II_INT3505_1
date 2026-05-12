from flask import Blueprint, request

from app.services.book_service import create_book, delete_book, get_book, get_books
from app.utils.response import error_response, success_response

books_bp = Blueprint("books", __name__, url_prefix="/api/v1/books")


@books_bp.get("")
def list_books():
    books = get_books()
    return success_response([book.to_dict() for book in books])


@books_bp.get("/<int:book_id>")
def get_book_by_id(book_id):
    book = get_book(book_id)
    if not book:
        return error_response("Book not found", 404)
    return success_response(book.to_dict())


@books_bp.post("")
def create_new_book():
    data = request.get_json(silent=True) or {}
    if not data.get("title") or not data.get("author"):
        return error_response("title and author are required", 400)
    book = create_book(data)
    return success_response(book.to_dict(), 201)


@books_bp.delete("/<int:book_id>")
def remove_book(book_id):
    book = delete_book(book_id)
    if not book:
        return error_response("Book not found", 404)
    return success_response(None, 204)
