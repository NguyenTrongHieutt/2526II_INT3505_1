import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging(app):
    logs_dir = os.path.abspath(os.path.join(app.root_path, "..", "logs"))
    os.makedirs(logs_dir, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s [method=%(method)s route=%(route)s status=%(status_code)s duration_ms=%(duration_ms)s]",
        defaults={
            "method": "-",
            "route": "-",
            "status_code": "-",
            "duration_ms": "-",
        }
    )

    file_handler = RotatingFileHandler(
        os.path.join(logs_dir, "app.log"),
        maxBytes=1_000_000,
        backupCount=3,
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    app.logger.handlers.clear()
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)
