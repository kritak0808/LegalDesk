# LegalDesk AI — Multi-Dimensional Risk Engine Specification

## 1. Overview

The **Multi-Dimensional AI Risk Engine** analyzes legal contracts against enterprise playbooks, calculating quantitative risk scores (0-100) across 5 risk dimensions.

---

## 2. Risk Dimension Formulas

$$\text{Overall Risk Score} = 0.30 \times \text{Legal} + 0.25 \times \text{Financial} + 0.20 \times \text{Compliance} + 0.15 \times \text{Privacy} + 0.10 \times \text{Vendor}$$

### Risk Tiers
- **0.0 - 25.0**: Low Exposure (Auto-Approval Eligible)
- **25.1 - 60.0**: Medium Exposure (Senior Counsel Review)
- **60.1 - 100.0**: High / Critical Exposure (General Counsel Signoff Required)
