from datetime import datetime

from flask import jsonify


def success_response(data=None, status=200, meta=None):
    response = {
        "data": data,
        "meta": meta or {
            "timestamp": datetime.utcnow().isoformat()
        }
    }

    return jsonify(response), status


def error_response(message, status=400, code=None):
    response = {
        "error": {
            "code": code or status,
            "message": message,
        },
        "meta": {
            "timestamp": datetime.utcnow().isoformat()
        }
    }

    return jsonify(response), status
