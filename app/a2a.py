"""Contratos e adaptação A2A 1.0 para o caso de uso conversacional."""

from __future__ import annotations

from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.schemas import ChatRequest

A2A_VERSION = "1.0"


class A2APart(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str | None = Field(None, min_length=1, max_length=4000)
    data: Any | None = None
    url: str | None = None
    raw: str | None = None
    mediaType: str | None = None
    filename: str | None = None
    metadata: dict[str, Any] | None = None

    @model_validator(mode="after")
    def exactly_one_content(self):
        if sum(value is not None for value in (self.text, self.data, self.url, self.raw)) != 1:
            raise ValueError("Cada part deve conter exatamente um entre text, data, url ou raw.")
        return self


class A2AMessage(BaseModel):
    model_config = ConfigDict(extra="forbid")
    messageId: str = Field(min_length=1, max_length=128)
    contextId: str | None = Field(None, min_length=8, max_length=128, pattern=r"^[A-Za-z0-9_.:-]+$")
    taskId: str | None = None
    role: Literal["ROLE_USER"]
    parts: list[A2APart] = Field(min_length=1, max_length=8)
    metadata: dict[str, Any] = Field(default_factory=dict)
    extensions: list[str] = Field(default_factory=list)
    referenceTaskIds: list[str] = Field(default_factory=list)


class SendMessageConfiguration(BaseModel):
    model_config = ConfigDict(extra="forbid")
    acceptedOutputModes: list[str] = Field(default_factory=list)
    historyLength: int | None = Field(None, ge=0, le=100)
    returnImmediately: bool = False


class SendMessageParams(BaseModel):
    model_config = ConfigDict(extra="forbid")
    message: A2AMessage
    configuration: SendMessageConfiguration = Field(default_factory=SendMessageConfiguration)
    metadata: dict[str, Any] = Field(default_factory=dict)

    def to_chat_request(self, trusted_identity: str | None) -> ChatRequest:
        text_parts = [part.text for part in self.message.parts if part.text is not None]
        if len(text_parts) != len(self.message.parts):
            raise ValueError("O ApolloAI aceita somente parts textuais.")
        accepted = self.configuration.acceptedOutputModes
        if accepted and "text/plain" not in accepted and "application/json" not in accepted:
            raise ValueError("Nenhum modo de saída compatível foi solicitado.")
        metadata = {**self.metadata, **self.message.metadata}
        user_id = trusted_identity or metadata.get("userId")
        session_id = self.message.contextId or str(uuid4())
        return ChatRequest.model_validate({
            "user_id": user_id,
            "session_id": session_id,
            "pergunta": "\n".join(text_parts),
            "contexto": metadata.get("contexto", {}),
        })


def agent_card(base_url: str, version: str, authentication_required: bool) -> dict[str, Any]:
    card: dict[str, Any] = {
        "name": "ApolloAI",
        "description": "Agente técnico para orientação fundamentada sobre ativos fotovoltaicos, manutenção e segurança.",
        "supportedInterfaces": [{
            "url": f"{base_url.rstrip('/')}/a2a/v1",
            "protocolBinding": "JSONRPC",
            "protocolVersion": A2A_VERSION,
        }],
        "version": version,
        "documentationUrl": f"{base_url.rstrip('/')}/docs",
        "capabilities": {"streaming": False, "pushNotifications": False, "extendedAgentCard": False},
        "defaultInputModes": ["text/plain", "application/json"],
        "defaultOutputModes": ["text/plain", "application/json"],
        "skills": [
            {
                "id": "solar-asset-guidance", "name": "Orientação sobre ativos solares",
                "description": "Explica componentes e condições de ativos fotovoltaicos com fontes recuperadas.",
                "tags": ["fotovoltaico", "ativos", "RAG", "fontes"],
                "examples": ["Quais fatores podem reduzir a eficiência de um módulo fotovoltaico?"],
            },
            {
                "id": "solar-maintenance-safety", "name": "Manutenção e segurança solar",
                "description": "Organiza hipóteses e próximos passos seguros sem substituir procedimentos internos.",
                "tags": ["manutenção", "segurança", "diagnóstico"],
                "examples": ["Como verificar uma anomalia com segurança?"],
            },
        ],
    }
    if authentication_required:
        card["securitySchemes"] = {
            "apolloBearer": {"httpAuthSecurityScheme": {
                "scheme": "Bearer", "bearerFormat": "opaque",
                "description": "Token do serviço Apollo; a identidade final é propagada em X-User-ID.",
            }}
        }
        card["securityRequirements"] = [{"schemes": {"apolloBearer": {"list": []}}}]
    return card


def response_message(chat_response, context_id: str) -> dict[str, Any]:
    return {
        "messageId": str(uuid4()),
        "contextId": context_id,
        "role": "ROLE_AGENT",
        "parts": [
            {"text": chat_response.resposta, "mediaType": "text/plain"},
            {"data": {
                "status": chat_response.status,
                "route": chat_response.rota,
                "sources": [source.model_dump(mode="json") for source in chat_response.fontes],
                "safetyAlert": chat_response.alerta_seguranca,
            }, "mediaType": "application/json"},
        ],
    }
