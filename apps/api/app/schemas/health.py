from typing import Dict, Any, Optional
from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    service: str
    environment: str
    version: str


class ServiceStatus(BaseModel):
    status: str  # 'healthy' | 'degraded' | 'unhealthy'
    latency_ms: Optional[float] = None
    details: Optional[Dict[str, Any]] = None


class DetailedHealthResponse(BaseModel):
    status: str
    timestamp: str
    environment: str
    version: str
    services: Dict[str, ServiceStatus]
