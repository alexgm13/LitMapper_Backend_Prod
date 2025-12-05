from fastapi import APIRouter, File, UploadFile, Depends, Form
from app.schemas.base import APIResponse
from app.services.articule_service import ArticuleService
from app.api.dependencies import articule_service

router = APIRouter()

@router.post("/")
async def create_articule(file: UploadFile = File(...), service: ArticuleService = Depends(articule_service)):
    
    text = await file.read()
    articule = await service.create_new_article(text)
    
    return APIResponse(
        success=True,
        message="Articule created",
        data=articule,
        status_code=200,
    )

@router.post("/detalle")
async def get_articule(
    file: UploadFile = File(...),
    id_proyecto: int = Form(...),
    area_general: str = Form(...),
    tema_especifico: str = Form(...),
    problema_investigacion: str = Form(...),
    metodologia: str = Form(...),
    service: ArticuleService = Depends(articule_service),
):
    articules = await service.insert_articles_csv(file)
    print(articules)
    articule_analyzed = await service.analyze_articles(articules, area_general, tema_especifico, problema_investigacion, metodologia)
    return APIResponse(
        success=True,
        message="Articule retrieved",
        data=articule_analyzed,
        status_code=200,
    )   

