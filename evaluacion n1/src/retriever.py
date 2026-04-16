from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import List

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

STOPWORDS = {
    "para", "con", "sin", "una", "uno", "del", "las", "los", "que", "por", "este",
    "esta", "como", "donde", "cuando", "sobre", "debe", "deben", "de", "la", "el",
    "mi", "mis", "sus", "hay", "más", "muy", "necesito", "ayuda", "caso", "sistema",
    "usuario", "equipo", "soporte", "proceso", "documentación", "modulo", "módulo",
}

@dataclass
class RetrievedDocument:
    source: str
    origin: str
    score: int
    content: str

def tokenize(text: str) -> set[str]:
    tokens = set(re.findall(r"[a-záéíóúñA-ZÁÉÍÓÚÑ]{3,}", text.lower()))
    return {t for t in tokens if t not in STOPWORDS}

def load_documents() -> list[tuple[str, str, str]]:
    documents: list[tuple[str, str, str]] = []
    for origin in ("internal", "external"):
        folder = DATA_DIR / origin
        for path in sorted(folder.glob("*.txt")):
            documents.append((path.name, origin, path.read_text(encoding="utf-8")))
    return documents

def retrieve(query: str, top_k: int = 3) -> List[RetrievedDocument]:
    query_tokens = tokenize(query)
    retrieved: list[RetrievedDocument] = []

    for filename, origin, content in load_documents():
        content_tokens = tokenize(content)
        score = len(query_tokens.intersection(content_tokens))
        if score > 0:
            retrieved.append(
                RetrievedDocument(
                    source=filename,
                    origin=origin,
                    score=score,
                    content=content.strip(),
                )
            )

    retrieved.sort(key=lambda doc: doc.score, reverse=True)
    return retrieved[:top_k]
