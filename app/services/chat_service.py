"""Caso de uso que executa o grafo e persiste seu resultado completo."""

from __future__ import annotations

import logging
import time

from flask import Flask

from app.graph import build_graph
from app.llms import LangChainAgentRuntime, ProviderUnavailable
from app.memory import MemoryUnavailable
from app.schemas import ChatRequest, ChatResponse, SourceReference
from app.services.mcp_client import MCPRetriever, MCPUnavailable, SolarMCPClient

logger = logging.getLogger(__name__)


class SessionAccessDenied(RuntimeError):
    """Impede que um usuário reutilize a sessão de outro."""


class ChatService:
    def __init__(self, config, memory, redis_support, metrics, runtime=None, retriever=None) -> None:
        self.config = config
        self.memory = memory
        self.redis = redis_support
        self.metrics = metrics
        self.runtime = runtime or LangChainAgentRuntime(config)
        if retriever is None:
            retriever = MCPRetriever(SolarMCPClient.from_config(config))
        self.retriever = retriever
        self.graph = build_graph(self.runtime, self.retriever, metrics)

    @classmethod
    def from_app(cls, app: Flask):
        from app.extensions import get_service

        return cls(
            app.config, get_service(app, "memory"), get_service(app, "redis"),
            app.extensions["metrics"],
        )

    def execute(self, request: ChatRequest) -> ChatResponse:
        started = time.perf_counter()
        self.metrics.record_request()
        if not self.memory.verify_ownership(request.user_id, request.session_id):
            self.metrics.record_error("acesso_sessao_negado")
            raise SessionAccessDenied
        if self.config["MONGODB_REQUIRED"] and self.memory.health() != "disponivel":
            self.metrics.mongo_failures.inc()
            self.metrics.record_error("mongodb_indisponivel")
            return self._error(request.session_id, "O histórico persistente está temporariamente indisponível. Tente novamente.")

        try:
            self.memory.start_session(request.user_id, request.session_id)
            recent, long_term = self.memory.context(request.user_id, request.session_id, request.pergunta)
            state = self.graph.invoke({
                "question": request.pergunta, "context": request.contexto.model_dump(exclude_none=True),
                "memories": [*recent, *long_term],
            })
            latency_ms = round((time.perf_counter() - started) * 1000, 2)
            response = ChatResponse(
                session_id=request.session_id, resposta=state["final_answer"], status=state.get("status", "sucesso"),
                rota=state.get("route", "fora_escopo"), agentes_chamados=state.get("agents_called", []),
                fontes=[SourceReference.model_validate(item) for item in state.get("sources", [])],
                alerta_seguranca=state.get("safety_alert"), motivo_bloqueio=state.get("block_reason"),
            )
            metadata = {
                "route": response.rota, "agents_called": response.agentes_chamados,
                "sources": [source.model_dump(mode="json") for source in response.fontes],
                "judge_decision": state.get("judge_decision", {}), "blocked": response.status == "bloqueado",
                "block_reason": response.motivo_bloqueio, "total_latency_ms": latency_ms,
            }
            self.memory.save_message(request.user_id, request.session_id, "usuario", request.pergunta)
            self.memory.save_message(request.user_id, request.session_id, "assistente", response.resposta, **metadata)
            self.memory.update_session_result(request.user_id, request.session_id, response.rota)
            self.memory.maybe_summarize(request.user_id, request.session_id)
            self.memory.save_observation({
                "route": response.rota, "agents_called": response.agentes_chamados,
                "judge_decision": state.get("judge_decision", {}), "blocked": response.status == "bloqueado",
                "block_reason": response.motivo_bloqueio, "agent_latencies_ms": state.get("agent_latencies_ms", {}),
                "total_latency_ms": latency_ms, "source_count": len(response.fontes),
            })
            self.redis.record_route(response.rota)
            self.metrics.total_latency.observe(latency_ms / 1000)
            input_tokens = _estimate_tokens(request.pergunta) + sum(_estimate_tokens(str(item)) for item in recent)
            output_tokens = _estimate_tokens(response.resposta)
            cost = _estimated_cost(input_tokens, output_tokens, self.config)
            self.metrics.record_usage(input_tokens, output_tokens, cost, response.status == "sucesso")
            return response
        except MCPUnavailable:
            self.metrics.mcp_failures.inc()
            return self._controlled_failure(request, "mcp_indisponivel", "A base técnica está temporariamente indisponível. Tente novamente.", started)
        except ProviderUnavailable:
            return self._controlled_failure(request, "provedor_ia_indisponivel", "O provedor de IA está temporariamente indisponível. Tente novamente.", started)
        except MemoryUnavailable:
            self.metrics.mongo_failures.inc()
            self.metrics.record_error("mongodb_indisponivel")
            return self._error(request.session_id, "Não foi possível persistir a conversa. Tente novamente.")

    def _controlled_failure(self, request: ChatRequest, reason: str, message: str, started: float) -> ChatResponse:
        self.metrics.record_error(reason)
        response = self._error(request.session_id, message)
        latency = round((time.perf_counter() - started) * 1000, 2)
        try:
            self.memory.save_message(request.user_id, request.session_id, "usuario", request.pergunta)
            self.memory.save_message(
                request.user_id, request.session_id, "assistente", message,
                route="fora_escopo", block_reason=reason, total_latency_ms=latency,
            )
        except MemoryUnavailable:
            self.metrics.mongo_failures.inc()
        return response

    @staticmethod
    def _error(session_id: str, message: str) -> ChatResponse:
        return ChatResponse(
            session_id=session_id, resposta=message, status="erro", rota="fora_escopo",
            agentes_chamados=[], fontes=[], motivo_bloqueio=None,
        )


def _estimate_tokens(text: str) -> int:
    return max(1, round(len(text) / 4))


def _estimated_cost(input_tokens: int, output_tokens: int, config) -> float:
    return round(
        input_tokens * config["PRICE_INPUT_PER_MILLION"] / 1_000_000
        + output_tokens * config["PRICE_OUTPUT_PER_MILLION"] / 1_000_000,
        8,
    )
