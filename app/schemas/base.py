from typing import Optional, Any
from pydantic import BaseModel


class MetaData(BaseModel):
    page: int
    limit: int
    total: int

class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None
    errors: Optional[Any] = None
    meta: Optional[MetaData] = None
    status_code: int