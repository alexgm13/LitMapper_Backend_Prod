from app.repositories.auth_repo import AuthRepository
from app.clients.openai_client import OpenAIClient
from app.core.security import get_password_hash, verify_password
from app.schemas.auth import UserCreate, UserResponse, LoginRequest
from fastapi import HTTPException

class AuthService:
    def __init__(self, repo: AuthRepository) :
        self.repo = repo

    async def register_new_user(self, user: UserCreate) -> UserResponse:
        password_hash = get_password_hash(user.password)
        try:
            async with self.repo.conn.transaction():
                
                new_user = await self.repo.register_new_user(
                    email=user.email, 
                    password_hash=password_hash, 
                    id_rol=user.id_rol
                )
                
                await self.repo.register_new_profile(
                    nombre=user.nombre,
                    fecha_nacimiento=user.fecha_nacimiento,
                    genero=user.genero,
                    id_usuario=new_user['id_usuario']
                )

            return UserResponse(
                id_usuario=new_user['id_usuario'],
                email=new_user['email'],
                nombre=user.nombre,
                estado=new_user['estado']
            )

        except Exception as e:
            print(f"Error en registro: {e}")
            raise HTTPException(status_code=500, detail="Error interno del servidor")
    
    async def login_user(self, credentials: LoginRequest) -> UserResponse:
        user = await self.repo.get_user_by_email(credentials.email)
        
        if not user:
            raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        
        if not verify_password(credentials.password, user['contrasena']):
            raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        
        if user['estado'] != 'ACTIVO':
             raise HTTPException(status_code=403, detail="Usuario inactivo")

        
        return UserResponse(
            id_usuario=user['id_usuario'],
            email=user['email'],
            nombre=user['nombre'], 
            estado=user['estado']
        )
      
           

        