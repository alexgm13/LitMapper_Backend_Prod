from pydantic import BaseModel


class ContextCreate(BaseModel):
    id_proyecto: int
    area_general: str
    tema_especifico: str
    problema_investigacion: str
    metodologia: str

class ContextResponse(BaseModel):
    id_contexto: int
    id_proyecto: int
    area_general: str
    tema_especifico: str
    problema_investigacion: str
    metodologia: str