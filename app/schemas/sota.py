from pydantic import BaseModel
from typing import List, Optional

class Contexto(BaseModel):
    area_general: str
    tema_especifico: str
    problema_investigacion: str
    metodologia_enfoque: str

class Brecha(BaseModel):
    categoria: str
    descripcion: str
    cita_evidencia_original: str

class ArticuloSota(BaseModel):
    doi: str
    autores: List[str]
    titulo: str
    palabras_clave: List[str]
    objetivo_estudio: str
    metodologia: str
    hallazgos: List[str]
    brecha: Brecha

class SotaRequest(BaseModel):
    contexto: Contexto
    articulos: List[ArticuloSota]

class SotaResponse(BaseModel):
    sota: str
    entropia: float
