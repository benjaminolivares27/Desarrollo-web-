import os
import secrets

from fastapi import Depends, FastAPI, Header, HTTPException

# Secreto interno compartido con el gateway
INTERNAL_GATEWAY_SECRET = os.getenv("INTERNAL_GATEWAY_SECRET")

if not INTERNAL_GATEWAY_SECRET:
    raise RuntimeError("INTERNAL_GATEWAY_SECRET no esta configurado")

app = FastAPI(
    title = "API de productos",
    description = "API de la Tienda Orgánica enrutada por el API gateway /api/productos"
)

# Valida que la solicitud venga desde el gateway
def verify_gateway(x_gateway_secret: str = Header(default = "")):
    if not secrets.compare_digest(x_gateway_secret, INTERNAL_GATEWAY_SECRET):
        raise HTTPException(status_code = 403, detail = "Solicitud no autorizada desde gateway")

@app.get("/health")
def salud():
    return {
        "estado": "OK",
        "servicio": "API de Productos Orgánicos"
    }

@app.get("/productos")
def productos(
    gateway = Depends(verify_gateway),
    x_authenticated_client: str = Header(default = None)
):
    return {
        "cliente_autenticado": x_authenticated_client,
        "productos": [
            {"id": 1, "nombre": "Tomate Orgánico (Malla 1kg)", "precio": 2500},
            {"id": 2, "nombre": "Palta Hass Chilena (1kg)", "precio": 5990},
            {"id": 3, "nombre": "Lechuga Hidropónica Surtida", "precio": 1200},
            {"id": 4, "nombre": "Espinaca Fresca Orgánica (Bol", "precio": 1800},
            {"id": 5, "nombre": "Zanahoria Orgánica (Atado)", "precio": 1500},
            {"id": 6, "nombre": "Frutos Rojos Congelados (500g)", "precio": 4500},
            {"id": 7, "nombre": "Pan Integral de Masa Madre", "precio": 3200},
            {"id": 8, "nombre": "Miel Pura de Abejas (500g)", "precio": 5000}
        ]
    }