from datetime import datetime, timedelta, timezone
import os
import secrets

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI(
    title="Tienda Orgánica - Servicio de Autenticación",
    description="Microservicio de autenticación, gestión de sesiones y emisión de tokens"
)

# Usuarios propios de la Tienda Orgánica
USERS = {
    "benjamin": {
        "password": "organic_admin_2026",
        "user_id": "ORG-USR-001",
        "roles": ["admin", "cliente"]
    },
    "ana": {
        "password": "organic_pass_123",
        "user_id": "ORG-USR-002",
        "roles": ["cliente"]
    },
    "carlos": {
        "password": "organic_pass_456",
        "user_id": "ORG-USR-003",
        "roles": ["cliente"]
    },
}

SESSIONS = {}
TOKEN_LIFETIME_MINUTES = 20

AUTH_INTROSPECTION_SECRET = os.getenv("AUTH_INTROSPECTION_SECRET")

if not AUTH_INTROSPECTION_SECRET:
    raise RuntimeError("AUTH_INTROSPECTION_SECRET no está configurado en el entorno")

def secreto_valido(recibido: str) -> bool:
    return secrets.compare_digest(
        recibido.encode("utf-8"),
        AUTH_INTROSPECTION_SECRET.encode("utf-8")
    )

class LoginRequest(BaseModel):
    username: str
    password: str

class IntrospectionRequest(BaseModel):
    token: str

@app.post("/login")
def login(request: LoginRequest, x_gateway_auth_secret: str = Header(default="")):
    if not secreto_valido(x_gateway_auth_secret):
        raise HTTPException(status_code=403, detail="Gateway no autorizado para autenticación")
    
    user = USERS.get(request.username)
    if user is None or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Credenciales de usuario inválidas")
    
    access_token = secrets.token_urlsafe(32)
    expiration = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_LIFETIME_MINUTES)
    
    SESSIONS[access_token] = {
        "user_id": user["user_id"],
        "username": request.username,
        "roles": user["roles"],
        "expires_at": expiration
    }
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": TOKEN_LIFETIME_MINUTES * 60
    }

@app.post("/introspect")
def introspect(request: IntrospectionRequest, x_gateway_auth_secret: str = Header(default="")):
    if not secreto_valido(x_gateway_auth_secret):
        raise HTTPException(status_code=403, detail="Gateway no autorizado")
    
    session = SESSIONS.get(request.token)
    if session is None or datetime.now(timezone.utc) > session["expires_at"]:
        SESSIONS.pop(request.token, None)
        return {"active": False}
    
    return {
        "active": True,
        "user_id": session["user_id"],
        "username": session["username"],
        "roles": session["roles"],
        "expires_at": session["expires_at"].isoformat()
    }

@app.post("/logout")
def logout(request: IntrospectionRequest, x_gateway_auth_secret: str = Header(default="")):
    if not secreto_valido(x_gateway_auth_secret):
        raise HTTPException(status_code=403, detail="Gateway no autorizado")
    SESSIONS.pop(request.token, None)
    return {"message": "Sesión cerrada correctamente en Tienda Orgánica"}

@app.get("/health")
def health(x_gateway_auth_secret: str = Header(default="")):
    if not secreto_valido(x_gateway_auth_secret):
        raise HTTPException(status_code=403, detail="Gateway no autorizado")
    return {"status": "OK", "service": "Tienda Orgánica - Auth Service"}