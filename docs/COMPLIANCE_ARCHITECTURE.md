# LegalDesk AI — Enterprise Compliance & GRC Architecture

## 1. Overview

The **Enterprise Governance, Risk & Compliance (GRC) Platform** transforms LegalDesk AI into a complete GRC operating system — providing real-time compliance scorecards, audit readiness tracking, control mapping, and regulatory framework libraries across Fortune 500 legal and compliance departments.

---

## 2. Built-In Regulatory Framework Library

| Framework Code | Name | Issuing Body | Mapped Controls |
|---|---|---|---|
| **EU-AI-ACT** | EU Artificial Intelligence Act (2024/1689) | European Parliament | 28 Controls |
| **GDPR** | General Data Protection Regulation (EU 2016/679) | European Union | 42 Controls |
| **SOC2-TYPE-2** | SOC 2 Type II Security & Trust Services | AICPA | 64 Controls |
| **ISO-27001** | ISO/IEC 27001:2022 Information Security | ISO/IEC | 93 Controls |
| **HIPAA** | Health Insurance Portability and Accountability Act | US HHS | 36 Controls |
| **CCPA** | California Consumer Privacy Act | State of California | 24 Controls |
| **DPDP-ACT** | Digital Personal Data Protection Act | Govt of India | 30 Controls |

---

## 3. Data Topology & Models

- **`RegulatoryFramework` & `FrameworkRequirement`**: Framework definitions and mapped article requirements.
- **`Policy` & `PolicyVersion`**: Policy lifecycle states (`Draft`, `Review`, `Approved`, `Published`, `Retired`) and employee signoff rates.
- **`Control` & `ControlTest`**: Preventive, Detective, Corrective, Technical, and Administrative controls with automated test execution logs.
- **`EnterpriseRisk`**: 5x5 Likelihood x Impact risk matrix with inherent and residual risk scores.
- **`Incident`**: Security breach, privacy failure, and AI governance incident tracking.
- **`BoardMeeting` & `BoardResolution`**: Board resolutions, voting records, meeting minutes, and board pack generation.
- **`AIGovernanceRecord`**: AI Model Registry cards, EU AI Act Article 10 risk classifications, bias audits (99.2% Fairness), and human-in-the-loop signoffs.
