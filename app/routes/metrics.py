"""Métricas Prometheus sem identificadores pessoais."""

from flask import Blueprint, current_app, Response

metrics_bp = Blueprint("metrics", __name__)


@metrics_bp.get("/metrics")
def metrics():
    registry = current_app.extensions["metrics"]
    return Response(registry.render_prometheus(), mimetype="text/plain; version=0.0.4")
