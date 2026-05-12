import time

from flask import Blueprint, Response, current_app, g, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, CollectorRegistry, generate_latest, multiprocess, ProcessCollector, PlatformCollector

metrics_bp = Blueprint("metrics", __name__)
registry = CollectorRegistry()

try:
    multiprocess.MultiProcessCollector(registry)
except Exception:
    pass

ProcessCollector(registry=registry)
PlatformCollector(registry=registry)

http_requests_total = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "route", "status_code"],
    registry=registry,
)

http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "Duration of HTTP requests in seconds",
    ["method", "route", "status_code"],
    buckets=(0.005, 0.01, 0.05, 0.1, 0.3, 0.5, 1, 3, 5),
    registry=registry,
)


def init_metrics(app):
    @app.before_request
    def start_timer():
        g.start_time = time.perf_counter()

    @app.after_request
    def record_metrics(response):
        route = request.url_rule.rule if request.url_rule else request.path
        status_code = str(response.status_code)
        duration = time.perf_counter() - getattr(g, "start_time", time.perf_counter())

        http_requests_total.labels(
            method=request.method,
            route=route,
            status_code=status_code,
        ).inc()

        http_request_duration_seconds.labels(
            method=request.method,
            route=route,
            status_code=status_code,
        ).observe(duration)

        current_app.logger.info(
            "HTTP request",
            extra={
                "method": request.method,
                "route": route,
                "status_code": status_code,
                "duration_ms": round(duration * 1000, 2),
            },
        )
        return response

    app.register_blueprint(metrics_bp)


@metrics_bp.get("/metrics")
def metrics():
    return Response(generate_latest(registry), mimetype=CONTENT_TYPE_LATEST)
