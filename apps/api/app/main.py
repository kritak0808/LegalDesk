from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_v1_router

app = FastAPI(
    title="LegalDesk AI — Enterprise AI Legal Operating System",
    description="Enterprise Multi-Tenant AI Legal Operations & Executive Intelligence Platform",
    version="1.0.0-RC1",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router)


@app.get("/")
async def root():
    return {
        "platform": "LegalDesk AI — Enterprise AI Legal Operating System",
        "version": "1.0.0-RC1",
        "status": "Operational",
        "release_candidate": "v1.0.0-RC1",
        "docs": "/docs"
    }
