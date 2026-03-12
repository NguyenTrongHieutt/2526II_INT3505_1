from flask import Blueprint, request
from app.services.book_service import *
from app.utils.response import success_response, error_response

books_bp = Blueprint(
    "books",
    __name__,
    url_prefix="/api/v1/books"
)


@books_bp.route("", methods=["GET"])
def list_books():

    books = get_books()

    data = [
        {"id": b.id, "title": b.title, "author": b.author}
        for b in books
    ]

    return success_response(data)


@books_bp.route("/<int:book_id>", methods=["GET"])
def get_book_by_id(book_id):

    book = get_book(book_id)

    if not book:
        return error_response("Book not found", 404)

    data = {
        "id": book.id,
        "title": book.title,
        "author": book.author
    }

    return success_response(data)


@books_bp.route("", methods=["POST"])
def create_new_book():

    data = request.json
    book = create_book(data)

    response_data = {
        "id": book.id,
        "title": book.title,
        "author": book.author
    }

    return success_response(response_data, 201)


@books_bp.route("/<int:book_id>", methods=["DELETE"])
def remove_book(book_id):

    book = delete_book(book_id)

    if not book:
        return error_response("Book not found", 404)

    return success_response(None, 204)