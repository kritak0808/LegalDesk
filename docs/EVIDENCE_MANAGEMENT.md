# LegalDesk AI — Evidence Management & Chain of Custody Specification

## 1. Overview

The **Evidence Management System** enforces strict chain of custody protocols, SHA256 file hashing, custodian tracking, and automated AI contradiction analysis across all case evidence.

---

## 2. Chain of Custody Protocol

1. **SHA256 Hash Generation**: Computed automatically upon file upload.
2. **Immutable Log**: `Evidence` model stores `sha256_hash`, `custodian_name`, and `collected_at` timestamp.
3. **Admissibility Tracking**: Tracks `Admissible`, `Challenged`, `Suppressed`, and `Pending Review` states.
4. **AI Contradiction Flags**: Highlights discrepancies between deposition transcripts and contractual terms.
