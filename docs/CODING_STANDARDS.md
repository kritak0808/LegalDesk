# LegalDesk AI — Coding Standards & Guidelines

## 1. General Principles
- **No Shortcuts**: Every feature must be production-grade with full typing, error handling, and documentation.
- **Strict Typing**:
  - TypeScript strict mode enabled (`noImplicitAny`, `strictNullChecks`).
  - Python 3.12 type hints required on all function signatures (`def foo(param: str) -> bool:`).

## 2. Frontend Conventions (Next.js & React 19)
- **Feature Component Structure**: Place reusable primitives in `src/components/ui/` and workspace layout components in `src/components/workspace/`.
- **State Management**:
  - Use **Zustand** for local workspace UI state (panel toggles, dock navigation, active matter).
  - Use **TanStack Query** for async data fetching and server-state caching.
- **Styling**: Use CSS variables for themes and glassmorphism. Merge Tailwind classes using `cn(...)`.

## 3. Backend Conventions (FastAPI & Python 3.12)
- **Layered Architecture**:
  - `Router` -> `Service` -> `Repository` -> `SQLAlchemy Model`.
- **Dependency Injection**: Pass database sessions and current user dependencies via `Depends()`.
- **Exception Handling**: Raise domain exceptions inheriting from `LegalDeskException`.
