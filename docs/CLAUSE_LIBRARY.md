# LegalDesk AI — Clause Library & Playbook Specification

## 1. Overview

The **Clause Library & Fallback Playbook** system manages standardized, pre-approved legal clauses, fallback wording variants, and jurisdiction-specific provisions across all corporate contracts.

---

## 2. Clause Classification & Fallback Architecture

### Clause Types
1. **Standard Clause**: Pre-approved corporate gold-standard wording.
2. **Fallback Clause**: Alternative pre-approved clause used when counterparty rejects standard terms.
3. **High Risk Clause**: Non-standard clause requiring General Counsel review if introduced.
4. **Jurisdiction-Specific Clause**: Tailored provisions for specific legal jurisdictions (e.g. Delaware Chancery, EU GDPR, UK Law).

### Sample Clause Matrix
| Category | Standard Wording | Fallback Wording | Jurisdiction |
|---|---|---|---|
| **Limitation of Liability** | Capped at 2x trailing 12-month fees | Capped at 1x total fees paid under Agreement | Delaware, USA |
| **Data Privacy & AI** | Full EU AI Act Article 10 compliance & model card warranties | Annual third-party audit report delivery | European Union |
| **Termination Notice** | 30-day written notice for convenience | 60-day written notice for convenience | Global |
