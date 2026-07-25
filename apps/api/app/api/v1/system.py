from fastapi import APIRouter, status
from app.core.config import settings
from app.schemas.system import SystemInfoResponse

router = APIRouter(prefix="/system", tags=["System Information"])


@router.get("/info", response_model=SystemInfoResponse, status_code=status.HTTP_200_OK)
async def get_system_info():
    """Retrieve platform status and engine configurations."""
    return SystemInfoResponse(
        app_name=settings.APP_NAME,
        version=settings.VERSION,
        environment=settings.APP_ENV,
        database_driver="SQLAlchemy 2.0 Async (PostgreSQL / SQLite)",
        redis_enabled=True,
        celery_enabled=True,
        active_features={
          "rag_clause_indexing": True,
          "eu_ai_act_audits": True,
          "automated_redlining": True,
          "websocket_copilot_stream": True,
        }
    )
