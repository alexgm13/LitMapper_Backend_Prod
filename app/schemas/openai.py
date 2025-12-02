from typing import List, Optional, Literal, Dict
from pydantic import BaseModel, Field
from enum import Enum





class GapCategory(str, Enum):
    CONCEPTUAL = "Conceptuales"
    METODOLOGICA = "Metodológicas"
    DE_DATOS = "De Datos"
    DE_COMPRENSION = "De Comprensión"
    DE_INTERVENCION = "De Intervención"

class GapAnalysis(BaseModel):
    categoria: GapCategory = Field(
        ..., 
        description="El tipo de brecha según la taxonomía definida (Conceptual, Metodológica, etc.)"
    )
    descripcion: str = Field(
        ..., 
        description="Explicación concisa de la brecha o limitación identificada."
    )
    seccion: str = Field(
        ..., 
        description="La sección del paper donde se encontró la brecha (ej: Introducción, Discusión). Debe ser una sección del paper original. COPY-PASTE"
    )
    cita_evidencia_original: str = Field(
        ...,
        description="COPY-PASTE la cita original del paper."
    )

class ScientificAnalysisResponse(BaseModel):
    doi: str 
    autores: List[str] 
    titulo: str 
    palabras_clave: List[str] 
    objetivo_estudio: str 
    metodologia: str 
    hallazgos: List[str]
    brecha: GapAnalysis

class StatusGap(str, Enum):
    APROBADO = "Aprobado"       
    OBSERVADO = "Observado"     
    RECHAZADO = "Rechazado"     

class GapAnalysisFinal(BaseModel):
    score_factualidad_cita: float = Field(
        ..., 
        ge=0.0, 
        le=1.0,
        description="Puntaje (0.0 a 1.0). 0.0 indica que la cita es una alucinación (no existe en el texto). 1.0 es una coincidencia exacta."
    )
    feedback_cita: str = Field(
        ...,
        description="Explica si se encontró el texto en el documento o detalla el error de búsqueda."
    )

    # --- DIMENSIÓN 2: LA DESCRIPCIÓN (Veracidad Semántica) ---
    score_factualidad_descripcion: float = Field(
        ..., 
        ge=0.0, 
        le=1.0,
        description="Puntaje (0.0 a 1.0). Evalúa si la explicación simplificada dice la verdad respecto a la cita original."
    )
    feedback_descripcion: str = Field(
        ...,
        description="Señala si hay distorsiones, exageraciones o mentiras en la explicación didáctica."
    )

    # --- RESULTADOS FINALES ---
    veredicto: StatusGap = Field(
        ...,
        description="Decisión final del auditor: Aprobado, Observado o Rechazado."
    )
    
    puntaje_promedio: float = Field(
        ...,
        ge=0.0, 
        le=1.0,
        description="Promedio simple de los scores anteriores."
    )