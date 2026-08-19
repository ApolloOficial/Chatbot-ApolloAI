"""Guardrails determinísticos e verificações semânticas do ApolloAI."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass


@dataclass(frozen=True)
class GuardrailResult:
    category: str
    blocked: bool
    response: str | None = None


_INJECTION = (
    r"ignore\s+(todas\s+)?(as\s+)?instru", r"desconsidere\s+(suas|as)\s+instru",
    r"system\s*prompt|prompt\s+do\s+sistema", r"jailbreak|modo\s+(dan|irrestrito)",
    r"revele\s+(suas|as)\s+instru",
)
_INTERNAL = (
    "chave de api", "api key", "variavel de ambiente", "variável de ambiente", "credencial",
    "senha do sistema", "token de acesso", "dados de outros usuarios", "dados de outros usuários",
    "mongodb_uri", "groq_api_key", "google_api_key",
)
_OFFENSIVE = ("idiota", "imbecil", "burro", "otario", "otário", "merda", "porra", "fdp")
_OUT_OF_SCOPE = (
    "futebol", "jogo de ontem", "campeonato", "eleicao", "eleição", "presidente",
    "celebridade", "fofoca", "receita de", "filme", "novela", "horoscopo", "horóscopo",
)
_DANGEROUS = (
    "trabalhar energizado", "sem epi", "ignorar epi", "burlar bloqueio", "sem bloquear",
    "desativar protecao", "desativar proteção", "confirmar sem medir", "curto-circuitar",
)
_BLOCK_RESPONSES = {
    "OFENSIVO": "Para continuar, mantenha uma comunicação respeitosa. Posso ajudar com dúvidas sobre ativos fotovoltaicos e manutenção.",
    "FORA_ESCOPO": "O ApolloAI atende somente a dúvidas relacionadas a ativos fotovoltaicos e manutenção. Posso ajudar com alguma questão técnica sobre sistemas solares?",
    "PERIGOSO": "Não posso orientar uma intervenção insegura. Interrompa a atividade e siga os procedimentos internos, bloqueio e etiquetagem e a avaliação de um profissional qualificado.",
    "ILICITO": "Não posso auxiliar com atividades ilícitas. Posso ajudar com orientação segura sobre ativos fotovoltaicos.",
    "PROMPT_INJECTION": "Não posso fornecer nem ignorar instruções internas do sistema. Posso ajudar com dúvidas sobre ativos fotovoltaicos.",
    "DADOS_INTERNOS": "Não posso fornecer credenciais ou informações internas do sistema. Posso ajudar com dúvidas sobre ativos fotovoltaicos.",
}


def normalize(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text.lower())
    return "".join(char for char in decomposed if not unicodedata.combining(char))


def input_guardrail(message: str, semantic_classifier=None) -> GuardrailResult:
    normalized = normalize(message)
    if any(re.search(pattern, normalized, re.I) for pattern in _INJECTION):
        return _blocked("PROMPT_INJECTION")
    if any(normalize(term) in normalized for term in _INTERNAL):
        return _blocked("DADOS_INTERNOS")
    if any(re.search(rf"\b{re.escape(normalize(term))}\b", normalized) for term in _OFFENSIVE):
        return _blocked("OFENSIVO")
    if any(normalize(term) in normalized for term in _DANGEROUS):
        return _blocked("PERIGOSO")
    if any(normalize(term) in normalized for term in _OUT_OF_SCOPE):
        return _blocked("FORA_ESCOPO")
    if semantic_classifier:
        category = semantic_classifier(message)
        if category in {"OFENSIVO", "FORA_ESCOPO", "PERIGOSO", "ILICITO"}:
            return _blocked(category)
    return GuardrailResult("APROVADO", False)


def _blocked(category: str) -> GuardrailResult:
    return GuardrailResult(category, True, _BLOCK_RESPONSES[category])


_PII = (
    (r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b", "[CPF OMITIDO]"),
    (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "[E-MAIL OMITIDO]"),
    (r"(?i)\b(?:sk-|gsk_|AIza)[A-Za-z0-9_-]{12,}\b", "[CREDENCIAL OMITIDA]"),
)
_UNSAFE_OUTPUT = (
    "pode trabalhar energizado", "esta desenergizado", "está desenergizado",
    "dispense o epi", "ignore o procedimento", "garanto que", "diagnostico confirmado",
    "diagnóstico confirmado",
)


def output_guardrail(answer: str, sources: list[dict], technical: bool = True) -> tuple[str, str | None]:
    sanitized = answer
    for pattern, replacement in _PII:
        sanitized = re.sub(pattern, replacement, sanitized)
    unsafe = any(normalize(term) in normalize(sanitized) for term in _UNSAFE_OUTPUT)
    if unsafe:
        return (
            "Não é possível validar essa orientação com segurança. Interrompa a intervenção e siga os procedimentos internos e a avaliação de um profissional qualificado.",
            "Orientação potencialmente insegura bloqueada.",
        )
    if technical and not sources and "não encontrei informações suficientes" not in sanitized.lower():
        return "Não encontrei informações suficientes nas fontes técnicas disponíveis para responder com segurança.", None
    return sanitized.strip(), None
