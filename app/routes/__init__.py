"""Registro central dos Blueprints Flask."""

from flask import Flask


def register_blueprints(app: Flask) -> None:
    from app.routes.a2a import a2a_bp
    from app.routes.chat import chat_bp
    from app.routes.health import health_bp
    from app.routes.metrics import metrics_bp
    from app.routes.openapi import docs_bp

    app.register_blueprint(a2a_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(metrics_bp)
    app.register_blueprint(docs_bp)
