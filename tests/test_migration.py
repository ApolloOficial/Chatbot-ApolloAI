from __future__ import annotations

import importlib
from pathlib import Path

from app import create_app

ROOT = Path(__file__).resolve().parents[1]


def _project_text() -> str:
    files = [*ROOT.glob("app/**/*.py"), ROOT / "wsgi.py", ROOT / "requirements.txt"]
    return "\n".join(path.read_text(encoding="utf-8") for path in files if path.is_file() and ".git" not in path.parts)


def test_no_fastapi_import_or_dependency():
    text = _project_text().lower()
    assert "from fastapi" not in text
    assert "import fastapi" not in text
    requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8").lower()
    assert "fastapi" not in requirements


def test_application_factory_and_blueprints():
    app = create_app({"TESTING": True})
    assert callable(create_app)
    assert {"chat", "health", "metrics", "docs"}.issubset(app.blueprints)


def test_wsgi_imports_application():
    module = importlib.import_module("wsgi")
    assert module.app.name == "app"


def test_no_postgresql_runtime_code():
    text = _project_text().lower()
    assert "psycopg2" not in text
    assert "database_url" not in text
    assert "postgresql" not in (ROOT / "requirements.txt").read_text(encoding="utf-8").lower()


def test_legacy_financial_and_agenda_identity_removed():
    source_files = [path for path in [*ROOT.glob("app/**/*.py"), *ROOT.glob("frontend/*")] if path.is_file()]
    text = "\n".join(path.read_text(encoding="utf-8") for path in source_files).lower()
    for legacy in ("assessor.ai", "assessor financeiro", "cvm", "anbima", "transação financeira", "agenda pessoal"):
        assert legacy not in text


def test_internal_errors_do_not_expose_traceback(client, monkeypatch):
    from app.services import chat_service

    monkeypatch.setattr(chat_service.ChatService, "execute", lambda *_: (_ for _ in ()).throw(RuntimeError("segredo interno")))
    response = client.post("/chat", json={
        "user_id": "tecnico-001", "session_id": "session-0001", "pergunta": "Olá", "contexto": {},
    })
    assert response.status_code == 500
    assert "traceback" not in response.get_data(as_text=True).lower()
    assert "segredo interno" not in response.get_data(as_text=True).lower()
