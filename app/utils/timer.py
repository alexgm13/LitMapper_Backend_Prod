import asyncio
import time

async def execute_with_rate_limit(coroutine, min_seconds=60):
    start_time = time.time()
    result = await coroutine  # Ejecuta la llamada a la API
    elapsed = time.time() - start_time
    
    wait_time = min_seconds - elapsed
    if wait_time > 0:
        print(f"Esperando {wait_time:.2f}s restantes...")
        await asyncio.sleep(wait_time)
        
    return result