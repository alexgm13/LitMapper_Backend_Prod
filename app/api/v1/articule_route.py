from fastapi import APIRouter, File, UploadFile, Depends
from app.schemas.base import APIResponse
from app.services.articule_service import ArticuleService
from app.api.dependencies import articule_service

router = APIRouter()

@router.post("/")
async def create_articule(file: UploadFile = File(...), service: ArticuleService = Depends(articule_service)):
    
    text = await file.read()
    articule = await service.create_new_articule(text)
    
    return APIResponse(
        success=True,
        message="Articule created",
        data=articule,
        status_code=200,
    )
