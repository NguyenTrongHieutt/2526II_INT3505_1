from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, Optional

from bson import ObjectId
from fastapi import HTTPException

from openapi_server.apis.default_api_base import BaseDefaultApi
from openapi_server.db import get_database
from openapi_server.models.book import Book
from openapi_server.models.book_input import BookInput
from openapi_server.models.book_response import BookResponse
from openapi_server.models.books_response import BooksResponse
from openapi_server.models.meta import Meta
from openapi_server.models.review import Review
from openapi_server.models.review_input import ReviewInput
from openapi_server.models.review_response import ReviewResponse
from openapi_server.models.reviews_response import ReviewsResponse
from openapi_server.models.user import User
from openapi_server.models.user_input import UserInput
from openapi_server.models.user_response import UserResponse
from openapi_server.models.users_response import UsersResponse


class DefaultApiImpl(BaseDefaultApi):
    def __init__(self) -> None:
        self.db = get_database()
        self.books = self.db["books"]
        self.users = self.db["users"]
        self.reviews = self.db["reviews"]

    @staticmethod
    def _meta() -> Meta:
        return Meta(timestamp=datetime.now(timezone.utc).isoformat())

    @staticmethod
    def _string_id(value: Any) -> str:
        return str(value)

    @staticmethod
    def _doc_to_book(document: Dict[str, Any]) -> Book:
        return Book.from_dict(
            {
                "id": DefaultApiImpl._string_id(document["_id"]),
                "title": document.get("title"),
                "author": document.get("author"),
            }
        )

    @staticmethod
    def _doc_to_user(document: Dict[str, Any]) -> User:
        return User.from_dict(
            {
                "id": DefaultApiImpl._string_id(document["_id"]),
                "username": document.get("username"),
                "email": document.get("email"),
            }
        )

    @staticmethod
    def _doc_to_review(document: Dict[str, Any]) -> Review:
        return Review.from_dict(
            {
                "id": DefaultApiImpl._string_id(document["_id"]),
                "rating": document.get("rating"),
                "comment": document.get("comment"),
                "book_id": document.get("book_id"),
                "user_id": document.get("user_id"),
            }
        )

    @staticmethod
    def _parse_object_id(identifier: str, entity_name: str) -> ObjectId:
        if not ObjectId.is_valid(identifier):
            raise HTTPException(status_code=404, detail=f"{entity_name} not found")
        return ObjectId(identifier)

    async def api_v1_books_get(self) -> BooksResponse:
        documents = list(self.books.find().sort("_id", -1))
        return BooksResponse(data=[self._doc_to_book(document) for document in documents], meta=self._meta())

    async def api_v1_books_post(self, book_input: BookInput) -> BookResponse:
        payload = book_input.model_dump()
        result = self.books.insert_one(payload)
        document = self.books.find_one({"_id": result.inserted_id})
        return BookResponse(data=self._doc_to_book(document), meta=self._meta())

    async def api_v1_books_book_id_get(self, book_id: str) -> BookResponse:
        object_id = self._parse_object_id(book_id, "Book")
        document = self.books.find_one({"_id": object_id})
        if not document:
            raise HTTPException(status_code=404, detail="Book not found")
        return BookResponse(data=self._doc_to_book(document), meta=self._meta())

    async def api_v1_books_book_id_delete(self, book_id: str) -> None:
        object_id = self._parse_object_id(book_id, "Book")
        result = self.books.delete_one({"_id": object_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Book not found")
        return None

    async def api_v1_users_get(self) -> UsersResponse:
        documents = list(self.users.find().sort("_id", -1))
        return UsersResponse(data=[self._doc_to_user(document) for document in documents], meta=self._meta())

    async def api_v1_users_post(self, user_input: UserInput) -> UserResponse:
        existing_user = self.users.find_one({"email": user_input.email})
        if existing_user:
            raise HTTPException(status_code=409, detail="Email already exists")

        payload = user_input.model_dump()
        result = self.users.insert_one(payload)
        document = self.users.find_one({"_id": result.inserted_id})
        return UserResponse(data=self._doc_to_user(document), meta=self._meta())

    async def api_v1_users_user_id_get(self, user_id: str) -> UserResponse:
        object_id = self._parse_object_id(user_id, "User")
        document = self.users.find_one({"_id": object_id})
        if not document:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse(data=self._doc_to_user(document), meta=self._meta())

    async def api_v1_users_user_id_delete(self, user_id: str) -> None:
        object_id = self._parse_object_id(user_id, "User")
        result = self.users.delete_one({"_id": object_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return None

    async def api_v1_book_reviews_get(self) -> ReviewsResponse:
        documents = list(self.reviews.find().sort("_id", -1))
        return ReviewsResponse(data=[self._doc_to_review(document) for document in documents], meta=self._meta())

    async def api_v1_book_reviews_post(self, review_input: ReviewInput) -> ReviewResponse:
        book_object_id = self._parse_object_id(review_input.book_id, "Book")
        user_object_id = self._parse_object_id(review_input.user_id, "User")

        if not self.books.find_one({"_id": book_object_id}):
            raise HTTPException(status_code=404, detail="Book not found")
        if not self.users.find_one({"_id": user_object_id}):
            raise HTTPException(status_code=404, detail="User not found")

        payload = review_input.model_dump()
        result = self.reviews.insert_one(payload)
        document = self.reviews.find_one({"_id": result.inserted_id})
        return ReviewResponse(data=self._doc_to_review(document), meta=self._meta())

    async def api_v1_book_reviews_review_id_get(self, review_id: str) -> ReviewResponse:
        object_id = self._parse_object_id(review_id, "Review")
        document = self.reviews.find_one({"_id": object_id})
        if not document:
            raise HTTPException(status_code=404, detail="Review not found")
        return ReviewResponse(data=self._doc_to_review(document), meta=self._meta())

    async def api_v1_book_reviews_review_id_delete(self, review_id: str) -> None:
        object_id = self._parse_object_id(review_id, "Review")
        result = self.reviews.delete_one({"_id": object_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Review not found")
        return None
