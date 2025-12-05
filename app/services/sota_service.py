from app.clients.openai_client import OpenAIClient
from app.repositories.sota_repo import SotaRepository
from app.schemas.sota import SotaRequest
from app.utils.shannon_entropy import calculate_entropy

class SotaService:
    def __init__(self, repo: SotaRepository, openai_client: OpenAIClient):
        self.repo = repo
        self.openai_client = openai_client
    
    async def generate_sota(self, request: SotaRequest):
        contexto = request.contexto.model_dump()
        articulos = [a.model_dump() for a in request.articulos]
        sota = await self.openai_client.generate_sota(contexto, articulos)
        print(sota)
        entropia = calculate_entropy(sota)
        return {
            "sota": sota,
            "entropia": entropia
        }