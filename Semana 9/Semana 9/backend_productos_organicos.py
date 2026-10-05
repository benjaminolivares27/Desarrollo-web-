import os
import secrets
from fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI(
    title="Tienda Orgánica - Backend Productos",
    description="Microservicio de inventario y catálogo ecológico enrutado por API Gateway"
)

INTERNAL_GATEWAY_SECRET = os.getenv("INTERNAL_GATEWAY_SECRET")

if not INTERNAL_GATEWAY_SECRET:
    raise RuntimeError("INTERNAL_GATEWAY_SECRET no está configurado")

def verify_gateway(x_gateway_secret: str = Header(default="")):
    if not secrets.compare_digest(x_gateway_secret, INTERNAL_GATEWAY_SECRET):
        raise HTTPException(status_code=403, detail="Acceso denegado: Gateway no autorizado")

@app.get("/health", dependencies=[Depends(verify_gateway)])
def health():
    return {"status": "OK", "service": "Backend Productos Orgánicos"}

@app.get("/productos", dependencies=[Depends(verify_gateway)])
def productos(
    x_authenticated_client: str | None = Header(default=None),
    x_authenticated_user: str | None = Header(default=None),
    x_authenticated_roles: str | None = Header(default=None),
):
    return {
        "identity": {
            "user_id": x_authenticated_client,
            "username": x_authenticated_user,
            "roles": x_authenticated_roles
        },
        "productos": [
            {"id": 1, "nombre": "Tomate Orgánico (Malla 1kg)", "precio": 2500, "categoria": "Verduras"},
            {"id": 2, "nombre": "Palta Hass Chilena (1kg)", "precio": 5990, "categoria": "Frutas"},
            {"id": 3, "nombre": "Lechuga Hidropónica Surtida", "precio": 1200, "categoria": "Verduras"},
            {"id": 4, "nombre": "Espinaca Fresca Orgánica (Bol)", "precio": 1800, "categoria": "Hojas Verdes"},
            {"id": 5, "nombre": "Zanahoria Orgánica (Atado)", "precio": 1500, "categoria": "Raíces"}
        ]
    }