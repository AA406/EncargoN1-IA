# Helpdesk con LLM + RAG para Implementos

Repositorio de apoyo para la evaluación parcial de **Ingeniería de Soluciones con IA**.  
El proyecto propone una solución de mesa de ayuda basada en un agente de IA con un flujo de **recuperación aumentada de información (RAG)**, orientado a responder consultas frecuentes, recuperar evidencia documental y derivar casos de baja confianza a un analista humano.

## Objetivo
Diseñar un prototipo funcional que permita:
- clasificar consultas de usuarios,
- recuperar información desde fuentes internas y externas,
- generar una respuesta con fuentes,
- estimar un nivel de confianza,
- escalar al analista cuando la evidencia sea insuficiente.

## Estructura del proyecto
```text
helpdesk-llm-rag-implementos/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── data/
│   ├── internal/
│   └── external/
├── docs/
│   ├── arquitectura.md
│   ├── caso_organizacional.md
│   ├── pruebas.md
│   ├── uso_ia.md
│   └── arquitectura_solucion.png
├── evidencias/
│   └── README.md
├── src/
│   ├── __init__.py
│   ├── classifier.py
│   ├── prompts.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   └── validator.py
└── tests/
    ├── casos_prueba.json
    └── test_pipeline.py
```

## Requisitos
- Python 3.10 o superior

## Instalación
1. Descargar o clonar este repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python -m venv .venv
```

### Windows
```bash
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### macOS / Linux
```bash
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Cómo funciona el prototipo
1. El usuario escribe una consulta.
2. El clasificador detecta la categoría del caso.
3. El motor RAG busca coincidencias en documentos internos y externos.
4. Se seleccionan los documentos más relevantes.
5. El validador calcula un nivel de confianza.
6. Si la confianza es alta, el sistema genera una respuesta con fuentes.
7. Si la confianza es baja, el caso se deriva a un analista.

## Ejemplos de consultas
- ¿Cómo restablezco mi contraseña del sistema?
- No puedo ingresar al portal y aparece error de autenticación.
- ¿Cuál es el horario de atención del soporte?
- Necesito instalar VPN en mi equipo corporativo.


## Integrantes
- Alejandro Paredes
## Enlace del repositorio
- https://github.com/AA406/EncargoN1-IA
