import asyncio
from app.repositories.articule_repo import ArticuleRepository
from app.clients.openai_client import OpenAIClient
from app.clients.modal_client import ModalClient
from app.utils.convert_to_text import extract_text_from_pdf_stream
from app.utils.shannon_entropy import calculate_entropy
from app.utils.parse_to_sections import parse_markdown_to_sections

class ArticuleService:
    def __init__(self, repo: ArticuleRepository, openai_client: OpenAIClient, modal_client: ModalClient):
        self.repo = repo
        self.openai_client = openai_client
        self.modal_client = modal_client

    async def create_new_articule(self, articule):
        
        markdown_result = self.modal_client.parse_pdf(articule)
        
        #text = extract_text_from_pdf_stream(articule)
        entropy = calculate_entropy(markdown_result)
        sections = parse_markdown_to_sections(markdown_result)
        response = await self.openai_client.analyze_article(markdown_result)
        #doi = response.doi
        #autores = ", ".join(response.autores)
        #titulo = response.titulo
        #palabras_clave = ", ".join(response.palabras_clave)
        #objetivo_estudio = response.objetivo_estudio
        #metodologia = response.metodologia
        #hallazgos = ", ".join(response.hallazgos)
        #gap = await self.openai_client.get_gaps(markdown_result)
        #await asyncio.sleep(60)
        #score = await self.openai_client.get_score(text, gap.analisis.cita_evidencia_original, gap.analisis.descripcion, gap.analisis.propuesta_investigacion)

        return {
            #"gap": gap,
            #"score": score,
            "response": response,
            "entropy": entropy,
            #"content_markdown": markdown_result,
            "sections": sections
        }