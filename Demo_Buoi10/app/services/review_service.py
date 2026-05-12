from app import db
from app.models import Review


def get_reviews():
    return Review.query.all()


def get_review(review_id):
    return Review.query.get(review_id)


def create_review(data):
    review = Review(
        rating=data["rating"],
        comment=data["comment"],
        book_id=data["book_id"],
        user_id=data["user_id"],
    )
    db.session.add(review)
    db.session.commit()
    return review
