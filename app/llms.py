"""Inicialização sob demanda de modelos e agentes LangChain."""

from __future__ import annotations

import json
import logging
from typing import Any

from langchain.agents import create_agent

from app.prompts import AGENT_PROMPTS, INPUT_CLASSIFIER_PROMPT

logger = logging.getLogger(__name__)


class ProviderUnavailable(RuntimeError):
    """Falha controlada do provedor de IA."""


class LangChainAgentRuntime:
    """Executa os agentes via `create_agent`, com instâncias em cache local."""

    def __init__(self, config) -> None:
        self.config = config
        self._model = None
        self._agents: dict[str, Any] = {}

    def _build_model(self):
        provider = self.config["AI_PROVIDER"].lower()
        common = {
            "model": self.config["AI_MODEL"], "temperature": 0,
            "timeout": self.config["AI_TIMEOUT_SECONDS"],
            "max_retries": self.config["AI_MAX_RETRIES"],
        }
        if provider == "groq":
            from langchain_groq import ChatGroq

            if not self.config.get("GROQ_API_KEY"):
                raise ProviderUnavailable("Provedor de IA não configurado.")
            return ChatGroq(api_key=self.config["GROQ_API_KEY"], **common)
        if provider in {"google", "gemini"}:
            from langchain_google_genai import ChatGoogleGenerativeAI

            if not self.config.get("GOOGLE_API_KEY"):
                raise ProviderUnavailable("Provedor de IA não configurado.")
            return ChatGoogleGenerativeAI(google_api_key=self.config["GOOGLE_API_KEY"], **common)
        raise ProviderUnavailable("Provedor de IA não suportado.")

    @property
    def model(self):
        if self._model is None:
            self._model = self._build_model()
        return self._model

    def invoke(self, agent_name: str, content: str) -> str:
        try:
            if agent_name not in self._agents:
                self._agents[agent_name] = create_agent(
                    model=self.model, system_prompt=AGENT_PROMPTS[agent_name], name=agent_name,
                )
            output = self._agents[agent_name].invoke({"messages": [{"role": "user", "content": content}]})
            text = getattr(output["messages"][-1], "content", "")
            return text if isinstance(text, str) else json.dumps(text, ensure_ascii=False)
        except ProviderUnavailable:
            raise
        except Exception as error:
            logger.warning("provedor_ia_indisponivel", extra={"error_type": type(error).__name__, "agent": agent_name})
            raise ProviderUnavailable("Falha temporária do provedor de IA.") from error

    def classify_input(self, message: str) -> str:
        try:
            result = self.model.invoke(INPUT_CLASSIFIER_PROMPT.format(message=message))
            return str(result.content).strip().upper().split()[0]
        except Exception as error:
            logger.warning("classificador_semantico_indisponivel", extra={"error_type": type(error).__name__})
            return "APROVADO"
