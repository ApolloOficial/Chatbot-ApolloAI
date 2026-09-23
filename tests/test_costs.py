import pytest

from app.services.costs import estimate_weekly_scenario


BASE_CONFIG = {
    "AVG_MESSAGES_PER_USER": 5,
    "AVG_AGENTS_PER_REQUEST": 4,
    "AVG_INPUT_TOKENS": 700,
    "AVG_OUTPUT_TOKENS": 350,
    "AVG_RAG_QUERIES": 1,
    "PRICE_INPUT_PER_MILLION": 0,
    "PRICE_OUTPUT_PER_MILLION": 0,
    "ESTIMATED_RESOLUTION_RATE": 0.75,
    "ESTIMATED_MINUTES_SAVED": 5,
    "TECHNICIAN_HOURLY_COST": 0,
    "AWS_LAB_BUDGET_USD": 50,
    "AWS_MONTHLY_COST_100_USERS": 12.50,
    "AWS_MONTHLY_COST_1000_USERS": 20.10,
    "AI_FREE_DAILY_REQUEST_LIMIT": 1000,
    "AI_FREE_DAILY_TOKEN_LIMIT": 200000,
}


@pytest.mark.parametrize(
    "users,monthly_cost",
    [(100, 12.50), (1000, 20.10)],
)
def test_weekly_scenario_includes_aws_lab_infrastructure(users, monthly_cost):
    scenario = estimate_weekly_scenario(users, BASE_CONFIG)

    assert scenario["estimated_ai_cost"] == 0
    assert scenario["estimated_monthly_infrastructure_cost"] == monthly_cost
    assert scenario["estimated_weekly_infrastructure_cost"] == pytest.approx(monthly_cost * 12 / 52, abs=0.0001)
    assert scenario["estimated_total_weekly_cost"] == scenario["estimated_weekly_infrastructure_cost"]
    assert scenario["estimated_monthly_budget_remaining"] == pytest.approx(50 - monthly_cost)
    assert scenario["cost_per_resolution"] > 0
    assert scenario["free_quota_feasible"] is False
