# LegalDesk AI — Litigation & Dispute Resolution Architecture

## 1. Overview

The **Litigation & Dispute Resolution Platform** powers end-to-end commercial litigation, employment disputes, arbitration, mediation, regulatory proceedings, and class action management.

---

## 2. Case Lifecycle State Machine

```
  [Case Intake] ──► [Conflict Check] ──► [Investigation] ──► [Legal Research] ──► [Evidence Collection]
                                                                                           │
     ┌─────────────────────────────────────────────────────────────────────────────────────┼──────────────────────────┐
     ▼                                                                                     ▼                          ▼
[Discovery]                                                                           [Pre-Trial]                  [Trial]
     │                                                                                     │                          │
     └─────────────────────────────────────────────────────────────────────────────────────┴──────────────────────────┘
                                                                                                                      │
                                                                                                                      ▼
                                                                                                                 [Judgment]
                                                                                                                      │
                                                                                           ┌──────────────────────────┼──────────────────────────┐
                                                                                           ▼                          ▼                          ▼
                                                                                       [Appeal]                 [Settlement]                 [Closed]
                                                                                           │                          │                          │
                                                                                           └──────────────────────────┴──────────────────────────┘
                                                                                                                      │
                                                                                                                      ▼
                                                                                                                  [Archived]
```

---

## 3. Data Topology & Models

- **`LitigationCase`**: Stores `case_number` (e.g. `LIT-2026-089`), `case_type`, `status`, `risk_level`, `risk_score`, `claim_amount`, `court_id`, `judge_id`, `matter_id`, `lead_counsel_id`, `filing_date`, `trial_date`, `ai_summary`, `ai_strategy_recommendation`.
- **`Court` & `Judge`**: Court Registry (Delaware Chancery, US District Court SDNY, High Court London) and Judicial Bench assignments.
- **`Evidence`**: Evidence Vault items with SHA256 immutable hashes, custodian logs, admissibility status, and AI contradiction flags.
- **`DiscoveryRequest`**: Interrogatories, Document Requests, and Depositions.
- **`Hearing`**: Court hearing dates, virtual meeting URLs, and outcome summaries.
- **`LegalFiling`**: Complaints, Answers, Motions, Affidavits, Briefs, and Court Orders.
- **`Settlement`**: Settlement offers, target values, confidential terms, and approval workflows.
