# LegalDesk AI — Architecture Specification

## Overview

**LegalDesk AI** is an enterprise-grade AI Legal Operating System designed for corporate legal departments, law firms, compliance auditors, and governance teams. Phase 1 establishes a modular, highly scalable monorepo structure.

---

## Architectural Principles

1. **Workspace-First UI Philosophy**:
   - Eschews traditional left-sidebar SaaS admin templates.
   - Features a **Floating Navigation Dock**, **Immersive Working Canvas**, **Dockable Tool Drawers**, **Adaptive Right AI Legal Copilot**, and a **`Cmd+K` Command Palette**.

2. **Clean Separation of Concerns**:
   - **Frontend Layer**: Next.js 15 App Router, React 19, Tailwind CSS, Framer Motion, Zustand state management, and TanStack Query.
   - **API Layer**: FastAPI Python 3.12 with async controller routing, dependency injection (`Depends`), and domain exception handling.
   - **Domain & Persistence Layer**: SQLAlchemy 2.0 Async ORM with repository pattern abstractions.
   - **Asynchronous Task & Streaming Layer**: Celery worker integration backed by Redis broker, alongside WebSockets for real-time AI response streaming.

3. **Multi-Tenancy & Security First**:
   - Role-Based Access Control (RBAC) foundation (`roles`, `permissions`, `user_organizations`).
   - JWT authentication tokens (Access + Refresh tokens).
   - Immutable audit logging for governance & regulatory compliance.

---

## High-Level Topology

```
                  ┌──────────────────────────────┐
                  │    Next.js 15 Workspace Shell │
                  │  (Floating Dock, Copilot,    │
                  │   Canvas & Command Palette)  │
                  └──────────────┬───────────────┘
                                 │ HTTP / WebSockets
                                 ▼
                  ┌──────────────────────────────┐
                  │   FastAPI Enterprise API V1   │
                  │   (Auth, Health, Users, Orgs)│
                  └──────┬───────────────┬───────┘
                         │               │
            SQLAlchemy   │               │ Redis / Async
            Async        ▼               ▼
           ┌────────────────┐   ┌────────────────┐
           │ PostgreSQL DB  │   │  Redis Cache & │
           │ & Alembic      │   │ Celery Task Q  │
           └────────────────┘   └────────────────┘
```
