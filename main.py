from fastapi import FastAPI
from app.api.v1 import auth_route, project_route, context_route, articule_route, sota_route
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from contextlib import asynccontextmanager
from app.core.database import init_db_pool, close_db_pool
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.errors import http_exception_handler, validation_exception_handler, general_exception_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db_pool()
    yield
    await close_db_pool()

app = FastAPI(
    title="LitMapper Backend",
    description="API para el análisis de artículos científicos usando IA Generativa",
    version="1.0.0",
    lifespan=lifespan
)

#Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.URL_CORS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Excepciones
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

#Rutas
app.include_router(auth_route.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(project_route.router, prefix="/api/v1/project", tags=["Project"])
app.include_router(context_route.router, prefix="/api/v1/context", tags=["Context"])
app.include_router(articule_route.router, prefix="/api/v1/articule", tags=["Articule"])
app.include_router(sota_route.router, prefix="/api/v1/sota", tags=["SOTA"])

@app.get("/")
def status():
    return {
        "status": "OK",
        "message" : "LitMapper is running"
    }
