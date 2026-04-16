from __future__ import annotations

def classify_query(query: str) -> str:
    q = query.lower()

    if any(word in q for word in ["contraseña", "clave", "password", "autenticación", "login", "ingresar"]):
        return "Incidente técnico"
    if any(word in q for word in ["vpn", "instalar", "configurar", "acceso", "habilitar"]):
        return "Requerimiento de servicio"
    if any(word in q for word in ["horario", "atención", "soporte", "contacto", "correo"]):
        return "Pregunta frecuente"
    if any(word in q for word in ["permiso", "solicitud", "administrativo"]):
        return "Consulta administrativa"

    return "Caso no clasificable"
