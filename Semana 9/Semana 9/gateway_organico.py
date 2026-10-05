import os
import httpx
from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI(title="Tienda Orgánica - API Gateway Principal")
security = HTTPBearer(auto_error=False)

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://127.0.0.1:8100")
BACKEND_PRODUCTOS_URL = "http://localhost:9100"

async def get_gateway_secret():
    return {
        "auth_introspection_secret": "organic_intro_secret_789",
        "backend_shared_secret": "organic_gateway_secret_456"
    }

async def authenticate_client(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials is None:
        raise HTTPException(status_code=401, detail="Token Bearer requerido en la cabecera")
    
    gateway_secrets = await get_gateway_secret()
    introspection_secret = gateway_secrets["auth_introspection_secret"]
    
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            response = await client.post(
                f"{AUTH_SERVICE_URL}/introspect",
                json={"token": credentials.credentials},
                headers={"X-Gateway-Auth-Secret": introspection_secret}
            )
    except httpx.ReadError:
        raise HTTPException(status_code=503, detail="Servicio de Autenticación no disponible")
        
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Error al consultar el Servicio de Autenticación")
        
    identity = response.json()
    if not identity.get("active", False):
        raise HTTPException(status_code=401, detail="Token inválido o sesión expirada")
        
    return {
        "user_id": identity["user_id"],
        "username": identity["username"],
        "roles": identity["roles"],
        "backend_secret": gateway_secrets["backend_shared_secret"]
    }

# Endpoint específico GET para productos para evitar problemas en Swagger
@app.get("/api/productos")
async def proxy_productos(request: Request, auth = Depends(authenticate_client)):
    target_url = f"{BACKEND_PRODUCTOS_URL}/productos"
    
    gateway_headers = {
        "X-Gateway-Secret": auth["backend_secret"],
        "X-Authenticated-Client": auth["user_id"],
        "X-Authenticated-User": auth["username"],
        "X-Authenticated-Roles": str(auth["roles"]),
    }
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            upstream = await client.get(
                url=target_url,
                params=request.query_params,
                headers=gateway_headers
            )
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Microservicio de productos no disponible")
        
    response_headers = {}
    if "content-type" in upstream.headers:
        response_headers["content-type"] = upstream.headers["content-type"]
        
    return Response(
        content=upstream.content,
        status_code=upstream.status_code,
        headers=response_headers
    )

# Ruta genérica para el resto
@app.api_route("/api/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def proxy(path: str, request: Request, auth = Depends(authenticate_client)):
    target_url = f"{BACKEND_PRODUCTOS_URL}/{path}"
    
    gateway_headers = {
        "X-Gateway-Secret": auth["backend_secret"],
        "X-Authenticated-Client": auth["user_id"],
        "X-Authenticated-User": auth["username"],
        "X-Authenticated-Roles": str(auth["roles"]),
    }
    
    content_type = request.headers.get("content-type")
    if content_type:
        gateway_headers["content-type"] = content_type
        
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            upstream = await client.request(
                method=request.method,
                url=target_url,
                params=request.query_params,
                headers=gateway_headers
            )
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Microservicio de productos no disponible")
        
    response_headers = {}
    if "content-type" in upstream.headers:
        response_headers["content-type"] = upstream.headers["content-type"]
        
    return Response(
        content=upstream.content,
        status_code=upstream.status_code,
        headers=response_headers
    )