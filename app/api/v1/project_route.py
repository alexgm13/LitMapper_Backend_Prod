from fastapi import APIRouter, Depends, Path
from app.api.dependencies import project_service
from app.schemas.project import ProjectCreate, ProjectResponse
from fastapi import Query
from app.schemas.base import APIResponse
from app.services.project_service import ProjectService


router = APIRouter()


@router.post("/")
async def create_project(
    project_data: ProjectCreate,
    service: ProjectService = Depends(project_service)
):
    new_project = await service.create_new_project(project_data)
    
    return APIResponse(
        success=True,
        message="Proyecto creado exitosamente",
        data=new_project,
        status_code=201
    )

@router.get("/{user_id}")
async def list_projects(
    service: ProjectService = Depends(project_service),
    user_id: int = Path(..., description="ID del usuario para filtrar proyectos")
):
    projects_list = await service.list_user_projects(user_id)
    
    return APIResponse(
        success=True,
        message="Lista de proyectos obtenida",
        data=projects_list,
        status_code=200
    )