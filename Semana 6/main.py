from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from contextlib import asynccontextmanager

# Configuración de la Base de Datos MongoDB
MONGODB_URI = "mongodb://localhost:27017"
DB_NAME = "tienda_organica"  # O el nombre de tu base de datos
COLL_NAME = "productos"

client: AsyncIOMotorClient | None = None
db = None
coll = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global client, db, coll
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client[DB_NAME]
    coll = db[COLL_NAME]
    yield
    client.close()

app = FastAPI(title="Organic Store API", version="1.0.0", lifespan=lifespan)

# ==================== MODELOS (Pydantic) ====================

class Producto(BaseModel):
    nombre: str = Field(min_length=1, description="Nombre del producto")
    precio: float = Field(gt=0, description="Precio mayor a 0")
    stock: int = Field(ge=0, description="Stock disponible")
    tags: List[str] = Field(default_factory=list)
    activo: bool = True

class ProductoIn(BaseModel):
    nombre: str = Field(min_length=1, description="Nombre del producto")
    precio: float = Field(gt=0, description="Precio mayor a 0")
    stock: int = Field(ge=0, description="Stock disponible")
    tags: List[str] = Field(default_factory=list)
    activo: bool = True

class ProductoOut(Producto):
    id: str

def doc_to_productoout(doc) -> ProductoOut:
    return ProductoOut(
        id=str(doc["_id"]),
        nombre=doc["nombre"],
        precio=doc["precio"],
        stock=doc.get("stock", 0),
        tags=doc.get("tags", []),
        activo=doc.get("activo", True)
    )

# ==================== ENDPOINTS (CRUD) ====================

@app.get("/health", tags=["Sistema"])
def health():
    return {"status": "ok"}

# 1. Consultar todos (con filtro opcional 'q')
@app.get("/productos", response_model=List[ProductoOut], tags=["Productos"])
async def consultar_todos(
    q: Optional[str] = Query(None, description="Filtrar por nombre"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
):
    query = {}
    if q:
        query["nombre"] = {"$regex": q, "$options": "i"}
    
    cursor = coll.find(query).skip(skip).limit(limit)
    productos: List[ProductoOut] = []
    async for doc in cursor:
        productos.append(doc_to_productoout(doc))
    return productos

# 2. Consultar por ID
@app.get("/productos/{producto_id}", response_model=ProductoOut, tags=["Productos"])
async def consultar_por_id(producto_id: str):
    if not ObjectId.is_valid(producto_id):
        raise HTTPException(status_code=400, detail="ID inválido")
    
    doc = await coll.find_one({"_id": ObjectId(producto_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    return doc_to_productoout(doc)

# 3. Insertar
@app.post("/productos", response_model=ProductoOut, status_code=201, tags=["Productos"])
async def insertar_producto(producto: ProductoIn):
    res = await coll.insert_one(producto.model_dump())
    doc = await coll.find_one({"_id": res.inserted_id})
    return doc_to_productoout(doc)

# 4. Actualizar (PUT)
@app.put("/productos/{producto_id}", response_model=ProductoOut, tags=["Productos"])
async def actualizar_producto(producto_id: str, producto: ProductoIn):
    if not ObjectId.is_valid(producto_id):
        raise HTTPException(status_code=400, detail="ID inválido")
    
    res = await coll.update_one(
        {"_id": ObjectId(producto_id)}, 
        {"$set": producto.model_dump()}
    )
    
    if res.matched_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
        
    doc = await coll.find_one({"_id": ObjectId(producto_id)})
    return doc_to_productoout(doc)

# 5. Eliminar (DELETE)
@app.delete("/productos/{producto_id}", status_code=204, tags=["Productos"])
async def eliminar_producto(producto_id: str):
    if not ObjectId.is_valid(producto_id):
        raise HTTPException(status_code=400, detail="ID inválido")
        
    res = await coll.delete_one({"_id": ObjectId(producto_id)})
    
    if res.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
        
    return None