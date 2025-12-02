from pydantic import BaseModel
from datetime import datetime

class ProjectCreate(BaseModel):
    titulo: str
    descripcion: str
    id_usuario: int 

class ProjectResponse(BaseModel):
    id_proyecto: int
    titulo: str
    fase: int
    estado: str
    fecha_creacion: datetime
    
