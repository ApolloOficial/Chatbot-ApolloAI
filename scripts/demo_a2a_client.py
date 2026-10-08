"""Demonstra uma chamada A2A a partir de um processo cliente separado."""

import json
import os
import sys
from urllib.request import Request, urlopen
from uuid import uuid4

from dotenv import load_dotenv

load_dotenv()


def main():
    base = os.getenv("PUBLIC_BASE_URL", "").rstrip("/")
    token = os.getenv("APOLLOAI_API_TOKEN", "")
    user = os.getenv("A2A_DEMO_USER_ID", "tecnico-demo")
    if not base or not token:
        raise SystemExit("Configure PUBLIC_BASE_URL e APOLLOAI_API_TOKEN no ambiente.")
    headers = {"Authorization": f"Bearer {token}", "X-User-ID": user}
    with urlopen(Request(f"{base}/.well-known/agent-card.json"), timeout=15) as response:
        card = json.load(response)
    payload = {
        "jsonrpc": "2.0", "id": str(uuid4()), "method": "SendMessage",
        "params": {"message": {
            "messageId": str(uuid4()), "role": "ROLE_USER", "parts": [{"text":
                "Quais fatores podem reduzir a eficiência de um módulo fotovoltaico?"}],
        }},
    }
    headers["Content-Type"] = "application/json"
    request = Request(f"{base}/a2a/v1", data=json.dumps(payload).encode(), headers=headers, method="POST")
    with urlopen(request, timeout=120) as response:
        result = json.load(response)
    print("Agente encontrado:", card["name"])
    if "error" in result:
        print("Erro A2A:", result["error"].get("message"))
        return 1
    print("Resposta:", result["result"]["message"]["parts"][0]["text"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
