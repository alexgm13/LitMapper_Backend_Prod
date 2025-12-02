from app.repositories.project_repo import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectResponse
from typing import List

class ProjectService:
    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    async def create_new_project(self, data: ProjectCreate) -> ProjectResponse:
        new_project = await self.repo.create(
            titulo=data.titulo,
            descripcion=data.descripcion,
            id_usuario=data.id_usuario
        )
        return ProjectResponse(**dict(new_project))

    async def list_user_projects(self, id_usuario: int) -> List[ProjectResponse]:
        records = await self.repo.list_by_user(id_usuario)
        return [ProjectResponse(**dict(row)) for row in records]