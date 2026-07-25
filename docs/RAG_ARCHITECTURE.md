# LegalDesk AI — RAG Vector Retrieval Architecture

## 1. Overview

The **Retrieval-Augmented Generation (RAG) Engine** tokenizes and indexes contracts, clauses, playbooks, and regulatory documents into dense vector space — enabling semantic hybrid search and context augmentation for LLM responses.

---

## 2. Chunking & Hybrid Retrieval Strategy

- **Semantic Chunking**: 512-token overlapping chunks aligned with clause boundaries.
- **Hybrid Retrieval**: Combines BM25 keyword matching with dense cosine similarity vector search.
- **Tenant Context Filtering**: Vector search scoped by `organization_id`.
