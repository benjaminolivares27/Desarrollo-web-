import os
import secrets

from fastapi import Depends, FastAPI, Header, HTTPException

# Secreto interno compartido con el gateway
INTERNAL_GATEWAY_SECRET = os.getenv("INTERNAL_GATEWAY_SECRET")

if not INTERNAL_GATEWAY_SECRET:
    raise RuntimeError("INTERNAL_GATEWAY_SECRET no esta configurado")

app = FastAPI(
    title = "API de clientes",
    description = "API de clientes de la Tienda Orgánica enrutada por el API gateway /api/clientes"
)

# Valida que la solicitud venga desde el gateway
def verify_gateway(x_gateway_secret: str = Header(default = "")):
    if not secrets.compare_digest(x_gateway_secret, INTERNAL_GATEWAY_SECRET):
        raise HTTPException(status_code = 403, detail = "Solicitud no autorizada desde gateway")

@app.get("/health")
def salud():
    return {
        "estado": "OK",
        "servicio": "API de Clientes"
    }

@app.get("/clientes")
def clientes(
    gateway = Depends(verify_gateway),
    x_authenticated_client: str = Header(default = None)
):
    return {
        "cliente_autenticado": x_authenticated_client,
        "clientes": [
            {"id": 1, "nombre": "Ana Gómez", "correo": "ana@example.com"},
            {"id": 2, "nombre": "Carlos Pérez", "correo": "carlos@example.com"},
            {"id": 3, "nombre": "Benjamín Olivares", "correo": "benjamin@example.com"},
            {"id": 4, "nombre": "María Silva", "correo": "maria.silva@example.com"},
            {"id": 5, "nombre": "José Morales", "correo": "jose.morales@example.com"},
            {"id": 6, "nombre": "Camila Rojas", "correo": "camila.rojas@example.com"}
        ]
    }