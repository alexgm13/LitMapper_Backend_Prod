from fastapi import APIRouter, Depends
from app.api.dependencies import context_service
from app.schemas.context import ContextCreate
from app.services.context_service import ContextService
from app.schemas.base import APIResponse

router = APIRouter()

@router.post(path="/")
async def insert_context(
    contexto: ContextCreate,
    service: ContextService = Depends(context_service)
):
    result = await service.insert_context(contexto)
    return APIResponse(
        success=True,
        message="Contexto insertado exitosamente",
        data=result,
        status_code=201
    )