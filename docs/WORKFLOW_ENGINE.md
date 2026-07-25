# LegalDesk AI — Visual Workflow & Process Engine Architecture

## 1. Overview

The **Enterprise Workflow & Process Engine** serves as the master orchestration layer connecting every module across LegalDesk AI (Matters, Contracts, Litigation, GRC, Research, and AI Reviews).

---

## 2. Built-In Visual Node Types

| Node Type | Category | Description |
|---|---|---|
| **Start** | Trigger | Initiates workflow (Contract Created, Case Filed, Schedule) |
| **Approval** | Action | Sequential or parallel multi-tier approval routing |
| **AI Review** | Intelligence | Automatic OCR, RAG analysis, and risk scoring |
| **Condition** | Decision | Business rule evaluation (If Contract Value >= $1M) |
| **Webhook** | Integration | Outbound HTTP webhook payload delivery |
| **End** | Terminal | Completes workflow and updates target entity status |
