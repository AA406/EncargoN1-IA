from __future__ import annotations

from typing import List
from src.retriever import RetrievedDocument

def assess_confidence(retrieved_docs: List[RetrievedDocument]) -> str:
    if not retrieved_docs:
        return "baja"

    top_score = retrieved_docs[0].score

    if top_score >= 2:
        return "alta"
    if top_score >= 1:
        return "media"
    return "baja"

def should_escalate(confidence: str) -> bool:
    return confidence == "baja"
