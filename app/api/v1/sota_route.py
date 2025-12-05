from fastapi import APIRouter, Depends
from app.api.dependencies import sota_service
from app.services.sota_service import SotaService
from app.schemas.base import APIResponse
from app.schemas.sota import SotaRequest

router = APIRouter()

@router.post("/")
async def sota(
    request: SotaRequest,
    service: SotaService = Depends(sota_service)):
    sota_data = await service.generate_sota(request)
    return APIResponse(
        success=True,
        message="SOTA generated",
        data=sota_data,
        status_code=200,
    )