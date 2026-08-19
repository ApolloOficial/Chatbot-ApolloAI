"""Documento OpenAPI e Swagger UI compatíveis com Flask."""

from flask import Blueprint, current_app, jsonify

docs_bp = Blueprint("docs", __name__)


@docs_bp.get("/openapi.json")
def openapi_spec():
    from app.openapi import build_openapi

    return jsonify(build_openapi(current_app.config["VERSION"]))


@docs_bp.get("/docs")
def swagger_ui():
    return """<!doctype html><html lang=\"pt-BR\"><head><title>ApolloAI API</title>
<link rel=\"stylesheet\" href=\"https://unpkg.com/swagger-ui-dist@5/swagger-ui.css\"></head>
<body><div id=\"swagger-ui\"></div><script src=\"https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js\"></script>
<script>SwaggerUIBundle({url:'/openapi.json',dom_id:'#swagger-ui'});</script></body></html>"""
