"""Registro Prometheus isolado por instância Flask."""

from __future__ import annotations

from prometheus_client import CollectorRegistry, Counter, Gauge, Histogram, generate_latest


class MetricsRegistry:
    def __init__(self) -> None:
        self._request_count = 0
        self._error_count = 0
        self._resolution_count = 0
        self._accumulated_cost = 0.0
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
        self.agent_latency = Histogram("apolloai_agent_latency_seconds", "Latência por agente", ["agente"], registry=self.registry)
        self.total_latency = Histogram("apolloai_response_latency_seconds", "Tempo total", registry=self.registry)
        self.input_tokens = Counter("apolloai_input_tokens_total", "Tokens estimados de entrada", registry=self.registry)
        self.output_tokens = Counter("apolloai_output_tokens_total", "Tokens estimados de saída", registry=self.registry)
        self.estimated_cost = Counter("apolloai_estimated_cost_total", "Custo estimado na moeda configurada", registry=self.registry)
        self.error_ratio = Gauge("apolloai_error_ratio", "Índice de erros observado", registry=self.registry)
        self.cost_per_resolution = Gauge("apolloai_cost_per_resolution", "Custo estimado por resolução", registry=self.registry)

    def render_prometheus(self) -> bytes:
        return generate_latest(self.registry)

    def record_request(self) -> None:
        self._request_count += 1
        self.requests.inc()

    def record_error(self, error_type: str) -> None:
        self._error_count += 1
        self.errors.labels(error_type).inc()
        self.error_ratio.set(self._error_count / max(self._request_count, 1))

    def record_usage(self, input_tokens: int, output_tokens: int, cost: float, resolved: bool) -> None:
        self.input_tokens.inc(input_tokens)
        self.output_tokens.inc(output_tokens)
        self.estimated_cost.inc(cost)
        self._accumulated_cost += cost
        if resolved:
            self._resolution_count += 1
        self.cost_per_resolution.set(self._accumulated_cost / max(self._resolution_count, 1))
