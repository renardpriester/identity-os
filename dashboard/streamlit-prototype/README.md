# IdentityOS

**IdentityOS** is a simulated identity operations platform built to demonstrate how modern Identity and Access Management teams can manage workforce identity lifecycle events, access approvals, provisioning workflows, governance evidence, and executive reporting.

The project models an end-to-end IAM operating system where HR identity intake, Joiner/Mover/Leaver workflows, access package recommendations, approval tickets, provisioning actions, access reviews, and audit evidence all connect into one command center.

---

## Project Purpose

IdentityOS was built as a hands-on IAM architecture portfolio project.

The goal is to demonstrate how an identity platform can:

* Capture new hire identity details from HR
* Evaluate workforce attributes such as department, job title, location, and employment type
* Recommend access packages based on policy logic
* Assign approval workflows and risk levels
* Generate approval tickets
* Track provisioning readiness
* Simulate account creation, access assignment, access removal, and offboarding
* Record audit evidence across the identity lifecycle
* Support access review campaigns and certification decisions
* Export evidence for governance, security, and audit review

---

## Core Platform Modules

### IdentityOS Product Header

The application includes a branded IdentityOS header, logo, version banner, and system status indicators.

Current version:

**IdentityOS v0.2 — Lifecycle Workflow, Governance, Reporting, and Persistence Prototype**

---

### Demo Scenario Launcher

The Demo Scenario Launcher allows users to instantly populate the platform with a complete sample identity lifecycle scenario.

This includes:

* HR intake records
* Approval tickets
* Provisioning history
* Joiner audit logs
* Mover audit logs
* Leaver audit logs
* Access review campaigns
* Access review decisions
* Reporting and evidence export data

This makes the platform demo-ready without requiring manual data entry.

---

### HR New Hire Onboarding Workflow

This module simulates the HR front door for the Joiner lifecycle.

HR can submit a new hire into IdentityOS, and the platform evaluates the user’s workforce attributes to recommend access, assign risk, determine approval routing, and prepare provisioning actions.

The workflow shows:

* New Hire Profile
* IdentityOS Decision
* Recommended Access Package
* Approval Workflow
* Risk Level
* Provisioning Action
* Joiner Lifecycle Timeline
* Manual Process vs IdentityOS Process
* Audit Evidence Preview

---

### Access Package Policy Engine

The Access Package Policy Engine maps workforce attributes to standardized access packages.

Example mappings include:

* HR Specialist → HR Core Access
* Finance Analyst → Finance Core Access
* Security Analyst → Security Operations Access
* IT Support Technician → IT Support Access
* Executive Assistant → Executive Support Access

If IdentityOS cannot match the department and job title, the access request is routed to manual IAM review.

---

### Joiner Access Decision Audit Log

IdentityOS records access recommendation decisions for audit visibility.

The audit log captures:

* Timestamp
* Department
* Job Title
* Recommended Access Package
* Approval Workflow
* Risk Level
* Provisioning Action
* Decision Source

---

### Mover Workflow Engine

The Mover Workflow Engine simulates what happens when an employee changes departments or job roles.

IdentityOS compares the employee’s current access package to the future-state access package and determines whether access should be retained, removed, assigned, or reviewed.

This helps demonstrate access creep prevention.

---

### Leaver Workflow Engine

The Leaver Workflow Engine simulates employee offboarding.

IdentityOS evaluates the employee’s current access, department, role, and departure type to recommend offboarding actions.

The workflow supports:

* Standard offboarding
* Immediate high-risk offboarding
* Account disablement
* Access package removal
* Group membership removal
* Active session revocation
* Audit evidence capture

---

### Approval Queue and Ticketing Simulation

IdentityOS converts lifecycle decisions into approval tickets.

Tickets include:

* Ticket ID
* Lifecycle Stage
* Employee
* Request Type
* Access Package or Control
* Approval Owner
* Risk Level
* Recommended Action
* Ticket Status
* Provisioning Status

This simulates the bridge between identity governance decisions and operational ticketing workflows.

---

### Provisioning Action Center

The Provisioning Action Center simulates execution of approved IAM actions.

Once a ticket is approved and marked ready for provisioning, IdentityOS displays the required provisioning steps and records the execution result.

Supported lifecycle actions include:

* Joiner provisioning
* Mover access changes
* Leaver access removal
* Manual review outcomes

---

### Governance Control Center

The Governance Control Center provides a consolidated view of identity governance posture.

It summarizes:

* Open approvals
* High-risk identity events
* Manual reviews
* Provisioning failures
* Immediate offboarding items
* Audit evidence records
* Governance health score
* Operational response plan

This module supports executive-level identity risk reporting.

---

### Access Review Campaign Center

IdentityOS includes an access certification workflow that simulates periodic access reviews.

The Access Review Campaign Center can generate review campaigns, identify review candidates, and record reviewer decisions.

Review decisions include:

* Approve / Retain Access
* Revoke Access
* Modify Access
* Escalate to Security
* Requires Additional Evidence

This demonstrates identity governance capabilities such as access certification, access creep review, high-risk access validation, and audit evidence retention.

---

### Reporting and Evidence Export Center

The Reporting and Evidence Export Center allows IdentityOS workflow records to be exported for audit, governance, security, and executive reporting.

Exportable evidence includes:

* HR identity intakes
* Approval queue records
* Provisioning history
* Joiner audit logs
* Mover audit logs
* Leaver audit logs
* Access review campaigns
* Access review decisions
* Executive evidence summary

Exports are available in CSV and JSON formats.

---

### Data Persistence Layer

IdentityOS includes a local JSON persistence layer that allows workflow records to survive application restarts.

Persisted data includes:

* HR intakes
* Approval tickets
* Provisioning history
* Joiner audit logs
* Mover audit logs
* Leaver audit logs
* Access review campaigns
* Access review decisions
* Persistence events

This moves IdentityOS beyond temporary session-only behavior and closer to platform-like operation.

---

## Technologies Used

* Python
* Streamlit
* Pandas
* Plotly
* JSON
* Git / GitHub
* Local file-based persistence

---

## How to Run the Project

From the Streamlit prototype folder, run:

```powershell
python -m streamlit run app.py
```

Project folder:

```text
dashboard/streamlit-prototype
```

---

## Recommended Demo Flow

1. Start IdentityOS.
2. Click **Load Full Demo Scenario** near the top of the app.
3. Review the HR New Hire Onboarding Workflow.
4. Review the Approval Queue.
5. Review the Provisioning Action Center.
6. Review the Governance Control Center.
7. Review the Access Review Campaign Center.
8. Review the Reporting and Evidence Export Center.
9. Download CSV or JSON evidence exports.

This flow demonstrates the full lifecycle:

```text
HR Intake
↓
Access Recommendation
↓
Approval Ticket
↓
Provisioning Action
↓
Governance Review
↓
Access Certification
↓
Evidence Export
```

---

## IAM Concepts Demonstrated

IdentityOS demonstrates several important IAM and identity governance concepts:

* Joiner / Mover / Leaver lifecycle management
* Role-based access package recommendations
* Attribute-based access decision logic
* Access approval workflows
* Provisioning readiness tracking
* Access creep prevention
* Offboarding controls
* High-risk identity event handling
* Access review campaigns
* Access certification decisions
* Governance health scoring
* Audit evidence retention
* Evidence export for compliance and security review

---

## Portfolio Summary

IdentityOS is a simulated identity lifecycle operations platform that connects HR intake, access package recommendations, approval ticketing, provisioning execution, access reviews, governance scoring, reporting, and audit evidence into one command center.

The project is designed to demonstrate IAM engineering, identity governance, workflow automation, and architecture-level thinking.
