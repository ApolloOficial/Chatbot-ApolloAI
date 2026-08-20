"""Especificação OpenAPI explícita do contrato público."""


def build_openapi(version: str) -> dict:
    chat_request = {
        "type": "object",
        "required": ["user_id", "session_id", "pergunta"],
        "properties": {
            "user_id": {"type": "string", "example": "tecnico-a8f3"},
            "session_id": {"type": "string", "example": "550e8400-e29b-41d4-a716-446655440000"},
            "pergunta": {"type": "string", "example": "Qual a diferença entre manutenção preditiva e preventiva?"},
            "contexto": {
                "type": "object", "additionalProperties": False,
                "properties": {
                    name: {"type": "string", "maxLength": limit}
                    for name, limit in {
                        "componente": 120, "fabricante": 120, "modelo": 120, "serial": 160,
                        "barcode": 160, "sintoma": 600, "alerta": 600, "medicoes": 1000,
                        "condicao_ambiental": 600, "procedimento_executado": 1000,
                    }.items()
                },
            },
        },
    }
    return {
        "openapi": "3.1.0",
        "info": {"title": "ApolloAI", "version": version, "description": "Orientação técnica sobre ativos fotovoltaicos; não altera o banco operacional do Apollo."},
        "paths": {
            "/chat": {"post": {"summary": "Executa o grafo multiagente", "security": [{"bearerAuth": []}], "parameters": [{"in": "header", "name": "X-User-ID", "schema": {"type": "string"}, "description": "Identidade confiável quando AUTH_REQUIRED=true"}], "requestBody": {"required": True, "content": {"application/json": {"schema": chat_request}}}, "responses": {"200": {"description": "Resposta processada", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/ChatResponse"}}}}, "401": {"description": "Autenticação ou identidade ausente"}, "403": {"description": "Sessão pertence a outro usuário"}, "422": {"description": "Payload inválido"}, "503": {"description": "Dependência essencial indisponível"}}}},
            "/sessions/{session_id}/close": {"post": {"summary": "Encerra e resume uma sessão", "parameters": [{"in": "path", "name": "session_id", "required": True, "schema": {"type": "string"}}], "responses": {"200": {"description": "Sessão encerrada"}, "403": {"description": "Sessão pertence a outro usuário"}}}},
            "/.well-known/agent-card.json": {"get": {"summary": "Publica o Agent Card A2A 1.0", "responses": {"200": {"description": "Capacidades A2A"}}}},
            "/a2a/v1": {"post": {"summary": "Executa SendMessage por A2A JSON-RPC 1.0", "responses": {"200": {"description": "Resposta JSON-RPC"}, "401": {"description": "Autenticação obrigatória"}}}},
            "/health": {"get": {"summary": "Saúde das dependências", "responses": {"200": {"description": "Saudável"}, "503": {"description": "Degradado"}}}},
            "/live": {"get": {"summary": "Vida do processo sem testar dependências", "responses": {"200": {"description": "Processo ativo"}}}},
            "/metrics": {"get": {"summary": "Métricas Prometheus", "responses": {"200": {"description": "Métricas sem PII"}}}},
        },
        "components": {"securitySchemes": {"bearerAuth": {"type": "http", "scheme": "bearer"}}, "schemas": {"ChatResponse": {
            "type": "object", "required": ["session_id", "resposta", "status", "rota", "agentes_chamados", "fontes"],
            "properties": {
                "session_id": {"type": "string"}, "resposta": {"type": "string"},
                "status": {"enum": ["sucesso", "bloqueado", "esclarecimento", "erro"]},
                "rota": {"enum": ["ativos_solares", "manutencao", "seguranca", "faq_apolloai", "fora_escopo"]},
                "agentes_chamados": {"type": "array", "items": {"type": "string"}},
                "fontes": {"type": "array", "items": {"type": "object"}},
                "alerta_seguranca": {"type": ["string", "null"]},
                "motivo_bloqueio": {"type": ["string", "null"]},
            },
        }}},
    }
