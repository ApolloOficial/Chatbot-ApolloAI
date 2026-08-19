"""Especificação OpenAPI explícita do contrato público."""


def build_openapi(version: str) -> dict:
    chat_request = {
        "type": "object",
        "required": ["user_id", "session_id", "pergunta"],
        "properties": {
            "user_id": {"type": "string", "example": "tecnico-a8f3"},
            "session_id": {"type": "string", "example": "550e8400-e29b-41d4-a716-446655440000"},
            "pergunta": {"type": "string", "example": "Qual a diferença entre manutenção preditiva e preventiva?"},
            "contexto": {"type": "object", "additionalProperties": False},
        },
    }
    return {
        "openapi": "3.1.0",
        "info": {"title": "ApolloAI", "version": version, "description": "Orientação técnica sobre ativos fotovoltaicos; não altera o banco operacional do Apollo."},
        "paths": {
            "/chat": {"post": {"summary": "Executa o grafo multiagente", "requestBody": {"required": True, "content": {"application/json": {"schema": chat_request}}}, "responses": {"200": {"description": "Resposta processada"}, "422": {"description": "Payload inválido"}, "503": {"description": "Dependência essencial indisponível"}}}},
            "/health": {"get": {"summary": "Saúde das dependências", "responses": {"200": {"description": "Saudável"}, "503": {"description": "Degradado"}}}},
            "/metrics": {"get": {"summary": "Métricas Prometheus", "responses": {"200": {"description": "Métricas sem PII"}}}},
        },
    }
