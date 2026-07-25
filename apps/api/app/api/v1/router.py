from fastapi import APIRouter
from app.api.v1.health import router as health_router
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.organizations import router as orgs_router
from app.api.v1.roles import router as roles_router
from app.api.v1.invitations import router as invitations_router
from app.api.v1.sessions import router as sessions_router
from app.api.v1.security import router as security_router
from app.api.v1.audit_logs import router as audit_router
from app.api.v1.matters import router as matters_router
from app.api.v1.contracts import router as contracts_router
from app.api.v1.ai import router as ai_router
from app.api.v1.litigation import router as litigation_router
from app.api.v1.grc import router as grc_router
from app.api.v1.research import router as research_router
from app.api.v1.workflows import router as workflows_router
from app.api.v1.executive import router as executive_router
from app.api.v1.integrations import router as integrations_router
from app.api.v1.operations import router as operations_router
from app.api.v1.system import router as system_router

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(health_router)
api_v1_router.include_router(auth_router)
api_v1_router.include_router(users_router)
api_v1_router.include_router(orgs_router)
api_v1_router.include_router(roles_router)
api_v1_router.include_router(invitations_router)
api_v1_router.include_router(sessions_router)
api_v1_router.include_router(security_router)
api_v1_router.include_router(audit_router)
api_v1_router.include_router(matters_router)
api_v1_router.include_router(contracts_router)
api_v1_router.include_router(ai_router)
api_v1_router.include_router(litigation_router)
api_v1_router.include_router(grc_router)
api_v1_router.include_router(research_router)
api_v1_router.include_router(workflows_router)
api_v1_router.include_router(executive_router)
api_v1_router.include_router(integrations_router)
api_v1_router.include_router(operations_router)
api_v1_router.include_router(system_router)
