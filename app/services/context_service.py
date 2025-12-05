from app.repositories.context_repo import ContextRepository
from asyncpg import Connection
from app.schemas.context import ContextCreate, ContextResponse

class ContextService:
    def __init__(self, repo: ContextRepository):
        self.repo = repo

    async def insert_context(self, contexto: ContextCreate):
        try:
            id_contexto = await self.repo.insert_context(
                id_proyecto=contexto.id_proyecto,
                area_general=contexto.area_general,
                tema_especifico=contexto.tema_especifico,
                problema_investigacion=contexto.problema_investigacion,
                metodologia=contexto.metodologia
            )
            result = await self.repo.get_context(contexto.id_proyecto)
            return ContextResponse(**result)
        except Exception as e:  
            raise e