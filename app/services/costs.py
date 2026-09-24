"""Estimativas configuráveis de custo, resolução e ROI."""

from __future__ import annotations


def estimate_weekly_scenario(users: int, config) -> dict[str, float | int | None]:
    requests = users * config["AVG_MESSAGES_PER_USER"]
    agent_calls = requests * config["AVG_AGENTS_PER_REQUEST"]
    input_tokens = agent_calls * config["AVG_INPUT_TOKENS"]
    output_tokens = agent_calls * config["AVG_OUTPUT_TOKENS"]
    daily_agent_calls = agent_calls / 7
    daily_tokens = (input_tokens + output_tokens) / 7
    free_quota_feasible = (
        daily_agent_calls <= config["AI_FREE_DAILY_REQUEST_LIMIT"]
        and daily_tokens <= config["AI_FREE_DAILY_TOKEN_LIMIT"]
    )
    ai_cost = (
        input_tokens * config["PRICE_INPUT_PER_MILLION"] / 1_000_000
        + output_tokens * config["PRICE_OUTPUT_PER_MILLION"] / 1_000_000
    )
    monthly_infrastructure_cost = (
        config["AWS_MONTHLY_COST_100_USERS"]
        if users <= 100
        else config["AWS_MONTHLY_COST_1000_USERS"]
    )
    weekly_infrastructure_cost = monthly_infrastructure_cost * 12 / 52
    total_cost = ai_cost + weekly_infrastructure_cost
    resolutions = requests * config["ESTIMATED_RESOLUTION_RATE"]
    cost_per_resolution = total_cost / resolutions if resolutions else None
    estimated_benefit = (
        resolutions * config["ESTIMATED_MINUTES_SAVED"] / 60 * config["TECHNICIAN_HOURLY_COST"]
    )
    roi = (estimated_benefit - total_cost) / total_cost if total_cost else None
    return {
        "weekly_users": users, "requests": round(requests), "agent_calls": round(agent_calls),
        "rag_queries": round(requests * config["AVG_RAG_QUERIES"]),
        "input_tokens": round(input_tokens), "output_tokens": round(output_tokens),
        "estimated_daily_agent_calls": round(daily_agent_calls, 2),
        "estimated_daily_tokens": round(daily_tokens, 2),
        "free_quota_feasible": free_quota_feasible,
        "free_daily_request_limit": config["AI_FREE_DAILY_REQUEST_LIMIT"],
        "free_daily_token_limit": config["AI_FREE_DAILY_TOKEN_LIMIT"],
        "estimated_resolutions": round(resolutions, 2), "estimated_ai_cost": round(ai_cost, 4),
        "estimated_monthly_infrastructure_cost": round(monthly_infrastructure_cost, 2),
        "estimated_weekly_infrastructure_cost": round(weekly_infrastructure_cost, 4),
        "estimated_total_weekly_cost": round(total_cost, 4),
        "aws_lab_budget": round(config["AWS_LAB_BUDGET_USD"], 2),
        "estimated_monthly_budget_remaining": round(
            config["AWS_LAB_BUDGET_USD"] - monthly_infrastructure_cost, 2
        ),
        "cost_per_resolution": round(cost_per_resolution, 6) if cost_per_resolution is not None else None,
        "estimated_benefit": round(estimated_benefit, 4), "estimated_roi": round(roi, 4) if roi is not None else None,
    }
