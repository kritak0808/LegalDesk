# LegalDesk AI — SLA Management & Escalation Specification

## 1. Overview

The **SLA Management Engine** calculates turnaround time limits, enforces business hours calendars, updates active countdown timers, and triggers automated escalations upon SLA breaches.

---

## 2. SLA Countdown Formulas

$$\text{Remaining Time} = \text{SLA Target Hours} - (\text{Current Timestamp} - \text{Execution Start Timestamp})$$
- **Breach Escalation**: Triggers Slack/Email notification and reassigns task to Department Lead.
