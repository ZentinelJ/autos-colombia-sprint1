from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from registro.registro_controller import router as registro_router
from novedad.novedad_controller import router as novedad_router
from vehiculo.vehiculo_controller import router as vehiculo_router

app = FastAPI(title="Autos Colombia API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(registro_router, prefix="/registro", tags=["Registro"])
app.include_router(novedad_router, prefix="/novedad", tags=["Novedad"])
app.include_router(vehiculo_router, prefix="/vehiculo", tags=["Vehiculo"])
