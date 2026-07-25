# LegalDesk AI — Local Development Guide

## Prerequisites
- **Node.js**: `v20.0.0` or higher
- **PNPM**: `v9.0.0` or higher
- **Python**: `3.12.x`
- **Docker**: Docker Desktop with Compose support

---

## Quickstart

### 1. Environment Setup
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

### 2. Frontend Development (`apps/web`)
Install workspace dependencies and run the web app locally:
```bash
cmd /c "pnpm --filter web dev"
```
The workspace shell will be available at `http://localhost:3000`.

### 3. Backend Development (`apps/api`)
Set up a Python virtual environment and run Uvicorn:
```bash
cd apps/api
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Interactive API docs will be available at `http://localhost:8000/docs`.

### 4. Running via Docker Compose
To launch the entire enterprise stack (Web, FastAPI, PostgreSQL, Redis, Celery Worker):
```bash
docker compose up -d --build
```
