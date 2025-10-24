# DATA ANALYTIC

## Python- SQL

---

### Start project

1. Install `Docker` \[and (optional) `lazydocker`\]
1. Install `uv`
1. Run `uv venv`

---

1. To run the project: `uv run main.py`
1. To run `Jupyter`: `uv run jupyter lab`
   (This is more convenient for connecting to the local database)

### Example

Using `asyncpg` only

```python
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(
        host="localhost",
        database="tu_base_de_datos",
        user="tu_usuario",
        password="tu_contraseña"
    )

    try:
        version = await conn.fetchval("SELECT version()")
        print("Versión:", version)

        usuarios = await conn.fetch("SELECT * FROM usuarios LIMIT 5")
        for usuario in usuarios:
            print(usuario['nombre'], usuario['email'])

        await conn.execute(
            "INSERT INTO usuarios (nombre, email) VALUES ($1, $2)",
            "María", "maria@email.com"
        )

    finally:
        await conn.close()

asyncio.run(main())

```

Using `psycopg2` only

```python
import psycopg2
from psycopg2.extras import DictCursor

def conectar_bd():
    return psycopg2.connect(
        host="localhost",
        database="tu_base_de_datos",
        user="tu_usuario",
        password="tu_contraseña"
    )

with conectar_bd() as conn:
    with conn.cursor(cursor_factory=DictCursor) as cur:
        # Consulta que retorna diccionarios
        cur.execute("SELECT * FROM productos WHERE precio > %s", (100,))
        productos = cur.fetchall()

        for producto in productos:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}")

```
