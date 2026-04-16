from __future__ import annotations

import os
from functools import lru_cache
from typing import Optional

from pymongo import MongoClient
from pymongo.database import Database

DEFAULT_MONGO_URI = "mongodb://127.0.0.1:27017/book_management"
DEFAULT_DB_NAME = "book_management"


@lru_cache(maxsize=1)
def get_client() -> MongoClient:
    mongo_uri = os.getenv("MONGO_URI", DEFAULT_MONGO_URI)
    return MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)


def get_database() -> Database:
    mongo_uri = os.getenv("MONGO_URI", DEFAULT_MONGO_URI)
    database_name = os.getenv("MONGO_DB_NAME")
    if database_name:
        return get_client()[database_name]

    if "/" in mongo_uri.rsplit("/", 1)[-1]:
        # Fallback for URIs like mongodb://host:port/database
        inferred_name = mongo_uri.rsplit("/", 1)[-1].split("?", 1)[0]
        if inferred_name:
            return get_client()[inferred_name]

    return get_client()[DEFAULT_DB_NAME]
