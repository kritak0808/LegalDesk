from typing import Dict, Any
from pydantic import BaseModel


class SystemInfoResponse(BaseModel):
    app_name: str
    version: str
    environment: str
    database_driver: str
    redis_enabled: bool
    celery_enabled: bool
    active_features: Dict[str, bool]
