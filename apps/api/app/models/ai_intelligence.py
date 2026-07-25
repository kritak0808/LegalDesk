from datetime import datetime, timezone
from typing import Optional, List
from sqlalchemy import String, Boolean, JSON, DateTime, ForeignKey, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class DocumentEmbedding(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "document_embeddings"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    chunk_text: Mapped[str] = mapped_column(Text, nullable=False)
    vector_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)  # Float array embedding vector
    token_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    page_number: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class ClauseEmbedding(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "clause_embeddings"

    clause_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("clause_library.id", ondelete="SET NULL"), nullable=True, index=True)
    contract_id: Mapped[Optional[str]] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=True, index=True)
    category_name: Mapped[str] = mapped_column(String(100), nullable=False)
    clause_text: Mapped[str] = mapped_column(Text, nullable=False)
    vector_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class Entity(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "entities"

    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    entity_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Organization, Person, Address, Money, Court, Statute, Regulation
    canonical_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class ExtractedEntity(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "extracted_entities"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    entity_id: Mapped[str] = mapped_column(String(36), ForeignKey("entities.id", ondelete="CASCADE"), nullable=False, index=True)
    mention_text: Mapped[str] = mapped_column(String(255), nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, default=0.95, nullable=False)
    page_number: Mapped[int] = mapped_column(Integer, default=1, nullable=False)

    entity: Mapped["Entity"] = relationship("Entity")


class RiskAssessment(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "risk_assessments"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    overall_score: Mapped[float] = mapped_column(Float, nullable=False)  # 0.0 to 100.0
    financial_risk: Mapped[float] = mapped_column(Float, nullable=False)
    legal_risk: Mapped[float] = mapped_column(Float, nullable=False)
    compliance_risk: Mapped[float] = mapped_column(Float, nullable=False)
    privacy_risk: Mapped[float] = mapped_column(Float, nullable=False)
    vendor_risk: Mapped[float] = mapped_column(Float, nullable=False)
    explanation_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)


class ClauseAnalysis(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "clause_analyses"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    clause_title: Mapped[str] = mapped_column(String(255), nullable=False)
    clause_category: Mapped[str] = mapped_column(String(100), nullable=False)
    clause_text: Mapped[str] = mapped_column(Text, nullable=False)
    risk_level: Mapped[str] = mapped_column(String(20), default="Medium", nullable=False)
    deviation_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    suggested_rewrite: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    confidence_score: Mapped[float] = mapped_column(Float, default=0.92, nullable=False)


class AISummary(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "ai_summaries"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    executive_summary: Mapped[str] = mapped_column(Text, nullable=False)
    business_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    legal_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    financial_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    obligation_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


class KnowledgeNode(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "knowledge_nodes"

    node_label: Mapped[str] = mapped_column(String(255), nullable=False)
    node_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Contract, Matter, Organization, Clause, Regulation, Person
    reference_id: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
    properties_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    organization_id: Mapped[str] = mapped_column(String(36), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)


class KnowledgeEdge(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "knowledge_edges"

    source_node_id: Mapped[str] = mapped_column(String(36), ForeignKey("knowledge_nodes.id", ondelete="CASCADE"), nullable=False, index=True)
    target_node_id: Mapped[str] = mapped_column(String(36), ForeignKey("knowledge_nodes.id", ondelete="CASCADE"), nullable=False, index=True)
    relationship_type: Mapped[str] = mapped_column(String(50), nullable=False)  # GOVERNS, BINDS, REFERENCES, REGULATES, CONTAINS
    weight: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)


class ReviewRecommendation(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "review_recommendations"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    recommendation_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Redline, Fallback, Additional Clause, Risk Warning
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    suggested_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    priority: Mapped[str] = mapped_column(String(20), default="Medium", nullable=False)


class NegotiationSuggestion(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "negotiation_suggestions"

    contract_id: Mapped[str] = mapped_column(String(36), ForeignKey("contracts.id", ondelete="CASCADE"), nullable=False, index=True)
    original_clause: Mapped[str] = mapped_column(Text, nullable=False)
    business_friendly_option: Mapped[str] = mapped_column(Text, nullable=False)
    legal_friendly_option: Mapped[str] = mapped_column(Text, nullable=False)
    fallback_option: Mapped[str] = mapped_column(Text, nullable=False)
    explanation: Mapped[str] = mapped_column(Text, nullable=False)
