"""Converte os PDFs do corpus solar em Markdown, localmente e sem API de IA.

Uso: python -m scripts.convert_pdfs_to_markdown [--force]
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

from pypdf import PdfReader

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import Config


def clean_page(text: str) -> str:
    """Preserva a ordem extraída e limita apenas espaços e linhas vazias."""
    text = unicodedata.normalize("NFKC", text).replace("\x00", "")
    lines = [line.rstrip() for line in text.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def convert_pdf(path: Path, output_dir: Path, force: bool = False) -> tuple[Path, int, int]:
    output = output_dir / f"{path.stem}.md"
    if output.exists() and not force and output.stat().st_mtime_ns >= path.stat().st_mtime_ns:
        return output, 0, 0

    reader = PdfReader(path)
    sections = [f"# {path.stem}", "", f"Fonte original: `{path.name}`", ""]
    empty_pages = 0
    for number, page in enumerate(reader.pages, 1):
        content = clean_page(page.extract_text() or "")
        if not content:
            empty_pages += 1
            content = "[Página sem texto extraível.]"
        sections.extend([f"## Página {number}", "", content, ""])

    output_dir.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")
    return output, len(reader.pages), empty_pages


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="recria todos os Markdown")
    args = parser.parse_args()

    source_dir = Path(Config.SOLAR_DOCUMENTS_DIR)
    output_dir = source_dir / "markdown"
    total_pages = total_empty = converted = 0
    for path in sorted(source_dir.glob("*.pdf")):
        output, pages, empty = convert_pdf(path, output_dir, force=args.force)
        converted += bool(pages)
        total_pages += pages
        total_empty += empty
        print(f"{path.name} -> {output.name}: {pages} páginas, {empty} sem texto", flush=True)
    print(f"Convertidos: {converted}; páginas: {total_pages}; páginas sem texto: {total_empty}")


if __name__ == "__main__":
    main()
