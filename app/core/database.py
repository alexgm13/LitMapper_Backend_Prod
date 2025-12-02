import aiosql
import asyncpg
from app.core.config import settings


queries = aiosql.from_path("sql/queries", "asyncpg")

db_pool = None

async def init_db_pool():
    global db_pool
    
    print(f"Conectando a la BD...")
    try:
        db_pool = await asyncpg.create_pool(settings.DATABASE_URL)
        print("Conexión exitosa a PostgreSQL")
    except Exception as e:
        print(f"Error conectando a la BD: {e}")
        raise e

async def close_db_pool():
    if db_pool:
        await db_pool.close()
        print("Conexión a BD cerrada.")

async def get_db_conn():
    if not db_pool:
        raise RuntimeError("La base de datos no está inicializada")
    
    async with db_pool.acquire() as conn:
        yield conn