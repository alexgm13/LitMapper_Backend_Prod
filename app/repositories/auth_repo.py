from asyncpg import Connection
from datetime import date

class AuthRepository:
    def __init__(self, conn: Connection, queries_loader):
        self.conn = conn
        self.queries = queries_loader

    async def register_new_user(self, email: str, password_hash: str, id_rol: int):
        try:
            return await self.queries.create_user(
                self.conn, 
                email=email, 
                contrasena=password_hash, 
                id_rol=id_rol
            )
        except Exception as e:
            raise e

    async def register_new_profile(self, nombre: str, fecha_nacimiento: date, genero: str, id_usuario: int):
        
        try:
            return await self.queries.create_profile(
                self.conn,
                nombre=nombre,
                fecha_nacimiento=fecha_nacimiento,
                genero=genero,
                id_usuario=id_usuario
            )
        except Exception as e:
            raise e
    
    async def get_user_by_email(self, email: str):
        try:
            return await self.queries.get_user_login_data(self.conn, email=email)
        except Exception as e:
            raise e