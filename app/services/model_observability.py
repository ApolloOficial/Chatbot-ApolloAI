"""Callbacks LangChain para registrar chamadas, latência, tokens e custo dos modelos."""

import time
from threading import Lock

from langchain_core.callbacks import BaseCallbackHandler


class ModelMetricsCallback(BaseCallbackHandler):
    def __init__(self, metrics, config, agent):
        self.metrics, self.config, self.agent = metrics, config, agent
        self.model = config["AI_MODEL"]
        self.starts = {}
        self.lock = Lock()

    def _start(self, run_id):
        with self.lock:
            self.starts[run_id] = time.perf_counter()

    def on_chat_model_start(self, serialized, messages, *, run_id, **kwargs):
        self._start(run_id)

    def on_llm_start(self, serialized, prompts, *, run_id, **kwargs):
        self._start(run_id)

    def _finish(self, run_id, status):
        with self.lock:
            started = self.starts.pop(run_id, None)
        self.metrics.model_calls.labels(self.agent, self.model, status).inc()
        if started is not None:
            self.metrics.model_latency.labels(self.agent, self.model).observe(time.perf_counter() - started)

    def on_llm_end(self, response, *, run_id, **kwargs):
        self._finish(run_id, "sucesso")
        usages = []
        for generations in response.generations:
            if generations:
                usage = getattr(getattr(generations[0], "message", None), "usage_metadata", None)
                if usage:
                    usages.append(usage)
        if usages:
            input_tokens = sum(u.get("input_tokens", 0) for u in usages)
            output_tokens = sum(u.get("output_tokens", 0) for u in usages)
        else:
            usage = (response.llm_output or {}).get("token_usage") or (response.llm_output or {}).get("usage")
            if not usage:
                self.metrics.missing_usage.inc()
                return
            input_tokens = usage.get("prompt_tokens", usage.get("input_tokens", 0))
            output_tokens = usage.get("completion_tokens", usage.get("output_tokens", 0))
        for direction, value in (("entrada", input_tokens), ("saida", output_tokens)):
            self.metrics.model_tokens.labels(self.agent, self.model, direction).inc(value)
        cost = (input_tokens * self.config["PRICE_INPUT_PER_MILLION"] + output_tokens * self.config["PRICE_OUTPUT_PER_MILLION"]) / 1_000_000
        self.metrics.record_usage(input_tokens, output_tokens, cost, False)

    def on_llm_error(self, error, *, run_id, **kwargs):
        self._finish(run_id, "erro")
        self.metrics.missing_usage.inc()
