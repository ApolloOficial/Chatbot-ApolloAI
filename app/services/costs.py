"""Estimativas configuráveis de custo, resolução e ROI."""

from __future__ import annotations


def estimate_weekly_scenario(users: int, config) -> dict[str, float | int | None]:
    requests = users * config["AVG_MESSAGES_PER_USER"]
    agent_calls = requests * config["AVG_AGENTS_PER_REQUEST"]
    input_tokens = agent_calls * config["AVG_INPUT_TOKENS"]
    output_tokens = agent_calls * config["AVG_OUTPUT_TOKENS"]
    ai_cost = (
        input_tokens * config["PRICE_INPUT_PER_MILLION"] / 1_000_000
        + output_tokens * config["PRICE_OUTPUT_PER_MILLION"] / 1_000_000
    )
    resolutions = requests * config["ESTIMATED_RESOLUTION_RATE"]
    cost_per_resolution = ai_cost / resolutions if resolutions else None
    estimated_benefit = (
        resolutions * config["ESTIMATED_MINUTES_SAVED"] / 60 * config["TECHNICIAN_HOURLY_COST"]
    )
    roi = (estimated_benefit - ai_cost) / ai_cost if ai_cost else None
    return {
        "weekly_users": users, "requests": round(requests), "agent_calls": round(agent_calls),
        "rag_queries": round(requests * config["AVG_RAG_QUERIES"]),
        "input_tokens": round(input_tokens), "output_tokens": round(output_tokens),
        "estimated_resolutions": round(resolutions, 2), "estimated_ai_cost": round(ai_cost, 4),
        "cost_per_resolution": round(cost_per_resolution, 6) if cost_per_resolution is not None else None,
        "estimated_benefit": round(estimated_benefit, 4), "estimated_roi": round(roi, 4) if roi is not None else None,
    }
