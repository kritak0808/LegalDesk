# LegalDesk AI — Internal Event Bus Architecture

## 1. Overview

The **Internal Event Bus** provides an asynchronous publish-subscribe event backbone that decouples core legal modules from external integrations, audit logging, and WebSockets notification engines.

---

## 2. Event Dispatch Flow

```
[Module Action] ──► [Event Bus Publisher] ──► [Webhook Engine]
                                         ├──► [Audit Log Service]
                                         └──► [WebSockets Real-Time Stream]
```
