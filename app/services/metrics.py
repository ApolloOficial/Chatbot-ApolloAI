"""Métricas de chat e modelos com agregação dos workers do Gunicorn."""

from __future__ import annotations

import os

from prometheus_client import CollectorRegistry, Counter, Gauge, Histogram, generate_latest, multiprocess

LATENCY_BUCKETS = (.1, .5, 1, 2, 4, 8, 15, 30, 60, 90, 120)


class MetricsRegistry:
    def __init__(self) -> None:
        self.registry = CollectorRegistry()
        self.requests = Counter("apolloai_requests_total", "Requisições ao chatbot", registry=self.registry)
        self.errors = Counter("apolloai_errors_total", "Erros controlados", ["tipo"], registry=self.registry)
        self.blocked = Counter("apolloai_blocked_total", "Perguntas bloqueadas", ["motivo"], registry=self.registry)
        self.routes = Counter("apolloai_routes_total", "Rotas selecionadas", ["rota"], registry=self.registry)
        self.agents = Counter("apolloai_agents_total", "Agentes executados", ["agente"], registry=self.registry)
        self.rag_queries = Counter("apolloai_rag_queries_total", "Consultas ao RAG", ["resultado"], registry=self.registry)
        self.judge_rejections = Counter("apolloai_judge_rejections_total", "Respostas reprovadas pelo juiz", registry=self.registry)
        self.mongo_failures = Counter("apolloai_mongodb_failures_total", "Falhas de MongoDB", registry=self.registry)
        self.mcp_failures = Counter("apolloai_mcp_failures_total", "Falhas de MCP", registry=self.registry)
        self.agent_latency = Histogram("apolloai_agent_latency_seconds", "Latência por agente", ["agente"], buckets=LATENCY_BUCKETS, registry=self.registry)
        self.agent_handoff_latency = Histogram("apolloai_agent_handoff_seconds", "Tempo entre o fim de um agente e o início do próximo, incluindo preparação e RAG", ["origem", "destino"], buckets=LATENCY_BUCKETS, registry=self.registry)
        self.total_latency = Histogram("apolloai_response_latency_seconds", "Tempo total incluindo falhas e persistência", buckets=LATENCY_BUCKETS, registry=self.registry)
        self.outcomes = Counter("apolloai_turns_total", "Turnos concluídos por status", ["status"], registry=self.registry)
        for status in ("sucesso", "bloqueado", "esclarecimento", "erro", "negado"):
            self.outcomes.labels(status)
        self.in_progress = Gauge("apolloai_in_progress", "Turnos em andamento", multiprocess_mode="livesum", registry=self.registry)
        self.resolutions = Counter("apolloai_resolutions_total", "Respostas com status sucesso; proxy de resolução, sem confirmação humana", registry=self.registry)
        self.model_calls = Counter("apolloai_model_calls_total", "Chamadas de modelo", ["agente", "modelo", "status"], registry=self.registry)
        self.model_tokens = Counter("apolloai_model_tokens_total", "Tokens informados pelo provedor", ["agente", "modelo", "direcao"], registry=self.registry)
        self.model_latency = Histogram("apolloai_model_latency_seconds", "Latência de chamadas de modelo", ["agente", "modelo"], buckets=(.1, .5, 1, 2, 4, 8, 15, 30, 60, 90), registry=self.registry)
        self.missing_usage = Counter("apolloai_model_usage_missing_total", "Chamadas sem metadados de tokens; custo não conhecido", registry=self.registry)
        self.input_tokens = Counter("apolloai_input_tokens_total", "Tokens de entrada informados pelo provedor", registry=self.registry)
        self.output_tokens = Counter("apolloai_output_tokens_total", "Tokens de saída informados pelo provedor", registry=self.registry)
        self.estimated_cost = Counter("apolloai_estimated_cost_total", "Custo estimado na moeda configurada", registry=self.registry)

    def render_prometheus(self) -> bytes:
        registry = self.registry
        if os.environ.get("PROMETHEUS_MULTIPROC_DIR"):
            registry = CollectorRegistry()
            multiprocess.MultiProcessCollector(registry)
        collected = [sample for metric in registry.collect() for sample in metric.samples]
        samples = {sample.name: sample.value for sample in collected if not sample.labels}
        turns = [sample for sample in collected if sample.name == "apolloai_turns_total"]
        errors = sum(sample.value for sample in turns if sample.labels.get("status") == "erro")
        ratio = errors / max(sum(sample.value for sample in turns), 1)
        resolutions = samples.get("apolloai_resolutions_total", 0)
        cost = samples.get("apolloai_estimated_cost_total", 0) / resolutions if resolutions else "NaN"
        derived = f"# TYPE apolloai_error_ratio gauge\napolloai_error_ratio {ratio}\n# TYPE apolloai_cost_per_resolution gauge\napolloai_cost_per_resolution {cost}\n"
        return generate_latest(registry) + derived.encode()

    def record_request(self) -> None:
        self.requests.inc()

    def record_error(self, error_type: str) -> None:
        self.errors.labels(error_type).inc()

    def record_usage(self, input_tokens: int, output_tokens: int, cost: float, resolved: bool) -> None:
        self.input_tokens.inc(input_tokens)
        self.output_tokens.inc(output_tokens)
        self.estimated_cost.inc(cost)
        if resolved:
            self.resolutions.inc()
