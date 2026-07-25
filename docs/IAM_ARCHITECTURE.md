# LegalDesk AI — Identity & Access Management (IAM) Architecture

## 1. Multi-Tenancy & Logical Isolation
- **Tenant Context**: Every organization has complete logical isolation.
- **Tenant Middleware**: Extracting `X-Tenant-ID` or JWT claims into `TenantContext` to ensure tenant-aware queries.
- **Hierarchy Support**:
  - `Organization`: Parent/Subsidiary self-referencing relationship (`parent_id`).
  - `Department`: Logical division within tenant (e.g. Litigation, Corporate M&A).
  - `PracticeGroup`: Specialization team (e.g. Data Privacy & AI, IP).
  - `OfficeLocation`: Physical location (e.g. Wilmington HQ, London).

---

## 2. Granular Role-Based Access Control (RBAC)

### Permission Key Format
Permissions are formatted as `module:action` (e.g., `contracts:review`, `matters:create`, `compliance:audit`, `administration:manage`).

### Default Role Mapping Matrix
| Role | Assigned Module:Action Permissions |
|---|---|
| **Super Administrator / Org Owner** | `*:*` (Full System Wildcard) |
| **General Counsel** | `contracts:*`, `cases:*`, `matters:*`, `litigation:*`, `compliance:*`, `policies:*`, `governance:*`, `documents:*`, `approvals:*`, `research:*`, `administration:*`, `analytics:*`, `ai:*` |
| **Legal Director** | `contracts:*`, `matters:*`, `litigation:*`, `compliance:*`, `documents:*`, `approvals:*`, `analytics:*`, `ai:*` |
| **Senior Counsel** | `contracts:create`, `contracts:read`, `contracts:update`, `contracts:review`, `contracts:approve`, `matters:create`, `matters:read`, `matters:update`, `documents:*`, `ai:*` |
| **Associate** | `contracts:read`, `contracts:review`, `matters:read`, `matters:update`, `documents:read`, `research:*`, `ai:*` |
| **Compliance Officer** | `compliance:*`, `policies:*`, `governance:read`, `documents:read`, `analytics:read` |
| **Auditor** | `compliance:read`, `documents:read`, `audit:read`, `governance:read` |
| **External Counsel** | `matters:read`, `matters:update`, `contracts:read`, `contracts:review`, `documents:read` |
| **Guest / Read-Only** | `*:read` |

---

## 3. Session & Security Lifecycle
- **Session Tokens**: Unique session tokens tracking `device_type`, `browser`, `os`, `ip_address`, `country`, and `last_activity_at`.
- **Session Revocation**: Real-time session invalidation via Redis token blacklisting.
- **Account Lockout**: 5 failed login attempts trigger 15-minute lockouts.
- **Audit Logging**: Every identity event (`AUTH_LOGIN`, `ROLE_CHANGED`, `INVITATION_SENT`, `SESSION_REVOKED`) generates immutable audit entries.
