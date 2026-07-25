# LegalDesk AI — Matter Architecture & Lifecycle Specification

## 1. Overview

**Matter Management** serves as the central operational backbone for LegalDesk AI. All legal activities — including contract reviews, litigation cases, corporate governance resolutions, regulatory investigations, compliance audits, IP filings, privacy incidents, M&A due diligence, and vendor negotiations — attach to one or more **Matters**.

---

## 2. Matter Lifecycle State Machine

```
  [Draft] ──► [Intake] ──► [Assigned] ──► [Under Review] ──► [Active]
                                                                │
     ┌──────────────────────────────────────────────────────────┼──────────────────────────┐
     ▼                                                          ▼                          ▼
[Waiting]                                                   [Escalated]            [Pending Approval]
     │                                                          │                          │
     └──────────────────────────────────────────────────────────┴──────────────────────────┘
                                                                │
                                                                ▼
                                                            [Resolved]
                                                                │
                                                                ▼
                                                            [Closed] ──► [Archived] / [Cancelled]
```

### Lifecycle Transition Rules
1. **Draft / Intake**: Initial record creation and preliminary intake triage.
2. **Assigned**: Primary counsel, supporting counsel, and reviewers are attached.
3. **Under Review / Active**: Counsel actively performing legal work, drafting, or negotiating.
4. **Waiting / Escalated / Pending Approval**: Paused for external responses, escalated to General Counsel, or pending board/GC signoff.
5. **Resolved / Closed**: All deliverables complete; `closed_at` timestamp recorded.

---

## 3. Data Topology & Models

- **`Matter`**: Core record storing `matter_number` (e.g. `MAT-2026-089`), `status`, `priority`, `risk_level`, `risk_score` (0-100), `ai_summary`, and `ai_suggested_actions`.
- **`MatterCategory`**: Configurable categories (Corporate M&A, Employment, Regulatory, Privacy, IP, Litigation, Commercial, Tax, Vendor).
- **`MatterParticipant`**: Assignees mapped to roles (Primary Counsel, Supporting Counsel, Legal Assistant, Compliance Officer, Risk Manager, External Counsel).
- **`MatterTimeline`**: Chronological stream capturing creation, assignments, status transitions, document uploads, hearings, and AI risk audits.
- **`MatterTask`**: Kanban task items with due dates, assignees, subtasks, and priorities (`To Do`, `In Progress`, `In Review`, `Completed`, `Blocked`).
- **`MatterComment`**: Threaded discussion feed with @mentions, pinned comments, internal/external badges, and resolution toggles.
