from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Microservicio de Clientes", version="1.0")

# Modelo de datos para un cliente
class Cliente(BaseModel):
    id: int
    nombre: str
    correo: str
    telefono: Optional[str] = None

# Base de datos simulada en memoria
db_clientes = [
    Cliente(id=1, nombre="Ana Gómez", correo="ana@example.com", telefono="912345678"),
    Cliente(id=2, nombre="Carlos Pérez", correo="carlos@example.com", telefono="987654321")
]

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "clientes"}

@app.get("/clientes", response_model=List[Cliente])
def obtener_clientes():
    return db_clientes

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: int):
    for cliente in db_clientes:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.post("/clientes", response_model=Cliente, status_code=201)
def crear_cliente(cliente: Cliente):
    for c in db_clientes:
        if c.id == cliente.id:
            raise HTTPException(status_code=400, detail="El ID del cliente ya existe")
    db_clientes.append(cliente)
    return cliente