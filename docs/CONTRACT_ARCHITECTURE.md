# LegalDesk AI — Contract Lifecycle Management (CLM) Architecture

## 1. Overview

The **Contract Lifecycle Management (CLM) Platform** powers the complete contract lifecycle across enterprise legal departments, law firms, and procurement teams — supporting contract requests, drafting, internal and legal review, multi-party negotiations, multi-tiered approvals, execution, obligation tracking, and renewal management.

---

## 2. Contract Lifecycle State Machine

```
  [Request] ──► [Draft] ──► [Internal Review] ──► [Legal Review] ──► [Business Review]
                                                                          │
     ┌────────────────────────────────────────────────────────────────────┼──────────────────────────┐
     ▼                                                                    ▼                          ▼
[Negotiation]                                                     [Pending Approval]            [Approved]
     │                                                                    │                          │
     └────────────────────────────────────────────────────────────────────┴──────────────────────────┘
                                                                                                     │
                                                                                                     ▼
                                                                                           [Ready for Signature]
                                                                                                     │
                                                                                                     ▼
                                                                                                [Executed]
                                                                                                     │
                                                                                                     ▼
                                                                                                 [Active]
                                                                                                     │
                                                                          ┌──────────────────────────┼──────────────────────────┐
                                                                          ▼                          ▼                          ▼
                                                                  [Renewal Pending]             [Expired]                 [Terminated]
                                                                          │                                                     │
                                                                          ▼                                                     ▼
                                                                      [Renewed]                                             [Archived]
```

---

## 3. Data Schema & Model Topology

- **`Contract`**: Core record storing `contract_number` (e.g. `CTR-2026-089`), `status`, `risk_level`, `deviation_score` (0-100), `total_value`, `annual_value`, `effective_date`, `expiration_date`, `auto_renew`, `renewal_notice_days`, `ai_summary`, `clause_risk_json`, `suggested_clauses_json`, `missing_clauses_json`, and `similarity_index`.
- **`ContractType`**: Configurable types (NDA, MSA, SOW, Employment, Vendor, Supplier, Procurement, Licensing, Partnership, DPA, M&A).
- **`ContractParty`**: Party details (Internal Entity, Customer, Vendor, Supplier, Government, Partner, External Counsel, Subsidiary) with signatory name, email, and tax ID.
- **`ContractVersion`**: Major and minor version control with file hashes, author tracking, diff comparison, and restoration capabilities.
- **`ContractObligation`**: Contractual obligations (Payment, Delivery, SLA Reporting, Notice, Compliance) with owner and due date.
- **`ContractRenewal`**: Upcoming renewal notice calculation engine (e.g. 60-day notice window prior to expiration).
