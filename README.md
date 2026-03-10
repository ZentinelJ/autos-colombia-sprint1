# Autos Colombia - Sprint 1

Sistema de gestión de parqueadero por mensualidad llamado **"Autos Colombia"**.

## Descripción

Sistema web para la gestión de operaciones diarias del parqueadero "Autos Colombia". Permite registrar entradas y salidas de vehículos, reportar novedades sobre vehículos activos y consultar el historial por placa. Desarrollado como parte del Sprint 1.

## Stack

| Capa | Tecnología |
|---|---|
| Frontend | HTML + CSS + JS vanilla |
| Backend | Python 3.11 + FastAPI + Uvicorn |
| Base de datos | PostgreSQL 15 |
| Conector BD | psycopg2 (SQL puro, sin ORM) |

## Estructura

```
autos_colombia/
├── backend/
│   ├── main.py
│   ├── db.py
│   ├── registro/
│   ├── novedad/
│   └── vehiculo/
├── frontend/
│   ├── login.html
│   └── app.html
├── sql/
│   └── init.sql
└── README.md
```

## Requisitos previos

- Python 3.11+
- PostgreSQL 15+
- pip: `fastapi`, `uvicorn`, `psycopg2-binary`, `pydantic`

## Ejecutar en Windows

El proyecto está optimizado para Linux. En Windows puede presentarse un error
de codificación (`UnicodeDecodeError`) causado por psycopg2 al leer archivos
de configuración de PostgreSQL que contienen caracteres especiales en Latin-1.

### Solución requerida — Activar UTF-8 a nivel de sistema

1. Panel de Control → **Región** → pestaña **Administrativo**
2. Clic en **Cambiar configuración regional del sistema**
3. Marcar ✅ **"Beta: usar Unicode UTF-8 para compatibilidad con idiomas en todo el mundo"**
4. Reiniciar Windows

Este cambio es necesario una sola vez. Sin él, psycopg2 falla antes de
establecer la conexión con la base de datos independientemente de cualquier
configuración en el código.

### Arrancar el backend en Windows

Desde CMD:
```cmd
cd C:\ruta\al\proyecto\backend
python -m uvicorn main:app --reload
```

> **Importante:** evitar rutas con caracteres especiales como guiones largos (`–`).

## Paso 1 — Crear y poblar la base de datos

```bash
# Opción A: ejecutar el script completo (crea la BD y las tablas)
psql -U postgres -f sql/init.sql

# Opción B: si la BD ya existe, solo crear tablas
psql -U postgres -d "Autos_Colombia" -f sql/init.sql
```

### Poblar la base de datos en Windows

Abrir **pgAdmin** → conectarse al servidor local → crear la base de datos:
1. Clic derecho en **Databases** → **Create** → **Database**
2. Name: `Autos_Colombia`, Owner: `postgres` → Guardar
3. Clic derecho sobre `Autos_Colombia` → **Query Tool**
4. Abrir el archivo `sql/init.sql` → ejecutar con **F5**

O desde CMD usando psql:
```cmd
psql -U postgres -f sql\init.sql
## Paso 2 — Instalar dependencias Python

```bash
pip install fastapi uvicorn psycopg2-binary pydantic
```

## Paso 3 — Arrancar el backend

```bash
cd backend
PYTHONPATH=. python3 -m uvicorn main:app --reload
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

## Problemas comunes

**uvicorn: orden no encontrada**  
Usar `python3 -m uvicorn main:app --reload` en lugar de `uvicorn` directo.

**Error de autenticación PostgreSQL**  
Cambiar la contraseña del usuario postgres:
```bash
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
```

**ModuleNotFoundError al arrancar**  
Asegurarse de ejecutar uvicorn desde la carpeta `backend/` con:
```bash
PYTHONPATH=. python3 -m uvicorn main:app --reload
```

**Posesión dudosa detectada (Git)**  
Si Git lanza este error al trabajar como root sobre una carpeta de otro usuario:
```bash
git config --global --add safe.directory /ruta/al/proyecto
```
