"""Exibe cenários semanais usando somente premissas configuradas."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import Config
from app.services.costs import estimate_weekly_scenario


if __name__ == "__main__":
    scenarios = [estimate_weekly_scenario(users, Config.__dict__) for users in (100, 1000)]
    print(json.dumps(scenarios, ensure_ascii=False, indent=2))
