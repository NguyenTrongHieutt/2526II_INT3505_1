from flask import Flask, request, jsonify
from flask_cors import CORS
import time

from db import get_conn, release_conn

app = Flask(__name__)
CORS(app)


def query(sql, params=None):

    conn = get_conn()
    cur = conn.cursor()

    try:
        start = time.time()

        cur.execute(sql, params)
        rows = cur.fetchall()

        end = time.time()

        result = []

        for r in rows:
            result.append({
                "id": r[0],
                "name": r[1],
                "email": r[2]
            })

        return result, round(end - start, 4)

    finally:
        cur.close()
        release_conn(conn)


# =========================
# OFFSET PAGINATION
# =========================
@app.route("/offset")
def offset_pagination():

    limit = int(request.args.get("limit", 20))
    offset_val = int(request.args.get("offset", 0))

    sql = """
    SELECT id, name, email
    FROM users
    ORDER BY id
    LIMIT %s OFFSET %s
    """

    data, time_taken = query(sql, (limit, offset_val))

    return jsonify({
        "type": "offset",
        "offset": offset_val,
        "limit": limit,
        "time": time_taken,
        "data": data
    })


# =========================
# PAGE PAGINATION
# =========================
@app.route("/page")
def page_pagination():

    page = int(request.args.get("page", 1))
    size = int(request.args.get("size", 20))

    offset_val = (page - 1) * size

    sql = """
    SELECT id, name, email
    FROM users
    ORDER BY id
    LIMIT %s OFFSET %s
    """

    data, time_taken = query(sql, (size, offset_val))

    return jsonify({
        "type": "page",
        "page": page,
        "size": size,
        "offset": offset_val,
        "time": time_taken,
        "data": data
    })


# =========================
# CURSOR PAGINATION
# =========================
@app.route("/cursor")
def cursor_pagination():

    cursor = request.args.get("cursor")
    limit = int(request.args.get("limit", 20))

    if cursor:
        cursor = int(cursor)

        sql = """
        SELECT id, name, email
        FROM users
        WHERE id > %s
        ORDER BY id
        LIMIT %s
        """

        params = (cursor, limit)

    else:
        sql = """
        SELECT id, name, email
        FROM users
        ORDER BY id
        LIMIT %s
        """

        params = (limit,)

    data, time_taken = query(sql, params)

    next_cursor = None
    if data:
        next_cursor = data[-1]["id"]

    return jsonify({
        "type": "cursor",
        "cursor": cursor,
        "next_cursor": next_cursor,
        "limit": limit,
        "time": time_taken,
        "data": data
    })


# =========================
# HEALTH CHECK
# =========================
@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)