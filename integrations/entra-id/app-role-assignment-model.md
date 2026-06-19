# App Role Assignment Model

## Purpose

This document defines how IdentityOS could model Microsoft Entra application access using Microsoft Graph app role assignments.

App role assignments represent access to applications and application-defined roles. IdentityOS can use this model to connect policy decisions, access requests, role packages, governance controls, access drift detection, and audit evidence to application access.

---

## Objective

The objective of the app role assignment model is to answer:

> Which identities have application access, why do they have it, who approved it, and should that access still exist?

---

## Conceptual Model

```text id="ec7m2w"
IdentityOS Policy Decision
        ↓
Application Access Requirement
        ↓
App Role Assignment Mapping
        ↓
Microsoft Graph App Role Assignment
        ↓
Microsoft Entra Enterprise Application
        ↓
Application Access
        ↓
Governance Evidence
```

---

## App Role Assignment Components

An app role assignment includes three core parts.

| Component            | Purpose                                                                     |
| -------------------- | --------------------------------------------------------------------------- |
| Principal            | The identity receiving access, such as a user, group, or service principal. |
| Resource Application | The enterprise application or service principal that exposes the app role.  |
| App Role             | The specific application role being assigned.                               |

---

## IdentityOS App Access Model

IdentityOS should model application access as a governed decision.

| IdentityOS Concept          | Microsoft Entra / Graph Concept                   |
| --------------------------- | ------------------------------------------------- |
| Application Access Decision | App role assignment.                              |
| Identity                    | User, group, or service principal.                |
| Application                 | Enterprise application or service principal.      |
| Role                        | App role exposed by the application.              |
| Approval Requirement        | Governance or app owner approval.                 |
| Risk Level                  | IdentityOS risk score.                            |
| Drift Status                | Expected access vs actual app role assignment.    |
| Audit Evidence              | Assignment, approval, review, and removal record. |

---

## Assignment Types

IdentityOS may support several app role assignment patterns.

| Assignment Type              | Description                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------- |
| Direct User Assignment       | App role is assigned directly to a user.                                        |
| Group-Based Assignment       | App role is assigned to a group, and users inherit access through membership.   |
| Service Principal Assignment | App role is assigned to an application or workload identity.                    |
| Temporary Assignment         | App access is granted for a limited duration.                                   |
| Exception Assignment         | Access is outside the standard role package and requires governance.            |
| Privileged Assignment        | Access provides elevated application capability and requires security approval. |

---

## Preferred Assignment Strategy

Where possible, IdentityOS should prefer group-based application access.

```text id="7vgiju"
User
  ↓
Security Group
  ↓
App Role Assignment
  ↓
Application Access
```

This makes access easier to manage, review, remove, and audit.

Direct user assignments should be used carefully because they can be harder to govern at scale.

---

## App Role Assignment Flow

```text id="sr00l4"
IdentityOS receives lifecycle or access event
        ↓
Policy Engine determines application access need
        ↓
Risk and governance checks are applied
        ↓
Application owner approval is evaluated
        ↓
App role assignment is mapped
        ↓
Microsoft Graph action is prepared
        ↓
App role assignment is created or removed
        ↓
Evidence is generated
```

---

## Joiner App Assignment

A Joiner event may require application access.

| Joiner Scenario                                         | App Role Action                                  | Governance Requirement           |
| ------------------------------------------------------- | ------------------------------------------------ | -------------------------------- |
| New employee receives baseline app access               | Assign standard app role through baseline group. | Standard evidence.               |
| Finance analyst needs finance application               | Assign finance application role.                 | App owner approval if sensitive. |
| Legal operations analyst needs document system access   | Assign legal application role.                   | Legal owner review.              |
| Security analyst needs read-only security portal access | Assign security reader role.                     | Security approval.               |
| Contractor needs project app access                     | Assign temporary app role or group-based access. | Sponsor approval and expiration. |

---

## Mover App Assignment

A Mover event may require app access to change.

| Mover Scenario                              | App Role Action                                           | Governance Requirement                |
| ------------------------------------------- | --------------------------------------------------------- | ------------------------------------- |
| Finance to Legal                            | Remove finance app role, assign legal app role.           | Drift evidence required.              |
| Employee changes manager but role unchanged | Retain app role.                                          | Record retained access justification. |
| Employee moves into security role           | Assign security app role.                                 | Security approval required.           |
| Contractor changes project                  | Remove old project app role, assign new project app role. | Sponsor approval required.            |
| User retains previous app access            | Flag as access drift.                                     | Review or remove access.              |

---

## Leaver App Assignment

A Leaver event should remove application access.

| Leaver Scenario             | App Role Action                                                | Governance Requirement            |
| --------------------------- | -------------------------------------------------------------- | --------------------------------- |
| Employee termination        | Remove all direct user app role assignments.                   | Offboarding evidence required.    |
| Contractor end date reached | Remove temporary app role assignment.                          | Sponsor evidence required.        |
| Vendor contract ended       | Remove vendor application role.                                | Vendor closure evidence required. |
| Privileged leaver           | Remove privileged application roles first.                     | Security escalation required.     |
| Service account retirement  | Remove service principal app assignments after owner approval. | NHI evidence required.            |

---

## Non-Human Identity App Assignments

Non-human identities can also receive app role assignments.

| Identity Type        | Governance Requirement                                                   |
| -------------------- | ------------------------------------------------------------------------ |
| Service Account      | Owner, purpose, scope, credential review, and access review.             |
| App Registration     | Application owner, permission review, and credential lifecycle.          |
| Workload Identity    | Workload owner, environment, scope, and least-privilege review.          |
| Automation Identity  | Technical owner, script purpose, and access justification.               |
| Integration Identity | System owner, integration purpose, and access expiration where possible. |

---

## App Role Assignment Mapping Record

Each app role assignment should have a mapping record.

| Field            | Purpose                                             |
| ---------------- | --------------------------------------------------- |
| Assignment ID    | Unique assignment reference.                        |
| Principal ID     | User, group, or service principal receiving access. |
| Principal Type   | User, group, or service principal.                  |
| Resource ID      | Application or service principal exposing the role. |
| App Role ID      | Specific role being assigned.                       |
| Application Name | Human-readable application name.                    |
| Role Name        | Human-readable role name.                           |
| Access Reason    | Business reason for assignment.                     |
| Approval Owner   | Person or team approving access.                    |
| Risk Level       | IdentityOS risk score.                              |
| Expiration       | Access expiration if applicable.                    |
| Review Frequency | Access review cadence.                              |
| Evidence Link    | Related audit evidence.                             |

---

## Example Assignment Record

```text id="w4urti"
Assignment ID: APPROLE-001
Principal: Morgan Lee
Principal Type: User
Application: Financial Reporting Portal
Role: Finance Analyst
Access Reason: Required for Finance Analyst role
Approval Owner: Finance Application Owner
Risk Level: Medium
Expiration: None for employee
Review Frequency: Quarterly
Audit Required: Yes
Status: Approved and assigned
```

---

## App Role Assignment Risk Factors

App role assignments should influence IdentityOS risk scoring.

| Risk Factor                     | Impact                                  |
| ------------------------------- | --------------------------------------- |
| Sensitive application access    | Increases risk.                         |
| Privileged application role     | High or critical risk.                  |
| Direct user assignment          | May increase governance complexity.     |
| External identity assignment    | Requires sponsor and expiration review. |
| Service principal assignment    | Requires non-human identity governance. |
| Missing approval                | High governance risk.                   |
| Missing owner                   | High operational risk.                  |
| Expired assignment still active | Critical access drift.                  |

---

## App Role Assignment Drift

IdentityOS should detect app role assignment drift.

| Drift Condition                                               | Meaning                   |
| ------------------------------------------------------------- | ------------------------- |
| User has app role outside expected role package               | Role drift.               |
| User retains app role from previous department                | Department drift.         |
| Contractor app role remains after expiration                  | Contractor drift.         |
| Vendor app role lacks sponsor                                 | Sponsor drift.            |
| Service principal app role lacks owner                        | Non-human identity drift. |
| Privileged app role not reviewed                              | Privilege drift.          |
| Direct assignment exists where group-based access is expected | Governance drift.         |

---

## Approval Requirements

| App Access Type              | Approval Requirement                    |
| ---------------------------- | --------------------------------------- |
| Standard business app access | Manager or policy-based approval.       |
| Sensitive app access         | Application owner approval.             |
| Financial system access      | Finance owner or governance approval.   |
| Legal document access        | Legal owner approval.                   |
| Security portal access       | Security approval.                      |
| Privileged app role          | Privileged access owner approval.       |
| Contractor app access        | Sponsor approval and expiration.        |
| Vendor app access            | Sponsor and application owner approval. |
| Service principal app role   | Technical owner and security review.    |

---

## Suggested Graph Permissions

| Permission                        | Purpose                                              |
| --------------------------------- | ---------------------------------------------------- |
| `Application.Read.All`            | Read application and service principal metadata.     |
| `AppRoleAssignment.Read.All`      | Read app role assignments.                           |
| `AppRoleAssignment.ReadWrite.All` | Create or remove app role assignments when approved. |
| `Directory.Read.All`              | Read directory context where required.               |
| `AuditLog.Read.All`               | Read activity and audit evidence where required.     |

---

## Safety Controls

App role assignment automation should include safety controls.

| Control                        | Purpose                                                |
| ------------------------------ | ------------------------------------------------------ |
| Application Mapping Validation | Confirms the correct app and role are selected.        |
| Approval Enforcement           | Prevents sensitive app access without approval.        |
| Least Privilege                | Assigns only the required app role.                    |
| Prefer Group-Based Access      | Reduces direct assignment sprawl.                      |
| Expiration Tracking            | Prevents temporary app access from becoming permanent. |
| Owner Validation               | Confirms application owner accountability.             |
| Drift Detection                | Detects app access outside expected role.              |
| Evidence Generation            | Records assignment and removal history.                |

---

## Failure Handling

| Failure                   | Response                                        |
| ------------------------- | ----------------------------------------------- |
| Application not found     | Stop assignment and log missing resource.       |
| App role not found        | Stop assignment and escalate to app owner.      |
| Principal not found       | Stop assignment and validate identity.          |
| Approval missing          | Stage assignment until approval.                |
| Permission denied         | Log Graph permission issue and escalate.        |
| Assignment already exists | Record as existing access and evaluate drift.   |
| Assignment removal fails  | Create remediation task.                        |
| Partial failure           | Record completed and failed actions separately. |

---

## Evidence Requirements

Each app role assignment should generate evidence.

| Evidence Item     | Purpose                                           |
| ----------------- | ------------------------------------------------- |
| Identity          | Shows who received or lost app access.            |
| Application       | Shows which application was involved.             |
| App Role          | Shows what role was assigned or removed.          |
| Assignment Method | Direct user, group-based, or service principal.   |
| Approval          | Shows who approved access.                        |
| Risk Level        | Shows IdentityOS risk score.                      |
| Drift Status      | Shows whether assignment matches expected access. |
| Expiration        | Shows whether access is time-bound.               |
| Timestamp         | Shows when assignment or removal occurred.        |
| Audit Status      | Shows whether evidence was retained.              |

---

## Dashboard Impact

App role assignments should support dashboard visibility.

| Dashboard                       | Impact                                          |
| ------------------------------- | ----------------------------------------------- |
| Executive Dashboard             | Shows sensitive and privileged app access risk. |
| IAM Operations Dashboard        | Shows app access assignments and removals.      |
| Governance Dashboard            | Shows approvals and review requirements.        |
| Risk Dashboard                  | Uses app access as a risk signal.               |
| Access Drift Dashboard          | Detects unexpected app role assignments.        |
| Contractor and Vendor Dashboard | Tracks external app access.                     |
| Non-Human Identity Dashboard    | Tracks service principal app roles.             |
| Audit Evidence Dashboard        | Shows app access evidence.                      |

---

## Summary

The App Role Assignment Model connects IdentityOS policy decisions to Microsoft Entra application access.

The key architectural idea is:

> Application access should be assigned intentionally, approved when sensitive, reviewed regularly, removed when no longer needed, and evidenced for audit.
