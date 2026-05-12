from flask import Blueprint, request

from app.services.review_service import create_review, get_review, get_reviews
from app.utils.response import error_response, success_response

reviews_bp = Blueprint("reviews", __name__, url_prefix="/api/v1/book-reviews")


@reviews_bp.get("")
def list_reviews():
    reviews = get_reviews()
    return success_response([review.to_dict() for review in reviews])


@reviews_bp.get("/<int:review_id>")
def get_review_by_id(review_id):
    review = get_review(review_id)
    if not review:
        return error_response("Review not found", 404)
    return success_response(review.to_dict())


@reviews_bp.post("")
def create_new_review():
    data = request.get_json(silent=True) or {}
    required_fields = ["rating", "comment", "book_id", "user_id"]
    if any(field not in data for field in required_fields):
        return error_response(
            "rating, comment, book_id and user_id are required",
            400,
        )
    review = create_review(data)
    return success_response(review.to_dict(), 201)
