import asyncio
import pandas as pd
from io import BytesIO
from app.repositories.articule_repo import ArticuleRepository
from app.clients.openai_client import OpenAIClient
from app.clients.modal_client import ModalClient
from app.utils.convert_to_text import extract_text_from_pdf_stream
from app.utils.shannon_entropy import calculate_entropy
from app.utils.parse_to_sections import parse_markdown_to_sections
from app.utils.timer import execute_with_rate_limit

class ArticuleService:
    def __init__(self, repo: ArticuleRepository, openai_client: OpenAIClient, modal_client: ModalClient):
        self.repo = repo
        self.openai_client = openai_client
        self.modal_client = modal_client

    async def create_new_article(self, articule):
        
        #markdown_result = self.modal_client.parse_pdf(articule)
        text_pdf = extract_text_from_pdf_stream(articule)
        entropy = calculate_entropy(text_pdf)
        response = await execute_with_rate_limit(self.openai_client.analyze_article(text_pdf))
        score = await self.openai_client.get_score(text_pdf, response.brecha.cita_evidencia_original, response.brecha.descripcion)

        return {
            "articule":{
                "details": response,
                "entropy": entropy,
                "score": score
            }
        }
    
    async def insert_articles_csv(self, csv_file):
        
        contents = await csv_file.read()
        df = pd.read_csv(BytesIO(contents))
        df = df.where(pd.notnull(df), None)
        

        all_articles = df.to_dict(orient="records")
        selected_articles = []
        for article in all_articles:

            doi = article.get("DOI")
            abstract = article.get("Abstract")
            year = article.get("Year")
            title = article.get("Title")
            has_doi = doi is not None and isinstance(doi, str) and len(doi) > 0
            has_abstract = abstract is not None and isinstance(abstract, str) and len(abstract) > 0
            
            if has_doi and has_abstract:
                doi_exists = await self.repo.verify_article_doi(doi)
                if doi_exists:
                    record = await self.repo.get_article_doi(doi)
                else:
                    record = await self.repo.insert_article(doi, title, abstract)
            if record:
                selected_articles.append(dict(record))
        return selected_articles
    
    async def analyze_articles(self, articles, area_general, tema_especifico, problema_investigacion, metodologia):
        tasks = []
        for articule in articles:
            # Llamamos a una función auxiliar que maneje la lógica individual
            task = self.analyze_one_article(
                articule, 
                area_general, 
                tema_especifico, 
                problema_investigacion, 
                metodologia
            )
            tasks.append(task)
        articles_analyzed = await asyncio.gather(*tasks, return_exceptions=True)
        valid_results = [art for art in articles_analyzed if not isinstance(art, Exception)]
        
        return valid_results
    
    async def analyze_one_article(self, article, area_general, tema_especifico, problema_investigacion, metodologia):
            abstract = article.get("resumen") 
            title = article.get("titulo") 
            result = await self.openai_client.analize_articules_csv(
                area_general, tema_especifico, problema_investigacion, metodologia, title, abstract
            )
            article["detalle"] = result
            return article
