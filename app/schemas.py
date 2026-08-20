"""Contratos de entrada, saída e estado estruturado do ApolloAI."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class AssetContext(BaseModel):
    model_config = ConfigDict(extra="forbid")
    componente: str | None = Field(None, max_length=120)
    fabricante: str | None = Field(None, max_length=120)
    modelo: str | None = Field(None, max_length=120)
    serial: str | None = Field(None, max_length=160)
    barcode: str | None = Field(None, max_length=160)
    sintoma: str | None = Field(None, max_length=600)
    alerta: str | None = Field(None, max_length=600)
    medicoes: str | None = Field(None, max_length=1000)
    condicao_ambiental: str | None = Field(None, max_length=600)
    procedimento_executado: str | None = Field(None, max_length=1000)


class ChatRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    user_id: str = Field(min_length=3, max_length=128, pattern=r"^[A-Za-z0-9_.:@-]+$")
    session_id: str = Field(min_length=8, max_length=128, pattern=r"^[A-Za-z0-9_.:-]+$")
    pergunta: str = Field(min_length=1, max_length=4000)
    contexto: AssetContext = Field(default_factory=AssetContext)

    @field_validator("user_id")
    @classmethod
    def reject_direct_personal_identifier(cls, value: str) -> str:
        if "@" in value and "." in value.split("@")[-1]:
            raise ValueError("Use um identificador pseudonimizado, não um e-mail.")
        return value


class SessionCloseRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    user_id: str = Field(min_length=3, max_length=128, pattern=r"^[A-Za-z0-9_.:@-]+$")

    @field_validator("user_id")
    @classmethod
    def reject_direct_personal_identifier(cls, value: str) -> str:
        if "@" in value and "." in value.split("@")[-1]:
            raise ValueError("Use um identificador pseudonimizado, não um e-mail.")
        return value


class SourceReference(BaseModel):
    documento: str
    pagina: int | None = None
    secao: str | None = None
    url: str | None = None
    trecho: str | None = None
    score: float | None = None


class JudgeDecision(BaseModel):
    decisao: Literal["aprovada", "corrigir", "rejeitada"]
    fundamentada: bool
    segura: bool
    dentro_escopo: bool
    fontes_validas: bool
    hipotese_como_diagnostico: bool = False
    motivos: list[str] = Field(default_factory=list)
    resposta_corrigida: str | None = None


class ChatResponse(BaseModel):
    session_id: str
    resposta: str
    status: Literal["sucesso", "bloqueado", "esclarecimento", "erro"]
    rota: Literal["ativos_solares", "manutencao", "seguranca", "faq_apolloai", "fora_escopo"]
    agentes_chamados: list[str] = Field(default_factory=list)
    fontes: list[SourceReference] = Field(default_factory=list)
    alerta_seguranca: str | None = None
    motivo_bloqueio: str | None = None


def public_validation_errors(errors: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [{"campo": ".".join(map(str, item["loc"])), "mensagem": item["msg"]} for item in errors]
