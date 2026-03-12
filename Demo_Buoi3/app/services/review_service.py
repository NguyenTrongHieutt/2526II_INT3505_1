from app.models import Review
from app import db

def get_reviews():
    return Review.query.all()

def create_review(data):
    review = Review(
        rating=data["rating"],
        comment=data["comment"],
        book_id=data["book_id"],
        user_id=data["user_id"]
    )
    db.session.add(review)
    db.session.commit()
    return review