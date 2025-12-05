from asyncpg import Connection


class ArticuleRepository():
    def __init__(self, conn: Connection, queries_loader):
        self.conn = conn
        self.queries = queries_loader
    
    async def verify_article_doi(self, doi):
        return await self.queries.existing_doi(self.conn, doi=doi)

    async def get_article_doi(self, doi):
        return await self.queries.get_articule_doi(self.conn, doi=doi)
    
    async def insert_article(self, doi, titulo, resumen):
        return await self.queries.create_articulo(self.conn, doi=doi, titulo=titulo, resumen=resumen)
    
