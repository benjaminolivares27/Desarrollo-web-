from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="API Gateway - Proyecto Orgánico", version="1.0")

# Habilitar CORS para que tu página web pueda consumir la API sin problemas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CLIENTES_SERVICE_URL = "http://localhost:9001"

@app.get("/api/health")
async def gateway_health():
    return {"gateway": "active"}

@app.get("/api/clientes")
async def proxy_obtener_clientes():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{CLIENTES_SERVICE_URL}/clientes")
            return response.json()
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Servicio de clientes no disponible")

@app.post("/api/clientes")
async def proxy_crear_cliente(payload: dict):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{CLIENTES_SERVICE_URL}/clientes", json=payload)
            return response.json()
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Servicio de clientes no disponible")