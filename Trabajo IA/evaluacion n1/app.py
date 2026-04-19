from src.rag_pipeline import HelpdeskRAGPipeline

def main() -> None:
    pipeline = HelpdeskRAGPipeline()
    print("=== Helpdesk con LLM + RAG (prototipo académico) ===")
    print("Escribe tu consulta. Para salir, escribe 'salir'.\n")

    while True:
        query = input("Consulta: ").strip()
        if query.lower() in {"salir", "exit", "quit"}:
            print("Sesión finalizada.")
            break

        result = pipeline.process_query(query)

        print("\n--- Resultado ---")
        print(f"Categoría: {result['category']}")
        print(f"Confianza: {result['confidence']}")
        print(f"Escalar: {'Sí' if result['escalate'] else 'No'}")
        print("\nRespuesta:")
        print(result["answer"])

        print("\nFuentes:")
        for source in result["sources"]:
            print(f"- {source}")

        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()
