from typing import List, Optional
from fastapi import APIRouter, Depends, status, Body, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.ocr_service import OCRService
from app.services.parser_service import ParserService
from app.services.risk_engine import RiskEngine
from app.services.embedding_service import EmbeddingService
from app.services.knowledge_graph_service import KnowledgeGraphService
from app.services.negotiation_service import NegotiationService
from app.core.tenant import get_current_tenant, TenantContext

router = APIRouter(prefix="/ai", tags=["AI Contract Intelligence Engine"])


@router.post("/ocr", status_code=status.HTTP_200_OK)
async def process_document_ocr(file_name: str = Body(..., embed=True)):
    """Run enterprise OCR extraction and bounding box page mapping."""
    return await OCRService.process_document_ocr(file_name, "/uploads/" + file_name)


@router.post("/parse", status_code=status.HTTP_200_OK)
async def parse_contract(contract_id: str = Body(..., embed=True), text: str = Body("", embed=True)):
    """Intelligently parse contract attributes, jurisdictions, dates, and indemnities."""
    return await ParserService.parse_legal_contract(contract_id, text)


@router.get("/review/{contract_id}", status_code=status.HTTP_200_OK)
async def get_contract_ai_review(contract_id: str):
    """Retrieve multi-dimensional AI risk evaluation and flagged clause deviations."""
    return await RiskEngine.evaluate_contract_risk(contract_id)


@router.post("/search", status_code=status.HTTP_200_OK)
async def semantic_search(
    query: str = Body(..., embed=True),
    tenant: TenantContext = Depends(get_current_tenant)
):
    """Execute hybrid semantic RAG vector search across indexed contracts and playbooks."""
    return await EmbeddingService.hybrid_semantic_search(query, tenant.tenant_id)


@router.get("/knowledge-graph", status_code=status.HTTP_200_OK)
async def get_knowledge_graph(tenant: TenantContext = Depends(get_current_tenant)):
    """Retrieve legal entity node-and-edge knowledge graph."""
    return await KnowledgeGraphService.get_legal_knowledge_graph(tenant.tenant_id)


@router.post("/negotiate", status_code=status.HTTP_200_OK)
async def negotiate_clause(
    clause_text: str = Body(..., embed=True),
    category: str = Body("Limitation of Liability", embed=True)
):
    """Generate AI clause rewrites, business-friendly vs legal-friendly options, and fallbacks."""
    return await NegotiationService.generate_clause_rewrites(clause_text, category)
