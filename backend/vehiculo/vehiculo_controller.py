from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db import get_connection

router = APIRouter()

class VehiculoCreateDTO(BaseModel):
    placa: str
    marca: str
    modelo: str

@router.post("")
def create_vehiculo(vehiculo: VehiculoCreateDTO):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO vehiculo (placa, marca, modelo)
            VALUES (%s, %s, %s)
            ON CONFLICT (placa) DO NOTHING
            """,
            (vehiculo.placa, vehiculo.marca, vehiculo.modelo)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Vehículo procesado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{placa}")
def get_vehiculo(placa: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT placa, marca, modelo FROM vehiculo WHERE placa = %s", (placa,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if not row:
            raise HTTPException(status_code=404, detail="La placa ingresada no existe en el sistema.")
        return {"placa": row[0], "marca": row[1], "modelo": row[2]}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
