import time
from app.worker.celery_app import celery_app
from app.core.logging import logger


@celery_app.task(name="tasks.index_legal_document_rag")
def index_legal_document_rag(document_id: str, file_path: str):
    logger.info("background_task_started", task="index_legal_document_rag", document_id=document_id)
    # Background RAG indexing simulation
    time.sleep(2)
    logger.info("background_task_completed", task="index_legal_document_rag", document_id=document_id)
    return {"status": "indexed", "document_id": document_id}


@celery_app.task(name="tasks.run_compliance_audit_job")
def run_compliance_audit_job(organization_id: str, regulation_type: str):
    logger.info("background_task_started", task="run_compliance_audit_job", org=organization_id, reg=regulation_type)
    time.sleep(3)
    logger.info("background_task_completed", task="run_compliance_audit_job", org=organization_id, reg=regulation_type)
    return {"status": "audit_complete", "score": 98.4, "regulation": regulation_type}
