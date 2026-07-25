import time
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from app.core.database import get_db
from app.core.config import settings
from app.core.redis import get_redis_client
from app.schemas.health import HealthResponse, DetailedHealthResponse, ServiceStatus

router = APIRouter(prefix="/health", tags=["Health & Diagnostics"])


@router.get("", response_model=HealthResponse, status_code=status.HTTP_200_OK)
async def health_check():
    """Basic health check endpoint."""
    return HealthResponse(
        status="healthy",
        service=settings.APP_NAME,
        environment=settings.APP_ENV,
        version=settings.VERSION,
    )


@router.get("/liveness", status_code=status.HTTP_200_OK)
async def liveness():
    """Kubernetes / Docker liveness probe."""
    return {"status": "alive"}


@router.get("/readiness", status_code=status.HTTP_200_OK)
async def readiness(db: AsyncSession = Depends(get_db)):
    """Kubernetes / Docker readiness probe checking DB connectivity."""
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "ready"}
    except Exception as e:
        return {"status": "not_ready", "reason": str(e)}


@router.get("/detailed", response_model=DetailedHealthResponse, status_code=status.HTTP_200_OK)
async def detailed_health_check(db: AsyncSession = Depends(get_db)):
    """Detailed health check for database, redis, and system components."""
    services = {}

    # Database Check
    db_start = time.time()
    try:
        await db.execute(text("SELECT 1"))
        db_latency = round((time.time() - db_start) * 1000, 2)
        services["database"] = ServiceStatus(status="healthy", latency_ms=db_latency, details={"driver": "async"})
    except Exception as exc:
        services["database"] = ServiceStatus(status="unhealthy", details={"error": str(exc)})

    # Redis Check
    redis_start = time.time()
    try:
        r = await get_redis_client()
        if r is not None:
            redis_latency = round((time.time() - redis_start) * 1000, 2)
            services["redis"] = ServiceStatus(status="healthy", latency_ms=redis_latency)
        else:
            services["redis"] = ServiceStatus(status="degraded", details={"info": "redis connection unavailable"})
    except Exception as exc:
        services["redis"] = ServiceStatus(status="degraded", details={"error": str(exc)})

    overall_status = "healthy"
    if any(s.status == "unhealthy" for s in services.values()):
        overall_status = "unhealthy"
    elif any(s.status == "degraded" for s in services.values()):
        overall_status = "degraded"

    return DetailedHealthResponse(
        status=overall_status,
        timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        environment=settings.APP_ENV,
        version=settings.VERSION,
        services=services,
    )
