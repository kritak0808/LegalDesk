# LegalDesk AI — Enterprise AI Legal Operating System & Executive Intelligence Platform (v1.0.0-RC1)

[![Release Candidate](https://img.shields.io/badge/release-v1.0.0--RC1-gold.svg)](https://github.com/kritak0808/roadsense-ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Next.js 15](https://img.shields.io/badge/Next.js-15.1.7-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-emerald.svg)](https://fastapi.tiangolo.com/)
[![Python 3.12](https://img.shields.io/badge/Python-3.12+-3776AB.svg)](https://www.python.org/)
[![TypeScript 5.7](https://img.shields.io/badge/TypeScript-5.7+-3178C6.svg)](https://www.typescriptlang.org/)
[![SOC 2 Ready](https://img.shields.io/badge/Security-SOC%202%20Type%20II-purple.svg)](#security--compliance)

LegalDesk AI is a commercial-grade, multi-tenant AI Legal Operating System and Executive Intelligence Platform designed for enterprise In-House Legal Departments, General Counsels, Law Firms, and Corporate Governance teams.

---

## 🏛️ Platform Architecture

```
+-----------------------------------------------------------------------------------+
|                                  LEGALDESK AI UI                                  |
|   Floating Dock • Workspace Canvas • Tool Drawer • Legal Copilot PRO • Command K   |
+----------------------------------------+------------------------------------------+
                                         | Next.js 15 App Router / REST & WebSockets
                                         v
+-----------------------------------------------------------------------------------+
|                              FASTAPI API GATEWAY (v1)                             |
|  Auth | IAM | Matters | CLM | AI RAG | Litigation | GRC | Workflows | Operations   |
+--------------------+-------------------+--------------------+---------------------+
                     |                   |                    |
                     v                   v                    v
          +------------------+  +-----------------+  +------------------+
          | PostgreSQL DB    |  | Redis Cluster   |  | Celery Workers   |
          | Async SQLAlchemy |  | Cache & Pub/Sub |  | Job Queues       |
          +------------------+  +-----------------+  +------------------+
```

---

## 🌟 Key Platform Modules

### 1. Executive Intelligence & General Counsel Studio
- **Strategic Risk Matrix**: Live monitoring of active litigation exposure ($42.5M), regulatory impact scores, and board compliance indexes.
- **External Counsel Spend Center**: Billing rate card analytics, LEDES-98 invoice validation, and law firm budget variance tracking.
- **Board Reporting Deck Builder**: Automated quarterly legal risk presentation slides and ESG compliance reports.

### 2. Enterprise CLM & AI Contract Intelligence
- **Lifecycle Studio**: End-to-end drafting, redlining, counterparty negotiations, and e-signature envelope tracking (DocuSign / Adobe Sign).
- **Automated AI Redlining**: High-risk clause detection, compliance scoring (94/100), and 1-click fallback clause insertion.
- **Clause Library & Renewal Center**: Standard fallback clause repository and proactive 30/60/90-day contract renewal alerts.

### 3. AI Platform, Vector RAG & Knowledge Graph
- **OCR Pipeline**: Multi-modal document layout extraction and classification.
- **Vector RAG Search**: High-dimensional semantic embeddings search across 50,000+ legal documents.
- **Knowledge Graph**: Interactive graph node networks linking corporate entities, contracts, litigation matters, and regulations.

### 4. Litigation & Evidence Custody Vault
- **Litigation Operating Canvas**: Case detail management, claim tracking, judge/court analytics, and motion filing deadlines.
- **SHA-256 Hash Vault**: Immutable evidence custody logging with cryptographic verification.
- **Settlement Workspace**: NPV financial loss modeling and mediation offer calculators.

### 5. Governance, Risk & Compliance (GRC)
- **Regulatory Frameworks Matrix**: EU AI Act (Article 10), GDPR, SOC 2 Type II, CCPA, HIPAA, ISO 27001 tracking.
- **AI Governance Register**: Model risk card validation, bias testing logs, and human-in-the-loop audit logs.

### 6. Workflow Automation & Process Orchestration
- **Visual DAG Builder**: Approval loops, conditional triggers, SLA timers, and Celery retries.
- **Approval Center**: 1-click authorization queue for contracts, spend caps, and policy exceptions.

### 7. Reliability, SOC Operations & Integration Ecosystem
- **Operations Center**: Real-time platform availability (99.99%), API P99 latency (42ms), and worker node health.
- **Connected Ecosystem**: Bi-directional integration connectors for Microsoft 365, Google Workspace, DocuSign, Salesforce, Workday, and Slack.

---

## 🚀 Quick Start & Installation

### Prerequisites
- **Node.js**: `^20.0.0` or higher
- **Python**: `^3.12` or higher
- **pnpm**: `^9.0.0` or higher
- **Docker & Docker Compose** (Optional for containerized deployment)

### 1. Repository Setup

```bash
git clone https://github.com/kritak0808/roadsense-ai.git
cd LegalDesk
```

### 2. Environment Configuration

Copy the example environment configuration:

```bash
cp .env.example .env
```

### 3. Frontend Setup (`apps/web`)

```bash
cd apps/web
npm install
npm run dev
```
Access the application at `http://localhost:3000`.

### 4. Backend Setup (`apps/api`)

```bash
cd apps/api
python -m venv venv
# On Windows: venv\Scripts\activate | On macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python -m pytest
uvicorn app.main:app --reload --port 8000
```
Access API documentation at `http://localhost:8000/docs`.

### 5. Containerized Docker Deployment

```bash
docker compose up -d --build
```

---

## 🧪 Build & Test Verification Commands

```bash
# Frontend Type Checking & Production Build
npm --prefix apps/web run build

# Frontend Linting
npm --prefix apps/web run lint

# Backend Pytest Test Suite
cd apps/api && python -m pytest
```

---

## 📂 Monorepo Folder Structure

```
LegalDesk/
├── apps/
│   ├── api/                    # FastAPI Backend Application (Python 3.12)
│   │   ├── alembic/            # Database Migrations & Version Tracking
│   │   ├── app/                # Core API Engine (Models, Routers, Services)
│   │   └── tests/              # Pytest Test Suite & Release Certification
│   └── web/                    # Next.js 15 Frontend Web Application (TypeScript)
│       ├── src/
│       │   ├── app/            # App Router Layouts & Pages
│       │   ├── components/     # Production Workspace Components
│       │   ├── store/          # Zustand State Management
│       │   └── styles/         # Glassmorphism & Vanilla CSS System
├── docker/                     # Dockerfiles & Deployment Manifests
├── docs/                       # Architectural & Technical Documentation (55 Docs)
├── docker-compose.yml          # Multi-Container Production Composition
└── README.md                   # Master Platform Documentation
```

---

## 📄 License & Legal Notice

This project is licensed under the [MIT License](LICENSE).  
Copyright © 2026 LegalDesk AI Technologies Inc. All Rights Reserved.
