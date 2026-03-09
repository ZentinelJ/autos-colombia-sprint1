# Autos Colombia - Sprint 1

Sistema de gestión de parqueadero por mensualidad llamado **"Autos Colombia"**.

## Requisitos previos
- Python 3.11+
- PostgreSQL 15+
- pip: `fastapi`, `uvicorn`, `psycopg2-binary`, `pydantic`

## Paso 1 — Crear y poblar la base de datos
```bash
# Opción A: ejecutar el script completo (crea la BD y las tablas)
psql -U postgres -f sql/init.sql

# Opción B: si la BD ya existe, solo crear tablas
psql -U postgres -d "Autos_Colombia" -f sql/init.sql
```

## Paso 2 — Instalar dependencias Python
```bash
pip install fastapi uvicorn psycopg2-binary pydantic
```

## Paso 3 — Arrancar el backend
```bash
cd backend
uvicorn main:app --reload
# El servidor queda en http://localhost:8000
```

## Paso 4 — Abrir el frontend
Abrir `frontend/login.html` directamente en el navegador (doble clic o arrastrar al navegador).  
También funciona con Live Server de VS Code.

## Credenciales
- **Login:** `demoapp` / `midemo1234`
- **PostgreSQL:** `postgres` / `postgres`

## Documentación de la API
`http://localhost:8000/docs`
