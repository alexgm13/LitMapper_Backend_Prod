from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from typing import Any

def create_error_response(status_code: int, message: str, errors: Any = None) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
            "data": None,
            "errors": errors,
            "status_code": status_code
        },
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    return create_error_response(exc.status_code, exc.detail)

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors_dict = {}
    for error in exc.errors():
        field = error["loc"][-1] if error["loc"] else "unknown"
        msg = error["msg"]
        errors_dict[field] = msg

    return create_error_response(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        message="Error de validación en los datos",
        errors=errors_dict
    )

async def general_exception_handler(request: Request, exc: Exception):
    print(f"Error Crítico no controlado: {exc}") 
    return create_error_response(
        status_code=500,
        message="Error interno del servidor",
        errors=str(exc) 
    )