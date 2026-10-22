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
    r"esqueca\s+(tudo|todas?|suas?)\s+(as\s+)?(regras|instru)",
    r"finja\s+(que|ser)\b", r"a\s+partir\s+de\s+agora\s+voce\s+(e|sera|deve)\b",
    r"ignore\s+(all|any|previous|prior|the|your)\s+(previous\s+|prior\s+)?(instructions|rules)",
    r"developer\s+mode|modo\s+desenvolvedor", r"reveal\s+.{0,30}(prompt|instructions)",
    r"repita\s+(tudo|o\s+texto)\s+acima",
)
_INTERNAL = (
    "chave de api", "api key", "variavel de ambiente", "variável de ambiente", "credencial",
    "senha do sistema", "token de acesso", "dados de outros usuarios", "dados de outros usuários",
    "mongodb_uri", "groq_api_key", "google_api_key",
)
_OFFENSIVE = ("idiota", "imbecil", "burro", "otario", "otário", "fdp")
_OUT_OF_SCOPE = (
    "futebol", "jogo de ontem", "campeonato", "eleicao", "eleição", "presidente da republica",
    "celebridade", "fofoca", "novela", "horoscopo", "horóscopo",
)
_DANGEROUS = (
    r"trabalhar\s+energizad", r"\bsem\s+(usar\s+)?(o\s+)?epis?\b",
    r"\b(ignorar|ignore|dispensar|dispense)\s+(o\s+|os\s+)?epis?\b",
    r"burlar\s+(o\s+)?bloqueio", r"\b(pular|pule)\s+(o\s+)?bloqueio\b", r"\bsem\s+bloquear\b",
    r"desativar\s+(a\s+)?protec", r"confirmar\s+sem\s+medir", r"curto-?circuitar",
)
_DOMAIN = re.compile(
    r"\b(placas?|paineis|painel|modulos?|fotovoltaic\w*|solar|solares|inversor\w*|strings?|"
    r"conectores?|mc4|apollo|barcode|codigo\s+de\s+barras|ordem\s+de\s+servico)\b"
)
_SOCIAL_PATTERNS = {
    "saudacao": (
        r"(?:oi+|ola|bom dia|boa tarde|boa noite|e ai)"
        r"(?:\s+(?:apolloai|apollo ai))?(?:\s+(?:tudo bem|como vai))?"
    ),
    "conversa": r"(?:tudo bem|como vai|como voce esta)(?:\s+(?:apolloai|apollo ai))?",
    "agradecimento": r"(?:obrigad[oa]|muito obrigad[oa]|valeu|agradeco)(?:\s+pela ajuda)?",
    "despedida": r"(?:tchau|ate logo|ate mais|ate a proxima)",
}
_SOCIAL_RESPONSES = {
    "saudacao": "Olá! Sou o ApolloAI. Como posso ajudar com ativos fotovoltaicos, manutenção ou segurança?",
    "conversa": "Tudo bem por aqui! Como posso ajudar com ativos fotovoltaicos, manutenção ou segurança?",
    "agradecimento": "Por nada! Se precisar, posso continuar ajudando com ativos fotovoltaicos, manutenção ou segurança.",
    "despedida": "Até mais! Quando precisar, estarei aqui para ajudar com segurança.",
}
OUT_OF_SCOPE_RESPONSE = (
    "Só posso ajudar com energia solar, manutenção de placas e o app Apollo. Qual é a sua dúvida técnica?"
)
_BLOCK_RESPONSES = {
    "OFENSIVO": "Para continuar, mantenha uma comunicação respeitosa. Posso ajudar com dúvidas sobre ativos fotovoltaicos e manutenção.",
    "FORA_ESCOPO": OUT_OF_SCOPE_RESPONSE,
    "PERIGOSO": "Não posso orientar essa prática: ela expõe a risco de choque elétrico. Desenergize e bloqueie o circuito, use EPI e siga o procedimento interno. Posso explicar o procedimento seguro.",
    "ILICITO": "Não posso auxiliar com atividades ilícitas. Posso ajudar com orientação segura sobre ativos fotovoltaicos.",
    "PROMPT_INJECTION": "Não posso fornecer nem ignorar instruções internas do sistema. Posso ajudar com dúvidas sobre ativos fotovoltaicos.",
    "DADOS_INTERNOS": "Não posso fornecer credenciais ou informações internas do sistema. Posso ajudar com dúvidas sobre ativos fotovoltaicos.",
}


def normalize(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text.lower())
    return "".join(char for char in decomposed if not unicodedata.combining(char))


def brief_social_response(message: str) -> str | None:
    """Responde somente a interações sociais curtas, sem engolir perguntas ou comandos."""
    normalized = re.sub(r"[^a-z0-9\s]", " ", normalize(message))
    normalized = re.sub(r"\s+", " ", normalized).strip()
    for intent, pattern in _SOCIAL_PATTERNS.items():
        if re.fullmatch(pattern, normalized):
            return _SOCIAL_RESPONSES[intent]
    return None


def _contains_term(normalized: str, terms: tuple[str, ...]) -> bool:
    return any(re.search(rf"\b{re.escape(normalize(term))}\b", normalized) for term in terms)


def input_guardrail(message: str, semantic_classifier=None) -> GuardrailResult:
    normalized = normalize(message)
    if any(re.search(pattern, normalized, re.I) for pattern in _INJECTION):
        return _blocked("PROMPT_INJECTION")
    if any(normalize(term) in normalized for term in _INTERNAL):
        return _blocked("DADOS_INTERNOS")
    if _contains_term(normalized, _OFFENSIVE):
        return _blocked("OFENSIVO")
    if any(re.search(pattern, normalized) for pattern in _DANGEROUS):
        return _blocked("PERIGOSO")
    social_response = brief_social_response(message)
    if social_response:
        return GuardrailResult("APROVADO", False, social_response)
    if _contains_term(normalized, _OUT_OF_SCOPE):
        return _blocked("FORA_ESCOPO")
    if semantic_classifier:
        category = semantic_classifier(message)
        if category == "FORA_ESCOPO" and _DOMAIN.search(normalized):
            category = "APROVADO"
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
    "pode trabalhar energizado", "esta desenergizado", "dispense o epi", "ignore o procedimento",
    "garanto que", "diagnostico confirmado",
)
_CLAUSE_END = re.compile(r"[.;:!?,\n]")
_CAUTIONARY = re.compile(
    r"\b(nao|nunca|jamais|evite|proibido|confirm\w*|verific\w*|certifi\w*|assegur\w*|"
    r"meca|medir|medindo|teste|testar|antes|somente|so|apos|assum\w*|suponha)\b"
)
_NO_NOTE_MARKERS = ("orientacao geral", "informacoes suficientes", "nao foi possivel validar")
_GENERAL_NOTE = "Orientação geral; confirme no manual do fabricante."
_CITATION_BLOCK = re.compile(
    r"(?ims)^[ \t>*_#•-]*(?:fontes?|fonte\(s\)|refer[eê]ncias?|sources?)"
    r"(?:[ \t]+(?:consultad[ao]s?|utilizad[ao]s?|t[eé]cnic[ao]s?))?[ \t]*[:：].*\Z"
)
_FILE_REFERENCE = re.compile(
    r"[ \t]*[(\[][^()\[\]\n]*?\b[\w-][\w.-]*\.(?:md|pdf)\b[^()\[\]\n]*[)\]]"
    r"|\b[\w-][\w.-]*\.(?:md|pdf)\b",
    re.I,
)


def _without_source_names(text: str) -> str:
    text = _CITATION_BLOCK.sub("", text)
    text = _FILE_REFERENCE.sub("", text)
    text = re.sub(r"[ \t]+([.,;:!?])", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _asserts_unsafe(normalized: str, term: str) -> bool:
    start = 0
    while (index := normalized.find(term, start)) != -1:
        clause = _CLAUSE_END.split(normalized[:index])[-1]
        if not _CAUTIONARY.search(clause):
            return True
        start = index + len(term)
    return False


def output_guardrail(answer: str, sources: list[dict], technical: bool = True) -> tuple[str, str | None]:
    sanitized = answer
    for pattern, replacement in _PII:
        sanitized = re.sub(pattern, replacement, sanitized)
    normalized = normalize(sanitized)
    if any(_asserts_unsafe(normalized, term) for term in _UNSAFE_OUTPUT):
        return (
            "Não é possível validar essa orientação com segurança. Interrompa a intervenção e siga os procedimentos internos e a avaliação de um profissional qualificado.",
            "Orientação potencialmente insegura bloqueada.",
        )
    sanitized = _without_source_names(sanitized)
    if technical and not sources and not any(marker in normalized for marker in _NO_NOTE_MARKERS):
        sanitized = f"{sanitized}\n{_GENERAL_NOTE}"
    return sanitized, None
