from fastapi import APIRouter
from app.services.auth_service import AuthService
from app.api.dependencies import auth_service
from app.schemas.auth import UserCreate, LoginRequest
from fastapi import status, Depends 
from app.schemas.base import APIResponse

router = APIRouter()

@router.post(path="/login")
async def login(credentials: LoginRequest, service: AuthService = Depends(auth_service)):

    user_data = await service.login_user(credentials)
    return APIResponse(
        success=True,
        message="Login exitoso",
        data=user_data,
        status_code=200
    )

@router.post(path="/register")
async def register_new_user(
    user: UserCreate,
    service: AuthService = Depends(auth_service)
):
    new_user = await service.register_new_user(user)
    
    return APIResponse(
        success=True,
        message="Usuario registrado exitosamente",
        data=new_user,
        status_code=201
    )
    