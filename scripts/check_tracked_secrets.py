"""Falha quando arquivos rastreados contêm credenciais de alta confiança."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


FORBIDDEN_FILES = re.compile(r"(^|/)(?:\.env|deploy\.env)$|\.(?:pem|p12|pfx|key)$", re.IGNORECASE)
TOKEN_PATTERNS = {
    "chave privada": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
    "Groq API key": re.compile(r"\bgsk_[A-Za-z0-9]{20,}\b"),
    "Google API key": re.compile(r"\bAIza[A-Za-z0-9_-]{30,}\b"),
}
ASSIGNMENT = re.compile(
    r"(?im)^[ \t]*(APOLLOAI_API_TOKEN|GROQ_API_KEY|GOOGLE_API_KEY|GEMINI_API_KEY|"
    r"QDRANT_API_KEY|MONGODB_URI|REDIS_URL|AWS_SECRET_ACCESS_KEY)[ \t]*[:=][ \t]*([^\s#]+)"
)
ASSIGNMENT_FILES = {".env", ".example", ".yaml", ".yml", ".json", ".md", ".toml"}
SAFE_MARKERS = ("${", "<", "...", "replace", "test", "exemplo", "valor", "chave", "preencha", "seu_", "sua_", "troque")


def versioned_files() -> list[Path]:
    output = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8").split("\0")
    return [Path(name) for name in output if name]


def history_findings() -> list[str]:
    findings: list[str] = []
    names = subprocess.run(
        ["git", "log", "--all", "--name-only", "--format="],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.splitlines()
    for name in sorted(set(names)):
        if FORBIDDEN_FILES.search(name) and not name.endswith(".example"):
            findings.append(f"histórico:{name}: arquivo sensível foi versionado")
    objects = subprocess.run(
        ["git", "rev-list", "--objects", "--all"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.splitlines()
    entries = [(line.split(" ", 1)[0], line.split(" ", 1)[1]) for line in objects if " " in line]
    seen_objects: set[str] = set()
    for object_id, path in entries:
        if object_id in seen_objects:
            continue
        seen_objects.add(object_id)
        if Path(path).suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".zip"}:
            continue
        result = subprocess.run(
            ["git", "cat-file", "blob", object_id], check=False, capture_output=True,
        )
        if result.returncode:
            continue
        blob = result.stdout
        if len(blob) > 2_000_000:
            continue
        content = blob.decode("utf-8", errors="ignore")
        for name, pattern in TOKEN_PATTERNS.items():
            if pattern.search(content):
                findings.append(f"histórico:{path}: possível {name}")
    return findings


def main() -> int:
    findings = history_findings()
    for path in versioned_files():
        normalized = path.as_posix()
        if FORBIDDEN_FILES.search(normalized) and not normalized.endswith(".example"):
            findings.append(f"{normalized}: arquivo sensível não deve ser rastreado")
            continue
        try:
            if path.stat().st_size > 2_000_000:
                continue
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for name, pattern in TOKEN_PATTERNS.items():
            for match in pattern.finditer(content):
                line = content.count("\n", 0, match.start()) + 1
                findings.append(f"{normalized}:{line}: possível {name}")
        if path.suffix.lower() in ASSIGNMENT_FILES:
            for match in ASSIGNMENT.finditer(content):
                value = match.group(2).strip("\"'").lower()
                if not value or any(marker in value for marker in SAFE_MARKERS):
                    continue
                line = content.count("\n", 0, match.start()) + 1
                findings.append(f"{normalized}:{line}: possível valor real em {match.group(1)}")
    if findings:
        print("\n".join(findings))
        return 1
    print("Nenhuma credencial de alta confiança encontrada nos arquivos versionáveis ou no histórico Git.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
