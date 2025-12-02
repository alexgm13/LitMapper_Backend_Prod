from typing import Dict
from openai import AsyncOpenAI
from app.core.config import settings
from app.schemas.openai import ScientificAnalysisResponse, GapAnalysis, GapAnalysisFinal
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

    async def get_score(self, text: str, cita_evidencia: str, descripcion: str, propuesta_investigacion: str):
        try:
            response = await self.client.responses.parse(
                model="gpt-4o",
                prompt={    
                    "id": "pmpt_6928e8e9102081938cf5a1737d8ef83001f7cdaa14c17911",
                    "version": "4",
                    "variables": {
                        "texto_completo_paper": text,
                        "cita_evidencia": cita_evidencia,
                        "descripcion": descripcion,
                        "propuesta_investigacion": propuesta_investigacion
                    }
                },
                text_format= GapAnalysisFinal
            )
            return response.output_parsed
        except Exception as e:
            print(f"Error llamando a OpenAI: {e}")
            raise e