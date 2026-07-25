# LegalDesk AI — Extended Legal Knowledge Graph Specification

## 1. Overview

The **Extended Legal Knowledge Graph** connects judicial decisions, statutes, regulations, policies, active litigation cases, contracts, research notes, and board resolutions into an interconnected node-and-edge network.

---

## 2. Graph Topology

### Nodes
- `LegalSource`, `Precedent`, `Statute`, `Contract`, `LitigationCase`, `Matter`, `Organization`, `BoardResolution`, `ResearchNotebook`.

### Edges
- `CITES`, `OVERRULES`, `APPLIES_TO`, `GOVERNS`, `REFERENCES`, `DERIVED_FROM`.
