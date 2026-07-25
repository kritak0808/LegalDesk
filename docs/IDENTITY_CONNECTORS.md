# LegalDesk AI — Identity Connectors & SCIM Provisioning Specification

## 1. Overview

The **Identity Integration Layer** supports Single Sign-On (SSO) via Microsoft Entra ID, Okta, Google Workspace, and SAML 2.0 / OpenID Connect, alongside automated SCIM 2.0 user lifecycle provisioning.

---

## 2. SCIM 2.0 User Lifecycle

- **Automatic User Provisioning**: Syncs new employee accounts, departments, and roles.
- **Deprovisioning Event**: Revokes sessions immediately upon employee termination in Okta / Entra ID.
