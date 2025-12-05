from typing import Annotated 
from fastapi import Depends
from asyncpg import Connection
from app.core.database import get_db_conn, queries
from app.repositories.auth_repo import AuthRepository
from app.services.auth_service import AuthService
from app.core.config import settings
from app.repositories.project_repo import ProjectRepository
from app.services.project_service import ProjectService
from app.repositories.context_repo import ContextRepository
from app.services.context_service import ContextService
from app.repositories.articule_repo import ArticuleRepository
from app.services.articule_service import ArticuleService
from app.clients.openai_client import OpenAIClient
from app.clients.modal_client import ModalClient
from app.repositories.sota_repo import SotaRepository
from app.services.sota_service import SotaService


#OpenAI dependencies
async def openai_client() -> OpenAIClient:
    return OpenAIClient(api_key=settings.OPEN_API_KEY)

async def modal_client() -> ModalClient:
    return ModalClient()


# Auth dependencies
async def auth_repo(conn: Connection = Depends(get_db_conn)) -> AuthRepository:
    return AuthRepository(conn, queries)

async def auth_service(repo: AuthRepository = Depends(auth_repo)) -> AuthService:
    return AuthService(repo)

# Project dependencies
async def project_repo(conn: Connection = Depends(get_db_conn)) -> ProjectRepository:
    return ProjectRepository(conn, queries)

async def project_service(repo: ProjectRepository = Depends(project_repo)) -> ProjectService:
    return ProjectService(repo)

# Context dependencies
async def context_repo(conn: Connection = Depends(get_db_conn)) -> ContextRepository:
    return ContextRepository(conn, queries)

async def context_service(repo: ContextRepository = Depends(context_repo)) -> ContextService:
    return ContextService(repo)

# Articule dependencies
async def articule_repo(conn: Connection = Depends(get_db_conn)) -> ArticuleRepository:
    return ArticuleRepository(conn, queries)

async def articule_service(repo: ArticuleRepository = Depends(articule_repo), openai_client: OpenAIClient = Depends(openai_client), modal_client: ModalClient = Depends(modal_client)) -> ArticuleService:
    return ArticuleService(repo, openai_client, modal_client)

# SOTA dependencies
async def sota_repo(conn: Connection = Depends(get_db_conn)) -> SotaRepository:
    return SotaRepository(conn, queries)

async def sota_service(repo: SotaRepository = Depends(sota_repo), openai_client: OpenAIClient = Depends(openai_client)) -> SotaService:
    return SotaService(repo, openai_client)


