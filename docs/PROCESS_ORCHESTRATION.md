# LegalDesk AI — Process Orchestration & Execution State Machine Specification

## 1. Overview

The **Process Execution Engine** maintains state persistence for long-running legal processes across restarts, handling retries, compensation, timeouts, and pause/resume controls.

---

## 2. Execution State Lifecycle

```
[Trigger Event] ──► [Running] ──► [Pending Approval] ──► [Completed]
                       │                 │
                       ▼                 ▼
                  [Paused]          [SLA Breach / Escalate]
```
