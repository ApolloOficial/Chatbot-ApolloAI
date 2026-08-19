"""Application factory do ApolloAI."""

from __future__ import annotations

import logging
from pathlib import Path

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from pydantic import ValidationError

from app.config import Config
from app.extensions import init_extensions
from app.routes import register_blueprints


def create_app(config: type[Config] | dict | None = None) -> Flask:
    """Cria e configura uma instância Flask sem efeitos externos no import."""
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)
    if isinstance(config, dict):
        app.config.update(config)
    elif config is not None:
        app.config.from_object(config)

    logging.basicConfig(
        level=app.config["LOG_LEVEL"],
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    CORS(
        app,
        origins=app.config["CORS_ORIGINS"],
        methods=["GET", "POST", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"],
    )
    init_extensions(app)
    register_blueprints(app)
    _register_error_handlers(app)
    _register_test_frontend(app)
    return app


def _register_error_handlers(app: Flask) -> None:
    @app.errorhandler(ValidationError)
    def handle_validation_error(error: ValidationError):
        return jsonify({"status": "erro", "erro": "Payload inválido.", "detalhes": error.errors(include_url=False)}), 422

    @app.errorhandler(404)
    def handle_not_found(_error):
        return jsonify({"status": "erro", "erro": "Recurso não encontrado."}), 404

    @app.errorhandler(413)
    def handle_too_large(_error):
        return jsonify({"status": "erro", "erro": "Payload excede o limite permitido."}), 413

    @app.errorhandler(Exception)
    def handle_unexpected(error: Exception):
        app.logger.exception("erro_nao_tratado", extra={"error_type": type(error).__name__})
        return jsonify({"status": "erro", "erro": "Erro interno controlado."}), 500


def _register_test_frontend(app: Flask) -> None:
    frontend_dir = Path(app.config["FRONTEND_DIR"])
    if not frontend_dir.is_dir():
        return

    @app.get("/")
    def local_test_interface():
        return send_from_directory(frontend_dir, "index.html")

    @app.get("/<path:filename>")
    def local_test_asset(filename: str):
        return send_from_directory(frontend_dir, filename)
