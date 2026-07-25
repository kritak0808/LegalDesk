# LegalDesk AI — Directory & Workspace Structure

## Root Monorepo Structure

```
LegalDesk/
├── apps/
│   ├── web/                     # Next.js 15 Enterprise Legal Workspace UI
│   │   ├── src/
│   │   │   ├── app/             # App Router pages, layout, and providers
│   │   │   ├── components/      # Workspace components (FloatingDock, Canvas, Copilot, CmdK)
│   │   │   │   ├── ui/          # Primitive UI design system elements
│   │   │   │   └── workspace/   # Legal workspace modules
│   │   │   ├── store/           # Zustand state stores (workspace, copilot, theme)
│   │   │   ├── styles/          # Design tokens, CSS variables, glassmorphism
│   │   │   └── lib/             # Utility helpers & API clients
│   │   ├── next.config.js
│   │   ├── tailwind.config.ts
│   │   └── package.json
│   │
│   └── api/                     # FastAPI Python 3.12 Backend Platform
│       ├── app/
│       │   ├── api/v1/          # Modular API routers (health, auth, users, orgs, system)
│       │   ├── core/            # Settings, security, database, redis, logging, exceptions
│       │   ├── models/          # SQLAlchemy ORM models (User, Organization, Role, AuditLog)
│       │   ├── schemas/         # Pydantic request/response validation schemas
│       │   ├── repositories/    # Data access layer pattern (Base, User, Org)
│       │   ├── services/        # Business logic services (AuthService, UserService)
│       │   ├── middleware/      # Request ID & Audit logging middlewares
│       │   ├── websockets/      # Real-time WebSocket connection manager
│       │   ├── worker/          # Celery background task definitions
│       │   └── main.py          # FastAPI application entrypoint
│       ├── alembic/             # Database migration environment
│       └── requirements.txt
│
├── docker/                      # Multi-stage Dockerfiles
│   ├── Dockerfile.web
│   └── Dockerfile.api
│
├── docs/                        # Monorepo architecture & engineering documentation
│   ├── ARCHITECTURE.md
│   ├── FOLDER_STRUCTURE.md
│   ├── CODING_STANDARDS.md
│   └── DEVELOPMENT_GUIDE.md
│
├── docker-compose.yml           # Full-stack container orchestration
├── package.json                 # Monorepo package configuration
├── pnpm-workspace.yaml          # PNPM monorepo workspace definition
└── .env.example                 # Root environment variables template
```
