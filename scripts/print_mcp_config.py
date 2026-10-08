"""Imprime a configuração local de Cursor/Cline, sem copiar credenciais."""

import json
from pathlib import Path
import sys


if __name__ == "__main__":
    server = Path(__file__).resolve().parents[1] / "app" / "mcp_server.py"
    print(json.dumps({"mcpServers": {"apolloai-solar-knowledge": {
        "command": sys.executable, "args": [str(server)],
    }}}, indent=2, ensure_ascii=True))
