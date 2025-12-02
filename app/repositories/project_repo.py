from asyncpg import Connection
from typing import List
from app.schemas.project import ProjectCreate
import traceback

class ProjectRepository:
    def __init__(self, conn: Connection, queries_loader): 
        self.conn = conn
        self.queries = queries_loader

    async def create(self, titulo: str, descripcion: str, id_usuario: int):
        try:
            return await self.queries.create_project(
                self.conn, 
                titulo=titulo, 
                descripcion=descripcion, 
                id_usuario=id_usuario
            )
        except Exception as e:
            raise e

    async def list_by_user(self, id_usuario: int):
        resultado = self.queries.list_by_user(self.conn, id_usuario=id_usuario)

        if hasattr(resultado, "__aiter__"):
            return [row async for row in resultado]
        else:
            return await resultado