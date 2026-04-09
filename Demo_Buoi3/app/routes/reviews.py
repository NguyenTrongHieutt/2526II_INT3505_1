from flask import Blueprint, request
from app.services.review_service import *
from app.models import Review
from app import db
from app.utils.response import success_response, error_response

reviews_bp = Blueprint(
    "reviews",
    __name__,
    url_prefix="/api/v1/book-reviews"
)


@reviews_bp.route("", methods=["GET"])
def list_reviews():

    reviews = get_reviews()

    data = [
        {
            "id": r.id,
            "rating": r.rating,
            "comment": r.comment,
            "book_id": r.book_id,
            "user_id": r.user_id
        }
        for r in reviews
    ]

    return success_response(data)


@reviews_bp.route("/<int:review_id>", methods=["GET"])
def get_review(review_id):

    review = Review.query.get(review_id)

    if not review:
        return error_response("Review not found", 404)

    data = {
        "id": review.id,
        "rating": review.rating,
        "comment": review.comment,
        "book_id": review.book_id,
        "user_id": review.user_id
    }

    return success_response(data)


@reviews_bp.route("", methods=["POST"])
def create_new_review():

    data = request.json
    review = create_review(data)

    response_data = {
        "id": review.id,
        "rating": review.rating,
        "comment": review.comment,
        "book_id": review.book_id,
        "user_id": review.user_id
    }

    return success_response(response_data, 201)


@reviews_bp.route("/<int:review_id>", methods=["DELETE"])
def delete_review(review_id):

    review = Review.query.get(review_id)

    if not review:
        return error_response("Review not found", 404)

    db.session.delete(review)
    db.session.commit()

    return success_response(None, 204)