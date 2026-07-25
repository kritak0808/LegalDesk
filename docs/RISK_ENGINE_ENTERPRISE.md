# LegalDesk AI — Enterprise Risk Register & Heatmap Specification

## 1. Overview

The **Enterprise Risk Register** implements a 5x5 Likelihood x Impact matrix calculating inherent and residual risk scores across Legal, Financial, Operational, Cyber, Privacy, Compliance, Vendor, and AI risk categories.

---

## 2. Risk Matrix & Formulas

$$\text{Inherent Risk Score} = \text{Likelihood (1 to 5)} \times \text{Impact (1 to 5)}$$

$$\text{Residual Risk Score} = \text{Inherent Score} \times (1.0 - \text{Control Effectiveness Percentage})$$

### Heatmap Grid Tiers
- **1 - 5 (Green)**: Low Risk — Monitor
- **6 - 12 (Yellow)**: Medium Risk — Active Mitigation Plan Required
- **15 - 25 (Red)**: High / Critical Risk — Board Level Escalation & Executive Signoff Required
