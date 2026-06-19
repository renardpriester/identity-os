# IdentityOS Core

## Purpose

IdentityOS Core is the simulated IAM operating system engine for the IdentityOS project.

This folder will contain the working local prototype that processes identity lifecycle events, maps identities to role packages, determines required access, evaluates approval requirements, generates mock tickets, creates audit evidence, and produces outputs that can later feed the Streamlit dashboard.

---

## Core Objective

The objective of IdentityOS Core is to demonstrate the following workflow:

```text id="l4tnoo"
HR Event
   ↓
IdentityOS Event Processor
   ↓
Role Package Mapping
   ↓
Policy Decision Engine
   ↓
Access Assignment Plan
   ↓
Approval and Ticketing Logic
   ↓
Audit Evidence Output
   ↓
Dashboard Metrics
```

---

## What IdentityOS Core Will Simulate

IdentityOS Core will simulate:

* Joiner events
* Mover events
* Leaver events
* Contractor onboarding
* Contractor expiration
* Role package mapping
* Access assignment planning
* Approval-required decisions
* Mock ticket creation
* Risk scoring
* Access drift detection
* Audit evidence generation
* Dashboard-ready outputs

---

## Initial MVP Scope

The first MVP will focus on a simple Joiner workflow.

A sample HR event will include:

```text id="u8e9wx"
Name
Department
Job Title
Location
Worker Type
Manager
Start Date
```

IdentityOS Core will then determine:

```text id="5ixikl"
Role Package
Required Access
Approval Requirements
Risk Level
Mock Ticket
Audit Evidence
Dashboard Output
```

---

## Planned Folder Structure

```text id="k9pzja"
identityos-core/
├── README.md
├── data/
│   ├── role-packages.json
│   └── sample-hr-events.json
├── engine/
│   └── process-identity-event.py
└── outputs/
    ├── tickets/
    ├── evidence/
    └── dashboard/
```

---

## Planned Core Files

| File                               | Purpose                                           |
| ---------------------------------- | ------------------------------------------------- |
| `data/role-packages.json`          | Defines role packages and access bundles.         |
| `data/sample-hr-events.json`       | Provides sample Joiner, Mover, and Leaver events. |
| `engine/process-identity-event.py` | Processes events and generates decisions.         |
| `outputs/tickets/`                 | Stores mock ticket records.                       |
| `outputs/evidence/`                | Stores audit evidence output.                     |
| `outputs/dashboard/`               | Stores dashboard-ready output.                    |

---

## Example Joiner Input

```json id="j3blxk"
{
  "event_id": "EVT-JOINER-001",
  "event_type": "joiner",
  "display_name": "Sarah Johnson",
  "department": "Finance",
  "job_title": "Financial Analyst",
  "location": "Miami",
  "worker_type": "Employee",
  "manager": "Michelle Carter",
  "start_date": "2026-07-01"
}
```

---

## Example IdentityOS Output

```json id="h5d8re"
{
  "event_id": "EVT-JOINER-001",
  "role_package": "Finance Analyst",
  "required_access": [
    "Base Employee Access",
    "Finance SharePoint",
    "Financial Reporting Portal"
  ],
  "approval_required": true,
  "approval_owner": "Finance Application Owner",
  "risk_level": "Medium",
  "ticket_created": true,
  "audit_evidence_generated": true
}
```

---

## Safety Boundary

IdentityOS Core is a local simulation engine.

It does not make production identity changes.

Future Microsoft Graph integration should only be tested in a lab tenant and should include dry-run mode, approval checks, least privilege, logging, rollback planning, and audit evidence.

---

## Portfolio Value

IdentityOS Core demonstrates how IAM architecture can become an operating model.

It shows how identity lifecycle events can drive access decisions, approval workflows, ticketing records, evidence generation, and dashboard visibility.

This moves IdentityOS from architecture documentation into a working IAM orchestration prototype.

---

## Summary

IdentityOS Core is the beginning of the working identity operating system layer.

> IdentityOS Core turns identity lifecycle events into access decisions, tickets, evidence, and dashboard outputs.
