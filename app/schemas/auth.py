from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    id_rol: int = 1
    nombre: str
    fecha_nacimiento: date
    genero: str

class UserResponse(BaseModel):
    id_usuario: int
    email: EmailStr
    nombre: str
    estado: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str