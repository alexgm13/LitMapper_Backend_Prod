from asyncpg import Connection

class ContextRepository:
    def __init__(self, conn: Connection, queries_loader):
        self.conn = conn
        self.queries = queries_loader
    
    async def insert_context(self, id_proyecto: int, area_general: str, tema_especifico: str, problema_investigacion: str, metodologia: str):
        try:
            return await self.queries.insert_context(
                self.conn,
                id_proyecto=id_proyecto,
                area_general=area_general,
                tema_especifico=tema_especifico,
                problema_investigacion=problema_investigacion,
                metodologia=metodologia
            )
        except Exception as e:
            raise e
    
    async def get_context(self, id_proyecto: int):
        try:
            return await self.queries.get_context(
                self.conn,
                id_proyecto=id_proyecto
            )
        except Exception as e:
            raise e