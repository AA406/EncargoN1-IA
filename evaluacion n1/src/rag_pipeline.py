from __future__ import annotations

from typing import Dict, List
from src.classifier import classify_query
from src.retriever import retrieve, RetrievedDocument
from src.validator import assess_confidence, should_escalate

class HelpdeskRAGPipeline:
    def _build_answer(self, query: str, docs: List[RetrievedDocument], confidence: str, escalate: bool) -> str:
        if escalate or not docs:
            return (
                "No se encontró evidencia documental suficiente para entregar una respuesta confiable. "
                "Se recomienda derivar el caso a un analista humano para revisión."
            )

        evidence_lines = []
        for doc in docs:
            snippet = doc.content.split(".")[0].strip()
            evidence_lines.append(f"- ({doc.origin}) {snippet}.")

        return (
            f"Para la consulta '{query}', el sistema recuperó evidencia relevante y estima una confianza {confidence}. "
            "Con base en los documentos encontrados, se sugiere la siguiente orientación:\n"
            + "\n".join(evidence_lines)
            + "\n\nRespuesta sintetizada: siga el procedimiento indicado en los documentos fuente y, "
              "si el problema persiste, contacte a soporte de segundo nivel."
        )

    def process_query(self, query: str) -> Dict[str, object]:
        category = classify_query(query)
        docs = retrieve(query)
        confidence = assess_confidence(docs)
        escalate = should_escalate(confidence)
        answer = self._build_answer(query, docs, confidence, escalate)

        return {
            "category": category,
            "confidence": confidence,
            "escalate": escalate,
            "answer": answer,
            "sources": [f"{doc.source} ({doc.origin})" for doc in docs] if docs else ["Sin fuentes suficientes"],
        }
