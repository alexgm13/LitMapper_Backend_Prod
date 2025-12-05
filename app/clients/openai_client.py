from typing import Dict
from openai import AsyncOpenAI
from app.core.config import settings
from app.schemas.openai import ScientificAnalysisResponse, GapAnalysis, GapAnalysisFinal, ArticuleAnalyzed, SoTA
import json

class OpenAIClient:
    def __init__(self, api_key: str):
        self.client = AsyncOpenAI(api_key=api_key)
    
    async def analyze_article(self, text: str):
        try:
            response = await self.client.responses.parse(
                model="gpt-4o-mini",
                temperature=0,
                prompt={    
                    "id": "pmpt_6927c78563cc8195b026175128a4622904bad3888b42c046",
                    "version": "10",
                    "variables": {
                        "papper": text
                    }
                },
                text_format= ScientificAnalysisResponse
            )
            return response.output_parsed
        except Exception as e:
            print(f"Error llamando a OpenAI: {e}")
            raise e
    
    async def get_gaps(self, text: str):
        try:
            response = await self.client.responses.parse(
                model="gpt-4o",
                prompt={    
                    "id": "pmpt_6928d7b0ec908196a42e9b5c921155260c4b22459eaadf5c",
                    "version": "6",
                    "variables": {
                        "papper": text
                    }
                },
                text_format= GapAnalysis
            )
            return response.output_parsed
        except Exception as e:
            print(f"Error llamando a OpenAI: {e}")
            raise e

    async def get_score(self, text: str, cita_evidencia: str, descripcion: str):
        try:
            response = await self.client.responses.parse(
                model="gpt-4o",
                prompt={    
                    "id": "pmpt_6928e8e9102081938cf5a1737d8ef83001f7cdaa14c17911",
                    "version": "5",
                    "variables": {
                        "texto_completo_paper": text,
                        "cita_evidencia": cita_evidencia,
                        "descripcion": descripcion
                    }
                },
                text_format= GapAnalysisFinal
            )
            return response.output_parsed
        except Exception as e:
            print(f"Error llamando a OpenAI: {e}")
            raise e
    
    async def analize_articules_csv(self, area_general: str, tema_especifico: str, problema_investigacion: str, metodologia_enfoque: str, titulo: str, resumen: str):
        try:
            response = await self.client.responses.parse(
            model="gpt-4o-mini",
            prompt={
                "id": "pmpt_68f9aa116718819392fb28a8e837530b0b951877105ae7c8",
                "version": "5",
                "variables": {
                    "area_general": area_general,
                    "tema_especifico": tema_especifico,
                    "problema_investigacion": problema_investigacion,
                    "metodologia_enfoque": metodologia_enfoque,
                    "titulo": titulo,
                    "resumen": resumen
                }
            },
            text_format= ArticuleAnalyzed
            )
            return response.output_parsed
        except Exception as e:
            print(f"Error llamando a OpenAI: {e}")
            raise e
    
    async def generate_sota(self, contexto: dict, articulos: list):
        try:
            lista_resultados_json = json.dumps(articulos)
            contexto_json = json.dumps(contexto)
            response = await self.client.responses.create(
            model="gpt-4o",
            prompt={
                "id": "pmpt_690ac478cdb481958f36f4e0f3fceda50f0e106ba5d73b63",
                "version": "7",
                "variables": {
                    "contexto": contexto_json,
                    "lista_resultados_json": lista_resultados_json
                }
            },
            )   
            return response.output_text
        except Exception as e:
            print(f"Error llamando a OpenAI: {e}")
            raise e