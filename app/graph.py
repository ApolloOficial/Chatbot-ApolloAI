"""Grafo multiagente real: guardrail → roteador → especialista → juiz → orquestrador."""

from __future__ import annotations

import json
import re
import time
from typing import Any, Literal, Protocol, TypedDict

from langgraph.graph import END, StateGraph

from app.guardrail import input_guardrail, normalize, output_guardrail
from app.schemas import JudgeDecision

Route = Literal["ativos_solares", "manutencao", "seguranca", "faq_apolloai", "fora_escopo"]
VALID_ROUTES = {"ativos_solares", "manutencao", "seguranca", "faq_apolloai", "fora_escopo"}
TECHNICAL_ROUTES = {"ativos_solares", "manutencao", "seguranca"}


class AgentRuntime(Protocol):
    def invoke(self, agent_name: str, content: str) -> str: ...
    def classify_input(self, message: str) -> str: ...


class Retriever(Protocol):
    def retrieve(self, query: str, route: str) -> list[dict[str, Any]]: ...


class GraphState(TypedDict, total=False):
    question: str
    context: dict[str, Any]
    memories: list[dict[str, Any]]
    route: Route
    agents_called: list[str]
    sources: list[dict[str, Any]]
    blocked: bool
    block_reason: str | None
    status: str
    draft: str
    judge_decision: dict[str, Any]
    final_answer: str
    safety_alert: str | None
    agent_latencies_ms: dict[str, float]


def _json_object(text: str) -> dict[str, Any]:
    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        return {}
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return {}


def _fallback_route(question: str) -> Route:
    text = normalize(question)
    if any(word in text for word in ("segur", "tensao", "choque", "epi", "bloqueio", "energiz")):
        return "seguranca"
    if any(word in text for word in ("manutenc", "preventiv", "preditiv", "corretiv", "relatorio", "falha", "anomalia")):
        return "manutencao"
    if any(word in text for word in ("placa", "modulo", "fotovolta", "inversor", "string", "eficien", "solar", "cabeamento", "conector")):
        return "ativos_solares"
    if any(word in text for word in ("apolloai", "o que voce", "quem e voce", "ola", "oi", "obrigad")):
        return "faq_apolloai"
    return "fora_escopo"


def _source_context(sources: list[dict[str, Any]]) -> str:
    if not sources:
        return "Nenhum trecho técnico recuperado."
    parts = []
    for index, source in enumerate(sources, 1):
        parts.append(
            f"[FONTE {index}] documento={source.get('documento')} página={source.get('pagina')} "
            f"seção={source.get('secao')}\n{source.get('trecho', '')}"
        )
    return "\n\n".join(parts)


def build_graph(runtime: AgentRuntime, retriever: Retriever, metrics):
    """Compila um StateGraph; o histórico durável permanece exclusivamente no MongoDB."""

    def timed(agent_name: str, content: str, state: GraphState) -> tuple[str, dict[str, float]]:
        started = time.perf_counter()
        answer = runtime.invoke(agent_name, content)
        latency = (time.perf_counter() - started) * 1000
        metrics.agents.labels(agent_name).inc()
        metrics.agent_latency.labels(agent_name).observe(latency / 1000)
        latencies = dict(state.get("agent_latencies_ms", {}))
        latencies[agent_name] = round(latency, 2)
        return answer, latencies

    def guard_input(state: GraphState) -> GraphState:
        result = input_guardrail(state["question"], runtime.classify_input)
        if not result.blocked:
            return {"blocked": False, "agents_called": [], "agent_latencies_ms": {}}
        metrics.blocked.labels(result.category.lower()).inc()
        return {
            "blocked": True, "block_reason": result.category.lower(), "route": "fora_escopo",
            "status": "bloqueado", "final_answer": result.response or "Solicitação bloqueada.",
            "agents_called": [], "sources": [], "judge_decision": {}, "agent_latencies_ms": {},
        }

    def after_guard(state: GraphState) -> str:
        return "blocked" if state.get("blocked") else "router"

    def router(state: GraphState) -> GraphState:
        content = f"MENSAGEM ORIGINAL:\n{state['question']}\n\nCONTEXTO FORNECIDO:\n{json.dumps(state.get('context', {}), ensure_ascii=False)}"
        answer, latencies = timed("roteador", content, state)
        route = _json_object(answer).get("rota")
        if route not in VALID_ROUTES:
            route = _fallback_route(state["question"])
        metrics.routes.labels(route).inc()
        return {"route": route, "agents_called": ["roteador"], "agent_latencies_ms": latencies}

    def choose_specialist(state: GraphState) -> str:
        return state["route"]

    def specialist(agent_name: str):
        def node(state: GraphState) -> GraphState:
            sources = [] if agent_name == "faq_apolloai" else retriever.retrieve(state["question"], agent_name)
            metrics.rag_queries.labels("com_fontes" if sources else "sem_fontes").inc()
            prompt = (
                f"PERGUNTA ORIGINAL:\n{state['question']}\n\nCONTEXTO DO ATIVO FORNECIDO PELO TÉCNICO:\n"
                f"{json.dumps(state.get('context', {}), ensure_ascii=False)}\n\nMEMÓRIAS RELEVANTES:\n"
                f"{json.dumps(state.get('memories', []), ensure_ascii=False)}\n\nTRECHOS RECUPERADOS:\n{_source_context(sources)}"
            )
            draft, latencies = timed(agent_name, prompt, state)
            return {
                "draft": draft, "sources": sources,
                "agents_called": state.get("agents_called", []) + [agent_name],
                "agent_latencies_ms": latencies,
            }
        return node

    def out_of_scope(state: GraphState) -> GraphState:
        metrics.blocked.labels("fora_escopo").inc()
        return {
            "blocked": True, "block_reason": "fora_escopo", "status": "bloqueado", "sources": [],
            "final_answer": "O ApolloAI atende somente a dúvidas relacionadas a ativos fotovoltaicos e manutenção. Posso ajudar com alguma questão técnica sobre sistemas solares?",
        }

    def judge(state: GraphState) -> GraphState:
        prompt = f"RASCUNHO:\n{state['draft']}\n\nFONTES RECUPERADAS:\n{_source_context(state.get('sources', []))}\n\nROTA: {state['route']}"
        raw, latencies = timed("juiz_factual", prompt, state)
        payload = _json_object(raw)
        try:
            decision = JudgeDecision.model_validate(payload)
        except Exception:
            decision = JudgeDecision(
                decisao="rejeitada", fundamentada=False, segura=False, dentro_escopo=True,
                fontes_validas=False, motivos=["O juiz não retornou uma decisão estruturada válida."],
            )
        if state["route"] in TECHNICAL_ROUTES and not state.get("sources"):
            decision = JudgeDecision(
                decisao="rejeitada", fundamentada=False, segura=decision.segura,
                dentro_escopo=decision.dentro_escopo, fontes_validas=False,
                motivos=[*decision.motivos, "Não há fonte recuperada para sustentar a resposta técnica."],
            )
        if decision.decisao == "rejeitada":
            metrics.judge_rejections.inc()
        return {
            "judge_decision": decision.model_dump(),
            "agents_called": state.get("agents_called", []) + ["juiz_factual"],
            "agent_latencies_ms": latencies,
        }

    def orchestrator(state: GraphState) -> GraphState:
        decision = JudgeDecision.model_validate(state["judge_decision"])
        if decision.decisao == "rejeitada":
            approved = "Não encontrei informações suficientes nas fontes técnicas disponíveis para responder com segurança."
        elif decision.decisao == "corrigir" and decision.resposta_corrigida:
            approved = decision.resposta_corrigida
        else:
            approved = state["draft"]
        prompt = f"CONTEÚDO APROVADO PELO JUIZ:\n{approved}\n\nLIMITAÇÕES:\n{'; '.join(decision.motivos)}"
        final, latencies = timed("orquestrador", prompt, state)
        return {
            "final_answer": final,
            "agents_called": state.get("agents_called", []) + ["orquestrador"],
            "agent_latencies_ms": latencies,
        }

    def guard_output(state: GraphState) -> GraphState:
        answer, alert = output_guardrail(
            state["final_answer"], state.get("sources", []), state.get("route") in TECHNICAL_ROUTES,
        )
        status = "esclarecimento" if "informações suficientes" in answer else "sucesso"
        return {"final_answer": answer, "safety_alert": alert, "status": status}

    graph = StateGraph(GraphState)
    graph.add_node("guardrail_entrada", guard_input)
    graph.add_node("roteador", router)
    for route in ("ativos_solares", "manutencao", "seguranca", "faq_apolloai"):
        graph.add_node(route, specialist(route))
    graph.add_node("fora_escopo", out_of_scope)
    graph.add_node("juiz_factual", judge)
    graph.add_node("orquestrador", orchestrator)
    graph.add_node("guardrail_saida", guard_output)
    graph.set_entry_point("guardrail_entrada")
    graph.add_conditional_edges("guardrail_entrada", after_guard, {"blocked": END, "router": "roteador"})
    graph.add_conditional_edges("roteador", choose_specialist, {route: route for route in VALID_ROUTES})
    for route in ("ativos_solares", "manutencao", "seguranca", "faq_apolloai"):
        graph.add_edge(route, "juiz_factual")
    graph.add_edge("fora_escopo", END)
    graph.add_edge("juiz_factual", "orquestrador")
    graph.add_edge("orquestrador", "guardrail_saida")
    graph.add_edge("guardrail_saida", END)
    return graph.compile()
