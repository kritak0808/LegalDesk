# LegalDesk AI — Enterprise Security & OWASP Review Specification

## 1. Overview

The **Security Audit** certifies multi-tenant isolation, RBAC `module:action` enforcement, JWT sliding-window session security, AES-256 backup encryption, and SOC threat detection.

---

## 2. Security Mandates

- **JWT Claims**: Validates `user_id`, `org_id`, and `role` claims on every request.
- **Evidence Immutability**: SHA256 hashing on evidence files prevents tamper attempts.
