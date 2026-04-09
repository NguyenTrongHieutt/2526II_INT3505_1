import psycopg2
from psycopg2.pool import SimpleConnectionPool
import time
import os

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "pagination")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

pool = None


def init_pool():
    global pool

    retries = 20

    while retries > 0:
        try:
            print("Connecting to database...")

            pool = SimpleConnectionPool(
                1,
                10,
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )

            print("Database connected!")
            return

        except Exception as e:
            print("Database not ready, retrying...", e)
            retries -= 1
            time.sleep(2)

    raise Exception("Could not connect to database")


def get_conn():
    global pool

    if pool is None:
        init_pool()

    return pool.getconn()


def release_conn(conn):
    pool.putconn(conn)